<template>
  <div class="world-view">
    <div class="placeholder">
      <h1>🌍 世界数据可视化</h1>
      <p>正在建设中...</p>
      <div class="features">
        <span class="feature">🗺️ 世界地图</span>
        <span class="feature">📊 全球指标</span>
        <span class="feature">🌐 大洲筛选</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.world-view {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.placeholder {
  text-align: center;
  padding: 48px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
}

.placeholder h1 {
  font-size: 32px;
  color: #333;
  margin-bottom: 16px;
}

.placeholder p {
  font-size: 18px;
  color: #666;
  margin-bottom: 32px;
}

.features {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.feature {
  padding: 12px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 24px;
  font-size: 14px;
  font-weight: 500;
}
</style>
