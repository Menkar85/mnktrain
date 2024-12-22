pizza = {
    'Pepperoni': {'consist': ['pepperoni', 'mozarella', 'tomato sause'],
                  'size_price': {'S': 395, 'M': 545}},
    'Margharitta': {'consist': ['tomatoes', 'mozarella', 'tomato sause'],
                  'size_price': {'S': 395, 'M': 545}},
    'Hawaian': {'consist': ['chicken', 'ham', 'pineapple', 
                            'mozarella', 'tomato sause'],
                  'size_price': {'S': 415, 'M': 595}},
}

print(pizza['Hawaian']['size_price']['M'])