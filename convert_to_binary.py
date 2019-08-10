num = 10
# rev_bin=''
# while num >0:
#     rem = num%2
#     rev_bin = rev_bin+str(rem)
#     num = num//2

# list = list(rev_bin)
# list.reverse()
# print(''.join(list))

from stack import stack

s = stack()
while num >0:
     rem = num%2
     s.push(rem)
     num = num//2

r =''
while not s.isEmpty():
    r += str(s.pop())

print(r)