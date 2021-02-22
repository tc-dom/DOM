การโปรแกรมคอมพิวเตอร์ 1

1.สร้างตัวแปรขึ้นมา แล้วเก็บข้อมูล ชื่อ นามสกุล และรหัสนักศึกษาของตัวเอง

my_data = 'Thammanoon Chumnit 016330641020-6'
2.แสดงผลข้อมูลของตัวแปรจากข้อ 1 ในรูปแบบรหัสนักศึกษา วรรค และชื่อเต็ม

global my_data
track_data = my_data.split()
fullName = track_data[0]+track_data[1] 
print (track_data[2]+' '+fullName)
016330641020-6 ThammanoonChumnit
3.เขียนโปรแกรมรับค่าจากแป้นพิมพ์เพื่อเก็บชื่อ และนามสกุล เป็นภาษาอังกฤษของตัวเอง

f_name = input('intput your first name: ')
l_name = input('Input your last name: ')
intput your first namethammanoon
Input your last nameChumnit
4.แสดงผลข้อมูลของตัวแปรจากข้อ 3 ในรูปแบบชื่อเต็มโดยให้ตัวอักษรตัวแรกของชื่อและนามสกุลแสดงเป็นตัวพิมพ์ใหญ่

global f_name,l_name
s_name = f_name+' '+l_name
print(s_name.title())
Thammanoon Chumnit
5.เขียนโปรแกรมรับค่ารหัสนักศึกษาของตัวเองจากทางแป้นพิมพ์ แล้วให้แสดงผลว่ารหัสนักศึกษาที่ป้อน เข้าศึกษาเมื่อปี พศ.ใด

('คุณเริ่มเข้าศึกษาเมื่อปี
code = str(input('intput your student_code: '))
ema = list(code)
yea_code = (ema[2]+ema[3])
print('คุณเริ่มเข้าศึกษาเมื่อปี 25'+yea_code)
intput your student_code: 016330641020-6
คุณเริ่มเข้าศึกษาเมื่อปี 2563
6.เขียนโปรแกรมรับค่าตัวเลขจากทางแป้นพิมพ์ 6ตัว จากนั้นให้แสดงตัวเลขที่มากที่สุดและน้อยที่สุดออกมา

some
lst = [] 
for i in range(0, 6): 
    ele = int(input('Enter some number : ')) 
    lst.append(ele)
print(max(lst))
print('ค่าที่มากที่สุด คือ '+ str(max( lst )) + ' - ค่าที่น้อยที่สุด คือ ' + str(min( lst )))
​
Enter some number : 10
Enter some number : 20
Enter some number : 20
Enter some number : 50
Enter some number : 40
Enter some number : 10
50
ค่าที่มากที่สุด คือ 50 - ค่าที่น้อยที่สุด คือ 10
7.เขียนโปรแกรมรับusernameและpasswordเพื่อเปรียบเทียบกับที่กำหนดใว้ใน(หากผิดจะให้ใส่ใหม่) ถ้าตรงกันให้แสดงข้อความ Access grant หากผิด 3ครั้งให้จบการทำงาน

print('LOGIN')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='JQD' and username=='DQM':
        print('Access grant')
        break
    else:
        print('Someting went wrong Access denied. Try again.')
        count += 1
​
LOGIN
Enter username: dqm
Enter password: jqd
Someting went wrong Access denied. Try again.
Enter username: DQM
Enter password: JQD
Access grant
8.สร้างฟังก์ชันแบบส่งค่ากลับเพื่อคำนวนหาเเส้นรอบวง และหาพื้นที่ของวงกลม

circle = 0
def redius(num):
    try:
        global circle
        num = int(num)
        circle = num*3.14 
        return circle;
    except:
        return ('Cannot calculate');
​
levi = input('intput redius of circle : ')
print(redius(levi))
​
intput your student_code: s1
Cannot calculate
9.สร้างฟังก์ชันที่สามาถรับพารามิเตอร์ตัวเดียวหรือหลายตัวได้ เพื่อรับค่าตัวเลขแล้วคำนวนหาค่าเฉลี่ยออกมา

def Average(lst): 
    return sum(lst) / len(lst) 
​
lst = [] 
n = int(input('ต้องการป้อนตัวเลขกี่ชุด: '))
for i in range(0, n): 
    ele = int(input('ป้อนตัวเลข : ')) 
    lst.append(ele)
print(Average(lst))
ต้องการป้อนตัวเลขกี่ชุด: 4
ป้อนตัวเลข : 10
ป้อนตัวเลข : 20
ป้อนตัวเลข : 10
ป้อนตัวเลข : 10
12.5
10.เขียนโปรแกรมให้แสดงสูตรคูณแม่ 1 - 12 โดยใช้ฟังก์ชัน

#กำหนดขนาดแต่ละช่องของหัวตาราง
title = "{0:>9}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}" \
         "{7:>4}{8:>4}{9:>5}{10:>5}{11:>4}"
#เนื้อหา
tables = "{0:>3}{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}" \
          "{6:>4}{7:>4}{8:>4}{9:>4}{10:>5}{11:>5}{12:>4}"
print(" :----------------------------------------------------:")
print(title.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
print(" :-------------------แม่สูตรคูณ-------------------------:")
​
for i in range(1, 13):
    print(tables.format(str(i) + ":", i*1, i*2, i*3, i*4, i*5, i*6,
                         i*7, i*8, i*9,  i*10, i*11, i*12))
print(" :----------------------------------------------------:")
 :----------------------------------------------------:
        1   2   3   4   5   6   7   8   9   10   11  12
 :-------------------แม่สูตรคูณ-------------------------:
 1:     1   2   3   4   5   6   7   8   9   10   11  12
 2:     2   4   6   8  10  12  14  16  18   20   22  24
 3:     3   6   9  12  15  18  21  24  27   30   33  36
 4:     4   8  12  16  20  24  28  32  36   40   44  48
 5:     5  10  15  20  25  30  35  40  45   50   55  60
 6:     6  12  18  24  30  36  42  48  54   60   66  72
 7:     7  14  21  28  35  42  49  56  63   70   77  84
 8:     8  16  24  32  40  48  56  64  72   80   88  96
 9:     9  18  27  36  45  54  63  72  81   90   99 108
10:    10  20  30  40  50  60  70  80  90  100  110 120
11:    11  22  33  44  55  66  77  88  99  110  121 132
12:    12  24  36  48  60  72  84  96 108  120  132 144
 :----------------------------------------------------: