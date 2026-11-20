import unittest

from privacy_aware_recommender_lab import Item, recommend


class PrivacyAwareRecommenderTests(unittest.TestCase):
    def test_preference_overlap_ranks_item(self):
        items = [
            Item("A", frozenset({"ai", "systems"}), 10),
            Item("B", frozenset({"sports"}), 10),
        ]
        self.assertEqual(recommend(items, opted_in_preferences={"ai"})[0][0], "A")

    def test_low_support_item_suppressed(self):
        items = [Item("rare", frozenset({"ai"}), 2)]
        self.assertEqual(recommend(items, opted_in_preferences={"ai"}, min_cohort_support=5), [])

    def test_invalid_top_k_and_privacy_threshold_are_rejected(self):
        with self.assertRaises(ValueError):
            recommend([], opted_in_preferences=set(), top_k=0)
        with self.assertRaises(ValueError):
            recommend([], opted_in_preferences=set(), min_cohort_support=1)

    def test_duplicate_item_ids_are_rejected(self):
        items = [Item("A", frozenset({"ai"}), 10), Item("A", frozenset({"systems"}), 10)]
        with self.assertRaises(ValueError):
            recommend(items, opted_in_preferences={"ai"})

    def test_empty_preferences_do_not_infer_hidden_interests(self):
        items = [Item("A", frozenset({"ai"}), 10), Item("B", frozenset({"sports"}), 10)]
        result = recommend(items, opted_in_preferences=set())
        self.assertEqual(result, [("A", 0.0), ("B", 0.0)])


if __name__ == "__main__":
    unittest.main()
