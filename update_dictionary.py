import json

ACCENT_MAP = str.maketrans("ΆΈΉΊΌΎΏάέήίόύώϊϋΐΰ", "ΑΕΗΙΟΥΩαεηιουωιυιυ")

with open("hunspell_4letter.txt", encoding="utf-8") as f:
    words = [line.strip().translate(ACCENT_MAP).upper() for line in f if line.strip()]

words = sorted(set(words))

with open("dictionary.json", encoding="utf-8") as f:
    data = json.load(f)

data["dictionary"] = words

with open("dictionary.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done! {len(words)} words written to dictionary.")
