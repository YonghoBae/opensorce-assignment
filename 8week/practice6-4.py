from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    ccnt = 0
    scnt = 0

    while k < n - 1:
        last = n - 1
        print(f'패스 {k + 1}')
        for j in range(n - 1, k, -1):
            ccnt += 1
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                      ' +' if a[j - 1] > a[j] else ' -'),
                                      end = '')
                print(f'{a[n - 1]:2}')
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                scnt += 1
                last = j
        k = last
        print(f'비교를 {ccnt}번 했습니다.')
        print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print("버블 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')