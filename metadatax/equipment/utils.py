def byte_to_readable(byte: int):
    num = byte
    for unit in (
        "b",
        "Kb",
        "Mb",
        "Gb",
    ):
        if abs(num) < 1000:
            return f"{int(num)}{unit}"
        num /= 1000
    return f"{int(num)}Tb"


def readable_to_byte_unit(readable: str) -> (int, str):
    offset = 1
    if readable[-2:] in ["Kb", "Mb", "Gb"]:
        offset = 2
    return readable[:-offset], readable[-offset:]


def byte_unit_to_byte(byte: int, unit: str) -> int:
    if not byte:
        return byte
    num = byte
    if unit == "Kb":
        num *= 1_000
    if unit == "Mb":
        num *= 1_000_000
    if unit == "Gb":
        num *= 1_000_000_000
    if unit == "Tb":
        num *= 1_000_000_000_000
    return num


def byte_to_byte_unit(byte: int) -> (int, str):
    return readable_to_byte_unit(byte_to_readable(byte))
