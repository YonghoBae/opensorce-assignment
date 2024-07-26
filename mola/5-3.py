n = int(input('***숫자를 입력하세요: '))
if n==2:
    print(f'{n}는 소수입니다')
        
for i in range(3,n):
    if n%i == 0:
        print(f'{n}는 소수가 아닙니다.')
        break
    elif i >= n//2:
        print(f'{n}는 소수입니다.')
        break
        
    
