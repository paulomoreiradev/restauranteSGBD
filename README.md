# Flask Restaurante

Este projeto é uma aplicação web desenvolvida com Flask para gerenciar mesas, faturamento e funcionários de um restaurante.

## Requisitos

Antes de iniciar o projeto, certifique-se de ter instalado:
- Python 3
- PostgreSQL
- Um ambiente virtual configurado

## Configuração

### 1. Criar e ativar o ambiente virtual
```sh
python -m venv venv
```

No Windows:
```sh
venv\Scripts\activate
```

No macOS/Linux:
```sh
source venv/bin/activate
```

### 2. Instalar dependências
```sh
pip install flask psycopg2
```

### 3. Configurar o banco de dados
Certifique-se de que o PostgreSQL esteja rodando e crie o banco de dados `RestauranteDB`. Atualize as credenciais no arquivo `app.py` conforme necessário:

```python
conn = psycopg2.connect(
    dbname="RestauranteDB",
    user="postgres",
    password="sua_senha",
    host="localhost",
    port="5432"
)
```

### 4. Executar a aplicação
```sh
python app.py
```
Acesse no navegador: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Funcionalidades
- Listar mesas e seus responsáveis
- Exibir relatório de faturamento diário
- Listar, adicionar e excluir funcionários

## Estrutura do Projeto
```
/
│── templates/               # Arquivos HTML
│   ├── index.html
│   ├── faturamento_diario.html
│   ├── funcionarios.html
│   ├── criar_funcionario.html
│── app.py                   # Código principal do Flask
│── README.md                # Documentação do projeto
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias para o projeto!

## Licença
Este projeto é de código aberto e está disponível sob a licença MIT.