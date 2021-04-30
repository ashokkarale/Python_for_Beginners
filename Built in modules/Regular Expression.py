import re

if re.search(r"A..l", "Aopline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")
if re.search(r"A\d\dl", "A22line") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"A\d*", "Aline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"A\d+", "A2irline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"A\d?i", "Airline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"A\d{2}i", "A22irline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"A[4-8]l", "A22225line") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"^A", "Birline") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if None != re.search(r"j$", "Airline"):
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"\w$", "Airline%") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"\w$", "Airline8") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"Air\s", "Air line") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

if re.search(r"Hell|Fell|Dell", "Dellow") is not None:
    print("Pattern found")
else:
    print("Pattern not found")

import re

flight_details = "Flight Savana Airlines a2134"
print(flight_details)
print(re.sub(r"Flight", r"Plane", flight_details))
