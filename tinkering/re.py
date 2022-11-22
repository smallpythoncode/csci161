import re


x = "Shaken, not stirred."

y = re.split(r"\W+", x)
print(y)
