# 🎯 Audio Relay - Quick Reference Card

## 🚀 Start Server
```powershell
python server.py
```

## 📱 Connect Phone
```
http://YOUR_LAPTOP_IP:5000
```
Example: `http://192.168.29.196:5000`

---

## 🔊 Audio Source Selection

### Default: Microphone Audio
Just run the server - it captures microphone by default.

### Stream VLC/Media Players (System Audio)
See **[SYSTEM_AUDIO_GUIDE.md](SYSTEM_AUDIO_GUIDE.md)** for detailed setup.

**Quick Setup:**
- **Windows**: Enable "Stereo Mix" or install VB-CABLE
- **macOS**: Install BlackHole  
- **Linux**: `pactl load-module module-loopback`

---

## 🛠️ Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| No sound on phone | Tap screen once (browser autoplay policy) |
| Can't connect | Check both devices on same Wi-Fi |
| Firewall blocking | Allow Python on port 5000 |
| Hearing mic instead of media | Set up audio loopback (see guide) |
| Choppy audio | Increase CHUNK to 2048 in server.py |
| High latency | Use 5GHz Wi-Fi, close other apps |

---

## 📊 Server Configuration (in `server.py`)

```python
CHUNK = 1024        # Buffer size (1024-4096)
CHANNELS = 2        # 1=Mono, 2=Stereo
RATE = 44100        # Sample rate (22050, 44100, 48000)
```

**Higher values = Better quality but more latency**

---

## 🎬 Typical Workflow

1. **Set up audio loopback** (if streaming media players)
2. **Run server**: `python server.py`
3. **Note the IP** shown in terminal
4. **Open browser on phone**: `http://IP:5000`
5. **Tap screen** to start playback
6. **Play audio** on laptop - streams to phone!

---

## 💡 Pro Tips

✅ Use 5GHz Wi-Fi for better quality  
✅ Keep devices close to router  
✅ Close bandwidth-heavy apps  
✅ Multiple devices can connect simultaneously  
✅ Phone controls its own volume  
✅ Press Ctrl+C to stop server  

---

## 📁 Important Files

- `server.py` - Main server code
- `templates/index.html` - Client web interface
- `SYSTEM_AUDIO_GUIDE.md` - Media player setup guide
- `README.md` - Full documentation

---

**Need help? Check README.md or SYSTEM_AUDIO_GUIDE.md**
