import json

def read_json(file_path):
    try:
        # Tenta abrir e ler o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)  # Imprime o conteúdo do JSON
    except Exception as e:
        # Se ocorrer qualquer erro, imprime a mensagem de erro
        print("Ocorreu um erro!")
    finally:
        # Sempre imprime a mensagem de conclusão
        print("Processo concluído!")