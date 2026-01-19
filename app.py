from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
)

mail = Mail(app)

# Example predefined groups
RECIPIENT_GROUPS = {
    "All Members": [
        "f20220233@dubai.bits-pilani.ac.in",
        "f20220234@dubai.bits-pilani.ac.in"
    ],
    "Core Team": [
        "core1@dubai.bits-pilani.ac.in",
        "core2@dubai.bits-pilani.ac.in"
    ]
}

@app.route("/")
def index():
    return render_template("index.html", groups=RECIPIENT_GROUPS)

@app.route("/send", methods=["POST"])
def send_email():
    to = request.form.get("to", "").split(",")
    cc = request.form.get("cc", "").split(",")
    bcc = request.form.get("bcc", "").split(",")
    subject = request.form.get("subject")
    body = request.form.get("body")

    msg = Message(
        subject=subject,
        sender=app.config["MAIL_USERNAME"],
        recipients=[e for e in to if e],
        cc=[e for e in cc if e],
        bcc=[e for e in bcc if e],
        html=body
    )

    # Attachments
    files = request.files.getlist("attachments")
    for file in files:
        if file.filename:
            msg.attach(
                file.filename,
                file.content_type,
                file.read()
            )

    mail.send(msg)
    return render_template("sent.html")
