# === Stage 15: История изменений ===
# Project: CropRotation
"""CropRotation Stage 15: Beds change history.

Adds a change log to the Bed entity: what was changed and when.
The history is stored as a list of ChangeEntry records.
"""

from datetime import datetime


class ChangeEntry:
    """A single record describing one modification made to a bed."""

    __slots__ = ("field", "old_value", "new_value", "timestamp")

    def __init__(self, field, old_value, new_value, timestamp):
        self.field = field
        self.old_value = old_value
        self.new_value = new_value
        self.timestamp = timestamp

    def __repr__(self):
        return (
            "ChangeEntry(field={!r}, old={!r}, new={!r}, "
            "timestamp={!r})".format(
                self.field, self.old_value, self.new_value, self.timestamp
            )
        )


class Bed:
    """A garden bed with a change history."""

    def __init__(self, name, area, crop, season):
        self.name = name
        self.area = area
        self.crop = crop
        self.season = season
        self.change_history = []

    def record_change(self, field, old_value, new_value):
        """Append a ChangeEntry for the given field change."""
        entry = ChangeEntry(field, old_value, new_value, datetime.now())
        self.change_history.append(entry)

    def get_history(self):
        """Return a copy of the change history."""
        return list(self.change_history)
