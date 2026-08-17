# 🚀 Enterprise QA Automation Framework

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-UI_Testing-2EAD33.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-Test_Runner-0A9EDC.svg)](https://docs.pytest.org/en/latest/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)](https://github.com/features/actions)

A production-grade, full-stack test automation framework built to validate the [Practice Software Testing](https://practicesoftwaretesting.com/) application. 

This framework demonstrates a **Layer-Driven Architecture**, separating the UI, API, and Database execution layers to ensure high maintainability, rapid execution, and robust isolation of concerns.

## 🏗️ Architectural Highlights

* **Layer-Driven Structure:** Test files only contain business logic and assertions. Complex interactions are abstracted into the `api_clients`, `page_objects`, and `core` engine layers.
* **API Engine (Requests):** Implements the Base Client pattern with automated connection pooling, HTTP adapter retries for network blips, and JSON Schema contract validation.
* **UI Engine (Playwright):** Implements the Page Object Model (POM) using tag-agnostic `data-test` locators. Strictly utilizes Playwright's auto-retrying `expect()` assertions to eliminate Single Page Application (SPA) race conditions natively.
* **Database Integration (SQLAlchemy):** Cross-layer End-to-End (E2E) testing validates that UI/API actions are accurately persisted in the MariaDB backend, including security checks (e.g., verifying password hashes).
* **Dynamic Data (Faker):** Test data is generated dynamically at runtime to prevent database collision and ensure tests are stateless and repeatable.
* **Strict Configuration (Pydantic):** Environment variables are strictly typed and validated at runtime startup, preventing deep-execution failures caused by missing `.env` variables.

## 📁 Repository Structure

```text
├── .github/workflows/      # CI/CD Ephemeral Environment Pipelines
├── api_clients/            # API Engine (Base Client, Auth, Products)
├── page_objects/           # UI Engine (Playwright POMs)
├── core/                   # Centralized Config, DB Connections, Logging
├── data/                   # JSON Schemas, Static Payloads, Data Factories
├── tests/                  # Test Execution Layer
│   ├── api/                # Isolated API contract and functional tests
│   ├── ui/                 # Isolated RBAC UI tests
│   └── e2e/                # Cross-layer integration tests
├── .env.example            # Environment configuration template
├── conftest.py             # Global Pytest fixtures and dependency injection
└── pytest.ini              # Pytest execution markers and reporting configs