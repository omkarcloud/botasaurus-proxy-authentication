# Botasaurus Proxy Authentication

Botasaurus Proxy Authentication provides SSL support for authenticated proxies. 

Proxy providers like BrightData, IPRoyal, and others typically provide authenticated proxies in the format "http://username:password@proxy-provider-domain:port". For example, "http://greyninja:awesomepassword@geo.iproyal.com:12321".

However, if you use an authenticated proxy with a library like seleniumwire to scrape a Cloudflare protected website like G2.com, you will surely be blocked because you are using a non-SSL connection. 

To verify this, run the following code:

First, install the necessary packages:
```bash 
python -m pip install selenium_wire chromedriver_autoinstaller
```

Then, execute this Python script:
```python
from seleniumwire import webdriver
from chromedriver_autoinstaller import install

# Define the proxy
proxy_options = {
    'proxy': {
        'http': 'http://username:password@proxy-provider-domain:port', # TODO: Replace with your own proxy
        'https': 'http://username:password@proxy-provider-domain:port', # TODO: Replace with your own proxy
    }
}

# Install and set up the driver
driver_path = install()
driver = webdriver.Chrome(driver_path, seleniumwire_options=proxy_options)

# Navigate to the desired URL
driver.get("https://ipinfo.io/")

# Prompt for user input
input("Press Enter to exit...")

# Clean up
driver.quit()
```

You will definetely encounter a block by Cloudflare:

![blocked](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/seleniumwireblocked.png)

However, using proxies with botasaurus_proxy_authentication prevents this issue. See the difference by running the following code:

First, install the necessary packages:
```bash 
python -m pip install botasaurus
```

Then, execute this Python script:

```python
from botasaurus import *

@browser(proxy="http://username:password@proxy-provider-domain:port") # TODO: Replace with your own proxy 
def scrape_heading_task(driver: AntiDetectDriver, data):
    driver.get("https://ipinfo.io/")
    driver.prompt()
scrape_heading_task()    
```  

Result: 
![not blocked](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/botasurussuccesspage.png)

NOTE: To run the code above, you will need Node.js installed.


## Usage with Botasaurus 

```python
from botasaurus import *

@browser(proxy="http://username:password@proxy-provider-domain:port") # TODO: Replace with your own proxy 
def visit_ipinfo(driver: AntiDetectDriver, data):
    driver.get("https://ipinfo.io/")
    driver.prompt()
visit_ipinfo()    
```  

## Usage with Selenium 

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_autoinstaller import install
from botasaurus_proxy_authentication import add_proxy_options

# Define the proxy settings
proxy = 'http://username:password@proxy-provider-domain:port'  # TODO: Replace with your own proxy

# Set Chrome options
chrome_options = Options()
add_proxy_options(chrome_options, proxy)

# Install and set up the driver
driver_path = install()
driver = webdriver.Chrome(driver_path, options=chrome_options)

# Navigate to the desired URL
driver.get("https://ipinfo.io/")

# Prompt for user input
input("Press Enter to exit...")

# Clean up
driver.quit()
```  

## Botasaurus

We encourage you to learn about [Botasaurus](https://github.com/omkarcloud/botasaurus). The All-in-One Web Scraping Framework with Anti-Detection, Parallelization, Asynchronous, and Caching Superpowers.

## Thanks

- Kudos to the Apify Team for creating `proxy-chain` library. The implementation of SSL-based Proxy Authentication wouldn't be possible without their groundbreaking work on `proxy-chain`.

## Love It? [Star It! ⭐](https://github.com/omkarcloud/botasaurus)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/botasaurus](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=botasaurus)](https://github.com/omkarcloud/botasaurus/stargazers)

## Made with ❤️ in Bharat 🇮🇳 - Vande Mataram
