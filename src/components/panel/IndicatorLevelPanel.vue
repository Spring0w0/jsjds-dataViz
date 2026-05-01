<template>
  <div class="indicator-panel">
    <div class="panel-header">
      <span class="panel-title">选择指标</span>
    </div>
    
    <div class="level-tabs">
      <button 
        class="level-tab"
        :class="{ active: currentLevel === 'raw' }"
        @click="$emit('update:currentLevel', 'raw')"
      >
        原始数据层
      </button>
      <button 
        class="level-tab"
        :class="{ active: currentLevel === 'derived' }"
        @click="$emit('update:currentLevel', 'derived')"
      >
        分析衍生层
      </button>
    </div>
    
    <div class="category-section">
      <div class="category-label">指标分类</div>
      <div class="category-list">
        <button 
          v-for="cat in categories"
          :key="cat"
          class="category-item"
          :class="{ active: currentCategory === cat }"
          @click="$emit('update:currentCategory', cat)"
        >
          {{ cat }}
        </button>
      </div>
    </div>
    
    <div class="indicator-list">
      <div class="list-label">可选指标</div>
      <div class="list-items">
        <button 
          v-for="item in indicators"
          :key="item.id"
          class="indicator-item"
          :class="{ active: currentIndicator === item.id }"
          @click="$emit('update:currentIndicator', item.id)"
        >
          <div class="item-main">
            <span class="item-name">{{ item.name }}</span>
            <span class="item-unit">{{ item.unit }}</span>
          </div>
          <span class="item-desc">{{ item.desc }}</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  currentLevel: 'raw' | 'derived'
  currentCategory: string
  currentIndicator: string
  categories: string[]
  indicators: Array<{
    id: string
    name: string
    unit: string
    desc: string
  }>
}

defineProps<Props>()

defineEmits<{
  (e: 'update:currentLevel', value: 'raw' | 'derived'): void
  (e: 'update:currentCategory', value: string): void
  (e: 'update:currentIndicator', value: string): void
}>()
</script>

<style scoped>
.indicator-panel {
  height: 100%;
  background: var(--color-bg);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
}

.panel-header {
  padding: 24px 24px 0;
}

.panel-title {
  font-size: 14px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
}

.level-tabs {
  display: flex;
  gap: 6px;
  padding: 16px 24px;
  border-bottom: 1px solid var(--color-border-light);
}

.level-tab {
  flex: 1;
  padding: 10px 16px;
  border: 1px solid var(--color-border);
  background: transparent;
  border-radius: var(--radius-md);
  font-size: 13px;
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.level-tab:hover {
  background: var(--color-bg-secondary);
  color: var(--color-text-primary);
}

.level-tab.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: white;
  box-shadow: var(--shadow-sm);
}

.category-section {
  padding: 16px 24px;
  border-bottom: 1px solid var(--color-border-light);
}

.category-label {
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.category-item {
  padding: 6px 14px;
  background: var(--color-bg-secondary);
  border: none;
  border-radius: var(--radius-full);
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.category-item:hover {
  background: var(--color-bg-tertiary);
  color: var(--color-text-primary);
}

.category-item.active {
  background: var(--color-primary-bg);
  color: var(--color-primary);
}

.indicator-list {
  flex: 1;
  overflow-y: auto;
  padding: 16px 24px 24px;
}

.list-label {
  font-size: 12px;
  font-weight: var(--font-medium);
  color: var(--color-text-tertiary);
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.list-items {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.indicator-item {
  padding: 14px 16px;
  background: var(--color-bg-secondary);
  border: 1px solid transparent;
  border-radius: var(--radius-lg);
  text-align: left;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.indicator-item:hover {
  background: var(--color-bg-tertiary);
  border-color: var(--color-border);
}

.indicator-item.active {
  background: var(--color-primary-bg);
  border-color: var(--color-primary);
}

.item-main {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 4px;
}

.item-name {
  font-size: 14px;
  font-weight: var(--font-medium);
  color: var(--color-text-primary);
}

.indicator-item.active .item-name {
  color: var(--color-primary);
}

.item-unit {
  font-size: 12px;
  color: var(--color-text-tertiary);
}

.item-desc {
  font-size: 12px;
  color: var(--color-text-secondary);
  display: block;
}
</style>
