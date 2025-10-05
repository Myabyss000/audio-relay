# 🎵 How to Capture System Audio (VLC, Media Players, etc.)

**🎯 GOAL:** Make your phone a wireless speaker for laptop audio (music, videos, games, etc.)

**⚡ QUICK START** (Pick your OS):

<details>
<summary><b>🪟 WINDOWS - Click here for 2-minute setup</b></summary>

### Option A: Stereo Mix (If available - try this first!)
1. Right-click speaker icon → "Sound settings"
2. Click "Sound Control Panel" 
3. "Recording" tab → Right-click empty space → "Show Disabled Devices"
4. If you see **"Stereo Mix"**: Right-click → Enable → Set as Default
5. Done! Run `python server.py` - it will now stream system audio!

### Option B: VB-CABLE (If Stereo Mix not available)
1. Download: https://vb-audio.com/Cable/
2. Extract ZIP → Right-click `VBCABLE_Setup_x64.exe` → "Run as administrator"
3. Install → Restart computer
4. Sound settings → Output: "CABLE Input" | Input: "CABLE Output"  
5. Done! Run `python server.py`

**To hear on laptop too:** Recording tab → CABLE Output → Properties → Listen tab → Check "Listen to this device" → Select your speakers

</details>

<details>
<summary><b>🍎 macOS - Click here for 2-minute setup</b></summary>

1. Install BlackHole: `brew install blackhole-2ch`
2. Open "Audio MIDI Setup" (Spotlight search)
3. Click "+" → "Create Multi-Output Device"
4. Check: BlackHole 2ch + Built-in speakers
5. System Preferences → Sound → Output: Multi-Output | Input: BlackHole
6. Done! Run `python server.py`

</details>

<details>
<summary><b>🐧 LINUX - Click here for 1-minute setup</b></summary>

```bash
# Enable loopback
pactl load-module module-loopback latency_msec=1

# Run server
python server.py

# To disable later
pactl unload-module module-loopback
```

</details>

---

## 📖 Detailed Instructions Below

By default, the audio relay captures your **microphone**. To stream audio from VLC, YouTube, Spotify, or any media player, you need to set up **audio loopback**.

---

## 🪟 Windows Setup (Recommended Method)

### Option 1: Using Stereo Mix (Built-in, if available)

1. **Right-click the speaker icon** in the taskbar
2. Select **"Sound settings"**
3. Scroll down and click **"Sound Control Panel"** (or "More sound settings")
4. Go to the **"Recording"** tab
5. Right-click in the empty space and enable **"Show Disabled Devices"**
6. You should see **"Stereo Mix"** appear
7. **Right-click "Stereo Mix"** → **"Enable"**
8. **Right-click "Stereo Mix"** again → **"Set as Default Device"**
9. Click **"OK"**
10. **Run your server** - it will now capture system audio!

**Note**: Not all sound cards support Stereo Mix. If you don't see it, use Option 2.

---

### Option 2: Using VB-CABLE (Virtual Audio Cable)

This is the most reliable method and works on all Windows systems.

#### Step 1: Download and Install VB-CABLE

1. Go to: https://vb-audio.com/Cable/
2. Download **VB-CABLE Virtual Audio Device**
3. Extract the ZIP file
4. **Right-click `VBCABLE_Setup_x64.exe`** → **"Run as administrator"**
5. Click **"Install Driver"**
6. Restart your computer (important!)

#### Step 2: Configure Audio Settings

1. **Right-click speaker icon** → **"Sound settings"**
2. Under **"Output"**, select **"CABLE Input (VB-Audio Virtual Cable)"**
3. Under **"Input"**, select **"CABLE Output (VB-Audio Virtual Cable)"**

#### Step 3: Hear Audio on Your Laptop Too (Optional)

If you also want to hear the audio on your laptop speakers:

1. Open **Sound Control Panel** (search "Sound" in Windows)
2. Go to **"Recording"** tab
3. Find **"CABLE Output"**
4. **Right-click** → **"Properties"**
5. Go to **"Listen"** tab
6. Check **"Listen to this device"**
7. Select your **actual speakers/headphones** from the dropdown
8. Click **"OK"**

#### Step 4: Run the Server

```powershell
python server.py
```

Now play anything (VLC, Spotify, YouTube) and it will stream to your phone!

---

## 🍎 macOS Setup

### Using BlackHole (Free Virtual Audio Driver)

#### Step 1: Install BlackHole

```bash
brew install blackhole-2ch
```

Or download from: https://existential.audio/blackhole/

#### Step 2: Create Multi-Output Device

1. Open **"Audio MIDI Setup"** (search in Spotlight)
2. Click the **"+"** button at the bottom left
3. Select **"Create Multi-Output Device"**
4. Check both:
   - **BlackHole 2ch**
   - **Your built-in speakers** (to hear audio on Mac too)
5. Set this Multi-Output as your **default output** in System Preferences

#### Step 3: Set BlackHole as Input

1. In System Preferences → Sound → Input
2. Select **"BlackHole 2ch"**

#### Step 4: Run the Server

```bash
python server.py
```

---

## 🐧 Linux Setup

### Using PulseAudio Loopback

#### Quick Method:

```bash
# Load the loopback module
pactl load-module module-loopback latency_msec=1

# To unload later
pactl unload-module module-loopback
```

#### Permanent Setup:

1. Edit PulseAudio config:
   ```bash
   sudo nano /etc/pulse/default.pa
   ```

2. Add this line at the end:
   ```
   load-module module-loopback latency_msec=1
   ```

3. Restart PulseAudio:
   ```bash
   pulseaudio --kill
   pulseaudio --start
   ```

#### Run the Server:

```bash
python server.py
```

---

## 🔧 Troubleshooting

### "No sound" or "Microphone audio instead of system audio"

- **Windows**: Make sure VB-CABLE is set as BOTH input AND output
- **Mac**: Verify BlackHole is selected as input
- **Linux**: Check that loopback module is loaded: `pactl list modules | grep loopback`

### Audio plays on laptop but not phone

- Check that the server is running
- Verify phone is connected (check terminal for "Client connected")
- Tap the screen on your phone once

### Audio is choppy or has gaps

- Close unnecessary applications
- Try increasing CHUNK size in `server.py`:
  ```python
  CHUNK = 2048  # or 4096
  ```

### Want to switch back to normal audio?

**Windows:**
1. Sound settings → Set your normal speakers as default output
2. Set your normal microphone as default input

**Mac:**
1. System Preferences → Sound → Output → Select built-in speakers
2. Input → Select built-in microphone

**Linux:**
```bash
pactl unload-module module-loopback
```

---

## ✅ Testing

1. **Set up audio loopback** (using one of the methods above)
2. **Run the server**: `python server.py`
3. **Connect your phone** to the URL shown
4. **Play a video/music** on your laptop
5. **You should hear it on your phone!**

---

## 📝 Device Selection (Advanced)

If you have multiple audio devices and want to select a specific one:

1. Run the server - it will list all available devices:
   ```
   === Available Audio Devices ===
   Device 0: Microphone
   Device 1: CABLE Output (VB-Audio)
   Device 2: Stereo Mix
   ```

2. Edit `server.py` and specify the device:
   ```python
   stream = audio.open(
       format=FORMAT,
       channels=CHANNELS,
       rate=RATE,
       input=True,
       frames_per_buffer=CHUNK,
       input_device_index=1  # Change this number
   )
   ```

---

**You're all set! Now you can stream any audio from your laptop to your phone! 🎉**
