car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

# # color_car =[]
# # year_car = []
# # engine_volume = []
# # car_type = []
# list_of_price = []
# max_price = 0
# counter = 0

# for k in car_data:
#   color_car += [car_data[k][0]]
# # print(color_car)
#
# for k in car_data:
#   year_car += [car_data[k][1]]
# # print(year_car)
#
# for k in car_data:
#   engine_volume += [car_data[k][2]]
# # print(engine_volume)
#
# for k in car_data:
#   car_type += [car_data[k][3]]
# # print(car_type)

# for k in car_data:
#     list_of_price += [car_data[k][4]]  # create list with all price
#
# list_of_price.sort()  # sort list with all price
# max_price_first_5_cars = list_of_price[0:5]  # create variable with first 5 lower price
#
# for k in max_price_first_5_cars:  # find max price in list with first 5 lower price
#     if max_price <= k:
#         max_price = k
#
# for k in car_data:  # find in dict 5 lower price in a cars
#     if car_data[k][-1] <= max_price:
#         print(k, car_data[k][1], car_data[k][2], car_data[k][-1])
#         counter += 1
#     if counter == 5:
#         break


# min_price = max_price
# for k in list_of_price: ----- find min price
#   if k <= min_price:
#     min_price = k
# print(min_price)

# for k in car_data:
#     if 2017 <= car_data[k][1]:
#         if 1.6 <= car_data[k][2]:
#             if 36000 >= car_data[k][-1]:


sorted_car_dict_by_criteria = {}
prices = []
counter = 0
for k, v in car_data.items():
    if 2017 <= car_data[k][1] and 1.6 <= car_data[k][2] and 36000 >= car_data[k][-1]:
        sorted_car_dict_by_criteria.update({k:v})
# print(sorted_car_dict_by_criteria)
sorted_by_price = dict(sorted(sorted_car_dict_by_criteria.items(), key=lambda price: price[1][-1]))

print(sorted_by_price)

for k, v in sorted_by_price.items():
    print(k,v)
    counter += 1
    if counter == 5:
        break
# for k in sorted_by_price:
#     print()
#     counter += 1
#     if counter == 5:
#         break



# list_sorted_car_dict_by_criteria = list(sorted_car_dict_by_criteria.items())
# print(list_sorted_car_dict_by_criteria)
# print(sorted(list_sorted_car_dict_by_criteria))

# for k in car_data:
#     if 2017 <= car_data[k][1]:
#         if 1.6 <= car_data[k][2]:
#             if 36000 >= car_data[k][-1]:
#                 with_price.append(car_data[k][-1])

