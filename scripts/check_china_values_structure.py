import json

# 检查中国 values_2023.json 结构
china_data = json.load(open(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\values_2023.json', encoding='utf-8'))
print('Top-level keys:', list(china_data.keys()))
print('values type:', type(china_data.get('values')))
print('statistics type:', type(china_data.get('statistics')))

if isinstance(china_data.get('values'), dict):
    first_key = next(iter(china_data['values'].keys()))
    print(f'values first key: {first_key}')
    print(f'values[{first_key}] type:', type(china_data['values'][first_key]))

if isinstance(china_data.get('statistics'), dict):
    first_stat_key = next(iter(china_data['statistics'].keys()))
    print(f'statistics first key: {first_stat_key}')
