# symportal_kitchen
Python package as a collection of functions to maintain SymPortal Web Application and Computation Framework

# Get Started

Prepare `.env` file

```commandline
SENDGRID_API_KEY=''
SENDGRID_EMAIL_SENDER=''
```

# Usage

Use the function in Python Console

```python
from symportal_kitchen.email_notifications.submission_status_update import send_email
send_email('john_doe@company.com', 'test_submission_status')
```
