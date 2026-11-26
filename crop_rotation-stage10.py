# === Stage 10: Поиск дубликатов ===
# Project: CropRotation
def normalize_field(value):
    if value is None:
        return ""
    return str(value).strip().lower()


def find_duplicate_beds(beds):
    seen = {}
    duplicates = []
    for bed in beds:
        key = (
            normalize_field(getattr(bed, "name", None)),
            normalize_field(getattr(bed, "area", None)),
            normalize_field(getattr(bed, "crop", None)),
            normalize_field(getattr(bed, "season", None)),
        )
        if key in seen:
            duplicates.append((key, seen[key], bed))
        else:
            seen[key] = bed
    return duplicates


def format_duplicate_report(duplicates):
    if not duplicates:
        return "No duplicate beds found."
    lines = ["Duplicate beds found:"]
    for key, first, second in duplicates:
        lines.append(
            f"  '{first.name}' (area={first.area}, crop={first.crop}, "
            f"season={first.season}) == '{second.name}' "
            f"(area={second.area}, crop={second.crop}, season={second.season})"
        )
    return "\n".join(lines)
