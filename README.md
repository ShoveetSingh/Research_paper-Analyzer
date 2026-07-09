📄 AI Research Paper Analyzer

An AI-powered web application that analyzes research papers and generates structured insights using Large Language Models (LLMs).

🚀 Features
📤 Upload research papers in PDF format
📖 Extract text from PDFs
🧠 Generate AI-powered summaries
🔍 Identify the research problem
⚙️ Explain the methodology
📊 Highlight key findings
⚠️ List limitations
🔮 Suggest future work
💡 Explain papers in simple language (ELI5)
❓ Generate quiz questions / MCQs (Future Feature)
🏗️ Project Architecture
User
   │
   ▼
React Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
PyMuPDF
(Text Extraction)
   │
   ▼
Prompt Engineering
   │
   ▼
Gemini / OpenAI API
   │
   ▼
AI Response
   │
   ▼
Frontend
🛠️ Tech Stack
Frontend
React
Vite
Tailwind CSS
Axios
Backend
FastAPI
Uvicorn
Pydantic
AI
Gemini API (or OpenAI API)
PDF Processing
PyMuPDF



Future
Chroma / FAISS (RAG)
Redis (Caching & Chat History)
Docker
JWT Authentication

⚙️ Workflow
User uploads a research paper (PDF)
FastAPI receives the file
PyMuPDF extracts the text
Backend creates a structured prompt
Prompt + Paper text are sent to the LLM
LLM analyzes the paper
Backend returns the response
React displays the analysis
📋 AI Output Format

The AI generates:

Title
Authors
Research Problem
Objective
Methodology
Dataset Used (if available)
Model/Algorithm Used
Key Findings
Limitations
Future Work
Keywords
One-Paragraph Summary
🔮 Future Features
Chat with Research Paper (RAG)
Compare Two Research Papers
Citation Extraction
Reference Analysis
Keyword Extraction
Research Trend Detection
Multi-PDF Analysis
Save Previous Analyses
Export Analysis to PDF
📦 Python Libraries

Backend

fastapi
uvicorn
pymupdf
pydantic
python-multipart
python-dotenv

Frontend

react
vite
tailwindcss
axios

AI

google-generativeai (or OpenAI SDK)
🎯 Learning Goals

This project demonstrates:

FastAPI
REST APIs
File Upload Handling
PDF Processing
Prompt Engineering
LLM API Integration
React + FastAPI Communication
AI Application Development
📈 Planned Roadmap

Build React UI

Implement PDF upload

Extract text using PyMuPDF

Integrate Gemini/OpenAI API

Display structured analysis

Improve prompts

Add markdown formatting

Add loading animations

Add export to PDF

Implement RAG for Paper Q&A

Deploy application

👨‍💻 Author

Built as a portfolio project to learn modern Generative AI application development using FastAPI, React, LLM APIs, and prompt engineering.