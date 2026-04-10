# 📊 Laboratório 02: Evolução e Qualidade de Sistemas Java Open-Source

## 📝 Sobre o Projeto
Este repositório contém a infraestrutura de mineração, extração e análise de dados desenvolvida para o **Laboratório 02** da disciplina de Laboratório de Experimentação de Software (Engenharia de Software). 

O objetivo principal do estudo foi investigar empiricamente se características do ciclo de vida de repositórios open-source no GitHub (popularidade, maturidade, frequência de *releases* e tamanho em linhas de código) impactam a qualidade estrutural interna de sistemas desenvolvidos em Java. 

A pesquisa analisou os **1.000 repositórios Java mais populares**, extraindo a Árvore de Sintaxe Abstrata (AST) via ferramenta **CK** para calcular as medianas das métricas CBO (Acoplamento), DIT (Herança) e LCOM (Falta de Coesão), culminando na aplicação de testes de **Correlação de Spearman**.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Coleta de Dados:** API GraphQL do GitHub
* **Extração de Métricas:** Ferramenta de análise estática [CK (Aniche et al., 2021)](https://github.com/mauricioaniche/ck)
* **Análise de Dados e Estatística:** `pandas`, `scipy.stats`
* **Visualização de Dados:** `matplotlib`, `seaborn`
* **Geração de Relatório:** `markdown`, `WeasyPrint` (renderização de PDF avançada)
* **Ambiente Recomendado:** Linux / WSL (Windows Subsystem for Linux)

## 📁 Estrutura do Repositório

```text
├── data/                       # Arquivos CSV brutos e consolidados (métricas do CK)
├── reports/                    # Artefatos gerados
│   ├── figures/                # Gráficos (Dispersão, Boxplots, Heatmaps, Histogramas)
│   ├── relatorio.md            # Relatório técnico em Markdown
│   └── relatorio.pdf           # Relatório final renderizado
├── src/                        # Código fonte do projeto
│   ├── analysis/               # Scripts de análise estatística e geração de gráficos
│   └── utils/
│       └── md_to_pdf.py        # Script de automação para renderização do relatório
├── .gitignore
├── requirements.txt            # Dependências Python do projeto
└── README.md
```

## 🚀 Como Executar o Projeto

Para garantir a estabilidade das bibliotecas de renderização de PDF (WeasyPrint) e evitar conflitos de sistema, **recomenda-se fortemente a execução em ambiente Linux/WSL**.

### 1. Pré-requisitos de Sistema (Debian/Ubuntu)
Instale as bibliotecas gráficas nativas necessárias para a formatação do PDF e gerenciamento de pacotes:
```bash
sudo apt update
sudo apt install -y python3-venv python3-full libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libffi-dev
```

### 2. Configuração do Ambiente Virtual
Clone o repositório e crie um ambiente virtual isolado (PEP 668):
```bash
git clone https://github.com/JoaoYM/lab-exp-softw-2
cd lab-exp-softw-2
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalação das Dependências
Com o `.venv` ativado, instale os pacotes Python:
```bash
pip install -r requirements.txt
```
*(Caso não tenha o arquivo `requirements.txt` estruturado, instale manualmente: `pip install pandas matplotlib seaborn scipy markdown weasyprint`)*

### 4. Geração das Análises Estatísticas e Gráficos
Para processar o arquivo `ck_metrics_consolidated.csv` e gerar todos os testes de hipótese (Spearman), Boxplots e Histogramas na pasta `reports/figures/`, execute:
```bash
python src/analysis/data_analyzer.py
```
*(Substitua o caminho do script acima pelo nome exato do seu arquivo de análise).*

### 5. Renderização do Relatório (PDF)
Para consolidar os achados e gerar o relatório final de submissão no formato exigido:
```bash
python src/utils/md_to_pdf.py
```
O arquivo `relatorio.pdf` será gerado automaticamente na pasta `reports/` com formatação e paginação acadêmica.
