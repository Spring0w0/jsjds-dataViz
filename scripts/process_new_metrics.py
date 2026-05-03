#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理新增指标数据脚本
将 risk_factor_importance, mortality_rate, health_inequality 数据添加到 world data JSON 文件
"""

import csv
import json
from pathlib import Path
from typing import Dict, Any, List
import statistics

# 路径配置
CSV_DIR = Path(r"C:\Users\yangd\Documents\GitHub\world\total")
WORLD_DATA_DIR = Path(r"C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\world")

# 国家名称映射（CSV中的中文名 -> GeoJSON中的英文名）
CN_TO_EN_MAPPING = {
    "捷克共和国": "Czech Republic",
    "卢森堡": "Luxembourg",
    "不丹": "Bhutan",
    "东帝汶民主共和国": "Timor-Leste",
    "中国": "China",
    "中非共和国": "Central African Republic",
    "丹麦": "Denmark",
    "乌克兰": "Ukraine",
    "乌兹别克斯坦": "Uzbekistan",
    "乌干达": "Uganda",
    "乌拉圭": "Uruguay",
    "乍得": "Chad",
    "也门": "Yemen",
    "亚美尼亚": "Armenia",
    "以色列": "Israel",
    "伊拉克": "Iraq",
    "伊朗伊斯兰共和国": "Iran",
    "伯利兹城": "Belize",
    "佛得角": "Cabo Verde",
    "俄罗斯": "Russia",
    "保加利亚": "Bulgaria",
    "克罗地亚": "Croatia",
    "关岛": "Guam",
    "冈比亚": "Gambia",
    "冰岛": "Iceland",
    "几内亚": "Guinea",
    "几内亚比绍": "Guinea-Bissau",
    "刚果": "Republic of the Congo",
    "刚果民主共和国": "Democratic Republic of the Congo",
    "利比亚": "Libya",
    "利比里亚": "Liberia",
    "加拿大": "Canada",
    "加纳": "Ghana",
    "加蓬": "Gabon",
    "匈牙利": "Hungary",
    "北马其顿": "North Macedonia",
    "北马里亚纳群岛": "Northern Mariana Islands",
    "南苏丹": "South Sudan",
    "南非": "South Africa",
    "博茨瓦纳": "Botswana",
    "卡塔尔": "Qatar",
    "卢旺达": "Rwanda",
    "卢森堡公国": "Luxembourg",
    "印度": "India",
    "印度尼西亚": "Indonesia",
    "危地马拉": "Guatemala",
    "厄瓜多尔": "Ecuador",
    "厄立特里亚国": "Eritrea",
    "古巴": "Cuba",
    "吉尔吉斯斯坦": "Kyrgyzstan",
    "吉布提": "Djibouti",
    "哈萨克斯坦": "Kazakhstan",
    "哥伦比亚": "Colombia",
    "哥斯达黎加": "Costa Rica",
    "喀麦隆": "Cameroon",
    "图瓦卢": "Tuvalu",
    "土库曼斯坦": "Turkmenistan",
    "土耳其": "Turkey",
    "圣卢西亚岛": "Saint Lucia",
    "圣基茨和尼维斯联邦": "Saint Kitts and Nevis",
    "圣多美和普林西比民主共和国": "Sao Tome and Principe",
    "圣文森特和格林纳丁斯": "Saint Vincent and the Grenadines",
    "圣马力诺共和国": "San Marino",
    "坦桑尼亚联合共和国": "Tanzania",
    "埃及": "Egypt",
    "埃塞俄比亚": "Ethiopia",
    "基里巴斯": "Kiribati",
    "塔吉克斯坦": "Tajikistan",
    "塞内加尔": "Senegal",
    "塞尔维亚": "Serbia",
    "塞拉利昂": "Sierra Leone",
    "塞浦路斯": "Cyprus",
    "塞舌尔": "Seychelles",
    "墨西哥": "Mexico",
    "多哥": "Togo",
    "多米尼加共和国": "Dominican Republic",
    "多米尼加岛": "Dominica",
    "大韩民国": "South Korea",
    "奥地利": "Austria",
    "委内瑞拉玻利瓦尔共和国": "Venezuela",
    "孟加拉国": "Bangladesh",
    "安哥拉": "Angola",
    "安提瓜和巴布达": "Antigua and Barbuda",
    "安道尔共和国": "Andorra",
    "密克罗尼西亚联邦": "Micronesia, Fed. Sts.",
    "尼加拉瓜": "Nicaragua",
    "尼日利亚": "Nigeria",
    "尼日尔": "Niger",
    "尼泊尔": "Nepal",
    "巴勒斯坦": "Palestine",
    "巴哈马": "Bahamas",
    "巴基斯坦": "Pakistan",
    "巴巴多斯": "Barbados",
    "巴布亚新几内亚": "Papua New Guinea",
    "巴拉圭": "Paraguay",
    "巴拿马": "Panama",
    "巴林岛": "Bahrain",
    "巴西": "Brazil",
    "布基纳法索": "Burkina Faso",
    "布隆迪": "Burundi",
    "希腊": "Greece",
    "帕劳共和国": "Palau",
    "库克群岛": "Cook Islands",
    "德国": "Germany",
    "意大利": "Italy",
    "所罗门群岛": "Solomon Islands",
    "托克劳群岛": "Tokelau",
    "拉脱维亚": "Latvia",
    "挪威": "Norway",
    "捷克共和国": "Czech Republic",
    "摩尔多瓦共和国": "Moldova",
    "摩洛哥": "Morocco",
    "摩纳哥公国": "Monaco",
    "文莱达鲁萨兰国": "Brunei",
    "斐济": "Fiji",
    "斯威士兰": "Eswatini",
    "斯洛伐克": "Slovakia",
    "斯洛文尼亚": "Slovenia",
    "斯里兰卡": "Sri Lanka",
    "新加坡": "Singapore",
    "新西兰": "New Zealand",
    "日本": "Japan",
    "智利": "Chile",
    "朝鲜民主主义人民共和国": "North Korea",
    "柬埔寨": "Cambodia",
    "格林纳达": "Grenada",
    "格陵兰": "Greenland",
    "格鲁吉亚": "Georgia",
    "比利时": "Belgium",
    "毛里塔尼亚": "Mauritania",
    "毛里求斯": "Mauritius",
    "汤加": "Tonga",
    "沙特阿拉伯": "Saudi Arabia",
    "法国": "France",
    "波兰": "Poland",
    "波多黎各": "Puerto Rico (US)",
    "波斯尼亚和黑塞哥维那": "Bosnia and Herzegovina",
    "泰国": "Thailand",
    "津巴布韦": "Zimbabwe",
    "洪都拉斯": "Honduras",
    "海地": "Haiti",
    "澳大利亚": "Australia",
    "爱尔兰": "Ireland",
    "爱沙尼亚": "Estonia",
    "牙买加": "Jamaica",
    "特立尼达拉岛和多巴哥": "Trinidad and Tobago",
    "玻利维亚国": "Bolivia",
    "瑙鲁共和国": "Nauru",
    "瑞典": "Sweden",
    "瑞士": "Switzerland",
    "瓦努阿图": "Vanuatu",
    "白俄罗斯": "Belarus",
    "百慕大": "Bermuda",
    "科威特": "Kuwait",
    "科摩罗": "Comoros",
    "科特廸亚": "Cote d'Ivoire",
    "秘鲁": "Peru",
    "突尼斯": "Tunisia",
    "立陶宛": "Lithuania",
    "索马里": "Somalia",
    "约旦": "Jordan",
    "纳米比亚": "Namibia",
    "纽埃": "Niue",
    "缅甸": "Myanmar",
    "罗马尼亚": "Romania",
    "美利坚合众国": "United States",
    "美属维尔京群岛": "Virgin Islands (U.S.)",
    "美属萨摩亚群岛": "American Samoa",
    "老挝人民民主共和国": "Laos",
    "肯尼亚": "Kenya",
    "芬兰": "Finland",
    "苏丹": "Sudan",
    "苏里南": "Suriname",
    "英国": "United Kingdom",
    "荷兰": "Netherlands",
    "莫桑比克": "Mozambique",
    "莱索托": "Lesotho",
    "菲律宾": "Philippines",
    "萨尔瓦多": "El Salvador",
    "萨摩亚": "Samoa",
    "葡萄牙": "Portugal",
    "蒙古": "Mongolia",
    "西班牙": "Spain",
    "贝宁": "Benin",
    "赞比亚": "Zambia",
    "赤道几内亚": "Equatorial Guinea",
    "越南": "Vietnam",
    "阿塞拜疆": "Azerbaijan",
    "阿富汗": "Afghanistan",
    "阿尔及利亚": "Algeria",
    "阿尔巴尼亚": "Albania",
    "阿拉伯叙利亚共和国": "Syria",
    "阿拉伯联合酋长国": "United Arab Emirates",
    "阿曼": "Oman",
    "阿根廷": "Argentina",
    "马尔他": "Malta",
    "马尔代夫": "Maldives",
    "马拉维": "Malawi",
    "马来西亚": "Malaysia",
    "马绍尔群岛": "Marshall Islands",
    "马达加斯加": "Madagascar",
    "马里": "Mali",
    "黑山共和国": "Montenegro",
}


def load_risk_factor_data() -> Dict[str, Dict[str, float]]:
    """加载风险因素重要性数据（长格式）"""
    data = {}  # {国家: {年份: 值}}

    with open(CSV_DIR / "risk_factor_importance_all_years.csv", 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 移除BOM
            country_cn = row['地区'].replace('\ufeff', '')
            year = str(int(row['年份']))
            value = float(row['risk_factor_importance'])

            # 转换为英文名
            country_en = CN_TO_EN_MAPPING.get(country_cn, country_cn)

            if country_en not in data:
                data[country_en] = {}
            data[country_en][year] = value

    return data


def load_mortality_rate_data() -> Dict[str, Dict[str, float]]:
    """加载死亡率数据（宽格式）"""
    data = {}  # {国家: {年份: 值}}

    with open(CSV_DIR / "mortality_rate_all_years.csv", 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country_cn = row['国家'].replace('\ufeff', '')
            country_en = CN_TO_EN_MAPPING.get(country_cn, country_cn)

            if country_en not in data:
                data[country_en] = {}

            for year in range(2000, 2024):
                year_str = str(year)
                if year_str in row and row[year_str].strip():
                    try:
                        data[country_en][year_str] = float(row[year_str])
                    except ValueError:
                        pass

    return data


def load_health_inequality_data() -> Dict[str, Dict[str, float]]:
    """加载健康不平等指数数据（宽格式）"""
    data = {}  # {国家: {年份: 值}}

    with open(CSV_DIR / "health_inequality_wide.csv", 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country_cn = row['国家'].replace('\ufeff', '')
            country_en = CN_TO_EN_MAPPING.get(country_cn, country_cn)

            if country_en not in data:
                data[country_en] = {}

            for year in range(2000, 2024):
                year_str = str(year)
                if year_str in row and row[year_str].strip():
                    try:
                        data[country_en][year_str] = float(row[year_str])
                    except ValueError:
                        pass

    return data


def process_year_data(year: int, risk_data: Dict, mortality_data: Dict, inequality_data: Dict, existing_data: Dict) -> Dict:
    """处理单个年份的数据"""
    year_str = str(year)

    # 合并新指标到 values
    # values 结构: {国家: {指标: 值}}
    for country in existing_data.get('values', {}):
        if country in risk_data and year_str in risk_data[country]:
            existing_data['values'][country]['risk_factor_importance'] = risk_data[country][year_str]

        if country in mortality_data and year_str in mortality_data[country]:
            existing_data['values'][country]['mortality_rate'] = mortality_data[country][year_str]

        if country in inequality_data and year_str in inequality_data[country]:
            existing_data['values'][country]['health_inequality'] = inequality_data[country][year_str]

    # 更新 statistics
    # statistics 结构: {指标Id: {max, min, avg, top10, bottom10}}
    new_metrics = ['risk_factor_importance', 'mortality_rate', 'health_inequality']
    for metric in new_metrics:
        values_with_metric = {c: v[metric] for c, v in existing_data['values'].items() if metric in v}
        if values_with_metric:
            metric_values = list(values_with_metric.values())
            sorted_countries = sorted(values_with_metric.items(), key=lambda x: x[1], reverse=True)

            existing_data['statistics'][metric] = {
                'max': max(metric_values),
                'min': min(metric_values),
                'avg': statistics.mean(metric_values),
                'top10': [c[0] for c in sorted_countries[:10]],
                'bottom10': [c[0] for c in sorted_countries[-10:]]
            }

    return existing_data


def main():
    print("=" * 60)
    print("开始处理新增指标数据...")
    print("=" * 60)

    # 加载数据
    print("\n[1/4] 加载风险因素重要性数据...")
    risk_data = load_risk_factor_data()
    print(f"  加载了 {len(risk_data)} 个国家的数据")

    print("\n[2/4] 加载死亡率数据...")
    mortality_data = load_mortality_rate_data()
    print(f"  加载了 {len(mortality_data)} 个国家的数据")

    print("\n[3/4] 加载健康不平等指数数据...")
    inequality_data = load_health_inequality_data()
    print(f"  加载了 {len(inequality_data)} 个国家的数据")

    print("\n[4/4] 更新年度数据文件...")

    years = list(range(2000, 2024))
    for year in years:
        year_file = WORLD_DATA_DIR / f"values_{year}.json"

        if not year_file.exists():
            print(f"  警告: {year_file.name} 不存在，跳过")
            continue

        # 读取现有数据
        with open(year_file, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

        # 处理数据
        processed_data = process_year_data(year, risk_data, mortality_data, inequality_data, existing_data)

        # 保存更新后的数据
        with open(year_file, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)

        print(f"  Updated: values_{year}.json")

    print("\n" + "=" * 60)
    print("数据处理完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
