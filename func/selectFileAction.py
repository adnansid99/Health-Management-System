def selectFileAction():
    theAct = int(
        input("Enter 1 to write Log\nEnter 2 to show Log\nChoose--> "))
    if theAct > 2 or theAct < 1:
        exit()
    else:
        return theAct
