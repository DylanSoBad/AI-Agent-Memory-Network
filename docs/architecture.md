# SAMN Architecture

SAMN provides decentralized working memory for AI agents.

System Flow

AI Agent
   │
   │ generate conversation memory
   ▼
Memory Client
   │
   │ upload JSON memory
   ▼
Shelby Hot Storage
   │
   │ return CID
   ▼
Aptos Smart Contract
   │
   │ store pointer
   ▼
Other Agents retrieve memory
