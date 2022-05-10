from enum import Enum

from colorama import Fore

from resturant import Menu, Item, Order


class Actions(Enum):
    CONTINUE = 1
    CALCULATE = 2
    EXIT = 3


class ActionsPayment(Enum):
    PAYMENT = 1
    EXIT = 2


def init_menu() -> Menu:
    """ Initital the menu of the resturant """
    
    menu = Menu()

    # adding items
    menu.add_item(Item(1, 'Green apple bubble milk tea', 7.99))
    menu.add_item(Item(2, 'Passion fruit bubble milk green tea', 6.99))
    menu.add_item(Item(3, 'oyster omelette', 12.99))
    menu.add_item(Item(4, 'Stinky tofu', 10.99))
    menu.add_item(Item(5, 'Braised pork on rice with tea egg', 9.99))
    
    return menu


def calculate(order: Order) -> None:
    """ Calculate process of the order """
    
    # show order_items
    order.show_order_items()

    # calculates
    order.get_subtotal()
    order.get_tax()
    order.get_final_total()

    # show results
    order.show_payment_info()
    
    try:
        action = int(input(Fore.GREEN + '1. Payment   2. Exit\n>>> '))
        if action == ActionsPayment.PAYMENT.value:
            payment(order)
        elif action == ActionsPayment.EXIT.value:
            print(Fore.CYAN + 'See you later.')
            return None
    except ValueError as err:
        print(Fore.RED + str(err))
        return None

    return order


def create_order(menu: Menu) -> Order:
    """ Creating order """
    order = Order()
    
    while True: 
        try:
            item_id = int(input(Fore.LIGHTYELLOW_EX + 'Select item you want to buy(just enter the number): '))
            
            # get the item instance
            item = menu.find_item_by_id(item_id)
            if item is None:
                raise ValueError(f'Sorry! item does not found.')
            
            # print the item in the terminal
            item.print()

            # ask the count
            count = int(input(Fore.CYAN + 'How many you want: '))
            if count <= 0:
                raise ValueError(f'Invalid count {count}')
            
            # add to order
            order.add(item, count)

            # what's next
            action = int(input(Fore.GREEN + '1: Continue   2: Pay   3: Exit\n>>> ')) 
            if action == Actions.CONTINUE.value:
                continue
            elif action == Actions.CALCULATE.value:
                calculate(order)
                break
            elif action == Actions.EXIT.value:
                print(Fore.LIGHTYELLOW_EX + 'See you later.')
                break

        except ValueError as err: 
            print(Fore.RED + str(err))
            break 


def payment(order: Order) -> None:
    """ Payment process of order """
    is_paid = False
    if order.final_total != .0:
        try:
            attmept = 3
            while attmept > 0:
                amount = int(input(Fore.WHITE + 'Enter amount of your payment: '))
                if amount < order.final_total:
                    attmept -= 1
                    if attmept != 0:
                        print(Fore.RED + f'Not enough payment. please try again({attmept} attmept left)')
                else:
                    change = amount - order.final_total
                    if change > 0:
                        print(Fore.GREEN + f'Here your change {change}')
                    print(Fore.GREEN + 'Thank you')
                    is_paid = True
                    break

            if not is_paid:
                print('Come back later.')
        except ValueError:
            pass


def main() -> None:
    """ Main """
    menu = init_menu()
    
    print('Menu: ')
    menu.show()
    
    # create order
    create_order(menu)


if __name__ == '__main__':
    main()