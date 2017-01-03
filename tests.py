import unittest
import vending_machine


class mainTestClass(unittest.TestCase):
    def setUp(self):
        self.I = vending_machine.Inventory()
        self.I.add_item('Coke', 15, 4)
        self.I.add_item('Candy', 3, 4)
        self.I.add_item('Redbull', 5, 5)
        self.F = vending_machine.FundManager()
        self.F.add_coins([1, 2, 2, 3, 5])

        self.VM = vending_machine.vendingMachine(self.I, self.F)


    def test_cancelRequest(self):
        R = vending_machine.Request('test_item', [0, 0])
        R.cancelRequest()
        self.assertEquals(1, R.isRequestCancelled())


    def test_getPrice(self):
        self.assertEquals(15, self.I.get_price('Coke'))


    def test_validateFunds(self):
        self.assertEquals(1, self.F.validate_funds(7))


    def test_getCoinChange(self):
        expected = [3, 5]
        self.assertEquals(expected, self.F.get_coin_change(8))


    def test_update_funds(self):
        expected = [1, 2, 2]
        self.F.update_funds([3, 5])
        self.assertEquals(expected, self.F.coins_list)


    def test_vending_machine_process_request(self):
        print('Testing process request')
        R = vending_machine.Request('Candy', [5])
        ret_val = self.VM.process_request(R)
        self.assertEquals([2], ret_val)
        print('Process request tested')


    def test_vending_machine_process_request_errors(self):
        print('Testing error paths')
        R = vending_machine.Request('Coke', [30, 30])
        ret_val = self.VM.process_request(R)
        self.assertEquals(0, ret_val)
