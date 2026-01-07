## MTC Messenger

A simple Flask web application to send emails using Gmail SMTP.

### Features
- Web interface to trigger sending an email.
- Uses Flask-Mail for email delivery.
- Environment variables managed with python-dotenv.

### Project Structure
- `app.py`: Main Flask application.
- `templates/`: HTML templates for the UI.
- `static/`: Static files (if any).
- `requirements.txt`: Python dependencies.

### Setup Instructions
1. **Clone the repository**
2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
3. **Configure environment variables:**
	- Create a `.env` file with your email credentials if needed.
4. **Run the app:**
	```bash
	python app.py
	```
5. **Open in browser:**
	- Visit `http://localhost:5000` to use the app.

### Dependencies
- Flask
- Flask-Mail
- python-dotenv

### Usage
1. Go to the home page and click the "Mail!" button to send a test email.
2. You will see a confirmation page when the email is sent.

---
**Note:**
This project is for demonstration purposes. Do not commit real credentials. Use environment variables for sensitive data.
