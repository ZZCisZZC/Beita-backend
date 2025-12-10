"""配对与排名核心逻辑单元测试。使用 unittest 避免额外依赖。"""
import unittest
from go_pairing_system.models import Player
from go_pairing_system.pairing import pair_players, apply_results
from go_pairing_system.ranking import rank_players


class PairingTestCase(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player(id=f"p{i}", name=f"选手{i}", number=i) for i in range(1, 9)
        ]

    def test_no_repeat_pairing(self):
        matches_round1 = pair_players(self.players, 1)
        apply_results(matches_round1, self.players)
        matches_round2 = pair_players(self.players, 2)
        ids_round1 = {(m.black_id, m.white_id) for m in matches_round1 if m.white_id != "BYE"}
        ids_round2 = {(m.black_id, m.white_id) for m in matches_round2 if m.white_id != "BYE"}
        self.assertTrue(ids_round1.isdisjoint(ids_round2))

    def test_bye_assigned_to_low_score(self):
        short_list = self.players[:5]
        short_list[0].score = 4
        short_list[1].score = 2
        short_list[2].score = 1
        short_list[3].score = 0
        short_list[4].score = 0
        matches = pair_players(short_list, 1)
        bye_match = next(m for m in matches if m.white_id == "BYE" or m.black_id == "BYE")
        self.assertEqual(bye_match.black_id, short_list[3].id)


class RankingTestCase(unittest.TestCase):
    def test_rank_by_score_then_opponent(self):
        p1 = Player(id="a", name="A", score=4)
        p2 = Player(id="b", name="B", score=4)
        p3 = Player(id="c", name="C", score=2)
        # 为对手分提供引用
        p1.opponent_refs = [p3]
        p2.opponent_refs = [p3]
        ranked = rank_players([p1, p2, p3], {"priority": ["score", "opponent_score"]})
        self.assertEqual(ranked[0].score, 4)
        self.assertEqual(len(ranked), 3)


if __name__ == "__main__":
    unittest.main()
