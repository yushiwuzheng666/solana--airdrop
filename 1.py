import requests
import json

# Solana RPC 端点
url = "https://api.mainnet-beta.solana.com"

# RPC 请求头
headers = {
    "Content-Type": "application/json"
}

# 构建请求数据
data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTokenAccountsByOwner",
    "params": [
        "<TOKEN_MINT_ADDRESS>", 
        {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
        {"encoding": "jsonParsed"}
    ]
}

# 发起请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 处理响应
if response.status_code == 200:
    token_accounts = response.json()
    with open('snapshot.json', 'w') as file:
        json.dump(token_accounts, file, indent=4)
else:
    print("Error:", response.status_code, response.text)
