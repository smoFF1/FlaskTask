from flask import Flask,redirect,url_for,render_template,send_file
app=Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route('/<room>')
def start_chat(room):
    room_number = request.args.get('room')
    return send_file('resources/html/index.html')

if __name__=="__main__":
    app.run()