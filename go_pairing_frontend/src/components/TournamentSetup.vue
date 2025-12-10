<template>
  <div class="panel">
    <h2>初始化赛事</h2>
    <label>赛事名称：<input v-model="name" /></label>
    <label>总轮数：<input type="number" v-model.number="rounds" /></label>
    <label>排名规则优先级（逗号分隔）：<input v-model="priority" /></label>
    <button @click="create">创建赛事</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('示例赛事')
const rounds = ref(5)
const priority = ref('score,opponent_score,progressive')
const emit = defineEmits(['created'])

function create() {
  const id = Date.now().toString()
  localStorage.setItem('tournament_priority_' + id, priority.value)
  emit('created', id)
}
</script>

<style scoped>
.panel { border: 1px solid #ddd; padding: 8px; margin-bottom: 12px; }
</style>
