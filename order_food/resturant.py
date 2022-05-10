from dataclasses import dataclass, field
from typing import List, Optional

from colorama import Fore


TAX = 13

@dataclass
class Item:
    item_id: int    
    title: str
    price: float

    def print(self) -> None:
        """ Print the item on console """
        print(Fore.GREEN + f"({self.title} ${self.price})")


@dataclass
class OrderItem:
    item: Item
    count: int
    total: int = 0

    def __post_init__(self) -> None:
        # calculate total
        self.total = self.count * self.item.price


@dataclass
class Order:
    order_items: List[OrderItem] = field(default_factory=list)
    subtotal: float = .0
    tax: float = .0
    final_total: float = .0

    def add(self, item: Item, count: int) -> OrderItem:
        """Add item with count to the order_items"""
        order_item = OrderItem(item, count)
        self.order_items.append(order_item)
        return order_item
    
    def get_subtotal(self, as_round: bool = True) -> float:
        """ Calculate the subtotal """
        self.subtotal = sum((order_item.total for order_item in self.order_items))
        if as_round:
            self.subtotal = round(self.subtotal, 2)
        return self.subtotal

    def get_tax(self, as_round: bool = True) -> float:
        """ Calculate the tax """
        self.tax = self.subtotal * TAX / 100
        if as_round:
            self.tax = round(self.tax, 2)
        return self.tax
    
    def get_final_total(self, as_round: bool = True) -> float:
        """ Calculate the final_total """
        self.final_total = self.subtotal + self.tax
        if as_round:
            self.final_total = round(self.final_total, 2)
        return self.final_total
        
        return self.final_total
    
    def show_payment_info(self) -> None:
        """ Show payment information """
        print(Fore.WHITE + f'Subtotal: {self.subtotal}')
        print(Fore.WHITE + f'Tax: {self.tax}')
        print(Fore.WHITE + f'Final Total: {self.final_total}')
    
    def show_order_items(self) -> None:
        """ Show order items """
        for order_item in self.order_items:
            print(Fore.LIGHTBLUE_EX + f'{order_item.count}x: {order_item.item.title} - ${order_item.total}')


@dataclass
class Menu:
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        """Adding item to the items"""
        self.items.append(item)
    
    def show(self) -> None:
        """Show the items in console"""
        for item in self.items:
            print(f"{item.item_id}. {item.title} ${item.price}")

    def find_item_by_id(self, item_id: int) -> Optional[Item]:
        """Find item by id"""
        item = [item for item in self.items if item.item_id == item_id]
        if item:
            return item[0]
        return None
        
        