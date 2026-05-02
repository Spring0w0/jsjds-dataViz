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
}

const props = withDefaults(defineProps<Props>(), {
  height: '300px'
})

const appStore = useAppStore()
const dataStore = useDataStore()

const chartOption = computed<EChartsOption>(() => {
  const mode = appStore.mode
  const year = appStore.currentYear
  const dataSet = mode === 'china' ? dataStore.chinaData : dataStore.worldData
  
  if (!dataSet || !dataSet.values[year]) {
    return {
      title: { text: '暂无数据' }
    }
  }
  
  const yearData = dataSet.values[year]
  const chartData: any[] = []
  
  // 为了演示，我们使用两个指标来绘制四象限图
  const metrics = Object.values(dataStore.currentLayerMetrics).flat()
  if (metrics.length >= 2) {
    const xMetric = metrics[0]
    const yMetric = metrics[1]
    
    Object.entries(yearData).forEach(([name, values]) => {
      const xValue = values[xMetric.id]
      const yValue = values[yMetric.id]
      
      if (xValue != null && yValue != null) {
        chartData.push({
          name,
          value: [xValue, yValue]
        })
      }
    })
    
    return {
      backgroundColor: '#F5F8FA',
      title: {
        text: '四象限分布图',
        left: 'center',
        textStyle: {
          fontSize: 14,
          color: '#333'
        }
      },
      tooltip: {
        trigger: 'item',
        formatter: (params: any) => {
          return `${params.name}<br/>${xMetric.name}: ${params.value[0]}${xMetric.unit}<br/>${yMetric.name}: ${params.value[1]}${yMetric.unit}`
        }
      },
      grid: {
        left: '3%',
        right: '7%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'value',
        name: xMetric.name,
        nameLocation: 'middle',
        nameGap: 30,
        splitLine: {
          lineStyle: {
            type: 'dashed'
          }
        }
      },
      yAxis: {
        type: 'value',
        name: yMetric.name,
        nameLocation: 'middle',
        nameGap: 50,
        splitLine: {
          lineStyle: {
            type: 'dashed'
          }
        }
      },
      series: [
        {
          type: 'scatter',
          symbolSize: 10,
          data: chartData,
          itemStyle: {
            color: '#003366',
            opacity: 0.7
          },
          emphasis: {
            itemStyle: {
              color: '#FF8C00',
              opacity: 1
            }
          }
        }
      ]
    }
  }
  
  return {
    title: { text: '请选择至少两个指标' }
  }
})
</script>
