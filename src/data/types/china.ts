// 中国数据类型定义
export interface RawDataPoint {
  province: string
  year: number
  [key: string]: any
}

export interface DerivedDataPoint {
  province: string
  year: number
  [key: string]: any
}

export enum IndicatorLevel {
  RAW = 'raw',
  DERIVED = 'derived'
}
