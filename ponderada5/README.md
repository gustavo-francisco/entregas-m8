# Chatbot com LangChain

Este diretório contém um sistema de chatbot construído usando a biblioteca LangChain. O chatbot é projetado para responder perguntas com base em um contexto fornecido, usando um modelo de linguagem.

Vídeos de execução do projeto (dividios em 2, input e output):
[Screencast from 05-12-2023 16:00:39.webm](https://github.com/gustavo-francisco/entregas-m8/assets/99208114/923c9b1c-3b19-45b3-bd60-fbd1fa59b93c)

[Screencast from 05-12-2023 16:04:34.webm](https://github.com/gustavo-francisco/entregas-m8/assets/99208114/49caa224-ec9a-4493-b175-7c6f657152f3)



## Instalação

Clone o repositório para a sua máquina local:

`git clone https://github.com/entregas-m8/ponderada5.git`

Navegue para a pasta:

`cd ponderada5`

Instale as dependências necessárias:

`pip install -r requirements.txt`

## Uso

Execute o sistema de chatbot:

`python3 main.py`

Acesse a interface do chatbot em seu navegador da web, navegando para http://localhost:7860.

Insira um contexto e uma pergunta na caixa de texto fornecida e clique em "Enviar" para obter a resposta do chatbot.

## Explicação do Código

Os principais componentes do sistema de chatbot são os seguintes:

*Carregamento de Texto*: O sistema carrega dados de texto de um arquivo usando a classe TextLoader.

*Divisão de Texto*: O texto é dividido em pedaços usando a classe CharacterTextSplitter.

*Incorporação de Sentenças*: As incorporações de sentenças são geradas usando o modelo SentenceTransformer.

*Armazenamento de Vetores*: As incorporações são usadas para criar um armazenamento de vetores (Chroma) para recuperação eficiente de documentos.

*Modelo de Prompt de Chat*: Um modelo é definido para estruturar a entrada para o chatbot.

*Modelo Ollama*: O modelo de linguagem Mistral (Ollama) é usado para gerar respostas.

*Interface Gradio*: Gradio é usado para criar uma interface simples baseada na web para o chatbot.

*Cadeia do Chatbot*: A lógica do chatbot é definida como uma cadeia de processamento usando o LangChain, incorporando o recuperador, prompt e modelo.

Sinta-se à vontade para explorar e modificar o código para personalizar o chatbot para o seu caso de uso específico.

Para mais informações, consulte a documentação oficial do LangChain:
https://langchain.readthedocs.io/
