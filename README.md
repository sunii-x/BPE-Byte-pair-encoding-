# 🧠 Byte Pair Encoding (BPE) Tokenizer

[![CI Testing](https://github.com/sunii-x/BPE-Byte-pair-encoding-/actions/workflows/tests.yml/badge.svg)](https://github.com/sunii-x/BPE-Byte-pair-encoding-/actions)

A from-scratch implementation of a **Byte Pair Encoding (BPE)** tokenizer in Python. 

## 🚀 Why I Built This
I built this project to move beyond treating AI as a "black box" and to deeply understand the mechanics of natural language processing. Understanding how text is compressed and converted into the numerical logic of neural networks is a crucial step for developing advanced AI applications and agents, including my work on projects like Bengine (AI Tutor).

## ✨ Features
*   **Train from Scratch:** Build a custom vocabulary by training the tokenizer on any text dataset.
*   **Encode:** Convert raw strings of text into a sequence of integer token IDs.
*   **Decode:** Perfectly reconstruct the original text from token IDs.
*   **Automated Testing:** Fully unit-tested using GitHub Actions to ensure reliable encoding and decoding loops.

## 💻 Example Usage

Here is how you can train the tokenizer and use it to encode and decode text:

```python
from tokenizer import BPETokenizer

# 1. Initialize the Tokenizer
tokenizer = BPETokenizer()

# 2. Train it on sample text
training_data = "The quick brown fox jumps over the lazy dog. Tokenization is the foundation of LLMs."
tokenizer.train(training_data)

# 3. Encode a sentence
text = "The quick brown fox"
tokens = tokenizer.encode(text)
print(f"Encoded Tokens: {tokens}") 
# Example Output: [12, 45, 8, 99]

# 4. Decode back to text
decoded_text = tokenizer.decode(tokens)
print(f"Decoded Text: {decoded_text}") 
# Output: "The quick brown fox"
