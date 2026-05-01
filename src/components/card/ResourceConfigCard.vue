<template>
  <div class="resource-card card">
    <div class="card-header">
      <span class="card-label">资源配置分析</span>
    </div>
    <div class="card-content">
      <div class="quadrant-badge" :class="quadrantClass">
        <span class="quadrant-dot"></span>
        <span class="quadrant-text">{{ quadrantText }}</span>
      </div>
      <div class="resource-type" :class="resourceTypeClass">
        <span class="type-icon">{{ resourceTypeIcon }}</span>
        <span class="type-text">{{ resourceTypeText }}</span>
      </div>
      <div class="desc-section">
        <p class="desc-text">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  quadrant: 'collaborative' | 'inefficient' | 'exemplary' | 'deficient'
  resourceType: 'surplus' | 'efficient' | 'deficit' | 'balanced'
  description?: string
}

const props = withDefaults(defineProps<Props>(), {
  description: ''
})

const quadrantText = computed(() => {
  const map: Record<string, string> = {
    collaborative: '协同型',
    inefficient: '低效型',
    exemplary: '模范型',
    deficient: '匮乏型'
  }
  return map[props.quadrant] || ''
})

const quadrantClass = computed(() => {
  return `quadrant-${props.quadrant}`
})

const resourceTypeText = computed(() => {
  const map: Record<string, string> = {
    surplus: '资源冗余',
    efficient: '高效配置',
    deficit: '资源缺口',
    balanced: '配置均衡'
  }
  return map[props.resourceType] || ''
})

const resourceTypeClass = computed(() => {
  return `type-${props.resourceType}`
})

const resourceTypeIcon = computed(() => {
  const map: Record<string, string> = {
    surplus: '⬆️',
    efficient: '✅',
    deficit: '⬇️',
    balanced: '⚖️'
  }
  return map[props.resourceType] || ''
})
</script>

<style scoped>
.resource-card {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card-header {
  display: flex;
  align-items: center;
}

.card-label {
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.quadrant-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: var(--radius-lg);
  width: fit-content;
}

.quadrant-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.quadrant-text {
  font-size: 14px;
  font-weight: var(--font-semibold);
}

.quadrant-collaborative {
  background: var(--color-quadrant-collaborative-bg);
}
.quadrant-collaborative .quadrant-dot {
  background: var(--color-quadrant-collaborative);
}
.quadrant-collaborative .quadrant-text {
  color: var(--color-quadrant-collaborative);
}

.quadrant-inefficient {
  background: var(--color-quadrant-inefficient-bg);
}
.quadrant-inefficient .quadrant-dot {
  background: var(--color-quadrant-inefficient);
}
.quadrant-inefficient .quadrant-text {
  color: var(--color-quadrant-inefficient);
}

.quadrant-exemplary {
  background: var(--color-quadrant-exemplary-bg);
}
.quadrant-exemplary .quadrant-dot {
  background: var(--color-quadrant-exemplary);
}
.quadrant-exemplary .quadrant-text {
  color: var(--color-quadrant-exemplary);
}

.quadrant-deficient {
  background: var(--color-quadrant-deficient-bg);
}
.quadrant-deficient .quadrant-dot {
  background: var(--color-quadrant-deficient);
}
.quadrant-deficient .quadrant-text {
  color: var(--color-quadrant-deficient);
}

.resource-type {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border-radius: var(--radius);
  width: fit-content;
}

.type-icon {
  font-size: 14px;
}

.type-text {
  font-size: 13px;
  font-weight: var(--font-medium);
}

.type-surplus {
  background: var(--color-quadrant-deficient-bg);
  color: var(--color-quadrant-deficient);
}

.type-efficient {
  background: var(--color-quadrant-collaborative-bg);
  color: var(--color-quadrant-collaborative);
}

.type-deficit {
  background: var(--color-quadrant-inefficient-bg);
  color: var(--color-quadrant-inefficient);
}

.type-balanced {
  background: var(--color-quadrant-exemplary-bg);
  color: var(--color-quadrant-exemplary);
}

.desc-section {
  padding-top: 12px;
  border-top: 1px solid var(--color-border-light);
}

.desc-text {
  font-size: 13px;
  color: var(--color-text-secondary);
  line-height: 1.6;
  margin: 0;
}
</style>
