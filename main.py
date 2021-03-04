import ccxt
import helpers
import sys

total = 0.0
currency = sys.argv[1] if len(sys.argv) > 1 else "BTC"

# exchanges = ccxt.exchanges
exchanges = ['ftx', 'binance', 'bitfinex', 'bitflyer', 'bitkk', 'bitlish', 'bitmarket', 'bitmex', 'bitstamp', 'bittrex', 'bitz', 'bl3p', 'bleutrade', 'braziliex', 'btcbox', 'btcchina', 'btcexchange', 'btcmarkets', 'btctradeim', 'btctradeua', 'btcturk', 'btcx', 'ccex', 'cex', 'chbtc', 'ethfinex', 'exmo', 'exx', 'flowbtc', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'gateio', 'gdax', 'gemini', 'getbtc', 'hadax', 'huobi', 'huobicny', 'huobipro', 'ice3x', 'itbit', 'jubi', 'kraken', 'kucoin', 'kuna', 'lakebtc', 'lbank', 'liqui', 'livecoin', 'luno', 'lykke', 'mercado', 'mixcoins', 'negociecoins', 'nova', 'okcoincny', 'okcoinusd', 'okex', 'paymium', 'poloniex', 'qryptos', 'quadrigacx', 'quoinex', 'southxchange', 'surbitcoin', 'therock', 'tidebit', 'tidex', 'urdubit', 'vbtc', 'virwox', 'wex', 'xbtce', 'yobit', 'yunbi', 'zaif', 'zb']

print(f"CALCULATING LIQUIDITY FOR {currency}")
print("=====================================")

for exchange in exchanges:
    try:
        # Get volume for each exchange
        reference = eval("ccxt.{}()".format(exchange))
        markets = reference.load_markets()

        # Get tickers
        tickers = []
        for key, _ in markets.items():
            tickers.append(key)

        # Calculate volume
        volume = 0.0
        for ticker in tickers:
            if ticker[-4:] == "/{}".format(currency):
                try:
                    vol = helpers.get_volume(
                        reference.fetch_order_book(symbol=ticker, limit=1000)["bids"]
                    )
                    volume += vol
                    print("{} \t{:.2f} \t{:.2f}".format(ticker, vol, volume))
                except:
                    pass
            elif ticker[:4] == "{}/".format(currency):
                try:
                    vol = helpers.get_volume_(
                        reference.fetch_order_book(symbol=ticker, limit=1000)["asks"]
                    )
                    volume += vol
                    print("{} \t{:.2f} \t{:.2f}".format(ticker, vol, volume))
                except:
                    pass

        print("===> \t{} \t{:.2f}".format(exchange, volume))
        total += volume
    except:
        # Avoids missing api key error
        pass

print(">>>> {:.2f}".format(total))
