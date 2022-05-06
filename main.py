import os
from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename
import Text

UPLOAD_FOLDER = 'C:\\Users\\georg\\PycharmProjects\\Flask\\templates\\Images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_text = Text.get_text(f'{UPLOAD_FOLDER}\\{filename}')
            return render_template('result.html', result=image_text)
        return redirect("/faq")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
