def max(a, b):
    if a > b:
        return a
    else:
        return b
    
valueA = int(input("Entrer la valeur de a:"))
valueB = int(input("Entrer la valeur de b:"))
max_value = max(valueA, valueB)
print(max_value)