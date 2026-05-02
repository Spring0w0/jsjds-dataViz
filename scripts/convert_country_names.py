#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
国家名转换脚本
将数据文件中的中文国家名转换为英文（与GeoJSON匹配）
"""

import json
from pathlib import Path

# 路径配置
GEOJSON_PATH = Path(r"c:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\maps\世界地图.geojson")
WORLD_DATA_DIR = Path(r"c:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\world")

# 完整的中文-英文国家名映射表
CN_TO_EN = {
    "阿富汗": "Afghanistan",
    "阿尔巴尼亚": "Albania",
    "阿尔及利亚": "Algeria",
    "安道尔": "Andorra",
    "安哥拉": "Angola",
    "阿根廷": "Argentina",
    "亚美尼亚": "Armenia",
    "澳大利亚": "Australia",
    "奥地利": "Austria",
    "阿塞拜疆": "Azerbaijan",
    "巴哈马": "Bahamas",
    "巴林": "Bahrain",
    "孟加拉国": "Bangladesh",
    "巴巴多斯": "Barbados",
    "白俄罗斯": "Belarus",
    "比利时": "Belgium",
    "伯利兹": "Belize",
    "贝宁": "Benin",
    "不丹": "Bhutan",
    "玻利维亚": "Bolivia",
    "波斯尼亚和黑塞哥维那": "Bosnia and Herzegovina",
    "博茨瓦纳": "Botswana",
    "巴西": "Brazil",
    "文莱": "Brunei",
    "保加利亚": "Bulgaria",
    "布基纳法索": "Burkina Faso",
    "布隆迪": "Burundi",
    "柬埔寨": "Cambodia",
    "喀麦隆": "Cameroon",
    "加拿大": "Canada",
    "佛得角": "Cabo Verde",
    "中非共和国": "Central African Republic",
    "乍得": "Chad",
    "智利": "Chile",
    "中国": "China",
    "哥伦比亚": "Colombia",
    "科摩罗": "Comoros",
    "刚果民主共和国": "Democratic Republic of the Congo",
    "刚果共和国": "Republic of the Congo",
    "哥斯达黎加": "Costa Rica",
    "科特迪瓦": "Cote d'Ivoire",
    "克罗地亚": "Croatia",
    "古巴": "Cuba",
    "塞浦路斯": "Cyprus",
    "捷克共和国": "Czech Republic",
    "丹麦": "Denmark",
    "吉布提": "Djibouti",
    "多米尼克": "Dominica",
    "多米尼加共和国": "Dominican Republic",
    "厄瓜多尔": "Ecuador",
    "埃及": "Egypt",
    "萨尔瓦多": "El Salvador",
    "赤道几内亚": "Equatorial Guinea",
    "厄立特里亚": "Eritrea",
    "爱沙尼亚": "Estonia",
    "斯威士兰": "Eswatini",
    "埃塞俄比亚": "Ethiopia",
    "斐济": "Fiji",
    "芬兰": "Finland",
    "法国": "France",
    "加蓬": "Gabon",
    "冈比亚": "Gambia",
    "格鲁吉亚": "Georgia",
    "德国": "Germany",
    "加纳": "Ghana",
    "希腊": "Greece",
    "格陵兰": "Greenland",
    "格林纳达": "Grenada",
    "危地马拉": "Guatemala",
    "几内亚": "Guinea",
    "几内亚比绍": "Guinea-Bissau",
    "圭亚那": "Guyana",
    "海地": "Haiti",
    "洪都拉斯": "Honduras",
    "匈牙利": "Hungary",
    "冰岛": "Iceland",
    "印度": "India",
    "印度尼西亚": "Indonesia",
    "伊朗": "Iran",
    "伊拉克": "Iraq",
    "爱尔兰": "Ireland",
    "以色列": "Israel",
    "意大利": "Italy",
    "牙买加": "Jamaica",
    "日本": "Japan",
    "约旦": "Jordan",
    "哈萨克斯坦": "Kazakhstan",
    "肯尼亚": "Kenya",
    "科威特": "Kuwait",
    "吉尔吉斯斯坦": "Kyrgyzstan",
    "老挝": "Laos",
    "拉脱维亚": "Latvia",
    "黎巴嫩": "Lebanon",
    "莱索托": "Lesotho",
    "利比里亚": "Liberia",
    "利比亚": "Libya",
    "立陶宛": "Lithuania",
    "卢森堡": "Luxembourg",
    "马达加斯加": "Madagascar",
    "马拉维": "Malawi",
    "马来西亚": "Malaysia",
    "马尔代夫": "Maldives",
    "马里": "Mali",
    "马耳他": "Malta",
    "毛里塔尼亚": "Mauritania",
    "毛里求斯": "Mauritius",
    "墨西哥": "Mexico",
    "摩尔多瓦": "Moldova",
    "摩纳哥": "Monaco",
    "蒙古": "Mongolia",
    "黑山": "Montenegro",
    "摩洛哥": "Morocco",
    "莫桑比克": "Mozambique",
    "缅甸": "Myanmar",
    "纳米比亚": "Namibia",
    "尼泊尔": "Nepal",
    "荷兰": "Netherlands",
    "新西兰": "New Zealand",
    "尼加拉瓜": "Nicaragua",
    "尼日尔": "Niger",
    "尼日利亚": "Nigeria",
    "北马其顿": "North Macedonia",
    "挪威": "Norway",
    "阿曼": "Oman",
    "巴基斯坦": "Pakistan",
    "巴拿马": "Panama",
    "巴布亚新几内亚": "Papua New Guinea",
    "巴拉圭": "Paraguay",
    "秘鲁": "Peru",
    "菲律宾": "Philippines",
    "波兰": "Poland",
    "葡萄牙": "Portugal",
    "卡塔尔": "Qatar",
    "罗马尼亚": "Romania",
    "俄罗斯联邦": "Russia",
    "卢旺达": "Rwanda",
    "圣基茨和尼维斯": "Saint Kitts and Nevis",
    "圣卢西亚": "Saint Lucia",
    "圣文森特和格林纳丁斯": "Saint Vincent and the Grenadines",
    "萨摩亚": "Samoa",
    "圣马力诺": "San Marino",
    "圣多美和普林西比": "Sao Tome and Principe",
    "沙特阿拉伯": "Saudi Arabia",
    "塞内加尔": "Senegal",
    "塞尔维亚": "Serbia",
    "塞舌尔": "Seychelles",
    "塞拉利昂": "Sierra Leone",
    "新加坡": "Singapore",
    "斯洛伐克共和国": "Slovakia",
    "斯洛文尼亚": "Slovenia",
    "所罗门群岛": "Solomon Islands",
    "索马里": "Somalia",
    "南非": "South Africa",
    "南苏丹": "South Sudan",
    "西班牙": "Spain",
    "斯里兰卡": "Sri Lanka",
    "苏丹": "Sudan",
    "苏里南": "Suriname",
    "瑞典": "Sweden",
    "瑞士": "Switzerland",
    "叙利亚": "Syria",
    "塔吉克斯坦": "Tajikistan",
    "坦桑尼亚": "Tanzania",
    "泰国": "Thailand",
    "东帝汶": "Timor-Leste",
    "多哥": "Togo",
    "汤加": "Tonga",
    "特立尼达和多巴哥": "Trinidad and Tobago",
    "突尼斯": "Tunisia",
    "Turkiye": "Turkey",
    "土库曼斯坦": "Turkmenistan",
    "乌干达": "Uganda",
    "乌克兰": "Ukraine",
    "阿拉伯联合酋长国": "United Arab Emirates",
    "英国": "United Kingdom",
    "美国": "United States",
    "乌拉圭": "Uruguay",
    "乌兹别克斯坦": "Uzbekistan",
    "瓦努阿图": "Vanuatu",
    "委内瑞拉": "Venezuela",
    "Viet Nam": "Vietnam",
    "也门共和国": "Yemen",
    "赞比亚": "Zambia",
    "津巴布韦": "Zimbabwe",
    "大韩民国": "South Korea",
    "吉尔吉斯共和国": "Kyrgyzstan",
    "老挝人民民主共和国": "Laos",
    "阿拉伯叙利亚共和国": "Syria",
    "委内瑞拉玻利瓦尔共和国": "Venezuela",
    "中国香港特别行政区": "Hong Kong",
    "中国澳门特别行政区": "Macau",
    "约旦河西岸和加沙地带": "Palestine",
    "Korea, Dem. People's Rep.": "North Korea",
    "Somalia, Fed. Rep.": "Somalia",
}

# 区域聚合项保持原样（不在GeoJSON中）
REGIONAL_AGGREGATES = {
    "Africa Eastern and Southern",
    "Africa Western and Central",
    "American Samoa",
    "Antigua and Barbuda",
    "Arab World",
    "Aruba",
    "Bahamas, The",
    "Barbados",
    "Belize",
    "Bermuda",
    "Bhutan",
    "British Virgin Islands",
    "Brunei Darussalam",
    "Caribbean small states",
    "Cayman Islands",
    "Central Europe and the Baltics",
    "Channel Islands",
    "Czechia",
    "Early-demographic dividend",
    "East Asia & Pacific",
    "East Asia & Pacific (IDA & IBRD countries)",
    "East Asia & Pacific (excluding high income)",
    "Equatorial Guinea",
    "Eritrea",
    "Eswatini",
    "Euro area",
    "Europe & Central Asia",
    "Europe & Central Asia (IDA & IBRD countries)",
    "Europe & Central Asia (excluding high income)",
    "European Union",
    "Faroe Islands",
    "Fiji",
    "Fragile and conflict affected situations",
    "French Polynesia",
    "Gibraltar",
    "Grenada",
    "Guam",
    "Guinea-Bissau",
    "Guyana",
    "Heavily indebted poor countries (HIPC)",
    "High income",
    "IBRD only",
    "IDA & IBRD total",
    "IDA blend",
    "IDA only",
    "IDA total",
    "Isle of Man",
    "Kiribati",
    "Korea, Dem. People's Rep.",
    "Kosovo",
    "Late-demographic dividend",
    "Latin America & Caribbean",
    "Latin America & Caribbean (excluding high income)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Least developed countries: UN classification",
    "Liechtenstein",
    "Low & middle income",
    "Low income",
    "Lower middle income",
    "Marshall Islands",
    "Micronesia, Fed. Sts.",
    "Middle East, North Africa, Afghanistan & Pakistan",
    "Middle East, North Africa, Afghanistan & Pakistan (IDA & IBRD)",
    "Middle East, North Africa, Afghanistan & Pakistan (excluding high income)",
    "Middle income",
    "Nauru",
    "New Caledonia",
    "North America",
    "Northern Mariana Islands",
    "Not classified",
    "OECD members",
    "Other small states",
    "Pacific island small states",
    "Palau",
    "Post-demographic dividend",
    "Pre-demographic dividend",
    "Puerto Rico (US)",
    "Sao Tome and Principe",
    "Seychelles",
    "Sint Maarten (Dutch part)",
    "Small states",
    "South Asia",
    "South Asia (IDA & IBRD)",
    "St. Kitts and Nevis",
    "St. Lucia",
    "St. Martin (French part)",
    "St. Vincent and the Grenadines",
    "Sub-Saharan Africa",
    "Sub-Saharan Africa (IDA & IBRD countries)",
    "Sub-Saharan Africa (excluding high income)",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Upper middle income",
    "Virgin Islands (U.S.)",
    "World",
}


def extract_geojson_country_names():
    """从GeoJSON提取所有国家名"""
    with open(GEOJSON_PATH, 'r', encoding='utf-8') as f:
        geojson = json.load(f)
    
    countries = []
    for feature in geojson['features']:
        name = feature['properties']['name']
        countries.append(name)
    
    return set(countries)


def convert_country_name(name):
    """转换国家名"""
    if name in REGIONAL_AGGREGATES:
        return name
    return CN_TO_EN.get(name, name)


def process_year_file(year_path):
    """处理单个年份文件"""
    with open(year_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 转换values中的国家名
    new_values = {}
    for cn_name, value in data.get('values', {}).items():
        en_name = convert_country_name(cn_name)
        new_values[en_name] = value
    data['values'] = new_values
    
    # statistics不需要转换（它是值的统计，不依赖国家名）
    
    with open(year_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def process_metadata(metadata_path):
    """处理metadata.json"""
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    # 转换countries数组
    new_countries = []
    for cn_name in metadata.get('countries', []):
        en_name = convert_country_name(cn_name)
        new_countries.append(en_name)
    metadata['countries'] = new_countries
    
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def main():
    print("=" * 60)
    print("开始国家名转换...")
    print("=" * 60)
    
    # 提取GeoJSON中的国家名
    geojson_countries = extract_geojson_country_names()
    print(f"\nGeoJSON包含 {len(geojson_countries)} 个国家/地区")
    
    # 获取年份列表
    years = list(range(2000, 2024))
    
    print(f"\n处理 {len(years)} 个年份文件...")
    
    for year in years:
        year_file = WORLD_DATA_DIR / f"values_{year}.json"
        if year_file.exists():
            process_year_file(year_file)
            print(f"  Updated: values_{year}.json")
    
    # 处理metadata
    print("\n处理 metadata.json...")
    metadata_path = WORLD_DATA_DIR / "metadata.json"
    if metadata_path.exists():
        process_metadata(metadata_path)
        print("  Updated: metadata.json")
    
    print("\n" + "=" * 60)
    print("转换完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
