from typing import Iterable, Any


class ObjectToDictConverter:
    def __init__(self, obj: Any, fields: list[str] = []) -> None:
        self.obj = obj
        if len(fields) == 0:
            self.fields = list()
            for field in obj._meta.fields:
                self.fields.append(field.name)

    def convert(self) -> dict[str, Any]:
        item: dict[str, Any] = dict()
        for field in self.fields:
            item[field] = getattr(self.obj, field)
        return item


class ObjectsListToDictConverter:
    def __init__(self, objects_list: Iterable[Any], fields: list[str] = []) -> None:
        self.objects_list = objects_list
        self.fields = fields

    def convert(self) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        for item in self.objects_list:
            items.append(ObjectToDictConverter(item, self.fields).convert())
        return items
