from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("main.html")  # Render the HTML template

if __name__ == '__main__':
    app.run(debug=True)
