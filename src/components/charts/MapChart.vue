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

const getCategoryConfig = (): Record<string, string> | null => {
  const metricId = dataStore.currentMetricId
  const dataSet = appStore.mode === 'china' ? dataStore.chinaData : dataStore.worldData

  if (!dataSet) return null

  if (categoricalMetrics.includes(metricId)) {
    const stats: any = dataSet.statistics?.[metricId]
    if (stats && stats.unique_values) {
      const colors = ['#36A2EB', '#FF6384', '#FFCE56', '#4BC0C0', '#9966FF']
      const colorMap: Record<string, string> = {}
      stats.unique_values.forEach((val: string, idx: number) => {
        colorMap[val] = colors[idx % colors.length]
      })
      return colorMap
    }
  }
  return null
}

const chartOption = computed(() => {
  const mode = appStore.mode
  const mapName = mode === 'china' ? 'china' : 'world'
  const metric = dataStore.currentMetric
  const metricId = dataStore.currentMetricId

  const mapData = getMapData()
  const categoryConfig = getCategoryConfig()
  const isCategorical = categoricalMetrics.includes(metricId)

  let seriesData: any[] = []
  if (isCategorical && categoryConfig) {
    seriesData = mapData.map((item: any) => ({
      name: item.name,
      value: item.value,
      itemStyle: {
        areaColor: categoryConfig[item.value] || '#CCCCCC'
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
      pieces: Object.entries(categoryConfig).map(([value, color]) => ({
        value,
        label: value,
        color
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