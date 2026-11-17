"""Preference-overlap recommender prototype.

cohort_support is a supplied count, not a privacy guarantee. This module does
not implement differential privacy, secure aggregation, or cohort verification.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: str
    features: frozenset[str]
    cohort_support: int

    def __post_init__(self):
        if not isinstance(self.item_id, str) or not self.item_id.strip():
            raise ValueError("item_id is required")
        if not isinstance(self.features, frozenset) or any(not isinstance(value, str) or not value.strip() for value in self.features):
            raise ValueError("features must be a frozenset of non-empty strings")
        object.__setattr__(self, "features", frozenset(value.strip().casefold() for value in self.features))
        if not isinstance(self.cohort_support, int) or isinstance(self.cohort_support, bool) or self.cohort_support < 0:
            raise ValueError("cohort_support must be a non-negative integer")


def recommend(
    items: list[Item],
    *,
    opted_in_preferences: set[str],
    min_cohort_support: int = 5,
    top_k: int = 5,
) -> list[tuple[str, float]]:
    if not isinstance(min_cohort_support, int) or isinstance(min_cohort_support, bool) or min_cohort_support < 1:
        raise ValueError("min_cohort_support must be a positive integer")
    if not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    if any(not isinstance(value, str) or not value.strip() for value in opted_in_preferences):
        raise ValueError("opted-in preferences must be non-empty strings")

    normalized_preferences = {value.strip().casefold() for value in opted_in_preferences}
    results: list[tuple[str, float]] = []
    for item in items:
        if item.cohort_support < min_cohort_support:
            continue
        if not normalized_preferences:
            score = 0.0
        else:
            score = len(item.features & normalized_preferences) / len(normalized_preferences)
        results.append((item.item_id, score))

    return sorted(results, key=lambda x: (-x[1], x[0]))[:top_k]


if __name__ == "__main__":
    items = [
        Item("A", frozenset({"ai", "systems"}), 20),
        Item("B", frozenset({"design"}), 20),
    ]
    print(recommend(items, opted_in_preferences={"ai", "systems"}))
