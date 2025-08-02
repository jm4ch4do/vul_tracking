import abc
import typing as _t
import uuid as _uuid

_T = _t.TypeVar("_T")


class BaseInMemoryRepo(_t.Generic[_T]):

    id = "id"
    _storage: _t.List[_t.Dict[str, _t.Any]]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._storage = []

    def list_all(self) -> _t.List[_T]:
        return [self._to_entity(raw) for raw in self._storage]

    def add(self, entity: _T) -> None:
        if not getattr(entity, self.id):
            setattr(entity, self.id, str(_uuid.uuid4()))
        self._storage.append(self._serialize(entity))

    def get_by_id(self, entity_id: str) -> _t.Optional[_T]:
        for raw in self._storage:
            if raw[self.id] == entity_id:
                return self._to_entity(raw)
        return None

    def remove(self, entity_id: str) -> bool:
        for i, raw in enumerate(self._storage):
            if raw[self.id] == entity_id:
                del self._storage[i]
                return True
        return False

    def clear(self) -> None:
        self._storage.clear()

    def populate(self, entities: _t.List[_T]) -> None:
        self._storage = [self._serialize(entity) for entity in entities]

    @abc.abstractmethod
    def _to_entity(self, raw: _t.Dict[str, _t.Any]) -> _T:
        pass

    @abc.abstractmethod
    def _serialize(self, entity: _T) -> _t.Dict[str, _t.Any]:
        pass
