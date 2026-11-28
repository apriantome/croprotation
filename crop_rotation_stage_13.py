# === Stage 13: Избранное ===
# Project: CropRotation
from dataclasses import dataclass, field
from typing import List, Dict, Set


@dataclass
class GardenBed:
    name: str
    area: float
    crop: str
    season: str
    is_favorite: bool = False

    def toggle_favorite(self) -> bool:
        self.is_favorite = not self.is_favorite
        return self.is_favorite

    def mark_favorite(self) -> None:
        self.is_favorite = True

    def unmark_favorite(self) -> None:
        self.is_favorite = False

    def favorite(self) -> bool:
        return self.is_favorite


class CropRotation:
    def __init__(self):
        self.beds: List[GardenBed] = []
        self.favorites: Set[str] = set()

    def add_bed(self, name: str, area: float, crop: str, season: str) -> GardenBed:
        bed = GardenBed(name=name, area=area, crop=crop, season=season)
        self.beds.append(bed)
        if bed.is_favorite:
            self.favorites.add(bed.name)
        return bed

    def get_favorite_beds(self) -> List[GardenBed]:
        return [bed for bed in self.beds if bed.favorite()]

    def get_favorite_names(self) -> List[str]:
        return sorted(self.favorites)

    def toggle_favorite(self, bed: GardenBed) -> None:
        if bed.favorite():
            self.unmark_favorite(bed)
        else:
            self.mark_favorite(bed)

    def mark_favorite(self, bed: GardenBed) -> None:
        bed.mark_favorite()
        self.favorites.add(bed.name)

    def unmark_favorite(self, bed: GardenBed) -> None:
        bed.unmark_favorite()
        self.favorites.discard(bed.name)

    def is_favorite(self, bed: GardenBed) -> bool:
        return bed.favorite()

    def list_favorites(self) -> str:
        names = self.get_favorite_names()
        if not names:
            return "No favorite beds."
        return ", ".join(names)
