# Multi-Agent Chat Testing Flowchart.md
---
title: Multi-Agent Testing Architecture
description: Complete testing pipeline for Agent1 with chat modes and termination
---

# Multi-Agent Chat Testing Pipeline

## Architecture Flowchart

```mermaid
flowchart TB
    subgraph AGENTS["1. AGENTS & ROLES"]
        A1[🧪 Agent1<br/>System Under Test]
        A2[🤖 AssistantAgent<br/>AI Helper]
        A3[👤 UserProxyAgent<br/>User Simulator]
    end
    
    subgraph MODES["2. CHAT MODES"]
        B1[🔄 RoundRobinChat<br/>Fixed sequence<br/>Every agent speaks]
        B2[🎯 SelectorGroupChat<br/>Conditional subset<br/>Dynamic selection]
    end
    
    subgraph TERMINATION["3. TERMINATION"]
        C1[📊 Max Messages<br/>e.g. 20 rounds]
        C2[👥 Participants<br/>Agent selection]
        C3[⚙️ Triggers<br/>-  Message count<br/>-  Goal reached<br/>-  Keyword<br/>-  Time limit]
    end
    
    D[🚀 RUN SIMULATION<br/>Debug AI behaviors<br/>Test interactions]
    
    AGENTS --> MODES
    MODES --> TERMINATION
    TERMINATION --> D
    
    classDef agents fill:#e1f5fe,stroke:#01579b
    classDef modes fill:#f3e5f5,stroke:#4a148c  
    classDef term fill:#e8f5e8,stroke:#1b5e20
    classDef run fill:#fff3e0,stroke:#e65100
    
    class A1,A2,A3 agents
    class B1,B2 modes
    class C1,C2,C3 term
    class D run
