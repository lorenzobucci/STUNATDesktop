import socket

import netifaces
import stun

from model.STUNLogger import STUNLogger


def createUDPSocket(ip, port):
    """
    Metodo statico per la creazione di una bind UDP usando l'indirizzo IP e la porta desiderati.
    :return: socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    return s


class Model:

    def __init__(self):
        """
        Inizializzazione variabili del modello.
        """
        self._logger = STUNLogger()  # Logger per la libreria pystun
        self.rawLog = ""

        # Crea un socket sull'interfaccia di default e sulla prima porta libera in modo da 'prenotare' una porta
        self._socket = createUDPSocket("0.0.0.0", 0)
        self.localPort = self._socket.getsockname()[1]

        self.testResults = None
        self.localIPList = ["Default"]

        # Recupero degli indirizzi IP relativi a tutte le interfacce di rete del sistema locale
        for iface in netifaces.interfaces():
            ifaceDetails = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in ifaceDetails:
                for ip_interfaces in ifaceDetails[netifaces.AF_INET]:
                    for key, ip in ip_interfaces.items():
                        if key == 'addr' and ip != '127.0.0.1':
                            self.localIPList.append(ip)

    def startTest(self, serverHostname, serverPort, sourceIP, localPort):
        """
        Esegue il test STUN mediante la libreria pystun e salva i risultati.
        """
        self._logger.resetLog()

        # Traduzione "Default" in "0.0.0.0"
        _sourceIP = sourceIP
        if _sourceIP == "Default":
            _sourceIP = "0.0.0.0"

        # Si chiude il socket attivo e se ne apre un altro che, eventualmente, ha una diversa porta e/o indirizzo IP
        self._socket.close()
        self.localPort = int(localPort)
        self._socket = createUDPSocket(_sourceIP, self.localPort)

        res = stun.get_nat_type(self._socket, _sourceIP, self.localPort, serverHostname, int(serverPort))
        self.testResults = resultsMap[res[0]]
        self.testResults["extIP"] = res[1]['ExternalIP']
        self.testResults["extPort"] = res[1]['ExternalPort']

        self.rawLog = self._logger.getLog()


# Dizionario statico usato per dettagliare il risultato ottenuto dalla libreria pystun
resultsMap = {
    "Blocked": {
        "isAnError": True,
        "errorName": "Connection blocked",
        "errorDescription": "Unable to reach STUN server.\nPlease, check your connection and try again.",
        "natRepresentationImage": "Blocked.png"
    },
    "Open Internet": {
        "isAnError": False,
        "natType": "Open Internet",
        "natRepresentationImage": "OpenInternet.png"
    },
    "Full Cone": {
        "isAnError": False,
        "natType": "Full Cone NAT",
        "natRepresentationImage": "FullConeNAT.png"
    },
    "Symmetric UDP Firewall": {
        "isAnError": False,
        "natType": "Symmetric UDP Firewall",
        "natRepresentationImage": "SymmetricFirewall.png"
    },
    "Restric NAT": {
        "isAnError": False,
        "natType": "Restricted Cone NAT",
        "natRepresentationImage": "RestrictedConeNAT.png"
    },
    "Restric Port NAT": {
        "isAnError": False,
        "natType": "Port Restricted NAT",
        "natRepresentationImage": "PortRestrictedNAT.png"
    },
    "Symmetric NAT": {
        "isAnError": False,
        "natType": "Symmetric NAT",
        "natRepresentationImage": "SymmetricNAT.png"
    },
    "Meet an error, when do Test1 on Changed IP and Port": {
        "isAnError": True,
        "errorName": "Changed address error",
        "errorDescription": "Meet an error, when do Test1 on Changed IP and Port. Try change STUN server.",
        "natRepresentationImage": "UnknownNAT.png"
    }
}
