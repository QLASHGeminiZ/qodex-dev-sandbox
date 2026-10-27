"""Display-name formatting for the synthetic Qodex integration fixture."""


def normalise_display_name(value: str) -> str:
    """Trim the ends of a Unicode display name."""
    if not isinstance(value, str):
        raise TypeError("display name must be text")
    return value.strip()
