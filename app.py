from flask import Flask, render_template

app = Flask(__name__)

@app.route("/freeads")
def freeads():
    return render_template("freeads.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
