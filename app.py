from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("website.html")


@app.route("/process_form", methods=['POST'])
def process_form():
    if request.method == 'POST':
        filename = request.form.get('filename')
        if filename:
            return redirect(url_for('analysis'))
    return "Error: Invalid form submission or missing filename"


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/process_query", methods=["POST"])
def process_query():
    if request.method == "POST":
        query = request.form.get('query')
        print(query)
        if query:
            return render_template('analysis.html', query=query)
    return("Error: Missing query or failed analysis")


if __name__ == '__main__':
    app.run(debug=True, port=8000)