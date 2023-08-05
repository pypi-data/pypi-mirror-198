# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         23/02/23 10:18
# Project:      CFHL Transactional Backend
# Module Name:  __init__.py
# Description:
# ****************************************************************
from .coffee_ware_house import CoffeeWareHouseListSerializer
from .offer import OfferListSerializer

__all__ = [
    "CoffeeWareHouseListSerializer",
    "OfferListSerializer"
]