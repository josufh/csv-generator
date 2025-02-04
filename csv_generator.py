import csv
from kanji_list import kanji_n5 as list_to_csv

csv_filename = "kanji_n5_ankipro_cards.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for kanji_data in list_to_csv:
        kanji = kanji_data["kanji"]
        onyomi = kanji_data["onyomi"]
        kunyomi = kanji_data["kunyomi"]
        
        examples_onyomi = "<br>".join([f"{word}" for word in kanji_data["examples_onyomi"].split("　")])
        examples_kunyomi = "<br>".join([f"{word}" for word in kanji_data["examples_kunyomi"].split("　")])
        examples_irregular = "<br>".join([f"{word}" for word in kanji_data["examples_irregular"].split("　")])

        front_reading = f"<b>{kanji}</b>"
        back_reading = f"<b>{onyomi}</b><br>{examples_onyomi}<br><br><b>{kunyomi}</b><br>{examples_kunyomi}<br>{examples_irregular}"
        writer.writerow([front_reading, back_reading])

print(f"CSV file '{csv_filename}' created successfully!")