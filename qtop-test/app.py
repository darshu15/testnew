from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)  # Fixed here

@app.route('/htop')
def htop():
    name = "K Darshan"
    username = os.getenv('USER', 'codespace_user')
    ist_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -bn1")

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist_time}</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':  # Fixed here
    app.run(host='0.0.0.0', port=5000)
