# задача 13-1
print('задача 13-1')
def plus_minus():
    n=1
    while True:
        if n%2==0:
            yield -n
            n+=1
        else:
            yield n
            n+=1
            

gf = plus_minus()
for i in range(20):
    print(next(gf), end=' ')

print()

# задача 13-2
print('задача 13-2')
def nums():
    i=1
    while True:
        if(str(i)==str(i)[::-1]):
            yield i
            i+=1
        else:
            i+=1
            

gf_2 = nums()
for i in range(20):
    print(next(gf_2), end=' ')

print()

# задача 13-3
print('задача 13-3')
nums = list(map(int, input('Введите список целых чисел: ').split()))
def odd_numbers(nums):
    for i in nums:
        if i%2==1:
            yield i

gf_3 = odd_numbers(nums)
for s in gf_3:
    print(s, end = " ")