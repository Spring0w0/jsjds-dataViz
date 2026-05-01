<template>
  <div class="world-map">
    <div class="map-content">
      <div class="map-placeholder">
        世界地图可视化区域
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.world-map {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.map-content {
  flex: 1;
  padding: 24px;
}

.map-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg-secondary);
  border-radius: var(--radius-lg);
  font-size: 14px;
  color: var(--color-text-tertiary);
}
</style>
