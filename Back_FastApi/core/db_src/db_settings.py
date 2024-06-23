from .getenv_helper import getenv
db_type = getenv('DB_TYPE')


class Settings:
    """
    Settings of DB
    """
    db_type = getenv('DB_TYPE')

    def db_uri(self) -> str:
        """
        Gets URL for DB of currently used type
        :return: URI of DB
        """
        if self.db_type == 'postgres':
            return getenv('DB_POSTGRES_URI')
        if self.db_type == 'lite':
            return getenv('DB_LITE_URI')

    def db_token(self) -> str:
        """
        Gets secret of JWT for currently used DB encryption
        :return: secret of JWT
        """
        if self.db_type == 'postgres':
            return getenv('JWT_SECRET_POSTGRES')
        if self.db_type == 'lite':
            return getenv('JWT_SECRET_LITE')
