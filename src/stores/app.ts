import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    mode: 'china' as 'china' | 'world',
    currentYear: 2024,
    isPlaying: false
  }),
  actions: {
    setMode(mode: 'china' | 'world') {
      this.mode = mode
      if (mode === 'china') {
        this.currentYear = 2024
      } else {
        this.currentYear = 2023
      }
    },
    setYear(year: number) {
      this.currentYear = year
    },
    togglePlaying() {
      this.isPlaying = !this.isPlaying
    },
    setPlaying(playing: boolean) {
      this.isPlaying = playing
    }
  }
})
