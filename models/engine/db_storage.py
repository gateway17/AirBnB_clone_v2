#!/usr/bin/python3
""" New engine DBStorage: (models/engine/db_storage.py)"""

class DBStorage():
    """Storage data in Databse """
    __engine = None
    __session = None

    def __init__(self):
        """Initiaze engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)



    Base.metadata.create_all(engine)

    cities = relationship("City", back_populates="state")
