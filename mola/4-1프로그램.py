money, c500, c100, c50, c1 = 0, 0, 0, 0, 0

money = int(input("지폐로 교환할 돈은 얼마?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 50000원짜리 ==> %d개"%c500)
print(" 10000원짜리 ==> %d개"%c100)
print(" 5000원짜리 ==> %d개"%c50)
print(" 1000원짜리 ==> %d개"%c10)
print("지폐로 바꾸지 못한 잔돈 ==> %d원"%money)
