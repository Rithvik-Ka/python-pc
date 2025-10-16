from datetime import datetime

name = input("Your name: ").strip()
mood = input("Mood (1-5): ").strip()
note = input("One thing you learned: ").strip()
stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("l15g.csv", "a", encoding="utf-8") as f:
    f.write(f"{stamp},{name},{mood},{note}"+"\n")
print("Logged! Open l15.csv to verify.")