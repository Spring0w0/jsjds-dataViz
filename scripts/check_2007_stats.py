import json

# 检查2007年数据的统计信息
data = json.load(open(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\values_2007.json', encoding='utf-8'))

print('=== 2007年统计信息 ===')
print(f'statistics keys: {list(data["statistics"].keys())}')
print(f'\nquadrant stats: {data["statistics"].get("quadrant")}')
print(f'\nresource_type stats: {data["statistics"].get("resource_type")}')
print(f'\nhealth_personnel stats: {data["statistics"].get("health_personnel")}')
