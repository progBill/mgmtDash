from flask import (
    Flask, 
    render_template, 
    session,
    request,
    redirect, 
    url_for
)
from mgmtDash import app
import json
from data.data_access import Database as DB
from data.agenda_item import Agenda_Item

###########
## VIEWS ##
###########

@app.route('/', methods=['GET'])
@app.route('/entry', methods=['GET'])
def main():
    agenda = DB().get_agenda_items()
    return render_template('entry.html', agenda=agenda)

@app.route('/<user>/dash', methods=['GET'])
@app.route('/dash',methods=['GET'])
def dash(user='Bill'):
    """Returns a dashboard for a particular user"""
    agenda = DB().get_agenda_items()
    return render_template('dash.html', user=user, agenda=agenda)


################
## AJAX CALLS ##
################

@app.route('/get_agenda_items', methods=['POST'])
def get_agenda_items():
    items = [str(Agenda_Item(x[0],x[1],x[2])) for x in DB().get_agenda_items()]

    return "[" + ",".join(items) + "]"

@app.route('/delete_agenda_item/<agenda_id>', methods=['DELETE','POST'])
def delete_agenda_item(agenda_id):
    """Removes an item with the given id"""
    DB().remove_agenda_item(agenda_id)
    return redirect(url_for('main'))

@app.route('/create_agenda_item', methods=['POST'])
def agenda_maker():
    new_item = json.loads( request.data )
    topic = new_item["topic"]
    meeting = new_item["meeting"]
    DB().save_agenda_item(topic, meeting)

    return json.dumps({'save':'success'})


