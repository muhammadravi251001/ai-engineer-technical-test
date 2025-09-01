# Engineering Knowledge AI Agent Test

This document contains answers to the theoretical section of the **Technical AI Engineer Test**.

---

## 1. Describe differences between REST API, MCP in the context of AI.

**REST API** is a standard way for applications to communicate over HTTP using methods like GET or POST. In AI systems, REST APIs are often used to fetch or update data from external services (for example: databases, payments, or user profiles). It is simple, reliable, and works well for request–response interactions.

**MCP (Model Context Protocol)** is a newer protocol designed specifically for connecting Large Language Models (LLMs) with external data and tools. MCP provides two-way communication, gives models structured context, and ensures security and provenance (clear origin of data). It helps prevent risks like hallucination or prompt injection by controlling what information goes into and out of the model.

In short: REST API is a **general-purpose interface** for applications, while MCP is a **specialized protocol for AI**, focusing on giving LLMs the right context and safe tool access.

---

## 2. How REST API, MCP, can improve the AI use case.

**REST API** allows AI systems to connect with reliable external services and data sources. By fetching data through REST APIs (for example: customer records, transactions, or weather information), the AI can provide more accurate answers instead of guessing. REST APIs also let AI perform actions like creating records or updating information, not just generating text.

**MCP (Model Context Protocol)** ensures that AI agents use external data and tools in a structured, secure, and auditable way. It prevents prompt injection, enforces data provenance, and gives the model only the right context it needs. Together, REST API and MCP make AI use cases more accurate, trustworthy, and safe for real-world applications.

---

## 3. How do you ensure that your AI agent answers correctly?

To ensure correctness, an AI agent should always be grounded in reliable data sources instead of relying only on the model’s guesses (via their own embedded knowledge). This can be achieved using Retrieval-Augmented Generation (RAG), database queries, or REST API calls for deterministic answers. Tool calling ensures that when a user asks for specific information, the agent fetches it from the right source instead of hallucinating.

Additionally, results should be validated and cross-checked before being returned to the user. Confidence thresholds, monitoring, and feedback loops help detect and correct errors. In sensitive use cases, human-in-the-loop review can add an extra layer of trust. Together, grounding, validation, and monitoring make the agent’s answers accurate and reliable.

---

## 4. Describe what can you do with Docker / Containerize environment in the context of AI

In AI projects, Docker helps create a consistent environment by packaging all dependencies (Python, libraries like TensorFlow, PyTorch, or OpenCV) into containers. This makes AI applications portable, so they can run the same way on local machines, servers, or cloud platforms without complex setup. It also improves isolation and security, since containers keep the AI environment separate from the host system.

Docker also makes deployment and scaling much easier. An AI application can be bundled and run with a single command, or scaled across clusters with Kubernetes. Combined with CI/CD pipelines, containers ensure AI systems are reproducible, maintainable, and ready for real-world use.

---

## 5. How do you finetune the LLM model from raw? 

To finetune a Large Language Model (LLM) from raw, firstly we need to prepare a domain-specific dataset. This data should be cleaned, normalized, and formatted (for example in JSON or CSV) so the model can learn the patterns relevant to the target use case. You then choose a base model and decide on the finetuning method. Full finetuning retrains all parameters but requires massive compute resources, while parameter-efficient (PEFT) methods like LoRA or adapters adjust only a small subset of parameters, making training faster and lighter.

Next, the model is trained using frameworks like PyTorch or HuggingFace Transformers with carefully chosen hyperparameters. Once training is complete, the model is validated against a test set to check accuracy and consistency. If the results are good, the finetuned model can be deployed, often wrapped in an API or Docker container, making it ready to use in real-world applications.

---