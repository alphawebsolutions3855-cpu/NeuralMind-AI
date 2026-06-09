"""Unit Tests for NeuralMind-AI"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from neural_mind import NeuralMind
import numpy as np

passed = 0
failed = 0

def test(name, condition):
    global passed, failed
    if condition:
        print(f"✓ {name}")
        passed += 1
    else:
        print(f"✗ {name}")
        failed += 1

print("\n🧪 NeuralMind-AI Test Suite\n")

# Test 1: Model creation
model = NeuralMind()
test("Model creation", model is not None)
test("Vocab size", model.vocab_size == 10000)
test("Embedding dim", model.embedding_dim == 512)

# Test 2: Tokenization
tokens = model.tokenize("Hello world")
test("Tokenization works", len(tokens) > 0)
test("Start token", tokens[0] == 1)
test("End token", tokens[-1] == 2)

# Test 3: Generation
response = model.generate("Hello", max_tokens=10)
test("Generation works", response is not None)
test("Response is string", isinstance(response, str))

# Test 4: Learning
result = model.learn("What is AI?", "AI is artificial intelligence", 0.9)
test("Learning returns True", result == True)
test("Learning entry added", len(model.learning_history) > 0)

# Test 5: Statistics
stats = model.get_stats()
test("Stats dict created", isinstance(stats, dict))
test("Has interactions", 'interactions' in stats)

# Test 6: Softmax
x = np.array([1.0, 2.0, 3.0])
probs = model._softmax(x)
test("Softmax shape correct", probs.shape == x.shape)
test("Softmax sums to 1", abs(probs.sum() - 1.0) < 0.001)

# Test 7: Model save
result = model.save_model('test_model.json')
test("Model save works", result == True)
test("Model file exists", os.path.exists('test_model.json'))

if os.path.exists('test_model.json'):
    os.remove('test_model.json')

# Test 8: Multiple interactions
model2 = NeuralMind()
for i in range(5):
    model2.generate(f"Prompt {i}")
test("Multiple interactions", len(model2.interactions) == 5)

# Test 9: Temperature parameter
resp1 = model.generate("Test", temperature=0.1)
resp2 = model.generate("Test", temperature=0.9)
test("Low temp generation", len(resp1) > 0)
test("High temp generation", len(resp2) > 0)

# Test 10: Tokenize/Detokenize
tokens = model.tokenize("Hello world test")
detok = model.detokenize(tokens)
test("Detokenize works", len(detok) > 0)

print(f"\n✅ Results: {passed} Passed | ❌ {failed} Failed\n")

if failed == 0:
    print("🎉 ALL TESTS PASSED! No errors detected.\n")
    sys.exit(0)
else:
    sys.exit(1)
