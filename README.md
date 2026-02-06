# 📚 Multi-PDF & Web-Scraped RAG Chatbot  
**College Information Chatbot – SGSITS Indore**

---

## 🚀 Overview
Accessing accurate information from large collections of PDFs and scattered college web pages can be time-consuming and inefficient. This project solves that problem by building an **AI-powered Retrieval-Augmented Generation (RAG) chatbot** that answers user queries using **multiple PDFs** and **selected HTML webpages of SGSITS Indore**.

The chatbot allows users to ask questions in natural language and receive **context-aware, precise, and conversational answers** related to college academics, departments, notices, policies, and other institutional information.

---

## 🎯 Problem Statement
Colleges and institutions store information across multiple sources:
- 📄 PDF documents (notices, circulars, academic guidelines)
- 🌐 HTML webpages (departments, administration, rules, facilities)

Traditional search mechanisms:
- Depend heavily on keywords  
- Lack semantic understanding  
- Require manual navigation across multiple files and pages  

This results in poor user experience and delayed access to important information.

---

## 💡 Solution
This project implements a **Multi-Source RAG-based Chatbot** that:
- Ingests and processes **multiple PDF documents**
- Scrapes and parses **selected SGSITS Indore official HTML webpages**
- Converts content into vector embeddings
- Uses a **Generative AI model** to produce accurate and human-like responses

The chatbot acts as a **virtual college assistant**, providing instant answers from trusted internal sources.

---

## 🎯 Objectives
The primary goals of this chatbot are:
- Provide fast and accurate answers to college-related queries
- Enable natural language interaction with PDFs and web data
- Reduce manual effort in searching documents and webpages
- Improve accessibility of SGSITS Indore information
- Demonstrate real-world application of RAG, NLP, and Generative AI

---

## 🧠 How It Works
The chatbot follows a **Retrieval-Augmented Generation (RAG)** pipeline:

1. **User Query**  
   The user asks a question (e.g., *“What departments are available at SGSITS?”*).

2. **Retrieval Phase**  
   Relevant content is retrieved from:
   - Embedded PDF documents
   - Embedded SGSITS Indore HTML webpages

3. **Context Injection**  
   Retrieved text chunks are passed as context to the LLM.

4. **Answer Generation**  
   The generative model produces a clear, concise, and contextual response.

5. **Response Delivery**  
   The final answer is shown to the user in chatbot form.

---

## 🏗️ System Architecture
**Data Sources**
- Multiple PDFs (college notices, academic documents)
- SGSITS Indore HTML webpages (selected pages only)

**Processing Pipeline**
- Text extraction (PDF & HTML)
- Text chunking
- Embedding generation
- Vector storage (FAISS)
- Query-based retrieval
- LLM-based response generation

---

## 🔑 Key Components

### 1️⃣ Data Ingestion
- PDF text extraction
- Web scraping of SGSITS Indore webpages using HTML parsers

### 2️⃣ Text Chunking
- Large documents are split into smaller semantic chunks for better retrieval

### 3️⃣ Embedding Generation
- Each chunk is converted into a vector embedding using a transformer-based model

### 4️⃣ Vector Database
- FAISS is used for efficient similarity search

### 5️⃣ Generative AI Model
- A GPT-style or open-source LLM generates responses using retrieved context

### 6️⃣ Chat Interface
- Users interact with the system through a simple chatbot UI

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Web Scraping:** BeautifulSoup / Requests  
- **PDF Processing:** PyPDF / PDFMiner  
- **Embeddings:** Sentence Transformers  
- **Vector Store:** FAISS  
- **LLM:** OLLAMA (gemma 3:1b)
- **Backend:** Flask  
- **Frontend:** HTML, CSS, JavaScript  

---

## 📌 Use Cases
- Students querying college rules, departments, or notices
- Freshers exploring SGSITS Indore information
- Quick access to academic and administrative data
- Demonstration of RAG-based AI systems for education

---

## 🌟 Key Features
- Multi-PDF support
- Web-scraped college data integration
- Semantic search (not keyword-based)
- Context-aware responses
- Scalable and extensible architecture
- College-specific knowledge base

---

## 📈 Future Enhancements
- Add more SGSITS webpages automatically
- Role-based responses (student, faculty, admin)
- Voice-based query support
- Chat history and personalization
- Multilingual support

---

## 📜 Conclusion
This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be effectively used to build an intelligent, domain-specific chatbot. By combining **PDFs**, **web-scraped college data**, an
