export interface Metric {
  id: string
  name: string
  unit: string
  description: string
  colorRange: [string, string]
  indicatorCode?: string
}

export interface MetricCategory {
  [category: string]: Metric[]
}

export interface MetricsLayer {
  [layer: string]: MetricCategory
}

export const METRICS_CONFIG: {
  china: MetricsLayer
  world: MetricsLayer
} = {
  china: {
    "原始数据层": {
      "卫生资源": [
        {
          id: "health_personnel",
          name: "卫生人员数量",
          unit: "万人",
          description: "各省份卫生技术人员总数",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "health_institutions",
          name: "医疗机构数量",
          unit: "个",
          description: "各省份医疗卫生机构总数",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "health_tech_per_1000",
          name: "每千人口卫生技术人员数",
          unit: "人",
          description: "每千人口拥有的卫生技术人员数",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "institutions_per_10000",
          name: "万人口医疗机构数",
          unit: "个",
          description: "每万人口拥有的医疗机构数",
          colorRange: ["#E8F4FD", "#003366"]
        }
      ],
      "健康产出": [
        {
          id: "life_expectancy",
          name: "平均预期寿命",
          unit: "岁",
          description: "各省份人口平均预期寿命",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "population_mortality",
          name: "人口死亡率",
          unit: "‰",
          description: "各省份人口死亡率",
          colorRange: ["#FFF5F5", "#991B1B"]
        },
        {
          id: "health_expenditure_gdp",
          name: "卫生支出占GDP比重",
          unit: "%",
          description: "各省份卫生支出占GDP的比重",
          colorRange: ["#E8F4FD", "#003366"]
        }
      ]
    },
    "分析衍生层": {
      "效率指标": [
        {
          id: "efficiency_life_personnel",
          name: "效率评分（寿命/人员）",
          unit: "分",
          description: "寿命与卫生人员配置的效率评分",
          colorRange: ["#FFF5F5", "#003366"]
        },
        {
          id: "efficiency_life_institutions",
          name: "效率评分（寿命/机构）",
          unit: "分",
          description: "寿命与医疗机构配置的效率评分",
          colorRange: ["#FFF5F5", "#003366"]
        },
        {
          id: "efficiency_life_expenditure",
          name: "效率评分（寿命/支出）",
          unit: "分",
          description: "寿命与卫生支出配置的效率评分",
          colorRange: ["#FFF5F5", "#003366"]
        },
        {
          id: "comprehensive_efficiency",
          name: "综合效率评分",
          unit: "分",
          description: "衡量卫生资源配置效率的综合指标",
          colorRange: ["#FFE8E6", "#1A365D"]
        }
      ],
      "资源分类": [
        {
          id: "resource_type",
          name: "资源类型",
          unit: "",
          description: "根据指标分析得到的资源类型分类",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "quadrant",
          name: "所属象限",
          unit: "",
          description: "基于投入-产出分析的四象限分类",
          colorRange: ["#E8F4FD", "#003366"]
        }
      ]
    }
  },
  world: {
    "原始数据层": {
      "健康营养和人口统计数据": [
        {
          id: "life_expectancy",
          name: "出生时预期寿命",
          unit: "岁",
          description: "出生时的预期寿命（总）",
          indicatorCode: "SP.DYN.LE00.IN",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "mortality_under5",
          name: "5岁以下儿童死亡率",
          unit: "‰",
          description: "每1000名活产婴儿中5岁以下儿童死亡数",
          indicatorCode: "SH.DYN.MORT",
          colorRange: ["#FFF5F5", "#991B1B"]
        },
        {
          id: "fertility_rate",
          name: "总和生育率",
          unit: "个/妇女",
          description: "平均每个妇女生育子女数",
          indicatorCode: "SP.DYN.TFRT.IN",
          colorRange: ["#E8F4FD", "#003366"]
        }
      ],
      "健康风险因素估算数据": [
        {
          id: "tobacco_use",
          name: "烟草使用率",
          unit: "%",
          description: "15岁以上人口烟草使用比例",
          indicatorCode: "SH.PRV.SMOK",
          colorRange: ["#FFF5F5", "#991B1B"]
        },
        {
          id: "alcohol_consumption",
          name: "酒精消费",
          unit: "升/人/年",
          description: "人均纯酒精消费量（15岁以上）",
          indicatorCode: "SH.ALC.PCAP.LI",
          colorRange: ["#FFF5F5", "#991B1B"]
        }
      ],
      "核心疾病与死亡估算数据": [
        {
          id: "disease_cardiovascular",
          name: "心血管疾病死亡数",
          unit: "人",
          description: "心血管疾病导致的死亡人数",
          colorRange: ["#FFF5F5", "#991B1B"]
        },
        {
          id: "disease_cancer",
          name: "肿瘤死亡数",
          unit: "人",
          description: "肿瘤导致的死亡人数",
          colorRange: ["#FFF5F5", "#991B1B"]
        }
      ],
      "社会经济发展背景数据": [
        {
          id: "gdp_per_capita",
          name: "人均GDP",
          unit: "美元",
          description: "人均国内生产总值（现价美元）",
          indicatorCode: "NY.GDP.PCAP.CD",
          colorRange: ["#E8F4FD", "#003366"]
        },
        {
          id: "health_expenditure_per_capita",
          name: "人均卫生支出",
          unit: "美元",
          description: "人均卫生支出（现价美元）",
          indicatorCode: "SH.XPD.CHEX.PC.CD",
          colorRange: ["#E8F4FD", "#003366"]
        }
      ]
    },
    "分析衍生层": {
      "效率指标": [
        {
          id: "health_efficiency",
          name: "卫生效率指数",
          unit: "分",
          description: "卫生投入产出效率综合评分",
          colorRange: ["#FFE8E6", "#1A365D"]
        },
        {
          id: "risk_factor_importance",
          name: "风险因素重要性",
          unit: "分",
          description: "各风险因素对疾病负担影响程度的量化评估（1.0-9.9分制）",
          colorRange: ["#FFF5F5", "#991B1B"]
        },
        {
          id: "mortality_rate",
          name: "死亡率",
          unit: "‰",
          description: "每1000人口的死亡人数（0.18-24.04‰）",
          colorRange: ["#F0FDF4", "#166534"]
        },
        {
          id: "health_inequality",
          name: "健康不平等指数",
          unit: "",
          description: "衡量不同社会群体之间健康状况差异的综合指标（0.1-0.59）",
          colorRange: ["#FAF5FF", "#6B21A8"]
        }
      ]
    }
  }
}

export const getMetricById = (mode: 'china' | 'world', metricId: string): Metric | null => {
  const layers = METRICS_CONFIG[mode]
  for (const layerName in layers) {
    const categories = layers[layerName]
    for (const categoryName in categories) {
      const metrics = categories[categoryName]
      const metric = metrics.find(m => m.id === metricId)
      if (metric) {
        return metric
      }
    }
  }
  return null
}
