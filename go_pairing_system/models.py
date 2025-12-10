"""围棋赛事数据模型定义。"""
from dataclasses import dataclass, field
from typing import List, Literal, Dict, Optional

Color = Literal["B", "W"]
Result = Literal["B", "W", "D", "FF"]  # 黑胜、白胜、和棋、双负


def default_list_factory():
    return []


@dataclass
class Player:
    """棋手实体，包含瑞士制编排所需的全部状态。"""

    id: str
    name: str
    gender: Optional[str] = None
    team: Optional[str] = None
    dan: Optional[str] = None  # 段位
    is_seed: bool = False
    number: int = 0  # 抽签编号
    score: float = 0.0  # 当前积分
    opponents: List[str] = field(default_factory=default_list_factory)
    color_history: List[Color] = field(default_factory=default_list_factory)
    bye_count: int = 0
    total_up_adjust: int = 0
    total_down_adjust: int = 0
    consecutive_adjust: int = 0

    def color_balance(self) -> int:
        """返回黑白差值（黑-白）。"""
        return self.color_history.count("B") - self.color_history.count("W")


@dataclass
class Match:
    round_no: int
    board_no: int
    black_id: str
    white_id: str
    result: Optional[Result] = None


@dataclass
class Tournament:
    id: str
    name: str
    total_rounds: int
    rules_config: Dict[str, List[str]]
    groups: List[str]
