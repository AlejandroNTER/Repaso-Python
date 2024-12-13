num=999
print(num)

print(num +1)

print(num -10)

print(num*10)

print(num/5)

print(num%60)

a= 1000
b= 100
c= 200
d= 300
print(f"Si a es mayor que b y c menor que d, devolverá true {True if a>b & c<d else False}")

print(f"Si la suma de a y b es mayor o igual que c o la suma de b y c es mayor o igual que d {True if a+b>=c or b+c<d else False}")

list1 = [1,2,3,4,5]

list2 = ['Hello','Word','Python']

list3 = ['Operator','Membership', 100,200]

comp1 = 5 in list1
comp2 = "Hello" in list2 or "Python" in list2
comp3 =  list2 == list3

print(comp1)
print(comp2)
print(comp3)

print(type(a) is int)
print(type(a) is not int)