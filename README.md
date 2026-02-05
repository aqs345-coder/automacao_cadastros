# 🤖 Automação de Cadastro em Massa (Selenium + PyAutoGUI)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Desktop%20Automation-orange)
![Status](https://img.shields.io/badge/Status-Finalizado-success)

> Uma solução robusta para automatizar a entrada de dados em sistemas web, eliminando o erro humano e aumentando a produtividade operacional.

## 📄 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema comum em ambientes corporativos: a **tarefa repetitiva e propensa a erros** de cadastrar grandes volumes de dados manualmente.

Utilizando uma abordagem híbrida com **PyAutoGUI** (para interações a nível de sistema operacional, como upload de arquivos e janelas nativas), o bot é capaz de processar planilhas de dados e realizar o cadastro autônomo.

### 🎯 Principais Resultados
* **Eficiência:** Redução no tempo de cadastro por item.
* **Precisão:** Eliminação de erros de digitação (typos) e inconsistência de dados.
* **Disponibilidade:** Capacidade de operar 24/7 sem supervisão constante.

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem base do projeto.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Para controle de mouse/teclado e manipulação de janelas de upload de arquivos.
* **[Pandas](https://pandas.pydata.org/):** Para leitura e tratamento da base de dados (Excel/CSV) antes do envio.
* **OpenPyXL:** Engine para leitura de arquivos `.xlsx`.

---

## ⚙️ Funcionalidades

- [x] **Leitura de Dados:** Importa dados automaticamente de planilhas Excel (`.xlsx`) ou CSV.
- [x] **Login Automático:** Realiza autenticação segura no portal alvo.
- [x] **Preenchimento Inteligente:** Itera sobre as linhas da planilha preenchendo os campos do formulário web.
- [x] **Tratamento de Uploads:** Usa PyAutoGUI para selecionar arquivos no Windows Explorer quando necessário.

