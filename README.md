![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Tema](https://img.shields.io/badge/Foco-Monitoramento%20de%20Reservat%C3%B3rio-blue?style=for-the-badge)


# Controle de Níveis de Água 💧
Programa em Python desenvolvido para simular o monitoramento de um reservatório de água, exibindo mensagens de alerta coloridas no terminal de acordo com o nível atual do reservatório.

# Regras e Níveis do Reservatório
O sistema trabalha com cinco níveis de água, associando cada um a uma mensagem de alerta específica e a uma cor distinta para destacar a progressão de risco:

* **Nível 1 (Vermelho):** Muito baixo (crítico)
* **Nível 2 (Amarelo):** Baixo
* **Nível 3 (Verde):** Médio
* **Nível 4 (Ciano):** Alto
* **Nível 5 (Azul):** Muito alto (alerta)


# Como executar o programa no VSCode

### Pré-requisitos
Antes de começar, você precisará ter instalado em sua máquina:
* [VSCode](https://code.visualstudio.com/)
* [Git](https://git-scm.com)
* [Python 3.x](https://www.python.org/)

### 1) Visual Studio Code
Para abrir o terminal integrado do VS Code, acesse o menu superior em **Terminal** > **Novo Terminal** (ou use o atalho `Ctrl + '`).

### 2) Git
No terminal do VS Code, baixe o repositório e acesse a pasta do projeto:

```bash
# a) Clonar o repositório do github para o seu computador
git clone https://github.com/carlaraiol/controle-nivel-agua.git

# b) Acessar a subpasta do projeto
cd controle-niveis-agua
