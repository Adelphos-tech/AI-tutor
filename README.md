# ✦ AI Science Learning Platform

> **Two Premium Experiences - One Powerful Platform**

An advanced voice-based interactive learning system featuring two distinct designs:
- **✦ Nexus Scholar AI** (Premium Dark Theme) - Sophisticated, luxury learning experience
- **🌟 Amlak AI Science Teacher** (Classic White Theme) - Bright, friendly educational interface

Both versions offer the same powerful AI voice interaction technology with different visual aesthetics.

## 🎨 Choose Your Experience

### ✦ **Nexus Scholar AI** (Premium Dark - Recommended)
**File**: `nexus_premium.html` | **Default**: Yes

Premium luxury learning experience with sophisticated dark theme:
- 🌑 Deep navy background with gold/emerald accents
- ✦ Professional Poppins typography
- 💎 Glassmorphism effects and premium shadows
- 🎯 Executive-level aesthetic
- 👔 Perfect for: Serious learners, professionals, late-night study sessions

### 🌟 **Amlak AI Science Teacher** (Classic White)
**File**: `voice_white_theme.html`

Bright, friendly learning interface with classic design:
- ☀️ Clean white background with purple/pink accents
- 🎨 Inter typography
- 🌈 Cheerful, approachable design
- ✏️ Perfect for: Younger students, bright environments, casual learning

**📖 See detailed comparison:** [DESIGN_COMPARISON.md](DESIGN_COMPARISON.md)

## ✨ Core Features (Both Versions)

- **🎤 Voice Interaction**: Real-time voice communication with AI teacher
- **📚 20+ Topics**: Comprehensive coverage of plant life processes
- **🖼️ Visual Learning**: Dynamic images and illustrations
- **❓ Ask Questions**: Students can interrupt and ask questions anytime
- **🎨 Beautiful UI**: Two distinct themes to match your preference
- **⚡ Real-time Audio**: Low-latency audio streaming for natural conversation

## 🚀 Quick Start

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, or Edge)
- Microphone access
- Internet connection (connects to backend API)

### Running the Application

#### Option 1: Direct File Access
Simply open `voice_white_theme.html` in your web browser:
```bash
open voice_white_theme.html
```

#### Option 2: Local Server (Recommended)
Using Python's built-in server:
```bash
python3 -m http.server 8000
```
Then open `http://localhost:8000/voice_white_theme.html` in your browser.

#### Option 3: Using Node.js
```bash
npx serve .
```
Then follow the URL shown in the terminal.

## 📖 How to Use

1. **Connect**: Click the "🚀 Connect" button and allow microphone access
2. **Select Topic**: Choose a topic from the dropdown menu
3. **Learn**: Listen to the AI teacher explain the topic
4. **Ask Questions**: Click "🙋 Ask Question" to interrupt and ask anything
5. **Submit**: Click "📤 Submit Question" when you're done speaking

## 🎯 Topics Covered

- Introduction to Life Processes in Plants
- Plant Growth and Observation
- Growth Factors and Experiments
- Photosynthesis (The Food Factory)
- Stomata and Gas Exchange
- Transport in Plants
- Ancient Indian Plant Science (Vṛkṣāyurveda)
- And many more...

## 🔧 Technical Details

### Architecture
- **Frontend**: Single-page HTML5 application with vanilla JavaScript
- **Backend**: WebSocket connection to `wss://sciencetutorapi.apilproperties.com/teach_voice`
- **Audio**: 16kHz input, 24kHz playback with real-time streaming
- **Protocol**: Binary audio + JSON control messages

### Audio Pipeline
```
Microphone → AudioContext (16kHz) → WebSocket → Backend TTS → 
WebSocket → AudioContext (24kHz) → Speakers
```

### Browser Support
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support (may require HTTPS)
- Mobile: ⚠️ Limited (microphone API varies)

## 🛠️ Development

### File Structure
```
AI tutor/
├── nexus_premium.html         # Premium dark theme (default)
├── voice_white_theme.html     # Classic white theme
├── index.html                 # Landing page (redirects to premium)
├── README.md                  # This file (overview)
├── README_PREMIUM.md          # Premium version documentation
├── DESIGN_COMPARISON.md       # Detailed theme comparison
├── package.json               # Node.js configuration
├── start_server.py            # Python development server
├── start.sh                   # Universal launcher script
└── images/                    # Educational visuals (backend hosted)
    ├── image0.png
    ├── image1.png
    └── ... (20+ images)
```

### Customization

The application uses CSS custom properties for easy theming:
```css
:root {
    --bg-primary: #ffffff;
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* ... more variables ... */
}
```

## 🎨 Features Deep Dive

### Voice Recognition
- Continuous audio streaming
- Real-time speech detection
- Automatic silence detection
- Support for questions and interruptions

### Question Mode
1. Click "Ask Question" to interrupt the lesson
2. Audio stops instantly
3. Student speaks their question
4. Click "Submit Question" to process
5. AI answers specifically to the question
6. Lesson resumes automatically

### Visual Content
- Topic-specific images load automatically
- Gallery view for multiple images
- Fallback placeholders for missing content
- Responsive image sizing

## 🐛 Troubleshooting

### Microphone Not Working
- Check browser permissions (usually shows in address bar)
- Try refreshing the page
- Ensure no other app is using the microphone

### No Audio
- Check system volume and browser audio settings
- Some browsers require user interaction before playing audio
- Try clicking anywhere on the page first

### Connection Issues
- Check internet connection
- The backend server must be running
- WebSocket connection requires stable internet

### Audio Cutting Out
- Check network stability
- Close other bandwidth-intensive applications
- Try refreshing the connection

## 📝 License

This project is part of an educational initiative focused on interactive learning.

## 🤝 Contributing

This is an educational tool. For suggestions or improvements, please reach out to the development team.

## 📧 Support

For technical support or questions about the content, please contact the educational team.

---

**Made with ❤️ for interactive science education**
