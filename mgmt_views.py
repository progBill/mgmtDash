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

mgmtDash = Blueprint('mgmtDash', __name__, template_folder='templates', static_folder='static')

###########
## VIEWS ##
###########

@mgmtDash.route('/', methods=['GET'])
@mgmtDash.route('/entry', methods=['GET'])
def main():
    agenda = DB().get_agenda_items()
    return render_template('entry.html', agenda=agenda)

################
## AJAX CALLS ##
################

@mgmtDash.route('/get_agenda_items', methods=['POST','GET'])
def get_agenda_items():
    items = [str(Agenda_Item(x[0],x[1],x[2])) for x in DB().get_agenda_items()]

    return "[" + ",".join(items) + "]"

@mgmtDash.route('/delete_agenda_item/<agenda_id>', methods=['DELETE','POST'])
def delete_agenda_item(agenda_id):
    """Removes an item with the given id"""
    DB().remove_agenda_item(agenda_id)
    return json.dumps({'delete':'success'})

@mgmtDash.route('/create_agenda_item', methods=['POST'])
def agenda_maker():
    new_item = json.loads( request.data )
    topic = new_item["topic"]
    meeting = new_item["meeting"]
    DB().save_agenda_item(topic, meeting)

    return json.dumps({'save':'success'})

