#LIST
'''mylist=[127,"python",36.01,True,127,"pramathi"]
mylist.append(342)
mylist.insert(3,"hello")
print(mylist)
print(mylist[7])
print(mylist[1:3])
print(mylist[:4])
print(mylist[0::-1])
print(mylist[1:5:2])
print(len(mylist))
for i in range(0,6):
    print(mylist[i])
for i in  mylist:
    print(i)
print()'''

#TUPLE
'''mytuple=("life",81,27.9,False,"fam")
print(mytuple)
print(type(mytuple))
mytuple=mytuple+("friends",)
mytuple=mytuple+(36,4.4,"asa")
print(mytuple)
for i in range(0,6):
    n=int(input("enter"))
    mytuple=mytuple+(n,)
print(mytuple)'''

#DICTIONARY
'''mydict={101:"hello",102:"python",103:999,104:12.6,105:True}
print(mydict)
mydict[102]="Pramathi"
mydict[90]=90909
print(mydict[101],mydict[104])
for i in mydict:
    print(i)
for j in mydict.values():
    print(j)
for i,j in mydict.items():
    print(i,j)
mydict.pop(103)
print(mydict)'''

#MULTI-D LISTS
'''list=[[18,36,27],["r","a","m"],[5.4,0.9]]
print(list)
print(list[1])
print(list[0][2])'''

#SET
'''myset={1,9,"hooiii",8.1,90.7,False,9}
yourset={9,10,"hooiii",True}
print(myset)
myset.add("booii")
print(myset)
myset.update([1,89,6,"peehh"])
print(myset)
myset.remove(89)
myset.discard(8.1)
newset=myset.union(yourset)
print(newset)
newset=myset.intersection(yourset)
print(newset)
newset=myset.difference(yourset)
print(newset)'''


c =["mahindra","suzuki","toyota"]

if mahindra in c:
    print("welcome to mahindra family",c[0])
elif toyota in c:
    print(c[2],"welcome to toyota family")
else:
    print(c[1],"welcome to  Suzuki family")
        
