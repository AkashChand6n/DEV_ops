# lang = "python"
# lst = list(lang)
# print(type(lst))
# print(lst)

# print("=================================================")

# lst1 = [i for i in lang]
# print(lst)
# print(type(lst1))

# print("=================================================")

# lst2 = [i for i in range(20)]
# print(lst2)

# print("===================================================")

# lst3 = [i*i for i in range(20)]
# print(lst3)

# print("===================================================")

# lst4 = [(i,i*i) for i in range(20)]
# print(lst4)

# print("===================================================")

# lst5 = [(i*2) for i in range(20)]
# print(lst5)

# print("===================================================")

# lst6 = [i for i in range(20) if i%2!=0]
# print(lst6)


list7 = [[1,2,3],[4,5,6],[7,8,9]]
flat_list=[number for row in list7 for number in row]
print(flat_list)