# === Stage 3: Хранилище в памяти ===
# Project: CropRotation
class GardenBed:
    def __init__(self, bed_id, name, area, crop, season):
        self.bed_id = bed_id
        self.name = name
        self.area = area
        self.crop = crop
        self.season = season

    def __repr__(self):
        return f"GardenBed(id={self.bed_id}, name={self.name}, area={self.area}, crop={self.crop}, season={self.season})"


class BedStorage:
    def __init__(self):
        self._beds = {}

    def add(self, bed):
        if not isinstance(bed, GardenBed):
            raise TypeError("bed must be a GardenBed instance")
        self._beds[bed.bed_id] = bed
        return bed

    def get(self, bed_id):
        return self._beds.get(bed_id)

    def list_all(self):
        return list(self._beds.values())

    def __len__(self):
        return len(self._beds)
