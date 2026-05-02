<template>
  <div class="main-layout">
    <!-- 顶部标题 -->
    <header class="layout-header">
      <h1 class="app-title">卫生数据可视化平台</h1>
    </header>
    
    <!-- 主内容区 -->
    <div class="layout-content">
      <!-- 左侧指标面板 -->
      <aside class="left-panel">
        <MetricTreePanel />
      </aside>
      
      <!-- 中间地图区 -->
      <main class="center-panel">
        <div class="map-container">
          <MapChart @region-click="handleRegionClick" />
        </div>
      </main>
      
      <!-- 右侧详情面板 -->
      <aside class="right-panel">
        <DetailPanel />
      </aside>
    </div>
    
    <!-- 底部时间轴 -->
    <footer class="layout-footer">
      <TimelineController />
    </footer>
  </div>
</template>

<script setup lang="ts">
import { watch } from 'vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'
import MetricTreePanel from './MetricTreePanel.vue'
import MapChart from '../charts/MapChart.vue'
import DetailPanel from './DetailPanel.vue'
import TimelineController from './TimelineController.vue'

const appStore = useAppStore()
const dataStore = useDataStore()

const handleRegionClick = (region: string) => {
  // 处理区域点击
}

watch(() => appStore.mode, (newMode) => {
  if (newMode === 'china') {
    dataStore.loadChinaData()
  } else {
    dataStore.loadWorldData()
  }
})
</script>

<style scoped>
.main-layout {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #F5F8FA;
  overflow: hidden;
}

.layout-header {
  background: #003366;
  color: white;
  padding: 16px 32px;
  flex-shrink: 0;
}

.app-title {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: white;
}

.layout-content {
  flex: 1;
  display: flex;
  overflow: hidden;
}

.left-panel {
  width: 280px;
  flex-shrink: 0;
  overflow: hidden;
}

.center-panel {
  flex: 1;
  overflow: hidden;
  padding: 16px;
}

.map-container {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.right-panel {
  width: 320px;
  flex-shrink: 0;
  overflow: hidden;
}

.layout-footer {
  flex-shrink: 0;
}
</style>
