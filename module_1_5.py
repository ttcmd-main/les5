immutable_var = (1,1.0,'name',True)
print(immutable_var)
# immutable_var[0][0] = 2 - не можем изменить потому что коллекция в круглых скобках
mutable_list = ([2,10.2,'a','b'])
mutable_list[0] = 3
mutable_list[1] = 5.1
mutable_list[2] = True
mutable_list = mutable_list, 'awd'
print(mutable_list)