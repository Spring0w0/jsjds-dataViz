// 世界数据状态管理
import { ref } from 'vue'

export const useWorldStore = () => {
  const currentIndicator = ref('')
  const currentYear = ref(2023)
  const selectedCountry = ref<string | null>(null)
  const currentLevel = ref<'raw' | 'derived'>('raw')
  const selectedContinent = ref<string | null>(null)

  return {
    currentIndicator,
    currentYear,
    selectedCountry,
    currentLevel,
    selectedContinent
  }
}
