#!/usr/bin/env python3
"""
mapped declearation
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    """
    base class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    def __repr__(self):
        """
        instance
        """
        return (
                f"<User(email='%s',"
                f"hashed_password='%s',"
                f"session_id='%s',"
                f"reset_token='%s')>"
                % (
                    self.email,
                    self.hashed_password,
                    self.session_id,
                    self.reset_token
                    )
                )
