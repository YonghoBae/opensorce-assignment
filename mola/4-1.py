money, c50, c10, c5, c1 = 0, 0, 0, 0, 0

money = int(input("지폐로 교환할 돈은 얼마?"))

c50 = money // 50000
money %= 50000

c10 = money // 10000
money %= 10000

c5 = money // 5000
money %= 5000

c1 = money // 1000
money %= 1000

print("\n 50000원짜리 ==> %d개"%c50)
print(" 10000원짜리 ==> %d개"%c10)
print(" 5000원짜리 ==> %d개"%c5)
print(" 1000원짜리 ==> %d개"%c1)
print("지폐로 바꾸지 못한 잔돈 ==> %d원"%money)
