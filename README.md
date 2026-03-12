# SAMN

## Decentralized Working Memory Layer for AI Agents

![version](https://img.shields.io/badge/version-1.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![blockchain](https://img.shields.io/badge/blockchain-Aptos-purple)
![storage](https://img.shields.io/badge/storage-Shelby-orange)

SAMN is a decentralized infrastructure layer that provides persistent working memory for autonomous AI agents.

By combining ultra-fast decentralized storage with blockchain verification, SAMN enables agents to store, retrieve, and share knowledge without relying on centralized servers.

---

# Why SAMN

Modern AI agents rely heavily on centralized infrastructure to maintain conversation history and contextual memory.

If the server disappears, the agent effectively loses its memory.

SAMN introduces a decentralized working memory system where AI agents can maintain persistent state across sessions and environments.

This unlocks a new paradigm for collaborative AI systems.

---

# Core Idea

Instead of storing memory directly on-chain, SAMN uses a hybrid architecture.

High-frequency data is stored in fast decentralized storage, while the blockchain manages ownership and access control.

```
AI Agent
   │
   │ generate memory
   ▼
Shelby Hot Storage
   │
   │ store chat logs + embeddings
   ▼
Aptos Smart Contract
   │
   │ store pointer (CID)
   ▼
Other AI Agents
```

---

# Key Features

### Persistent AI Memory

Agents can store conversation history and vector embeddings permanently.

### Sub-Second Retrieval

Shelby hot storage allows memory queries with extremely low latency.

### On-Chain Ownership

Memory pointers are verified using smart contracts.

### Knowledge Monetization

Agents can monetize datasets through pay-per-read models.

### Agent-to-Agent Learning

AI agents can access shared knowledge pools.

---

# Repository Structure

```
samn-memory-layer

contracts/
    agent_memory.move

scripts/
    shelby_memory_client.py
    agent_cli.py
    memory_indexer.py

docs/
    architecture.md

examples/
    sample_memory.json

Move.toml
requirements.txt
README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourname/samn-memory-layer
cd samn-memory-layer
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Quick Start

Store a new memory entry

```
python scripts/agent_cli.py store "Hello agent" "Hi there"
```

Execution flow

1. Memory JSON is generated
2. Data is uploaded to Shelby storage
3. Memory pointer is updated on Aptos

---

# Example Memory Object

```
{
  "agent_id": "0xAgent",
  "timestamp": 1710000000,
  "content": {
    "user": "Explain decentralized storage",
    "ai": "Shelby provides fast decentralized hot storage."
  }
}
```

---

# Smart Contract Overview

The Move contract stores memory pointers and enforces access control.

Functions

initialize_agent
update_memory
get_memory

This allows AI agents to verify ownership of their memory data.

---

# Benchmark (Conceptual)

| Storage  | Latency | Use Case         |
| -------- | ------- | ---------------- |
| Shelby   | <1s     | AI agent memory  |
| Filecoin | minutes | archival storage |
| Arweave  | seconds | permanent files  |

SAMN uses Shelby because AI conversations require near real-time data access.

---

# Development Roadmap

Phase 1 — Infrastructure

smart contract deployment
memory client implementation
Shelby storage integration

Phase 2 — AI Integration

vector embedding storage
AI agent memory pipeline
memory indexing

Phase 3 — AI Knowledge Network

agent knowledge marketplace
pay-per-read datasets
collaborative AI learning

---

# Developer Guide

Deploy contract

```
aptos move compile
aptos move publish
```

Run memory client

```
python scripts/agent_cli.py test
```

---

# Future Vision

SAMN aims to become a decentralized memory layer powering autonomous AI systems across Web3 ecosystems.

This infrastructure could support:

• AI trading agents
• decentralized assistants
• autonomous research bots
• collaborative AI networks

---

# License

MIT License
## Demo

Run AI agent simulation

python scripts/agent_cli.py demo

Run storage benchmark

python scripts/agent_cli.py benchmark
