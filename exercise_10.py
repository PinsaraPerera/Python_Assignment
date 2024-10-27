import os

class WeatherData:
    def __init__(self):
        self.weekly_temperatures = ()

        try:
            if os.listdir("weather_data.csv"):
                with open("weather_data.csv", "r") as file:
                    for line in file:
                        self.weekly_temperatures += (float(line),)
        except:
            pass

    def add_temperature(self, temperature):
        self.weekly_temperatures += (temperature,)
        # store data in a file
        with open("weather_data.csv", "a") as file:
            file.write(str(temperature) + "\n")

    def get_average_temperature(self):
        return sum(self.weekly_temperatures) / len(self.weekly_temperatures)
    
    def get_max_temperature(self):
        max = float('-inf')

        for temperature in self.weekly_temperatures:
            if temperature > max:
                max = temperature
        
        return max
    
    def get_min_temperature(self):
        min = float('inf')

        for temperature in self.weekly_temperatures:
            if temperature < min:
                min = temperature
        
        return min
    
    def print_weekly_temperatures(self):
        DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print()
        for day, temperature in zip(DAYS, self.weekly_temperatures):
            print(day, ":", temperature)

# add temperatures to the file
weather_data = WeatherData()

weather_data.add_temperature(20.8)
weather_data.add_temperature(25.3)
weather_data.add_temperature(30.0)
weather_data.add_temperature(35.7)
weather_data.add_temperature(40.2)
weather_data.add_temperature(45.6)
weather_data.add_temperature(50.9)

print("\nAverage temperature:", weather_data.get_average_temperature())
print("\nMax temperature:", weather_data.get_max_temperature())
print("\nMin temperature:", weather_data.get_min_temperature())

weather_data.print_weekly_temperatures()

    