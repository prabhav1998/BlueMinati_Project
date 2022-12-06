from flask import Flask,render_template

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/endpoint')
def endpoint():
    return "Hello World ! , this is a Flask Application"

@app.route('/linker')
def linker():
    return render_template('link.html')

if __name__ == "__main__":
    app.run(host="13.232.159.216",port=5000)

