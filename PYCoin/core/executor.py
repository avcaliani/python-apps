import re
from entities.coin import Coin
from services.http_service import Http

class Executor:
    def __init__(self):
        self.http = Http()
        self.url = "https://api.coinmarketcap.com/v1/ticker/"
        self.coins = []

    def httpGet(self, url):
        print("Getting coins, please wait...")

        array = self.http.get(url)
        del self.coins[:]
        for coin in array:
            self.coins.append(Coin(coin))

        print("%d Coins Received!" % len(self.coins))

    def execute(self, cmd):
        # Show Command List
        if cmd == "help":
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Commands ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("$ get coins               # Get some coins (Default is 100 Coins)")
            print ("$ get coins -n $NUMBER    # Get $NUMBER coins, 0 to bring all.")
            print ("$ show coins              # Show All Coins")
            print ("$ show coins -s \"$SYMBOL\" # Show Coin that is represented by $SYMBOL")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return

        # Get Coins From Coin Market CAP API
        if cmd == "get coins":
            self.httpGet(self.url)
            return

        pattern = re.compile("get coins -n \d+")
        if pattern.match(cmd):
            try:
                limit = int(re.sub(r"[^\d]", "", cmd))
                self.httpGet(self.url + "?limit=%d" % limit)
            except:
                print("Please define a Integer number.")
            return

        # Show Captured Coins
        if cmd == "show coins":
            for coin in self.coins:
                print(coin.toString())
            return

        pattern = re.compile("show coins -s \"\\w+\"")
        if pattern.match(cmd):
            symbol = re.sub(r"([^A-Z])", "", cmd)
            if symbol == "":
                print("Please insert a valid value for Symbol.")

            for coin in self.coins:
                if coin.symbol == symbol:
                    print(coin.toString())
                    return
            print("Symbol '%s' not found!" % symbol)
            return

        print("Sorry, command '%s' not found!" % cmd)
