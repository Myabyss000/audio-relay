# 🔧 NO SOUND ON PHONE - DEBUG GUIDE

## Let's fix this step by step!

---

## ✅ STEP 1: Check Phone Connection

**On your phone browser (`http://192.168.29.196:5000`):**

1. What do you see on the screen?
   - [ ] Green screen with "AUDIO RELAY" text?
   - [ ] Error message?
   - [ ] Blank/white screen?

2. What's the status message?
   - [ ] "Connecting..."
   - [ ] "Connected - Playing Audio"
   - [ ] "Disconnected"

3. **DID YOU TAP THE SCREEN?** (VERY IMPORTANT!)
   - Browsers BLOCK audio until you tap/click
   - **Tap anywhere on the screen ONCE**
   - Status should change to "Connected - Playing Audio"

---

## ✅ STEP 2: Check Phone Settings

1. **Phone volume:**
   - [ ] Is phone volume turned UP?
   - [ ] Phone not on silent/vibrate mode?
   - [ ] Ringer and media volume both up?

2. **Browser:**
   - [ ] Using Chrome or Safari?
   - [ ] Try opening in **private/incognito mode**
   - [ ] Try a different browser if available

---

## ✅ STEP 3: Check Laptop Audio

**On your laptop:**

1. **Is audio ACTUALLY playing?**
   - Open YouTube
   - Play a video
   - [ ] Can you see sound bars in Windows volume mixer?
   - [ ] Is the video actually making sound (unmute laptop to check)?

2. **Check Windows Volume Mixer:**
   - Right-click speaker icon → "Open Volume Mixer"
   - [ ] Is VLC/Chrome/Media Player slider up?
   - [ ] Is it not muted?

---

## ✅ STEP 4: Verify Stereo Mix is Working

**Test if Stereo Mix is actually capturing audio:**

1. **Open Windows Sound Settings:**
   - Right-click speaker icon → "Sound settings"
   - Click "Sound Control Panel"
   - Go to "Recording" tab

2. **Play YouTube video on laptop**

3. **Look at Stereo Mix device:**
   - [ ] Do you see **GREEN BARS moving** next to Stereo Mix?
   - If YES → Stereo Mix is capturing audio ✅
   - If NO → Stereo Mix not capturing (see fix below)

**FIX if no green bars:**
   - Right-click Stereo Mix → Properties
   - Go to "Listen" tab
   - Make sure "Listen to this device" is UNCHECKED
   - Go to "Levels" tab
   - Make sure volume is at 100%
   - Click OK

---

## ✅ STEP 5: Check Browser Console (Advanced)

**On your phone browser:**

1. If using Chrome on Android:
   - Type in address bar: `chrome://inspect`
   - Or connect to laptop and use Chrome DevTools

2. Look for errors in console

3. Common errors:
   - "AudioContext was not allowed to start" → **TAP SCREEN!**
   - "Connection failed" → Check Wi-Fi
   - "Failed to decode audio" → Audio format issue

---

## 🧪 QUICK TEST - Do This Right Now:

### On Laptop:
```powershell
# Server should be running. Check terminal shows:
✓ Found system audio device: Stereo Mix (Realtek(R) Audio)
Client connected
```

1. **Unmute laptop speakers** (so you can verify audio is playing)
2. **Open YouTube** → Play: "Test Audio Left Right"
3. **You should HEAR it on laptop speakers**

### On Phone:
1. **Open browser:** `http://192.168.29.196:5000`
2. **You see green "AUDIO RELAY" screen?**
3. **TAP THE SCREEN ONCE** (very important!)
4. **Status changes to "Connected - Playing Audio"?**
5. **Wait 3-5 seconds**
6. **Do you hear the YouTube test audio?**

---

## 🔍 What's the Result?

**Tell me:**
- [ ] Phone shows "AUDIO RELAY" green screen? (Yes/No)
- [ ] You tapped the screen? (Yes/No)
- [ ] Status says "Connected - Playing Audio"? (Yes/No)
- [ ] Laptop is playing audio (you can hear it)? (Yes/No)
- [ ] Stereo Mix shows green bars in Recording tab? (Yes/No)
- [ ] Phone hears ANYTHING? (Yes/No)

---

## 🎯 Common Fixes:

### Problem: "Phone shows page but no audio"
**Solution:** TAP THE SCREEN ONCE! (Browsers block autoplay)

### Problem: "Stereo Mix not showing green bars"
**Solution:** 
- Stereo Mix volume at 100%
- Play audio on laptop
- Stereo Mix set as default recording device

### Problem: "Phone shows 'Disconnected'"
**Solution:**
- Check Wi-Fi (same network)
- Refresh page
- Restart server

### Problem: "Audio crackling/distorted"
**Solution:**
- Increase CHUNK size in server.py to 2048
- Use 5GHz Wi-Fi
- Close other apps

---

## 🔧 Emergency Reset:

If nothing works, try this complete reset:

```powershell
# 1. Stop server (Ctrl+C)

# 2. Verify Stereo Mix setup:
#    Sound Control Panel → Recording → Stereo Mix
#    - Enabled? ✓
#    - Default device? ✓
#    - Levels at 100%? ✓

# 3. Restart server
python server.py

# 4. On phone:
#    - Close browser completely
#    - Reopen browser
#    - Go to http://192.168.29.196:5000
#    - TAP SCREEN ONCE
#    - Play audio on laptop

# 5. Wait 5 seconds
```

---

## 📞 Tell Me Exactly What You See:

For each step, tell me Yes/No:

1. Phone browser shows green "AUDIO RELAY" screen?
2. You tapped the screen?
3. Status shows "Connected - Playing Audio"?
4. Laptop playing YouTube video right now?
5. You can hear YouTube on laptop speakers?
6. Stereo Mix showing green bars in Recording tab?
7. Phone making ANY sound at all?

**Answer these 7 questions and I'll tell you exactly what's wrong!** 🎯
