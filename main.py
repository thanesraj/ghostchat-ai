from flask import Flask, render_template, request, url_for
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {e}"
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
