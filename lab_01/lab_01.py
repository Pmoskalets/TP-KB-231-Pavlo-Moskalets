
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "years":"15", "email":"bob@exmp.com"},
    {"name":"Emma", "phone":"0631234567", "years":"17", "email":"emma@exmp.com"},
    {"name":"Jon",  "phone":"0631234567", "years":"22", "email":"jon@exmp.com"},
    {"name":"Zak",  "phone":"0631234567", "years":"19", "email":"zak@exmp.com"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Age is " + elem["age"] + ", Email is " + elem["email"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    insertPosition = -1
    for item in list:
        if name == item["name"]:
            insertPosition = list.index(item)
            break
    if insertPosition == -1:
        print("Name not found")
    else:
        oldname = list[insertPosition]["name"]
        oldphone = list[insertPosition]["phone"]
        oldage = list[insertPosition]["age"]
        oldemail = list[insertPosition]["email"]

        strForPrint = "Student name is " + oldname + ",  Phone is " + oldphone + ", Age is " + oldage + ", Email is " + oldemail
        print(strForPrint)

        newname = input("Please enter student name or skip: ") or oldname
        newphone = input("Please enter student phone or skip: ") or oldphone
        newage = input("Please enter student age or skip: ") or oldage
        newemail = input("Please enter student email or skip: ") or oldemail

        updateElement = {"name":newname, "phone":newphone, "age":newage, "email":newemail}
        del list[insertPosition]
        updatePosition = 0
        for item in list:
            if newname > item["name"]:
                updatePosition += 1
        list.insert(updatePosition, updateElement)
        print("New information has been added")
    return
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()