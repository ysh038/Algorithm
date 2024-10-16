import sys

def recursion(new_len):
  if new_len == 1:
    return "-"
  else:
    str_left = recursion(new_len // 3)
    str_mid = " " * (new_len // 3)
    return str_left+str_mid+str_left

while True: 
  try:
    N = int(sys.stdin.readline())

    len = (3 ** N)
    str = ['-'] * len
    result = recursion(len)
    print(result)
  except:
    break
