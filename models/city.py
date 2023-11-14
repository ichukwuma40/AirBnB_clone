#!/usr/bin/python3
"""the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """the Class city.

    Attributes:
        state_id (string): The state id.
        name (string): The name.
    """

    state_id = ""
    name = ""
