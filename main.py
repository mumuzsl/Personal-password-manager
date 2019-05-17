import sqlfile
import eel

eel.init('web')


@eel.expose
def add(a, b):
    print(a, b)
    return {'r': a + b}


@eel.expose
def get():
    # print(sqlfile.select())
    return sqlfile.select()


eel.start('index.html')
