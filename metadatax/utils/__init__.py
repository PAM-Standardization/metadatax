def admin_display_min_max(obj: dict | object, min_key: str, max_key: str) -> str:
    obj = obj.__dict__
    if not obj[min_key] and not obj[max_key]:
        return "-"
    if not obj[max_key]:
        return f"> {obj[min_key]}"
    if not obj[min_key]:
        return f"< {obj[max_key]}"
    if obj[min_key] == obj[max_key]:
        return f"{obj[min_key]}"
    return f"{obj[min_key]} - {obj[max_key]}"
