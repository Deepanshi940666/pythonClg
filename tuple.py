x=4,6,2 #"," is must otherwise it shows integer
print(type(x))
 
tpl = (1,2,3,4, 4)
print(id(tpl))
tpl+=("hello", 6,8,3)
print(id(tpl))
print (tpl)
print (tpl[2:])
print (tpl.count(4))
