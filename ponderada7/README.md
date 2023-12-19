# Ponderada 7

Este repositório contém um sistema simples de reconhecimento de dígitos usando a base de dados MNIST e a biblioteca Keras.

## Instalação

Certifique-se de ter o Python e o pip instalados em seu ambiente. Recomenda-se o uso de um ambiente virtual para evitar conflitos com outras dependências do sistema.

1. Clone o repositório:

    ```bash
    git clone https://github.com/gustavo-francisco/entregas-m8.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd ponderada7
    ```

## Execução

Certifique-se de ter ativado seu ambiente virtual, se estiver usando um.

Recomenda-se o upload do notebook presente no projeto no serviço Google Colab, pois o projeto foi criado e testado no mesmo.

Execute as células de código no notebook para treinar o modelo e testá-lo na base de dados MNIST. Certifique-se de ter conexão com a internet para baixar o conjunto de dados no primeiro uso.

## Descrição do Código

O código está organizado da seguinte forma:

### 1. Carregamento e Pré-processamento de Dados:

Os dados MNIST são carregados e normalizados para o intervalo [0, 1].<br></br>
As imagens são formatadas para entrada na rede neural.

### 2. Definição do Modelo CNN:

Uma CNN (Rede Neural Convolucional) simples é criada utilizando camadas convolucionais, de max pooling e uma camada totalmente conectada.

### 3. Compilação e Treinamento do Modelo:

O modelo é compilado com uma função de perda e um otimizador específicos, e então é treinado usando os dados de treinamento.

### 4. Avaliação do Modelo:

O modelo é avaliado nos dados de teste e a precisão é exibida.

### 5. Prova de Acurácia e Visualização dos Dados:

O modelo realiza previsões em um conjunto de amostras e exibe os resultados, além de visualizar uma amostra aleatória.

## Vídeo de demonstração do projeto:
[Screencast from 13-12-2023 15:32:24.webm](https://github.com/gustavo-francisco/entregas-m8/assets/99208114/11f84533-c6b0-43ea-bd17-f7467ed380cc)
