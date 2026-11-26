# === Stage 11: Слияние записей ===
# Project: CropRotation
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bed:
    name: str
    area: float
    crop: str
    season: str

    def __post_init__(self) -> None:
        if self.area <= 0:
            raise ValueError(f"Bed {self.name!r}: area must be positive")

    def __str__(self) -> str:
        return f"{self.name} | {self.crop} | {self.season} | {self.area} m^2"


@dataclass
class MergeChoice:
    """Winner selection for one field of the merged bed."""

    field: str
    winner: str
    reason: str = ""


@dataclass
class MergedBed:
    """Result of combining two beds, field by field."""

    bed_a: Bed
    bed_b: Bed
    choices: dict[str, MergeChoice] = field(default_factory=dict)

    def field(self, field_name: str) -> str:
        return self.choices[field_name].winner

    def __str__(self) -> str:
        lines = [f"merged bed: {self.bed_a.name} + {self.bed_b.name}"]
        for field_name, choice in self.choices.items():
            lines.append(
                f"  {field_name}: {choice.winner} "
                f"(from {choice.reason or 'bed_a'})"
            )
        return "\n".join(lines)


def merge_beds(
    bed_a: Bed,
    bed_b: Bed,
    *,
    name: str = "a",
    area: str = "a",
    crop: str = "a",
    season: str = "a",
) -> MergedBed:
    merged = MergedBed(bed_a=bed_a, bed_b=bed_b)
    merged.choices = {
        name: MergeChoice(name, bed_a.name, "first bed wins"),
        area: MergeChoice(area, str(bed_a.area + bed_b.area), "sum of areas"),
        crop: MergeChoice(crop, bed_a.crop, "prefer bed_a crop"),
        season: MergeChoice(season, bed_a.season, "prefer bed_a season"),
    }
    return merged


if __name__ == "__main__":
    first = Bed("North", 4.0, "tomato", "summer")
    second = Bed("South", 6.0, "pea", "spring")
    result = merge_beds(first, second)
    print(result)
    print("crop:", result.field("crop"))
    print("area:", result.field("area"))
