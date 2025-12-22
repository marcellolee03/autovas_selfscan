# Gerador de Patch Inteligente

**Solução completa de avaliação de vulnerabilidade e geração de patch inteligente automatizada**

## Features
- **Descoberta de Vulnerabilidade Automatizada**: Identifica automaticamente o IP do localhost, cria a tarefa no OpenVAS e a inicia.
- **Sensível ao Ambiente Computacional**: Incorpora informações do ambiente computacional na geração do patch.
- **Processamento de Dados Inteligente**: Gera um prompt detalhado contendo informações da vulnerabilidade e do ambiente computacional para efetividade máxima.
- **Geração Inteligente de Correção com IA**: Gera patches customizados utilizando a API do Google Gemini ou do Deepseek.
- **Automação Completa**: Automatiza o processo completamente, desde a detecção até a solução.


### Exemplos de Patches Gerados

O repositório contem exemplos reais dos patches gerados com esta solução no diretório `Generated Scripts`.

## Pre-requisitos

- Docker Compose

## Instalação

1. Clonar o Repositório:
```bash
git clone https://github.com/your-username/AutoVAS.git
cd AutoVAS
```

2. Executar o script de setup:
```bash
./setup-autovas.sh
```

## Uso
### Configuração

1. Seleção de LLM: Modifique a linha 46 em 'src/main.py' baseado na LLM que deseja utilizar:
   **Para o Google Gemini:**
   ```python
   response = ask_LLM.ask_gemini(API_KEY, prompt)
   ```
   
   **Para o DeepSeek:**
   ```python
   response = ask_LLM.ask_deepseek(API_KEY, API_URL, prompt)
   ```


### Rodando AutoVAS

Execute a aplicação principal:
```bash
python src/main.py
```
