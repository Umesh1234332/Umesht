from flask import Flask, render_template_string
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    # Your full name
    name = "Umesh T."

    # Get system username safely
    try:
        username = os.getlogin()
    except:
        username = os.environ.get("USER", "unknown")

    # Get current time in IST
    ist_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")

    # Get top output (first 10 lines)
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -n 10")
    except Exception as e:
        top_output = f"Error running top command: {e}"

    # HTML template as string
    html_template = """
    <h2>/htop Endpoint</h2>
    <p><strong>Name:</strong> {{ name }}</p>
    <p><strong>Username:</strong> {{ username }}</p>
    <p><strong>Server Time (IST):</strong> {{ ist_time }}</p>
    <pre><strong>Top Output:</strong><br>{{ top_output }}</pre>
    """

    return render_template_string(html_template, name=name, username=username, ist_time=ist_time, top_output=top_output)
