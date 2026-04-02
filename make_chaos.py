from PIL import Image, ImageDraw, ImageFont
import random

# Tworzymy obrazek 1200x800 (poczucie wielkiego arkusza)
img = Image.new('RGB', (1200, 800), color=(240, 240, 240))
d = ImageDraw.Draw(img)

# Rysujemy siatkę Excela
for i in range(0, 1200, 100): d.line([(i, 0), (i, 800)], fill=(200, 200, 200), width=1)
for i in range(0, 800, 30): d.line([(0, i), (1200, i)], fill=(200, 200, 200), width=1)

# Wypełniamy chaosem
errors = ["#REF!", "#ADR!", "#DZIEL/0!", "BŁĄD!", "NIECZYTELNE", "NULL", "???"]
headers = ["ID_STARE", "DATA_2018", "KOSZT_UKRYTY", "UWAGI_FINAL_v3", "X_PROD"]

for x in range(0, 1200, 100):
    for y in range(0, 800, 30):
        if random.random() > 0.7:
            txt = random.choice(errors + headers + [str(random.randint(1000, 9999))])
            color = random.choice([(255, 200, 200), (255, 255, 200), (200, 255, 200)])
            d.rectangle([x+1, y+1, x+99, y+29], fill=color)
            d.text((x+5, y+5), txt, fill=(50, 50, 50))

# Dodajemy zakładki na dole
d.rectangle([0, 770, 1200, 800], fill=(220, 220, 220))
tabs = ["Kancelaria_ARCHIWUM", "Logistyka_STARA", "MED_FINAL_2022"]
curr_x = 10
for tab in tabs:
    d.text((curr_x, 775), tab, fill=(0, 0, 0))
    curr_x += 200

img.save('excel_chaos.png')
print("Plik excel_chaos.png został stworzony!")
