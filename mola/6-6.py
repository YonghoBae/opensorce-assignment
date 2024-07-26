hap = 0
a, b = 0, 0

while True:
    a = input('더할 첫 번째 수를 입력하세요: ')
    if a=='$':
        break
    b = int(input('더할 두 번째 수를 입력하세요: '))
    hap = int(a)+b
    print('%s + %d = %d' %(a, b, hap))

print("$를 입력해 반복문을 탈출했습니다.")
