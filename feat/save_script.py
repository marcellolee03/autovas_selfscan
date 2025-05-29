
def save_response(response: str, task_name: str):

    caminho = f'generatedscripts/{task_name}.sh'
    with open(caminho, 'w') as f:
        f.write(response)
        
    print(f'Script salvo em: {caminho}')