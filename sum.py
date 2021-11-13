string = "hello54236726hdfjds"
sum=0
for s in string:
    if(s.isdigit()):
        sum = sum+int(s)

print("sum is :", sum)