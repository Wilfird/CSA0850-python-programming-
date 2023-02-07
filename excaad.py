letters=["a","b","c"]
letters.append("d")
print(letters)
letters.pop(0)
print(letters)
letters.insert(0,"x")
print(letters)
letters.pop(2)
print(letters)
print(letters.index("b"))
if "d" in letters:
    print("letter found")
