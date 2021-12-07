@author: ALEFIA RINI MUTMAINNAH
NIM: 064002100010
"""

def bubbleSort(q):
    count = 0
    for idx in range(len(q)-1):
        if q[idx] > q[idx + 1]:
            q[idx],q[idx + 1] = q[idx + 1],q[idx]
            count += 1
    if count == 0:
        return q
    else:
        bubbleSort(q)

while True:
    while True:
        try:        
            sort = str(input('Insert number : (x,y,z,...)\n~>>> ')).split(',')
            sort = [int(i) for i in sort]
        except:
            print('\nError value entered!\n*Not an integer!')
        else:
            break
    
    print(f'\nList: {sort}')
    
    bubbleSort(sort)
    
    print(f'\nList*: {sort}')
