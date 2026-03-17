name=str(input("Enter driver name: "))
dist=float(input("Enter distance (km): "))
cons=float(input("Enter fuel consumption (L/100km): "))
price=float(input("Enter fuel price (KZT/L): "))
lit_need=dist*cons/100
fuel_cost=lit_need*price
cost_per_km=fuel_cost/dist

print("==============================")
print("ROAD TRIP SUMMARY".center(30))
print("==============================")
print(f"Driver: {name}")
print(f"Distance: {dist} km")
print(f"Fuel Consumption: {cons} L/100km")
print(f"Fuel Price: {price} KZT/L")
print("------------------------------")
print(f"Litres Needed: {lit_need:.1f} L")
print(f"Total Fuel Cost: {fuel_cost:.1f} KZT")
print(f"Cost Per Km: {cost_per_km:.1f} KZT/km")
print("==============================")
if(dist>500):
    print("Distance is too long and more than 500 km")
else:
    print("Distance is acceptable and less than 500 km")
if(cost_per_km>10):
    print("Cost per km is too high and more than 10 KZT/km")
else:
    print("Cost per km is acceptable and less than 10 KZT/km")