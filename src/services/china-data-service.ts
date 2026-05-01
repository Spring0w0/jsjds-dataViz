// 中国数据服务
import { DataService } from './data-service'

export class ChinaDataService extends DataService {
  getIndicators(_level: string): any[] {
    // 待实现
    return []
  }

  getData(_indicator: string, _year?: number): any {
    // 待实现
    return null
  }
}
