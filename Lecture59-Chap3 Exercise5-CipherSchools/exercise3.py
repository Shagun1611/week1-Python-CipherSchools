name=input("Enter your name: ")
i=0
while i<len(name):
    y=name[i]
    print(f"{y} : {name.count(y)}")
    i=i+1 