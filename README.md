# ChatGPT Streamlit

Este projeto cria uma interface interativa com o modelo ChatGPT utilizando o Streamlit, permitindo que os usuários façam perguntas e recebam respostas em tempo real.

## Funcionalidades

- Interface simples e interativa com Streamlit.
- Consumo da API do ChatGPT para gerar respostas.
- Personalizável para adicionar novas funcionalidades ou melhorar a interação.

## Requisitos

Antes de rodar o projeto, instale as dependências necessárias:

- Python 3.x
- Streamlit
- OpenAI (API key necessária para usar o modelo ChatGPT)

### Instalação

Clone este repositório:

git clone https://github.com/leticiael/ChatGPT-Streamlit.git

Instale as dependências do projeto:

pip install -r requirements.txt

### Configuração da API

Este projeto depende da API da OpenAI para consumir o modelo ChatGPT. Para usar a API, você precisará de uma chave de API da OpenAI.

1. **Obtenha sua chave de API da OpenAI:**
   - Acesse [OpenAI](https://beta.openai.com/signup/) e crie uma conta.
   - Após o login, obtenha a chave da API em [API keys](https://platform.openai.com/account/api-keys).

2. **Configure a chave da API:**
   - Crie um arquivo `.streamlit/secrets.toml` na raiz do projeto.
   - Adicione a chave da API ao arquivo `secrets.toml`:

   [general]  
   openai_api_key = "sua-chave-api"

## Como rodar

1. Navegue até o diretório do projeto:

cd ChatGPT-Streamlit

2. Execute o Streamlit para iniciar a aplicação:

streamlit run streamlitGPT.py

3. Acesse a aplicação no navegador em `http://localhost:8501`.

## Detalhes Técnicos

- **Streamlit:** Usado para criar a interface web interativa, permitindo que o usuário insira texto e veja as respostas geradas pelo ChatGPT.
- **OpenAI API:** A API do ChatGPT é consumida para gerar respostas. As requisições para a API são feitas com a chave configurada no arquivo `secrets.toml`.
- **Arquitetura:** O projeto utiliza Python, com o código principal implementado em `streamlitGPT.py`. A aplicação é construída de forma modular para fácil expansão e customização.

## Contribuindo

Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Fork este repositório.
2. Crie uma branch para sua contribuição (`git checkout -b minha-nova-funcionalidade`).
3. Faça as modificações necessárias.
4. Faça o commit das suas mudanças (`git commit -am 'Adicionando nova funcionalidade'`).
5. Envie as mudanças para o repositório remoto (`git push origin minha-nova-funcionalidade`).
6. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
