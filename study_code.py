sid = '016330641002'
reverse_id = sid[::-1]
l = len(reverse_id)
print(l)
digit = 0
p = 0
c = 1
tot = 0
for c in range(l):
    p = int(reverse_id[c])
    if((c+1) % 2 != 0):
        p = p*2
        if(p > 9):
            p = p - 9
    tot = tot + p
digit = tot % 10
if(digit != 0):
    digit = 10 - digit
print(sid + '-' + str(digit))
   



