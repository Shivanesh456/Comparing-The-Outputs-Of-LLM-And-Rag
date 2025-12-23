# Normal LLM (Without RAG)

## Overview
This project uses a standard Large Language Model (LLM) to answer user questions.  
The model responds based only on what it learned during training and does not use any external documents or datasets.

This setup is intentionally kept simple and is mainly used as a baseline to compare against a RAG-based system.

---

## What does this project do?
- Takes a question from the user
- Sends the question directly to a pretrained language model
- Displays the model’s response
- Supports multiple questions in a single run

There is no retrieval step involved.

---

## Why is this needed?
This implementation helps demonstrate how a normal LLM behaves when:
- It does not have access to external data
- It relies only on pretrained knowledge
- Answers may be generic or outdated

The output from this project is later compared with a RAG-based setup to highlight the differences.

---

## Project Structure
Normal_LLM/
- normal_llm.py
- README.md

---

## Technologies Used
- Python 3.10
- Hugging Face Transformers
- FLAN-T5 (google/flan-t5-base)

---

## How to Run

### Step 1: Install dependencies
pip install transformers torch

### Step 2: Run the script
python normal_llm.py

---

## How it works (simple flow)
1. The script loads a pretrained FLAN-T5 model.
2. The user types a question in the terminal.
3. The model generates an answer using only its internal knowledge.
4. The process repeats until the user exits.

---

## Example
Ask a question: What is AI?

Answer:
Artificial intelligence is the simulation of human intelligence in machines.

Ask a question: What is machine learning?

Answer:
Machine learning is a subset of AI that focuses on learning from data.

Type 'exit' to stop the program.

---

## Limitations
- The model cannot access external documents
- Answers may be generic
- Knowledge cannot be updated dynamically
- Higher chance of hallucination compared to RAG

---

## Purpose of This Setup
This project serves as a comparison point for evaluating the benefits of Retrieval-Augmented Generation (RAG), where external documents are retrieved and used to generate more accurate answers.

---

## Summary
This is a simple, interactive LLM-based question-answer system without retrieval.  
It is useful for understanding the limitations of a standalone language model before introducing RAG.
