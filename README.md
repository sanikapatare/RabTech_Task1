# RabTech Diagnostic CLI

## Task 1 - Python Software Engineering Internship

This project is an installable Python command-line tool that performs basic diagnostic checks on a development environment.

## Features

The CLI checks:

- Python version
- Operating system and platform
- Available disk space
- Environment variables
- Configured developer tools such as Git, Python, pip, and VS Code
- JSON configuration files
- Human-readable reports
- Structured JSON reports
- Useful exit codes

## Project Structure

```text
RabTech_Task1/
│
├── rabtech_diagnostic/
│   ├── __init__.py
│   └── cli.py
│
├── tests/
│   └── test_cli.py
│
├── config.json
├── diagnostic-events.json
├── sample-report.json
├── pyproject.toml
├── analyze_events.py
└── README.md