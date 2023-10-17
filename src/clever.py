import requests
import hashlib
import time

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

cookies = None
cbsid = None
xai = None
last_response = None
last_cookie_update = 0

def send_message(stimulus, context=[], language=None):
    global cookies, cbsid, xai, last_response, last_cookie_update
    
    _context = context.copy()
    
    if cookies is None or time.time() - last_cookie_update >= 86400:
        date = time.strftime("%Y%m%d")
        url = f"https://www.cleverbot.com/extras/conversation-social-min.js?{date}"
        req = requests.get(url, headers={"User-Agent": USER_AGENT})
        cookies = req.headers.get("Set-Cookie")
        last_cookie_update = time.time()
    
    payload = f"stimulus={requests.utils.quote(stimulus)}&"
    
    reverse_context = _context[::-1]
    for i, msg in enumerate(reverse_context):
        payload += f"vText{i + 2}={requests.utils.quote(msg)}&"
    
    payload += f"{'cb_settings_language=' + language + '&' if language else ''}cb_settings_scripting=no&islearning=1&icognoid=wsf&icognocheck="
    payload += hashlib.md5(payload[7:33].encode()).hexdigest()
    
    for _ in range(15):
        try:
            headers = {"Cookie": f"{cookies.split(';')[0]}; _cbsid=-1", "User-Agent": USER_AGENT}
            payload_data = payload.encode('utf-8')
            
            req = requests.post(
                f"https://www.cleverbot.com/webservicemin?uc=UseOfficialCleverbotAPI{'&out=' + requests.utils.quote(last_response) + '&in=' + requests.utils.quote(stimulus) + '&bot=c&cbsid=' + cbsid + '&xai=' + xai + '&ns=2&al=&dl=&flag=&user=&mode=1&alt=0&reac=&emo=&sou=website&xed=&' if cbsid else ''}",
                headers=headers, data=payload_data, timeout=(10, 60), allow_redirects=False
            )
            
            lines = req.text.split("\r")
            cbsid = lines[1]
            xai = f"{cbsid[:3]},{lines[2]}"
            last_response = lines[0]
            
            return last_response
        
        except requests.exceptions.RequestException as err:
            if isinstance(err, requests.exceptions.Timeout):
                # Retry after a bit
                time.sleep(1)
            else:
                raise
        
    raise ValueError("Failed to get a response after 15 tries.")
