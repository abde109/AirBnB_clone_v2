#!/usr/bin/python3
"""DBStorage engine for HBnB project."""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

class DBStorage:
    """New Database Storage for HBnB clone"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStorage instance."""
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_pwd = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_db = getenv("HBNB_MYSQL_DB")
        environment = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}",
            pool_pre_ping=True,
        )

        if environment == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Initializes the session for the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        ScopedSession = scoped_session(session_factory)
        self.__session = ScopedSession()

    def all(self, model=None):
        """Queries the database session for all objects or a specific class."""
        object_dict = {}
        model_classes = [User, Place, State, City, Amenity, Review]
        
        if model:
            for item in self.__session.query(model).all():
                key = f"{item.__class__.__name__}.{item.id}"
                object_dict[key] = item
        else:
            for cls in model_classes:
                for item in self.__session.query(cls).all():
                    key = f"{item.__class__.__name__}.{item.id}"
                    object_dict[key] = item
        return object_dict

    def search(self, cls, id):
        """Search for a particular object by its class and id."""
        if cls and id:
            return self.__session.query(cls).get(id)
        return None

    def new(self, obj):
        """Adds a new object to the current session."""
        self.__session.add(obj)

    def save(self):
        """Commits changes in the current session to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Removes an object from the current session."""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes the session."""
        self.__session.close()
