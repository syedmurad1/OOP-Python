# for item in sequence:
# statement(s) 

for letter in "Syed":
    print(letter)

print("--------------------------------------------------------")
friends=["Tom","Ali"]
for fr in friends:
    print(fr)

print("--------------------------------------------------------")
for num in range(4):
    print(num)
print("--------------------------------------------------------")
for num in range(1,4):
    print(num)

print("--------------------------------------------------------")

number=int(input("enter an integer: "))
for num in range(1,4):
    cal=number* num
    print(number, "X", num, "=", cal)

print("--------------------------------------------------------")
fr1=["Tom","Ali","M"]
for num in range(len(fr1)): # len(friends)
    print(fr1[num])

print("--------------------------------------------------------")
for num in range(5):
    if num ==0:
        print ("first")
    else:
        print("not")