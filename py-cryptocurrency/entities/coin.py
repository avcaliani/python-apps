""""
Model Reference: https://coinmarketcap.com/api/
"""
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


class Coin:

    def __init__(self, json):
        self.id = json ['id']
        self.name = json ['name']
        self.symbol = json ['symbol']
        self.rank = json ['rank']
        self.price_usd = json ['price_usd']
        self.price_btc = json ['price_btc']
        self.volume_usd_24h = json ['24h_volume_usd']
        self.market_cap_usd = json ['market_cap_usd']
        self.available_supply = json ['available_supply']
        self.total_supply = json ['total_supply']
        self.percent_change_1h = json ['percent_change_1h']
        self.percent_change_24h = json ['percent_change_24h']
        self.percent_change_7d = json ['percent_change_7d']
        self.last_updated = json ['last_updated']

    def to_string(self):
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
                self.price_usd, self.price_btc, self.volume_usd_24h,
                self.market_cap_usd, self.available_supply, self.total_supply,
                self.percent_change_1h, self.percent_change_24h, self.percent_change_7d,
                self.last_updated
            )
        return ret
