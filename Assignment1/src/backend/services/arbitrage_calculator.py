def calculate_arbitrage(solana_price, base_price, fees):
    price_diff = solana_price - base_price
    total_fees = solana_price * fees['dex_fee'] + base_price * fees['dex_fee'] + fees['network_fee']
    net_profit = price_diff - total_fees
    
    if net_profit > 0:
        return {
            "net_profit": round(net_profit, 6),
            "solana_price": round(solana_price, 6),
            "base_price": round(base_price, 6),
        }
    else:
        return None