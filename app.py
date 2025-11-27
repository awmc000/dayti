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

prompts = {
    1: "今天天气怎么样？",
    2: "你最喜欢听什么音乐？",
    3: "你多长时间买一次新手机？上次是为什么？",
    4: "你讲个尴尬故事吧。"
}

@app.route('/')
def index():
    return render_template('index.html', prompt="你多长时间买一次新手机？上次是为什么？")

@app.route('/prompt/<int:level>')
def prompt(level):
    return render_template('index.html', prompt=prompts[level])
