n = 37  # Example number
k = 3   # Bit position to check (0-indexed)

if (n >> k) & 1:
    print("k-th bit is SET")
else:
    print("k-th bit is NOT SET")