import pyqrcode
from pyqrcode import QRCode
a='hii sarang'
url=pyqrcode.create(a)
url.svg("a.svg",scale=8)
