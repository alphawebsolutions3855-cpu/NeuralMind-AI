# NeuralMind-AI - Installation & Setup Guide

## 📋 Prerequisites

- **Python 3.8+** (download from https://www.python.org/downloads/)
- **Node.js 14+** (optional)
- **4GB RAM minimum**
- **pip** (comes with Python)

## 🚀 Quick Start (5 minutes)

### Step 1: Clone Repository
```bash
git clone https://github.com/alphawebsolutions3855-cpu/NeuralMind-AI.git
cd NeuralMind-AI
```

### Step 2: Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### Step 3: Run Tests
```bash
python backend/tests.py
```

Expected: ✅ All 10 tests passed!

### Step 4: Start Backend
```bash
python backend/app.py
```

Server runs at: http://localhost:5000

### Step 5: Open Frontend (new terminal)
```bash
# Option A: Python server
python -m http.server 8000
# Open: http://localhost:8000/frontend/

# Option B: Node server
cd frontend && npm install && npm start
# Open: http://localhost:3000/frontend/
```

## 📚 Complete Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
python tests.py      # Verify installation
python app.py        # Start server
```

### Frontend
```bash
cd frontend
npm install
npm start            # Or use Python server
```

## 🎯 Usage

### Web Chat
1. Open UI at http://localhost:3000
2. Type message and click Send
3. AI generates response
4. Click 👍 or 👎 for feedback
5. Model learns continuously

### API Examples

```bash
# Generate response
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello"}'

# Get stats
curl http://localhost:5000/api/stats

# Health check
curl http://localhost:5000/api/health
```

### Python
```python
import sys
sys.path.insert(0, 'backend')
from neural_mind import NeuralMind

model = NeuralMind()
response = model.generate("Hello")
model.learn("Hello", response, 0.9)
print(model.get_stats())
```

## 📁 Structure

```
NeuralMind-AI/
├── backend/
│   ├── app.py              # Flask API
│   ├── neural_mind.py      # AI Model (100% custom)
│   ├── tests.py            # 10 tests, all passing
│   ├── requirements.txt    # Dependencies
│   └── data/               # SQLite database
├── frontend/
│   ├── index.html          # Web UI
│   └── package.json        # Config
├── models/                 # Saved models
├── README.md               # Main docs
└── LICENSE                 # MIT
```

## 🧪 Tests

```bash
python backend/tests.py
```

Output:
```
✓ Model creation
✓ Tokenization works
✓ Generation works
✓ Learning system
✓ Statistics
✓ Softmax function
✓ Tokenize/detokenize cycle
✓ Temperature parameter
✓ Multiple interactions
✓ Model persistence

✅ Results: 10 Passed | ❌ 0 Failed
🎉 ALL TESTS PASSED! No errors detected.
```

## 🔧 Configuration

**Backend (app.py)**
- Host: 0.0.0.0
- Port: 5000
- Debug: True

**Model (neural_mind.py)**
- Vocab size: 10,000
- Embedding dim: 512
- Max tokens: 256
- Temperature: 0.7

## 🚨 Troubleshooting

### Port 5000 in use
```bash
lsof -i :5000        # Find process
kill -9 <PID>        # Kill it
```

### Missing modules
```bash
pip install --upgrade -r backend/requirements.txt
```

### Tests fail
```bash
rm -rf backend/__pycache__
python backend/tests.py
```

## 📊 Performance

- Model Size: 50MB
- Memory: 200MB-2GB
- Inference: 100-500ms
- Training: 2-5 q/sec
- Vocab: 10,000+ tokens

## 🎓 Learning

The model learns automatically:
- Collects conversations
- Tracks feedback
- Daily fine-tuning
- Weight adjustments
- Saves to disk

## 🔒 Offline

Everything works without internet:
- Generate responses ✓
- Learn from interactions ✓
- Save models ✓
- Access UI ✓

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/generate` | Generate response |
| POST | `/api/learn` | Submit feedback |
| GET | `/api/stats` | Statistics |
| GET | `/api/health` | Health check |
| GET | `/api/info` | Model info |
| POST | `/api/save` | Save model |
| GET | `/api/interactions` | Past chats |

## 📄 License

MIT License

---

**Built by alphawebsolutions3855-cpu** 🚀
