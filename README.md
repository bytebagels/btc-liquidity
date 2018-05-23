# Analyzing Cryptocurrency Liquidity

This repo analyzes how many digital tokens are currently in circulation on exchanges. The volume calculation is done based on the orderbooks.

## Requirements
```
python 3.6
===> pip install ccxt
```

## Results

### Digital Tokens on Exchanges (Limit Order Volume)
```
2715099 XMR (0.17%)
1353106 ETH (1.36%)
71350 BTC (0.42%)
751496.79 ZEC (0.18%)
```

### Largest Exchanges (Volume)
```
15307.36 BTC (HitBtc)
917055.28 XMR (HitBtc)
182167.48 ETH (HitBtc)
136188.43 ZEC (HitBtc)

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
