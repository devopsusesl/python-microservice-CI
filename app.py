from flask import Flask, render_template

app = Flask(__name__)

@app.route("/news")
def news():
    return render_template("news.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
