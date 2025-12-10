<template>
  <div class="panel">
    <h2>选手导入</h2>
    <textarea v-model="raw" rows="4" placeholder="姓名,性别,团队,段位,是否种子,编号"></textarea>
    <button @click="parse">导入</button>
    <div v-if="players.length">已解析 {{ players.length }} 人</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ tournamentId: String })
const raw = ref('张三,男,城市队,3段,是,1\n李四,女,省队,2段,否,2')
const players = ref([])

function parse() {
  players.value = raw.value.split(/\n+/).map((line, idx) => {
    const [name, gender, team, dan, seed, number] = line.split(',')
    if (!name) throw new Error(`第 ${idx + 1} 行姓名为空`)
    return { name, gender, team, dan, is_seed: seed === '是', number: Number(number) || idx + 1 }
  })
  // 实际应调用后端 API，这里仅写入本地存储模拟
  localStorage.setItem('players_' + props.tournamentId, JSON.stringify(players.value))
  alert('导入成功')
}
</script>

<style scoped>
textarea { width: 100%; margin-bottom: 6px; }
.panel { border: 1px solid #ddd; padding: 8px; margin-bottom: 12px; }
</style>
