def are_nearly_equal(s1, s2, threshold=2):
    length_diff = abs(len(s1) - len(s2))
    if length_diff > threshold:
        return False

    diff_count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff_count += 1

    diff_count += length_diff

    return diff_count <= threshold

print(are_nearly_equal("kitten", "sitten"))
print(are_nearly_equal("book", "back"))
