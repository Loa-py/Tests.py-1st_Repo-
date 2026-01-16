def find_occurrences(text, pattern):
    positions = []
    pattern_length = len(pattern)

    for i in range(len(text) - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            positions.append(i)

    if positions:
        return (True, len(positions), positions)
    else:
        return (False, 0, [])


# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)
