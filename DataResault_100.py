import requests
import pandas as pd
import numpy as np

url = 'https://airtable.com/v0.3/view/viwqbAQrO7YMOUflm/readSharedViewData?stringifiedObjectParams=%7B%22shouldUseNestedResponseFormat%22%3Atrue%7D&requestId=req3dJoefidMcxv8I&accessPolicy=%7B%22allowedActions%22%3A%5B%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwqbAQrO7YMOUflm%22%2C%22action%22%3A%22readSharedViewData%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwqbAQrO7YMOUflm%22%2C%22action%22%3A%22getMetadataForPrinting%22%7D%2C%7B%22modelClassName%22%3A%22view%22%2C%22modelIdSelector%22%3A%22viwqbAQrO7YMOUflm%22%2C%22action%22%3A%22readSignedAttachmentUrls%22%7D%2C%7B%22modelClassName%22%3A%22row%22%2C%22modelIdSelector%22%3A%22rows%20*%5BdisplayedInView%3DviwqbAQrO7YMOUflm%5D%22%2C%22action%22%3A%22createDocumentPreviewSession%22%7D%5D%2C%22shareId%22%3A%22shrWxNV1xJGDRW0pj%22%2C%22applicationId%22%3A%22appDBSdCKHNgr9mfc%22%2C%22generationNumber%22%3A0%2C%22expires%22%3A%222023-08-17T00%3A00%3A00.000Z%22%2C%22signature%22%3A%2249642f5f6e4d363a1a200aa986a7cdc3451b23942c38380a0411da52544f3e98%22%7D'
headers = {
    'authority': 'airtable.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
    'cookie': 'brw=brwjgJYdP2Onq4kbz; __Host-airtable-session=eyJzZXNzaW9uSWQiOiJzZXNVT0hFaUZZWk9MZ3lGUCIsImNzcmZTZWNyZXQiOiJUaDRNbmp6YXhjNlVMZUdlaFA3dmVfdk0ifQ==; __Host-airtable-session.sig=zGasdYZ514ISDpNUmVwZ3uHFcJ1CW9htmHJffjd-PjA; _gcl_au=1.1.1085323700.1690198386; _gid=GA1.2.871164957.1690198387; _mkto_trk=id:458-JHQ-131&token:_mch-airtable.com-1690198410859-45165; _uetsid=ea472d202a1511eeabaedf3bb1df3cb6; _uetvid=ea4777402a1511ee871807e6f46ca8b0; _ga=GA1.1.1942318434.1690198387; _ga_VJY8J9RFZM=GS1.1.1690198389.1.1.1690198523.0.0.0; _ga_H59XFK8PRM=GS1.1.1690198518.1.0.1690198523.0.0.0; AWSALB=OrlPwNA/vcaZeVdevtejMKHtIsS4REeoiDuAA5YHgV/FmV2LBw6FJdq/DPJOlh4uLPb0kekBk6v0ujoDgf0+nNgSFhRZlzh0Z22oOpUh29snCQ5w7VH5RI2fMvJ9; AWSALBCORS=OrlPwNA/vcaZeVdevtejMKHtIsS4REeoiDuAA5YHgV/FmV2LBw6FJdq/DPJOlh4uLPb0kekBk6v0ujoDgf0+nNgSFhRZlzh0Z22oOpUh29snCQ5w7VH5RI2fMvJ9; AWSALB=8SLp+Et3fe1CMrLqfs0/fArW1QhyFtI+hlpqE0N8FGcX4x3sbmzp0MhjAXzP0Ca/sBjcj35S0GSoJDyXhg5wA4MNkF6hqKqfYlH04xGoBx0JiVHiKeEoDIyK7zoG; AWSALBCORS=8SLp+Et3fe1CMrLqfs0/fArW1QhyFtI+hlpqE0N8FGcX4x3sbmzp0MhjAXzP0Ca/sBjcj35S0GSoJDyXhg5wA4MNkF6hqKqfYlH04xGoBx0JiVHiKeEoDIyK7zoG; brw=brwjgJYdP2Onq4kbz',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-airtable-accept-msgpack': 'true',
    'x-airtable-application-id': 'appDBSdCKHNgr9mfc',
    'x-airtable-inter-service-client': 'webClient',
    'x-airtable-page-load-id': 'pglZ9z0q88yKHkIY4',
    'x-early-prefetch': 'true',
    'x-requested-with': 'XMLHttpRequest',
    'x-time-zone': 'Asia/Tehran',
    'x-user-locale': 'en'
}
response = requests.get(url, headers=headers)

js = response.json()


#Extracting the names of all cities
city_map = {}
cities = js['data']['table']['columns'][4]['typeOptions']['choices']
for city in cities:
    city_map[city] = cities[city]['name']
#Extracting the names of all countries
country_map = {}
countries = js['data']['table']['columns'][5]['typeOptions']['choices']
for country in countries:
    country_map[country] = countries[country]['name']
#Extracting the names of all Role
role_map = {}
roles = js['data']['table']['columns'][3]['typeOptions']['choices']
for role in roles:
    role_map[role] = roles[role]['name']


rows = js['data']['table']['rows']
result = []

for row in rows:
    result.append(
        {
            'Full_name': row['cellValuesByColumnId']['fldko18Ysq8u01OWJ'] if row[
                'cellValuesByColumnId'].get('fldko18Ysq8u01OWJ', None) else None,
            'job_Title': row['cellValuesByColumnId']['fldWjv7ZeTWIfM1wv'] if row[
                'cellValuesByColumnId'].get('fldWjv7ZeTWIfM1wv', None) else None,
            'Employer': ''.join(
                map(lambda x: x['foreignRowDisplayName'] + ',', row['cellValuesByColumnId']['fld44dFbruGl44dy9']))[
                        :-1] if row[
                'cellValuesByColumnId'].get('fld44dFbruGl44dy9', None) else None,
            'Role': ''.join(map(lambda x: role_map[x] + ',', row['cellValuesByColumnId']['fldOV1shcDO4wndpY']))[:-1] if row[
                'cellValuesByColumnId'].get('fldOV1shcDO4wndpY', None) else None,
            'city': ''.join(map(lambda x: city_map[x] + ',', row['cellValuesByColumnId']['fldmMIku9y3LHpQBK']))[:-1] if
            row[
                'cellValuesByColumnId'].get('fldmMIku9y3LHpQBK', None) else None,
            'country': ''.join(map(lambda x: country_map[x] + ',', row['cellValuesByColumnId']['fldyDMa7vDcTyOauM']))[
                       :-1] if row[
                'cellValuesByColumnId'].get('fldyDMa7vDcTyOauM', None) else None,

            'Founding_partner': row['cellValuesByColumnId']['fldSkqfR1fwgllMAZ'] if row[
                'cellValuesByColumnId'].get('fldSkqfR1fwgllMAZ', None) else None,

            'LinkedIn': row['cellValuesByColumnId']['fldLRQdhIWoYCCxGX'] if row[
                'cellValuesByColumnId'].get('fldLRQdhIWoYCCxGX', None) else None,

        }
    )


# full_name = 'fldko18Ysq8u01OWJ'
# roll = 'fldOV1shcDO4wndpY'
# Employer = 'fld44dFbruGl44dy9'
# Linkdin = 'fldLRQdhIWoYCCxGX'
# city = 'fldmMIku9y3LHpQBK'
# country = 'fldyDMa7vDcTyOauM'
# job_Title = 'fldWjv7ZeTWIfM1wv'
# Founding_partner = 'fldSkqfR1fwgllMAZ'

DataFrame = pd.DataFrame(result)
DataFrame_100 = DataFrame.head(99)
DataFrame_100.to_excel('DataResault_100.xlsx', index=False)
