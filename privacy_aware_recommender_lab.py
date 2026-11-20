from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: str
    features: frozenset[str]
    cohort_support: int

    def __post_init__(self) -> None:
        if not isinstance(self.item_id, str) or not self.item_id.strip():
            raise ValueError("item_id must be non-empty")
        if any(not isinstance(value, str) or not value.strip() for value in self.features):
            raise ValueError("item features must be non-empty strings")
        if isinstance(self.cohort_support, bool) or not isinstance(self.cohort_support, int) or self.cohort_support < 0:
            raise ValueError("cohort_support must be a non-negative integer")


def recommend(
    items: list[Item],
    *,
    opted_in_preferences: set[str],
    min_cohort_support: int = 5,
    top_k: int = 5,
) -> list[tuple[str, float]]:
    if (isinstance(min_cohort_support, bool) or not isinstance(min_cohort_support, int)
            or min_cohort_support < 2):
        raise ValueError("min_cohort_support must be an integer >= 2")
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    if any(not isinstance(value, str) or not value.strip() for value in opted_in_preferences):
        raise ValueError("opted-in preferences must be non-empty strings")
    item_ids = [item.item_id for item in items]
    if len(item_ids) != len(set(item_ids)):
        raise ValueError("item IDs must be unique")

    results: list[tuple[str, float]] = []
    for item in items:
        if item.cohort_support < min_cohort_support:
            continue
        if not opted_in_preferences:
            score = 0.0
        else:
            score = len(item.features & opted_in_preferences) / len(opted_in_preferences)
        results.append((item.item_id, score))

    return sorted(results, key=lambda x: (-x[1], x[0]))[:top_k]


if __name__ == "__main__":
    items = [
        Item("A", frozenset({"ai", "systems"}), 20),
        Item("B", frozenset({"design"}), 20),
    ]
    print(recommend(items, opted_in_preferences={"ai", "systems"}))
