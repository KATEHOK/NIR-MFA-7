from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=False)
    unsuccessful_logins = Column(Integer, nullable=False, default=0)
    successful_logins = Column(String(150), nullable=False, default="")
    key = Column(String(150), nullable=False, default="")
    otp = Column(String(150), nullable=False, default="")
    def __repr__(self):
        return f"<User(id='{self.id}', is_active='{self.is_active}')>"
    
class JWT(Base):
    __tablename__ = "jwt"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")
    is_authorized = Column(Boolean, nullable=False, default=False)
    issued_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    revoked = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    