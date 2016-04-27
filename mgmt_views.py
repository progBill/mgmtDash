from flask import (
    Flask, 
    render_template, 
    session,
    request)
from mgmtDash import app
import json
from data.data_access import Database as DB

###########
## VIEWS ##
###########

@app.route('/', methods=['GET'])
def main():
    try:
        return render_template('entry.html')
    except Exception:
        return 'problem'

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

    try:
      DB().save_agenda_item(topic, meeting)
    except Exception:
      print Exception

    return dash("Bill")

@app.route('/delete_agenda_item/<agenda_id>', methods=['GET'])
def delete_agenda_item(agenda_id):
    """Removes an item with the given id"""
    DB().remove_agenda_item(agenda_id)
    return redirect(url_for('/dash'))





