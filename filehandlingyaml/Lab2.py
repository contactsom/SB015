import yaml

with open('items.yaml','r') as yamlfile:
    data=yaml.load(yamlfile,Loader=yaml.FullLoader)
    print(data)