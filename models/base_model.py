#!/usr/bin/python3
"""
Module for BaseModel class
"""
from datetime import datetime
import uuid
import models

class BaseModel:
    """
    Class that is the base of other models
    """

    count = 0
    def __init__(self, *args, **kwargs):
        """
        Constructor of class BaseModel instance
        """
        if kwargs is not None and len(kwargs) != 0:
            for i in kwargs:
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    kwargs[i] = datetime.strptime(kwargs[i],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, i, kwargs[i])
            BaseModel.count += 1
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(tz=None)
            self.updated_at = self.created_at
            models.storage.new(self)
            BaseModel.count += 1

    def __str__(self):
        """
        String representation of the instance created
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all keys and values of instance
        Filters data that starts with underscores, methods, and functions.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
