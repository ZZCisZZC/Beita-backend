<template>
  <div class="panel">
    <h2>名次展示</h2>
    <button @click="load">刷新</button>
    <ol>
      <li v-for="p in ranking" :key="p.name">{{ p.name }} - {{ p.score }} 分</li>
    </ol>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ tournamentId: String })
const ranking = ref([])

function load() {
  const players = JSON.parse(localStorage.getItem('players_' + props.tournamentId) || '[]')
  ranking.value = players.sort((a,b)=> b.score - a.score)
}
</script>

<style scoped>
.panel { border: 1px solid #ddd; padding: 8px; margin-bottom: 12px; }
</style>
