from flask import Flask, session
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

import application.views

if __name__ == "__main__":
    app.run()