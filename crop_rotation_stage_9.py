# === Stage 9: Постраничный вывод ===
# Project: CropRotation
from collections.abc import Sequence


def page_range(total, page_number, page_size):
    if page_size < 1:
        raise ValueError("page_size must be at least 1")
    if page_number < 1:
        raise ValueError("page_number must be at least 1")
    return range((page_number - 1) * page_size, min(total, page_number * page_size))


def paginate(items, page_number=1, page_size=10):
    if not isinstance(items, Sequence):
        raise TypeError("items must be a sequence of beds")
    total = len(items)
    start, end = page_range(total, page_number, page_size)
    return list(items[start:end]), total, page_number, page_size


def build_links(base_url, total, page_number, page_size):
    params = {"page": page_number, "size": page_size}
    queries = ["&".join(f"{key}={value}" for key, value in params.items())]
    if page_number > 1:
        queries.append(f"{base_url}?page={page_number - 1}&size={page_size}")
    if page_number * page_size < total:
        queries.append(f"{base_url}?page={page_number + 1}&size={page_size}")
    return ["<".join(f'<a href="{url}">{label}</a>' for url, label in zip(queries, ["prev", "next"]))]
