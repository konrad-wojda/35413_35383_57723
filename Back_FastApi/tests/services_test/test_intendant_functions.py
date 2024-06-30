import unittest

from core.db_src.functions.intendant_functions import *


class TestValidation(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    def test_are_passwords_matched():
        """2 tests for password are matched and 2 failed"""
        assert are_passwords_matched("ala", "ala")
        assert are_passwords_matched("alaALA123!@#", "alaALA123!@#")
        assert are_passwords_matched("alaALA123!", "alaALA123!@#") is False
        assert are_passwords_matched("alaALA123;", "alaALA123;") is False

    @staticmethod
    def test_is_valid_password():
        """password should have lower case, upper case, number and special character #?!@$%^&*- nor length"""
        assert is_valid_password("Ala123@#")
        assert is_valid_password("AAlaa123123123!#!asdadSds")
        assert is_valid_password("Ala12a@") is False  # too short
        assert is_valid_password("Aa@45678911.14.17.20.23.26.29.32.35.38.41.44.47.50.53.56.59.62.65.68.71.74.77.80.") is False  # too long
        assert is_valid_password("ala123@#") is False  # no upper
        assert is_valid_password("ALA123@#") is False  # no lower
        assert is_valid_password("Alaala@#") is False  # no number
        assert is_valid_password("Ala123Ala") is False  # not special character #?!@$%^&*-

    @staticmethod
    async def test_is_valid_passwords():
        """checks if both password are same and both are matching regex... combined test"""
        assert await is_valid_passwords("AlaMa1*!", "AlaMa1*!")
        assert await is_valid_passwords("AlaMaKota1!", "AlaMaKota1!")

        assert await is_valid_passwords("", "AlaMaKota") is False  # different
        assert await is_valid_passwords("AlaMaKota", "") is False  # different
        assert await is_valid_passwords("AlaMaKota123!", "AlaMaKota123") is False  # different

    @staticmethod
    async def test_multiple_email():
        """tests if email matches regex"""
        assert await is_valid_email("AlaMaKota@sasadcom.pl")
        assert await is_valid_email("AlaMaKota@sasad.com.pl")
        assert await is_valid_email("AlaMaKota@sasad.compl") is False  # too long last part
        assert await is_valid_email("AlaM20.23.26.29.32.35.38.41.44.47.50.53.56.59.61@aehit.com.pl") is False  # too long
