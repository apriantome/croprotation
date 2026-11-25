# === Stage 8: Группировка ===
# Project: CropRotation
from collections import Counter


def group_by_area(beds):
    """Group beds by their area and count how many beds fall into each group."""
    buckets = {}
    for bed in beds:
        key = bed["area"]
        buckets.setdefault(key, []).append(bed)
    return buckets


def count_groups(beds):
    """Return the number of distinct area groups among the given beds."""
    return len(group_by_area(beds))


def summarize_areas(beds):
    """Return a Counter-like mapping of area value to the number of beds."""
    return Counter(bed["area"] for bed in beds)


if __name__ == "__main__":
    sample = [
        {"name": "bed_1", "area": 2.0, "crop": "tomato", "season": "summer"},
        {"name": "bed_2", "area": 2.0, "crop": "cucumber", "season": "summer"},
        {"name": "bed_3", "area": 4.0, "crop": "pea", "season": "spring"},
        {"name": "bed_4", "area": 2.0, "crop": "carrot", "season": "spring"},
        {"name": "bed_5", "area": 4.0, "crop": "bean", "season": "spring"},
    ]

    grouped = group_by_area(sample)
    for area in sorted(grouped):
        print(f"area={area} count={len(grouped[area])} beds={grouped[area]}")

    print("number_of_groups:", count_groups(sample))
    print("area_summary:", summarize_areas(sample))
