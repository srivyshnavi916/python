sno=int(input('enter sno'))
sname=input('enter student name')
group=input('enter student group')
s1=int(input('enter maths marks'))
s2=int(input('enter phy marks'))
s3=int(input('enter cs marks'))
total=s1+s2+s3
avg=total
if avg>=90:
    print('O GRADE')
elif avg>=80:
    print('A GRADE')
elif avg>=70:
    print('B GRADE')
elif avg>=60:
    print('C GRADE')
elif avg>=50:
    print('D GRADE')
else:
    print('Pass')
