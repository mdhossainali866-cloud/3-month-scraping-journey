import requests
import csv 
import sys 
from datetime import datetime
import os 
sys.stdout.reconfigure(encoding='utf-8')
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd,bdt"
print("📡 Connecting to Crypto API...\n")
response= requests.get(url)
if response.status_code == 200 : 
    data= response.json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    btc_usd = data['bitcoin']['usd']
    btc_bdt=data['bitcoin']['bdt']
    
    eth_usd= data['ethereum']['usd']
    eth_bdt=data['ethereum']['bdt']
    
    sol_usd = data['solana']['usd']
    sol_bdt = data['solana']['bdt']
    print("==========================================")
    print("      🚀 REAL-TIME CRYPTO DASHBOARD      ")
    print(f"      🕒 Time: {now}")
    print("==========================================\n")
    
    print(f"🪙 Bitcoin (BTC)  : ${btc_usd:,.2f} | ৳{btc_bdt:,.2f}")
    print(f"💎 Ethereum (ETH) : ${eth_usd:,.2f} | ৳{eth_bdt:,.2f}")
    print(f"⚡ Solana (SOL)   : ${sol_usd:,.2f} | ৳{sol_bdt:,.2f}\n")
    print("==========================================")
    file_exists= os.path.isfile('crypto_history.csv')
    with open ('crypto_history.csv' , 'a' , newline = '',encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp","BTC_USD","BTC_BDT","ETH_USD","ETH_BDT","SOL_USD","SOL_BDT"])
            
        writer.writerow([now, btc_usd, btc_bdt, eth_usd, eth_bdt, sol_usd, sol_bdt])
        
    print("\n✅ Live data successfully appended to 'crypto_history.csv'!")
else:
    print(
        f"❌ Failed to fetch data. Status Code: {response.status_code}"
    ) 
            
    