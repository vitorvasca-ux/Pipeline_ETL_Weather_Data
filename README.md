# Pipeline ETL — Dados Meteorológicos de São Paulo

Projeto prático de Engenharia de Dados desenvolvido com Python, Pandas, PostgreSQL e Apache Airflow, com o objetivo de construir um pipeline ETL para coleta, transformação e armazenamento de dados meteorológicos.

## Objetivo

Desenvolver um pipeline capaz de consumir dados meteorológicos da API OpenWeather, realizar transformações utilizando Python e Pandas e armazenar os dados em um banco de dados PostgreSQL.

O fluxo foi integrado ao Apache Airflow para permitir a orquestração e o agendamento das etapas do processo.

## Arquitetura do projeto

O projeto segue o fluxo ETL (Extract, Transform, Load):

```text
OpenWeather API
      |
      v
   EXTRACT
 Python + Requests
      |
      v
 weather_data.json
      |
      v
  TRANSFORM
 Python + Pandas
      |
      v
 temp_data.parquet
      |
      v
    LOAD
 Pandas + SQLAlchemy
      |
      v
 PostgreSQL
   sp_weather
```

O Apache Airflow é responsável por orquestrar as três etapas, enquanto o Docker Compose gerencia o ambiente de execução.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento do pipeline |
| Requests | Consumo da API OpenWeather |
| Pandas | Manipulação e transformação dos dados |
| JSON | Armazenamento inicial dos dados extraídos |
| Parquet | Armazenamento intermediário dos dados transformados |
| SQLAlchemy | Integração entre Python e PostgreSQL |
| PostgreSQL | Armazenamento dos dados |
| Apache Airflow | Orquestração do pipeline |
| Docker / Docker Compose | Gerenciamento dos containers |
| WSL2 / Ubuntu | Ambiente de desenvolvimento |

## Etapas do pipeline

### 1. Extract — Extração

- Consumo da API OpenWeather utilizando a biblioteca Requests.
- Coleta de informações meteorológicas de São Paulo, Brasil.
- Armazenamento da resposta da API em formato JSON.

### 2. Transform — Transformação

- Leitura e estruturação dos dados utilizando Pandas.
- Normalização de campos aninhados.
- Seleção, renomeação e organização das colunas.
- Tratamento de informações de data e horário.
- Conversão dos dados para formato Parquet.

### 3. Load — Carregamento

- Leitura do arquivo Parquet.
- Integração com PostgreSQL utilizando SQLAlchemy.
- Inserção dos dados na tabela `sp_weather`.

## Orquestração com Apache Airflow

Foi criada uma DAG chamada `projeto_weather_pipeline`, responsável por coordenar as três tarefas:

- `extract`
- `transform`
- `load`

As tarefas possuem dependências sequenciais, garantindo que cada etapa seja executada após a conclusão da anterior.

**Configurações principais:**

- Agendamento: execução a cada hora.
- Retries: 2 tentativas adicionais.
- Retry delay: 5 minutos.
- Catchup: desabilitado.

## Ambiente de execução

O Apache Airflow foi configurado utilizando Docker Compose, com seus serviços executados em containers.

O desenvolvimento foi realizado em ambiente Ubuntu através do WSL2 no Windows.

## Estrutura do projeto

```text
Primeiro Projeto DATA_ENGINEER/
│
├── config/
├── data/
├── dags/
│   └── weather_dag.py
│
├── src/
│   ├── Exctract_data.py
│   ├── transform_data.py
│   ├── load_data.py
│   └── main.py
│
├── notebooks/
├── docker-compose.yaml
├── pyproject.toml
├── uv.lock
└── README.md
```

## Desafios e aprendizados

Durante o desenvolvimento, foram trabalhados conceitos e desafios relacionados a:

- Consumo de APIs e tratamento de respostas JSON.
- Manipulação de dados com Pandas.
- Diferenças entre formatos JSON e Parquet.
- Integração de Python com PostgreSQL.
- Configuração de ambientes utilizando Docker e WSL2.
- Criação e execução de DAGs no Apache Airflow.
- Identificação e resolução de inconsistências entre a estrutura dos dados e o schema do banco de dados.

Um dos desafios encontrados foi uma divergência entre as colunas do DataFrame e a estrutura da tabela PostgreSQL, identificada por meio da análise do erro e da consulta ao schema do banco.

## Como executar

Para reproduzir o projeto, são necessários:

- Python.
- Docker e Docker Compose.
- PostgreSQL.
- Uma chave de API da [OpenWeather](https://openweathermap.org/api).

As variáveis de ambiente devem ser configuradas localmente, conforme o arquivo `.env.example`, sem expor chaves de API ou credenciais.

O ambiente do Airflow pode ser iniciado com:

```bash
docker compose up -d
```

A interface web do Airflow fica disponível em:

```text
http://localhost:8080
```

As credenciais devem ser configuradas conforme o ambiente local.

## Status do projeto

**Concluído:** pipeline ETL executado com sucesso, incluindo extração, transformação, carregamento e orquestração com Apache Airflow.

Este foi meu primeiro projeto prático na área de Engenharia de Dados, desenvolvido em um processo de aprendizado guiado, com foco na compreensão das etapas de um pipeline ETL e na utilização das ferramentas envolvidas.

---

Desenvolvido por Vitor Vasca.
