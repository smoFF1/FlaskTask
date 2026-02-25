from datetime import datetime
from flask import Flask, redirect, url_for, send_file, request
from db_utils import get_db_connection, init_db

app = Flask(__name__)

init_db()

# Roi - Show HTML file
@app.route("/")
def home():
    return send_file("index.html")

# Sami
@app.route('/<room>')
def start_chat(room):
    return send_file('index.html')

# Roi - Retrieves the chat history for a specific room
@app.route('/api/chat/<room>', methods=['GET'])
def api_chat_get(room):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT created_at, username, message FROM messages WHERE room = %s ORDER BY created_at ASC", (room,))
    rows = cursor.fetchall()
    
    chat_history = ""
    for created_at, username, msg_text in rows:
        formatted_time = created_at.strftime("[%Y-%m-%d %H:%M:%S]") # type: ignore
        chat_history += f"{formatted_time} {username}: {msg_text}\n"
        
    cursor.close()
    conn.close()
    
    return chat_history, 200, {'Content-Type': 'text/plain'}

# Sami - saving incoming messages inside the DB
@app.route('/api/chat/<room>', methods=['POST'])
def api_chat_post(room):
    username = request.form.get('username')
    message = request.form.get('msg') or request.form.get('message')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (room, username, message) VALUES (%s, %s, %s)", (room, username, message))
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Message received", 200

# Sami - reroute unhandled routes to home
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)