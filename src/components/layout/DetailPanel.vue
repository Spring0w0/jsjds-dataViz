<template>
  <div class="detail-panel">
    <div class="panel-header">
      <h3>详情信息</h3>
    </div>
    
    <div class="panel-content">
      <!-- 指标详情卡片 -->
      <div class="info-card">
        <h4 class="card-title">指标说明</h4>
        <div class="card-content" v-if="currentMetric">
          <div class="info-item">
            <span class="label">名称</span>
            <span class="value">{{ currentMetric.name }}</span>
          </div>
          <div class="info-item">
            <span class="label">单位</span>
            <span class="value">{{ currentMetric.unit || '-' }}</span>
          </div>
          <div class="info-item">
            <span class="label">说明</span>
            <span class="value">{{ currentMetric.description }}</span>
          </div>
          <!-- 数值型指标的统计信息 -->
          <template v-if="currentStats && typeof currentStats.max === 'number'">
            <div class="info-item">
              <span class="label">最大值</span>
              <span class="value">{{ currentStats.max }}{{ currentMetric.unit }}</span>
            </div>
            <div class="info-item">
              <span class="label">最小值</span>
              <span class="value">{{ currentStats.min }}{{ currentMetric.unit }}</span>
            </div>
            <div class="info-item">
              <span class="label">平均值</span>
              <span class="value">{{ typeof currentStats.avg === 'number' ? currentStats.avg.toFixed(2) : '' }}{{ currentMetric.unit }}</span>
            </div>
          </template>
          <!-- 分类指标的统计信息 -->
          <template v-else-if="currentStats && Array.isArray(currentStats.unique_values)">
            <div class="info-item">
              <span class="label">分类数量</span>
              <span class="value">{{ currentStats.unique_values.length }}</span>
            </div>
            <div class="info-item">
              <span class="label">分类示例</span>
              <span class="value">{{ currentStats.unique_values.join('、') }}</span>
            </div>
          </template>
        </div>
        <div v-else class="empty-text">请选择指标</div>
      </div>
      
      <!-- 选中区域卡片 -->
      <div class="info-card" v-if="selectedRegion && currentRegionData">
        <h4 class="card-title">{{ selectedRegion }}</h4>
        <div class="card-content">
          <div class="info-item" v-if="currentRegionValue != null">
            <span class="label">{{ currentMetric?.name || '当前值' }}</span>
            <span class="value">{{ currentRegionValue }}{{ currentMetric?.unit }}</span>
          </div>
          <div class="info-item" v-if="currentRegionData.rank">
            <span class="label">排名</span>
            <span class="value">第 {{ currentRegionData.rank }} 位</span>
          </div>
          <div class="info-item" v-if="currentRegionData.resource_type">
            <span class="label">资源类型</span>
            <span class="value">{{ currentRegionData.resource_type }}</span>
          </div>
          <div class="info-item" v-if="currentRegionData.quadrant">
            <span class="label">所属象限</span>
            <span class="value">{{ currentRegionData.quadrant }}</span>
          </div>
        </div>
      </div>
      
      <!-- 趋势图 -->
      <div class="chart-card">
        <TrendChart height="250px" />
      </div>
      
      <!-- Top 10 -->
      <div class="chart-card">
        <RankChart height="250px" :showTop="true" />
      </div>
      
      <!-- Bottom 10 -->
      <div class="chart-card">
        <RankChart height="250px" :showTop="false" />
      </div>
      
      <!-- 四象限分布图 -->
      <div class="chart-card" v-if="appStore.mode === 'china'">
        <QuadrantChart height="250px" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'
import { useMapStore } from '../../stores/map'
import TrendChart from '../charts/TrendChart.vue'
import RankChart from '../charts/RankChart.vue'
import QuadrantChart from '../charts/QuadrantChart.vue'

const appStore = useAppStore()
const dataStore = useDataStore()
const mapStore = useMapStore()

const currentMetric = computed(() => dataStore.currentMetric)
const selectedRegion = computed(() => mapStore.selectedRegion)

const currentStats = computed(() => {
  const mode = appStore.mode
  const year = appStore.currentYear
  const metricId = dataStore.currentMetricId
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData

  if (!dataSet) return null
  
  const categoricalMetrics = ['resource_type', 'quadrant', 'new_quadrant']
  if (categoricalMetrics.includes(metricId)) {
    return dataSet.statistics?.[metricId]
  }
  
  return dataSet.statistics?.[year]?.[metricId] || dataSet.statistics?.[metricId]
})

const currentRegionData = computed(() => {
  const mode = appStore.mode
  const year = appStore.currentYear
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  
  if (!dataSet || !selectedRegion.value || !dataSet.values[year]) return null
  return dataSet.values[year][selectedRegion.value]
})

const currentRegionValue = computed(() => {
  if (!currentRegionData.value || !dataStore.currentMetricId) return null
  return currentRegionData.value[dataStore.currentMetricId]
})
</script>

<style scoped>
.detail-panel {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: white;
  border-left: 1px solid #e0e0e0;
  min-height: 0;
}

.panel-header {
  padding: 16px;
  border-bottom: 1px solid #e0e0e0;
  flex-shrink: 0;
}

.panel-header h3 {
  margin: 0;
  font-size: 16px;
  color: #333;
}

.panel-content {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* 自定义滚动条样式 */
.panel-content::-webkit-scrollbar {
  width: 8px;
}

.panel-content::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.panel-content::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
  transition: background 0.3s;
}

.panel-content::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.info-card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 16px;
  flex-shrink: 0;
}

.card-title {
  margin: 0 0 12px 0;
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.info-item {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
}

.info-item .label {
  color: #666;
}

.info-item .value {
  color: #333;
  font-weight: 500;
}

.empty-text {
  color: #999;
  font-size: 14px;
  text-align: center;
  padding: 20px 0;
}

.chart-card {
  background: #f8f9fa;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}
</style>