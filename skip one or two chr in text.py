s = input('enter value: ') #python

count = 0
for i in s:
    if i == 't' or i == 'o':
        continue
    print(i,end='')
    count += 1
print()
print('{} is count of val'.format(count))
print('-'*50)

for i in s:
    if i in ['t','o']:
        continue
    print(i,end='')