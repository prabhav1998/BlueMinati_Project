from flask import Flask,render_template

app = Flask('__name__')

@app.route('/')
def home():
    return "Hello World ! , this is a Flask Application 1.1qqq"


@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return 0 #jsonify({ "success": True, "message": "Server is shutting down..." })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

