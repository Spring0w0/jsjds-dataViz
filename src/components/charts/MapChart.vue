<template>
  <div ref="chartRef" :style="{ width: '100%', height: height }"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import * as echarts from 'echarts'
import type { ECharts, EChartsOption } from 'echarts'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'
import { useMapStore } from '../../stores/map'

interface Props {
  height?: string
}

const props = withDefaults(defineProps<Props>(), {
  height: '100%'
})

const emit = defineEmits(['region-click', 'region-hover'])

const chartRef = ref<HTMLElement>()
let chartInstance: ECharts | null = null

const appStore = useAppStore()
const dataStore = useDataStore()
const mapStore = useMapStore()

const loadChinaMap = async () => {
  const response = await fetch('/maps/中华人民共和国.geojson')
  const chinaGeoJSON = await response.json()
  echarts.registerMap('china', chinaGeoJSON)
  mapStore.setMapLoaded('china', true)
}

const loadWorldMap = async () => {
  const response = await fetch('/maps/世界地图.geojson')
  const worldGeoJSON = await response.json()
  echarts.registerMap('world', worldGeoJSON)
  mapStore.setMapLoaded('world', true)
}

const getMapData = () => {
  const mode = appStore.mode
  const year = appStore.currentYear
  const metricId = dataStore.currentMetricId
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  
  if (!dataSet || !dataSet.values[year]) return []
  
  const yearData = dataSet.values[year]
  return Object.entries(yearData).map(([name, values]) => ({
    name,
    value: values[metricId]
  })).filter(item => item.value != null)
}

const getVisualMapConfig = () => {
  const mode = appStore.mode
  const metric = dataStore.currentMetric
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  const year = appStore.currentYear
  
  if (!dataSet || !metric) return null
  
  const stats = dataSet.statistics[year]?.[metric.id]
  if (!stats) return null
  
  return {
    min: stats.min,
    max: stats.max,
    inRange: {
      color: metric.colorRange
    }
  }
}

const chartOption = computed<EChartsOption>(() => {
  const mode = appStore.mode
  const mapName = mode === 'china' ? 'china' : 'world'
  const metric = dataStore.currentMetric
  
  const visualMap = getVisualMapConfig()
  
  return {
    backgroundColor: '#F5F8FA',
    tooltip: {
      trigger: 'item',
      formatter: (params: any) => {
        if (params.value != null) {
          return `${params.name}<br/>${metric?.name || ''}: ${params.value}${metric?.unit || ''}`
        }
        return params.name
      }
    },
    visualMap: visualMap ? {
      type: 'continuous',
      min: visualMap.min,
      max: visualMap.max,
      left: 'left',
      top: 'bottom',
      inRange: visualMap.inRange,
      text: ['高', '低'],
      calculable: true
    } : undefined,
    series: [
      {
        name: metric?.name || '',
        type: 'map',
        map: mapName,
        roam: true,
        scaleLimit: {
          min: 1,
          max: 5
        },
        label: {
          show: false
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 12
          },
          itemStyle: {
            areaColor: '#FF8C00'
          }
        },
        data: getMapData()
      }
    ]
  }
})

const initChart = async () => {
  if (!chartRef.value) return
  
  const mode = appStore.mode
  
  if (mode === 'china' && !mapStore.mapLoaded.china) {
    await loadChinaMap()
  } else if (mode === 'world' && !mapStore.mapLoaded.world) {
    await loadWorldMap()
  }
  
  chartInstance = echarts.init(chartRef.value)
  chartInstance.setOption(chartOption.value)
  
  chartInstance.on('click', (params: any) => {
    if (params.name) {
      mapStore.selectRegion(params.name)
      emit('region-click', params.name)
    }
  })
  
  chartInstance.on('mouseover', (params: any) => {
    if (params.name) {
      mapStore.hoverRegion(params.name)
      emit('region-hover', params.name)
    }
  })
  
  chartInstance.on('mouseout', () => {
    mapStore.hoverRegion(null)
  })
  
  window.addEventListener('resize', handleResize)
}

const handleResize = () => {
  chartInstance?.resize()
}

const updateChart = async () => {
  if (!chartInstance) return
  
  const mode = appStore.mode
  
  if (mode === 'china' && !mapStore.mapLoaded.china) {
    await loadChinaMap()
  } else if (mode === 'world' && !mapStore.mapLoaded.world) {
    await loadWorldMap()
  }
  
  chartInstance.setOption(chartOption.value, true)
}

onMounted(() => {
  initChart()
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  chartInstance?.dispose()
})

watch(() => [appStore.mode, appStore.currentYear, dataStore.currentMetricId], updateChart, { deep: true })
</script>
