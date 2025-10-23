# ConversaAI 🤖

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

ConversaAI é um chatbot inteligente desenvolvido em Python, capaz de responder perguntas e manter conversas de forma natural. Ideal para aprendizado, integração com outros sistemas ou para uso pessoal.  

---

## 🚀 Funcionalidades

- Conversa em linguagem natural.
- Mantém contexto de conversa.
- Modular e fácil de expandir.
- Suporte para persistência em SQLite.
- Configuração rápida e fácil execução.

---

## 🛠 Tecnologias

- **Python 3.11+**
- **SQLite** (opcional)
- Bibliotecas listadas em `requirements.txt`

---

## 💻 Instalação

Clone o repositório:

```bash
git clone https://github.com/duskkmusic/ConversaAI.git
cd ConversaAI
Crie e ative o ambiente virtual:

bash
Copiar código
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Linux / Mac
source .venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt

🏃‍♂️ Executando o chatbot

bash
Copiar código
python chatbot.py
Agora o bot está pronto para interagir com você via terminal.

💡 Dica: Você pode modificar chatbot.py para adicionar mais respostas ou integrar APIs externas.

📁 Estrutura do projeto
bash
Copiar código
ConversaAI/
│
├─ .venv/             # Ambiente virtual (não versionado)
├─ __pycache__/       # Arquivos compilados Python (não versionados)
├─ chatbot.py         # Arquivo principal do chatbot
├─ chatbot.db         # Banco de dados SQLite (opcional)
├─ requirements.txt   # Dependências do projeto
└─ README.md          # Este arquivo



📌 Observações
Não versionar .venv, __pycache__ e arquivos temporários.

Fácil de expandir com frameworks de IA ou APIs externas.

📄 Licença
MIT License © 2025 duskkmusic