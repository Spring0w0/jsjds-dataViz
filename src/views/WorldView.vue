<template>
  <div class="world-view">
    <div class="main-layout">
      <div class="panel-section">
        <IndicatorLevelPanel
          :current-level="currentLevel"
          :current-category="currentCategory"
          :current-indicator="currentIndicator"
          :categories="categories"
          :indicators="indicators"
          @update:current-level="currentLevel = $event"
          @update:current-category="currentCategory = $event"
          @update:current-indicator="currentIndicator = $event"
        />
      </div>
      
      <div class="content-section">
        <div class="map-container">
          <WorldMap />
        </div>
        
        <div class="bottom-section">
          <div class="cards-row">
            <div class="card-wrapper">
              <IndicatorInfoCard
                indicator-name="平均预期寿命"
                unit="岁"
                value="72.3"
                description="衡量国家整体健康水平的综合指标"
                level="raw"
                :stats="{ max: 84.8, min: 52.1, avg: 71.5 }"
              />
            </div>
            <div class="card-wrapper">
              <ProvinceDetailCard
                province-name="日本"
                value="84.8"
                unit="岁"
                :rank="1"
                trend="up"
                trend-value="1.2%"
              />
            </div>
            <div class="card-wrapper">
              <ResourceConfigCard
                quadrant="exemplary"
                resource-type="efficient"
                description="健康投入与产出表现优异，处于全球领先水平"
              />
            </div>
          </div>
          
          <div class="charts-row">
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">全球趋势变化</span>
              </div>
              <div class="chart-placeholder">
                趋势图表区域
              </div>
            </div>
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">各大洲对比</span>
              </div>
              <div class="chart-placeholder">
                对比图表区域
              </div>
            </div>
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">TOP 20 国家</span>
              </div>
              <div class="chart-placeholder">
                排名图表区域
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import IndicatorLevelPanel from '../components/panel/IndicatorLevelPanel.vue'
import IndicatorInfoCard from '../components/card/IndicatorInfoCard.vue'
import ProvinceDetailCard from '../components/card/ProvinceDetailCard.vue'
import ResourceConfigCard from '../components/card/ResourceConfigCard.vue'
import WorldMap from '../components/map/WorldMap.vue'

const currentLevel = ref<'raw' | 'derived'>('raw')
const currentCategory = ref('健康营养')
const currentIndicator = ref('lifespan')

const categories = ['健康营养', '健康风险', '核心疾病', '社会经济']
const indicators = [
  { id: 'lifespan', name: '平均预期寿命', unit: '岁', desc: '衡量国家整体健康水平' },
  { id: 'mortality', name: '婴儿死亡率', unit: '‰', desc: '反映国家医疗保健水平' },
  { id: 'nutrition', name: '营养不良率', unit: '%', desc: '衡量人口营养状况' },
  { id: 'gdp', name: '人均GDP', unit: '美元', desc: '反映国家经济发展水平' }
]
</script>

<style scoped>
.world-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.main-layout {
  flex: 1;
  display: flex;
  overflow: hidden;
}

.panel-section {
  width: 320px;
  flex-shrink: 0;
  overflow: hidden;
}

.content-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.map-container {
  flex: 1;
  min-height: 0;
  background: var(--color-bg);
}

.bottom-section {
  height: 360px;
  flex-shrink: 0;
  border-top: 1px solid var(--color-border);
  background: var(--color-bg);
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cards-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.card-wrapper {
  min-width: 0;
}

.charts-row {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  min-height: 0;
}

.chart-card {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  overflow: hidden;
}

.chart-header {
  flex-shrink: 0;
}

.chart-title {
  font-size: 13px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.chart-placeholder {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg-secondary);
  border-radius: var(--radius);
  font-size: 12px;
  color: var(--color-text-tertiary);
}
</style>
