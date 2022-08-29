def selectTask():
    task = int(input("Enter 1 for Food\nEnter 2 for Excrcise\nChoose--> "))
    if task > 2 or task < 1:
        exit()
    else:
        return task
