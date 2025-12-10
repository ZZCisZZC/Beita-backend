"""瑞士制+特殊规则编排引擎实现。"""
from dataclasses import replace
from typing import List, Tuple

from .models import Player, Match

BYE_PLAYER_ID = "BYE"


def pick_bye_candidate(players: List[Player]) -> Player:
    """在人数为奇数时选择轮空选手：优先低分且未轮空。"""
    eligible = [p for p in players if p.bye_count == 0]
    if not eligible:
        eligible = players
    # 低分优先，编号次序稳定
    candidate = sorted(eligible, key=lambda p: (p.score, p.number))[0]
    return candidate


def order_in_group(group: List[Player], round_no: int) -> List[Player]:
    """奇数轮按编号升序，偶数轮按编号降序。"""
    reverse = round_no % 2 == 0
    return sorted(group, key=lambda p: p.number, reverse=reverse)


def avoid_repeat(pair: Tuple[Player, Player], used_pairs: set) -> Tuple[Player, Player]:
    """若出现重遇则交换顺序，简单处理。"""
    a, b = pair
    if (a.id, b.id) in used_pairs or (b.id, a.id) in used_pairs:
        return b, a
    return pair


def pair_group(group: List[Player], round_no: int, used_pairs: set, board_offset: int) -> List[Match]:
    ordered = order_in_group(group, round_no)
    matches: List[Match] = []
    for idx in range(0, len(ordered), 2):
        if idx + 1 >= len(ordered):
            break
        p1, p2 = avoid_repeat((ordered[idx], ordered[idx + 1]), used_pairs)
        # 简单颜色平衡：黑白差大者执相反颜色
        if p1.color_balance() > p2.color_balance():
            black, white = p2, p1
        else:
            black, white = p1, p2
        matches.append(Match(round_no=round_no, board_no=board_offset + len(matches) + 1, black_id=black.id, white_id=white.id))
        used_pairs.add((black.id, white.id))
    return matches


def pair_players(players: List[Player], round_no: int) -> List[Match]:
    """按积分分组后配对，支持下调规则。"""
    # 奇数补bye
    work_list = players.copy()
    bye_player = None
    if len(work_list) % 2 == 1:
        bye_player = pick_bye_candidate(work_list)
        bye_player.bye_count += 1
        bye_player.score += 2
        bye_player.opponents.append(BYE_PLAYER_ID)
        bye_match = Match(round_no=round_no, board_no=0, black_id=bye_player.id, white_id=BYE_PLAYER_ID, result="B")
    # 按积分段排序
    groups = {}
    for p in work_list:
        groups.setdefault(p.score, []).append(p)
    sorted_scores = sorted(groups.keys(), reverse=True)
    matches: List[Match] = []
    used_pairs: set = set()
    carry = None
    board_offset = 1
    for score in sorted_scores:
        g = groups[score]
        if carry:
            # 下调过来的人与本段首位配对
            carry.total_down_adjust += 1
            carry.consecutive_adjust += 1
            g = [carry] + g
            carry = None
        if len(g) % 2 == 1:
            carry = g.pop()  # 最后一名下调
            carry.total_down_adjust += 1
            carry.consecutive_adjust += 1
        matches.extend(pair_group(g, round_no, used_pairs, board_offset))
        board_offset = len(matches) + 1
    if carry:
        # 最低分段仍然有单人，只能与最低分段首位配对
        g = [carry]
        matches.extend(pair_group(g, round_no, used_pairs, board_offset))
    if bye_player:
        matches.insert(0, bye_match)
    return matches


def apply_results(matches: List[Match], players: List[Player]) -> None:
    """录入比赛结果并更新积分。"""
    player_map = {p.id: p for p in players}
    for m in matches:
        if m.white_id == BYE_PLAYER_ID:
            continue
        black = player_map[m.black_id]
        white = player_map[m.white_id]
        black.opponents.append(white.id)
        white.opponents.append(black.id)
        if m.result == "B":
            black.score += 2
            black.color_history.append("B")
            white.color_history.append("W")
        elif m.result == "W":
            white.score += 2
            black.color_history.append("B")
            white.color_history.append("W")
        elif m.result == "D":
            black.score += 1
            white.score += 1
            black.color_history.append("B")
            white.color_history.append("W")
        else:  # 双负
            black.color_history.append("B")
            white.color_history.append("W")
