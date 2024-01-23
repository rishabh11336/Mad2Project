import os
from json import dumps
from httplib2 import Http
from jinja2 import Template
from datetime import datetime



def create_html_report(user, orders, total_expenditure):
    # Load HTML template (assuming you have an HTML template file)
    template = """
<!DOCTYPE html>
<html>
<head>
    <title>Monthly Activity Report</title>
    <style type="text/css">
        body { font-family: Arial, sans-serif; }
        .container { width: 100%; max-width: 600px; margin: auto; }
        .header { background-color: #4CAF50; padding: 10px; text-align: center; color: white; }
        .content { background-color: #ffffff; padding: 20px; }
        .footer { background-color: #333; padding: 10px; text-align: center; color: white; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
        th { background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://raw.githubusercontent.com/namansehwal/Assets/main/login.webp" alt="Larder Vault Logo" style="max-width: 100px;"/>
            <h2>Larder Vault Monthly Activity Report</h2>
        </div>
        <div class="content">
            <p>Dear {{ user.username | upper  }},</p>
            <p>Here is your activity report for the month.</p>

            <h3>Order Summary</h3>
            <table>
                <tr>
                    <th>Order ID</th>
                    <th>Date</th>
                    <th>Total</th>
                </tr>
                {% for order in orders %}
                <tr>
                    <td>{{ order.id }}</td>
                    <td>{{ order.created_at }}</td>
                    <td>₹{{ order.total }}</td>
                </tr>
                {% endfor %}
            </table>

            <p><strong>Total Expenditure:</strong> ₹{{ total_expenditure }}</p>
        </div>
        <div class="footer">
            <p>Thank you for shopping with Larder Vault.</p>
        </div>
    </div>
</body>
</html>

"""

    # Render the template with the user's data
    html_report = Template(template).render(user=user, orders=orders, total_expenditure=total_expenditure)

    return html_report


def create_html_reminder(user):
    # Load HTML template (assuming you have an HTML template file)
    template = """
<!DOCTYPE html>
<html>
<head>
    <title>Reminder</title>
    <style type="text/css">
        body { font-family: Arial, sans-serif; }
        .container { width: 100%; max-width: 600px; margin: auto; }
        .header { background-color: #4CAF50; padding: 10px; text-align: center; color: white; }
        .content { background-color: #ffffff; padding: 20px; }
        .footer { background-color: #333; padding: 10px; text-align: center; color: white; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
        th { background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://raw.githubusercontent.com/namansehwal/Assets/main/login.webp" alt="Larder Vault Logo" style="max-width: 100px;"/>
            <h2>Larder Vault Reminder</h2>
        </div>
        <div class="content">
            <p>Dear {{ user.username | upper  }},</p>
            <p>You have not visited our store today. Please visit us soon.</p>
        </div>
        <div class="footer">
            <p>Thank you for shopping with Larder Vault.</p>
        </div>
    </div>
</body>
</html>

"""

    # Render the template with the user's data
    html_reminder = Template(template).render(user=user)

    return html_reminder

def google_chat_webhook(user):
    """Google Chat incoming webhook with a card message resembling an HTML template."""
    url = "https://chat.googleapis.com/v1/spaces/AAAA7MSq7Cw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=6qGFxBH5DrboF2epaqFr_m8xFx1iUEMafNgRdQrxnR0"

    # Replace with actual user information
    username = user

    card_message = {
        "cards": [
            {
                "header": {
                    "title": "Larder Vault Reminder",
                    "imageUrl": "https://raw.githubusercontent.com/namansehwal/Assets/main/login.webp",
                    "imageStyle": "IMAGE"
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "textParagraph": {
                                    "text": f"<b><font color=\"#4CAF50\">Dear {username.upper()},</font></b>"
                                }
                            },
                            {
                                "textParagraph": {
                                    "text": "You have not visited our store today. Please visit us soon."
                                }
                            }
                        ]
                    }
                ]
            },
            
        ]
    }

    message_headers = {"Content-Type": "application/json; charset=UTF-8"}

    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(card_message),
    )
    if response[0].status == 200:
        print("Message successfully posted to Google Chat for user: ", username)