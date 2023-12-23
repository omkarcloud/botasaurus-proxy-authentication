from javascript import require

proxyChain = require("proxy-chain")

def create_proxy(proxy_url):
    return proxyChain.anonymizeProxy(proxy_url);

def close_proxy(proxy_url):
    proxyChain.closeAnonymizedProxy(proxy_url, True)

def add_proxy_options(chrome_options, proxy):
    new_proxy = create_proxy(proxy)
    chrome_options.add_argument(f'--proxy-server='  + new_proxy)
    
    chrome_options.new_proxy = new_proxy
    chrome_options.close_proxy = lambda: close_proxy(new_proxy)

    return chrome_options