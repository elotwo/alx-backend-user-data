#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:

            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password) ->User:
        """
        adding user
        """
        new_user = User(
                email='email',
                hashed_password='hashed_password',
                session_id='None',
                reset_token='None',
                )
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs) ->User:
        if not kwargs:
            raise ValueError("no keyword argumnet")
        try:
            user = self._session.query(User).filter_by(**kwargs).first()

            if user is None:
                raise NoResultFound("invalid")
            return user

        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid query arguments: {e}")

    def update_user(self, user_id:int, *kwargs) ->None:
        if not kwargs:
            raise ValueError("No attributes provided to update")

        try:
            find = self.find_user_by(id=user_id)

            


