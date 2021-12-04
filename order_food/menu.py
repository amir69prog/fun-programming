menu = [
    {
        'item':1,
        'name':'Green Apple Bubble Milk Tea',
        'price':7.99,
    },
    {
        'item':2,
        'name':'Passion Fruit Bubble Green Tea',
        'price':6.99,
    },
    {
        'item':3,
        'name':'Oyster Omelette',
        'price':12.99,
    },
    {
        'item':4,
        'name':'Stinky Tofu',
        'price':10.99,
    },
    {
        'item':5,
        'name':'Braised Pork on rice with tea egg ',
        'price':9.99,
    },
]

order = []

def get_data_of_item(item_id):
    item = list(filter(lambda food: item_id == food['item'], menu))
    item = item[0]
    return item['price'], item['name']


def get_order_subtotal(order):
    prices = list(map(lambda order: order['price'], order))
    subtotal = sum(prices)
    return subtotal


def generate_tax_of_subtotal(subtotal):
    tax = subtotal * 13 / 100
    return tax


def get_final_total(subtotal, tax):
    return subtotal + tax


title = 'Welcome to Mr.Chu\'s Grottol'
print(title, 'Menu:',sep='\n')

for food in menu:
    template_text = '{}. {} ${}'.format(food['item'], food['name'], food['price'])
    print(template_text)

print('{}. {}'.format('6', 'Check out.'))

while True:
    try:
        action = int(input('Select the item you want to buy(just enter the number): '))
        if action > 6 or action <= 0:
            continue
        elif action != 6:
            while True:
                count = int(input('How many you want? '))
                if count <= 0:
                    continue
                break
            price, name = get_data_of_item(action)
            order.append({'price':price, 'name':name, 'count':count})
        elif action == 6:
            if order:
                print('Your order')
                for item in order:
                    template_text = '{} x {}. ${}'.format(item['count'], item['name'], item['price'])
                    print(template_text)
                subtotal = get_order_subtotal(order)
                tax = generate_tax_of_subtotal(subtotal)
                total = get_final_total(subtotal, tax)
                print('Subtotal: ${}'.format(subtotal))
                print('Tax: ${}.'.format(tax))
                print('Total: ${}'.format(total))
                break
            else:
                print('Order is empty.')
                break
    except:
        continue


if order:
    retries = 3
    while retries > 0:
        try:
            paymet_amount = float(input('Enter the amount of your payment: '))
            if paymet_amount < total:
                # the amout is lower than total
                retries -= 1
                if retries != 0:
                    print(f'Not enough payment, please try again ({retries} retries left)')
            else:
                # the amount id bigger or equal to the total
                change = paymet_amount - total
                if change != 0:
                    print(f'Transaction approved! Your change is ${change}')
                print('Thank you for dining at Mr.Chu\'s Grotto, see you again soon!')
                break
        except:
            pass

    if retries == 0:
        print("Sorry you don't have enough money and you've reached the maximum amount of retries. Come back again  later")