menu = [
    {
        'item_id':1,
        'title':'Green apple bubble milk tea',
        'price':7.99
    },
    {
        'item_id':2,
        'title':'Passion fruit bubble milk green tea',
        'price':6.99
    },
    {
        'item_id':3,
        'title':'oyster omelette',
        'price':12.99
    },
    {
        'item_id':4,
        'title':'Stinky tofu',
        'price':10.99
    },
    {
        'item_id':5,
        'title':'Braised pork on rice with tea egg',
        'price':9.99
    },
]


order = []

print('Welcome to Mr.Chu\'s Grottol')
print('Menu:')

for food in menu:
    print(f"{food['item_id']}. {food['title']} ${food['price']}")
print('6. check out')

def get_title_and_price_of_food(item_id):
    # return the food by item_id
    food = list(filter(lambda food:food['item_id'] == item_id, menu))[0]
    return food['title'], food['price']


def get_order_subtotal(order):
    prices = list(map(lambda item:item['price'] * item['count'], order))
    return sum(prices)

def generate_tax_of_order(subtotal):
    return subtotal * 13 / 100

while True:
    try:
        item_id = int(input('Select item you want to buy(just enter the number): '))
        if item_id <= 0 or item_id > 6:
            continue
        elif item_id != 6:
            while True:
                count = int(input('How many you want? '))
                if count <= 0:
                    continue
                else:
                    break
            
            # append to order
            # get the food by item_id
            title, price = get_title_and_price_of_food(item_id)
            order.append({'title':title,'price':price,'count':count})
        elif item_id == 6:
            # paymet stuff
            if order:
                # payment do
                for item in order:
                    print(f"{item['count']} x {item['title']} ${item['price']}")
                subtotal = get_order_subtotal(order)
                tax = generate_tax_of_order(subtotal)
                final_total = subtotal + tax
                print(f'SubTotal : {subtotal}')
                print(f'Tax : {tax}')
                print(f'Total : {final_total}')
                break
            else:
                print('Goodbye for ever')
                break
    except ValueError:
        continue


if order:
    try:
        retires = 3
        while retires > 0:
            amount = int(input('Enter amount of your payment: '))
            if amount < final_total:
                retires -= 1
                if retires != 0:
                    print(f'Not enough payment. please try again({retires} retires left)')
            else:
                change = amount - final_total
                if change > 0:
                    print(f'Here your change {change}')
                print('Thank you')
                break

        if retires == 0:
            print('Come back later.')
    except ValueError:
        pass