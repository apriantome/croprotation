# === Stage 14: Статусы записей ===
# Project: CropRotation
from enum import Enum, auto


class BedLifecycleStatus(Enum):
    """Lifecycle states a garden bed can be in."""
    EMPTY = auto()
    PREPARING = auto()
    PLANTED = auto()
    GROWING = auto()
    HARVESTED = auto()
    RESTING = auto()
    REMOVED = auto()


# Table of allowed transitions between bed lifecycle statuses.
# Each key maps a status to the set of statuses it may transition into.
ALLOWED_TRANSITIONS = {
    BedLifecycleStatus.EMPTY: {
        BedLifecycleStatus.PREPARING,
        BedLifecycleStatus.REMOVED,
    },
    BedLifecycleStatus.PREPARING: {
        BedLifecycleStatus.PLANTED,
        BedLifecycleStatus.RESTING,
        BedLifecycleStatus.REMOVED,
    },
    BedLifecycleStatus.PLANTED: {
        BedLifecycleStatus.GROWING,
        BedLifecycleStatus.HARVESTED,
        BedLifecycleStatus.REMOVED,
    },
    BedLifecycleStatus.GROWING: {
        BedLifecycleStatus.HARVESTED,
        BedLifecycleStatus.PLANTED,
        BedLifecycleStatus.REMOVED,
    },
    BedLifecycleStatus.HARVESTED: {
        BedLifecycleStatus.RESTING,
        BedLifecycleStatus.EMPTY,
        BedLifecycleStatus.PREPARING,
    },
    BedLifecycleStatus.RESTING: {
        BedLifecycleStatus.EMPTY,
        BedLifecycleStatus.PREPARING,
    },
    BedLifecycleStatus.REMOVED: set(),
}


def is_valid_transition(current: BedLifecycleStatus, target: BedLifecycleStatus) -> bool:
    """Return True if target status is reachable from current status."""
    return target in ALLOWED_TRANSITIONS.get(current, set())


def all_possible_transitions(current: BedLifecycleStatus) -> set:
    """Return the set of statuses the given status can transition into."""
    return ALLOWED_TRANSITIONS.get(current, set())


def get_transition_table() -> dict:
    """Return a copy of the allowed transitions table."""
    return {status: set(states) for status, states in ALLOWED_TRANSITIONS.items()}
