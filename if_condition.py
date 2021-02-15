txt = 'raja mangala university technology tawan ok'
txt_final = txt.title()
print (txt_final)
for s in txt_final:
    if(s.isupper()):
        print(s,end='')

print('\n--------------------------')

user = input('Your name : ')
lower_user = user.lower()
data = lower_user.split(' ')
f_name = data[0]
l_name = data[1]

final_l = l_name[:3]
print(f_name + '.' + final_l +'@rmutto.ac.th')


