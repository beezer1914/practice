weight = 8.4

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 or weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 or weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print(cost_ground)