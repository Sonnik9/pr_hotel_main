import unicodedata

text = "Your text with problematic symbols 😃"
# text = "Your text with problematic symbols 😞"

# Remove problematic symbols
text = "".join(c for c in text if unicodedata.category(c) != "So")

print("Output Text:", text)


