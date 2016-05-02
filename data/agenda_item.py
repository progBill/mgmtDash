from json import dumps

class Agenda_Item(object):

    def __init__(self, topic, meeting, *args, **kwargs):
        self.topic = topic
        self.meeting = meeting

    def __repr__(self):
        return dumps({'topic':self.topic, 'meeting':self.meeting})


if __name__ == '__main__':
    a = Agenda_Item('do stuff','later')
    print a

