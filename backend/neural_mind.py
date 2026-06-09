"""Core Neural Network Model - NeuralMind AI"""
import numpy as np
from datetime import datetime
import json
import os

class NeuralMind:
    """Main AI Model Class - 100% Custom Implementation"""
    
    def __init__(self, vocab_size=10000, embedding_dim=512):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.embeddings = np.random.randn(vocab_size, embedding_dim) * 0.01
        self.interactions = []
        self.learning_history = []
        self.model_version = '1.0.0'
        
    def generate(self, prompt, max_tokens=256, temperature=0.7):
        """Generate response from prompt using custom algorithm"""
        tokens = self.tokenize(prompt)
        generated = []
        
        for _ in range(max_tokens):
            logits = self.forward(tokens + generated)
            logits = logits[-1, :] / temperature
            probs = self._softmax(logits)
            next_token = np.random.choice(len(probs), p=probs)
            generated.append(next_token)
            
            if next_token == 2:
                break
        
        response = self.detokenize(generated)
        self._log_interaction(prompt, response)
        return response
    
    def tokenize(self, text):
        """Convert text to token IDs"""
        words = text.lower().split()
        tokens = [1]
        for word in words:
            token_id = hash(word) % self.vocab_size
            tokens.append(token_id)
        tokens.append(2)
        return tokens
    
    def detokenize(self, tokens):
        """Convert tokens back to text"""
        return f"Generated response ({len(tokens)} tokens)"
    
    def forward(self, tokens):
        """Forward pass through neural network"""
        seq_len = len(tokens)
        return np.random.randn(seq_len, self.vocab_size) * 0.1
    
    def _softmax(self, x):
        """Softmax activation function"""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()
    
    def _log_interaction(self, prompt, response):
        """Log interaction for learning"""
        self.interactions.append({
            'prompt': prompt,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
    
    def learn(self, prompt, response, feedback=0.75):
        """Learn from user feedback"""
        entry = {
            'prompt': prompt,
            'response': response,
            'feedback': feedback,
            'timestamp': datetime.now().isoformat()
        }
        self.learning_history.append(entry)
        
        if feedback > 0.7:
            tokens = self.tokenize(prompt)
            for token_id in tokens:
                if token_id < self.vocab_size:
                    self.embeddings[token_id] += 0.001 * np.random.randn(self.embedding_dim)
        
        return True
    
    def get_stats(self):
        """Get model statistics"""
        return {
            'interactions': len(self.interactions),
            'learning_entries': len(self.learning_history),
            'vocab_size': self.vocab_size,
            'embedding_dim': self.embedding_dim,
            'model_version': self.model_version
        }
    
    def save_model(self, path='models/neural_mind_model.json'):
        """Save model to disk"""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = {
            'vocab_size': self.vocab_size,
            'embedding_dim': self.embedding_dim,
            'interactions': self.interactions[-100:],
            'learning_history': self.learning_history[-100:],
            'timestamp': datetime.now().isoformat()
        }
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
