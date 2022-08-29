def selectName():
    name = int(input(
        "Enter 1 for Sid\nEnter 2 for Opi\nEnter 3 for Adu\nChoose--> "))
    if name > 3 or name < 1:
        exit()
    else:
        return name
