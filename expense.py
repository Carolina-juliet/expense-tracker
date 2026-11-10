a="EXPENSE TRACKER "
print(a)
list1=[]
def add():
    cat=input("Enter category: ")
    amnt=int(input("Enter amount "))
    print("you have spent", amnt, "on",cat)
    
    view={"category":cat, "Amount": amnt}
    list1.append(view)
    return view
def vexp(a):
    for i in range(len(a)):
        print(a[i])
    
def subt(a,b):
    tot=0
    for i in range(len(b)):
        if b[i].get("category") == a:
            tot+=b[i].get("Amount")
    return tot
def tot(b):
    total=0
    for i in range(len(b)):
        total+=b[i].get("Amount")
    return total
def delete(del2, a):
    for i in range(len(a)):
        if a[i].get("category")==del2:
            a.pop(i)

view={}
while(True):
    print("1.Add expense ")
    print("2.view expense ")
    print("3.Total")
    print("4.Subtotal")
    print("5. Delete expense")
    print("6.Exit ")
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            view.update(add())
        case 2:
            vexp(list1)
        case 3:
            total=tot(list1)
            print("Total=",total)
        case 4:
            sub=input("Enter the category: ")
            total=subt(sub,list1)
            print("Total expense on ", sub,total)
        case 5:
            del1=input("Enter the category to be deleted")
            delete(del1, list1)
        case 6:
            break
        case _:
            print("Error")







    
