digits = int(input("enter three digits (each digit for one pig):"))

pig1 = digits // 100
pig2 = (digits // 10) % 10
pig3 = digits % 10

sum = pig1 + pig2 + pig3

print("sum:" + str(sum))
print(sum // 3)
print(sum % 3)

check = not(sum % 3)
print(check)
