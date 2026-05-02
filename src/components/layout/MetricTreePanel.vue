<template>
  <div class="metric-panel">
    <div class="panel-header">
      <h3>指标选择</h3>
    </div>
    
    <div class="layer-switch">
      <el-radio-group v-model="currentLayer" size="small" @change="handleLayerChange">
        <el-radio-button value="原始数据层">原始数据层</el-radio-button>
        <el-radio-button value="分析衍生层">分析衍生层</el-radio-button>
      </el-radio-group>
    </div>
    
    <div class="metric-tree">
      <el-collapse v-model="activeCategories">
        <el-collapse-item v-for="(metrics, category) in currentLayerMetrics" :key="category" :name="category">
          <template #title>
            <span class="category-title">{{ category }}</span>
          </template>
          <div class="metric-list">
            <div
              v-for="metric in metrics"
              :key="metric.id"
              class="metric-item"
              :class="{ active: currentMetricId === metric.id }"
              @click="handleSelectMetric(metric)"
            >
              <span class="metric-name">{{ metric.name }}</span>
              <span class="metric-unit">{{ metric.unit }}</span>
            </div>
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'
import { METRICS_CONFIG, type Metric } from '../../config/metrics-config'

const appStore = useAppStore()
const dataStore = useDataStore()

const currentLayer = ref(dataStore.currentLayer)
const activeCategories = ref<string[]>([])

const currentLayerMetrics = computed(() => {
  const mode = appStore.mode
  return METRICS_CONFIG[mode][currentLayer.value] || {}
})

const currentMetricId = computed(() => dataStore.currentMetricId)

const handleLayerChange = (layer: string) => {
  dataStore.setLayer(layer)
  const metrics = currentLayerMetrics.value
  const firstCategory = Object.keys(metrics)[0]
  if (firstCategory && metrics[firstCategory]?.[0]) {
    handleSelectMetric(metrics[firstCategory][0])
  }
}

const handleSelectMetric = (metric: Metric) => {
  dataStore.setMetric(appStore.mode, metric.id)
}

watch(() => appStore.mode, () => {
  const mode = appStore.mode
  const metrics = METRICS_CONFIG[mode][currentLayer.value]
  const firstCategory = Object.keys(metrics)[0]
  if (firstCategory && metrics[firstCategory]?.[0]) {
    handleSelectMetric(metrics[firstCategory][0])
  }
})
</script>

<style scoped>
.metric-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: white;
  border-right: 1px solid #e0e0e0;
}

.panel-header {
  padding: 16px;
  border-bottom: 1px solid #e0e0e0;
}

.panel-header h3 {
  margin: 0;
  font-size: 16px;
  color: #333;
}

.layer-switch {
  padding: 12px 16px;
  border-bottom: 1px solid #e0e0e0;
}

.metric-tree {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
}

.category-title {
  font-weight: 500;
  color: #333;
}

.metric-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.metric-item {
  padding: 8px 12px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s;
}

.metric-item:hover {
  background: #f0f0f0;
}

.metric-item.active {
  background: #00336620;
  color: #003366;
  font-weight: 500;
}

.metric-name {
  font-size: 14px;
}

.metric-unit {
  font-size: 12px;
  color: #999;
}
</style>
