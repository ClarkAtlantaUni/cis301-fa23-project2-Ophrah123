from typing import list
from cis301.phonebill.abstract_phonecall import AbstractPhoneCall

class PhoneCall(AbstractPhoneCall):
    def __init__(self,caller,calle,starttime,endtime):
        self.__caller = caller
        self.__calle = calle
        self.__starttime = starttime
        self.__endtime = endtime

    def get_caller(self) -> str:
        return
    def get_callee(self) -> str:
        return

    def get_starttime(self) -> date:
        return
    def get_starttime_atring(self) -> str:
        starttime = str(starttime)

    def get_endtime(self) -> date:
        return
    def get_endtime_string(self) -> str:
        endtime = str(endtime)