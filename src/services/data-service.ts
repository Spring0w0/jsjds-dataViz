// 数据服务基类
export abstract class DataService {
  abstract getIndicators(level: string): any[]
  abstract getData(indicator: string, year?: number): any
}
