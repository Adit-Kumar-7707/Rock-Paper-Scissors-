import random as r
s=0
d={1:'Rock',2:'Paper',3:'Scissors'}
for i in range(5):
    user=int(input('''
1:Rock
2:Paper
3:Scissors
Enter Here : '''))
    comp=r.randint(1,3)
    print(f'User : {d[user]} V/s Computer : {d[comp]}')
    if user==comp:
        print(f'Draw !')
    elif (user==1 and comp==3) or (user==2 and comp==1) and (user==3 and comp==2):
        print('Win !')
        s+=1
    else:
        print('Lost !')
        s-=1
# print(f"\nTotal Score : {s}")
    if s>0:
        print(f'You Won!\nScore : {s}')
    elif s<0:
        print(f'Computer Won!\nScore : {s}') 
    else:
        print('Draw !')
