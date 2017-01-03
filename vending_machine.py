import algorithms
import abc


class Request:
    def __init__(self, name, coins_added):
        self.item_name = name
        self.money = coins_added
        self._cancel = 0


    def cancelRequest(self):
        self._cancel = 1


    def isRequestCancelled(self):
        return self._cancel


class Inventory:
    def __init__(self):
        self.inventory_list = []


    def add_item(self, item_name, item_price, item_qty):
        self.inventory_list.append({'name': item_name, 'price': item_price, 'quantity': item_qty})


    def get_price(self, it_name):
        for each in self.inventory_list:
            if each['name'] == it_name:
                return each['price']


    def get_qty(self, it_name):
        for each in self.inventory_list:
            if each['name'] == it_name:
                return each['quantity']


    def update_inventory(self, dispensed_item):
        for each in self.inventory_list:
            if each['name'] == dispensed_item:
                each['quantity'] -= 1
            print('Inventory Updated')
            break


class FundManager:
    def __init__(self):
        self.coins_list = []


    def add_coins(self, arr):
        for each in arr:
            self.coins_list.append(each)


    def validate_funds(self, balance):
        if balance < 0:
            return -1
        arr = algorithms.coin_change(self.coins_list, balance)
        if len(arr) > 0:
            return 1
        return 0


    def get_coin_change(self, balance):
        arr = algorithms.coin_change(self.coins_list, balance)
        return arr


    def update_funds(self, arr):
        new_arr = []
        i = 0
        j = 0
        while i < len(arr):
            if arr[i] == self.coins_list[j]:
                i += 1
                j += 1
            else:
                new_arr.append(self.coins_list[j])
                j += 1
        while j < len(self.coins_list):
            new_arr.append(self.coins_list[j])
            j += 1
        self.coins_list = new_arr
        print("The updated coins list is ", self.coins_list)


class ProductDispenser:
    def dispense(self, item_name):
        print("Item dispensed : ", item_name)


class MoneyDispenser:
    def dispense(self, arr):
        print("Money dispensed : ", arr)


class Canceller:
    def cancel(self):
        self.print_cancel_reason()


    @abc.abstractmethod
    def print_cancel_reason(self):
        pass


class UserCancellation(Canceller):
    def print_cancel_reason(self):
        print("The user has cancelled the request. Do you want to request for something else?")


class LimitedDenCancellation(Canceller):
    def print_cancel_reason(self):
        print("Sorry. We don't have the right coins to give you balance for this amount")


class LackingFundsCancellation(Canceller):
    def print_cancel_reason(self):
        print("Sorry. You did not input enough money to get this product.")


class vendingMachine:
    def __init__(self, I, F):
        self.I = I
        self.F = F
        self.Dm = MoneyDispenser()
        self.Dp = ProductDispenser()
        self.C = Canceller()


    def reset_machine(self):
        self.I.inventory_list = []
        self.F.coins_list = []


    def process_request(self, R):
        price = self.I.get_price(R.item_name)
        input_amt = sum(R.money)
        bal = input_amt - price
        if self.F.validate_funds(bal) == 1 and not R.isRequestCancelled():
            balance_coins = self.F.get_coin_change(bal)
            self.Dp.dispense(R.item_name)
            self.Dm.dispense(balance_coins)
            self.I.update_inventory(R.item_name)
            self.F.update_funds(balance_coins)
            return balance_coins
        if R.isRequestCancelled():
            C = UserCancellation()
            C.cancel()
            return 0
        if self.F.validate_funds(bal) == -1:
            C = LackingFundsCancellation()
            C.cancel()
            return 0
        if self.F.validate_funds(bal) == 0:
            C = LimitedDenCancellation()
            C.cancel()
            return 0
