# Python 3
# pip3 install pyJwt
import jwt 
import uuid
import hashlib
import time
from urllib.parse import urlencode
import requests
import json

accessKey = input("빗썸 API Key를 입력하세요: ").strip()
secretKey = input("밧썸 Secret Key를 입력하세요: ").strip()
apiUrl = 'https://api.bithumb.com'
tradeToken = f"KRW-{input('거래할 토큰 티커를 입력하세요 (예: BTC, ETH, XRP): ').strip().upper()}"
TradeVolumeKoreanWon = max(int(float(input(f"매수에 사용할 원화 금액을 입력하세요 (단위 KRW, 최소 {6000}): ").strip().replace(',',''))), 6000)
tradeTokenAmount = 0
tradeTokenPrice = 0


# --- 현재가 조회 함수 (Public API) ---
def get_current_price(market_token):
    # Public API는 "order_currency/payment_currency" 형식 (예: SOPH_KRW)을 사용합니다.
    try:
        order_currency = market_token.split('-')[1]
        url = f"https://api.bithumb.com/public/ticker/{order_currency}_KRW"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data.get('status') == '0000':
            return float(data['data']['closing_price'])
        else:
            raise Exception(f"현재가 조회 실패: {data.get('message', '알 수 없는 오류')}")
    except Exception as e:
        raise Exception(f"API 호출 중 오류 발생: {e}")

# --- 주문 실행 함수 (JWT 생성 및 API 호출) ---
def execute_order(requestBody, accessKey, secretKey, apiUrl, order_type):
    """주문 정보를 받아 JWT를 생성하고 Bithumb API를 호출합니다."""
    
    # Generate access token
    query = urlencode(requestBody).encode()
    hash = hashlib.sha512()
    hash.update(query)
    query_hash = hash.hexdigest()
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000), 
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }   
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
      'Authorization': authorization_token,
      'Content-Type': 'application/json'
    }

    print(f"\n--- {order_type} 주문 API 호출 ---")
    try:
        response = requests.post(apiUrl + '/v1/orders', data=json.dumps(requestBody), headers=headers)
        print(f"HTTP 상태 코드: {response.status_code}")
        print(f"응답 JSON: {response.json()}")
    except Exception as err:
        print(f"API 호출 중 오류 발생: {err}")


#1. tradeToken의 현재 가격을 tradeTokenPrice에 넣는다. 2. TradeVolumeKoreanWon을 tradeToken의 현재 가격으로 나누어 tradeTokenAmount를 구한다 2. tradeToken, tradeTokenPrice, tradeTokenAmount, TradeVolumeKoreanWon을 출력한다.
tradeTokenPrice = get_current_price(tradeToken); 
tradeTokenAmount = TradeVolumeKoreanWon / tradeTokenPrice; 
print(f'\n--- 거래 정보 계산 결과 ---\n마켓: {tradeToken}\n현재가: {tradeTokenPrice:,.2f} KRW\n매수 원화 금액: {TradeVolumeKoreanWon:,} KRW\n계산된 수량: {tradeTokenAmount:.8f} {tradeToken.split("-")[1]}\n-------------------------')


# ----------------------------------------------------
# 1차: 지정가 매수 주문 (Buy Order) 실행
# ----------------------------------------------------
requestBody = dict( 
    market=tradeToken, 
    side='bid', 
    volume=round(tradeTokenAmount, 4), 
    price=round(tradeTokenPrice * 1.1, 2), # 현재가보다 10% 높은 가격으로 매수 지정
    ord_type='limit' 
)
execute_order(requestBody, accessKey, secretKey, apiUrl, "매수(BUY)")


# ----------------------------------------------------
# 2차: 지정가 매도 주문 (Sell Order) 실행
# ----------------------------------------------------
# 10초 대기 후 매도 주문 진행
time.sleep(2)

requestBody = dict( 
    market=tradeToken, 
    side='ask', 
    volume=round(tradeTokenAmount, 4), 
    price=round(tradeTokenPrice * 0.9, 2), # 현재가보다 10% 낮은 가격으로 매도 지정
    ord_type='limit' 
) 
execute_order(requestBody, accessKey, secretKey, apiUrl, "매도(SELL)")