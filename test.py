import pandas as p


houses = {
    "price":[1,2,3,4],
    "locality":["a","b","c","d"]
}
houses["price"].append(5)
houses["locality"].append("e")

df = p.DataFrame(houses)
df
