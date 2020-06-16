N = int(input())
books = {}

for _ in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_value = max(books.values())
result = []

for k, v in books.items():
    if v == max_value:
        result.append(k)

result.sort()
print(result[0])
