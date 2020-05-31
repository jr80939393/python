list_ex = list(range(2,101,2))
print(list_ex)
del list_ex[45:50]
print(list_ex)
str_classtime = "15:10:00"
list_classtime = list(str_classtime.split(':'))
print(list_classtime)
list_ex[0] = list_classtime[0]
list_ex[1] = list_classtime[1:3]
print(list_ex)
print(type(list_ex))
print(type(list_ex[0]),type(list_ex[1]),type(list_ex[2]))
