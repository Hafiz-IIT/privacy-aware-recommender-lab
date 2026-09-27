# Architecture

```mermaid
flowchart LR
    N0[opt-in preferences] --> N1
    N1[cohort-support filter] --> N2
    N2[feature overlap] --> N3
    N3[score] --> N4
    N4[deterministic ranking]
```

## User input
Only explicit opted-in preference features enter scoring.

## Support gate
Items below the minimum cohort-support threshold are suppressed.

## Scoring
Overlap with explicit preferences produces a simple interpretable score.

## Ranking
Results are sorted deterministically; empty preferences do not trigger hidden inference.

## Design principle
When privacy is the priority, absence of preference data should mean ‘do not infer’, not ‘guess harder’.
