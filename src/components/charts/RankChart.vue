<template>
  <BaseChart :height="height" :option="chartOption" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { EChartsOption } from 'echarts'
import BaseChart from './BaseChart.vue'
import { useAppStore } from '../../stores/app'
import { useDataStore } from '../../stores/data'

interface Props {
  height?: string
  showTop?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  height: '300px',
  showTop: true
})

const appStore = useAppStore()
const dataStore = useDataStore()

const chartOption = computed<EChartsOption>(() => {
  const mode = appStore.mode
  const year = appStore.currentYear
  const metricId = dataStore.currentMetricId
  const metric = dataStore.currentMetric
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  
  if (!dataSet || !metric || !dataSet.statistics[year]) {
    return {
      title: { text: '暂无数据' }
    }
  }
  
  const stats = dataSet.statistics[year][metricId]
  if (!stats) {
    return {
      title: { text: '暂无数据' }
    }
  }
  
  const regions = props.showTop ? stats.top10 : stats.bottom10
  const yearData = dataSet.values[year]
  
  const chartData = regions
    .map(name => ({
      name,
      value: yearData[name]?.[metricId] as number
    }))
    .filter(item => item.value != null)
  
  if (!props.showTop) {
    chartData.reverse()
  }
  
  return {
    backgroundColor: '#F5F8FA',
    title: {
      text: props.showTop ? `Top 10 - ${metric.name}` : `Bottom 10 - ${metric.name}`,
      left: 'center',
      textStyle: {
        fontSize: 14,
        color: '#333'
      }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      name: metric.unit
    },
    yAxis: {
      type: 'category',
      data: chartData.map(item => item.name)
    },
    series: [
      {
        name: metric.name,
        type: 'bar',
        data: chartData.map(item => item.value),
        itemStyle: {
          color: {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 1,
            y2: 0,
            colorStops: [
              { offset: 0, color: metric.colorRange[0] },
              { offset: 1, color: metric.colorRange[1] }
            ]
          }
        }
      }
    ]
  }
})
</script>
