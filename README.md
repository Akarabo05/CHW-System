# 🏥 Community Health Worker Visit Reporting System

> **Course:** SENG 8240 — Best Programming Practices & Design Patterns  
> **Institution:** Adventist University of Central Africa  
> **Academic Year:** 2025/2026 | Semester II  

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Design Patterns](#-design-patterns)
- [Getting Started](#-getting-started)
- [Running with Docker](#-running-with-docker)
- [Running Tests](#-running-tests)
- [Test Accounts](#-test-accounts)
- [Phase Summary](#-phase-summary)

---

## 📌 Project Overview

A web-based reporting system for Community Health Workers (CHWs) at **Irembo Health Post, Gasabo District, Kigali**. CHWs submit patient visit reports digitally, and supervisors monitor all reports in real time through a dedicated dashboard.

---

## ❗ Problem Statement

Community Health Workers in Rwanda traditionally use paper-based reporting, leading to:
- 📄 Lost or damaged visit reports
- ⏰ Delayed data reaching supervisors
- 🚑 No real-time referral alerts for urgent cases
- 📊 No patient history tracking across visits

---

## 📁 Project Structure

```
files (2)/
│
├── app.py                  # Main Flask application (routes, logic, DB)
├── chw.db                  # SQLite database (auto-created on first run)
├── requirements.txt        # Python dependencies
│
├── templates/              # HTML templates (Jinja2)
│   ├── login.html          # Login page (CHW & Supervisor)
│   ├── chw.html            # CHW dashboard + report form
│   └── supervisor.html     # Supervisor dashboard with all reports
│
├── test_app.py             # Phase 4: Unit tests (8 test cases)
│
├── Dockerfile              # Phase 3: Docker image definition
├── docker-compose.yml      # Phase 3: Container orchestration
│
├── TEST_PLAN.md            # Phase 4: Software test plan document
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 🛠 Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python 3.11, Flask 3.0  |
| Frontend | HTML5, CSS3, Jinja2     |
| Database | SQLite (chw.db)         |
| Auth     | Flask Sessions          |
| DevOps   | Docker, Docker Compose  |
| VCS      | Git                     |
| Testing  | Python unittest         |

---

## 🧩 Design Patterns

### 1. Observer Pattern
**Where:** `app.py` → `submit_report()` route  
**How:** When a CHW submits a report with `Referred=Yes`, the supervisor dashboard is automatically notified and updates to highlight the referral in red.

### 2. Strategy Pattern
**Where:** `supervisor.html` → report rendering block  
**How:** The supervisor dashboard supports multiple viewing strategies (table view, summary stats) that share the same data interface but render differently.

### 3. Repository Pattern
**Where:** `app.py` → database functions section  
**How:** All database operations (init, insert, select) are centralized in dedicated functions, keeping route handlers clean and focused.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- pip

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
python app.py
```

Visit **http://localhost:5000** in your browser.

---

## 🐳 Running with Docker

### Build the image
```bash
docker build -t chw-system .
```

### Start the container
```bash
docker-compose up
```

### Stop the container
```bash
docker-compose down
```

The app will be available at **http://localhost:5000**

---

## 🧪 Running Tests

```bash
python test_app.py
```

Expected output:
```
test_01_login_page_loads ... ok
test_02_valid_chw_login ... ok
test_03_valid_supervisor_login ... ok
test_04_invalid_login ... ok
test_05_empty_login ... ok
test_06_chw_page_requires_login ... ok
test_07_supervisor_page_requires_login ... ok
test_08_logout_clears_session ... ok

Ran 8 tests in 0.5s
OK
```

---

## 👤 Test Accounts

| Role       | Username | Password  |
|------------|----------|-----------|
| CHW        | alice    | alice123  |
| CHW        | bob      | bob123    |
| Supervisor | admin    | admin123  |

---

## 📦 Phase Summary

| Phase | Description                        | Status |
|-------|------------------------------------|--------|
| 1     | PowerPoint documentation & UML     | ✅ Done |
| 2     | Working prototype + design patterns| ✅ Done |
| 3     | Docker + Git version control       | ✅ Done |
| 4     | Test plan + 8 passing test cases   | ✅ Done |

---

> *Built with ❤️ for SENG 8240 — Adventist University of Central Africa*
