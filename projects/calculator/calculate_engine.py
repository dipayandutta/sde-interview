"""
This is the main calculation point
"""

from addition import Addition
from division import Division
from multiplication import Multiplication
from operations import operations
from subtraction import Subtraction


class CalculateEngine:
    def __init__(self):

        for key, value in operations.items():
            print(value)
