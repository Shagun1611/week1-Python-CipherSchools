age=int(input("Enter your age: "))
if age==0:
    print("you can not watch")
elif 0<age<=3:
    print("ticket price : free")
elif 3<age<=10:
    print("ticket price : 150")
elif 10<age<=60:
    print("ticket price: 250")
else:
    print("ticket price:200")
