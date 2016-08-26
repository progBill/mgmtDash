from flask import Flask
from mgmtDash.mgmt_views import mgmtDash_BP

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.secret_key = app.config['SECRET_KEY']

app.register_blueprint(mgmtDash_BP, url_prefix='/mgmtDash')

@app.route('/')
def landing():
    return "You've arrived"



