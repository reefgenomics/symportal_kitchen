import os
import unittest
from dotenv import load_dotenv
from unittest.mock import patch
from symportal_kitchen.email_notifications.submission_status import send_email

# Load environment variables from .env file
load_dotenv()

SENDGRID_EMAIL_SENDER = os.environ.get("SENDGRID_EMAIL_SENDER")


class TestSendEmail(unittest.TestCase):
    # These are the class attributes shared among all test methods in the class
    to_email = "test@example.com"
    submission_status = "test_submission_status"

    def test_send_email_success(self):
        # Test sending email with a successful response
        result = send_email(self.to_email, self.submission_status)
        self.assertTrue(result)

    @patch(
        "symportal_kitchen.email_notifications.submission_status_update."
        "SendGridAPIClient"
    )
    def test_send_email_failure(self, mock_sendgrid):
        # Mock the SendGridAPIClient to raise an exception,
        # simulating a failed email sending
        mock_sendgrid.return_value.send.side_effect = Exception("Send failed!")
        result = send_email(self.to_email, self.submission_status)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
