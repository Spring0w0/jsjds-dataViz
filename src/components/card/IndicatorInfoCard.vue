<template>
  <div class="indicator-card card">
    <div class="card-header">
      <span class="card-label">当前指标</span>
      <span class="card-badge" :class="levelClass">{{ levelText }}</span>
    </div>
    <div class="card-content">
      <h3 class="indicator-name">{{ indicatorName }}</h3>
      <div class="indicator-value">
        <span class="value-number">{{ value }}</span>
        <span class="value-unit">{{ unit }}</span>
      </div>
      <p class="indicator-desc">{{ description }}</p>
      <div class="stats-grid" v-if="stats">
        <div class="stat-item">
          <span class="stat-label">最大值</span>
          <span class="stat-value">{{ stats.max }}</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">最小值</span>
          <span class="stat-value">{{ stats.min }}</span>
        </div>
        <div class="stat-item">
          <span class="stat-label">平均值</span>
          <span class="stat-value">{{ stats.avg }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  indicatorName: string
  unit: string
  value: string | number
  description: string
  level?: 'raw' | 'derived'
  stats?: {
    max: string | number
    min: string | number
    avg: string | number
  }
}

const props = withDefaults(defineProps<Props>(), {
  level: 'raw'
})

const levelText = computed(() => {
  return props.level === 'raw' ? '原始数据层' : '分析衍生层'
})

const levelClass = computed(() => {
  return props.level === 'raw' ? 'badge-raw' : 'badge-derived'
})
</script>

<style scoped>
.indicator-card {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-label {
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.card-badge {
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-size: 12px;
  font-weight: var(--font-medium);
}

.badge-raw {
  background: var(--color-bg-tertiary);
  color: var(--color-text-secondary);
}

.badge-derived {
  background: var(--color-primary-bg);
  color: var(--color-primary);
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.indicator-name {
  font-size: 16px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
  margin: 0;
}

.indicator-value {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.value-number {
  font-size: 32px;
  font-weight: var(--font-bold);
  color: var(--color-text-primary);
  line-height: 1.2;
}

.value-unit {
  font-size: 14px;
  font-weight: var(--font-normal);
  color: var(--color-text-tertiary);
}

.indicator-desc {
  font-size: 13px;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin: 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-top: 8px;
  padding-top: 16px;
  border-top: 1px solid var(--color-border-light);
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-label {
  font-size: 12px;
  color: var(--color-text-tertiary);
}

.stat-value {
  font-size: 15px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}
</style>
