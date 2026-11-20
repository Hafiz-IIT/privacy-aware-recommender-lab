from __future__ import annotations

from dataclasses import dataclass, field

from privacy_aware_recommender_lab import Item, recommend


@dataclass
class ConsentLedger:
    preferences: set[str] = field(default_factory=set)
    events: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.preferences, set) or any(
            not isinstance(value, str) or not value.strip() for value in self.preferences
        ):
            raise ValueError("preferences must be a set of non-empty strings")
        self.preferences = {value.strip().casefold() for value in self.preferences}
        if not isinstance(self.events, list) or any(not isinstance(event, str) for event in self.events):
            raise ValueError("events must be a list of strings")

    def opt_in(self, preference: str) -> None:
        if not isinstance(preference, str) or not preference.strip():
            raise ValueError("preference must be a non-empty string")
        normalized = preference.strip().casefold()
        self.preferences.add(normalized)
        self.events.append("opt_in")  # Do not copy potentially sensitive preference text into the audit log.

    def revoke(self, preference: str) -> None:
        if not isinstance(preference, str) or not preference.strip():
            raise ValueError("preference must be a non-empty string")
        normalized = preference.strip().casefold()
        self.preferences.discard(normalized)
        self.events.append("revoke")  # Record the consent action without retaining the preference value.

    def snapshot(self) -> frozenset[str]:
        return frozenset(self.preferences)


def recommend_with_consent(
    items: list[Item],
    ledger: ConsentLedger,
    *,
    min_cohort_support: int = 5,
    top_k: int = 5,
) -> list[tuple[str, float]]:
    if not isinstance(ledger, ConsentLedger):
        raise TypeError("ledger must be a ConsentLedger")
    return recommend(
        items,
        opted_in_preferences=set(ledger.snapshot()),
        min_cohort_support=min_cohort_support,
        top_k=top_k,
    )
