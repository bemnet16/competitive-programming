n,m,a = map(int, input.split())

if m % a == 0:
    side_1 = m // a
else:
    side_1 = m // a + 1
if n % a == 0:
    side_2 = n // a
else:
    side_2 = n // a + 1
    
square = side_1 * side_2 
print(square)
