# Cryptocurrency Liquidity Analysis

This repository analyzes how many digital tokens are currently in circulation on exchanges. The volume calculation is done based on orderbook depth.

## Usage
```
pip3 install -r requirements.txt
python3 main.py btc
```

## Results

Examples are provided in `btc.txt` and `eth.txt` (March, 2021). If you are only looking to track the BTCUSD pair I highly recommend [CryptoQuant](https://cryptoquant.com/). Approximations below are from May, 2018. The liquidity tracking script offers great support and is based on [ccxt](https://github.com/ccxt/ccxt). Note that cryptocurrency exchanges are known for reporting incorrect volume and orderbook data. Reputation of exchanges should be taken into account when looking at orderbook data. HitBTC and BitHumb were excluded from further calculations. 

BTC liquidity has dropped approximately 80% on exchanges in the past two years (March, 2021). ETH liquidity increased by 12.5% during the same time.

### Digital Tokens on Exchanges (Limit Order Volume)
```
2715099 XMR (0.17%)
1353106 ETH (1.36%)
71350 BTC (0.42%)
751496.79 ZEC (0.18%)
```

### Largest Exchange (Volume)
```
5024.63 BTC (Bitfinex)
766905.37 XMR (Bitfinex)
216592.87 ETH (Bitfinex)
171579.10 ZEC (Bitfinex)
```

### Cold Storage (Volume)

#### Bitcoin
```
COLDSTORAGE / LIMITORDERVOLUME
=================================
189799 / 5024.63 = 37.77 (Bitfinex)
152779 / 8580.46 = 17.81 (Binance)
117203 / 3044.34 = 38.50 (Bittrex)
98041 / 2822.21 = 33.55 (Huobi)
=================================
AVERAGE ([COLDSTORAGE / LIMITORDERVOLUME] + 1) => 32.94
```

#### Ethereum
```
COLDSTORAGE / LIMITORDERVOLUME
=================================
801159 / 98812.68 = 8.11 (Kraken)
650491 / 12433.35 = 52.32 (Bittrex)
=================================
AVERAGE ([COLDSTORAGE / LIMITORDERVOLUME] + 1) => 31.22
```

#### Total Supply on Exchanges
```
32 x LIMITORDERVOLUME
=================================
43.52% ETH
13.44% BTC
5.44% XMR
5.76% ZEC
```

#### Lost Funds
```
5% ETH
16% BTC
```
