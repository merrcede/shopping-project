from typing import NewType, Dict, List, Optional

from shop.models import product

GenderID = NewType('GenderID', int)
CategoryID = NewType('CategoryID', int)
BrandID = NewType('BrandID', int)
SizeID = NewType('SizeID', int)
ProductID = NewType('ProductID', int)

Product = Dict[str, Optional[ProductID or List[GenderID]
                             or List[CategoryID] or List[BrandID]
                             or List[SizeID] or str or int]
]
Basket = NewType('Basket', list[Product])
