def LinearSearchProduct(productlist, target Product):
indices = []

for index,product in enumerate(productList):
  if product == targetProduct:
    indices.append(index)

return indices


#Example usage:
product = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = LinearSearchProduct(product, target)
print(result)