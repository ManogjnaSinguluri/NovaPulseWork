from flask import Blueprint, jsonify

from ..services.arbitrage_calculator import calculate_arbitrage
from ..services.price_fetcher import fetch_token_price
arbitrage_blueprint = Blueprint('arbitrage', __name__)

@arbitrage_blueprint.route('/arbitrage')
def get_arbitrage():
    try:
        solana_price = fetch_token_price("solana")
        base_price = fetch_token_price("base")
        
        if solana_price is None or base_price is None:
            raise ValueError("Failed to fetch price data")
        
        fees = {
            "dex_fee": 0.003,
            "network_fee": 0.00001,
        }
        
        arbitrage_opportunity = calculate_arbitrage(solana_price, base_price, fees)
        
        if arbitrage_opportunity:
            return jsonify(arbitrage_opportunity)
        else:
            return jsonify({"message": "No profitable arbitrage opportunities found"}), 200
    except Exception as e:
        # Error handling would be better in a separate utility
        return jsonify({"error": f"Bad Request: {str(e)}"}), 400