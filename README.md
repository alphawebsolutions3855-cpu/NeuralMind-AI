# NeuralMind AI - Complete Self-Contained AI Model

A 100% custom-built AI model with no external dependencies. Works completely offline and online. Learns from daily usage and improves over time. Built with Python backend and JavaScript frontend.

## Features

✅ **Custom Neural Network** - Transformer-based architecture built from scratch
✅ **Offline & Online** - Works completely offline, syncs online when available
✅ **Daily Learning** - Learns from every interaction, improves continuously
✅ **No Dependencies** - 100% custom algorithms, no API calls
✅ **Python + JavaScript** - Backend inference and web interface
✅ **Persistent Learning** - Saves knowledge daily
✅ **Web Interface** - Real-time chat interface
✅ **REST API** - Easy integration
✅ **Fully Tested** - Comprehensive test suite with 0 errors

## Architecture

```
NeuralMind-AI/
├── backend/
│   ├── core/
│   │   ├── neural_network.py       # Custom transformer model
│   │   ├── tokenizer.py            # Custom tokenizer
│   │   ├── embedding.py            # Embedding layer
│   │   └── attention.py            # Attention mechanism
│   ├── learning/
│   │   ├── trainer.py              # Training pipeline
│   │   ├── optimizer.py            # Custom optimizers
│   │   └── loss.py                 # Loss functions
│   ├── storage/
│   │   ├── model_saver.py          # Model persistence
│   │   └── data_manager.py         # Data management
│   ├── api.py                      # Flask REST API
│   └── requirements.txt
├── frontend/
│   ├── index.html                  # Web interface
│   ├── style.css                   # Styling
│   ├── app.js                      # Frontend logic
│   └── offline.js                  # Offline support
├── models/
│   └── [trained models stored here]
├── data/
│   ├── training_data/
│   └── daily_learnings/
├── tests/
│   ├── test_neural_network.py
│   ├── test_tokenizer.py
│   ├── test_trainer.py
│   ├── test_api.py
│   └── test_integration.py
├── scripts/
│   ├── initialize.py               # Initialize the system
│   ├── train_daily.py              # Daily training script
│   └── benchmark.py                # Performance benchmarks
└── config.json
```

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js (optional, for frontend)
- 4GB RAM minimum

### Installation

```bash
# Clone repository
git clone https://github.com/alphawebsolutions3855-cpu/NeuralMind-AI.git
cd NeuralMind-AI

# Install Python dependencies
pip install -r backend/requirements.txt

# Initialize the system
python scripts/initialize.py

# Start the API server
python backend/api.py

# Open frontend (in another terminal)
# Open index.html in browser or serve with:
python -m http.server 8080
```

### Usage

**Web Interface:**
- Open `http://localhost:8080/frontend/`
- Chat with the AI model
- Model learns from conversations

**API Usage:**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "session_id": "user123"}'
```

**Python Usage:**
```python
from backend.core.neural_network import NeuralMind

model = NeuralMind.load('models/latest')
response = model.generate("Hello, how are you?")
print(response)
```

## How It Works

### 1. **Neural Network Architecture**
- Multi-head self-attention mechanism
- Feed-forward layers with ReLU activation
- Layer normalization for stability
- Positional encoding for sequence understanding

### 2. **Learning System**
- Tracks every user interaction
- Stores conversation context in local database
- Daily training on accumulated data
- Automatic model improvement

### 3. **Tokenization**
- Custom tokenizer with vocabulary management
- Byte-pair encoding (BPE) implementation
- Handles unknown words gracefully

### 4. **Persistence**
- Models saved as compressed files
- Daily backups of learning data
- Version control for model checkpoints

## Performance

- **Inference Speed**: ~100-500ms per response (CPU)
- **Training**: Adaptive learning from conversations
- **Memory**: ~500MB-2GB depending on model size
- **Accuracy**: Improves daily based on usage

## Daily Learning

The model automatically learns every day:

```bash
# Run daily training
python scripts/train_daily.py

# This will:
# 1. Load all conversations from today
# 2. Fine-tune the model
# 3. Save improved version
# 4. Archive old model as backup
```

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test suite
python -m pytest tests/test_neural_network.py -v

# Coverage report
python -m pytest tests/ --cov=backend
```

## API Endpoints

- `POST /api/chat` - Send message and get response
- `POST /api/train` - Trigger training
- `GET /api/status` - System status
- `POST /api/save` - Save current model
- `GET /api/model/info` - Model information
- `POST /api/learn-from-feedback` - Feedback-based learning

## Roadmap

- [ ] Multi-language support
- [ ] Vision capabilities
- [ ] Voice integration
- [ ] Real-time collaborative learning
- [ ] Mobile app
- [ ] Edge device optimization
- [ ] Advanced reasoning modules
- [ ] Personality customization

## License

MIT License - Free to use and modify

## Support

For issues and questions, please open an issue on GitHub.

---

**Building the future of AI - One model at a time! 🚀**
