from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = "мій_дуже_секретний_ключ_12345"
users = {
    "admin": {"name": "admin", "email": "admin@gmail.com", "password": "123456"},
    "ivan": {"name": "ivan", "email": "ivan@gmail.com", "password": "qwerty"},
    "igor": {"name": "igor", "email": "igor@gmail.com", "password": "zxc123"},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_input = request.form["nm"]
        password = request.form["password"]

        for username, data in users.items():
            if login_input in (username, data["email"]) and password == data["password"]:
                session["user"] = username
                flash("Ви успішно увійшли ✅", "success")
                return redirect(url_for("dashboard"))

        flash("❌ Невірне імʼя/email або пароль", "error")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", users=users)

# --- Додати користувача ---
@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    users[username] = {"name": username, "email": email, "password": password}
    flash("Ви успішно додали користувача ✅", "success")
    return redirect(url_for("dashboard"))


@app.route("/users/<username>", methods=["POST"])
def users_handler(username):
    method = request.form.get("_method").upper()

    if method == "PUT":
        users[username]["name"] = request.form["name"]
        users[username]["email"] = request.form["email"]
        users[username]["password"] = request.form["password"]
        flash("Ви успішно оновили дані користувача ✅", "success")
        return redirect(url_for("dashboard"))

    elif method == "PATCH":
        email = request.form.get("email")
        if email:
            users[username]["email"] = email
            flash("Email оновлено", "success")
            return redirect(url_for("dashboard"))
        
    elif method == "DELETE":
        users.pop(username, None)
        flash("Ви успішно видалили користувача ✅", "success")
        return redirect(url_for("dashboard"))

    return "Метод не підтримується", 400

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Ви вийшли з системи 👋", "success")
    return redirect(url_for("login"))

@app.route('/toggle-theme')
def toggle_theme():
    session['theme'] = 'dark' if session.get('theme') != 'dark' else 'light'
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)









