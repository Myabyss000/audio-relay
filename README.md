# 🎵 Audio Relay - Wireless Speaker System

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Turn your phone into a wireless speaker!** Stream audio from your laptop (VLC, Spotify, YouTube, any media player) to your phone over local Wi-Fi. No apps, no Bluetooth pairing, just a browser.

> **🎯 Main Purpose:** Stream system audio (music, videos, media players) from laptop to phone as a wireless speaker
> 
> **📢 To stream from VLC/Spotify/YouTube:** See [SYSTEM_AUDIO_GUIDE.md](SYSTEM_AUDIO_GUIDE.md) for quick setup!

## ✨ Features

- � **Wireless Speaker** - Turn any phone/tablet into a speaker for your laptop
- 📱 **Browser-Based** - No app installation required
- 🎵 **Stream Any Audio** - VLC, Spotify, YouTube, games, system sounds
- ⚡ **Real-Time** - Low-latency audio transmission
- 🔒 **Local Network Only** - Private and secure
- 💻 **Cross-Platform** - Works on Windows, Linux, and macOS
- 🎯 **Lightweight** - Minimal resources, pure Python

## 🎯 Use Cases

- **Wireless speaker** - Place phone anywhere, play laptop audio remotely
- **Stream music** - VLC, Spotify, YouTube to phone speakers
- **Gaming audio** - Play game sounds through phone
- **Video playback** - Watch videos on laptop, hear on phone
- **Multi-room audio** - Connect multiple phones for distributed sound
- **Test audio** - Quick A/B testing across devices

## 📋 How It Works

- **Server**: Captures laptop's system audio (music, videos, media players)
- **Client**: Phone browser receives and plays audio in real-time  
- **Protocol**: WebSocket-based streaming (Socket.IO)
- **Setup Required**: Enable audio loopback to capture system audio (see guide below)

---

## 🚀 Quick Start Guide

### For First-Time Users (Complete Setup - 5 minutes)

#### Step 1: Download the Project
```bash
git clone https://github.com/YOUR_USERNAME/audio-relay.git
cd audio-relay
```

Or download as ZIP and extract it.

#### Step 2: Install Python Dependencies
```powershell
pip install -r requirements.txt
```

> **Windows Users**: If PyAudio fails, use:
> ```powershell
> pip install pipwin
> pipwin install pyaudio
> ```

#### Step 3: **IMPORTANT** - Enable System Audio Capture

**This is required to stream from VLC, Spotify, YouTube, etc.**

Choose your OS:

**🪟 Windows (Quick)**
- Right-click speaker icon → Sound settings → Sound Control Panel
- Recording tab → Right-click empty space → "Show Disabled Devices"
- If "Stereo Mix" appears → Enable it → Set as Default
- If NOT available → Install VB-CABLE: https://vb-audio.com/Cable/

**🍎 macOS (Quick)**
```bash
brew install blackhole-2ch
# Then: Audio MIDI Setup → Create Multi-Output Device
```

**🐧 Linux (Quick)**
```bash
pactl load-module module-loopback latency_msec=1
```

📖 **Detailed instructions:** [SYSTEM_AUDIO_GUIDE.md](SYSTEM_AUDIO_GUIDE.md)

#### Step 4: Find Your Laptop's IP Address
Open PowerShell/Terminal and run:

**Windows:**
```powershell
ipconfig
```

**Mac/Linux:**
```bash
ifconfig
```

Look for your **IPv4 Address** (e.g., `192.168.1.100`)

#### Step 5: Start the Server
```powershell
python server.py
```

You'll see:
```
=== Audio Relay Server ===
Starting server...
Access from your phone at: http://<YOUR_LAPTOP_IP>:5000
Press Ctrl+C to stop
```

The server will automatically detect and use your system audio device!

#### Step 6: Connect from Your Phone
1. **Ensure phone and laptop are on the same Wi-Fi network**
2. Open any browser on your phone (Chrome, Safari, Firefox)
3. Enter the URL: `http://192.168.1.100:5000` *(use your actual laptop IP)*
4. You'll see a green screen with "AUDIO RELAY"
5. Tap the screen once if audio doesn't start immediately
6. **Play music/video on your laptop** - it streams to your phone!
7. **Done!** Your phone is now a wireless speaker! 🎉

---

## 📖 Detailed Usage

### Wireless Speaker Mode (Main Use)

**Goal:** Stream music, videos, games from laptop to phone as a wireless speaker.

**Prerequisites:** System audio capture enabled (Step 3 in Quick Start)

```powershell
python server.py
```

- Play **any audio** on your laptop (VLC, YouTube, Spotify, games)
- Audio automatically streams to your connected phone
- Phone acts as a wireless speaker
- Perfect for placing phone in another room or location

### Alternative: Microphone Mode

If you want to stream microphone instead (announcements, voice, etc.):

- **Don't** set up audio loopback  
- Just use default microphone
- Run `python server.py`
- Speak into laptop mic → plays on phone

### Multiple Devices

You can connect multiple phones/tablets simultaneously:
- All connected devices receive the same audio
- Each device can control its own volume
- Just open the URL on each device

### Using on Different Networks

**Local Network Only (Default):**
- Both devices must be on same Wi-Fi
- Most secure option

**Access from Different Network:**
- Not recommended (security risk)
- Would require port forwarding on router
- Consider VPN instead

---

## 💡 Common Use Cases

### 1. **Wireless Speaker**
Turn your old phone into a wireless speaker:
- Place phone anywhere in the room
- Stream music from laptop
- No Bluetooth pairing needed

### 2. **Room Announcements**
Broadcast announcements to multiple devices:
- Connect several phones/tablets
- Speak into laptop mic
- All devices play simultaneously

### 3. **Audio Testing**
Test how audio sounds on different devices:
- Quick A/B testing
- No file transfer needed
- Real-time feedback

### 4. **Remote Audio Monitoring**
Monitor audio from another room:
- Server in one room
- Phone in another
- Hear what's happening remotely

---

## Setup

> **Note**: If you followed the Quick Start Guide above, you can skip this section.

### Installation Steps

#### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

**Note for Windows users**: PyAudio installation might fail. If it does, install it using:
```powershell
pip install pipwin
pipwin install pyaudio
```

Or download the `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually.

#### 2. Find Your Laptop's Local IP

Open PowerShell and run:
```powershell
ipconfig
```

Look for `IPv4 Address` under your active network adapter (usually starts with `192.168.x.x` or `10.0.x.x`).

Example: `192.168.1.100`

#### 3. Run the Server

```powershell
python server.py
```

You'll see output like:
```
=== Audio Relay Server ===
Starting server...
Access from your phone at: http://<YOUR_LAPTOP_IP>:5000
Press Ctrl+C to stop
```

#### 4. Connect Your Phone

1. Make sure your phone and laptop are on the **same Wi-Fi network**
2. Open any browser on your phone (Chrome, Safari, etc.)
3. Go to: `http://192.168.1.100:5000` (replace with your actual laptop IP)
4. You should see "AUDIO RELAY" page with status "Connected - Playing Audio"
5. Audio from your laptop microphone will now play through your phone

---

## 🛠️ Troubleshooting

**No sound on phone?**
- Tap the screen once (browsers require user interaction to play audio)
- Check phone volume

**Can't connect?**
- Verify both devices are on same Wi-Fi
- Check Windows Firewall (allow Python/port 5000)
- Try disabling firewall temporarily to test

**Want to stream system audio instead of microphone?**
- You'll need a virtual audio cable (e.g., VB-Audio Virtual Cable)
- Set it as default playback device
- Set it as default recording device in PyAudio

**Audio quality is poor?**
- Check your Wi-Fi signal strength
- Try moving closer to the router
- Close other bandwidth-heavy applications
- Reduce network congestion

**Latency/delay issues?**
- Normal latency is 100-300ms
- Ensure strong Wi-Fi connection
- Close unnecessary apps on both devices
- Try using 5GHz Wi-Fi instead of 2.4GHz

**PyAudio installation fails?**
- Windows: Use `pipwin` as shown above
- Mac: Try `brew install portaudio` then `pip install pyaudio`
- Linux: `sudo apt-get install portaudio19-dev python3-pyaudio`

**More issues?**
📋 See the complete **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** guide for a comprehensive checklist.

---

## ⚙️ Technical Details

- **Audio Format**: 16-bit PCM, 44.1kHz, Stereo
- **Buffer Size**: 1024 frames (~23ms latency)
- **Protocol**: WebSocket (Socket.IO) for real-time streaming
- **No recording**: Audio is only transmitted, not saved

---

## 🎬 Demo & Screenshots

### Server Running
```
=== Audio Relay Server ===
Starting server...
Access from your phone at: http://192.168.1.100:5000
Press Ctrl+C to stop

Client connected
```

### Phone Interface
A minimalistic green-on-black terminal-style interface showing:
- **AUDIO RELAY** header
- Connection status
- Simple instructions

---

## ❓ FAQ

**Q: Does this work on public Wi-Fi?**  
A: Yes, but both devices must be on the same network. Some public networks isolate devices for security.

**Q: Can I use this over the internet?**  
A: Not recommended. It's designed for local networks only. For internet use, you'd need VPN or port forwarding (security risk).

**Q: How many devices can connect?**  
A: Multiple devices can connect simultaneously. All receive the same audio stream.

**Q: Does it work on iPhone/Android?**  
A: Yes! It works on any device with a modern web browser (Chrome, Safari, Firefox, etc.).

**Q: Can I adjust audio quality?**  
A: Yes, modify the `RATE` and `CHUNK` values in `server.py`. Higher values = better quality but more latency.

**Q: Is the audio encrypted?**  
A: No. It's transmitted over local network without encryption. Don't use for sensitive audio.

**Q: Can I stream to speakers instead of phone?**  
A: Yes! Open the URL on any device - laptop, tablet, smart TV browser, etc.

---

## Stop the Server

Press `Ctrl+C` in the terminal where server is running.

---

## 📁 Project Structure

```
audio-relay/
├── server.py              # Flask-SocketIO server
├── templates/
│   └── index.html        # Browser client interface
├── requirements.txt      # Python dependencies
├── README.md            # Main documentation
├── SYSTEM_AUDIO_GUIDE.md # How to stream from VLC/media players
├── QUICK_REFERENCE.md   # Quick command reference
├── CONTRIBUTING.md      # Contribution guidelines
├── SETUP_GITHUB.md      # GitHub setup guide
├── LICENSE              # MIT License
└── .gitignore          # Git ignore rules
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Known Limitations

- Streams microphone input by default (not system audio)
- For system audio streaming, requires virtual audio cable setup
- Browser autoplay policies may require user interaction
- Latency depends on network quality (~100-300ms typical)

## 🙏 Acknowledgments

- Built with Flask and Flask-SocketIO
- Uses PyAudio for audio capture
- Web Audio API for browser playback

## 📧 Support

If you encounter issues, please open an issue on GitHub with:
- Your OS and Python version
- Error messages or logs
- Steps to reproduce the problem

---

**Made with ❤️ by Arghya**

