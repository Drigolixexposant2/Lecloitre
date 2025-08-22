from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import urllib.request

def main():
    url = "https://raw.githubusercontent.com/Drigolixexposant2/Lecloitre/main/start_date.txt"
    with urllib.request.urlopen(url) as response:
        date_str = response.read().decode('utf-8').strip()

    start_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    now = datetime.now()
    delta = now - start_date
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    img = Image.new('RGB', (400, 50), color='white')
    draw = ImageDraw.Draw(img)
    text = f"Temps sans fumer : {days} jours, {hours} heures, {minutes} minutes"

    draw.text((10, 10), text, fill='black')
    img.save('elapsed_time.jpg')

if __name__ == "__main__":
    main()
