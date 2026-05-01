# 卫生数据可视化平台

基于 Vue 3 + TypeScript + ECharts 的交互式数据可视化平台，支持中国和全球卫生数据的探索与分析。

## 技术栈

- **框架**: Vue 3 (Composition API)
- **语言**: TypeScript
- **构建工具**: Vite
- **UI 组件库**: Element Plus
- **可视化**: ECharts
- **样式**: Tailwind CSS
- **路由**: Vue Router

## 核心架构

### 数据与组件解耦设计

```
src/
├── data/                    # 数据层（独立）
│   ├── china/
│   │   ├── raw/            # 原始数据层
│   │   └── derived/        # 衍生数据层
│   ├── world/
│   └── types/              # TypeScript 类型定义
├── services/               # 数据服务层
│   ├── data-service.ts     # 基类
│   ├── china-data-service.ts
│   └── world-data-service.ts
├── stores/                 # 状态管理层
├── components/             # 组件层（无数据依赖）
│   ├── layout/
│   ├── map/
│   ├── panel/
│   ├── card/
│   └── chart/
└── views/                  # 页面层（组装数据与组件）
```

## 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

### 构建生产版本

```bash
npm run build
```

### 预览构建结果

```bash
npm run preview
```

## 项目结构

```
jsjds-dataViz/
├── public/
│   └── geo/                # GeoJSON 地图数据
├── src/
│   ├── assets/
│   ├── components/
│   ├── data/
│   ├── services/
│   ├── stores/
│   ├── views/
│   ├── router/
│   ├── App.vue
│   ├── main.ts
│   └── style.css
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
└── postcss.config.js
```

## 功能列表

- [x] 项目初始化
- [ ] 数据预处理（CSV → JSON）
- [ ] 中国地图可视化
- [ ] 指标层级选择（原始/衍生）
- [ ] 数据卡片展示
- [ ] 统计图表（趋势/分布/象限）
- [ ] 世界地图可视化
- [ ] 性能优化
- [ ] 完整测试

## 开发计划

详见 [开发计划.md](../开发计划.md)

## 数据来源

- 中国卫生资源数据
- 世界银行健康数据
- 疾病负担数据

## License

MIT
