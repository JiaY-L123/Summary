# 汉诺塔
def move(n,a,b,c):
    if n==1:
        print(f'{a}->{c}')
    else:
        move(n-1,a,c,b)
        print(f'{a}->{c}')
        move(n-1,b,a,c)