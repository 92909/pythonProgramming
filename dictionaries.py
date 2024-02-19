months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr":"April",
    "May": "May",
    "June": "June",
    7: "July",
    8: "August"
} 

'''print(months["Feb"])
print(months["Jan"])
print(months["Mar"])'''
print(months.get("Lub", "not a valid key"))
print(months.get("Jan"))
print(months.get(7))
print(months[8])