import dns.resolver
import sys

typeDns = ""

def getIcon():
    print(''' _______  .__   __.      _______.   .______   .______        ______    __  ___  _______ .__   __. 
|       \ |  \ |  |     /       |   |   _  \  |   _  \      /  __  \  |  |/  / |   ____||  \ |  | 
|  .--.  ||   \|  |    |   (----`   |  |_)  | |  |_)  |    |  |  |  | |  '  /  |  |__   |   \|  | 
|  |  |  ||  . `  |     \   \       |   _  <  |      /     |  |  |  | |    <   |   __|  |  . `  | 
|  '--'  ||  |\   | .----)   |      |  |_)  | |  |\  \----.|  `--'  | |  .  \  |  |____ |  |\   | 
|_______/ |__| \__| |_______/       |______/  | _| `._____| \______/  |__|\__\ |_______||__| \__| 
                                                                                                  ''')
print("\n\n")

def split_arq(wordlist):
    try:
        with open(wordlist, "r") as arq:
            sub_domain_opts = arq.read().split("\n")
        return sub_domain_opts
    except:
        getIcon()
        print("\n\n use a valid wordlist")
        sys.exit()
try:
    domain = sys.argv[1]
    wordlist = sys.argv[2]
    if len(sys.argv) == 5 and sys.argv[3] == "-t":
        typeDns = sys.argv[4].upper()
    else:
        typeDns = "A"
except Exception as error:
    getIcon
    print("use: python dnsbroke domain wordlist -t type")
    print(error)
    sys.exit()

resolver = dns.resolver.Resolver()

subdomains = split_arq(wordlist)
getIcon()

for subdomain in subdomains:
    try:
        host = f"{subdomain}.{domain}"
        ips = resolver.resolve(host,typeDns)
        for ip in ips:
            print(f"{host} ---> {ip} --> {typeDns}")
    except:
        pass
print("\n\n")

