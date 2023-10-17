def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = [
    "AUDI", "DODGE", "PORSCHE", "MASERATI", "MCLAREN", "ASTON-MARTIN",
    "MASERATI", "AUDI", "AUDI"
]
target = "AUDI"
result = linearSearchProduct(products, target)
print(result)