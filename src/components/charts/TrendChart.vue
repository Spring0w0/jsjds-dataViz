<template>
  <BaseChart :height="height" :option="chartOption" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { EChartsOption } from 'echarts'
import BaseChart from './BaseChart.vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'
import { useMapStore } from '../../stores/map'

interface Props {
  height?: string
}

const props = withDefaults(defineProps<Props>(), {
  height: '300px'
})

const appStore = useAppStore()
const dataStore = useDataStore()
const mapStore = useMapStore()

const chartOption = computed<EChartsOption>(() => {
  const mode = appStore.mode
  const metricId = dataStore.currentMetricId
  const metric = dataStore.currentMetric
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  const selectedRegion = mapStore.selectedRegion
  
  if (!dataSet || !metric) {
    return {
      title: { text: '请选择指标' }
    }
  }
  
  const years = dataSet.metadata.years
  let trendData: number[] = []
  
  if (selectedRegion && dataSet.trends[selectedRegion]?.[metricId]) {
    const regionTrends = dataSet.trends[selectedRegion][metricId]
    trendData = years.map(year => regionTrends[year] ?? null)
  } else {
    trendData = years.map(year => {
      const yearData = dataSet.values[year]
      const values = Object.values(yearData).map(v => v[metricId] as number).filter(v => v != null)
      if (values.length === 0) return null
      return values.reduce((a, b) => a + b, 0) / values.length
    })
  }
  
  return {
    backgroundColor: '#F5F8FA',
    title: {
      text: selectedRegion ? `${selectedRegion} ${metric.name}趋势` : `全国/全球 ${metric.name}平均趋势`,
      left: 'center',
      textStyle: {
        fontSize: 14,
        color: '#333'
      }
    },
    tooltip: {
      trigger: 'axis'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: years
    },
    yAxis: {
      type: 'value',
      name: metric.unit
    },
    series: [
      {
        name: metric.name,
        type: 'line',
        smooth: true,
        data: trendData,
        areaStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
              { offset: 0, color: metric.colorRange[1] + '60' },
              { offset: 1, color: metric.colorRange[0] + '20' }
            ]
          }
        },
        lineStyle: {
          color: metric.colorRange[1]
        },
        itemStyle: {
          color: metric.colorRange[1]
        }
      }
    ]
  }
})
</script>
