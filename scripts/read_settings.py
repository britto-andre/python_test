import yaml

def read_file():
    print('Teste read file')

    with open("./settings.yaml", 'r') as file:
        print(file.read())
        print(yaml.load(file))
        for data in yaml.load_all(file):
            print(data)
        # try:
        #     print(yaml.load(file))
        # except yaml.YAMLError as exc:
        #     print('Arquivo inexistente')
        #     print(exc)



read_file()