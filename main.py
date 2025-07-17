import requests
import json

url = "https://app.loola.tv/api/authenticate-platform/configure"

payload = {
  "platformType": "tiktok",
  "username": "username/email",
  "password": "password"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36",
  'Content-Type': "application/json",
  'sec-ch-ua-full-version-list': "\"Not)A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"138.0.7204.63\", \"Google Chrome\";v=\"138.0.7204.63\"",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
  'sec-ch-ua-bitness': "\"\"",
  'sec-ch-ua-model': "\"Infinix X6531\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-arch': "\"\"",
  'sec-ch-ua-full-version': "\"138.0.7204.63\"",
  'sec-ch-ua-platform-version': "\"14.0.0\"",
  'origin': "https://app.loola.tv",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://app.loola.tv/main-video-room",
  'accept-language': "en-US,en;q=0.9,la;q=0.8",
  'priority': "u=1, i",
  'Cookie': "cf_clearance=8VqXhInCQWyw6Hr4axFxd9aWJlQuSwANGQXrcCzAm94-1752770552-1.2.1.1-6q7g8KB7SX4PbAwQE8BHhUXnY0eqHsZ0124g3xbDzhr_jkBcZQZECeH9yB_44f7NuR7NMTJIot9Kc.eqgmoKQR2Cgz5OaRrLj4qnwOreuRZVahEFsbBsFa8yhG6uNTTZU1VBKxA4ijTPlhoETa3IHEHzGv_3nlVBrJAvLX0ZZby8zIICFF6e.PDO.0700pYGdPShjU6K78Wx0cjwqfSUUrhKaYgr1QRfJICxd5jxGFo; connect.loolasid=eyJ0b2tlbnMiOnsiYWNjZXNzX3Rva2VuIjoieWEyOS5hMEFTM0g2Tnd0UWZ6Y3lKTkluSmNUcnBhT21KSGl6MmNPQ000MDl4SVQ4ekg5Q3JXNnZld0plX1RyellDem0yZmhrUUZrdWtMM251ZWxnRUN6V3hkNk9KUjRxZTY1RGh5clBJRVU0UU1tdTZVbUxkbHM3M251VzRmRzJFN0UteGZZSEJYdGtMSk1reDREenBEUVhfQjM5NTJBWkNaek1tOG9RSXRJRjEwS2FDZ1lLQWE0U0FSQVNGUUhHWDJNaVk4Y1FWc01qMHlhTXpVY3Q5UnlITGcwMTc1IiwicmVmcmVzaF90b2tlbiI6IjEvLzA1MVhZMEo2cDlBRmhDZ1lJQVJBQUdBVVNOZ0YtTDlJcmNDcG9hdTM4Yi1BeGRWSmFBQkJYbERZNnJjWWxOQV9yYmRkNkZwcDl6RTB3NWFUV3lfUHFfejc5Tm9sUHBBNXNEUSIsInNjb3BlIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC91c2VyaW5mby5wcm9maWxlIG9wZW5pZCBodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9hdXRoL3lvdXR1YmUgaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC91c2VyaW5mby5lbWFpbCIsInRva2VuX3R5cGUiOiJCZWFyZXIiLCJpZF90b2tlbiI6ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJbVl4TURNek9EWXdOekUyWlROaE1tRmhZak00TUdZd01HUmlaVE01WVRjeE1UUTRORFppWVRFaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwyRmpZMjkxYm5SekxtZHZiMmRzWlM1amIyMGlMQ0poZW5BaU9pSTFPRFkyT1RJNE9UTTJNakF0Y21Nd2EyZDBhMjF5Y1cxdmRtZHBaVFpvT0c1MU5UbDFOSFZ6TURReVozUXVZWEJ3Y3k1bmIyOW5iR1YxYzJWeVkyOXVkR1Z1ZEM1amIyMGlMQ0poZFdRaU9pSTFPRFkyT1RJNE9UTTJNakF0Y21Nd2EyZDBhMjF5Y1cxdmRtZHBaVFpvT0c1MU5UbDFOSFZ6TURReVozUXVZWEJ3Y3k1bmIyOW5iR1YxYzJWeVkyOXVkR1Z1ZEM1amIyMGlMQ0p6ZFdJaU9pSXhNREF4TXprek1ERXlPRGM0TWpBNU9URTFOalVpTENKbGJXRnBiQ0k2SW5OcGVtRm5iMlI2UUdkdFlXbHNMbU52YlNJc0ltVnRZV2xzWDNabGNtbG1hV1ZrSWpwMGNuVmxMQ0poZEY5b1lYTm9Jam9pYzB4a0xXRlZVRFZ3VGtkMk5FNU9TSFEzV1V0UFp5SXNJbTVoYldVaU9pSnphWHBoSWl3aWNHbGpkSFZ5WlNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkRaemh2WTBwS2QyVk9RVEJKYXpsTmFFNXBXVFZLZWtab2RsUTBlak5zVTJkRldIZE9aMlZwWVRWdFVFMW1iVmxmY1VVOWN6azJMV01pTENKbmFYWmxibDl1WVcxbElqb2ljMmw2WVNJc0ltbGhkQ0k2TVRjMU1qYzNNRFk0T1N3aVpYaHdJam94TnpVeU56YzBNamc1ZlEubV9UM3Q2clkzRkhWdzYtblM4eXVfeVd6Y0RySFMzY0d2ZWhBTzktNF8xRE9naWJDS2tVSHhvMUp2VVFPLU1TOFdPd1NMY3hYWS15ZUVpLTBqTklrbG5zT1VHWEFHZkp0SVYweUd6bEFrbWtpelM4cGpvaXdXWHd4MmtrNWtlNG5ESy1obk91Z19yak5HcEpWbnFyTzNJOGdSTU8xaGpLUGZTb2dMZFIwS0xMQlJxdy1LVUotNnNRZnN6RWNiY0FBeUZ0RUtfdWhQWVRybHVhTElPLTBPZ3kwSVl3aTZKR3FvV2Fzb1N4ZTN4dUd6LWJmdFZDczJhaWEzQVU5bDlDZUh3U0xqRUJwN1F2Sm9GOXBMTlBBUm5sRkhTMkVKd0szQlpjbkNCeEdoRkF3N2tvR0FtM2xhOEZqZnl3N192d2tIbjdJQ2toZ0lncW5rSGVBdDBVVlZRIiwiZXhwaXJ5X2RhdGUiOjE3NTI3NzQyODg2MjQsImV4cGlyZXNfaW4iOjM2MDB9LCJjdXJyZW50VXNlckVtYWlsIjoic2l6YWdvZHpAZ21haWwuY29tIiwiY3VycmVudFJvb20iOnsiY3JlYXRlZERhdGUiOiIyMDI1LTA3LTE3VDE2OjUzOjQ1LjA0NFoiLCJsYXN0TW9kaWZpZWQiOiIyMDI1LTA3LTE3VDE2OjUzOjQ1LjA0NFoiLCJob3N0Q29kZSI6ODIyNTk4LCJyb29tSWQiOjM0MzYxNTIzMiwicm9vbSI6eyJyb29tIjozNDM2MTUyMzJ9LCJ1c2VyIjp7ImlkIjoic2l6YWdvZHpAZ21haWwuY29tIiwibmFtZSI6InNpemEifSwiaXNEZWxldGVkIjpmYWxzZSwiX2lkIjoiNjg3OTJhOTk0OTg1Mjg1NTE1MTI0YjY3In19; connect.loolasid.sig=Z_gMuD58iXUrq-y2KjRe7g_jAkw; ajs_anonymous_id=ab551f9f-5c1b-4314-bd38-7926018a0cad; _ga=GA1.1.200835769.1752771228; _ga_YJGWT5ES88=GS2.1.s1752771228$o1$g0$t1752771228$j60$l0$h0; _vwo_uuid_v2=D4D5D74CFF1A42BA98F9DC00864236D37|520c1cddd17ac9217050d33b835b3398"
}

response = requests.post(url, data=json.dumps(payload), headers=headers).json()
try:
 reason=response['rawServerError']['reason']
 print(reason)
except:
 print(response)
