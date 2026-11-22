# === Stage 2: Проверка полей ===
# Project: CropRotation
import re


def normalize_text(value):
    """Return the trimmed, lower-cased, whitespace-collapsed string."""
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip().lower()


def normalize_area(value):
    """Return a positive float area parsed from a string like '1.5 m2'."""
    if value is None or str(value).strip() == "":
        raise ValueError("Area must not be empty")
    match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", str(value))
    if not match:
        raise ValueError("Area must be a number, e.g. '1.5'")
    area = float(match.group())
    if area <= 0:
        raise ValueError("Area must be greater than zero")
    return area


def normalize_season(value):
    """Return a season from a list of accepted values."""
    seasons = {"spring", "summer", "autumn", "winter"}
    normalized = normalize_text(value)
    if normalized not in seasons:
        raise ValueError(
            "Season must be one of: spring, summer, autumn, winter"
        )
    return normalized


def validate_plot(name, area, crop, season):
    """Validate a plot's fields and return a normalized plot dictionary."""
    normalized_name = normalize_text(name)
    if not normalized_name:
        raise ValueError("Plot name must not be empty")
    if len(normalized_name) > 50:
        raise ValueError("Plot name must be at most 50 characters long")

    normalized_area = normalize_area(area)

    normalized_crop = normalize_text(crop)
    if not normalized_crop:
        raise ValueError("Crop must not be empty")
    if len(normalized_crop) > 40:
        raise ValueError("Crop name must be at most 40 characters long")

    normalized_season = normalize_season(season)

    return {
        "name": normalized_name,
        "area": normalized_area,
        "crop": normalized_crop,
        "season": normalized_season,
    }
