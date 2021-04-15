n=int(input())
a=[int(x) for x in input().split()]

a.sort()

for x in a:
    print(int(a[-1])*int(a[-2]))
    break
