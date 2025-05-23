import pandas as pd

def generate_prompt(file_path: str, line:int, headers: list) -> str:
    
    descriptions = []
    prompt = 'generate a shell script capable of solving a problem that follows this descritpion:\n'

    df = pd.read_csv(file_path)
    for header in headers:
        content = df.loc[line, header]

        descriptions.append(content)

    for header, description in zip(headers, descriptions):
        prompt += f'{header}: {description}\n'
    
    prompt += 'leave anything that is not the shell script out of your response.'

    return prompt
