import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import time
import json


UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','js','zip'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compute_speed(t,s):
    return int(s/t/1024/1024*100)/100
#    return '{:.2f} MB/s'.format(s/t/1024/1024)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        begin = time.time()
        file = request.files['file']
        size = len(file.read())
        end = time.time()
        return json.dumps(dict(code=0,
          #  spend='{:.2f}s'.format(end-begin),
          remote_addr=request.remote_addr,
          spend=int(100*(end-begin))/100,
          size=size,filename=file.filename,speed=compute_speed(end-begin,size)))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/')
def index():
    return 'hello'

@app.route('/ip')
def ip():
    return request.remote_addr


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=19999)
