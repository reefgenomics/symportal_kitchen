# symportal_kitchen
Python package as a collection of functions to maintain SymPortal Web Application and Computation Framework

# Developer Guide

## Get Started

Prepare `.env` file:

```commandline
SENDGRID_API_KEY=''
SENDGRID_EMAIL_SENDER=''
```

Run tests:

```commandline
poetry run pytest --cov=symportal_kitchen tests
```

## Code Reformatting and Style Checks

### Run Formatter

```commandline
poetry run black symportal_kitchen
poetry run autopep8 --recursive --in-place symportal_kitchen
```

### Run Linter

```commandline
poetry run flake8 symportal_kitchen
poetry run pylint symportal_kitchen
poetry run mypy symportal_kitchen
```

# Usage

Use the function in Python Console:

```python
from symportal_kitchen.email_notifications.submission_status import send_email

send_email('john_doe@company.com', 'test_submission_status')
```

# About

The package was written by Yulia Iakovleva [yulia.iakovleva@uni-konstanz.de](yulia.iakovleva@uni-konstanz.de).