import datetime
import MySQLdb
from user import User
from config import mysql as c

class Database:

    ####################
    ## STANDARD SETUP ##
    ####################

    def __init__(self):
        pass

    def get_cursor(self):
#        self.conn = MySQLdb.connect(user='manage_user', passwd='Quarters25!',host='mysql-manage.billebeling.com',db='billebeling_management')
        self.conn = MySQLdb.connect(user=c['USER'], passwd=c['PASS'], host=c['HOST'], db=c['BASE'])
        
        return self.conn.cursor()

    #############
    ## QUERIES ##
    #############


    def is_registered(self, username, passhash):
        c = self.get_cursor()
        sql ="""
            SELECT *
            FROM users
            WHERE username = %s AND passhash = %s
        """
        c.execute(sql, [username, passhash])

        if c.rowcount:
            print c.fetchall
            return True
        else:
            return False


    def save_agenda_item(self, topic, meeting):
        c = self.get_cursor()
        sql="""
            INSERT INTO agenda (topic, meeting)
            VALUES (%s, %s)
        """
        c.execute(sql, [topic, meeting])
        self.conn.commit()

        return True

    def get_agenda_items(self):
        c = self.get_cursor()
        sql="""
            SELECT topic, meeting 
            FROM agenda
        """
        last_week = (datetime.datetime.now()- datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')

        c.execute(sql)
        return c.fetchall()


if __name__ == '__main__':
    db = Database()

