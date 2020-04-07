fruits = ["peaches", "pears","apples"]
years = [3, "1998", 2.5, 987, "1994"]

print (fruits, years)


fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

fruits.pop(0)
print(fruits)