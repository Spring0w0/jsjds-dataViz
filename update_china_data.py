import csv
import json
import os
import codecs

# 读取CSV文件
csv_path = r'c:\Users\yangd\Documents\GitHub\advanced_resource_analysis_results_complete.csv'
data_dir = r'c:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china'

print("正在读取CSV文件...")

# 存储所有数据，按年份分组
data_by_year = {}

# 使用utf-8-sig处理BOM
with codecs.open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"CSV列名: {reader.fieldnames}")
    for row in reader:
        year = int(row['年份'])
        if year not in data_by_year:
            data_by_year[year] = {}
        data_by_year[year][row['地区']] = row

print(f"找到年份: {list(data_by_year.keys())}")

def update_json(year):
    json_path = os.path.join(data_dir, f'values_{year}.json')
    
    if not os.path.exists(json_path):
        print(f"文件不存在: {json_path}")
        return
    
    print(f"\n正在处理 {year} 年数据...")
    
    # 读取现有JSON文件
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 获取该年份的数据
    year_data = data_by_year.get(year, {})
    
    # 更新 values
    update_count = 0
    quadrant_values = set()
    resource_type_values = set()
    new_quadrant_values = set()
    
    for region, row in year_data.items():
        if region in data['values']:
            # 更新分类字段
            data['values'][region]['quadrant'] = row['所属象限']
            data['values'][region]['resource_type'] = row['资源类型']
            data['values'][region]['new_quadrant'] = row['新象限']
            
            quadrant_values.add(row['所属象限'])
            resource_type_values.add(row['资源类型'])
            new_quadrant_values.add(row['新象限'])
            
            update_count += 1
    
    print(f"已更新 {update_count} 个地区的数据")
    
    # 更新 statistics 中的分类字段
    if 'quadrant' in data['statistics']:
        data['statistics']['quadrant']['unique_values'] = sorted(list(quadrant_values))
        data['statistics']['quadrant']['count'] = len(quadrant_values)
        print(f"quadrant 统计: {len(quadrant_values)} 个唯一值")
    
    if 'resource_type' in data['statistics']:
        data['statistics']['resource_type']['unique_values'] = sorted(list(resource_type_values))
        data['statistics']['resource_type']['count'] = len(resource_type_values)
        print(f"resource_type 统计: {len(resource_type_values)} 个唯一值")
    
    if 'new_quadrant' in data['statistics']:
        data['statistics']['new_quadrant']['unique_values'] = sorted(list(new_quadrant_values))
        data['statistics']['new_quadrant']['count'] = len(new_quadrant_values)
        print(f"new_quadrant 统计: {len(new_quadrant_values)} 个唯一值")
    
    # 保存更新后的JSON文件
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已保存: {json_path}")

# 处理所有年份
for year in sorted(data_by_year.keys()):
    update_json(year)

print("\n✅ 更新完成！")
