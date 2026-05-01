// 数据服务基类
export abstract class DataService {
  abstract getIndicators(_level: string): any[]
  abstract getData(_indicator: string, _year?: number): any
}
