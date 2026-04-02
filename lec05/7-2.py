mart = {"우유":2800, "계란": 300, "빵": 1200, "물": 1700}
cart = []
N = int(input("구매한 물품의 개수를 입력하시오:"))
for i in range(N):
    a= input("구매한 물품을 입력하시오(한개씩):")
    cart.append(a)
total_cost = 0
for item in cart:
    total_cost += mart[item]
print(total_cost)
