chain = None

def getchain():
    global chain
    if chain is None:
        from javascript_fixes import require
        chain = require("proxy-chain")
    return chain

def is_auth_proxy(proxy_url):
    from urllib.parse import urlparse
    parsed_proxy_url = urlparse(proxy_url)
    # If upstream proxy requires no password, return it directly
    if not parsed_proxy_url.username and not parsed_proxy_url.password:
        return False
    
    return True

def create_proxy(proxy_url):
    if is_auth_proxy(proxy_url):
        return getchain().anonymizeProxy(proxy_url,  timeout=300, authInfo={})
    else:
        return proxy_url

def close_proxy(proxy_url):
    if is_auth_proxy(proxy_url):
        return getchain().closeAnonymizedProxy(proxy_url, True)

def add_proxy_options(chrome_options, proxy):
    new_proxy = create_proxy(proxy)
    chrome_options.add_argument(f'--proxy-server='  + new_proxy)
    
    chrome_options.new_proxy = new_proxy
    chrome_options.close_proxy = lambda: close_proxy(new_proxy)

    return chrome_options