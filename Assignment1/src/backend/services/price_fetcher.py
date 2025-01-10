import requests
import time

def fetch_token_price(token_id, max_retries=3, initial_delay=1):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {  
        'ids': token_id,
        'vs_currencies': 'usd'
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data[token_id]['usd'] if token_id in data else None
            elif response.status_code == 429:
                delay = initial_delay * (2 ** attempt)
                print(f"Rate limit exceeded for {token_id}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Unexpected status code {response.status_code} for {token_id}")
                return None
        except requests.RequestException as e:
            print(f"Request failed for {token_id}: {e}")
            return None
    
    print(f"Max retries reached for {token_id}")
    return None