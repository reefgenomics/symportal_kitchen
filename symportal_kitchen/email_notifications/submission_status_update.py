import logging
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Content, TemplateId, Substitution

# Load environment variables from .env file
load_dotenv()

SENDGRID_EMAIL_SENDER = os.environ.get('SENDGRID_EMAIL_SENDER')


def read_email_template(template_name):
    template_file_path = os.path.join(os.path.dirname(__file__), 'templates', template_name)
    with open(template_file_path, 'r') as file:
        template_content = file.read()
    return template_content


def send_email(to_email, submission_status, from_email=SENDGRID_EMAIL_SENDER):
    # Prepare the dynamic content for the email template
    subject = "Status Update for Your Submission"
    substitutions = {
        "subject": subject,
        "recipient_name": to_email.split('@')[0],  # Just using the part before '@' as the recipient name
        "submission_status": submission_status
    }

    # Read the email template content from the file
    template_content = read_email_template('status_update_email_template.html').format(**substitutions)

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=template_content
    )

    # Send the email
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        if response.status_code == 202:
            logging.debug('Email sent successfully!')
            return True
        else:
            logging.error(f'Failed to send email. Status code: {response.status_code}')
            return False
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return False