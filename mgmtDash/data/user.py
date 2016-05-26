

class User(object):

    def __init__(self, username, email, verified, first=None, last=None):
        self.username = username
        self.email = email
        self.verified = verified
        self.first = first
        self.last = last


