# Project Document: Agentic RAG Knowledge Assistant

**Author:** Yash Shukla
Note: Just drafted a document based on what I have worked on since participating through Phone
---

## Project Overview

This project delivers an intelligent Knowledge Assistant that can:
- Ingest documents from sources like PDFs, text files, and web content.
- Use Retrieval Augmented Generation (RAG) to fetch relevant knowledge.
- Rely on an agentic reasoning layer that intelligently chooses how to answer: retrieving knowledge, refining queries, or invoking external tools (such as a calculator API).
- Provide natural, context-aware responses to user queries.

---

## Objectives & Scope

### Objectives

- Deliver accurate, context-aware answers sourced from both private and public knowledge bases.
- Enable agentic reasoning to select between retrieval, reasoning, and tool invocation for flexible processing.
- Ensure the architecture remains modular and extensible—new tools, sources, and logic can be added efficiently.

### Scope

- Ingest unstructured content and store its semantic representations in a vector database.
- Offer a REST/CLI interface for querying the system.
- Demonstrate tool selection logic using a combination of knowledge base lookup and LLM fallback for reasoning and calculation.

---

## High-Level Architecture

### Algorithm Description (Replaces Flowchart)

- System receives a user query.
- The agentic layer evaluates intent—does the user require knowledge retrieval, computational reasoning, or external tool usage?
- For retrieval:
    - Query relevant vectors in the database.
    - Extract top-matching content chunks via semantic search.
    - Supply query and retrieved content to the LLM for answer synthesis.
- For reasoning or computation:
    - Call on the LLM’s direct capabilities (math, logic, small talk).
    - Invoke external tools as needed (calculator, APIs).
- Synthesized answer is returned to the user.

---

## Workflow

### Detailed Steps

1. User submits a question.
2. The ReAct agent determines if the query requires knowledge lookup, generic reasoning, or tool invocation.
3. If knowledge base lookup is needed:
    - Retrieve relevant content chunks via semantic search in the vector DB.
    - Pass both the user query and retrieved content to the LLM for context-enriched answering.
4. If no match is found:
    - Perform open-ended reasoning via the LLM.
5. If an explicit computational or external function is required:
    - Route query to the appropriate tool or API.
6. Return the final synthesized response to the user.

---

## Tech Stack

| Component         | Technology Used                    |
|-------------------|-----------------------------------|
| LLM               | GPT-4.1                           |
| Embeddings        | Cohere Embed v4                   |
| Vector DB         | OpenSearch                        |
| Agent Framework   | LangChain (ReAct Agent)           |
| Backend           | Python (FastAPI / Flask optional) |
| Orchestration     | LangChain Tools (RetrievalQA, Calculator, etc.)  |

---

## Sample Interaction Flow

**User:** What is RAG?  
**Agent:**
- Detects a knowledge lookup.
- Queries the vector DB (OpenSearch, using Cohere Embed v4).
- Retrieves content explaining “Retrieval Augmented Generation.”
- Returns a synthesized answer (via GPT-4.1).

**User:** What is 25 * 14?  
**Agent:**
- Detects a math computation request.
- Skips document retrieval.
- Uses GPT-4.1 reasoning or invokes a calculator tool.
- Returns: "25 × 14 = 350."

---

## Future Enhancements

- **API Interface:** Build REST endpoints (/ingest, /ask) using FastAPI for scalable interaction.
- **Advanced Tools:** Add support for SQL connectors, web searches, or code interpretation.
- **Multi-Modal Support:** Enable ingestion and processing of PDFs, images (using OCR to embeddings), and other data types.
- **Hybrid Retrieval:** Combine BM25 keyword search with vector similarity for enhanced results.
- **Agentic Control:** Integrate advanced stateful reasoning frameworks (e.g., LangGraph) to replace basic ReAct-style reasoning.

---
