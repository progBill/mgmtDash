from flask import Flask

app = Flask(__name__)
from mgmtDash import mgmt_views 


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

