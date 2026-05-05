import json
data = json.load(open(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\metadata.json', encoding='utf-8'))
print('Keys in metadata:', list(data.keys()))

# 检查是否有 trends.json
import os
trends_path = r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\trends.json'
print(f'trends.json exists: {os.path.exists(trends_path)}')
