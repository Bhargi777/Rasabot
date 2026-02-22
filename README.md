# RasaBot - Advanced Conversational AI Chatbot

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Rasa](https://img.shields.io/badge/Rasa-3.x-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A feature-rich conversational AI chatbot application built with **Rasa** and **Python**, featuring a modern graphical user interface using CustomTkinter. The application includes voice input, text-to-speech, emotion detection, sentiment analysis, and real-time interactions with a locally running Rasa server.

---

## 🚀 Features

### Core Capabilities
- **Rasa Integration**: Seamless connection to local Rasa NLU/Core server for intelligent conversations
- **Modern GUI**: Clean, intuitive interface built with CustomTkinter
- **Real-time Chat**: Instant message exchange with the chatbot
- **Conversation History**: Maintains context across chat sessions

### Audio Features
- **🎤 Voice Input**: Speech-to-text functionality using microphone input
- **🔊 Text-to-Speech**: Read bot responses aloud (toggleable in settings)
- **Audio Processing**: High-quality audio input/output handling

### Intelligence & Analysis
- **😊 Emotion Detection**: Analyzes user emotions and sentiment
- **📊 Sentiment Analysis**: Determines positive/negative/neutral sentiment
- **🔤 Word Cloud Generation**: Visual representation of conversation topics
- **📈 Chat Statistics**: Detailed analytics about conversations

### Personalization
- **🎨 Theme Customization**: Multiple color themes (blue, green, dark-blue)
- **🔤 Font Selection**: Various fonts with adjustable sizes
- **⚙️ Settings Panel**: Easy configuration of all features
- **💾 Preferences Save**: Remembers your customization choices

### Additional Features
- **🌐 Wikipedia Integration**: Quick access to information
- **🔍 Web Search**: Open search results from chat
- **🗣️ Translation Support**: Multi-language support
- **📱 Responsive Design**: Works on different screen sizes

---

## 📋 System Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.8+ |
| Rasa | 3.x |
| RAM | 4GB minimum (8GB recommended) |
| Disk Space | 2GB+ for models |
| OS | Windows, macOS, or Linux |

---

## 📦 Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/Bhargi777/Rasabot.git
cd Rasabot
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Rasa

Ensure your Rasa config files are in the `config/` directory:
- `config.yml` - NLU pipeline configuration
- `domain.yml` - Bot domain and actions
- `credentials.yml` - External service credentials
- `endpoints.yml` - API endpoints

### Step 5: Train Rasa Model

```bash
rasa train --config config/config.yml --domain config/domain.yml --data data/ --out models/
```

### Step 6: Start Rasa Server

In a separate terminal:

```bash
rasa run --model models/<your-model>.tar.gz --enable-api --cors "*"
```

Verify server is running:
```bash
curl http://localhost:5005/health
```

Expected response:
```json
{"status":"ok"}
```

### Step 7: Run Application

```bash
cd src
python main.py
```

---

## 📁 Project Structure

```
Rasabot/
├── src/                              # Application source code
│   ├── main.py                       # Application entry point
│   ├── chatbot_app.py                # Main application class
│   ├── chat_ui.py                    # Chat interface UI
│   ├── voice_input.py                # Voice input handler
│   ├── emotion_detection.py          # Emotion/sentiment analysis
│   ├── ai_model.py                   # AI model utilities
│   ├── utils.py                      # Helper functions
│   ├── style_config.py               # UI styling
│   └── __init__.py
│
├── config/                           # Rasa configuration
│   ├── config.yml                    # NLU/Core pipeline config
│   ├── domain.yml                    # Domain definition
│   ├── credentials.yml               # Service credentials
│   └── endpoints.yml                 # API endpoints
│
├── data/                             # Training data
│   ├── nlu.yml                       # NLU training examples
│   ├── stories.yml                   # Conversation flows
│   └── rules.yml                     # Bot rules
│
├── actions/                          # Custom Rasa actions
│   ├── actions.py                    # Action implementations
│   └── __init__.py
│
├── models/                           # Trained models (generated)
│   └── (model files)
│
├── tests/                            # Test suite
│   └── test_stories.yml              # Story tests
│
├── assets/                           # Images & resources
│   └── (UI assets)
│
├── docs/                             # Documentation
│
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
├── .gitignore                        # Git ignore rules
└── LICENSE                           # MIT License
```

---

## 🎮 Usage Guide

### Launching the Application

1. **Start Rasa Server** (in separate terminal):
   ```bash
   rasa run --model models/<model>.tar.gz
   ```

2. **Run Application**:
   ```bash
   cd src
   python main.py
   ```

3. **Welcome Screen** appears with options to start chatting

### Chat Interface

#### Text Chat
- Type your message in the input field
- Press `Enter` or click **Send** button
- View bot response in chat window

#### Voice Chat
- Click the **🎤 Microphone** button
- Speak your message clearly
- Release to send
- TTS response plays automatically (if enabled)

#### Settings Panel
1. Click **⚙️ Settings** button
2. Configure:
   - **Theme**: Choose color scheme
   - **Font**: Select font family and size
   - **TTS**: Enable/disable voice responses
   - **Language**: Select language preference
3. Click **Save** to apply changes

### Analyzing Conversations

- View **Word Cloud**: Visual analysis of topics discussed
- Check **Sentiment**: Overall conversation sentiment
- See **Statistics**: Message counts and patterns
- Export **Chat History**: Save conversations

---

## 🔧 Configuration Guide

### Rasa NLU Pipeline

Edit `config/config.yml`:

```yaml
language: en
pipeline:
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: DIETClassifier
  - name: EntitySynonymMapper
  - name: ResponseSelector
```

### Bot Domain

Edit `config/domain.yml` to define:
- Intents (what users want)
- Entities (important data)
- Slots (memory/context)
- Responses (bot replies)
- Actions (custom behaviors)

### Training Data

Add examples in `data/nlu.yml`:

```yaml
version: "3.1"
nlu:
  - intent: greet
    examples: |
      - hello
      - hi
      - hey there
      - good morning
```

Add flows in `data/stories.yml`:

```yaml
version: "3.1"
stories:
  - story: greeting path
    steps:
      - intent: greet
      - action: utter_greet
```

---

## 📚 Module Reference

### `chatbot_app.py`
Main application controller orchestrating all components and UI updates.

### `chat_ui.py`
Handles chat display, message rendering, and user input widgets.

### `voice_input.py`
Manages speech-to-text conversion using SpeechRecognition library.

### `emotion_detection.py`
Analyzes user sentiment and emotions using transformers and NLP.

### `ai_model.py`
Utilities for loading and managing AI models.

### `utils.py`
Helper functions: image loading, translation, sentiment analysis, etc.

### `style_config.py`
UI theming and styling configuration for CustomTkinter.

---

## 🐛 Troubleshooting

### Issue: "No trained model found"
**Solution**: Train a model using `rasa train` command. Model must be in `models/` directory.

### Issue: Cannot connect to Rasa server
**Solutions**:
- Verify Rasa is running: `rasa run --model models/<model>.tar.gz`
- Check port 5005 is not blocked by firewall
- Ensure no other service uses port 5005

### Issue: Microphone not working
**Solutions**:
- Check OS microphone permissions
- Grant microphone access in system settings
- Test microphone with other applications
- Ensure microphone is not muted/disabled

### Issue: Text-to-Speech has no audio
**Solutions**:
- Enable TTS in settings
- Check system volume is not muted
- Verify audio output device is connected
- Check speaker/headphone connection

### Issue: Application crashes on startup
**Solutions**:
- Verify all dependencies installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Ensure Rasa server is running
- Check for model file in `models/` directory

---

## 🚀 Advanced Usage

### Custom Actions

Create custom actions in `actions/actions.py`:

```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> str:
        return "action_greet"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker, domain: dict) -> list:
        dispatcher.utter_message(text="Hello! How can I help?")
        return []
```

### Integrate External APIs

Extend `actions.py` to call external services:

```python
import requests

class ActionGetWeather(Action):
    def name(self) -> str:
        return "action_get_weather"
    
    def run(self, dispatcher, tracker, domain):
        # Call weather API
        response = requests.get("https://api.weather.com/...")
        dispatcher.utter_message(text=response.json())
        return []
```

### Database Integration

Add database support for persistent conversations:

```python
from sqlalchemy import create_engine
# Create engine for storing conversations
engine = create_engine('sqlite:///conversations.db')
```

---

## 📊 Performance Optimization

### Model Optimization
- Use quantized models for faster inference
- Reduce NLU pipeline complexity for real-time responses
- Cache frequently used responses

### Memory Management
- Clear conversation history periodically
- Limit word cloud size
- Optimize image assets

### Server Configuration
- Use production-ready server (gunicorn, nginx)
- Enable model caching
- Configure connection pooling

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Write unit tests for new features
- Update README with new features

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

**Bhargava Srisai**
- GitHub: [@Bhargi777](https://github.com/Bhargi777)
- Project: [Rasabot](https://github.com/Bhargi777/Rasabot)

---

## 🙏 Acknowledgments

This project stands on the shoulders of great open-source projects:

- **[Rasa](https://rasa.com/)** - Open source conversational AI framework
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern Python GUI
- **[Hugging Face](https://huggingface.co/)** - ML models and transformers
- **[Google Cloud](https://cloud.google.com/)** - Translation services
- **[spaCy](https://spacy.io/)** - NLP library
- **[NLTK](https://www.nltk.org/)** - Natural Language Toolkit

---

## 📞 Support & Contact

**Have Questions?**
- Open an [Issue](https://github.com/Bhargi777/Rasabot/issues)
- Check [Discussions](https://github.com/Bhargi777/Rasabot/discussions)
- Read [Documentation](https://rasa.com/docs/)

**Report Bugs**
Please include:
- Python version
- OS and version
- Error message/traceback
- Steps to reproduce

---

## 🔗 Useful Resources

- [Rasa Official Documentation](https://rasa.com/docs/)
- [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Rasa Community Forum](https://forum.rasa.com/)
- [StackOverflow - Rasa Tag](https://stackoverflow.com/questions/tagged/rasa)

---

## 📈 Roadmap

- [ ] Web interface version
- [ ] Multi-language support enhancement
- [ ] Integration with popular messaging platforms
- [ ] Advanced analytics dashboard
- [ ] Model deployment to cloud
- [ ] Mobile application
- [ ] REST API for external integrations

---

**Last Updated**: February 22, 2026  
**Status**: ✅ Active Development  
**Version**: 1.0.0
