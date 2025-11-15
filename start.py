from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

# ------------------------
# Logging configuration
# ------------------------
logging.basicConfig(
    filename='bot_activity.log',    # Log file
    level=logging.INFO,             # Info + warnings + errors
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to log both requests and bot events
def log_event(event_type, message):
    logging.info(f"[{event_type}] {message}")
    print(f"[{event_type}] {message}")  # Also print to console

# ------------------------
# HTTP request logging
# ------------------------
@app.before_request
def log_request():
    ip = request.remote_addr
    path = request.path
    method = request.method
    log_event("HTTP_REQUEST", f"{ip} requested {path} via {method}")

# ------------------------
# Bot endpoints
# ------------------------
@app.route("/")
def home():
    log_event("BOT_EVENT", "Homepage accessed")
    return "Auto-Approval Bot is running!"

@app.route("/approve/<username>")
def approve_user(username):
    # Simulate approval process
    log_event("BOT_EVENT", f"User approved: {username}")
    return f"✅ User {username} approved!"

# ------------------------
# Error logging
# ------------------------
@app.errorhandler(Exception)
def handle_exception(e):
    log_event("ERROR", str(e))
    return "An error occurred", 500

# ------------------------
# Run server
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
