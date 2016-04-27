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
            SELECT topic, meeting, id 
            FROM agenda
        """
        last_week = (datetime.datetime.now()- datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')

        c.execute(sql)
        return c.fetchall()



    def remove_agenda_item(self, agenda_id):
        c = self.get_cursor()
        sql="""
            DELETE FROM agenda WHERE id = %s
        """

        c.execute(sql, [agenda_id])
        self.conn.commit()
        return True




if __name__ == '__main__':
    asdf = Database()
#    asdf.remove_agenda_item(11)
    print asdf.get_agenda_items()



