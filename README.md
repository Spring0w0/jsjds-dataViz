# jsjds-dataViz

一个基于 Vue 3 的数据可视化平台，提供中国和世界多维度数据的交互式可视化展示。

## 技术栈

- **前端框架**: Vue 3 (Composition API + `<script setup>`)
- **类型系统**: TypeScript
- **构建工具**: Vite
- **状态管理**: Pinia
- **UI 组件库**: Element Plus
- **图表库**: ECharts
- **HTTP 客户端**: Axios

## 功能特性

### 核心功能
- 🌍 **世界地图可视化**: 展示全球各国的多维度数据
- 🇨🇳 **中国地图可视化**: 展示中国各省份的多维度数据
- 📊 **多种图表类型**:
  - 趋势图: 展示数据随时间的变化趋势
  - 排名图: 展示地区/国家的排名对比
  - 象限图: 多维度数据交叉分析
  - 地图: 地理数据可视化
- ⏱️ **时间轴控制**: 支持 2000-2024 年数据的时间维度选择
- 🔍 **指标树**: 灵活切换不同的数据指标

### 数据范围
- **世界数据**: 2000-2023 年
- **中国数据**: 2005-2024 年

## 快速开始

### 安装依赖

```bash
npm install
```

### 启动开发服务器

```bash
npm run dev
```

### 构建生产版本

```bash
npm run build
```

### 预览生产构建

```bash
npm run preview
```

## 项目结构

```
jsjds-dataViz/
├── public/
│   ├── data/           # 数据文件
│   │   ├── china/      # 中国数据
│   │   └── world/      # 世界数据
│   └── maps/           # 地图 GeoJSON 文件
├── src/
│   ├── components/
│   │   ├── charts/     # 图表组件
│   │   └── layout/     # 布局组件
│   ├── config/         # 配置文件
│   ├── stores/         # Pinia 状态管理
│   ├── views/          # 页面视图
│   ├── App.vue
│   └── main.ts
├── package.json
└── vite.config.ts
```

## 主要组件

- `BaseChart.vue`: 基础图表组件
- `MapChart.vue`: 地图可视化组件
- `TrendChart.vue`: 趋势图组件
- `RankChart.vue`: 排名图组件
- `QuadrantChart.vue`: 象限图组件
- `MainLayout.vue`: 主布局组件
- `MetricTreePanel.vue`: 指标树面板
- `TimelineController.vue`: 时间轴控制器
- `DetailPanel.vue`: 详情面板

## 状态管理

- `app.ts`: 应用全局状态
- `data.ts`: 数据加载与管理
- `map.ts`: 地图相关状态
