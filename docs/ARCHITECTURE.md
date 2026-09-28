# Architecture

Opted-in user preferences + item features + cohort support → privacy filter → overlap score → deterministic ranking.

## Invariants
1. Features not explicitly opted in must not influence score.
2. Low-support items below threshold must be suppressed.
3. Empty preferences must not trigger hidden-interest inference.
