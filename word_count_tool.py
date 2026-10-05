# Word Count Tool

from collections import Counter

try:
    # Open and read the file
    with open("data_st.txt", "r") as file:
        data = file.read()

    # Count lines
    lines = data.splitlines()
    line_count = len(lines)

    # Count words
    words = data.split()
    word_count = len(words)

    # Count characters
    character_count = len(data)

    # Word frequency analysis
    word_frequency = Counter(words)

    # Display results
    print("\n========== WORD COUNT ANALYSIS ==========")

    print("Number of Lines     :", line_count)
    print("Number of Words     :", word_count)
    print("Number of Characters:", character_count)

    print("\n========== WORD FREQUENCY ==========")

    for word, count in word_frequency.most_common():
        print(word, ":", count)

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)