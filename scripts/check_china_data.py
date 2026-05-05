import json
data = json.load(open(r'C:\Users\yangd\Documents\GitHub\jsjds-dataViz\public\data\china\values_2023.json', encoding='utf-8'))
print('resource_type stats:', data['statistics'].get('resource_type'))
print('\nquadrant stats:', data['statistics'].get('quadrant'))
print('\nSample data:')
for k, v in list(data['values'].items())[:3]:
    print(f'  {k}: resource_type={v.get("resource_type")}, quadrant={v.get("quadrant")}')
