<template>
  <div class="app">
    <h1>围棋对阵编排系统 Demo</h1>
    <TournamentSetup @created="onCreated" />
    <PlayerImport v-if="tournamentId" :tournament-id="tournamentId" />
    <PairingTable v-if="tournamentId" :tournament-id="tournamentId" />
    <RankingTable v-if="tournamentId" :tournament-id="tournamentId" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TournamentSetup from './components/TournamentSetup.vue'
import PlayerImport from './components/PlayerImport.vue'
import PairingTable from './components/PairingTable.vue'
import RankingTable from './components/RankingTable.vue'

const tournamentId = ref('')

function onCreated(id) {
  tournamentId.value = id
}
</script>

<style scoped>
.app {
  padding: 16px;
}
</style>
