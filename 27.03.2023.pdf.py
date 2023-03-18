models = [
    {"name": "model1", "id": 1},
    {"name": "model2", "id": 2},
    {"name": "model3", "id": 3},
    {"name": "model4", "id": 4},
]

for model in models:
    model["name"] = f"{model['name']} ({model['id']})"


for model in models:
    if model["id"] % 2 != 0:
        models.remove(model)











n = int(input())
sum_all = n * (n + 1) // 2
sum_left = sum(int(input()) for _ in range(n-1))
lost_card = sum_all - sum_left
print(lost_card)


n = int(input())
i = 1
while i**2 <= n:
    print(i**2)
    i += 1