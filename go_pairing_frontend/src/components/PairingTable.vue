<template>
  <div class="panel">
    <h2>对阵编排（本地模拟）</h2>
    <button @click="pair">生成本轮对阵</button>
    <table v-if="matches.length" border="1" cellspacing="0" cellpadding="4">
      <thead>
        <tr><th>台号</th><th>黑</th><th>白</th><th>录入结果</th></tr>
      </thead>
      <tbody>
        <tr v-for="m in matches" :key="m.board_no">
          <td>{{ m.board_no }}</td>
          <td>{{ m.black_id }}</td>
          <td>{{ m.white_id }}</td>
          <td>
            <button @click="setResult(m,'B')">黑胜</button>
            <button @click="setResult(m,'W')">白胜</button>
            <button @click="setResult(m,'D')">和棋</button>
            <button @click="setResult(m,'FF')">双负</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { pairPlayersLocal } from '../logic'

const props = defineProps({ tournamentId: String })
const matches = ref([])

function pair() {
  const players = JSON.parse(localStorage.getItem('players_' + props.tournamentId) || '[]')
  matches.value = pairPlayersLocal(players)
}

function setResult(m, r) {
  m.result = r
}
</script>

<style scoped>
.panel { border: 1px solid #ddd; padding: 8px; margin-bottom: 12px; }
</style>
