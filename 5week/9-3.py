def para_func(*args):
    result = 0
    for num in args:
        result += num
    return result

hap = 0

hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("매개변수가 10개인 함수를 호출한 결과 ==> %d" % hap)
