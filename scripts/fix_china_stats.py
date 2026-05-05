#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
补全中国数据的statistics缺失项
"""

import json
import statistics
from pathlib import Path

DATA_DIR = Path(r"C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china")

# 需要补充统计信息的指标
MISSING_METRICS = [
    'population_mortality',      # 人口死亡率
    'efficiency_life_personnel', # 效率评分（寿命/人员）
    'efficiency_life_institutions', # 效率评分（寿命/机构）
    'efficiency_life_expenditure',  # 效率评分（寿命/支出）
    'mortality_reverse',         # 死亡率倒数
    'quadrant',                  # 所属象限
    'resource_type',             # 资源类型
    'theoretical_demand',        # 理论需求
    'residual',                  # 残差
    'new_quadrant'               # 新象限
]


def add_statistics(data: dict) -> dict:
    """为缺失的指标添加统计信息"""
    values = data.get('values', {})
    stats = data.get('statistics', {})

    for metric in MISSING_METRICS:
        if metric in stats:
            continue  # 已有统计信息，跳过

        # 收集有该指标数据的国家
        values_with_metric = {region: v[metric] for region, v in values.items() if metric in v}
        
        if not values_with_metric:
            print(f"  警告: {metric} 没有数据")
            continue

        metric_values = list(values_with_metric.values())
        
        # 判断是否是数值类型
        if isinstance(metric_values[0], (int, float)):
            sorted_countries = sorted(values_with_metric.items(), key=lambda x: x[1], reverse=True)
            stats[metric] = {
                'max': max(metric_values),
                'min': min(metric_values),
                'avg': statistics.mean(metric_values),
                'top10': [c[0] for c in sorted_countries[:10]],
                'bottom10': [c[0] for c in sorted_countries[-10:]]
            }
        else:
            # 非数值类型（如分类数据）
            stats[metric] = {
                'unique_values': list(set(metric_values)),
                'count': len(values_with_metric)
            }

        print(f"  添加: {metric}")

    return data


def main():
    print("=" * 60)
    print("补全中国数据的statistics缺失项")
    print("=" * 60)

    years = list(range(2000, 2024))
    for year in years:
        year_file = DATA_DIR / f"values_{year}.json"
        
        if not year_file.exists():
            print(f"  跳过: values_{year}.json (不存在)")
            continue

        print(f"\n处理: values_{year}.json")
        
        # 读取数据
        with open(year_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 添加统计信息
        data = add_statistics(data)

        # 保存更新后的数据
        with open(year_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("处理完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()