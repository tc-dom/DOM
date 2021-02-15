grade = int(input('intput your point'))
fullname = input('Input your name')

if(grade>=80):
    print("%s Your Grade is A" %fullname)
elif(grade>=75):
    print("%s Your Grade is B+" %fullname);
elif(grade>=70):
    print("%s Your Grade is B" %fullname);
elif(grade>=65):
    print("%s Your Grade is C+" %fullname);
elif(grade>=60):
    print("%s Your Grade is C" %fullname);
elif(grade>=55):
    print("%s Your Grade is D+" %fullname);
elif(grade>=50):
    print("%s Your Grade is D" %fullname);
else:
    print("%s Strange Grade..!!" %fullname);