s = input()

vowles = 'AEIOU'
kevsc = 0
stusc = 0

for i in range(len(s)):
    if s[i] in vowles:
        kevsc += (len(s) - i)
    else:
        stusc += (len(s) - i)

if kevsc > stusc:
    print("Kevin: ", kevsc)
elif stusc > kevsc:
    print("Stuart: ", stusc)
else:
    print("Draw")