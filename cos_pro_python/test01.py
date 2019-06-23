'''
    "XS", "S", "M", "L", "XL", "XXL"
'''

category = list(["XS", "S", "M", "L", "XL", "XXL"])
print(category)

required_amt = list([1, 0, 2, 3, 1, 0])
print(required_amt)

for a, b in zip(category, required_amt):
    print(a, b)

required_size = list(["XS", "S", "L", "L", "XL", "S"])
print(required_size)

answer = [0 for _ in required_size]
print(answer)

for i, v in enumerate(required_size):
    if v == "XS":
        answer[0] += 1
    elif v == "S":
        answer[1] += 1
    elif v == "M":
        answer[2] += 1
    elif v == "L":
        answer[3] += 1
    elif v == "XL":
        answer[4] += 1
    elif v == "XXL":
        answer[5] += 1

print(answer)
