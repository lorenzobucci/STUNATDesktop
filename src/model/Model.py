import locale

import netifaces
import stun

resultsMap = {
    "Blocked": ("Blocked", "Blocked.png"),
    "Open Internet": ("Open Internet", "OpenInternet.png"),
    "Full Cone": ("Full Cone NAT", "FullConeNAT.png"),
    "Symmetric UDP Firewall": ("Symmetric UDP Firewall", "SymmetricFirewall.png"),
    "Restric NAT": ("Restricted Cone NAT", "RestrictedConeNAT.png"),
    "Restric Port NAT": ("Port Restricted NAT", "PortRestrictedNAT.png"),
    "Symmetric NAT": ("Symmetric NAT", "SymmetricNAT.png"),
    "Meet an error, when do Test1 on Changed IP and Port": ("Changed Address Error", "UnknownNAT.png")
}


class Model:
    def __init__(self):
        self.localIPList = ["Default"]
        for iface in netifaces.interfaces():
            ifaceDetails = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in ifaceDetails:
                for ip_interfaces in ifaceDetails[netifaces.AF_INET]:
                    for key, ip in ip_interfaces.items():
                        if key == 'addr' and ip != '127.0.0.1':
                            self.localIPList.append(ip)

        self.testResults = {
            "natType": "",
            "natRepresentationImage": "",
            "extIP": "",
            "extPort": 0
        }

        if locale.getdefaultlocale()[0] == "it_IT":
            self.currentOSLanguage = "Italiano"
        else:
            self.currentOSLanguage = "English"

    def startTest(self, serverHostname, serverPort, sourceIP, localPort):
        _sourceIP = sourceIP
        if _sourceIP == "Default":
            _sourceIP = "0.0.0.0"

        res = stun.get_ip_info(_sourceIP, int(localPort), serverHostname, int(serverPort))
        self.testResults["extIP"] = res[1]
        self.testResults["extPort"] = res[2]

        self.testResults["natType"] = resultsMap[res[0]][0]
        self.testResults["natRepresentationImage"] = resultsMap[res[0]][1]
