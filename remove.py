number = [221,32,69,42,89,22,24,26,40,30,20,45]
for i in number[:]:
    if(i%2==0):
        number.remove(i)
print(number)