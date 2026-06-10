#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, dis):
    if type(dis) == int and 0 <= dis <= 100:
      self._discount = dis
    else:
      print("Not valid discount")
    
  def  add_item(self, item, price, quantity):
    self.items.append(item)
    self.total += (price * quantity)
    self.previous_transactions.append({
      "item" : item,
      "price" : price,
      "quantity" : quantity
    })

  def apply_discount(self):
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return
    self.total = ((self.discount/100) * self.total)
    last = self.previous_transactions.pop()
    self.items.remove(last["item"])

  def  void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return
    last = self.previous_transactions.pop()
    self.total -= (last["price"] * last["quantity"])
    self.items.remove(last["item"])