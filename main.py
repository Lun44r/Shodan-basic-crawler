import shodan

### SHODAN API

SHODAN_API = 'YOUR_API_HERE'
api = shodan.Shodan(SHODAN_API)

### LAUNCH PROGRAM
print('''
   _____ _    _  ____  _____          _   _    _____ _____       __          ___      ______ _____  
  / ____| |  | |/ __ \|  __ \   /\   | \ | |  / ____|  __ \     /\ \        / / |    |  ____|  __ \ 
 | (___ | |__| | |  | | |  | | /  \  |  \| | | |    | |__) |   /  \ \  /\  / /| |    | |__  | |__) |
  \___ \|  __  | |  | | |  | |/ /\ \ | . ` | | |    |  _  /   / /\ \ \/  \/ / | |    |  __| |  _  / 
  ____) | |  | | |__| | |__| / ____ \| |\  | | |____| | \ \  / ____ \  /\  /  | |____| |____| | \ \ 
 |_____/|_|  |_|\____/|_____/_/    \_\_| \_|  \_____|_|  \_\/_/    \_\/  \/   |______|______|_|  \_\
 
 Search for:
 [1] YAWCAM (No Auth)
 [2] Webcam7 (No Auth)
 [3] Android IP CAM (No Auth)
 [4] HP Printers
 [5] Xerox Printers/Copiers
 [6] Epson Printers
 [7] More Epson Printers
 [8] Cannon Printers
 [9] Logged in root via telnet
 [10] VNC 
 [11] RDP
 '''
)

### DICTIONARY

options = {
    1: r'"Server: yawcam" "Mime-Type: text/html"',
    2: r'("webcam 7" OR "webcamXP") http.component:"mootools"',
    3: r'"Server: IP Webcam Server" "200 OK"',
    4: r'"Serial Number:" "Built:" "Server: HP HTTP"',
    5: r'ssl:"Xerox Generic Root"',
    6: r'"SERVER: EPSON_Linux UPnP" "200 OK"',
    7: r'"Server: KS_HTTP" "200 OK"',
    8: r'"Server: KS_HTTP" "200 OK"',
    9: r'"root@" port:23 -login -password -na',
    10: 'authentication disabled RFB 003.008',
    11: r'"\x03\x00\x00\x0b\x06\xd0\x00\x00\x124\x00"'
}
### SHODAN SEARCH SELECTION

selection = int(input('Select an option: '))
query = options[selection]

### Print Results

def printresult():
    try:
        results = api.search(query)

        print('Results found: ' + str(results['total']))
        for result in results['matches']:
            print('Country: ' + result['location']['country_name'])
            print('IP: ' + result['ip_str'])
            print('Port: ' + str(result['port']))
            print('--------------------------------------------------------------')
    except shodan.APIError:
        print('Error:')

printresult()
print('For educational purposes only')


