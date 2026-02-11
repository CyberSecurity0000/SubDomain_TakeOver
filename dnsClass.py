# Bibliotecas
import dns.resolver
import sys, time, json, socket

# Controle de dominios da wordlist
controle = []

# Dicionarios
domain_dict  = {}
domain_dict4 = {}
domain_dict6 = {}


# Classe
class Dnsscan:

    # Checagem de CNAME
    def cnameCheck(domain, wordlist):

        cname_dict = {}

        with open(wordlist, "r") as file:

            arq = file.read().splitlines()

            for i in arq:
                subdomain = f"{i}.{domain}"

                while True:

                    try:
                        resposta = dns.resolver.resolve(subdomain, "CNAME")
                        cname = resposta[0].target
                        cname_dict[subdomain] = str(cname)

                        print(f"{subdomain} tem um alias {cname}")
                        break

                    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                        break

                    except dns.resolver.LifetimeTimeout:
                        continue

            cname_json = json.dumps(cname_dict)

        with open(f"{domain}.json", "w") as file:
            file.write(cname_json)


    # Analise se SubDominio
    def subdomain(domain, wordlist):

        # Resolver - IPv4
        def DNSIPv4(subdomain):
    
            try:
                addr = socket.getaddrinfo(subdomain, None, socket.AF_INET)[2][4][0]
                return addr

            except socket.gaierror:
                pass

            except KeyboardInterrupt:
                print("Interrompido !")

            return 0


        # Resolver - IPv6
        def DNSIPv6(subdomain):

            try:
                addr = socket.getaddrinfo(subdomain, None, socket.AF_INET6)[2][4][0]
                return addr

            except socket.gaierror:
                pass

            except KeyboardInterrupt:
                print("Interrompido !")

            return 0


        # Arquivo com subdominios 
        try:
            with open(wordlist, "r") as file:
        
                # Transformação arquivo em linhas
                arq = file.read().splitlines()

                for i in arq:

                    # Montagem de subdominio
                    subdomain = f"{i}.{domain}"
            
                    try:
                        if subdomain not in controle:
                            addr4 = DNSIPv4(subdomain)
                            addr6 = DNSIPv6(subdomain)

                        if addr4 != 0:
                            print(f"{subdomain}\t\t => {addr4}")

                            controle.append(subdomain)
                            domain_dict4[subdomain] = addr4

                        if addr6 != 0:

                            print(f"{subdomain}\t\t => {addr6}")

                            controle.append(subdomain)
                            domain_dict6[subdomain] = addr6

                    except KeyboardInterrupt:
                        pass

        except KeyboardInterrupt as e:
            print("\n\nPrograma encerrado !")


        # Criação de arquivo Json
        domain_dict["ipv4"] = domain_dict4
        domain_dict["ipv6"] = domain_dict6
        domain_json = json.dumps(domain_dict)

        # Montagem de Json
        try:
            with open(f"lista_{domain}.json", "w") as file:
                file.write(domain_json)

        except Exception as e:
            pass
