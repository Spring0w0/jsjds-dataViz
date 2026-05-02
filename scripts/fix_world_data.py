#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据补全脚本
功能：补全 world/data/values_*.json 文件中缺失的指标数据
缺失指标：tobacco_use, alcohol_consumption, disease_cardiovascular, disease_cancer
"""

import csv
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import statistics

# 路径配置
DATASET_DIR = Path(r"C:\Users\yangd\Documents\GitHub\数据集")
WORLD_DATA_DIR = Path(r"C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\world")

# 国家名称映射（GeoJSON中使用的名称 -> 原始数据中的名称）
COUNTRY_NAME_MAPPING = {
    "阿富汗": "阿富汗",
    "阿尔巴尼亚": "阿尔巴尼亚",
    "阿尔及利亚": "阿尔及利亚",
    "亚美尼亚": "亚美尼亚",
    "澳大利亚": "澳大利亚",
    "奥地利": "奥地利",
    "阿塞拜疆": "阿塞拜疆",
    "白俄罗斯": "白俄罗斯",
    "比利时": "比利时",
    "波斯尼亚和黑塞哥维那": "波斯尼亚和黑塞哥维那",
    "博茨瓦纳": "博茨瓦纳",
    "巴西": "巴西",
    "保加利亚": "保加利亚",
    "柬埔寨": "柬埔寨",
    "喀麦隆": "喀麦隆",
    "加拿大": "加拿大",
    "智利": "智利",
    "中国": "中国",
    "哥伦比亚": "哥伦比亚",
    "哥斯达黎加": "哥斯达黎加",
    "克罗地亚": "克罗地亚",
    "古巴": "古巴",
    "捷克共和国": "捷克共和国",
    "丹麦": "丹麦",
    "多米尼克共和国": "多米尼克共和国",
    "厄瓜多尔": "厄瓜多尔",
    "埃及": "埃及",
    "萨尔瓦多": "萨尔瓦多",
    "爱沙尼亚": "爱沙尼亚",
    "埃塞俄比亚": "埃塞俄比亚",
    "芬兰": "芬兰",
    "法国": "法国",
    "格鲁吉亚": "格鲁吉亚",
    "德国": "德国",
    "加纳": "加纳",
    "希腊": "希腊",
    "危地马拉": "危地马拉",
    "海地": "海地",
    "洪都拉斯": "洪都拉斯",
    "匈牙利": "匈牙利",
    "冰岛": "冰岛",
    "印度": "印度",
    "印度尼西亚": "印度尼西亚",
    "伊朗": "伊朗",
    "伊拉克": "伊拉克",
    "爱尔兰": "爱尔兰",
    "以色列": "以色列",
    "意大利": "意大利",
    "牙买加": "牙买加",
    "日本": "日本",
    "约旦": "约旦",
    "哈萨克斯坦": "哈萨克斯坦",
    "肯尼亚": "肯尼亚",
    "韩国": "大韩民国",
    "科威特": "科威特",
    "吉尔吉斯斯坦": "吉尔吉斯共和国",
    "老挝": "老挝人民民主共和国",
    "拉脱维亚": "拉脱维亚",
    "黎巴嫩": "黎巴嫩",
    "立陶宛": "立陶宛",
    "卢森堡": "卢森堡公国",
    "马来西亚": "马来西亚",
    "马达加斯加": "马达加斯加",
    "马里": "马里",
    "毛里塔尼亚": "毛里塔尼亚",
    "墨西哥": "墨西哥",
    "摩尔多瓦": "摩尔多瓦",
    "蒙古": "蒙古",
    "黑山": "黑山",
    "摩洛哥": "摩洛哥",
    "莫桑比克": "莫桑比克",
    "缅甸": "缅甸",
    "纳米比亚": "纳米比亚",
    "尼泊尔": "尼泊尔",
    "荷兰": "荷兰",
    "新西兰": "新西兰",
    "尼加拉瓜": "尼加拉瓜",
    "尼日尔": "尼日尔",
    "尼日利亚": "尼日利亚",
    "挪威": "挪威",
    "巴基斯坦": "巴基斯坦",
    "巴拿马": "巴拿马",
    "巴拉圭": "巴拉圭",
    "秘鲁": "秘鲁",
    "菲律宾": "菲律宾",
    "波兰": "波兰",
    "葡萄牙": "葡萄牙",
    "卡塔尔": "卡塔尔",
    "罗马尼亚": "罗马尼亚",
    "俄罗斯联邦": "俄罗斯联邦",
    "卢旺达": "卢旺达",
    "沙特阿拉伯": "沙特阿拉伯",
    "塞内加尔": "塞内加尔",
    "塞尔维亚": "塞尔维亚",
    "塞拉利昂": "塞拉利昂",
    "新加坡": "新加坡",
    "斯洛伐克": "斯洛伐克共和国",
    "斯洛文尼亚": "斯洛文尼亚",
    "索马里": "索马里",
    "南非": "南非",
    "西班牙": "西班牙",
    "斯里兰卡": "斯里兰卡",
    "苏丹": "苏丹",
    "瑞典": "瑞典",
    "瑞士": "瑞士",
    "叙利亚": "阿拉伯叙利亚共和国",
    "塔吉克斯坦": "塔吉克斯坦",
    "坦桑尼亚": "坦桑尼亚",
    "泰国": "泰国",
    "多哥": "多哥",
    "特立尼达和多巴哥": "特立尼达和多巴哥",
    "突尼斯": "突尼斯",
    "土耳其": "Turkiye",
    "土库曼斯坦": "土库曼斯坦",
    "乌干达": "乌干达",
    "乌克兰": "乌克兰",
    "阿联酋": "阿拉伯联合酋长国",
    "英国": "英国",
    "美国": "美国",
    "乌拉圭": "乌拉圭",
    "乌兹别克斯坦": "乌兹别克斯坦",
    "委内瑞拉": "委内瑞拉玻利瓦尔共和国",
    "越南": "越南",
    "也门": "也门共和国",
    "赞比亚": "赞比亚",
    "津巴布韦": "津巴布韦",
}

def load_disease_data() -> Dict[str, Dict[int, Dict[str, float]]]:
    """加载核心疾病数据（心血管疾病和肿瘤死亡数）"""
    disease_data = {}  # {国家: {年份: {指标: 数值}}}

    disease_dir = DATASET_DIR / "全球各国核心疾病与死亡估算数据"

    for year_file in disease_dir.glob("*.csv"):
        year = int(year_file.stem)
        print(f"加载疾病数据 {year}...")

        with open(year_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                country = row.get('地理位置', '')
                cause = row.get('死亡或受伤原因', '')
                measure = row.get('测量', '')
                value = row.get('数值', '')

                if measure != '死亡' or not value:
                    continue

                if country not in disease_data:
                    disease_data[country] = {}

                if year not in disease_data[country]:
                    disease_data[country][year] = {}

                # 心血管疾病
                if '心血管' in cause:
                    disease_data[country][year]['disease_cardiovascular'] = float(value)

                # 肿瘤
                if '肿瘤' in cause:
                    disease_data[country][year]['disease_cancer'] = float(value)

    return disease_data


def load_tobacco_data() -> Dict[str, Dict[int, float]]:
    """加载烟草相关死亡数据"""
    tobacco_data = {}  # {国家: {年份: 烟草相关死亡数}}

    risk_dir = DATASET_DIR / "全球各国健康风险因素估算数据"

    for year_file in risk_dir.glob("*.csv"):
        year = int(year_file.stem)
        print(f"加载烟草数据 {year}...")

        with open(year_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                country = row.get('地理位置', '')
                risk_factor = row.get('风险因素', '')
                measure = row.get('测量', '')
                value = row.get('数值', '')

                if measure != '死亡' or not value:
                    continue

                if '烟草' in risk_factor:
                    if country not in tobacco_data:
                        tobacco_data[country] = {}

                    tobacco_data[country][year] = float(value)

    return tobacco_data


def load_alcohol_data() -> Dict[str, Dict[int, float]]:
    """加载酒精相关死亡数据"""
    alcohol_data = {}  # {国家: {年份: 酒精相关死亡数}}

    risk_dir = DATASET_DIR / "全球各国健康风险因素估算数据"

    for year_file in risk_dir.glob("*.csv"):
        year = int(year_file.stem)
        print(f"加载酒精数据 {year}...")

        with open(year_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                country = row.get('地理位置', '')
                risk_factor = row.get('风险因素', '')
                measure = row.get('测量', '')
                value = row.get('数值', '')

                if measure != '死亡' or not value:
                    continue

                if '饮酒' in risk_factor:
                    if country not in alcohol_data:
                        alcohol_data[country] = {}

                    alcohol_data[country][year] = float(value)

    return alcohol_data


def load_wdi_data() -> Dict[str, Dict[int, Dict[str, float]]]:
    """加载WDI数据（GDP和卫生支出）"""
    wdi_data = {}  # {国家: {年份: {指标: 数值}}}

    wdi_file = DATASET_DIR / "全球社会经济发展背景数据" / "WDICSV.csv"

    # 指标代码映射
    indicator_mapping = {
        'NY.GDP.PCAP.CD': 'gdp_per_capita',
        'SH.XPD.CHEX.PC.CD': 'health_expenditure_per_capita',
    }

    year_columns = [str(y) for y in range(2000, 2024)]

    with open(wdi_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            indicator_code = row.get('Indicator Code', '')
            if indicator_code not in indicator_mapping:
                continue

            metric_id = indicator_mapping[indicator_code]
            country_name = row.get('Country Name', '')

            if country_name not in wdi_data:
                wdi_data[country_name] = {}

            for year in year_columns:
                value = row.get(year, '')
                if value and value.strip():
                    try:
                        if country_name not in wdi_data:
                            wdi_data[country_name] = {}
                        if year not in wdi_data[country_name]:
                            wdi_data[country_name][year] = {}
                        wdi_data[country_name][year][metric_id] = float(value)
                    except ValueError:
                        pass

    return wdi_data


def calculate_statistics(values: Dict[str, Dict[str, float]], year: int, metric_id: str) -> Dict[str, Any]:
    """计算统计信息"""
    year_data = values.get(str(year), {})
    metric_values = [v[metric_id] for v in year_data.values() if metric_id in v and v[metric_id] is not None]

    if not metric_values:
        return {'max': 0, 'min': 0, 'avg': 0, 'top10': [], 'bottom10': []}

    sorted_values = sorted(metric_values)

    return {
        'max': max(metric_values),
        'min': min(metric_values),
        'avg': statistics.mean(metric_values),
        'top10': sorted_values[-10:] if len(sorted_values) >= 10 else sorted_values[-len(sorted_values):],
        'bottom10': sorted_values[:10] if len(sorted_values) >= 10 else sorted_values[:len(sorted_values)]
    }


def process_year_data(year: int, disease_data: Dict, tobacco_data: Dict, alcohol_data: Dict, wdi_data: Dict, existing_data: Dict) -> Dict:
    """处理单个年份的数据"""

    # 创建国家名称到原始数据名称的映射
    country_mapping = {}

    # 从existing_data获取国家列表
    countries = list(existing_data.get('values', {}).keys())

    result = {
        'values': {},
        'statistics': {}
    }

    # 合并所有指标数据
    all_values = {}  # {国家: {指标: 数值}}

    for country in countries:
        all_values[country] = {}

        # 复制现有数据
        if country in existing_data.get('values', {}):
            for metric, value in existing_data['values'][country].items():
                all_values[country][metric] = value

        # 查找对应的原始数据国家名
        source_country = country  # 默认使用相同名称

        # 尝试通过反向映射查找
        for geojson_name, source_name in COUNTRY_NAME_MAPPING.items():
            if geojson_name == country:
                source_country = source_name
                break

        # 添加心血管疾病数据
        if source_country in disease_data and year in disease_data[source_country]:
            disease = disease_data[source_country][year]
            if 'disease_cardiovascular' in disease:
                all_values[country]['disease_cardiovascular'] = disease['disease_cardiovascular']
            if 'disease_cancer' in disease:
                all_values[country]['disease_cancer'] = disease['disease_cancer']

        # 添加烟草相关死亡数据
        if source_country in tobacco_data and year in tobacco_data[source_country]:
            all_values[country]['tobacco_use'] = tobacco_data[source_country][year]

        # 添加酒精相关死亡数据
        if source_country in alcohol_data and year in alcohol_data[source_country]:
            all_values[country]['alcohol_consumption'] = alcohol_data[source_country][year]

        # 添加WDI数据 (GDP和卫生支出)
        if source_country in wdi_data and str(year) in wdi_data[source_country]:
            wdi = wdi_data[source_country][str(year)]
            if 'gdp_per_capita' in wdi:
                all_values[country]['gdp_per_capita'] = wdi['gdp_per_capita']
            if 'health_expenditure_per_capita' in wdi:
                all_values[country]['health_expenditure_per_capita'] = wdi['health_expenditure_per_capita']

    result['values'] = all_values

    # 计算统计信息
    metrics = ['life_expectancy', 'mortality_under5', 'fertility_rate',
               'gdp_per_capita', 'health_expenditure_per_capita',
               'disease_cardiovascular', 'disease_cancer',
               'tobacco_use', 'alcohol_consumption']

    for metric in metrics:
        values_with_metric = {c: v for c, v in all_values.items() if metric in v}
        if values_with_metric:
            metric_values = [v[metric] for v in values_with_metric.values()]
            sorted_values = sorted(metric_values)

            result['statistics'][metric] = {
                'max': max(metric_values),
                'min': min(metric_values),
                'avg': statistics.mean(metric_values),
                'top10': list(sorted_values[-10:]),
                'bottom10': list(sorted_values[:10])
            }

    return result


def main():
    print("开始数据补全处理...")
    print("=" * 60)

    # 加载原始数据
    print("\n[1/5] 加载核心疾病数据...")
    disease_data = load_disease_data()
    print(f"  加载了 {len(disease_data)} 个国家的心血管和肿瘤数据")

    print("\n[2/5] 加载健康风险因素数据（烟草）...")
    tobacco_data = load_tobacco_data()
    print(f"  加载了 {len(tobacco_data)} 个国家的烟草数据")

    print("\n[3/5] 加载健康风险因素数据（酒精）...")
    alcohol_data = load_alcohol_data()
    print(f"  加载了 {len(alcohol_data)} 个国家的酒精数据")

    print("\n[4/5] 加载WDI数据（GDP和卫生支出）...")
    wdi_data = load_wdi_data()
    print(f"  加载了 {len(wdi_data)} 个国家的WDI数据")

    # 获取年份列表
    years = list(range(2000, 2024))

    print("\n[5/5] 处理和更新每年的数据文件...")

    for year in years:
        year_file = WORLD_DATA_DIR / f"values_{year}.json"

        if not year_file.exists():
            print(f"  警告: {year_file.name} 不存在，跳过")
            continue

        print(f"  处理 {year} 年数据...")

        # 读取现有数据
        with open(year_file, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

        # 处理数据
        processed_data = process_year_data(year, disease_data, tobacco_data, alcohol_data, wdi_data, existing_data)

        # 合并数据
        existing_data['values'] = processed_data['values']
        existing_data['statistics'] = processed_data['statistics']

        # 保存更新后的数据
        with open(year_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)

        print(f"    更新了 {year} 年的数据，包含 {len(processed_data['values'])} 个国家")

    print("\n" + "=" * 60)
    print("数据补全完成！")


if __name__ == '__main__':
    main()
