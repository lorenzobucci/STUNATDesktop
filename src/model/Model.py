import netifaces
import stun


class Model:
    def __init__(self):
        self.testResults = None
        self.localIPList = ["Default"]
        for iface in netifaces.interfaces():
            ifaceDetails = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in ifaceDetails:
                for ip_interfaces in ifaceDetails[netifaces.AF_INET]:
                    for key, ip in ip_interfaces.items():
                        if key == 'addr' and ip != '127.0.0.1':
                            self.localIPList.append(ip)

    def startTest(self, serverHostname, serverPort, sourceIP, localPort):
        _sourceIP = sourceIP
        if _sourceIP == "Default":
            _sourceIP = "0.0.0.0"

        res = stun.get_ip_info(_sourceIP, int(localPort), serverHostname, int(serverPort))
        self.testResults = resultsMap[res[0]]
        self.testResults["extIP"] = res[1]
        self.testResults["extPort"] = res[2]


resultsMap = {
    "Blocked": {
        "isAnError": True,
        "errorName": "Connection blocked",
        "errorDescription": "Unable to reach STUN server.\nPlease, check your connection and try again.",
        "natRepresentationImage": "Blocked.png",
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
        "natRepresentationImage": "UnknownNAT.png",
    }
}
