<template>
  <nav class="nav-bar">
    <div class="nav-content">
      <div class="logo">
        <span class="logo-text">🏥 卫生数据可视化平台</span>
      </div>
      <div class="nav-tabs">
        <router-link 
          to="/china" 
          class="nav-tab"
          :class="{ active: $route.path === '/china' }"
        >
          🇨🇳 中国
        </router-link>
        <router-link 
          to="/world" 
          class="nav-tab"
          :class="{ active: $route.path === '/world' }"
        >
          🌍 世界
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
</script>

<style scoped>
.nav-bar {
  height: 60px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  flex-shrink: 0;
}

.nav-content {
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-text {
  font-size: 20px;
  font-weight: 600;
  color: white;
}

.nav-tabs {
  display: flex;
  gap: 8px;
}

.nav-tab {
  padding: 8px 24px;
  border-radius: 8px;
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  transition: all 0.3s;
}

.nav-tab:hover {
  background: rgba(255,255,255,0.15);
  color: white;
}

.nav-tab.active {
  background: white;
  color: #667eea;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
</style>
