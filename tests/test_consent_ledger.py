import unittest

from consent_ledger import ConsentLedger, recommend_with_consent
from privacy_aware_recommender_lab import Item


class ConsentLedgerTests(unittest.TestCase):
    def test_revocation_changes_ranking_signal(self):
        ledger = ConsentLedger()
        ledger.opt_in("ai")
        items = [
            Item("A", frozenset({"ai"}), 10),
            Item("B", frozenset({"sports"}), 10),
        ]
        before = recommend_with_consent(items, ledger)
        self.assertEqual(before[0][0], "A")

        ledger.revoke("ai")
        after = recommend_with_consent(items, ledger)
        self.assertEqual(after, [("A", 0.0), ("B", 0.0)])

    def test_events_record_consent_changes(self):
        ledger = ConsentLedger()
        ledger.opt_in("systems")
        ledger.revoke("systems")
        self.assertEqual(ledger.events, ["opt_in:systems", "revoke:systems"])


if __name__ == "__main__":
    unittest.main()
