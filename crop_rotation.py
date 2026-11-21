# === Stage 1: Каркас модуля ===
# Project: CropRotation
from dataclasses import dataclass


@dataclass
class Bed:
    name: str
    area: float
    crop: str
    season: str


def make_demo_beds() -> list[Bed]:
    return [
        Bed("north_row", 2.5, "tomato", "summer"),
        Bed("east_row", 1.8, "lettuce", "spring"),
        Bed("south_row", 3.0, "carrot", "autumn"),
    ]


def main() -> None:
    beds = make_demo_beds()
    for bed in beds:
        print(f"{bed.name}: {bed.crop} ({bed.season}), {bed.area} m^2")


if __name__ == "__main__":
    main()
