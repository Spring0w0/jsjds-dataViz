import json
data = json.load(open(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\values_2023.json', encoding='utf-8'))
print('China statistics structure:')
print(f'  statistics keys: {list(data["statistics"].keys())}')
print(f'  resource_type stats: {data["statistics"]["resource_type"]}')
print(f'  quadrant stats: {data["statistics"]["quadrant"]}')
print(f'  life_expectancy stats: {data["statistics"]["life_expectancy"]}')
