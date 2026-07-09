import json
import os
from datetime import datetime
from typing import List, Optional

from dtos.acc_info import AccInfo, AddresInfo
from engines.calculation import Calculation
from interfaces.operations import IOperations


class OptionsEngine(Calculation, IOperations):
    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path
        self.acc_infos: Optional[List[AccInfo]] = None
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, 'r') as f:
                json_data = f.read()
                if json_data.strip():
                    data_list = json.loads(json_data)
                    self.acc_infos = []
                    for item in data_list:
                        addres_data = item.get('Addres') or item.get('addres')
                        addres = None
                        if addres_data:
                            addres = AddresInfo(
                                pin=addres_data.get('Pin') or addres_data.get('pin'),
                                city=addres_data.get('City') or addres_data.get('city'),
                                state=addres_data.get('State') or addres_data.get('state')
                            )
                        acc_info = AccInfo(
                            name=item.get('Name') or item.get('name'),
                            date=item.get('Date') or item.get('date'),
                            balance=item.get('Balance') or item.get('balance', 0),
                            acc_no=item.get('AccNo') or item.get('acc_no', 0),
                            addres=addres
                        )
                        self.acc_infos.append(acc_info)
                else:
                    self.acc_infos = []
        else:
            self.acc_infos = []

    def _save_data(self):
        data_list = []
        if self.acc_infos:
            for acc in self.acc_infos:
                acc_dict = {
                    'Name': acc.name,
                    'Date': acc.date,
                    'Balance': acc.balance,
                    'AccNo': acc.acc_no,
                    'Addres': {
                        'Pin': acc.addres.pin if acc.addres else None,
                        'City': acc.addres.city if acc.addres else None,
                        'State': acc.addres.state if acc.addres else None
                    } if acc.addres else None
                }
                data_list.append(acc_dict)
        with open(self.json_file_path, 'w') as f:
            json.dump(data_list, f, indent=2)

    def acc_detail(self):
        acc_no = int(input("Enter Account No: "))
        acc_info = next((x for x in self.acc_infos if x.acc_no == acc_no), None)
        if acc_info is not None:
            print("Account Detail")
            print(json.dumps({
                'Name': acc_info.name,
                'Date': acc_info.date,
                'Balance': acc_info.balance,
                'AccNo': acc_info.acc_no,
                'Addres': {
                    'Pin': acc_info.addres.pin if acc_info.addres else None,
                    'City': acc_info.addres.city if acc_info.addres else None,
                    'State': acc_info.addres.state if acc_info.addres else None
                } if acc_info.addres else None
            }))
            print("*****************")
        else:
            print("Account not present")

    def create_acc(self):
        now = datetime.now()
        acc_info = AccInfo()
        addres = AddresInfo()
        
        acc_info.name = input("Full Name: ")
        addres.city = input("City: ")
        addres.state = input("State: ")
        addres.pin = int(input("Pin: "))
        acc_info.date = now.strftime("%d/%m/%Y")
        acc_info.balance = 0
        acc_info.acc_no = int(now.strftime("%M%H%S"))
        acc_info.addres = addres
        
        if self.acc_infos is not None:
            self.acc_infos.append(acc_info)

    def delete_acc(self):
        acc_no = int(input("Account Number: "))
        if self.acc_infos:
            del_ind = next((i for i, x in enumerate(self.acc_infos) if x.acc_no == acc_no), -1)
            if del_ind >= 0:
                self.acc_infos.pop(del_ind)

    def deposit_mony(self):
        acc_no = int(input("Enter Account No: "))
        acc_info = next((x for x in self.acc_infos if x.acc_no == acc_no), None)
        if acc_info is not None:
            amount = int(input("Enter your amount: "))
            if 0 < amount < 10000:
                self.addition(acc_info, amount)
            else:
                print("Enter correct amount")
        else:
            print("Account not present")

    def update_acc(self):
        acc_name = input("Full Name: ")
        acc_pin = int(input("Pin: "))

        acc_info = next((x for x in self.acc_infos if x.name == acc_name and x.addres and x.addres.pin == acc_pin), None)
        if acc_info is None:
            print("Account is not present")
            return
        
        print("Update city type - 1")
        print("Update state type - 2")
        option = input()
        
        if option == "1":
            if acc_info.addres:
                acc_info.addres.city = input("City name: ")
        elif option == "2":
            if acc_info.addres:
                acc_info.addres.state = input("State name: ")
        else:
            print("Choose proper option")

    def withwrew_mony(self):
        acc_no = int(input("Enter Account No: "))
        acc_info = next((x for x in self.acc_infos if x.acc_no == acc_no), None)
        if acc_info is not None:
            amount = int(input("Enter your amount: "))
            if 0 < amount < 10000:
                self.substraction(acc_info, amount)
            else:
                print("Enter correct amount")
        else:
            print("Account not present")
