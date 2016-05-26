from flask import Flask, redirect, url_for
from mgmtDash.mgmt_views import mgmtDash_BP

app = Flask(__name__)
app.secret_key = 'super secret'

app.register_blueprint(mgmtDash_BP, url_prefix='/mgmtDash')

@app.route('/')
def landing():
    return "You've arrived"
