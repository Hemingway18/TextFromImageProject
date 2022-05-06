from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    picture = db.Column(db.BLOB, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        picture = request.form.get('picture')
        user = User(picture=picture)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)



