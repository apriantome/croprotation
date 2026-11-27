# === Stage 12: Массовое обновление ===
# Project: CropRotation
from typing import List, Dict, Callable, Optional


# Mapping of crop names to their preferred predecessor crops.
CROP_PREDCESSOR_MAP: Dict[str, List[str]] = {
    "tomato": ["potato", "legume", "lettuce"],
    "cucumber": ["legume", "onion", "garlic"],
    "potato": ["legume", "lettuce", "onion"],
    "cabbage": ["legume", "onion", "garlic"],
    "lettuce": ["tomato", "potato", "bean"],
    "bean": ["cabbage", "carrot", "tomato"],
    "onion": ["cabbage", "potato", "corn"],
    "garlic": ["cabbage", "cucumber", "bean"],
    "carrot": ["cabbage", "bean", "potato"],
    "corn": ["bean", "lettuce", "cabbage"],
    "legume": ["corn", "cabbage", "onion"],
}


def _normalize(name: str) -> str:
    return name.strip().lower()


def find_beds_by_condition(
    beds: List[Dict],
    condition: Callable[[Dict], bool],
) -> List[Dict]:
    """Return only the beds that satisfy the given predicate."""
    return [bed for bed in beds if condition(bed)]


def compute_succession_crop(crop: str) -> Optional[str]:
    """Return the first suitable predecessor crop for the given crop."""
    key = _normalize(crop)
    if key not in CROP_PREDCESSOR_MAP:
        return None
    for predecessor in CROP_PREDCESSOR_MAP[key]:
        if _normalize(predecessor) not in {
            _normalize(bed.get("crop", "")) for bed in beds
        }:
            return predecessor
    return None


def preview_changes(
    beds: List[Dict],
    condition: Callable[[Dict], bool],
    crop: Optional[str] = None,
) -> List[Dict]:
    """Build a preview of the changes that would be applied to the beds.

    Each entry describes the bed and the fields that would change.
    """
    affected = find_beds_by_condition(beds, condition)
    preview: List[Dict] = []
    for bed in affected:
        entry: Dict = {
            "bed_name": bed.get("name", ""),
            "area": bed.get("area", 0),
            "season": bed.get("season", ""),
        }
        if crop is not None:
            entry["old_crop"] = bed.get("crop", "")
            entry["new_crop"] = crop
        preview.append(entry)
    return preview


def apply_changes(
    beds: List[Dict],
    condition: Callable[[Dict], bool],
    crop: Optional[str] = None,
    season: Optional[str] = None,
) -> int:
    """Apply the changes to the beds in place and return the number updated."""
    affected = find_beds_by_condition(beds, condition)
    count = 0
    for bed in affected:
        if crop is not None:
            bed["crop"] = crop
        if season is not None:
            bed["season"] = season
        count += 1
    return count


def main() -> None:
    sample_beds: List[Dict] = [
        {"name": "Bed A", "area": 2.0, "crop": "tomato", "season": "summer"},
        {"name": "Bed B", "area": 1.5, "crop": "cabbage", "season": "spring"},
        {"name": "Bed C", "area": 3.0, "crop": "tomato", "season": "summer"},
        {"name": "Bed D", "area": 1.0, "crop": "bean", "season": "spring"},
    ]

    def is_tomato(bed: Dict) -> bool:
        return _normalize(bed.get("crop", "")) == "tomato"

    preview = preview_changes(sample_beds, is_tomato, crop="potato")
    print("Preview of changes:")
    for change in preview:
        print(change)

    updated = apply_changes(
        sample_beds, is_tomato, crop="potato", season="autumn"
    )
    print(f"Updated {updated} beds.")
    for bed in sample_beds:
        print(bed)


if __name__ == "__main__":
    main()
