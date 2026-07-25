# Penny - Conversational PFM Agent

## Overview

Penny is an AI-powered personal finance assistant that helps users understand their spending through natural language conversations.

## Demo

Demo video:

![Watch the demo](./assets/Demo.gif)

## Note on LLM Integration

The assignment requires a live LLM integration. The project was structured with a provider abstraction layer to allow seamless integration with OpenAI, Anthropic, or another LLM provider.

Because an external provider API key was not available during development, the repository focuses on demonstrating the complete agent architecture:

- conversation orchestration
- tool selection flow
- transaction-grounded responses
- frontend integration
- mobile-style chat experience

Replacing the adapter implementation with a live provider requires only adding the provider-specific client and environment configuration.

## Features

- Spending analysis
- Top spending categories
- Subscription detection
- Period comparison
- Tool-based transaction analysis

## Architecture

See ARCHITECTURE.md

## Tech Stack

Backend:

- Python
- FastAPI
- Custom agent runtime
- Tool calling architecture

Frontend:

- React
- TypeScript
- Mobile phone UI

Data:

- Enriched transaction dataset

## Implemented User Stories

### Spending analysis ✅

Question:
"How much did I spend on groceries?"

Tool:
`get_spending_by_category()`

---

### Top spending categories ✅

Question:
"What are my top categories this month?"

Tool:
`get_top_categories()`

---

### Recurring charges ✅

Question:
"Show me my subscriptions"

Tool:
`get_subscriptions()`

---

### Trend analysis ✅

Question:
"Compare my spending this month and last month"

Tool:
`compare_periods()`

---

### Merchant insight ✅

Question:
"Which merchant do I spend the most at?"

Tool:
`get_top_merchants()`

---

## Not Implemented User Stories

### Savings goal tracking ❌

Requires:
- user-defined savings goals
- account balance
- savings history

---

### Income-to-budget ratio ❌

Requires:
- income information
- budget configuration

---

### Balance forecasting ❌

Requires:
- current account balance
- future income
- recurring expense data

## Run

Prepare environment variables for:

- agent/.env
- frontend/.env

The application can be started in two ways.

### Option 1: Run with Docker

Docker will install dependencies and start the application.

```bash
docker compose -f docker/docker-compose.yml up
```

### Option 2: Run locally

Install dependencies:

```bash
poetry install
```

Start the application:

```bash
poetry run pystart
```

## Requirements

- Python 3.13+
- Docker (optional)

## Tests

Install dependencies:

```bash
poetry install
```

Run tests:

```bash
poetry run pytest
```

## Potential improvements

- Add tool permissions.
  - Currently, all registered tools are available to the agent. A permission layer could restrict which tools can be used depending on the user, agent, or context.

- Add CI pipeline.
  - Introduce automated checks for pull requests, including linting, tests, and basic validation to ensure code quality and prevent regressions.

- Add complete test coverage for agent and frontend.
