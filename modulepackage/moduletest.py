import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(2)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(2)

from theater_module import *
price(3)
price_morning(4)
price_soldier(2)

from theater_module import price, price_morning
price(3)
price_morning(4)
# price_soldier(2) import가 안되면 사용 불가

from theater_module import price_soldier as ps
ps(2)