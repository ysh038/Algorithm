import sys

N = int(sys.stdin.readline())
rect = []

def recursion(new_N):
  if new_N == 1:
    return "*"
  else:
    stars = recursion(new_N // 3)
    array = []

    for star in stars:
      array.append(star * 3)
    for star in stars:
      array.append(star + ' ' * (new_N // 3) + star)
    for star in stars:
      array.append(star * 3)
    
    return array

print('\n'.join(recursion(N)))
