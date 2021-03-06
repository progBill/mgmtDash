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
        ret_val = c.fetchall()

        return ret_val

    def remove_agenda_item(self, agenda_id):
        c = self.get_cursor()
        sql="""
            DELETE FROM agenda WHERE id = %s
        """

        c.execute(sql, [agenda_id])
        self.conn.commit()
        return True

#    def get_all_skills(self):
#        c = self.get_cursor()
#        sql="""
#            SELECT id, node_name, parent_id
#            FROM skills
#        """

#        c.execute(sql)
#        rst = c.fetchall()
        
#        skills =[]
#        for i,x in enumerate(rst):
#            a = list(x)
#            skills.append({'id':a[0], 'name':a[1], 'parent':a[2]} )

#        skills = sorted(skills, key= lambda x: x['id'])

#        return skills


if __name__ == '__main__':
    import json
    asdf = Database()
    print json.dumps( asdf.get_all_skills() )


