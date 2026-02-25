from datetime import datetime

from flask import Flask,redirect,url_for,render_template,send_file,request
import os
app=Flask(__name__)
history_dir='history'
@app.route("/")
def home():
    return send_file("index.html")

@app.route('/<room>')
def start_chat(room):
    return send_file('index.html')

@app.route('/api/chat/<room>', methods=['GET'])
def api_chat_get(room):
    chat_history=""
    file_name=f"{history_dir}/{room}.txt"
    if not os.path.exists(file_name):
        return "",200
    else: 
        with open(file_name,'r') as file:
            for line in file:
                chat_history+=line
    return chat_history

@app.route('/api/chat/<room>', methods=['POST'])
def api_chat_post(room):

    os.makedirs(history_dir, exist_ok=True)
    chat_file=f"{history_dir}/{room}.txt"
    
    with open(chat_file, 'a') as file:
        now = datetime.now()
        formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
        line=f"{formatted} {request.form.get('username')}: {request.form.get('msg')}\n"
    return "Message received", 200

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run()