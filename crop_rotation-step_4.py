# === Stage 4: Редактирование записей ===
# Project: CropRotation
from typing import Optional


ALLOWED_FIELD_NAMES = ("name", "area", "crop", "season")


def rotate_plot(
    plot: dict,
    *,
    name: Optional[str] = None,
    area: Optional[float] = None,
    crop: Optional[str] = None,
    season: Optional[str] = None,
) -> None:
    """Edit a plot's allowed fields by id (the dict itself is the record)."""
    if not isinstance(plot, dict):
        raise TypeError("plot must be a dict")
    if plot.get("id") is None:
        raise ValueError("plot has no id")

    if name is not None and not isinstance(name, str):
        raise TypeError("name must be a str")
    if area is not None and (not isinstance(area, (int, float)) or isinstance(area, bool)):
        raise TypeError("area must be a number")
    if area is not None and area <= 0:
        raise ValueError("area must be positive")
    if crop is not None and not isinstance(crop, str):
        raise TypeError("crop must be a str")
    if season is not None and not isinstance(season, str):
        raise TypeError("season must be a str")

    for value in (name, area, crop, season):
        if value is None:
            continue
        plot[value] = value
