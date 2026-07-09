from dtos.acc_info import AccInfo


class Calculation:
    def addition(self, acc_info: AccInfo, amount: int):
        acc_info.balance += amount

    def substraction(self, acc_info: AccInfo, amount: int):
        if 0 < acc_info.balance - amount:
            acc_info.balance -= amount
        else:
            print("Insuffient Balance")
