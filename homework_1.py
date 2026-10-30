##1. Number of travelers. 2. Number of nights. 3. Accommodation cost per night **for the whole group**. 4. Transport cost **for the whole trip and whole group**, entered once. 5. Food budget **per person per day**.

number_of_travelers = int (input ("Number of travelers"))
number_of_nights = int(input("Number of nights"))
accommodation_cost_per_night = int(input("Accommodation cost per night")) #all

transport_cost =  15000 *  number_of_travelers
food_budget =   5000 * number_of_travelers
number_of_trip_days = number_of_nights + 1



cost_per_person = accommodation_cost_per_night * number_of_nights + number_of_trip_days *  food_budget + transport_cost
total_trip_cost =  cost_per_person * number_of_travelers
total_accommodation_cost = accommodation_cost_per_night * number_of_nights

print("Transport cost is", transport_cost, "AMD")
print("Food budget is",food_budget,"AMD")
print("Number of trip days is", number_of_trip_days)
print("Cost per person is", cost_per_person,"AMD")
print("Total trip cost is",total_trip_cost, ("AMD"))
print("Total_accommodation_cost", total_accommodation_cost, "AMD")

