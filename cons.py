import os
import img_mody as img
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)

# PEOPLE_FOLDER = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = "static/"
app.debug = True


@app.route('/')
@app.route('/index')
def form():
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        print(file1)
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        print(path)
        # Create a directory in a known location to save files to.
        # ploads_dir = os.path.join(app.instance_path, 'uploads')
        # os.makedirs(uploads_dir)
        for i in file1:
            file1.save(path)
            full_filename = img.imd_mod(path)
            return render_template("display.html", user_image=full_filename)


app.run(host='localhost', port=5000)
