import os
import logging
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from jinja2 import Environment, FileSystemLoader

# Load environment variables from .env file
load_dotenv()

SENDGRID_EMAIL_SENDER = os.environ.get("SENDGRID_EMAIL_SENDER")


def read_email_template(template_name):
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template


def send_email(to_email, submission_status,
               recipient_name='', from_email=SENDGRID_EMAIL_SENDER):
    if recipient_name == '':
        recipient_name = to_email.split("@")[0]
    # Prepare the dynamic content for the email template
    subject = "Status Update for Your Submission"
    substitutions = {
        "subject": subject,
        "recipient_name": recipient_name,
        "submission_status": submission_status,
    }

    # Read and render the email template
    template = read_email_template("status_update_email_template.html")
    template_content = template.render(substitutions)

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=template_content,
    )

    # Send the email
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        if response.status_code == 202:
            logging.debug("Email sent successfully!")
            return True
        else:
            logging.error(
                f"Failed to send email. Status code: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return False
