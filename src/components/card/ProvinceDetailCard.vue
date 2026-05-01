<template>
  <div class="province-card card">
    <div class="card-header">
      <div class="header-left">
        <span class="province-tag">{{ provinceName }}</span>
        <span class="province-rank" v-if="rank">#{{ rank }}</span>
      </div>
    </div>
    <div class="card-content">
      <div class="value-section">
        <div class="label">当前数值</div>
        <div class="value-display">
          <span class="value-number">{{ value }}</span>
          <span class="value-unit">{{ unit }}</span>
        </div>
      </div>
      <div class="info-section">
        <div class="info-item">
          <span class="info-label">较去年</span>
          <span class="info-value" :class="trendClass">{{ trendText }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  provinceName: string
  value: string | number
  unit: string
  rank?: number
  trend?: 'up' | 'down' | 'same'
  trendValue?: string
}

const props = withDefaults(defineProps<Props>(), {
  trend: 'same',
  trendValue: '0%'
})

const trendClass = computed(() => {
  return props.trend === 'up' ? 'trend-up' : props.trend === 'down' ? 'trend-down' : 'trend-same'
})

const trendText = computed(() => {
  const prefix = props.trend === 'up' ? '+' : props.trend === 'down' ? '-' : ''
  return `${prefix}${props.trendValue}`
})
</script>

<style scoped>
.province-card {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card-header {
  display: flex;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.province-tag {
  font-size: 16px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.province-rank {
  padding: 2px 8px;
  background: var(--color-primary-bg);
  color: var(--color-primary);
  border-radius: var(--radius-full);
  font-size: 12px;
  font-weight: var(--font-semibold);
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.value-section {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.label {
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.value-display {
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
  color: var(--color-text-tertiary);
}

.info-section {
  padding-top: 16px;
  border-top: 1px solid var(--color-border-light);
}

.info-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.info-label {
  font-size: 13px;
  color: var(--color-text-secondary);
}

.info-value {
  font-size: 14px;
  font-weight: var(--font-semibold);
}

.trend-up {
  color: var(--color-quadrant-deficient);
}

.trend-down {
  color: var(--color-quadrant-collaborative);
}

.trend-same {
  color: var(--color-text-secondary);
}
</style>
