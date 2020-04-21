import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)

print(avg)


print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))


# Remove missing data

cities = ["", "Berlin", "", "Cairo", "", "Buenos Aires",
          "Los Angeles", "Tokyo", "", "New York", "", ""
          "London", "Beijing", ""
          ]

print(list(filter(None, cities)))
