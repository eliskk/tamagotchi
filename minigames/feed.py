'''
Game where you choose click items in a sequence

the success rate how much hunger fixes

EXAMPLE:

80% correct click rate over 1 time => if hunger = 1 then hunger becomes 20% 
(4/5)
'''

# Add errors

import random

def generate_order():
  
  order_num = []
  order_food = []
  
  for i in range(5):
    order_num.append(random.randint(0,4))
  
  for food in order_num:
    
    match food:
      case 0:
        order_food.append("fries")
      case 1:
        order_food.append("apple")
      case 2:
        order_food.append("rice")
      case 3:
        order_food.append("chicken")
      case 4:
        order_food.append("pizza")
  
  return order_food
  
print(generate_order())