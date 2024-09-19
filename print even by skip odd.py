n = int(input('enter value:'))

count = 0
for i in range(1,n):
    if i%2 != 0:
        continue
    print(i,end=' ')
    count += 1
print()
print('{} is count of val'.format(count))