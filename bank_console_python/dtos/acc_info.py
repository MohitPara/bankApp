from dataclasses import dataclass
from typing import Optional


@dataclass
class AddresInfo:
    pin: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None


@dataclass
class AccInfo:
    name: Optional[str] = None
    date: Optional[str] = None
    balance: int = 0
    acc_no: int = 0
    addres: Optional[AddresInfo] = None
