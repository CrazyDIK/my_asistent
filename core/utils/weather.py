from selenium import webdriver
from PIL import Image


def get_screen_weather():
    driver = webdriver.Firefox()
    driver.get("https://www.gismeteo.ru/weather-lipetsk-4437/")
    driver.save_screenshot("screenshots\screenie.png")
    # driver.save_screenshot(".screenie.png")
    driver.quit()

def immage_modif():
    img = Image.open("screenshots\screenie.png")
    im_crop = img.crop((0, 300, 680, 760))
    im_crop.save("screenshots\guido_pillow_crop.png", quality=95)


def main():
    get_screen_weather()
    immage_modif()


if __name__ == "__main__":
    main()
