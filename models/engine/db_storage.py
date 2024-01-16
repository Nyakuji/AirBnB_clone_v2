#!/usr/bin/python3
"""
model to manage DB storage using sqlAlchemy
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


class DBStorage:
    """
    This class manage DB storage for AirBnb
    Clone using sqlAlchemy
    """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """Initialize DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects depending on the class name"""
        from models import classes

        objects = {}
        if cls:
            query_result = self.__session.query(classes[cls]).all()
        else:
            for cls in classes.values():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
         commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def close(self):
        """
        Closing the session
        """
        self.__session.remove()