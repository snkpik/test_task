import random
import xml.etree.ElementTree as ET
from urllib.request import urlopen

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

import haberdasher_twirp, haberdasher_pb2

class HaberdasherService(object):
    def MakeHatTest(self, context, size):
        if size.inches <= 0:
            raise InvalidArgument(argument="inches", error="I can't make a hat that small!")
        return haberdasher_pb2.Hat(
            size=size.inches,
            color= random.choice(["white", "black", "brown", "red", "blue"]),
            name=random.choice(["bowler", "baseball cap", "top hat", "derby"])
        )
    def GetDollarRate(self, context, empty):
        return haberdasher_pb2.DollarRate(
            rate= self.getDollar(),
        )
    def getDollar(self):
        with urlopen('http://www.cbr.ru/scripts/XML_daily.asp') as f:
            tree = ET.parse(f)
            dollar = float((tree.findall('./Valute[@ID="R01235"]/Value')[0].text).replace(',','.'))
            return dollar



# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `HaberdasherServer` class.
service = haberdasher_twirp.HaberdasherServer(service=HaberdasherService())
app = TwirpASGIApp()
app.add_service(service)