from datetime import datetime 
from typing import Annotated
from sqlalchemy import ForeignKey, func, text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base

int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
bool_default_false = Annotated[bool, mapped_column(nullable=False, server_default=False)]
str_default_free = Annotated[str, mapped_column(nullable=False, server_default="")]
datetime_default_now = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), nullable=False)]
datetime_default_update_now = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())"), nullable=False)]

class UserOrm(Base):
    __tablename__ = 'user'
    id: Mapped[int_pk]
    is_active: Mapped[bool_default_false]
    unsuccessful_logins: Mapped[int] = mapped_column(nullable=False, server_default=0)
    successful_logins: Mapped[str_default_free]
    key: Mapped[str_default_free]
    otp: Mapped[str_default_free]
    def __repr__(self):
        return f"<User(id='{self.id}', is_active='{self.is_active}')>"
    
class JWTOrm(Base):
    __tablename__ = "jwt"
    id: Mapped[int_pk]
    id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    is_authorized: Mapped[bool_default_false]
    revoked: Mapped[bool_default_false]
    issued_at: Mapped[datetime] = mapped_column(nullable=False)
    expires_at: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime_default_now]
    updated_at: Mapped[datetime_default_update_now]
