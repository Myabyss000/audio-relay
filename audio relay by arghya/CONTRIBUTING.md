# Contributing to Audio Relay

First off, thank you for considering contributing to Audio Relay! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment details**: OS, Python version, browser
- **Error logs** if available

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear description** of the proposed feature
- **Use case** - why would this be useful?
- **Possible implementation** (if you have ideas)

### Pull Requests

1. **Fork the repo** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style (simple, readable, commented)
   - Keep it minimal and functional
   - Test your changes thoroughly

3. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of what you added"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Describe what changes you made
   - Reference any related issues
   - Include testing details

## Code Style

- Keep code **simple and readable**
- Add **inline comments** for clarity
- Use **meaningful variable names**
- Follow **PEP 8** for Python code
- Keep functions **small and focused**

## What to Contribute?

### Good First Issues

- Improve error handling
- Add more audio format options
- Better connection status indicators
- Documentation improvements
- Cross-platform testing

### Feature Ideas

- Support for stereo audio
- Audio quality selection
- Multiple client support
- Connection authentication
- System audio capture guide
- Volume control on client side

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/audio-relay.git
cd audio-relay

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

## Testing

- Test on multiple devices (different phones, tablets)
- Test on different browsers (Chrome, Safari, Firefox)
- Test network conditions (different Wi-Fi networks)
- Verify no errors in browser console

## Questions?

Feel free to open an issue with the `question` label if you need help or clarification.

---

**Thank you for contributing! 🙌**
