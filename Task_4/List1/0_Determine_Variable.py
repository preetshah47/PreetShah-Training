# 0. Find out multiple ways of determining variable data type like integer, string or list.
x = 1
y = '1'
z = [1,2,3]
a = (1,2,3)
b = {1,2,3}
c = True

print(type(a), type(b), type(c), type(x), type(y), type(z))
print(isinstance(x,int))
print(z.__class__)