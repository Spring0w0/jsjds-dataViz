import { defineStore } from 'pinia'
import { getMetricById, type Metric } from '../config/metrics-config'

interface YearData {
  [region: string]: {
    [metricId: string]: number | string
    rank?: number
    resource_type?: string
    quadrant?: string
  }
}

interface Statistics {
  [metricId: string]: {
    max: number
    min: number
    avg: number
    top10: string[]
    bottom10: string[]
  }
}

interface Trends {
  [region: string]: {
    [metricId: string]: {
      [year: string]: number
    }
  }
}

interface DataSet {
  metadata: {
    years: number[]
    [key: string]: any
  }
  values: {
    [year: string]: YearData
  }
  statistics: {
    [year: string]: Statistics
  }
  trends: Trends
}

export const useDataStore = defineStore('data', {
  state: () => ({
    currentMetric: null as Metric | null,
    currentLayer: '原始数据层' as string,
    chinaData: null as DataSet | null,
    worldData: null as DataSet | null,
    isLoading: false,
    currentMetricId: 'health_personnel' as string
  }),
  actions: {
    async loadChinaData() {
      if (this.chinaData) return

      this.isLoading = true
      try {
        const [metadataResponse, trendsResponse] = await Promise.all([
          fetch('/data/china/metadata.json'),
          fetch('/data/china/trends.json')
        ])
        const metadata = await metadataResponse.json()
        const trends = await trendsResponse.json()

        const values: { [year: string]: YearData } = {}
        const statistics: { [year: string]: Statistics } = {}

        for (const year of metadata.years) {
          const valuesRes = await fetch(`/data/china/values_${year}.json`)
          const statsRes = await fetch(`/data/china/statistics_${year}.json`)
          values[year] = await valuesRes.json()
          statistics[year] = await statsRes.json()
        }

        this.chinaData = {
          metadata,
          values,
          statistics,
          trends
        }
      } catch (error) {
        console.error('Failed to load China data:', error)
      } finally {
        this.isLoading = false
      }
    },
    async loadWorldData() {
      if (this.worldData) return

      this.isLoading = true
      try {
        const [metadataResponse, trendsResponse] = await Promise.all([
          fetch('/data/world/metadata.json'),
          fetch('/data/world/trends.json')
        ])
        const metadata = await metadataResponse.json()
        const trends = await trendsResponse.json()

        const values: { [year: string]: YearData } = {}
        const statistics: { [year: string]: Statistics } = {}

        for (const year of metadata.years) {
          const valuesRes = await fetch(`/data/world/values_${year}.json`)
          const statsRes = await fetch(`/data/world/statistics_${year}.json`)
          values[year] = await valuesRes.json()
          statistics[year] = await statsRes.json()
        }

        this.worldData = {
          metadata,
          values,
          statistics,
          trends
        }
      } catch (error) {
        console.error('Failed to load World data:', error)
      } finally {
        this.isLoading = false
      }
    },
    setMetric(mode: 'china' | 'world', metricId: string) {
      this.currentMetricId = metricId
      this.currentMetric = getMetricById(mode, metricId)
    },
    setLayer(layer: string) {
      this.currentLayer = layer
    }
  }
})
