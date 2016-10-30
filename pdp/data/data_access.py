import datetime
import MySQLdb

class Database:

    ####################
    ## STANDARD SETUP ##
    ####################

    def __init__(self):
        pass

    def get_cursor(self):
        c = {'HOST': 'localhost', 'BASE': 'management', 'USER': 'bill', 'PASS': 'zardoz76'}
        self.conn = MySQLdb.connect(user=c['USER'], passwd=c['PASS'], host=c['HOST'], db=c['BASE'])
        
        return self.conn.cursor()

    #############
    ## QUERIES ##
    #############


    def get_all_skills(self):
        c = self.get_cursor()
        skills = []
        sql="""
            SELECT id, node_name, parent_id
            FROM skills WHERE hierarchy_id = 1
        """

        c.execute(sql)
        for domain in c.fetchall():
            skills.append({"name":domain[1],"id":domain[0], "data":[]})




        sql ="""
            SELECT id, node_name, parent_id
            FROM skills WHERE hierarchy_id = 2
        """
        c.execute(sql)
        for foci in c.fetchall():
            focus = {"name":foci[1],"parent_id":foci[2],"id":foci[0],"data":[]}
            for domain in skills:
                if focus["parent_id"] == domain["id"]:
                    domain["data"].append(focus)


        sql ="""
            SELECT id, node_name, parent_id
            FROM skills WHERE hierarchy_id = 3
        """

        c.execute(sql)
        for attributes in c.fetchall():
            attribute = {"name":attributes[1],"id":attributes[0],"parent_id":attributes[2],"data":[]}
            for domain in skills:
                for focus in domain["data"]:
                    #I know, I know...  too many loops
                    if attribute["parent_id"] == focus["id"]:
                        focus["data"].append(attribute)
                        break


        return skills

if __name__ == '__main__':

    t3 = Database().get_all_skills()

    print t3


