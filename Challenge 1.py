numbers = [5, 10, 7, 9]
for i in range(len(numbers)):
  numbers[i] = pow(numbers[i],3)

print("Original Numbers:", numbers)
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Changed Numbers:", numbers)

