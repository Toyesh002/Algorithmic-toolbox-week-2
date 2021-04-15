# Uses python3
def calc_fib(n):
    if(n<=1):
        return n
    prevnum=0
    curnum=1
    for i in range(1,n):
        prevprevnum=prevnum
        prevnum=curnum
        curnum=prevnum+prevprevnum
    return curnum%10
n = int(input())
print(calc_fib(n))
