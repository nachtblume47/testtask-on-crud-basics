
from pydantic import UUID4, PositiveFloat
from pydantic import BaseModel, constr
from typing import Union, Optional
from enum import Enum


class User(BaseModel):
    login: constr(max_length=15)
    password: str


class UserOptions(BaseModel):
    login: Optional[constr(max_length=15)] = None
    password: Optional[str] = None


class Wallet(BaseModel):
    userID: Union[int, str]
    address: UUID4
    value: Optional[float]


class Transaction(BaseModel):
    donor_address: UUID4
    receiver_address: UUID4


class BalanceOperationType(Enum):
    PLUS = 'PLUS'
    MINUS = 'MINUS'


class WalletOperation(BaseModel):
    type: BalanceOperationType
    amount: int


class FinTransaction(BaseModel):
    donor: UUID4
    recipient: UUID4
    operationType: BalanceOperationType
