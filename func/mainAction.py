import datetime


def getDate():
    t = datetime.datetime.now()
    return str(t)


def mainAction(sname, stask, saction):
    if sname == 1 and stask == 1 and saction == 1:
        write = input('Write your food log--> ')
        with open('data/Food/sid.txt', 'a') as sidFood:
            sidFood.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Food/sid.txt]')
    elif sname == 2 and stask == 1 and saction == 1:
        write = input('Write your food log--> ')
        with open('data/Food/opi.txt', 'a') as opiFood:
            opiFood.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Food/opi.txt]')
    elif sname == 3 and stask == 1 and saction == 1:
        write = input('Write your food log--> ')
        with open('data/Food/adu.txt', 'a') as aduFood:
            aduFood.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Food/adu.txt]')
    elif sname == 1 and stask == 2 and saction == 1:
        write = input('Write your exercise log--> ')
        with open('data/Exercise/sid.txt', 'a') as sidExer:
            sidExer.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Exercise/sid.txt]')
    elif sname == 2 and stask == 2 and saction == 1:
        write = input('Write your exercise log--> ')
        with open('data/Exercise/opi.txt', 'a') as opiExer:
            opiExer.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Exercise/opi.txt]')
    elif sname == 3 and stask == 2 and saction == 1:
        write = input('Write your exercise log--> ')
        with open('data/Exercise/adu.txt', 'a') as aduExer:
            aduExer.write(getDate()[:-7] + ':- ' + write + '\n')
            print('Your data has been saved in [data/Exercise/adu.txt]')
    elif sname == 1 and stask == 2 and saction == 2:
        with open('data/Exercise/sid.txt', 'r') as sidExer:
            data = sidExer.read()
            print(data)
    elif sname == 2 and stask == 2 and saction == 2:
        with open('data/Exercise/opi.txt', 'r') as opiExer:
            data = opiExer.read()
            print(data)
    elif sname == 3 and stask == 2 and saction == 2:
        with open('data/Exercise/adu.txt', 'r') as aduExer:
            data = aduExer.read()
            print(data)
    elif sname == 1 and stask == 1 and saction == 2:
        with open('data/Food/sid.txt', 'r') as sidFood:
            data = sidFood.read()
            print(data)
    elif sname == 2 and stask == 1 and saction == 2:
        with open('data/Food/opi.txt', 'r') as opiFood:
            data = opiFood.read()
            print(data)
    elif sname == 3 and stask == 1 and saction == 2:
        with open('data/Food/adu.txt', 'r') as aduFood:
            data = aduFood.read()
            print(data)
