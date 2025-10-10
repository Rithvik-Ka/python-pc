from datetime import datetime

name = input("Your name: ").strip()
mood = input("Mood (1-5): ").strip()
note = input("One thing you learned: ").strip()
stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("class_log.csv", "a", encoding="utf-8") as f:
    f.write(f"{stamp},{name},{mood},{note}"+"\n")
print("Logged! Open class_log.csv to verify.")