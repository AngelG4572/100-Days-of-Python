import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
# celsius = int(monday.temp)
# fahrenheit = (celsius * (9/5)) + 32
# print(fahrenheit)
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

'''
Figure out total number of Gray, Cinnamon, and Black Squirrels.
Use that info to create a new DataFrame.
Export the DataFrame into a final csv.
'''

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
print(squirrel_dict)
pandas.DataFrame(squirrel_dict).to_csv("squirrel_count.csv")
