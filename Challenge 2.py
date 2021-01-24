numbers = [5, 10, 7, 9]
print("Original Numbers:", numbers)

for i in range(len(numbers)):
  numbers[i] = pow(numbers[i],-2)
  numbers[i] = round(numbers[i], 4)

print("Changed Numbers:", numbers)

numbers = sorted(numbers)

print("Sorted Numbers:", numbers)

