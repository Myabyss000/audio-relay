# 🚀 Setting Up Your GitHub Repository

This guide will help you publish this project to GitHub.

## Prerequisites

- Git installed on your computer
- GitHub account created
- Project files ready (you have them!)

## Step 1: Initialize Git Repository

Open PowerShell in your project folder and run:

```powershell
cd "c:\Users\Arghya\OneDrive\Desktop\python projects\audio relay by arghya"
git init
git add .
git commit -m "Initial commit: Audio Relay v1.0"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name**: `audio-relay` (or your preferred name)
   - **Description**: `🎵 Stream audio from laptop to phone over local Wi-Fi`
   - **Visibility**: Public (or Private if you prefer)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click **"Create repository"**

## Step 3: Connect Local Repository to GitHub

GitHub will show you commands. Use these (replace with your actual repository URL):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/audio-relay.git
git branch -M main
git push -u origin main
```

## Step 4: Add Repository Details

On GitHub, edit your repository settings:

1. **About** (right side):
   - Add description
   - Add topics: `python`, `flask`, `audio-streaming`, `websocket`, `real-time`
   - Add website (if you have a demo)

2. **Repository Settings**:
   - Enable Issues (for bug reports)
   - Enable Discussions (optional, for community)

## Step 5: Create a Release (Optional)

1. Go to your repository
2. Click **"Releases"** → **"Create a new release"**
3. Tag version: `v1.0.0`
4. Release title: `Audio Relay v1.0.0`
5. Description: Brief overview of features
6. Click **"Publish release"**

## Step 6: Add Topics/Tags

Add these topics to make your repo discoverable:
- `python`
- `flask`
- `flask-socketio`
- `audio-streaming`
- `websocket`
- `real-time`
- `wireless-audio`
- `pyaudio`

## Future Updates

When you make changes:

```powershell
git add .
git commit -m "Description of changes"
git push
```

## Recommended Repository Settings

### Branch Protection (if working with others)
- Settings → Branches → Add rule for `main`
- Enable "Require pull request reviews before merging"

### Social Preview Image
- Settings → General → Social preview
- Upload a screenshot or logo (1280x640px recommended)

### GitHub Pages (Optional)
If you want to host documentation:
- Settings → Pages → Source: `main` branch → `/docs` folder

## Tips for Success

✅ Write clear commit messages
✅ Update README with screenshots/GIFs
✅ Respond to issues promptly
✅ Tag releases properly
✅ Keep documentation updated

## Promoting Your Project

- Share on Reddit (r/Python, r/programming)
- Tweet about it with hashtags
- Submit to Awesome Lists
- Write a blog post
- Share in Python Discord servers

---

**Your project is now ready for GitHub! 🎉**
