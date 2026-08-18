#defining a function called as "net_price", which include parameters such as list_price, discount and tax
def net_price (list_price, discount, tax):
  #it will return the output by using mathemtical formula which is defined by user
    return list_price * (1- discount) * (1 + tax)
#numbers have been defined where: list_price=500, discount=0, tax=0.5
print(net_price(500, 0, 0.5))
