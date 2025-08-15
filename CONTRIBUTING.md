 
# Contributing to Your Project Name

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please use the bug report template and include as many details as possible.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please use the feature request template and provide as much detail as possible.

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through `beginner` and `help-wanted` issues:

- **Beginner issues** - issues which should only require a few lines of code
- **Help wanted issues** - issues which should be a bit more involved

### Pull Requests

1. **Fork** the repo and create your branch from `main`
2. **Install development dependencies**: `pip install -r requirements/dev.txt`
3. **Install the package in development mode**: `pip install -e .`
4. **Make your changes** and add tests if applicable
5. **Ensure tests pass**: `pytest`
6. **Ensure code quality**: `black src/ tests/`, `flake8 src/ tests/`, `mypy src/`
7. **Update documentation** if needed
8. **Create a Pull Request** using the PR template

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-project.git
   cd your-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements/dev.txt
   pip install -e .
   ```

4. Install pre-commit hooks (optional but recommended):
   ```bash
   pre-commit install
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run specific test file
pytest tests/test_main.py
```

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **Flake8** for linting
- **isort** for import sorting
- **mypy** for type checking

Run these tools before submitting:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/
```

### Running the Application

```bash
# Run the main module
python -m geo_green.main

# Or run directly
python src/geo_green/main.py
```

## Project Structure

```
your-project/
├── .github/                 # GitHub-specific files
│   ├── workflows/          # GitHub Actions
│   └── ISSUE_TEMPLATE/     # Issue templates
├── src/geo_green/   # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── requirements/           # Dependencies
├── pyproject.toml          # Project configuration
├── README.md              # Project overview
└── CONTRIBUTING.md        # This file
```

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation changes
- `style:` formatting, missing semi colons, etc
- `refactor:` code refactoring
- `test:` adding tests
- `chore:` maintenance tasks

Examples:
```
feat: add user authentication
fix: resolve database connection timeout
docs: update installation instructions
```

## Branching Strategy

- `main` - Production-ready code
- `develop` - Development branch (if using)
- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `hotfix/critical-fix` - Critical production fixes

## Questions?

Feel free to create an issue with the "question" label if you have any questions about contributing!