// 中国数据状态管理
import { ref, reactive } from 'vue'

export const useChinaStore = () => {
  const currentIndicator = ref('')
  const currentYear = ref(2024)
  const selectedProvince = ref<string | null>(null)
  const currentLevel = ref<'raw' | 'derived'>('raw')

  return {
    currentIndicator,
    currentYear,
    selectedProvince,
    currentLevel
  }
}
