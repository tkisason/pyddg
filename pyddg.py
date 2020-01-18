#!/usr/bin/env python3

import requests, re

# yes, i didn't want to include lxml or beautifulsoup...
# and yes, this would all be unnesecary if we had a normal API...

def generateQueryParams(page=1):
    if page == 1:
        return f"s=0&dc=-29"
    elif page == 2:
        return f"s={30}&dc={29}"
    else:
        return f"s={30+(50*(page-2))}&dc={29+(47*(page-2))+1}"


def DDG(query, pages=1, kl="us-en"):
    urls = {}
    for page in range(1, pages + 1):
        url = (
            f"https://duckduckgo.com/lite/?q={query}&kl={kl}&api=%2Fd.js&o=json&nextParams=&v=l&"
            + generateQueryParams(page)
        )
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://duckduckgo.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://duckduckgo.com",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
        }
        data = {"q": query, "kl": kl}
        for line in requests.get(url, headers=headers, data=data).content.split(b"\n"):
            if line.find(b"class='result-link'") >= 0:
                link = re.search(b'href="([^"]*)', line).group(1)
                desc = re.search(b">.*</a>", line).group(0)
                urls[link] = desc
    return urls
