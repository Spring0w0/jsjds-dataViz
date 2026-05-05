import json
from pathlib import Path

data_dir = Path(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china')

for year in [2005, 2010, 2015, 2020, 2023]:
    data = json.load(open(data_dir / f'values_{year}.json', encoding='utf-8'))
    quadrant_stats = data['statistics'].get('quadrant')
    resource_type_stats = data['statistics'].get('resource_type')
    print(f'{year}:')
    print(f'  quadrant: {quadrant_stats}')
    print(f'  resource_type: {resource_type_stats}')
