N = int(input())
carry = [int(input()) for _ in range(5)]
min_carry = min(carry)
print((N + min_carry - 1) // min_carry + 4)
