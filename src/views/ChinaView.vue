<template>
  <div class="china-view">
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
          <ChinaMap />
        </div>
        
        <div class="bottom-section">
          <div class="cards-row">
            <div class="card-wrapper">
              <IndicatorInfoCard
                indicator-name="每千人口卫生技术人员数"
                unit="人/千人"
                value="6.8"
                description="衡量地区卫生人力资源配置水平的核心指标"
                level="raw"
                :stats="{ max: 12.5, min: 3.2, avg: 7.1 }"
              />
            </div>
            <div class="card-wrapper">
              <ProvinceDetailCard
                province-name="北京市"
                value="11.2"
                unit="人/千人"
                :rank="1"
                trend="up"
                trend-value="5.2%"
              />
            </div>
            <div class="card-wrapper">
              <ResourceConfigCard
                quadrant="exemplary"
                resource-type="efficient"
                description="卫生资源配置效率处于全国领先水平，资源投入与健康产出匹配度高"
              />
            </div>
          </div>
          
          <div class="charts-row">
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">全国趋势变化</span>
              </div>
              <div class="chart-placeholder">
                趋势图表区域
              </div>
            </div>
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">省份分布</span>
              </div>
              <div class="chart-placeholder">
                分布图表区域
              </div>
            </div>
            <div class="chart-card card">
              <div class="chart-header">
                <span class="chart-title">TOP 10 排名</span>
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
import ChinaMap from '../components/map/ChinaMap.vue'

const currentLevel = ref<'raw' | 'derived'>('raw')
const currentCategory = ref('卫生资源')
const currentIndicator = ref('personnel')

const categories = ['卫生资源', '健康产出', '人口经济', '疾病数据']
const indicators = [
  { id: 'personnel', name: '每千人口卫生技术人员数', unit: '人/千人', desc: '衡量地区卫生人力资源配置水平' },
  { id: 'institution', name: '每万人口医疗卫生机构数', unit: '个/万人', desc: '反映医疗服务机构覆盖程度' },
  { id: 'expense', name: '卫生支出占GDP比重', unit: '%', desc: '衡量政府对卫生事业的投入力度' },
  { id: 'lifespan', name: '平均预期寿命', unit: '岁', desc: '综合反映地区健康水平' }
]
</script>

<style scoped>
.china-view {
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
