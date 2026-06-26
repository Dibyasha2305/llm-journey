#  AI Customer Support Automation using LangGraph

An intelligent **AI-powered Customer Support Automation System** built using **LangGraph**, **LangChain**, **FAISS**, **SQLite**, and **Hugging Face Embeddings**. The system classifies customer queries, routes them to specialized support agents, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), maintains conversation history using SQLite, and incorporates a Human-in-the-Loop approval workflow for sensitive customer requests.

---

##  Features

*  Intent Classification
*  Multi-Agent Routing using LangGraph
*  Retrieval-Augmented Generation (RAG)
*  FAISS Vector Database
*  SQLite Conversation Memory
*  Human-in-the-Loop Approval
*  Supervisor Agent
*  Knowledge Base Search
*  Customer Support Workflow Automation

---

## System Workflow

```
Customer Query
       │
       ▼
Intent Classification
       │
       ├──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
       ▼              ▼              ▼              ▼              ▼
    Sales        Technical      Billing        Account        Memory
       │              │              │              │              │
       │              │              ▼              │              │
       │              │       Approval Check        │              │
       │              │              │              │              │
       │              │              ▼              │              │
       │              │      Supervisor Agent       │              │
       └──────────────┴──────────────┴──────────────┴──────────────┘
                              │
                              ▼
                        Final Response
```

---

## Knowledge Base

The RAG pipeline retrieves information from the following documents:

* Company Policy
* Pricing Guide
* Technical Manual
* Frequently Asked Questions (FAQ)

These documents are embedded using **Hugging Face Sentence Transformers** and stored in a **FAISS Vector Store** for semantic search.

---

## Memory

Customer conversations are stored using **SQLite**.

Example:

```
Customer:
I need a refund.

Later...

Customer:
What was my previous support issue?

AI:
Your previous support issue was:
I need a refund.
```

---

## Human-in-the-Loop Approval

The following requests require supervisor approval before a final response is sent:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

##  Tech Stack

* Python 3.x
* LangGraph
* LangChain
* FAISS
* Hugging Face Embeddings
* SQLite
* Sentence Transformers

---

##  Project Structure

```
02-customer-support-automation/
│
├── images/
│
├── knowledge_base/
│   ├── company_policy.txt
│   ├── pricing_guide.txt
│   ├── technical_manual.txt
│   └── faq.txt
│
├── app.py
├── graph.py
├── nodes.py
├── rag.py
├── memory.py
├── approval.py
├── supervisor.py
├── state.py
├── requirements.txt
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/Dibyasha2305/llm-journey.git
```

Navigate to the project:

```bash
cd Agentic-AI/02-customer-support-automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Run the Project

```bash
python app.py
```

---

##  Sample Queries

### Sales

```
What are the pricing plans available for your software?
```

---

### Account

```
I forgot my account password.
```

---

### Technical Support

```
My application crashes whenever I upload a file.
```

---

### Billing (Human Approval)

```
I need a refund for my annual subscription.
```

---

### Memory Recall

```
What was my previous support issue?
```

---

##  Screenshots

Project screenshots are available in the **images/** directory.

* Workflow Diagram
* Sales Agent
* Technical Agent
* Billing Approval
* Memory Recall
* RAG Retrieval
* Project Structure

---

##  Future Improvements

* Integrate with OpenAI or Gemini APIs
* Web-based chat interface
* Multi-user authentication
* Email notifications
* Voice-enabled customer support
* Persistent vector database
* Live customer support dashboard

---

##  Author

**Dibyasha**



---

##  License

This project is developed for educational purposes as part of an **Agentic AI / LangGraph** coursework assignment.
