# Privacy-Aware Recommender Lab

<p align="center"><strong>Recommendation With Explicit Consent Boundaries</strong><br/><sub>Rank only from opted-in preferences and suppress weak-support signals.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20prototype-blue" alt="Prototype"/> <img src="https://img.shields.io/badge/focus-consent%20%2B%20privacy-purple" alt="Privacy"/></p>

## Question

**Can a recommender be designed so that personalization depends on explicit user consent rather than hidden inference?**

```
Opted-in preferences
        +
Item features
        +
Cohort support
        ↓
Privacy filter
        ↓
Overlap score
        ↓
Deterministic ranking
```

## Try it

```bash
python privacy_aware_recommender_lab.py
python -m unittest discover -s tests -v
```

`consent_ledger.py` records opt-in/revocation events and feeds only the current consent snapshot into recommendation.

## Implemented

- explicit preference set
- minimum cohort support
- content-overlap scoring
- deterministic top-k ranking
- consent ledger
- revocation
- audit events
- deterministic CI

## Boundary

This is a controlled recommendation prototype, not a privacy certification or production recommender.

Related: [Predictive Intelligence Platform](https://github.com/Hafiz-IIT/predictive-intelligence-platform) · [Memory Governor](https://github.com/Hafiz-IIT/memory-governor)
