from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def home():
    global secret_number
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess < secret_number:
            message = "Too low!"
        elif guess > secret_number:
            message = "Too high!"
        else:
            message = "🎉 Correct! Starting a new game..."
            secret_number = random.randint(1, 100)

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
