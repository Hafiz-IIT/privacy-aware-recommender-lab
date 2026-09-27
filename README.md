# Privacy-Aware Recommender Lab

> **Recommend only from explicit opt-in preferences and suppress low-support signals instead of inferring hidden interests.**

Personalization can quietly become inference about information a user never chose to provide. This repository explores a deliberately constrained recommendation baseline using only opt-in preferences plus a minimum cohort-support threshold.

## Implemented
- item feature representation
- explicit opt-in preference set
- content-overlap scoring
- minimum cohort-support gate
- deterministic ranking
- no hidden-preference inference when preference set is empty

## Run
```bash
python -m unittest discover -s tests -v
python privacy_aware_recommender_lab.py
```

## Repository map
- `privacy_aware_recommender_lab.py` — implementation
- `tests/` — tests
- `examples/` — example input
- `docs/architecture.md` — architecture
- `docs/research-agenda.md` — experiments + research lineage
- `STATUS.md` — claims boundary
- `CITATION.cff` — citation

## Pipeline
**opt-in preferences → cohort-support filter → feature overlap → score → deterministic ranking**

## Research lineage
This links the Personal AI/Life OS work with the older adaptive-recommendation, privacy-preserving architecture, user-behavior, and ethical consumer-AI research directions.

## Evaluation direction
Compare utility and exposure under different minimum-support thresholds and preference sparsity. Future work can introduce formal privacy mechanisms without relabeling this simple gate as differential privacy.

## Maturity
**Research prototype.** This is not differential privacy, federated learning, k-anonymity certification, or a production recommender. The privacy behavior is a design constraint, not a formal guarantee.
