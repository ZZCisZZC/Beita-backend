# 围棋对阵编排系统设计与代码示例

## 第 1 步：需求检查
- 假设单赛事内仅裁判账号使用，无登录鉴权；仅做简单本地存储。
- Excel 导入格式按逗号分隔字符串演示；实际可用 xlsx 解析库。
- FastAPI/前端只做示例结构，重点在算法与数据结构。

## 第 2 步：工程架构设计
- 前端（Vue3）：`App.vue` + 组件 `TournamentSetup` / `PlayerImport` / `PairingTable` / `RankingTable`，使用本地存储模拟 API。
- 后端（Python 示例）：`go_pairing_system` 包，包含 `models.py`、`pairing.py`、`ranking.py`、`storage.py`、`api.py`。
- 算法模块：`pairing.py`（瑞士制+柔性下调）、`ranking.py`（可配置指标优先级）。
- CSV 管理：`storage.py` 按赛事 id 划分文件，支持多赛事。

## 第 3 步：数据结构与类型
- Python dataclass（可替换为 Pydantic）：见 `go_pairing_system/models.py`。
- TypeScript 接口（片段）：
```ts
interface Player { id:string; name:string; gender?:string; team?:string; dan?:string; is_seed:boolean; number:number; score:number; opponents:string[]; color_history:("B"|"W")[]; bye_count:number; total_up_adjust:number; total_down_adjust:number; consecutive_adjust:number; }
interface Match { round_no:number; board_no:number; black_id:string; white_id:string; result?:"B"|"W"|"D"|"FF"; }
interface Tournament { id:string; name:string; total_rounds:number; rules_config:Record<string,string[]>; groups:string[]; }
```

## 第 4 步：配对算法
- 核心逻辑：按积分段分组→奇偶轮排序→两两配对→奇数尾部下调→避免重遇→颜色平衡→奇数补 bye。
- 伪代码：
```
function pair_players(players, round_no):
  if len(players) odd: choose lowest score no-bye as bye, 给 2 分
  groups = 按 score 分段降序
  carry = None
  for 每个分段:
    if carry: 插入段首，累计下调
    若分段人数为奇数: 末位下调为 carry
    按奇偶轮排序编号，成对配对，若重遇则与前一对交换
  末段仍有 carry 则与最低分段首位配对
  byeMatch 如有则插入
```
- 运行代码：见 `go_pairing_system/pairing.py`，包含颜色平衡与结果录入。
- 单元测试：`go_pairing_system/tests/test_pairing.py` 覆盖不重遇、轮空分配等。

## 第 5 步：后端接口
- 使用 FastAPI 示例（`api.py`）
  - `POST /tournaments/{tid}/players/import` 导入校验：姓名为空/重复直接 400。
  - `POST /tournaments/{tid}/rounds/{round_no}/pair` 生成对阵并写回 CSV。
  - `POST /tournaments/{tid}/rounds/{round_no}/results` 录入结果，更新积分与颜色。
  - `GET /tournaments/{tid}/ranking` 按配置优先级排序。
- 返回示例：
```json
{"matches":[{"round_no":1,"board_no":1,"black_id":"p1","white_id":"p2"}]}
```

## 第 6 步：Vue 前端代码
- 组件示例均在 `go_pairing_frontend/src`，使用本地存储模拟后端流程。
- `PairingTable` 调用 `logic.js` 的临近编排（奇偶轮编号方向）生成对阵，并支持按钮录入结果。

## 第 7 步：示例运行流程
1. 在“初始化赛事”输入轮次和排名优先级，点击创建，获得赛事 id。
2. 在“选手导入”粘贴 Excel 行文本，点击导入，前端写入本地存储/后端可调用导入 API。
3. 点击“生成本轮对阵”，前端按编号方向生成表；后端可调用 `/pair` 使用瑞士制算法。
4. 录入结果后调用 `/results` 更新积分。
5. 打开“名次展示”，按配置优先级排序显示当前排名。

> 以上为可直接落地的本地演示与后端样例，满足题述需求并可继续扩展为生产方案。
