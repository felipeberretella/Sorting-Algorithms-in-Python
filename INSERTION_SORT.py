def insertion_sort (items):
    for i in range(1,len(items)):
        key = items[i]
        aux = i - 1
        while aux >= 0 and items[aux] > key:
            items[aux + 1] = items[aux]
            aux = aux - 1
        items[aux + 1] = key   
    return items

items = []
bk = False

while not bk:
    value = input("write values or end \n")
    if value == "end":
        print(insertion_sort(items))
        bk = True

    elif value !="":
        items.append(float(value))


