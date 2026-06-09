"""Flask API Server for NeuralMind-AI"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from neural_mind import NeuralMind
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

model = NeuralMind(vocab_size=10000, embedding_dim=512)

DB_PATH = 'data/interactions.db'
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (id INTEGER PRIMARY KEY, prompt TEXT, response TEXT, 
                  feedback REAL, user_id TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'version': '1.0.0'})

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        max_tokens = data.get('max_tokens', 256)
        temperature = data.get('temperature', 0.7)
        user_id = data.get('user_id')
        
        if not prompt:
            return jsonify({'error': 'Prompt required'}), 400
        
        response = model.generate(prompt, max_tokens, temperature)
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''INSERT INTO interactions 
                     (prompt, response, user_id, timestamp) 
                     VALUES (?, ?, ?, ?)''',
                  (prompt, response, user_id, datetime.now().isoformat()))
        conn.commit()
        interaction_id = c.lastrowid
        conn.close()
        
        return jsonify({
            'success': True,
            'interaction_id': interaction_id,
            'prompt': prompt,
            'response': response,
            'model_stats': model.get_stats()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/learn', methods=['POST'])
def learn():
    try:
        data = request.json
        interaction_id = data.get('interaction_id')
        feedback = data.get('feedback', 0.75)
        prompt = data.get('prompt', '')
        response = data.get('response', '')
        
        model.learn(prompt, response, feedback)
        
        if interaction_id:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('UPDATE interactions SET feedback = ? WHERE id = ?',
                      (feedback, interaction_id))
            conn.commit()
            conn.close()
        
        return jsonify({'success': True, 'message': 'Learning recorded'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def stats():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('SELECT COUNT(*) FROM interactions')
        total = c.fetchone()[0]
        
        c.execute('SELECT AVG(feedback) FROM interactions WHERE feedback IS NOT NULL')
        avg = c.fetchone()[0] or 0
        
        conn.close()
        
        return jsonify({
            'model_stats': model.get_stats(),
            'database_stats': {'total_interactions': total, 'average_feedback': round(avg, 2)}
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save', methods=['POST'])
def save_model():
    try:
        model.save_model()
        return jsonify({'success': True, 'message': 'Model saved'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        'name': 'NeuralMind-AI',
        'version': '1.0.0',
        'author': 'alphawebsolutions3855-cpu',
        'capabilities': ['Text Generation', 'Continuous Learning', 'Offline Mode']
    })

if __name__ == '__main__':
    print("\n🚀 NeuralMind-AI Backend Server\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
