# Evaluation

## Question
What utility/privacy trade-off emerges when recommendations are limited to explicitly consented features and a minimum cohort-support threshold?

## Metrics
- Recommendation utility
- Suppression rate
- Hidden-feature leakage tests
- Ranking stability
- Coverage
- Consent revocation effectiveness

## Implemented privacy boundary
- Recommendation scoring uses only features present in the explicit consent set.
- Items below the supplied minimum cohort-support count are suppressed.
- Consent event records store the action type, not the raw preference text.
- The active preference set still contains preference values in memory.

## Limitations
This prototype does **not** implement differential privacy, secure aggregation, encryption at rest, authenticated user isolation, or independent verification of cohort-support counts. A minimum-support threshold alone is not a formal privacy guarantee. Do not describe this as a differentially private recommender or use it with sensitive user data without a separate security and privacy design.

## Falsification
- Unconsented features affect rank.
- Low-support items leak through.
- Empty preference sets produce personalized inference.
- Revoked preferences continue to influence recommendations.
- Raw preference text appears in the consent event log.
