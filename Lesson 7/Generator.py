def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1
res = raise_to_the_degrees(2, 500)
print(res)
for _ in res:
    print(_)