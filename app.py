from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from waitress import serve

app =Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("file",validators=[InputRequired()])
    submit = SubmitField("upload file")

@app.route('/',methods= ['GET',"POST"])
@app.route('/home', methods= ['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "file is uploaded"
    return render_template('index.html', form=form)
if __name__ == '__main__':
    # Use Waitress to serve the Flask app
    serve(app, host='0.0.0.0', port=8000)
    

