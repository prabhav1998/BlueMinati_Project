from flask import Flask,render_template

app = Flask('__name__')

@app.route('/')
def home():
    return "Hello World ! , this is a Flask Application 8. .prabhav"




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

