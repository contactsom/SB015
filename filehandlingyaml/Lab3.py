import yaml

with open('data.yaml') as yamlfile:
    datas=yaml.load_all(yamlfile,Loader=yaml.FullLoader)
    for data in datas:
        for k , v in data.items():
            print(k,"->",v)