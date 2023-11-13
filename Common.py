from typing import Any


class Util:

    def __init__(self, obj: list):
        self.obj = obj

    def search_by_name(self, name: str) -> Any | None:
        for index, data_name in enumerate(self.obj):
            if data_name.nome == name:
                data = data_name
                return index, data
        return None, None


def util():
    return None