from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "мій_дуже_секретний_ключ_12345"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route('/toggle-theme')
def toggle_theme():
    session['theme'] = 'dark' if session.get('theme') != 'dark' else 'light'
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)





    



