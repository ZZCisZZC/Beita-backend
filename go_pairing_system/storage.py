"""CSV 存储封装，便于本地多赛事管理。"""
import csv
from pathlib import Path
from typing import List

from .models import Player


class CsvStorage:
    def __init__(self, base_dir: str = "./data"):
        self.base = Path(base_dir)
        self.base.mkdir(parents=True, exist_ok=True)

    def players_path(self, tournament_id: str) -> Path:
        return self.base / f"{tournament_id}_players.csv"

    def save_players(self, tournament_id: str, players: List[Player]):
        path = self.players_path(tournament_id)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "id",
                "name",
                "gender",
                "team",
                "dan",
                "is_seed",
                "number",
                "score",
                "bye_count",
                "total_up_adjust",
                "total_down_adjust",
                "consecutive_adjust",
                "opponents",
                "color_history",
            ])
            for p in players:
                writer.writerow([
                    p.id,
                    p.name,
                    p.gender or "",
                    p.team or "",
                    p.dan or "",
                    "1" if p.is_seed else "0",
                    p.number,
                    p.score,
                    p.bye_count,
                    p.total_up_adjust,
                    p.total_down_adjust,
                    p.consecutive_adjust,
                    "|".join(p.opponents),
                    "".join(p.color_history),
                ])

    def load_players(self, tournament_id: str) -> List[Player]:
        path = self.players_path(tournament_id)
        if not path.exists():
            return []
        players: List[Player] = []
        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                player = Player(
                    id=row["id"],
                    name=row["name"],
                    gender=row.get("gender") or None,
                    team=row.get("team") or None,
                    dan=row.get("dan") or None,
                    is_seed=row.get("is_seed") == "1",
                    number=int(row.get("number", 0)),
                    score=float(row.get("score", 0)),
                    bye_count=int(row.get("bye_count", 0)),
                    total_up_adjust=int(row.get("total_up_adjust", 0)),
                    total_down_adjust=int(row.get("total_down_adjust", 0)),
                    consecutive_adjust=int(row.get("consecutive_adjust", 0)),
                    opponents=[x for x in row.get("opponents", "").split("|") if x],
                    color_history=list(row.get("color_history", "")),
                )
                players.append(player)
        return players
