# === Stage 6: Генерация идентификаторов ===
# Project: CropRotation
import itertools
import string


PROJECT_PREFIX = "cr"


def _uniquify(base: str) -> str:
    candidate = base
    taken: set[str] = set()
    for suffix in itertools.count(1):
        if candidate not in taken:
            taken.add(candidate)
            return candidate
        candidate = f"{base}{suffix}"


class Identifier:
    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Identifier({self.value!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Identifier) and other.value == self.value

    def __hash__(self) -> int:
        return hash(self.value)


class IdentifierGenerator:
    def __init__(self, prefix: str = PROJECT_PREFIX, alphabet: str = string.ascii_lowercase + string.digits) -> None:
        self._prefix = prefix
        self._alphabet = alphabet
        self._available: dict[str, int] = {}
        self._counter = itertools.count(1)

    def generate(self, base: str) -> Identifier:
        raw = _uniquify(base)
        return Identifier(self._prefix + raw)

    def reserve(self, identifier: Identifier) -> None:
        self._available[identifier.value] = self._counter

    def is_available(self, identifier: Identifier) -> bool:
        return identifier.value not in self._available

    def claim(self, identifier: Identifier) -> None:
        if identifier.value in self._available:
            raise ValueError(f"Identifier {identifier.value!r} is already in use")
        self._available[identifier.value] = self._counter

    def release(self, identifier: Identifier) -> None:
        self._available.pop(identifier.value, None)

    def reset(self) -> None:
        self._available.clear()
        self._counter = itertools.count(1)
