# Contributing Guidelines

Thank you for your interest in contributing to the Sales Analysis Dashboard project! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and constructive in all interactions
- Focus on code quality and project goals
- Welcome diverse perspectives and ideas

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Development Environment

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Python_sales_project.git
   cd Python_sales_project
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Coding Standards

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Keep functions focused and concise
- Add docstrings to classes and functions
- Maximum line length: 100 characters

### Documentation
- Add comments for complex logic
- Update README.md for user-facing changes
- Document new functions with docstrings
- Include type hints where appropriate

### Testing
- Test your changes thoroughly
- Ensure existing functionality isn't broken
- Add test cases for new features

## Commit Guidelines

### Commit Messages
- Use clear, descriptive commit messages
- Format: `[TYPE] Subject line (50 chars max)`

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

**Example:**
```
feat: Add export to PDF functionality

- Implement PDF export using reportlab
- Add PDF option to export menu
- Update documentation
```

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes and commit with clear messages
3. Push to your fork: `git push origin feature/your-feature-name`
4. Create a Pull Request with a detailed description
5. Address feedback and make requested changes
6. Ensure all tests pass before merging

## Reporting Issues

### Bug Reports
Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Python and library versions
- Error messages or screenshots

### Feature Requests
Include:
- Clear description of the feature
- Use cases and benefits
- Proposed implementation (if applicable)
- Related issues or similar features

## Questions or Need Help?

- Check existing issues and documentation first
- Open a new issue with detailed questions
- Contact the maintainers for guidance

Thank you for contributing!
