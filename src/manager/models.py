from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, Text, JSON, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from src.database import Base


class User(Base):
    __tablename__ = 'user_table'
    index: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[Optional[str]] = mapped_column(server_default="unknown")
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), unique=True, server_default=func.uuid_generate_v4())
    passwordHash: Mapped[str]


class Wallet(Base):
    __tablename__ = 'wallet_table'
    index: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userID: Mapped[UUID] = mapped_column(ForeignKey(User.id, ondelete="CASCADE"))
    # не понимаю в каком виде представить кошелек - какие требования к адресации, так что пока str
    address: Mapped[str] = mapped_column(unique=True, server_default=func.uuid_generate_v4())
    value: Mapped[Optional[float]]







