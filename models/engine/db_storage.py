#!/usr/bin/python3
from models.base_model import Base
from sqlalchemy import create_engine
form sqlalchemy.orm import sessionmaker

from os import getenv

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}
class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        self.HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        self.HBNB_MYSQL_HOST = 'localhost'
        self.HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(self.HBNB_MYSQL_USER,
                                            self.HBNB_MYSQL_PWD,
                                            self.HBNB_MYSQL_HOST,
                                            self.HBNB_MYSQL_DB),
                                    pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()

        if getenv(HBNB_ENV) == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls != None:
            query_rows = self.__session.query(cls)
            for row in query_rows:
                print(row)
        else:
            pass

    def new(self, obj):
        self.__session.add(obj)
        self.__session.commit()
