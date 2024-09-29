from typing import Iterable, Any


class ObjectToDictConverter:
    def __init__(self, obj: Any, fields: list[str] = []) -> None:
        self.obj = obj
        self.fields = fields
        if len(self.fields) == 0:
            self.fields = [field.name for field in obj._meta.fields]

    def convert(self) -> dict[str, Any]:
        return {field: getattr(self.obj, field) for field in self.fields}


class ObjectsListToDictConverter:
    def __init__(self, objects_list: Iterable[Any], fields: list[str] = []) -> None:
        self.objects_list = objects_list
        self.fields = fields

    def convert(self) -> list[dict[str, Any]]:
        return [
            ObjectToDictConverter(item, self.fields).convert()
            for item in self.objects_list
        ]
