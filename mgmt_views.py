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

@app.route('/agenda_maker', methods=['POST'])
def agenda_maker():
    topic = request.form['agenda_topic']
    meeting=request.form['agenda_meeting']
    DB().save_agenda_item(topic, meeting)

    return redirect(url_for('main')) 

@app.route('/delete_agenda_item/<agenda_id>', methods=['GET'])
def delete_agenda_item(agenda_id):
    """Removes an item with the given id"""
    DB().remove_agenda_item(agenda_id)
    return redirect(url_for('main'))


@app.route('/get_agenda_items', methods=['POST','GET'])
def get_agenda_items():
    items = [str(Agenda_Item(x[0],x[1])) for x in DB().get_agenda_items()]

    return "[" + ",".join(items) + "]"

