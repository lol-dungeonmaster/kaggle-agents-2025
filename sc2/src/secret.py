import os

class UserSecretsClient:
    @classmethod
    def set_secret(cls, id: str, value: str):
        os.environ[id] = value
    @classmethod
    def get_secret(cls, id: str):
        try:
            return os.environ[id]
        except KeyError as e:
            print(f"KeyError: authentication token for {id} is undefined")