# Meat Freshness Classification

Este repositório apresenta um projeto sobre o desenvolvimento de uma aplicação para classificação de frescor de carne utilizando aprendizado de máquina. O objetivo é demonstrar o processo de desenvolvimento, refatoração de um algoritmo já existente, aplicação de padrões de projeto, desenvolvimento de uma API, integração em uma aplicação web usando Flask e, finalmente, o deploy da aplicação.

## Sumário
- [Descrição dos Arquivos](#descrição-dos-arquivos)
- [Instalação para Desenvolvimento](#instalação-para-desenvolvimento)
- [Como Contribuir](#como-contribuir)
- [Citação do Artigo Publicado no Latino Science 2023](#citação-do-artigo-publicado-no-latino-science-2023)


## Descrição dos Arquivos

O repositório está estruturado da seguinte maneira:

- **index.html**: Arquivo HTML utilizado como template para o frontend da aplicação. Responsável pela apresentação visual da classificação de frescor de carne.
- **app.py**: Arquivo principal da aplicação Flask. Contém a lógica para integrar a API de aprendizado de máquina com o frontend.
- **api.py**: Implementação da API Flask que expõe as funcionalidades do algoritmo de aprendizado de máquina para classificação de carne.
- **classificacao_de_carne_random.pkl**: Arquivo contendo o modelo de aprendizado de máquina treinado, utilizado pela API para realizar a classificação de frescor de carne.

## Instalação para Desenvolvimento

Para configurar o ambiente de desenvolvimento, siga estas etapas:

1. **Clone o Repositório**: Clone o repositório para o seu ambiente de desenvolvimento local.
   ```bash
   git clone https://github.com/seu-usuario/meat-freshness-classification.git
   ```
2. **Crie um Ambiente Virtual**: Crie um ambiente virtual para isolar as dependências do projeto.
   ```bash
   python -m venv env
   ```
3. **Ative o Ambiente Virtual**:
   - No Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - No MacOS/Linux:
     ```bash
     source env/bin/activate
     ```
4. **Instale as Dependências**: Instale as dependências necessárias a partir do arquivo `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute a Aplicação**: Execute a aplicação Flask.
   ```bash
   flask run
   ```
## Como Contribuir

Contribuições são bem-vindas! Para contribuir com este projeto, siga estas etapas:

1. **Fork o Repositório**: Crie um fork deste repositório para a sua conta do GitHub.
2. **Clone o Repositório**: Clone o repositório forkado para o seu ambiente de desenvolvimento local.
   ```bash
   git clone https://github.com/seu-usuario/meat-freshness-classification.git
   ```
3. **Crie uma Branch**: Crie uma nova branch para a sua feature ou correção.
   ```bash
   git checkout -b minha-feature
   ```
4. **Faça as Suas Mudanças**: Faça as mudanças necessárias no código.
5. **Commit as Mudanças**: Commit suas mudanças com uma mensagem descritiva.
   ```bash
   git commit -m "Adiciona a minha nova feature"
   ```
6. **Envie para o Repositório Forkado**: Envie suas mudanças para o repositório forkado.
   ```bash
   git push origin minha-feature
   ```
7. **Crie um Pull Request**: Navegue até o repositório original e clique em "New Pull Request" para enviar suas mudanças para revisão.

### Diretrizes de Contribuição

- **Pull Requests**: Todas as contribuições devem ser feitas via pull request. Não envie mudanças diretamente para a branch `main`.
- **Testes**: Certifique-se de que seu código passa todos os testes existentes e, se possível, adicione novos testes para cobrir suas mudanças.

## Citação do Artigo Publicado no Latino Science 2023

Ao utilizar o projeto em seu trabalho de pesquisa ou estudo acadêmico, por favor, faça referência ao artigo que apresenta o projeto:

Link: [https://sol.sbc.org.br/index.php/latinoware/article/view/26093/25916](https://sol.sbc.org.br/index.php/latinoware/article/view/26093/25916)  
Balsanello, Vitor; and Souza, Francisco; . "Adaptação, Desenvolvimento e Implantação de uma API para Classificação de Qualidade de Carne com Aprendizado de Máquina: Um Relato de Experiência." In: Anais do XX Congresso Latino-Americano de Software Livre e Tecnologias Abertas, 2023.

Agradecemos suas contribuições para melhorar o projeto!

