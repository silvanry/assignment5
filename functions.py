def hello():
    print("this is my first function")
hello()
def calculate():
    x=90
    y=59
    print(x*y)
calculate()
def majina(fname, lname):
    print(fname+ " "+lname)
majina("Joshua", "Kimmich")
def greetings(name, greeting="hello"):
    print(greeting +" "+name)
greetings("Joshua")
greetings("niaje", "Freddy")

def majina(Tname, point):
    print(Tname + " " + point)
majina("Chelsea", "90")
def maxvalue(a, b, c, d, e ,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,9,1,8,17,45)
print(result)

def minvalue(a, b, c, d, e ,f):
    return min(a,b,c,d,e,f)
result=minvalue(7,9,1,8,17,45)
print(result)
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4])
print(answer)

def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(10)