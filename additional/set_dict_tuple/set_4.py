basket = {'Old castle': {'count': 2, 'price': 28490},
        'Boots': {'count': 1, 'price': 2399},
        'Book': {'count': 2, 'price': 437}
}

sum = 0
for item in basket:
    sum += basket[item]['price'] * basket[item]['count']

print(sum)