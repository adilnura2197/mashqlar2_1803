#1
d = dict()
print(d)

d["x"] = 10
d["y"] = 20
d["z"] = 30

print(d)


#2
d = {
    "a": 5,
    "b": 10
}

print(d)

d["c"] = 15
d["d"] = 20

print(d)


#3
d = dict(name="Ali", age=20)
print(d)

d["age"] = 25
print(d)


#4
d = {}

for i in range(3):
    kalit = input(f"{i+1}-kalitni kiriting: ")
    qiymat = input(f"{i+1}-qiymatni kiriting: ")
    d[kalit] = qiymat

print("Yakuniy dictionary:", d)


#5
d1 = {"x": 1, "y": 2}
d2 = {"y": 3, "z": 4}
print(d1)
print(d2)

d = {**d1, **d2}
print(d)
