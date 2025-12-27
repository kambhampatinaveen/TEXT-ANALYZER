from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        TEXT = request.form["text"]

        # Keep only letters (remove spaces, numbers, symbols)
        letters_only = [ch for ch in TEXT if ch.isalpha()]

        cleaned_text = "".join(letters_only)

        result["text"] = TEXT
        result["length"] = len(cleaned_text)
        result["words"] = len(TEXT.split())

        freq = {}
        for letter in cleaned_text.lower():
            freq[letter] = freq.get(letter, 0) + 1

        result["frequency"] = freq

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
