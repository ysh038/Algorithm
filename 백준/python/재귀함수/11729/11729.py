import sys

N = int(sys.stdin.readline())

def recursion(n,start,mid,end):
  if n == 1:
    print(start,end)
    return
  recursion(n-1,start,end,mid)
  print(start,end)
  recursion(n-1,mid,start,end)
print(2 ** N - 1)
recursion(N,1,2,3)




import sys

N = sys

def recursion(n,start,mid,end):
  if n == 1:
    print(start,end)
    return
  recursion(n-1,start,end,mid)
  print(start,end)
  recursion(n-1,mid,start,end)

print(2**N - 1)
recursion(N,1,2,3)