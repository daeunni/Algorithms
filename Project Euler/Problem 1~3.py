# Problem 1
s = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        s = s + i
    else:
        pass
    
print(s)


# Problem 2
n1 = 0
n2 = 1
n3 = n1+n2
result = 0

while n3<=4000000:
  n3 = n1+n2
  # print(n3)
  n1 = n2
  n2 = n3

  if n3 % 2==0:
    result += n3

print('result_sum : ', result)

# Problem 3
a = 600851475143 
i = 2 
num = []
while (i<=a):
    if a%i==0:  
        num.append(i)
        a = a//i   # 이게 열쇠이다!
    i = i+1
print(max(num))


