from flask import (
    Blueprint,
    render_template, 
    session,
    request,
    redirect, 
    url_for
)

import json
from data.data_access import Database as DB

pdp_bp = Blueprint('pdp', __name__,template_folder='templates', static_folder='static') 

###########
## VIEWS ##
############

@pdp_bp.route('/', methods=["GET"])
def main():
    pdps = DB().get_all_skills()


    return render_template('pdp.html',pdp_items=pdps)


@pdp_bp.route('/get_skills', methods=['POST', 'GET'])
def get_pdp_skills():
    """gets all skills from DB"""
    return json.dumps( DB().get_all_skills() )

@pdp_bp.route('/save_skills', methods=['POST'])
def save_skills():
    """takes skills as they're filled out, saves them in a DB"""
    result = json.dumps( request.form )

    print 'res: {}'.format( result )

    return 'gotcha'

