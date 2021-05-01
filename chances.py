# currentChance
z = 0.06275
print("initial chance")
print(z)
print("\n")

# 1.22 = 22% =>
# print(1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3)


"""
Case #1

chance is simply the number
x = chance = 1.06138
"""
x = z + 1
print("starting case #1")
print(f"using chance value {x}")


# # subcase 1
# # x + 1.22 = 1.06183
# print("subcase 1")

# subcase 2
# x * 2.22 = 1.06183
y = x/2.22
print("subcase 2")
print(y)
print(1.045 < y < 1.055)

# subcase 3
# x * 1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3 = 1.06183
print("subcase 3")
y = x/(1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3)
print(y)
print(1.045 < y < 1.055)

# subcase 4
# x * (1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3) = 1.06183
print("subcase 4")
y = x/(1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3)
print(y)
print(1.045 < y < 1.055)

"""
Case #2

chance is 1 + chance
x = chance is 0.06138
"""
x = z
print("starting case #2")
print(f"using chance value {x}")

# # subcase 1
# # x + 1.22 = 0.06183
# print("subcase 1")

# subcase 2
# x * 2.22 = 0.06183
y = x/2.22
print("subcase 2")
print(y)
print(0.045 < y < 0.055)

# subcase 3
# x * 1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3 = 0.06183
y = x / (1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3)
print("subcase 3")
print(y)
print(0.045 < y < 0.055)

# check
# subcase 4
# x * (1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3) = 1.06183
y = x/(1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3)
print("subcase 4")
print(y)
print(0.045 < y < 0.055)

"""
Case #3

chance is 1 + chance/100
x = chance is 6.138
"""
x = z * 100
print("starting case #3")
print(f"using chance value {x}")

# subcase 1
# x + 1.22 = 6.183
y = x - 1.22
print("subcase 1")
print(y)
print(4.5 < y < 5.5)

# subcase 2
# x * 2.22 = 6.183
y = x/2.22
print("subcase 2")
print(y)
print(4.5 < y < 5.5)

# subcase 3
# x * 1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3 = 6.183
y = x / (1.1**4 * 1.05**3 * 1.12 * 1.25 * 1.3)
print("subcase 3")
print(y)
print(4.5 < y < 5.5)

# check
# subcase 4
# x * (1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3) = 1.06183
y = x/(1 + 0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3)
print("subcase 4")
print(y)
print(4.5 < y < 5.5)

# subcase 5
# x + (0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3) = 1.06183
y = x-(0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3)
print("subcase 4")
print(y)
print(4.5 < y < 5.5)

# conclusion
print("chance is calculated as follows")
print("x + ((chance item/100)*(amount of item) + (chance item/100)*(amount of item) etc) = chance")
print("x being the default weapon drop chance percentage")
print(" chance item being the chance percentage given by the item")
print("5 + (0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3) = 6.22")
print("this corresponds with the percentage given in game")
print("ie if the game says 122%% chance, then its default chance + that value/100")
print("chance = 5 + 1.22 = 6.22")
print(5 + (0.1*4 + 0.05*3 + 0.12 + 0.25 + 0.3))
