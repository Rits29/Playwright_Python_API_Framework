# Playwright Python API Automation Framework

A modular, multi-protocol API automation framework built with **Python, Playwright, Pytest and Pydantic**.

Supports **REST**, **GraphQL** and **SOAP** APIs under a single reusable architecture.

---

### Badges

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-API-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-red)

---

### Overview

This project demonstrates how to design a clean and maintainable API automation framework that can handle multiple protocols (REST, GraphQL, SOAP) using a shared foundation.

---

### Key Design Principles

- Layered architecture with clear separation of concerns
- Generic Base API Client supporting REST, GraphQL and SOAP
- Pydantic models for request and response validation
- Factory pattern for payload generation
- Centralized validation utilities
- Structured logging with sensitive data masking
- HTML reporting with pytest-html
- Config-driven environment management

---

### Architecture Overview

| Application        | Protocol | Status |
| ------------------ | -------- | ------ |
| Library Management | REST     | ✅     |
| EventHub           | REST     | ✅     |
| GraphQL Demo       | GraphQL  | ✅     |
| SOAP Calculator    | SOAP     | ✅     |

---

# 📈 Design Decisions

Several deliberate choices were made while designing this framework:

- Single Base API Client:
- Pydantic for both Request and Response:
A shared base client was preferred over protocol-specific base classes to keep request handling consistent across REST, GraphQL and SOAP.
Pydantic models are used not only for generating payloads but also for validating response structure. This provides early detection of contract changes.
- Factory Pattern for Test Data:
Dynamic data generation is handled through factories instead of static JSON files. This reduces test data conflicts and improves test independence.
- Centralized Validation Layer:
Common assertions (status code, schema, keys, messages, XML) are kept in one place to avoid duplication across test cases.
- Sensitive Data Masking in Logs:
Tokens, passwords and authorization headers are automatically masked in logs to make the framework safer for real project usage.
- Playwright APIRequestContext:
Playwright was chosen because it provides a modern and reliable request context with good support for headers, timeouts and response handling.
- Layered Architecture:
Clear separation between Tests, API Clients, Payload generation and Validation was maintained to improve long-term maintainability.

---

# Limitations
This project is intentionally focused on demonstrating framework design and architecture rather than exhaustive functional coverage.
The APIs used are publicly available practice endpoints and serve only as a vehicle to showcase multi-protocol automation patterns, layered design, and reusable components.

---

# 🏗️ Framework Architecture

The framework is organized into independent layers, where each layer has a single responsibility. This keeps business workflows, request execution, payload generation and validations loosely coupled and easier to maintain.

```
                     Test Cases
                         │
                         ▼
                 API Client Layer
                         │
                         ▼
                Payload Factory Layer
                         │
                         ▼
              Pydantic Request Models
                         │
                         ▼
                  Base API Client
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
      REST           GraphQL            SOAP
        │                │                │
        └────────────────┼────────────────┘
                         ▼
              Playwright API Context
                         │
                         ▼
                    Target API
                         │
                         ▼
                Validation Layer
                         │
                         ▼
                 Logging & Reporting
```

---

# 📂 Project Structure

```bash
PLAYWRIGHT_PYTHON_API_FRAMEWORK
│
├── api_clients/
│   ├── base_api_client.py
│   ├── library_api_client.py
│   ├── eventhub_api_client.py
│   ├── graphql_api_client.py
│   └── soap_api_client.py
│
├── payloads/
│   ├── generators/
│   ├── models/
│   └── randomdatagenerator.py
│
├── utilities/
│   ├── api_validation.py
│   ├── custom_logger.py
│   ├── log_utils.py
│   └── read_properties.py
│
├── tests/
│   ├── Library_Management_REST_API_Tests/
│   ├── Event_Hub_REST_API_Tests/
│   ├── Graphql_Tests/
│   ├── Soap_API_Tests/
│   └── conftest.py
│
├── reports/
├── logs/
├── config.ini
├── pytest.ini
└── README.md
```

---

# ⚙️ Core Components Explained

## ✅ Base API Client

Supports common HTTP methods including:

- GET
- POST
- PUT
- PATCH
- DELETE

and provides a single request execution layer shared across REST, GraphQL and SOAP clients.

📌 **Why?**

Avoids duplicate request handling across different applications.

---

## ✅ Payload Factory

Responsible for generating reusable payloads through Pydantic models.

```
Random data Generator
       │
       ▼
Pydantic Model
       │
       ▼
generate()
       │
       ▼
serialize()
       │
       ▼
API Client
```

📌 **Why?**

Keeps payload generation centralized and reusable.

---

## ✅ Pydantic Models

Used for

- Request Models
- Response Models
- Schema Validation

📌 **Why?**

Provides strong typing and automatic response validation.

---

## ✅ Centralized Validation

Common validations include

- Status Code
- Response Schema
- Required Keys
- Success Messages
- XML Validation
- Business Rule Validation

📌 **Why?**

Promotes reusable validation logic across all APIs.

---

## ✅ Structured Logging

Logs include

- Test Name
- API Name
- HTTP Method
- Endpoint
- Request Payload
- Response Body
- Status Code
- Response Time

Sensitive fields like

- Password
- Token
- Authorization

are automatically masked.

---

## ✅ HTML Reporting

Framework generates execution reports using **pytest-html**.

Provides

- Test Summary
- Execution Duration
- Pass / Fail Statistics
- Captured Logs

---

# 🔄 Execution Flow

```
pytest
   │
   ▼
conftest.py
   │
   ▼
Playwright API Context
   │
   ▼
Test Case
   │
   ▼
API Client
   │
   ▼
Payload Factory
   │
   ▼
Pydantic Model
   │
   ▼
serialize()
   │
   ▼
Base API Client
   │
   ▼
HTTP Request
   │
   ▼
Playwright APIRequestContext
   │
   ▼
Validation Layer
   │
   ▼
Logger
   │
   ▼
HTML Report
```

---

# 📖 Business Workflow Examples

## 📚 Library Management Workflow

```
Generate Book Payload
        │
        ▼
POST Add Book
        │
        ▼
Validate Response
        │
        ▼
Extract Book ID
        │
        ▼
POST Delete Book
        │
        ▼
Validate Response
        │
        ▼
PASS
```

---

## 🎫 EventHub Management Workflow

```
Register User
      │
      ▼
Login
      │
      ▼
Extract JWT Token
      │
      ▼
Create Event
      │
      ▼
Validate Response
      │
      ▼
PASS
```

---

## 🌐 GraphQL Query Workflow

```
Generate Mutation
       │
       ▼
Generate Variables
       │
       ▼
POST Request
       │
       ▼
Validate Response
       │
       ▼
PASS
```

---

## 🧾 SOAP Service Workflow

```
Generate XML Request
        │
        ▼
POST SOAP Request
        │
        ▼
Parse XML
        │
        ▼
XPath Validation
        │
        ▼
PASS
```

---

# ▶️ How to Execute

### Clone Repository

```bash
git clone <repository-url>
cd Playwright_Python_API_Framework
pip install -r requirements.txt
```

### Execute All Tests

```bash
pytest -v
```

### Generate HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

### Execute Against Specific Environment

```bash
pytest --env=QA
```

---

# 📊 Reporting & Logs

The framework captures both execution logs and HTML reports to help trace requests, responses and validation outcomes during test execution.

📁 Reports → `/reports`

Reports are generated automatically after test execution using pytest-html, providing an execution summary and links to captured logs.

📁 Logs → `/logs`

Each API request is logged with the following details:

- Request Payload
- Response Body
- Response Time
- Validation Details


---

# 🚀 Future Enhancements

- OAuth2 Authentication
- JWT Refresh Workflow
- Database Validation
- GitHub Actions CI
- Allure Reporting
- Parallel Execution
- API Contract Testing

---

# 👩‍💻 Author

**Ritvika Thakur**

QA Lead | Test Automation | Quality Engineering

11+ years of experience designing test strategies, automation frameworks and API/UI test solutions across Telecom and Enterprise applications.

---

# 🧭 Repository Walkthrough

If you're reviewing this project, explore it in the following order:

1. `tests/` → Business workflows
2. `api_clients/` → API abstraction layer
3. `payloads/` → Payload generation
4. `utilities/` → Logging, validation & configuration
5. `reports/` → Execution report
6. `logs/` → Runtime logs

---

# 💬 Final Note

The goal of this project is to demonstrate how a maintainable API automation framework can be structured using reusable components, clear separation of concerns, and protocol-independent request handling.