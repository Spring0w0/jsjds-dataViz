#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全面检查和修复中国数据的统计信息
确保所有年份所有指标都有正确的统计信息
"""

import json
import statistics as stats_module
from pathlib import Path

DATA_DIR = Path(r"C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china")

# 分类指标（字符串类型）
CATEGORICAL_METRICS = [
    'resource_type',    # 资源类型
    'quadrant',          # 所属象限
    'new_quadrant',      # 新象限
]

# 需要统计的所有指标
ALL_METRICS = [
    'health_personnel', 'health_institutions', 'life_expectancy',
    'population_mortality', 'population', 'health_tech_per_1000',
    'institutions_per_10000', 'health_expenditure_gdp',
    'mortality_reverse', 'efficiency_life_personnel',
    'efficiency_life_institutions', 'efficiency_life_expenditure',
    'comprehensive_efficiency', 'quadrant', 'resource_type',
    'theoretical_demand', 'residual', 'new_quadrant'
]


def calculate_stats(values_dict: dict, metric: str, is_categorical: bool):
    """计算某个指标的统计信息"""
    # 收集有该指标数据的省份
    values_with_metric = {region: v[metric] for region, v in values_dict.items() if metric in v}

    if not values_with_metric:
        return None

    metric_values = list(values_with_metric.values())

    if is_categorical:
        # 分类数据
        return {
            'unique_values': list(set(metric_values)),
            'count': len(values_with_metric)
        }
    else:
        # 数值型数据
        sorted_countries = sorted(values_with_metric.items(), key=lambda x: x[1], reverse=True)
        return {
            'max': max(metric_values),
            'min': min(metric_values),
            'avg': stats_module.mean(metric_values),
            'top10': [c[0] for c in sorted_countries[:10]],
            'bottom10': [c[0] for c in sorted_countries[-10:]]
        }


def fix_all_statistics():
    """修复所有年份的统计信息"""
    print("=" * 60)
    print("全面检查和修复中国数据的统计信息")
    print("=" * 60)

    years = list(range(2005, 2024))
    total_issues = 0

    for year in years:
        year_file = DATA_DIR / f"values_{year}.json"

        if not year_file.exists():
            print(f"  跳过: values_{year}.json (不存在)")
            continue

        print(f"\n处理: values_{year}.json")

        # 读取数据
        with open(year_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        values = data.get('values', {})
        current_stats = data.get('statistics', {})

        issues_this_file = 0

        for metric in ALL_METRICS:
            is_categorical = metric in CATEGORICAL_METRICS

            # 检查是否已有统计信息且格式正确
            existing = current_stats.get(metric)

            if existing is None:
                # 缺失，添加
                new_stats = calculate_stats(values, metric, is_categorical)
                if new_stats:
                    current_stats[metric] = new_stats
                    print(f"  [新增] {metric}")
                    issues_this_file += 1
            elif is_categorical:
                # 分类数据，检查是否有 unique_values
                if 'unique_values' not in existing:
                    new_stats = calculate_stats(values, metric, is_categorical)
                    if new_stats:
                        current_stats[metric] = new_stats
                        print(f"  [修复] {metric} (添加 unique_values)")
                        issues_this_file += 1
            else:
                # 数值型数据，检查是否有 min/max
                if 'min' not in existing or 'max' not in existing:
                    new_stats = calculate_stats(values, metric, is_categorical)
                    if new_stats:
                        current_stats[metric] = new_stats
                        print(f"  [修复] {metric} (添加 min/max)")
                        issues_this_file += 1

        data['statistics'] = current_stats

        # 保存更新后的数据
        with open(year_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        if issues_this_file > 0:
            print(f"  修复了 {issues_this_file} 个问题")
            total_issues += issues_this_file
        else:
            print(f"  无需修复")

    print("\n" + "=" * 60)
    print(f"处理完成！共修复 {total_issues} 个问题")
    print("=" * 60)


if __name__ == '__main__':
    fix_all_statistics()