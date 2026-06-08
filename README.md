# Gerador Inteligente de Patches

**Uma solução completa para avaliação automatizada de vulnerabilidades e geração inteligente de patches de remediação.**

## Funcionalidades

* **Descoberta Automatizada de Vulnerabilidades**: Identifica automaticamente o endereço IP local, cria a tarefa no OpenVAS e inicia sua execução.
* **Sensível ao Ambiente de Execução**: Incorpora informações do ambiente computacional ao processo de geração de patches.
* **Processamento Inteligente de Dados**: Gera um prompt detalhado contendo informações sobre vulnerabilidades e características do ambiente computacional para maximizar a eficácia da remediação.
* **Remediação Inteligente Baseada em IA**: Gera patches personalizados utilizando as APIs do Google Gemini ou do DeepSeek.
* **Automação Completa**: Automatiza todo o processo, desde a detecção das vulnerabilidades até a geração das remediações.

## Exemplos de Prompts Utilizados

No diretório `prompt` do repositório, é possível encontrar o prompt utilizado para a geração dos patches de remediação.
Observe que o prompt foi utilizado como uma *f-string* dentro da aplicação principal.

## Exemplos de Patches Gerados

O repositório contém exemplos reais de patches gerados por esta solução no diretório `Generated Scripts`.

## Pré-requisitos

* Docker Compose

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/your-username/AutoVAS.git
cd AutoVAS
```

2. Execute o script de instalação:

```bash
./setup-autovas.sh
```

## Utilização

### Configuração

1. **Definir a API_KEY**: Edite a linha 6 do arquivo `src/main` para incluir sua chave de API:

   * Para o Google Gemini: adicione sua chave da API do Google.
   * Para o DeepSeek: adicione sua chave da API do OpenRouter.

2. **Definir a API_URL**: Edite a linha 7 do arquivo `src/main` para incluir a URL da API:

   * Para o Google Gemini: a constante pode permanecer vazia.
   * Para o DeepSeek: defina `API_URL` como:

```text
https://openrouter.ai/api/v1/chat/completions
```

3. **Seleção do LLM**: Modifique a linha 46 do arquivo `src/main.py` de acordo com o modelo de linguagem que deseja utilizar:

**Para o Google Gemini:**

```python
response = ask_LLM.ask_gemini(API_KEY, prompt)
```

**Para o DeepSeek:**

```python
response = ask_LLM.ask_deepseek(API_KEY, API_URL, prompt)
```

### Executando o AutoVAS

Execute a aplicação principal:

```bash
python src/main.py
```
