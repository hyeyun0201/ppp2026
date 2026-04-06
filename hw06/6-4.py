import math

print("각  라디안   sin    cos   tan")
for n in range(1,11):
    rad = math.radians(n)
    print(f"{n} {round(rad,4)} {round(math.sin(rad),4)}  {round(math.cos(rad),4)} {round(math.tan(rad),4)}")
