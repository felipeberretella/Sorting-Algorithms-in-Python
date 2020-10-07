def bubble_sort (items):

    for j in range(len(items)-1):

        for i in range(len(items)-1):

            if items[i]> items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

    return items

items = []
bk = False

while not bk:
    value = input("write values or end \n")
    if value == "end":
        print(bubble_sort(items))
        bk = True

    elif value !="":
        items.append(float(value))
