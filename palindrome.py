s = 'abccba'
n = 3
ml = n*2
valid = True
for i in range(n):
    l = s[i]
    r = s[ml-1-i]
    print(l,r)
    if l!=r:
        valid = False
if valid:
    print('yes it is a palindrome')
else:
    print('no it not a palindrome')
