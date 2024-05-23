import unittest

from core.db_src.functions.intendant_functions import *


class TestValidation(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    def test_are_passwords_matched():
        assert are_passwords_matched("ala", "ala")
        assert are_passwords_matched("ala123", "ala123")
        assert are_passwords_matched("ala123ALA", "ala123ALA")
        assert are_passwords_matched("alaALA123!@#", "alaALA123!@#")
        assert are_passwords_matched("alaALA123!", "alaALA123!@#") is False

    @staticmethod
    def test_validate_password():
        assert is_valid_password("Ala123@#")
        assert is_valid_password("Al1@") is False
        assert is_valid_password("Ala12a@") is False
        assert is_valid_password("AAlaa123123123!#!asdadSds")

    @staticmethod
    async def test_validate_passwords():
        assert await is_valid_passwords("AlaMa1*!", "AlaMa1*!")
        assert await is_valid_passwords("AlaMaKota1!", "AlaMaKota1!")
        assert await is_valid_passwords("Aala123@@", "Aala123@@")

        assert await is_valid_passwords("AlaMaKota", "AlaMaKota") is False
        assert await is_valid_passwords("AlaMaKota1", "AlaMaKota1") is False
        assert await is_valid_passwords("ala@@", "ala@@") is False

        assert await is_valid_passwords("", "AlaMaKota") is False
        assert await is_valid_passwords("AlaMaKota", "") is False
        assert await is_valid_passwords("", "") is False

    @staticmethod
    async def test_multiple_email():
        assert await is_valid_email("AlaMaKota@sasad.compl") is False
        assert await is_valid_email("AlaMaKota@sasad.com.pl")
        assert await is_valid_email("AlaMaKota@sasadcom.pl")
        assert await is_valid_email("AlaMaKotaAlaMaKotaAlaMaKotaAlaMaAlaMaKotaAlaMaKota@sasad.com.pl") is False
