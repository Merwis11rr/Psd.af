# Contributing to PSD.af

Thank you for your interest in contributing to PSD.af! This document provides guidelines for contributing to this Persian design portfolio project.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Include detailed steps** to reproduce the issue
4. **Provide screenshots** if applicable for UI issues

### Suggesting Features

1. **Check the roadmap** in README.md first
2. **Use the feature request template**
3. **Provide use cases** and examples
4. **Consider the Persian/RTL context** of the application

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch** from `develop`
3. **Make your changes** following our coding standards
4. **Write tests** for new functionality
5. **Update documentation** if needed
6. **Submit a pull request**

## 📋 Development Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 13+
- Node.js 16+ (for frontend tooling)
- Git

### Local Development
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/psd-af-portfolio.git
cd psd-af-portfolio

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials

# Initialize database
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Add sample data
python -c "from routes import create_sample_data; create_sample_data()"

# Run the application
python main.py
```

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```

## 🎨 Coding Standards

### Python Code Style
- Follow **PEP 8** conventions
- Use **type hints** for function parameters and return values
- Maximum line length: **88 characters** (Black formatter)
- Use **descriptive variable names** in both English and Persian contexts

### Persian Language Guidelines
- Use **proper Persian typography** (Persian digits, punctuation)
- Maintain **RTL text direction** in all UI elements
- Use **Vazirmatn font** for Persian text
- Follow **Persian UI/UX conventions**

### Database Guidelines
- Use **descriptive table and column names**
- Add **proper indexes** for frequently queried columns
- Include **database migrations** for schema changes
- Use **soft deletes** instead of hard deletes where appropriate

### Frontend Guidelines
- Use **semantic HTML5** elements
- Maintain **Bootstrap RTL** structure
- Ensure **responsive design** for all screen sizes
- Follow **accessibility guidelines** (WCAG 2.1)

### CSS/SCSS Guidelines
- Use **CSS custom properties** for theme colors
- Follow **BEM methodology** for class naming
- Maintain **RTL-specific styles** in separate files
- Use **mobile-first** media queries

## 📝 Commit Message Format

Use the following format for commit messages:

```
type(scope): brief description

Detailed description if needed

Fixes #issue_number
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat(portfolio): add image upload functionality

Add ability to upload multiple images for portfolio items
with automatic resizing and optimization.

Fixes #123
```

## 🔀 Pull Request Process

1. **Update your fork** with the latest changes from `develop`
2. **Create a feature branch** with a descriptive name
3. **Make your changes** with proper tests and documentation
4. **Test thoroughly** on different devices and browsers
5. **Submit PR** with detailed description and screenshots
6. **Address review feedback** promptly

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Manual testing completed
- [ ] Cross-browser testing done

## Screenshots
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🐛 Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Screenshots
[Add screenshots if applicable]

## Environment
- OS: [e.g., Windows 10, macOS 12]
- Browser: [e.g., Chrome 95, Safari 15]
- Screen size: [e.g., Desktop 1920x1080, Mobile 375x667]
- Language: [Persian, English]
```

## ✨ Feature Request Template

```markdown
## Feature Summary
Brief description of the requested feature

## Use Case
Why is this feature needed?

## Detailed Description
Detailed explanation of the feature

## Alternative Solutions
Other ways to solve this problem

## Additional Context
Any other relevant information
```

## 📚 Documentation Guidelines

### Code Documentation
- Add **docstrings** to all functions and classes
- Include **type hints** for better code clarity
- Document **complex algorithms** with inline comments
- Provide **usage examples** for new features

### API Documentation
- Document all **route endpoints**
- Include **request/response examples**
- Specify **authentication requirements**
- List **error codes** and their meanings

### User Documentation
- Write in **clear, simple language**
- Provide **step-by-step instructions**
- Include **screenshots** for UI features
- Maintain **both Persian and English** versions

## 🔒 Security Guidelines

### Code Security
- **Validate all inputs** from users
- Use **parameterized queries** to prevent SQL injection
- **Sanitize output** to prevent XSS attacks
- Implement **proper authentication** and authorization

### Data Security
- **Encrypt sensitive data** at rest and in transit
- Follow **GDPR compliance** for user data
- Implement **proper session management**
- Use **secure password hashing** (bcrypt)

### Infrastructure Security
- Keep **dependencies updated**
- Use **environment variables** for secrets
- Implement **rate limiting**
- Add **security headers** to responses

## 🚀 Release Process

### Version Numbers
Follow **Semantic Versioning** (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Release Steps
1. Update version in `__init__.py`
2. Update `CHANGELOG.md`
3. Create release branch
4. Test thoroughly
5. Merge to `main`
6. Tag the release
7. Deploy to production

## 📞 Getting Help

### Community Support
- **GitHub Discussions** for general questions
- **Issues** for bug reports and feature requests
- **Discord/Telegram** for real-time chat

### Code Review
- All PRs require **at least one review**
- **Persian language review** for UI changes
- **Security review** for authentication/authorization changes
- **Performance review** for database/API changes

## 🎯 Project Priorities

### High Priority
- **User experience** improvements
- **Performance** optimizations
- **Security** enhancements
- **Accessibility** compliance

### Medium Priority
- **New features** from roadmap
- **Code quality** improvements
- **Documentation** updates
- **Testing** coverage

### Low Priority
- **Nice-to-have** features
- **Experimental** functionality
- **Legacy code** cleanup

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **Project website** credits page
- **Social media** acknowledgments

Thank you for contributing to PSD.af! 🙏

---

**Note**: This project serves the Persian design community. Please be mindful of cultural contexts and Persian language conventions when contributing.