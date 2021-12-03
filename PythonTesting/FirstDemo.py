
print("Hello word")
# here are the comments i have defined
# asi se dejan comentarios en python

a = 3
print(a)

Str = "hola mundo"
print(Str)

b, c, d = 3, 6.4, "bien"
print("{}{}{}{}{}{}".format("El valor es ", b, " el valor es ", c, " el valor es ", d))

values = [1, 2, "dario", 4, 5]

for i in range (len(values)):

    print(values[i])

print(values[3])  # 4
print(values[-1])  # 5
print(values[1:3]) # 2 , dario
print(values)
values.insert(4, "betty")
values.append("6")

print(values)
