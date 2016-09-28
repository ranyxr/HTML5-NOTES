
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
                


def admin(db):
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

def user(db):

    while True:
        print '''
           --------command-------
           --1: select  2: quit--
           ----------------------
           '''

        num = input("Input command >>")

        if num not in [1,2]:
            print "input error!"
            sys.stdin.flush()
            continue
        elif num == 2:
            db.close()
            return
        else:
            do_select(db)

def do_register(db):
    cursor = db.cursor()
    while True:
        name = raw_input("input name(string) >>")
        sql = "select * from usr where name = '%s'"%name
        cursor.execute(sql)
        data = cursor.fetchone()

        if not data:
            break
        else:
            print "sorry the name existe"

    passwd = raw_input("input passwd(string) >>")
    flog = input("input flog(0 or 1) >>")

    if flog not in [0,1]:
        print "sorry your set is error"
        return

    sql = "insert into usr value('%s','%s',%d)"%(name,passwd,flog)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()
        return

    print "register OK!"
    


def do_login(db):
    cursor = db.cursor()
    name = raw_input("input name(string) >>")
    passwd = raw_input("input passwd(string) >>")

    sql = "select * from usr where name = '%s' and passwd = '%s'"%(name,passwd)
    cursor.execute(sql)
    data = cursor.fetchone()
    print data
    
    if data == None:
        print "sorry,your name or passwd is error!"
        return
    elif data[2] == 0:
        admin(db)
    else:
        user(db)

def main():
    db = MySQLdb.connect('localhost','root','123','student')
    while True:
        print '''
           --------------command-------------
           --1: login  2. register  3: quit--
           ----------------------------------
           '''

        num = input("Input command >>")

        if num not in [1,2,3]:
            print "input error!"
            sys.stdin.flush()
            continue
        elif num == 1:
            do_login(db)
        elif num == 2:
            do_register(db)
        else:
            db.close()
            return
            
if __name__ == "__main__":
    main()
