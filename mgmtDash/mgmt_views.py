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
from data.agenda_item import Agenda_Item

mgmtDash_BP = Blueprint('mgmtDash_BP', __name__,template_folder='templates', static_folder='static') 

###########1
## VIEWS ##
###########

@mgmtDash_BP.route('/', methods=['GET'])
@mgmtDash_BP.route('/entry', methods=['GET'])
def mgmt_main():
    agenda = DB().get_agenda_items()
    return render_template('entry.html', agenda=agenda)

#@mgmtDash_BP.route('/pdp', methods=['GET'])
#def pdp():
#    pdps = []
#    for r in DB().get_all_skills():
#        pdps.append({'focus': r[0], 'name':r[1], 'type':r[2]})
#    return render_template('pdp.html', pdp_items=sorted(pdps))

################
## AJAX CALLS ##
################

@mgmtDash_BP.route('/get_agenda_items', methods=['POST','GET'])
def get_agenda_items():
    items = [str(Agenda_Item(x[0],x[1],x[2])) for x in DB().get_agenda_items()]

    return "[" + ",".join(items) + "]"

@mgmtDash_BP.route('/delete_agenda_item/<agenda_id>', methods=['DELETE','POST'])
def delete_agenda_item(agenda_id):
    """Removes an item with the given id"""
    DB().remove_agenda_item(agenda_id)
    return json.dumps({'delete':'success'})

@mgmtDash_BP.route('/create_agenda_item', methods=['POST'])
def agenda_maker():
    new_item = json.loads( request.data )
    topic = new_item["topic"]
    meeting = new_item["meeting"]
    DB().save_agenda_item(topic, meeting)

    return json.dumps({'save':'success'})

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(mgmtDash_BP, url_prefix='/mgmtDash')

    app.run()


