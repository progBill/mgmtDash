from json import dumps

class Agenda_Item(object):

    def __init__(self, topic, meeting, item_id, *args, **kwargs):
        self.topic = topic
        self.meeting = meeting
        self.item_id = item_id

    def __repr__(self):
        return dumps({'topic':self.topic, 'meeting':self.meeting, 'item_id':self.item_id})

if __name__ == '__main__':
    a = Agenda_Item('do stuff','later', 6L)
    print a

