"""FastAPI 接口示例，提供赛事管理与编排。"""
from typing import List, Dict

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:  # 无法联网安装时，给出占位提示
    FastAPI = None
    HTTPException = Exception
    CORSMiddleware = None

from .models import Player
from .pairing import pair_players, apply_results
from .ranking import rank_players
from .storage import CsvStorage

app = FastAPI(title="Go Pairing System") if FastAPI else None
storage = CsvStorage()

if app:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.post("/tournaments/{tid}/players/import")
def import_players(tid: str, payload: List[Dict]):
    if not app:
        raise HTTPException(status_code=503, detail="FastAPI 未安装")
    players: List[Player] = []
    names = set()
    for idx, item in enumerate(payload):
        name = item.get("name", "").strip()
        if not name:
            raise HTTPException(status_code=400, detail=f"第 {idx+1} 行姓名为空")
        if name in names:
            raise HTTPException(status_code=400, detail=f"姓名重复: {name}")
        names.add(name)
        players.append(
            Player(
                id=item.get("id") or f"p{idx+1}",
                name=name,
                gender=item.get("gender"),
                team=item.get("team"),
                dan=item.get("dan"),
                is_seed=item.get("is_seed", False),
                number=int(item.get("number") or idx + 1),
            )
        )
    storage.save_players(tid, players)
    return {"count": len(players)}


@app.post("/tournaments/{tid}/rounds/{round_no}/pair")
def api_pair(tid: str, round_no: int):
    if not app:
        raise HTTPException(status_code=503, detail="FastAPI 未安装")
    players = storage.load_players(tid)
    matches = pair_players(players, round_no)
    storage.save_players(tid, players)
    return {"matches": [m.__dict__ for m in matches]}


@app.post("/tournaments/{tid}/rounds/{round_no}/results")
def api_results(tid: str, round_no: int, payload: List[Dict]):
    if not app:
        raise HTTPException(status_code=503, detail="FastAPI 未安装")
    players = storage.load_players(tid)
    match_objs = []
    for item in payload:
        match_objs.append(
            type("Tmp", (), item)  # 简化，实际可用 Pydantic
        )
    apply_results(match_objs, players)
    storage.save_players(tid, players)
    return {"ok": True}


@app.get("/tournaments/{tid}/ranking")
def api_ranking(tid: str, priority: str = "score,opponent_score"):
    if not app:
        raise HTTPException(status_code=503, detail="FastAPI 未安装")
    players = storage.load_players(tid)
    ranked = rank_players(players, {"priority": priority.split(",")})
    return {"ranking": [{"id": p.id, "name": p.name, "score": p.score} for p in ranked]}
