
def making_plus(x):
    def make(n):
        return x+n
    return make

make_5 = making_plus(5)
print(make_5(4))

def reverse_title_case(s):
    x = s.split()
    x = [i[:-1]+i[-1].upper() for i in x]
    s = " ".join(x)
    return s
s = "hello world how are you"
print(reverse_title_case(s))

def simple(n):
    n = str(n)
    return int(n) == sum([ int(n[i])**(i+1) for i in range(len(n)) ])
print(simple(89))
a = 1
b = 100
print(list( filter( simple,range(a,b))))

def simple(n):
    n = str(n)
    return int(n) == sum([ int(n[i])**(i+1) for i in range(len(n)) ])
print(list( filter( simple,range(1,100))))


def move_zero(li):
    l = len(li)
    li = list(filter(lambda x:x!=0,li))
    for i in range(l-len(li)): li.append(0)
    return li
lis = [0,6,4,3,0,7,0,6,5]
print(move_zero(lis))

def product_pair(li,n):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]*li[j]==n: return [li[i],li[j]]
    return None
lis = [1,2,3,4]
print(product_pair(lis,2))
print(product_pair(lis,15))