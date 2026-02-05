# 🤖 Automação de Cadastro em Massa (Selenium + PyAutoGUI)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-green)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Desktop%20Automation-orange)
![Status](https://img.shields.io/badge/Status-Finalizado-success)

> Uma solução robusta para automatizar a entrada de dados em sistemas web, eliminando o erro humano e aumentando a produtividade operacional.

## 📄 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema comum em ambientes corporativos: a **tarefa repetitiva e propensa a erros** de cadastrar grandes volumes de dados manualmente.

Utilizando uma abordagem híbrida com **Selenium** (para interação com o navegador) e **PyAutoGUI** (para interações a nível de sistema operacional, como upload de arquivos e janelas nativas), o bot é capaz de processar planilhas de dados e realizar o cadastro autônomo.

### 🎯 Principais Resultados
* **Eficiência:** Redução de X% no tempo de cadastro por item (ex: de 2 min para 10 segundos).
* **Precisão:** Eliminação de erros de digitação (typos) e inconsistência de dados.
* **Disponibilidade:** Capacidade de operar 24/7 sem supervisão constante.

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem base do projeto.
* **[Selenium WebDriver](https://www.selenium.dev/):** Para navegação web, preenchimento de formulários e interação com elementos DOM.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Para controle de mouse/teclado e manipulação de janelas de upload de arquivos (onde o Selenium tem limitações).
* **[Pandas](https://pandas.pydata.org/):** Para leitura e tratamento da base de dados (Excel/CSV) antes do envio.
* **OpenPyXL:** Engine para leitura de arquivos `.xlsx`.

---

## ⚙️ Funcionalidades

- [x] **Leitura de Dados:** Importa dados automaticamente de planilhas Excel (`.xlsx`) ou CSV.
- [x] **Login Automático:** Realiza autenticação segura no portal alvo.
- [x] **Preenchimento Inteligente:** Itera sobre as linhas da planilha preenchendo os campos do formulário web.
- [x] **Tratamento de Uploads:** Usa PyAutoGUI para selecionar arquivos no Windows Explorer quando necessário.
- [x] **Log de Execução:** Gera um relatório (`log.txt` ou nova planilha) informando quais cadastros foram feitos com sucesso e quais falharam.
- [x] **Tratamento de Exceções:** O bot não para se um item der erro; ele registra a falha e passa para o próximo.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.x instalado.
* Google Chrome (ou navegador de sua preferência).
* ChromeDriver compatível com a versão do seu navegador.

### Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
