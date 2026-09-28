from __future__ import annotations

from dataclasses import dataclass, field

from privacy_aware_recommender_lab import Item, recommend


@dataclass
class ConsentLedger:
    preferences: set[str] = field(default_factory=set)
    events: list[str] = field(default_factory=list)

    def opt_in(self, preference: str) -> None:
        self.preferences.add(preference)
        self.events.append(f"opt_in:{preference}")

    def revoke(self, preference: str) -> None:
        self.preferences.discard(preference)
        self.events.append(f"revoke:{preference}")

    def snapshot(self) -> frozenset[str]:
        return frozenset(self.preferences)


def recommend_with_consent(
    items: list[Item],
    ledger: ConsentLedger,
    *,
    min_cohort_support: int = 5,
    top_k: int = 5,
) -> list[tuple[str, float]]:
    return recommend(
        items,
        opted_in_preferences=set(ledger.snapshot()),
        min_cohort_support=min_cohort_support,
        top_k=top_k,
    )
