import requests

url = "https://alpha-api-partner-bill.payco.com/pgTradeCheck/download/pay"
params = {
    "serviceCode": "PAY_D",
    "mrcCode": "S0FSJE",
    "ymd": "20240505",
    "token": "M1LSIT-MRC-C3FF5F8E-OEBE-4BD7",
    "version": "1.1"
}
headers = {
    "Host": "dev-apis.krp.toastoven.net",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"
}

response = requests.get(url, params=params, headers=headers)

# 응답 확인
if response.status_code == 200:
    print("Response received successfully.")
    print(response.content)  # 파일 내용 출력T
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
