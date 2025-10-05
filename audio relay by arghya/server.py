from flask import Flask, render_template
from flask_socketio import SocketIO
import pyaudio
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'audio_relay_secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Audio configuration
CHUNK = 512            # Reduced buffer size for lower latency (was 1024)
FORMAT = pyaudio.paInt16  # 16-bit audio
CHANNELS = 2           # Stereo audio (change to 1 for mono)
RATE = 44100           # Sample rate (44.1 kHz)

# PyAudio instance
audio = pyaudio.PyAudio()
stream = None
is_streaming = False

def list_audio_devices():
    """List all available audio input devices"""
    print("\n=== Available Audio Devices ===")
    info = audio.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    for i in range(0, numdevices):
        device_info = audio.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            print(f"Device {i}: {device_info.get('name')}")
    print("=" * 35)
    return None

def get_default_input_device():
    """Get the default input device (usually captures system audio if loopback is set)"""
    try:
        # Try to get default input device
        default_device = audio.get_default_input_device_info()
        print(f"\nUsing input device: {default_device['name']}")
        return default_device['index']
    except:
        return None

def find_loopback_device():
    """Try to find a loopback/stereo mix device for system audio capture"""
    info = audio.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    # Priority list - devices that typically capture system audio
    priority_keywords = [
        'stereo mix',
        'wave out mix', 
        'loopback',
        'cable output',
        'vb-audio',
        'blackhole',
        'what u hear',
        'what you hear'
    ]
    
    # First pass - look for system audio capture devices
    for i in range(0, numdevices):
        try:
            device_info = audio.get_device_info_by_host_api_device_index(0, i)
            if device_info.get('maxInputChannels') > 0:
                device_name = device_info.get('name').lower()
                for keyword in priority_keywords:
                    if keyword in device_name:
                        print(f"\n✓ Found system audio device: {device_info.get('name')}")
                        return i
        except:
            continue
    
    # If no loopback device found, show warning
    print("\n⚠️  WARNING: No system audio capture device found!")
    print("   This will capture MICROPHONE audio instead of system audio.")
    print("   To stream from VLC/Spotify/media players:")
    print("   → See SYSTEM_AUDIO_GUIDE.md for setup instructions\n")
    return None

@app.route('/')
def index():
    """Serve the HTML page"""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """When client connects, start streaming audio"""
    global is_streaming, stream
    print(f"Client connected")
    
    if not is_streaming:
        is_streaming = True
        
        # List available devices for user reference
        list_audio_devices()
        
        # Try to find and use a loopback device for system audio
        device_index = find_loopback_device()
        if device_index is None:
            device_index = get_default_input_device()
        
        # Open audio stream
        try:
            stream = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=device_index
            )
            # Start streaming in a separate thread
            threading.Thread(target=stream_audio, daemon=True).start()
        except Exception as e:
            print(f"Error opening audio stream: {e}")
            print("Make sure you have an audio input device configured.")
            is_streaming = False

@socketio.on('disconnect')
def handle_disconnect():
    """When client disconnects, stop streaming"""
    global is_streaming, stream
    print("Client disconnected")
    is_streaming = False
    if stream:
        stream.stop_stream()
        stream.close()

def stream_audio():
    """Continuously read audio and send to connected clients"""
    global is_streaming
    while is_streaming:
        try:
            # Read audio data from input device
            audio_data = stream.read(CHUNK, exception_on_overflow=False)
            # Send binary audio data to all connected clients (removed 'broadcast' parameter)
            socketio.emit('audio_data', audio_data)
        except Exception as e:
            print(f"Error streaming audio: {e}")
            break

if __name__ == '__main__':
    print("\n=== Audio Relay Server ===")
    print("Starting server...")
    print("Access from your phone at: http://<YOUR_LAPTOP_IP>:5000")
    print("Press Ctrl+C to stop\n")
    
    # Run the server on all network interfaces
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
