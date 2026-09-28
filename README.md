# Privacy-Aware Recommender Lab

> Recommendation lab constrained to explicitly opted-in preferences and minimum cohort support to reduce hidden inference risks.

## Status
**Reproducible prototype** with executable code, tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Recommendation systems can infer sensitive interests from opaque signals. This prototype deliberately restricts ranking to explicit opt-in preferences and suppresses low-support items.

## Architecture
Opted-in user preferences + item features + cohort support → privacy filter → overlap score → deterministic ranking.

## Run
```bash
python -m unittest discover -s tests -v
python privacy_aware_recommender_lab.py
```

## Implemented
- Explicit preference set
- Item feature sets
- Minimum cohort-support threshold
- Content-overlap scoring
- Deterministic top-k ranking
- Tests and CI

## Research lineage
- *Adaptive Recommendation Frameworks Using Hybrid Reinforcement Learning*
- *Privacy-Preserving Architectures for Intelligent Consumer Applications*
- *User Behavior Modeling with Adaptive Feedback Loops*

## Evaluation
Tests verify preference-driven ranking, cohort suppression and non-inference behavior when no preferences are provided.

## Limitations
- Content-based toy model
- No formal differential privacy
- No contextual bandit/RL yet
- No production user data

## License
MIT.

## Extended implementation

- `consent_ledger.py` records preference opt-in/revocation and feeds only the current consent snapshot into recommendation.
