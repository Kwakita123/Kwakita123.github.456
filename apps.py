from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/", methods=["GET", "POST"])
def home():

    # Create a secret number the first time
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)

    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        secret_number = session["secret_number"]

        if guess == secret_number:
            message = "🎉 You got it! Amazing job!"
            session["secret_number"] = random.randint(1, 100)
        elif guess < secret_number:
            message = "⬆️ Too low! Try a higher number."
        else:
            message = "⬇️ Too high! Try a lower number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
