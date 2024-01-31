
from fastapi import Depends
from src.database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.manager import schemas
from src.manager.models import User, Wallet
from sqlalchemy import select, func, text, union_all
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session
from typing import Union
from sqlalchemy import delete, insert, update
from pydantic import UUID4


async def create_user(user_data: schemas.User):
    try:
        async with async_session() as session:

            user = user_data.login
            no_hash_password = user_data.password
            insertion_user = User(login=user, passwordHash=generate_password_hash(no_hash_password))
            session.add(insertion_user)
            await session.commit()

        return {"user": user_data.login, "status": "OK"}
    except Exception as e:
        return {
            "user": user_data.login,
            "status": "error",
            "error_description": e
        }


async def delete_user(user_name: str):
    try:
        async with async_session() as session:

            stmt = delete(User).where(User.login == user_name)
            await session.execute(stmt)
            await session.commit()

        return {"user": user_name, "status": "deleted"}
    except Exception as e:
        return {
            "user": user_name,
            "status": "error",
            "error_description": e
        }


async def patch_user(user_name: str, user_data: schemas.UserOptions):
    try:
        async with async_session() as session:
            query = select(User).filter(User.login == user_name)
            current_user = await session.execute(query)
            current_user = current_user.first()[0]
            if user_data.password != 'None':
                current_user.password = user_data.password
            if user_data.login != 'None':
                current_user.login = user_data.login

            session.add(current_user)
            await session.commit()

            return {"user": user_name, "status": "updated"}
    except Exception as e:
        return {
            "user": user_name,
            "status": "error",
            "error_description": e
        }


async def get_all_users():
    try:
        async with async_session() as session:
            query = select(User.login, User.id, User.index)
            users = await session.execute(query)
            users = users.scalars()

        return [{"login": user[1], "id": user[2], "index": user[0]} for user in users.fetchall()]
    except Exception as e:
            return {
                "status": "error",
                "error_description": e
            }


async def create_wallet(wallet_user_uuid: UUID4, value: int):
    try:
        async with async_session() as session:

            insertion_wallet = Wallet(userID=wallet_user_uuid, value=value)
            session.add(insertion_wallet)
            await session.commit()

        return {"info": f"wallet for user with userID = {wallet_user_uuid} was added"}
    except Exception as e:
        return {
            "status": "error",
            "error_description": e
        }


async def get_wallets_for_user(user_name: str):
    try:
        async with async_session() as session:
            subquery = select(User.id).where(User.login == user_name)
            query = select(Wallet).where(Wallet.userID == subquery.scalars())

            wallets = await session.execute(query)
            print(wallets.scalars().first())

        return True
    except Exception as e:
        return {
            "status": "error",
            "error_description": e
        }


# async def patch_wallet(user_data, session: AsyncSession = Depends(get_async_session)):
#     async with async_session_maker() as session:
#         pass
#     return True
#
#
# async def get_all_wallets(user_data, session: AsyncSession = Depends(get_async_session)):
#     async with async_session_maker() as session:
#         pass
#     return True
#
#
# async def transaction(user_data, session: AsyncSession = Depends(get_async_session)):
#     async with async_session_maker() as session:
#         pass
#     return True