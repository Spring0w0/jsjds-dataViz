import { defineStore } from 'pinia'

export const useMapStore = defineStore('map', {
  state: () => ({
    selectedRegion: null as string | null,
    hoveredRegion: null as string | null,
    mapLoaded: {
      china: false,
      world: false
    }
  }),
  actions: {
    selectRegion(region: string | null) {
      this.selectedRegion = region
    },
    hoverRegion(region: string | null) {
      this.hoveredRegion = region
    },
    setMapLoaded(mode: 'china' | 'world', loaded: boolean) {
      this.mapLoaded[mode] = loaded
    }
  }
})
