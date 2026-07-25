# Architecture

## End-to-end flow

1. User sends a natural language spending question through the mobile chat UI.
2. FastAPI receives the request and passes it to the Orchestrator.
3. The Agent Loop sends conversation context and available tool definitions to the LLM adapter.
4. The LLM decides whether a tool call is required.
5. Tool Registry executes the requested transaction analysis function.
6. Tool results are returned back into the agent context.
7. The agent produces a user-friendly financial insight.
8. The response is returned to the mobile UI.

Schema:
                         User
                           |
                           v
                  Mobile Chat UI
                           |
                           v
                    FastAPI API
                           |
                           v
                     Guard Layer
                           |
                           v
                  Conversation Orchestrator
                           |
                           v
                    Agent Runtime
                           |
              +------------+-------------+
              |                          |
              v                          v
        LLM Provider              Tool Execution Layer
              |                          |
              v                          v
   Reasoning + Tool Selection     Finance Data Tools
                                         |
                                         v
                              Enriched Transactions CSV
                                         |
                                         v
                                Tool Result
                                         |
                                         v
                                  Agent Runtime
                                         |
                                         v
                              Final Financial Insight
                                         |
                                         v
                              Mobile Chat UI


## Components

### Guard Layer

Responsible for:
- enforcing safety boundaries before and after agent execution
- detecting prompt injection attempts
- preventing unsupported banking actions outside the PFM scope

Current protections:
- blocks requests attempting to reveal system instructions
- blocks requests asking the agent to perform payments or money transfers
- validates that generated responses are not empty

The guard layer ensures the assistant remains focused on spending analysis and financial insights rather than account operations.

### Agent Runtime

Responsible for:
- maintaining conversation loop
- deciding when tools are needed
- generating final responses
- coordinating LLM responses with tool execution

### Tool Registry

Responsible for:
- exposing available finance tools
- executing transaction queries
- providing structured results back to the agent runtime

Available tools include:
- spending by category
- top spending categories
- subscription detection
- period comparison

### Transaction Repository

Responsible for:
- loading transaction data
- providing structured records
- serving as the data source for finance analysis tools