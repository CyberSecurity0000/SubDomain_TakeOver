# 🕵️ SubDomainTakeOver & IP Checker

Ferramenta em Python para:

- 🔎 Descobrir o IP de um domínio
- 🚩 Identificar possível Subdomain Takeover
- 📂 Testar subdomínios usando wordlist

Projeto focado em estudos de Pentest, DNS e segurança ofensiva.

---

# ⚙️ Requisitos

- Python 3.10+
- Linux (recomendado: Kali)
- Dependências no arquivo `requirements.txt`

---

# 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/SubDomain_TakeOver.git
cd SubDomain_TakeOver
```

Crie ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Instale dependências:

```bash
pip install -r requirements.txt
```

---

# 🚀 Como usar

Uso básico:

```bash
python main.py dominio.com wordlist.txt
```

Exemplo real:

```bash
python main.py example.com Wordlists/subdomains.txt
```

---

# 🧠 O que o programa faz

1️⃣ Resolve o IP do domínio alvo  
2️⃣ Testa subdomínios da wordlist  
3️⃣ Analisa respostas DNS  
4️⃣ Detecta possíveis falhas de configuração (Subdomain Takeover)  

---

# 📁 Estrutura do Projeto

```
SubDomain_TakeOver/
│
├── Programs/
├── Wordlists/
├── requirements.txt
└── README.md
```

---

# ⚠️ Aviso

Ferramenta para fins educacionais e uso ético.  
Nunca teste domínios sem autorização.

---

# 🛠 Melhorias Futuras

- ⚡ Multi-threading para mais velocidade
- 📊 Exportação de resultados (JSON ou TXT)
- 🔍 Detecção automática de serviços vulneráveis
- 🌐 Integração com ferramentas OSINT

---

# 🧬 Autor

CyberSecurity0000  
Pentest • DNS Analysis • Subdomain Research
