import os
from PIL import Image
import os
import img_mody as img
from flask import Flask, render_template, request
app = Flask(__name__)

#@app.route('/static/images')
def imd_mod(path):

    image = Image.open(path)
    print(image)
    new_image = image.resize((400, 400))
    path_split = path.rsplit("\\", 1)
    img_name = path_split[1]
    name_split = img_name.split(".")
    new_img_name = name_split[0] + "_0." + name_split[1]
    new_path = os.path.join(path_split[0],new_img_name )
    new_image.save(new_path)
    return new_path

path=r"C:\Users\smurugan\Desktop\flask-task\templates\test"
imd_mod(path)