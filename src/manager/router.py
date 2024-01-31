

from fastapi import APIRouter, HTTPException, Depends
from typing import List, Union, Optional
from pydantic import UUID4, PositiveFloat
from src.manager import schemas, service


manager_router = APIRouter(
    prefix="/manager",
    tags=["manager router"]
)


@manager_router.post("/users")
async def create_user(user_data: schemas.User):
    result = await service.create_user(user_data)
    return result


@manager_router.get("/users")
async def get_all_users():
    result = await service.get_all_users()
    return result


@manager_router.delete("/users/{user_name}")
async def delete_user(user_name: str):
    result = await service.delete_user(user_name)
    return result


@manager_router.patch("/users/{user_name}")
async def update_user(user_name: str, user_data: schemas.UserOptions):
    result = await service.patch_user(user_name, user_data)
    return result


@manager_router.get("/users/{user_name}/get_wallets")
async def get_wallets(user_name: str):
    result = await service.get_wallets_for_user(user_name)
    return result


@manager_router.post("/make_wallet")
async def create_wallet(wallet_user_uuid: UUID4, value: int = 0):
    result = await service.create_wallet(wallet_user_uuid, value)
    return result


@manager_router.patch("/wallets/{wallet_address}/update_balance")
async def update_wallet(wallet_address: UUID4, wallet_operation: schemas.WalletOperation):
    result = await service.update_wallet(wallet_operation)
    return result


@manager_router.post("/transaction")
async def make_transaction(transaction: schemas.FinTransaction):
    result = await service.make_transaction(transaction)
    return result


