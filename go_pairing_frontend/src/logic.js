// 前端本地演示版配对，仅用于展示 UI，不等同后端算法。
export function pairPlayersLocal(players) {
  const list = [...players].sort((a, b) => b.number - a.number)
  const matches = []
  for (let i = 0; i < list.length; i += 2) {
    const a = list[i]
    const b = list[i + 1]
    if (!b) {
      matches.push({ board_no: 0, black_id: a.name, white_id: 'BYE' })
      continue
    }
    matches.push({ board_no: matches.length + 1, black_id: a.name, white_id: b.name })
  }
  return matches
}
