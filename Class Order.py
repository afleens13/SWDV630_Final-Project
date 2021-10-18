from abc import ABCMeta, abstractmethod
from sqlalchemy.sql.functions import user

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import INT
from MenuItemFactory import MenuItemFactory
from sqlalchemy import Column, Integer, String, PickleType, ForeignKey

from base import Base

class OrderTicket(Base):
    def __init__(self, items, storeCode, userId ):
        self.orderNumber = None
        self.items = items
        self.storeCode = storeCode
        self.userId = userId
        self.orderTotal = self.Total()
        self.availableRewards = self.CalculateRewards()

    def Total(self):
        orderTotal = 0
        for item in self.items:
            orderTotal = orderTotal + item.price
        return orderTotal

    def CalculateRewards(self):
        if self.orderTotal > 0:
            return 10
    
    def __repr__(self):
        itemString = ''
        for i in self.items:
            itemString = itemString + "\n{0}".format(i)
        return "\nOrder Number: {0} \nStoreCode: {1} \n{2} \nTotal: ${3:3,.2f} \n\nRewards: {4}".format(self.orderNumber, self.storeCode, itemString, self.orderTotal, self.availableRewards)

    __tablename__ = 'OrderTicket'

    orderNumber = Column(Integer, primary_key=True)
    storeCode = Column(String, ForeignKey('StoreLocation.storeCode'))
    userId = Column(Integer, ForeignKey('UserProfile.userId'))
    orderItems = Column(PickleType)
    total = Column(Integer)
    rewards = Column(Integer)