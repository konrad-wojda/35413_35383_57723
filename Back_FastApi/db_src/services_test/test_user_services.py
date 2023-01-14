import unittest
import db_src.functions.user_functions as services


class TestValidation(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def test_multiple_input_with_not_only_numbers():
        # trzeba przerobić pod wymagania: mała duża, cyfra, znak specjalny, dłuższe niż... a krótsze niż.
        assert await services.validate_passwords("AlaMaKota", "AlaMaKota")
        assert await services.validate_passwords("AlaMaKota1", "AlaMaKota1")
        assert await services.validate_passwords("ala@@", "ala@@")

        assert await services.validate_passwords("", "AlaMaKota") is False
        assert await services.validate_passwords("AlaMaKota", "") is False
        assert await services.validate_passwords("", "") is False

        assert await services.validate_passwords("AlaMaKota1", "alamakota1") is False
        assert await services.validate_passwords("AlaMaKota1", "AlaMaKota") is False
        assert await services.validate_passwords("AlaMaKota", "AlaMaKota2") is False
        assert await services.validate_passwords("AlaMaKota1", "AlaMaKota2") is False
