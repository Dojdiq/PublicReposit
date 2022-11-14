from cat import Cat

cat = Cat("Sam", "m", 2)
cat2 = Cat("Tom", "f", 1)
cats = [cat, cat2]
print("Cats:")
for i in cats:
    print(i())