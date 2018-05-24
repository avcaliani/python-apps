# Model Reference: https://coinmarketcap.com/api/
class Coin:

    def __init__(self, json):
        self.id = json ['id']
        self.name = json ['name']
        self.symbol = json ['symbol']
        self.rank = json ['rank']
        self.priceUsd = json ['price_usd']
        self.priceBtc = json ['price_btc']
        self.volumeUsd24h = json ['24h_volume_usd']
        self.marketCapUsd = json ['market_cap_usd']
        self.availableSupply = json ['available_supply']
        self.totalSupply = json ['total_supply']
        self.percentChange1h = json ['percent_change_1h']
        self.percentChange24h = json ['percent_change_24h']
        self.percentChange7d = json ['percent_change_7d']
        self.lastUpdated = json ['last_updated']

    def toString(self):
        ret = """
Id........................: %s
Name......................: %s
Symbol....................: %s
Rank......................: %s
Price USD.................: %s
Price BTC.................: %s
24h Volume USD............: %s
Market Cap USD............: %s
Available Supply..........: %s
Total Supply..............: %s
Percent Changed in 1h.....: %s
Percent Changed in 24h....: %s
Percent Changed in 7 Days.: %s
Last Updated..............: %s
            """ % (
                self.id, self.name, self.symbol, self.rank,
                self.priceUsd, self.priceBtc, self.volumeUsd24h,
                self.marketCapUsd, self.availableSupply, self.totalSupply,
                self.percentChange1h, self.percentChange24h, self.percentChange7d,
                self.lastUpdated
            )
        return ret
