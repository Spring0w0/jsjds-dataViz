<template>
  <nav class="nav-bar">
    <div class="nav-content">
      <div class="logo">
        <span class="logo-icon">🏥</span>
        <span class="logo-text">卫生数据可视化平台</span>
      </div>
      <div class="nav-tabs">
        <router-link 
          to="/china" 
          class="nav-tab"
          :class="{ active: $route.path === '/china' }"
        >
          中国
        </router-link>
        <router-link 
          to="/world" 
          class="nav-tab"
          :class="{ active: $route.path === '/world' }"
        >
          世界
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
</script>

<style scoped>
.nav-bar {
  height: 64px;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  flex-shrink: 0;
}

.nav-content {
  height: 100%;
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-icon {
  font-size: 24px;
}

.logo-text {
  font-size: 18px;
  font-weight: var(--font-semibold);
  color: var(--color-text-primary);
  letter-spacing: -0.01em;
}

.nav-tabs {
  display: flex;
  gap: 4px;
  background: var(--color-bg-secondary);
  padding: 4px;
  border-radius: var(--radius-lg);
}

.nav-tab {
  padding: 8px 24px;
  border-radius: var(--radius-md);
  color: var(--color-text-secondary);
  text-decoration: none;
  font-size: 14px;
  font-weight: var(--font-medium);
  transition: all var(--transition-fast);
}

.nav-tab:hover {
  color: var(--color-text-primary);
}

.nav-tab.active {
  background: var(--color-bg);
  color: var(--color-primary);
  box-shadow: var(--shadow-sm);
}
</style>
