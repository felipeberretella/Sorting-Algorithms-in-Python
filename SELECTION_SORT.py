def selection_sort (items):
    for j in range(len(items)-1):
        min_index = j

        for i in range(j,len(items)):

            if items[i] < items[min_index]:
                min_index = i

        if items[j] > items[min_index]:
            aux = items[j]
            items[j]= items[min_index]
            items[min_index] = aux
    return items

items = []
bk = False

while not bk:
    value = input("write values or end \n")
    if value == "end":
        print(selection_sort(items))
        bk = True

    elif value !="":
        items.append(float(value))
