from backend.core.ai.text_corrector import TextCorrector

corrector = TextCorrector()

tests = [
    "Nom:",
    "Prenom",
    "Telephone",
    "Teleph0ne",
    "Date Naiss",
    "e-mail",
]

print("=" * 50)
print("TEXT CORRECTOR")
print("=" * 50)

for t in tests:
    print(f"{t:15} -> {corrector.normalize(t)}")