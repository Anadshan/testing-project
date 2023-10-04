a = 4
b = 8

if a > 5:
    print(a)
else:
    print(a + b)

print("codition is completed")

# for loop
obj = [1, 2, 5, 6, 8]
for i in obj:
    i = i * 2
    print(i)

# sum of first 5 natural no.
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

#multiplication of natural no.

mul = 1
for i in range(1, 8):
    mul = mul*i
print(mul)

# if we want to jump the index by +2 or +5 instead of +1 then:
print("********************")
for k in range(1, 10, 2):
    print(k)
print("*****skipping first index*****")
for m in range(10):
    print(m)
print("*****while loop*******")
# while loop
t = 10
while t > 1:
    if t >= 9:
        t = t-1
        print(t)
        continue
    if t == 4:
        break

    print(t)
    t = t-1
