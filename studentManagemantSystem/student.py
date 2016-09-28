#!/usr/bin/python
#coding=utf-8

import sys
import MySQLdb

def do_insert(db):
    cursor = db.cursor()
    id = input("input id(int) >>")
    name = raw_input("input name(string) >>")
    age = input("input age(int) >>")
    score = input("input score(float) >>")

    sql = "insert into stu values(%d,'%s',%d,%f)"%(id,name,age,score)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()
        return

    print "insert OK!"

def do_delete(db):
    cursor = db.cursor()

    id = input('input the id(int)>>')

    sql = "delete from stu where id = %d"%id

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()
        return

    print "delete OK!"


def do_update(db):
    cursor = db.cursor()

    id = input('input the id(int)>>')
    score = input('update score (float)>>')

    sql = "update stu set score = %f where id = %d"%(score,id)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()
        return

    print "update OK!"
    
def do_select(db):
    cursor = db.cursor()

    sql = "select * from stu"

    try:
        cursor.execute(sql)

        results = cursor.fetchall()

        for field in cursor.description:
            print field[0],"   ",

        print ''

        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            score = row[3]
            print "%d    %s    %d      %.2f"%(id,name,age,score)

    except:
        print "sorry operation failed"
        db.rollback()
        return
                



def main():
    db = MySQLdb.connect('localhost','root','123','student')
    command = {1:do_insert,2:do_delete,3:do_update,4:do_select}
    def do_what():
        command.get(num)(db)

    while True:
        print '''
           ------------------------command------------------------
           --1: insert  2: delete  3: update  4: select  5: quit--
           -------------------------------------------------------
           '''

        num = input("Input command >>")

        if num not in [1,2,3,4,5]:
            print "input error!"
            sys.stdin.flush()
            continue
        elif num == 5:
            db.close()
            return
        else:
            do_what()

            
if __name__ == "__main__":
    main()
