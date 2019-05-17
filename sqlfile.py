import sqlite3

sql = {
    'ct': 'CREATE TABLE SERCET'
          '(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'
          'PLACE CHAR(50),'
          'ACCOUNT CHAR(50),'
          'PASSWORD CHAR(50),'
          'NOTE TEXT);',
    'in': 'INSERT INTO SERCET'
          '(PLACE,ACCOUNT,PASSWORD)'
          'VALUES',
    'se': 'SELECT * FROM SERCET',
    'up': 'UPDATE SERCET'
          'SET'
}

dic = {
    'place': 1,
    'account': 2,
    'pawword': 3,
    'pw': 3
}


def getUpdate(id, col, new, colIndex=0):
    id = str(id) if type(id) is int else id

    if type(col) is int:
        n = col
    elif type(col) is str:
        n = dic.get(col)

    if n == 1:
        return 'UPDATE SERCET SET place = \'' + new + '\' WHERE ID = ' + id
    elif n == 2:
        return 'UPDATE SERCET SET account = \'' + new + '\' WHERE ID = ' + id
    elif n == 3:
        return 'UPDATE SERCET SET password = \'' + new + '\' WHERE ID = ' + id


def getInsert(*args, p='', a='', pw=''):
    if len(args) == 1:
        return sql.get('in') + str(args[0])
    elif len(args) == 3:
        return sql.get('in') + '(' + str(args[0]) + ',' + str(args[1]) + ',' + str(args[2]) + ')'
    elif len(args) == 0:
        return sql.get('in') + str([p, a, pw])
    pass


def runsql(state):
    conn = sqlite3.connect('sercet.db')
    c = conn.cursor()
    c.execute(state)
    conn.commit()
    conn.close()
    pass


def insert(data: list):
    conn = sqlite3.connect('sercet.db')
    c = conn.cursor()

    for i in data:
        c.execute(getInsert(i))
        pass

    conn.commit()
    conn.close()
    pass


def getSelect(p):
    if p is '':
        return sql.get('se')
    return sql.get('se') + ' WHERE PLACE = \'' + str(p) + '\''
    pass


def select(place=''):
    conn = sqlite3.connect('sercet.db')
    c = conn.cursor()

    # print(getSelect(place))

    cursor = c.execute(getSelect(place))

    # for row in rows:
    #     print(row)
    rows = [{'id': i[0], 'p': i[1], 'a': i[2], 'pw': i[3]} for i in cursor]

    conn.commit()
    conn.close()

    return rows
    pass


def main():
    # print(sql.get('ct'))
    # print(getInsert('a', 'a', 'a'))
    # runsql(sql.get('ct'))
    # print(type(select()))
    # print(select())
    runsql(getUpdate(15, 2, 'Coolzmumu@163.com'))
    pass


if __name__ == '__main__':
    main()
    pass
