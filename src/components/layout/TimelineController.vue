<template>
  <div class="timeline-controller">
    <div class="timeline-content">
      <div class="mode-switch">
        <el-radio-group v-model="appStore.mode" size="default">
          <el-radio-button value="china">中国</el-radio-button>
          <el-radio-button value="world">世界</el-radio-button>
        </el-radio-group>
      </div>
      
      <div class="year-display">
        <span class="year-label">{{ appStore.mode === 'china' ? '年份' : '年份' }}:</span>
        <span class="year-value">{{ appStore.currentYear }}</span>
      </div>
      
      <div class="timeline-slider">
        <el-slider
          v-model="appStore.currentYear"
          :min="minYear"
          :max="maxYear"
          :step="1"
          :marks="yearMarks"
          show-stops
          @change="handleYearChange"
        />
      </div>
      
      <div class="play-controls">
        <el-button
          :icon="appStore.isPlaying ? VideoPause : VideoPlay"
          @click="togglePlay"
          circle
          size="small"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { VideoPlay, VideoPause } from '@element-plus/icons-vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'

const appStore = useAppStore()
const dataStore = useDataStore()

let playInterval: number | null = null

const minYear = computed(() => {
  const dataSet = appStore.mode === 'china' ? dataStore.chinaData : dataStore.worldData
  if (!dataSet) return appStore.mode === 'china' ? 2005 : 2000
  return Math.min(...dataSet.metadata.years)
})

const maxYear = computed(() => {
  const dataSet = appStore.mode === 'china' ? dataStore.chinaData : dataStore.worldData
  if (!dataSet) return appStore.mode === 'china' ? 2024 : 2023
  return Math.max(...dataSet.metadata.years)
})

const yearMarks = computed(() => {
  const marks: Record<number, string> = {}
  const dataSet = appStore.mode === 'china' ? dataStore.chinaData : dataStore.worldData
  if (!dataSet) return marks
  
  const years = dataSet.metadata.years
  const step = Math.max(1, Math.floor(years.length / 5))
  
  years.forEach((year, index) => {
    if (index % step === 0 || index === years.length - 1) {
      marks[year] = year.toString()
    }
  })
  
  return marks
})

const togglePlay = () => {
  if (appStore.isPlaying) {
    stopPlay()
  } else {
    startPlay()
  }
}

const startPlay = () => {
  appStore.setPlaying(true)
  playInterval = window.setInterval(() => {
    const nextYear = appStore.currentYear + 1
    if (nextYear > maxYear.value) {
      appStore.setYear(minYear.value)
    } else {
      appStore.setYear(nextYear)
    }
  }, 1500)
}

const stopPlay = () => {
  appStore.setPlaying(false)
  if (playInterval) {
    clearInterval(playInterval)
    playInterval = null
  }
}

const handleYearChange = () => {
  stopPlay()
}

watch(() => appStore.mode, () => {
  stopPlay()
})

onMounted(() => {
  // 初始化时加载数据
  if (appStore.mode === 'china') {
    dataStore.loadChinaData()
  } else {
    dataStore.loadWorldData()
  }
})

onUnmounted(() => {
  stopPlay()
})
</script>

<style scoped>
.timeline-controller {
  background: white;
  border-top: 1px solid #e0e0e0;
  padding: 16px 24px;
}

.timeline-content {
  display: flex;
  align-items: center;
  gap: 24px;
}

.mode-switch {
  flex-shrink: 0;
}

.year-display {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.year-label {
  font-size: 14px;
  color: #666;
}

.year-value {
  font-size: 20px;
  font-weight: 600;
  color: #003366;
  min-width: 60px;
}

.timeline-slider {
  flex: 1;
  padding: 0 12px;
}

.play-controls {
  flex-shrink: 0;
}
</style>
