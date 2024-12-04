from flask import Flask, render_template

app = Flask(__name__)

@app.route("/trending")
def trending():
    return render_template("trending.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
