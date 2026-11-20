# Privacy model and limitations

The recommender ranks items by overlap with explicitly opted-in preference tags and suppresses items whose caller-supplied cohort-support count is below a configured threshold.

## Consent behavior
- Only preferences present in the ConsentLedger snapshot are used for scoring.
- Revocation removes a preference from subsequent snapshots.
- Consent event strings record the action type, not the preference value.

## Important limitations
- cohort_support is caller-supplied and is not verified against a population database.
- A threshold of two is only a basic suppression rule; it is not k-anonymity, differential privacy, secure aggregation, or a re-identification risk assessment.
- The in-memory ledger is not durable, authenticated, tamper-evident, or connected to downstream deletion systems.
- The score is exact tag overlap, not a validated recommendation model.
- Do not use real personal or sensitive preference data in this prototype.
