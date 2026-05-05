<template>
  <div ref="chartRef" :style="{ width: '100%', height: height }"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import * as echarts from 'echarts'
import type { ECharts } from 'echarts'
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

const categoricalMetrics = ['resource_type', 'quadrant', 'new_quadrant']

// 固定的四个象限分类
const QUADRANT_CATEGORIES = [
  '低投入-低产出（匮乏型）',
  '高投入-低产出（低效型）',
  '低投入-高产出（高效型）',
  '高投入-高产出（协同型）'
]

const RESOURCE_TYPE_CATEGORIES = [
  '资源缺口区',
  '冗余/高效区'
]

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

const getCategoryConfig = (metricId: string) => {
  if (metricId === 'quadrant' || metricId === 'new_quadrant') {
    const colors = ['#36A2EB', '#FF6384', '#4BC0C0', '#FFCE56']
    const colorMap: Record<string, string> = {}
    QUADRANT_CATEGORIES.forEach((cat, idx) => {
      colorMap[cat] = colors[idx % colors.length]
    })
    return { colors: colorMap, categories: QUADRANT_CATEGORIES }
  }

  if (metricId === 'resource_type') {
    const colors = ['#FF6384', '#36A2EB']
    const colorMap: Record<string, string> = {}
    RESOURCE_TYPE_CATEGORIES.forEach((cat, idx) => {
      colorMap[cat] = colors[idx % colors.length]
    })
    return { colors: colorMap, categories: RESOURCE_TYPE_CATEGORIES }
  }

  return null
}

const chartOption = computed(() => {
  const mode = appStore.mode
  const mapName = mode === 'china' ? 'china' : 'world'
  const metric = dataStore.currentMetric
  const metricId = dataStore.currentMetricId

  const mapData = getMapData()
  const categoryConfig = getCategoryConfig(metricId)
  const isCategorical = categoricalMetrics.includes(metricId)

  let seriesData: any[] = []
  if (isCategorical && categoryConfig) {
    seriesData = mapData.map((item: any) => ({
      name: item.name,
      value: item.value,
      itemStyle: {
        areaColor: categoryConfig.colors[item.value] || '#CCCCCC'
      }
    }))
  } else {
    seriesData = mapData.map((item: any) => ({
      name: item.name,
      value: item.value
    }))
  }

  const option: any = {
    backgroundColor: '#F5F8FA',
    tooltip: {
      trigger: 'item',
      formatter: (params: any) => {
        if (params.value != null) {
          if (typeof params.value === 'string') {
            return `${params.name}<br/>${metric?.name || ''}: ${params.value}`
          }
          return `${params.name}<br/>${metric?.name || ''}: ${params.value}${metric?.unit || ''}`
        }
        return params.name
      }
    },
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
        data: seriesData
      }
    ]
  }

  if (isCategorical && categoryConfig) {
    option.visualMap = {
      type: 'piecewise',
      pieces: categoryConfig.categories.map((cat) => ({
        value: cat,
        label: cat,
        color: categoryConfig.colors[cat]
      })),
      left: 'left',
      top: 'bottom',
      calculable: false
    }
  } else if (metric) {
    const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
    const year = appStore.currentYear
    const stats = dataSet?.statistics?.[year]?.[metricId]
    option.visualMap = {
      type: 'continuous',
      min: stats?.min || 0,
      max: stats?.max || 100,
      inRange: {
        color: metric.colorRange || ['#E8F4FD', '#003366']
      },
      left: 'left',
      top: 'bottom',
      text: ['高', '低'],
      calculable: true
    }
  }

  return option
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
