<script setup lang="ts">
import MainLayout from './components/layout/MainLayout.vue'
import { useDataStore } from './stores/data'

const dataStore = useDataStore()

// 初始化默认指标
dataStore.setMetric('china', 'health_personnel')
</script>

<template>
  <MainLayout />
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

#app {
  width: 100%;
  height: 100vh;
}
</style>
