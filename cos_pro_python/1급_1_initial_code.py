from abc import *
import sys

import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
    주문한 메뉴의 전체 가격 Return
'''

class DeliveryStore(metaclass=ABCMeta):
    @abstractmethod
    def set_order_list(self, order_list):
        pass

    @abstractmethod
    def get_total_price(self):
        pass

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PizzaStore:
    def __init__(self):
        menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
        menu_prices = [11100, 12600, 13300, 21000, 19500];
        self.menu_list = []
        for i in range(5):
            self.menu_list.append(Food(menu_names[i], menu_prices[i]))

        self.order_list = []

    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)

    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
        return total_price

def solution(order_list):
    delivery_store = PizzaStore()

    delivery_store.set_order_list(order_list)
    total_price = delivery_store.get_total_price()
    return total_price

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
