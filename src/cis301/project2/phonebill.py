from typing import list
from cis301.phonebill.abstract_phonebill import AbstractPhoneBill

class Phonebill(AbstractPhoneBill):
    def __init__(self,owner,bill):
        self.__owner = owner
        self.__phonecalls = list()
        self.bill = bill
    def ger_customer(self) -> str:
        return self.__owner
    def add_phonecall(self,phonecall):
        bill += phonecall
    def get_phonecalls(self) -> List[T]:
        pass