#festivaloffers85%
#weekendoffers65%
soaps=25
shampoo=50
dress=850
print("welcome to python mall")
cname=input("Enter customer name:")
cphno=input("enter a number:")
itq1=int(input("enter no soaps"))
itq2=int(input("enter no shampoo"))
itq3=int(input("enter no dress"))
bill=(soaps*itq1)+(shampoo*itq2)+(dress*itq3)
pc=input("enter pc")
if pc=='festivaloffer':
    disc=bill*85/100
elif pc=='weekendoffer':
    disc=bill*65/100
elif bill>=1000:
        disc=bill*10/100
elif bill>=500:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc     
gst=tbill*12/100
obill=tbill+gst 
print("customer name:",cname)
print("customer phno:",cphno)
print("bill:",bill)
print("discount:",disc)
print("gst 12%:",gst)
print("bill to be paid:",obill)
print("thankyou! visit again")
        
