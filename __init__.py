from flask import Flask, url_for
from mgmtDash.mgmt_views import mgmtDash_BP
from pdp.pdp_views import pdp_bp

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.secret_key = app.config['SECRET_KEY']

app.register_blueprint(mgmtDash_BP, url_prefix='/mgmtDash') 
app.register_blueprint(pdp_bp, url_prefix='/pdp') 

@app.route('/')
def landing():
    return "Check out <a href='{}'>Management Dashboard</a>".format('./mgmtDash')

if __name__ == '__main__':
    app.run(debug=True, port=12012)    

