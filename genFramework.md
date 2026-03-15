
# Autogen Framework

## 1. Agents and Roles
- **Agent1 (Agent Testing)**: Primary agent or system under test.
- **AssistantAgent**: Acts as a helper or AI assistant in the system.
- **UserProxyAgent**: Simulates a user, generating messages or input for testing.

*Use case:* Testing AI behaviors, debugging multi-agent interactions, simulating conversations.

---

## 2. Chat Modes

### RoundRobinChat
- Each agent takes turns sending messages in a fixed sequence.
- Ideal for structured conversations where every agent contributes equally.

### SelectorGroupChat
- A subset of agents is selected for each turn, possibly based on conditions or priorities.
- Useful for scenario-based simulations where not all agents need to speak every turn.

---

## 3. Termination Conditions

- **Max Termination Chat Messages**: Stop the conversation after a predefined number of messages (e.g., 20 messages).
- **Participants**: Define which agents are participating in the chat session.
- **Termination Condition**: Can be based on:
  1. Number of messages.
  2. Reaching a goal or consensus.
  3. Specific keyword or trigger in conversation.
  4. Time limit or cycles of turns.

---
