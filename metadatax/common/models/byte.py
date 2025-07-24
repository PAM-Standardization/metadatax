from django.db import models


class ByteUnit(models.TextChoices):
    """Unit of bytes"""

    BYTE = ("b", "b")
    KILO_BYTE = ("Kb", "Kb")
    MEGA_BYTE = ("Mb", "Mb")
    GIGA_BYTE = ("Gb", "Gb")
    TERA_BYTE = ("Tb", "Tb")
    PETA_BYTE = ("Pb", "Pb")
    EXA_BYTE = ("Eb", "Eb")
    ZETTA_BYTE = ("Zb", "Zb")

    def __lt__(self, other):
        return ORDERED_LIST.index(self) < ORDERED_LIST.index(other)

    def __le__(self, other):
        return ORDERED_LIST.index(self) <= ORDERED_LIST.index(other)

    def __gt__(self, other):
        return ORDERED_LIST.index(self) > ORDERED_LIST.index(other)

    def __ge__(self, other):
        return ORDERED_LIST.index(self) >= ORDERED_LIST.index(other)


ORDERED_LIST = [
    ByteUnit.BYTE,
    ByteUnit.KILO_BYTE,
    ByteUnit.MEGA_BYTE,
    ByteUnit.GIGA_BYTE,
    ByteUnit.TERA_BYTE,
    ByteUnit.PETA_BYTE,
    ByteUnit.EXA_BYTE,
    ByteUnit.ZETTA_BYTE,
]


class Byte:
    def __init__(self, value: int, unit: ByteUnit = ByteUnit.BYTE):
        self.value = value
        self.unit = unit
        super().__init__()

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __eq__(self, other: "Byte") -> bool:
        if not isinstance(other, Byte):
            return False
        return self.value == other.value and self.unit == other.unit

    def __lt__(self, other: "Byte") -> bool:
        if self.unit == other.unit:
            return self.value < other.value
        return self.unit < other.unit

    def __gt__(self, other: "Byte") -> bool:
        if self.unit == other.unit:
            return self.value > other.value
        return self.unit > other.unit

    def __le__(self, other: "Byte") -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other: "Byte") -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __iter__(self):
        return iter([self.value, self.unit])

    def __len__(self) -> int:
        return 2
