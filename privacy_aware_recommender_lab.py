from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: str
    features: frozenset[str]
    cohort_support: int


def recommend(
    items: list[Item],
    *,
    opted_in_preferences: set[str],
    min_cohort_support: int = 5,
    top_k: int = 5,
) -> list[tuple[str, float]]:
    if min_cohort_support < 1:
        raise ValueError("min_cohort_support must be >= 1")

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
