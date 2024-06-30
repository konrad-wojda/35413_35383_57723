import unittest

from core.db_src.functions.student_functions import *

ref = {1: 'Śniadanie', 2: 'II Śniadanie', 3: 'Obiad', 4: 'Kolacja'}
person = ['Adam', 'Nowak', '1a', '4', '3', '2', '1']


class TestValidation(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    def test_format_presence():
        """changing ID of meals into attendance"""
        assert format_presence(person, ref) == ['Obecny', 'Obecny', 'Obecny', 'Obecny']

    @staticmethod
    async def test_format_person():
        """creating csv file content"""
        assert format_person(person, ref) == "Adam;Nowak;1a;Obecny;Obecny;Obecny;Obecny"

