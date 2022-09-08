import requests
from bs4 import BeautifulSoup

profile = 'https://etherscan.io/address/0x4c2836a464df6ccadd4dfafede852272d669fc7f'

cookies = {
    'cf_chl_2': 'b99aaa68feb2b12',
    'cf_chl_prog': 'x14',
    'cf_clearance': 'MRbb73NfacVwEYI3Y5EViXAH54jzGKqHMH43fDKCGd4-1662622078-0-250',
    'ASP.NET_SessionId': 'fkjd4laid4krtezoh0hd0sfy',
    '__cflb': '02DiuFnsSsHWYH8WqVXaqGvd6BSBaXQLUe5W6qQbNmQ3e',
    '__cf_bm': 'HatzPZ9dJ4JwRsRIHi8P1SsF4WVvUjpmNn01UGjuxxM-1662622080-0-AbEid/q7KD5HVtffqIUsuUdr2qQHLu2Ea00VzknXb5K0V56BkUTjzzNTFDna6Az5NOXu49gRvg/LNgHwbR8J10q3KdrjGifw38NBwWV4CD4JFxHte3s9GpTHZO+RRizZxQ==',
    '_ga': 'GA1.2.840890564.1662622103',
    '_gid': 'GA1.2.150673053.1662622103',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    # 'trk': 'public_profile_browsemap',
    # 'original_referer': '',
}

response = requests.get(profile, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
