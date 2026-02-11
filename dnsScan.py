# Bibliotecas
import sys
import dnsClass

# Paramêtros
domain   = sys.argv[1]
wordlist = sys.argv[2]

# Chamadas de métodos
dnsClass.Dnsscan.subdomain(domain, wordlist)
dnsClass.Dnsscan.cnameCheck(domain, wordlist)
