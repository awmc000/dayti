"""

dayti

app.py

point of entry

"""
from flask import Flask, render_template
from dotenv import load_dotenv
from markupsafe import escape

load_dotenv()

app = Flask(__name__,static_url_path='',static_folder='./static')

@app.route('/')
def index():
    return render_template('index.html', prompt="你多长时间买一次新手机？上次是为什么？")