import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6Iks0NDVQamxiRnhZemNPWHJLanBaWnc9PSIsInZhbHVlIjoiazYySCs0ZmtOQ2x5cXZXSFkyVFlIcHk4OW5YeFhjelh2WCtjdDNva0V5akdYVFNuZHlRMzNFbUFXOTJVMko2aiIsIm1hYyI6Ijk2NGU2YzA5Y2VjOGVlMzVkYWZmZGVlZTY2ZmNkZjhkMzFmNGM0NDcwYjRhNWM5MjdlYzQxYjI3MzEzOGM0ZTYifQ%3D%3D',
    'exploit_database_session': 'eyJpdiI6IlJwcUtwZmFHbUgxTkFmWXJBUmJXcXc9PSIsInZhbHVlIjoiQlhmQUR3ZGFIaVVBbTVWM3Z1cDhPM0ZvXC9VUWdoeDZHN2Z4dWJtaE03d2RqeFBLXC9HTlJpODBTNStpZ1JzMjZsIiwibWFjIjoiMjRlOGNiY2IyYzMxMWE3ZGNkNDAyMmJkYmRiMTAwNjA4ODFjZjE3OTk2NGJlN2YxMDkwNWM2NGFjMjUwOWY4YSJ9',
    'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1671179118467%2Cregion:%27TR%27}',
    '_ga': 'GA1.3.1886958225.1671179120',
    '_gid': 'GA1.3.1905509648.1671179120',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.exploit-db.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6Iks0NDVQamxiRnhZemNPWHJLanBaWnc9PSIsInZhbHVlIjoiazYySCs0ZmtOQ2x5cXZXSFkyVFlIcHk4OW5YeFhjelh2WCtjdDNva0V5akdYVFNuZHlRMzNFbUFXOTJVMko2aiIsIm1hYyI6Ijk2NGU2YzA5Y2VjOGVlMzVkYWZmZGVlZTY2ZmNkZjhkMzFmNGM0NDcwYjRhNWM5MjdlYzQxYjI3MzEzOGM0ZTYifQ%3D%3D; exploit_database_session=eyJpdiI6IlJwcUtwZmFHbUgxTkFmWXJBUmJXcXc9PSIsInZhbHVlIjoiQlhmQUR3ZGFIaVVBbTVWM3Z1cDhPM0ZvXC9VUWdoeDZHN2Z4dWJtaE03d2RqeFBLXC9HTlJpODBTNStpZ1JzMjZsIiwibWFjIjoiMjRlOGNiY2IyYzMxMWE3ZGNkNDAyMmJkYmRiMTAwNjA4ODFjZjE3OTk2NGJlN2YxMDkwNWM2NGFjMjUwOWY4YSJ9; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1671179118467%2Cregion:%27TR%27}; _ga=GA1.3.1886958225.1671179120; _gid=GA1.3.1905509648.1671179120; _gat=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'draw': '1',
    'columns[0][data]': 'date_published',
    'columns[0][name]': 'date_published',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'download',
    'columns[1][name]': 'download',
    'columns[1][searchable]': 'false',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'application_md5',
    'columns[2][name]': 'application_md5',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'verified',
    'columns[3][name]': 'verified',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'description',
    'columns[4][name]': 'description',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'false',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'type_id',
    'columns[5][name]': 'type_id',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'false',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'platform_id',
    'columns[6][name]': 'platform_id',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'columns[7][data]': 'author_id',
    'columns[7][name]': 'author_id',
    'columns[7][searchable]': 'false',
    'columns[7][orderable]': 'false',
    'columns[7][search][value]': '',
    'columns[7][search][regex]': 'false',
    'columns[8][data]': 'code',
    'columns[8][name]': 'code.code',
    'columns[8][searchable]': 'true',
    'columns[8][orderable]': 'true',
    'columns[8][search][value]': '',
    'columns[8][search][regex]': 'false',
    'columns[9][data]': 'id',
    'columns[9][name]': 'id',
    'columns[9][searchable]': 'false',
    'columns[9][orderable]': 'true',
    'columns[9][search][value]': '',
    'columns[9][search][regex]': 'false',
    'order[0][column]': '9',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '15',
    'search[value]': '',
    'search[regex]': 'false',
    'author': '',
    'port': '',
    'type': '',
    'tag': '',
    'platform': '',
    '_': '1671179337300',
}

response = requests.get('https://www.exploit-db.com/', params=params, cookies=cookies, headers=headers)
#print(response.text)
jsonData = response.json()

exploits = jsonData['data']

for exploit in exploits:
	id = exploit['id']
	title = exploit['description'][1]
	type = exploit['type']['display']
	platform = exploit['platform']['platform']
	author = exploit['author']['name']
	link = "https://www.exploit-db.com"+exploit['download'].split("\"")[1]
	print(id,title,type,platform,author,link)