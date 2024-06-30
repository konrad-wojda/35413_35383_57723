import unittest

from core.db_src.functions.jwt_functions import *


class TestValidation(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    def test_encode_jwt():
        """checks JWT encoding"""
        assert (encode_jwt({"id_user": 1, "email": "alamakota@com.pl"}) ==
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoxLCJlbWFp"
                "bCI6ImFsYW1ha290YUBjb20ucGwifQ.TveY1uhKzunvwsh9WfVkRZFD1h0-J6Xm1Riw3jOKeHE")
        assert (encode_jwt({"id_user": 3, "email": "aadakota@edu.com.pl"}) ==
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjozLCJlbWFpbCI6ImFhZGFrb3"
                "RhQGVkdS5jb20ucGwifQ.XREqEVl9ExIFPYn9Q0GFRQtMXkHvGR56Xpc5uKMZtCo")

        assert (encode_jwt({"id_user": 1, "email": "aadakota@edu.com.pl"}) ==
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjozLCJlbWFpbCI6ImFhZGFrb3"
                "RhQGVkdS5jb20ucGwifQ.XREqEVl9ExIFPYn9Q0GFRQtMXkHvGR56Xpc5uKMZtCo") is False  # wrong id_user
        assert (encode_jwt({"id_user": 1, "email": "alamaota@com.pl"}) ==
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoxLCJlbWFp"
                "bCI6ImFsYW1ha290YUBjb20ucGwifQ.TveY1uhKzunvwsh9WfVkRZFD1h0-J6Xm1Riw3jOKeHE") is False  # wrong email

    @staticmethod
    async def test_decode_jwt():
        """checks JWT decoding"""
        assert (decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoxLCJlbWFp"
                           "bCI6ImFsYW1ha290YUBjb20ucGwifQ.TveY1uhKzunvwsh9WfVkRZFD1h0-J6Xm1Riw3jOKeHE") ==
                {"id_user": 1, "email": "alamakota@com.pl"}
                )
        assert (decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjozLCJlbWFpbCI6ImFhZGFrb3"
                           "RhQGVkdS5jb20ucGwifQ.XREqEVl9ExIFPYn9Q0GFRQtMXkHvGR56Xpc5uKMZtCo") ==
                {"id_user": 3, "email": "aadakota@edu.com.pl"}
                )

        assert (decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoxLCJlbWFp"
                "bCI6ImFsYW1ha290YUBjb20ucGwifQ.TveY1uhKzunvwsh9WfVkRZFD1h0-J6Xm1Riw3jOKeHE") ==
                {"id_user": 3, "email": "alamakota@com.pl"}
                ) is False  # wrong id_user... 3 instead of 1
        assert (decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjozLCJlbWFpbCI6ImFhZGFrb3"
                "RhQGVkdS5jb20ucGwifQ.XREqEVl9ExIFPYn9Q0GFRQtMXkHvGR56Xpc5uKMZtCo") ==
                {"id_user": 3, "email": "aadakota@edu.com.en"}
                ) is False  # wrong email aadakota@edu.com.en not aadakota@edu.com.pl
