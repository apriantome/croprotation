# === Stage 5: Связи между сущностями ===
# Project: CropRotation
from collections import namedtuple


Planting = namedtuple("Planting", ["id", "bed", "crop", "season", "yield_kg"])


def get_all_plantings(bed):
    """Return a list of all plantings for a given bed."""
    return [p for p in all_plantings() if p.bed == bed]


def check_integrity(bed):
    """Verify that every planting for a bed references a valid bed name."""
    plantings = get_all_plantings(bed)
    return all(p.bed is not None for p in plantings)


def list_plantings(bed):
    """List all plantings for a given bed with their crop and season."""
    plantings = get_all_plantings(bed)
    return [(p.crop, p.season, p.yield_kg) for p in plantings]


def plant_crop(bed, crop, season, yield_kg):
    """Add a new planting to the given bed."""
    planting = Planting(
        id=len(all_plantings()) + 1,
        bed=bed,
        crop=crop,
        season=season,
        yield_kg=yield_kg,
    )
    all_plantings().append(planting)
    return planting


def all_plantings():
    """Return the full list of plantings."""
    return []


if __name__ == "__main__":
    bed = "bed_1"
    plant_crop(bed, "tomato", "summer", 5.0)
    plant_crop(bed, "cucumber", "summer", 3.0)
    print(list_plantings(bed))
    print(check_integrity(bed))
