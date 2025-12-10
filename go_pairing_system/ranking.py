"""排名引擎：支持配置化优先级。"""
from typing import List, Dict, Callable
from .models import Player


class RankingEngine:
    def __init__(self, priority: List[str]):
        self.priority = priority
        self.handlers: Dict[str, Callable[[Player], float]] = {
            "score": lambda p: p.score,
            "opponent_score": self._opponent_score,
            "progressive": self._progressive_score,
            "win_over": self._win_over_score,
        }

    def _opponent_score(self, player: Player) -> float:
        # 对手分：已记录对手积分之和，忽略轮空
        return sum(o.score for o in getattr(player, "opponent_refs", []) if o.id != "BYE")

    def _progressive_score(self, player: Player) -> float:
        # 累进分：假设score_history存储每轮积分
        history = getattr(player, "score_history", [])
        return sum((idx + 1) * s for idx, s in enumerate(history))

    def _win_over_score(self, player: Player) -> float:
        # 胜手和：战胜对手积分和
        wins = getattr(player, "wins", [])
        return sum(w.score for w in wins)

    def sort(self, players: List[Player]) -> List[Player]:
        def sort_key(p: Player):
            key = []
            for metric in self.priority:
                func = self.handlers.get(metric, lambda _: 0)
                key.append(func(p))
            return tuple(key)

        return sorted(players, key=sort_key, reverse=True)


def rank_players(players: List[Player], config: Dict[str, List[str]]) -> List[Player]:
    engine = RankingEngine(config.get("priority", ["score", "opponent_score", "progressive", "win_over"]))
    return engine.sort(players)
