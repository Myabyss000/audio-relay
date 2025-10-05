# ✅ Troubleshooting Checklist

Use this checklist to diagnose and fix common issues.

---

## 🔴 Server Won't Start

**Error: `ModuleNotFoundError: No module named 'flask'`**
- [ ] Run: `pip install -r requirements.txt`

**Error: `ModuleNotFoundError: No module named 'pyaudio'`**
- [ ] Windows: `pip install pipwin` then `pipwin install pyaudio`
- [ ] Mac: `brew install portaudio` then `pip install pyaudio`
- [ ] Linux: `sudo apt-get install portaudio19-dev python3-pyaudio`

**Error: Port 5000 already in use**
- [ ] Check if another app is using port 5000
- [ ] Change port in `server.py`: `socketio.run(app, host='0.0.0.0', port=5001)`

---

## 🔴 Can't Connect from Phone

**Browser shows "Can't reach this page" or "Connection refused"**
- [ ] Both devices on same Wi-Fi network? Check Wi-Fi name on both
- [ ] Using correct IP address? Check server output for IP
- [ ] Windows Firewall blocking? Try: Control Panel → Windows Defender Firewall → Allow an app
- [ ] Router has device isolation? Try hotspot from laptop instead

**Quick test:**
- [ ] Can you access `http://127.0.0.1:5000` on the laptop browser?
  - ✅ Yes = Server working, firewall/network issue
  - ❌ No = Server not running properly

---

## 🔴 No Sound on Phone

**Page loads but no audio plays**
- [ ] Did you tap/click the screen? (Browsers require user interaction)
- [ ] Phone volume turned up?
- [ ] Phone not on silent/vibrate mode?
- [ ] Check browser console for errors (Chrome: Menu → More tools → Developer tools)

**Browser console shows errors**
- [ ] Try refreshing the page
- [ ] Try different browser (Chrome, Firefox, Safari)
- [ ] Clear browser cache

---

## 🔴 Hearing Microphone Instead of VLC/Media

**Audio works but capturing wrong source**
- [ ] Did you set up audio loopback? See SYSTEM_AUDIO_GUIDE.md
- [ ] **Windows**: Is VB-CABLE or Stereo Mix set as default INPUT?
- [ ] **Mac**: Is BlackHole selected as input in System Preferences?
- [ ] **Linux**: Is loopback module loaded? `pactl list modules | grep loopback`

**Verify device selection:**
- [ ] Look at server output when it starts - shows which device it's using
- [ ] If wrong device, see SYSTEM_AUDIO_GUIDE.md for device selection

---

## 🔴 Audio Quality Issues

**Choppy/stuttering audio**
- [ ] Close other network-heavy apps (downloads, streaming)
- [ ] Move closer to Wi-Fi router
- [ ] Try 5GHz Wi-Fi instead of 2.4GHz
- [ ] Increase CHUNK size in server.py: `CHUNK = 2048` or `4096`
- [ ] Close unnecessary apps on both devices

**Audio has gaps or breaks**
- [ ] Wi-Fi signal strength good on both devices?
- [ ] Other people using the same Wi-Fi?
- [ ] Try reducing video quality if streaming video

**Poor audio quality/sounds bad**
- [ ] Check if audio source quality is good
- [ ] Try changing RATE in server.py: `RATE = 48000`
- [ ] Make sure CHANNELS matches source (2 for stereo, 1 for mono)

---

## 🔴 High Latency/Delay

**Audio delayed by several seconds**
- [ ] Normal latency is 100-300ms (acceptable for most uses)
- [ ] Reduce CHUNK size: `CHUNK = 512`
- [ ] Use 5GHz Wi-Fi
- [ ] Ensure strong signal on both devices
- [ ] Disable other network devices/apps

**Note:** Some latency is unavoidable with wireless streaming.

---

## 🔴 Multiple Connection Issues

**Multiple phones not working**
- [ ] Each phone must browse to the IP separately
- [ ] Make sure all phones are on same Wi-Fi
- [ ] Try connecting one at a time to test

**Some phones work, others don't**
- [ ] Different browsers may behave differently
- [ ] Try Chrome if Safari doesn't work (or vice versa)
- [ ] Check if older phones have outdated browsers

---

## 🔴 After Windows Update / System Restart

**Was working, now doesn't**
- [ ] Audio device changed? Run server to see device list
- [ ] VB-CABLE still set as default? Check Sound settings
- [ ] Need to reload loopback module? (Linux)
- [ ] Virtual audio driver needs reinstalling? (rare)

---

## 🔍 Advanced Debugging

### Check Server Logs
Look at terminal where server is running:
- `Client connected` = Phone connected successfully
- Error messages show what went wrong

### Check Browser Console
On phone browser:
- Chrome: Menu → More tools → Developer tools → Console
- Safari: Settings → Advanced → Web Inspector

### Test Local Connection First
1. On laptop, open browser
2. Go to `http://127.0.0.1:5000`
3. If works locally but not on phone = network issue
4. If doesn't work locally = server/audio issue

### Verify Network Setup
```powershell
# Windows - Check your IP
ipconfig

# See if firewall is blocking
netsh advfirewall show allprofiles
```

---

## 📞 Still Having Issues?

If you've tried everything above:

1. **Check GitHub Issues**: Someone may have had the same problem
2. **Create New Issue**: Include:
   - Your OS and Python version
   - Full error message
   - Steps you've tried
   - Server terminal output
   - Browser console errors

---

## ✅ Quick Success Test

Run through this to verify everything works:

1. [ ] Server starts without errors
2. [ ] Shows IP address in terminal
3. [ ] Shows "Client connected" when you visit from laptop browser
4. [ ] Laptop browser plays audio (speak into mic)
5. [ ] Phone browser loads the page
6. [ ] Phone plays audio after tapping screen

If all ✅ = System working perfectly! 🎉

---

**Most issues are solved by:**
1. Checking Wi-Fi connection
2. Setting up audio loopback correctly (see SYSTEM_AUDIO_GUIDE.md)
3. Tapping the screen on phone
4. Allowing through firewall
