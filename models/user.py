#!/usr/bin/python3

"""
Module that defines the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
