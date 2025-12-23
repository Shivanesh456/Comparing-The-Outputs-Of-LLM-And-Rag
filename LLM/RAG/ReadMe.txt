# Retrieval-Augmented Generation (RAG) System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline using a medium-sized textual dataset.  
The system retrieves relevant information from external documents using semantic search and generates grounded answers using a language model.

The approach avoids fine-tuning and instead enhances responses by retrieving context at inference time.

---

## What is RAG?
Retrieval-Augmented Generation (RAG) combines:
- Retrieval: Fetching relevant document chunks from a vector database
- Generation: Producing answers using a language model based on retrieved context

This improves factual accuracy and reduces hallucinations.

---

## Architecture
1. Load documents from the dataset
2. Split documents into chunks
3. Convert chunks into vector embeddings
4. Store embeddings in a FAISS vector database
5. Retrieve relevant chunks at query time
6. Generate responses using a language model

---

## Project Structure
RAG/
+-- data/
¦   +-- *.txt
+-- ingest.py
+-- rag_query.py
+-- requirements.txt
+-- README.md

---

## Dataset
- Format: Text files (.txt)
- Size: Medium-level dataset
- Domain: AI / Machine Learning / NLP
- Documents are chunked for semantic retrieval

---

## Technologies Used
- Python 3.10
- LangChain (0.1.16)
- LangChain Community
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- FLAN-T5

---

## Setup Instructions

### 1. Install Dependencies
pip install -r requirements.txt

---

### 2. Create Vector Database
python ingest.py

Expected output:
Loaded X documents  
Created Y chunks  
Vector database created successfully  

---

### 3. Run RAG System (Multiple Questions)
python rag_query.py

Example:
Ask a question: What is AI?  
Answer: Artificial intelligence refers to the simulation of human intelligence in machines.

Ask a question: What is machine learning?  
Answer: Machine learning is a subset of AI that focuses on learning from data.

Type 'exit' to stop.

---

## Key Features
- Semantic search using vector embeddings
- Interactive multi-question support
- Clean and concise answers
- No fine-tuning required
- Scalable to larger datasets

---

## Future Enhancements
- PDF and CSV support
- Source citations
- Larger datasets
- Web or API interface

---

## Summary
This project demonstrates a complete end-to-end RAG implementation using modern NLP tools.  
It showcases how external knowledge can be combined with language models to produce accurate, context-aware answers.
