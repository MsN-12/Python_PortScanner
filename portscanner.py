from socket import *
from threading import *
import optparse

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print ('[+] %d/tcp Open' %tgtPort)
    except:
        print ('[-] %d/tcp Closed' %tgtPort)
    finally:
        sock.close()

def portscan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print ('Unknown Host %s' %tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print ("[*] Scan Results For : " + tgtName[0])
    except:
        print ("[*] Scan Results For : " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target = connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of  program : ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target Ports')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if(tgtHost == None)| (tgtPorts[0] == None):
        print (parser.usage)
        exit(0)
    portscan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()


