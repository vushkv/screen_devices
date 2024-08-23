from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os
import time

start_time = time.time()
print(f"Стартовое время: {start_time}")

email = 'Kondrnikolay@gmail.com'
password = 'AirdropFactory!Support1'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

if os.path.exists("DevicesScreenshotsAirdrop") is False:
    os.mkdir("DevicesScreenshotsAirdrop")

viewports = [
    {"name": "iPhone 12 Pro Max", "width": 428, "height": 926},
    {"name": "iPhone 12 Pro", "width": 390, "height": 844},
    {"name": "iPhone 12", "width": 414, "height": 895},
    {"name": "iPhone 11", "width": 390, "height": 844},
    {"name": "iPhone XR", "width": 414, "height": 896},
    {"name": "iPhone XS", "width": 375, "height": 812},
    {"name": "iPhone XS Max", "width": 414, "height": 896},
    {"name": "iPhone X", "width": 375, "height": 812},
    {"name": "iPhone 8 Plus", "width": 414, "height": 736},
    {"name": "iPhone 8", "width": 375, "height": 667},
    {"name": "iPhone 7 Plus", "width": 414, "height": 736},
    {"name": "iPhone 7", "width": 375, "height": 667},
    {"name": "iPhone 6 Plus/6S Plus", "width": 414, "height": 736},
    {"name": "iPhone 6/6S", "width": 375, "height": 667},
    {"name": "iPhone 5", "width": 320, "height": 568},
    {"name": "iPod Touch", "width": 320, "height": 568},
    {"name": "iPad Pro", "width": 1024, "height": 1366},
    {"name": "iPad Third & Fourth Generation", "width": 768, "height": 1024},
    {"name": "iPad Air 1 & 2", "width": 768, "height": 1024},
    {"name": "iPad Mini 2 & 3", "width": 768, "height": 1024},
    {"name": "iPad Mini", "width": 768, "height": 1024},
    {"name": "Nexus 6P", "width": 412, "height": 732},
    {"name": "Nexus 5X", "width": 412, "height": 732},
    {"name": "Google Pixel 3 XL", "width": 412, "height": 847},
    {"name": "Google Pixel 3", "width": 412, "height": 824},
    {"name": "Google Pixel 2 XL", "width": 412, "height": 732},
    {"name": "Google Pixel XL", "width": 412, "height": 732},
    {"name": "Google Pixel", "width": 412, "height": 732},
    {"name": "Samsung Galaxy Note 9", "width": 360, "height": 740},
    {"name": "Samsung Galaxy Note 5", "width": 480, "height": 853},
    {"name": "LG G5", "width": 480, "height": 853},
    {"name": "One Plus 3", "width": 480, "height": 853},
    {"name": "Samsung Galaxy S9+", "width": 360, "height": 740},
    {"name": "Samsung Galaxy S9", "width": 360, "height": 740},
    {"name": "Samsung Galaxy S8+", "width": 360, "height": 740},
    {"name": "Samsung Galaxy S8", "width": 360, "height": 740},
    {"name": "Samsung Galaxy S7 Edge", "width": 360, "height": 640},
    {"name": "Samsung Galaxy S7", "width": 360, "height": 640},
    {"name": "Nexus 9", "width": 768, "height": 1024},
    {"name": "Nexus 7 (2013)", "width": 600, "height": 960},
    {"name": "Samsung Galaxy Tab 10", "width": 800, "height": 1280},
    {"name": "Chromebook Pixel", "width": 1280, "height": 850},
    {"name": "iPhone 13 Pro Max", "width": 430, "height": 932},
    {"name": "iPhone 13 Pro", "width": 390, "height": 844},
    {"name": "iPhone 13", "width": 390, "height": 844},
    {"name": "iPhone 13 Mini", "width": 375, "height": 812},
    {"name": "iPhone SE (2020)", "width": 375, "height": 667},
    {"name": "Samsung Galaxy S10", "width": 360, "height": 760},
    {"name": "Samsung Galaxy S10+", "width": 360, "height": 760},
    {"name": "Samsung Galaxy S10e", "width": 360, "height": 760},
    {"name": "Samsung Galaxy Note 10", "width": 360, "height": 760},
    {"name": "Samsung Galaxy Note 10+", "width": 412, "height": 869},
    {"name": "OnePlus 7", "width": 412, "height": 869},
    {"name": "OnePlus 7 Pro", "width": 412, "height": 869},
    {"name": "Google Pixel 4", "width": 412, "height": 869},
    {"name": "Google Pixel 4 XL", "width": 412, "height": 869},
    {"name": "Google Pixel 4a", "width": 412, "height": 869},
    {"name": "Google Pixel 4a (5G)", "width": 412, "height": 869},
    {"name": "Google Pixel 5", "width": 412, "height": 869},
    {"name": "Huawei P30", "width": 412, "height": 869},
    {"name": "Huawei P30 Pro", "width": 412, "height": 869},
    {"name": "Huawei Mate 20", "width": 412, "height": 869},
    {"name": "Huawei Mate 20 Pro", "width": 412, "height": 869},
    {"name": "Xiaomi Mi 9", "width": 392, "height": 851},
    {"name": "Xiaomi Mi 9 SE", "width": 392, "height": 851},
    {"name": "Xiaomi Mi 10", "width": 392, "height": 851},
    {"name": "Xiaomi Mi 10 Pro", "width": 392, "height": 851},
    {"name": "Sony Xperia 1", "width": 360, "height": 854},
    {"name": "Sony Xperia 5", "width": 360, "height": 854},
    {"name": "Asus ROG Phone", "width": 412, "height": 869},
    {"name": "Asus ROG Phone 2", "width": 412, "height": 869},
    {"name": "Motorola Moto G7", "width": 412, "height": 869},
    {"name": "Motorola Moto G8", "width": 412, "height": 869},
    {"name": "Nokia 7.1", "width": 412, "height": 869},
    {"name": "Nokia 8.1", "width": 412, "height": 869},
    {"name": "Nokia 9 PureView", "width": 412, "height": 869},
    {"name": "Oppo Find X", "width": 412, "height": 869},
    {"name": "Oppo Reno", "width": 412, "height": 869},
    {"name": "LG V50 ThinQ", "width": 412, "height": 869},
    {"name": "LG G8 ThinQ", "width": 412, "height": 869},
    {"name": "ZTE Axon 10 Pro", "width": 412, "height": 869},
    {"name": "Razer Phone 2", "width": 412, "height": 869},
    {"name": "Microsoft Surface Go", "width": 800, "height": 1280},
    {"name": "Microsoft Surface Book 2", "width": 1366, "height": 912},
    {"name": "Apple MacBook Pro 13", "width": 1280, "height": 800},
    {"name": "Apple MacBook Pro 15", "width": 1440, "height": 900},
    {"name": "Apple iMac 21.5", "width": 1920, "height": 1080},
    {"name": "Apple iMac 27", "width": 2560, "height": 1440},
    {"name": "Apple MacBook Air 13", "width": 1440, "height": 900},
    {"name": "Apple MacBook Air M1", "width": 1440, "height": 900},
    {"name": "Dell XPS 13", "width": 1920, "height": 1080},
    {"name": "Dell XPS 15", "width": 1920, "height": 1080},
    {"name": "Microsoft Surface Laptop 3", "width": 2496, "height": 1664},
    {"name": "HP Spectre x360 13", "width": 1920, "height": 1080},
    {"name": "HP Spectre x360 15", "width": 3840, "height": 2160},
    {"name": "Lenovo Yoga C940", "width": 1920, "height": 1080},
    {"name": "Lenovo Yoga C740", "width": 1920, "height": 1080},
    {"name": "Asus ZenBook 14", "width": 1920, "height": 1080},
    {"name": "Asus ZenBook Flip", "width": 1920, "height": 1080},
    {"name": "Acer Swift 3", "width": 1920, "height": 1080},
    {"name": "Acer Spin 5", "width": 2256, "height": 1504},
    {"name": "Samsung Galaxy Book Flex", "width": 1920, "height": 1080},
    {"name": "Samsung Galaxy Book Ion", "width": 1920, "height": 1080},
    {"name": "Razer Blade Stealth 13", "width": 1920, "height": 1080},
    {"name": "Razer Blade 15", "width": 1920, "height": 1080},
    {"name": "LG Gram 14", "width": 1920, "height": 1080},
    {"name": "LG Gram 17", "width": 2560, "height": 1600},
    {"name": "Google Pixelbook", "width": 2400, "height": 1600},
    {"name": "Google Pixel Slate", "width": 3000, "height": 2000},
    {"name": "HP Elite Dragonfly", "width": 1920, "height": 1080},
    {"name": "Asus Chromebook Flip", "width": 1920, "height": 1080},
    {"name": "Acer Chromebook Spin 13", "width": 2256, "height": 1504},
    {"name": "Samsung Galaxy Chromebook", "width": 3840, "height": 2160},
    {"name": "Microsoft Surface Pro 7+", "width": 2736, "height": 1824},
    {"name": "Apple iPad Pro 11 (2021)", "width": 1668, "height": 2388},
    {"name": "Apple iPad Air (2020)", "width": 1640, "height": 2360},
    {"name": "Apple iPad (2020)", "width": 1620, "height": 2160},
    {"name": "Samsung Galaxy Tab S7+", "width": 2800, "height": 1752},
    {"name": "Samsung Galaxy Tab S7", "width": 2560, "height": 1600},
    {"name": "Amazon Fire HD 10", "width": 1920, "height": 1200},
    {"name": "Amazon Fire HD 8", "width": 1280, "height": 800},
    {"name": "Huawei MatePad Pro", "width": 2560, "height": 1600},
    {"name": "Lenovo Tab P11 Pro", "width": 2560, "height": 1600},
    {"name": "Xiaomi Mi Pad 5", "width": 2560, "height": 1600},
    {"name": "iPhone 14 Pro Max", "width": 430, "height": 932},
    {"name": "iPhone 14 Pro", "width": 390, "height": 844},
    {"name": "iPhone 14", "width": 390, "height": 844},
    {"name": "iPhone 14 Mini", "width": 375, "height": 812},
    {"name": "Samsung Galaxy S20", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S20+", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S20 Ultra", "width": 412, "height": 915},
    {"name": "Google Pixel 6", "width": 412, "height": 915},
    {"name": "Google Pixel 6 Pro", "width": 412, "height": 915},
    {"name": "OnePlus 9", "width": 412, "height": 915},
    {"name": "OnePlus 9 Pro", "width": 412, "height": 915},
    {"name": "Sony Xperia 1 III", "width": 360, "height": 854},
    {"name": "Sony Xperia 5 II", "width": 360, "height": 854},
    {"name": "Samsung Galaxy Z Fold 3", "width": 360, "height": 800},
    {"name": "Samsung Galaxy Z Flip 3", "width": 360, "height": 800},
    {"name": "Asus ROG Phone 5", "width": 412, "height": 915},
    {"name": "Motorola Edge+", "width": 412, "height": 915},
    {"name": "Motorola One 5G", "width": 412, "height": 915},
    {"name": "Nokia 8.3 5G", "width": 412, "height": 915},
    {"name": "Nokia 5.4", "width": 412, "height": 915},
    {"name": "Oppo Find X3 Pro", "width": 412, "height": 915},
    {"name": "Oppo Reno 5 Pro", "width": 412, "height": 915},
    {"name": "LG Wing", "width": 412, "height": 915},
    {"name": "ZTE Axon 30 Ultra", "width": 412, "height": 915},
    {"name": "Razer Phone 3", "width": 412, "height": 915},
    {"name": "TCL 10 Pro", "width": 412, "height": 915},
    {"name": "Microsoft Surface Duo 2", "width": 540, "height": 720},
    {"name": "Apple MacBook Pro 16", "width": 3072, "height": 1920},
    {"name": "Dell Alienware m15", "width": 1920, "height": 1080},
    {"name": "HP Omen 15", "width": 1920, "height": 1080},
    {"name": "Lenovo Legion 5", "width": 1920, "height": 1080},
    {"name": "Acer Predator Helios 300", "width": 1920, "height": 1080},
    {"name": "Asus TUF Gaming A15", "width": 1920, "height": 1080},
    {"name": "Razer Blade Pro 17", "width": 1920, "height": 1080},
    {"name": "Microsoft Surface Book 3", "width": 3000, "height": 2000},
    {"name": "Apple iPad Mini (2021)", "width": 1536, "height": 2048},
    {"name": "Samsung Galaxy Tab A7", "width": 2000, "height": 1200},
    {"name": "Amazon Fire 7", "width": 1024, "height": 600},
    {"name": "Huawei MediaPad M5", "width": 2560, "height": 1600},
    {"name": "Lenovo Tab M10", "width": 1920, "height": 1200},
    {"name": "Xiaomi Pad 5 Pro", "width": 2560, "height": 1600},
    {"name": "iPhone SE (2022)", "width": 375, "height": 667},
    {"name": "iPhone 15 Pro Max", "width": 430, "height": 932},
    {"name": "iPhone 15 Pro", "width": 390, "height": 844},
    {"name": "iPhone 15", "width": 390, "height": 844},
    {"name": "iPhone 15 Mini", "width": 375, "height": 812},
    {"name": "Samsung Galaxy S21", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S21+", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S21 Ultra", "width": 412, "height": 915},
    {"name": "Google Pixel 7", "width": 412, "height": 915},
    {"name": "Google Pixel 7 Pro", "width": 412, "height": 915},
    {"name": "OnePlus 10", "width": 412, "height": 915},
    {"name": "OnePlus 10 Pro", "width": 412, "height": 915},
    {"name": "Sony Xperia 1 IV", "width": 360, "height": 854},
    {"name": "Sony Xperia 5 III", "width": 360, "height": 854},
    {"name": "Samsung Galaxy Z Fold 4", "width": 360, "height": 800},
    {"name": "Samsung Galaxy Z Flip 4", "width": 360, "height": 800},
    {"name": "Asus ROG Phone 6", "width": 412, "height": 915},
    {"name": "Motorola Edge 30", "width": 412, "height": 915},
    {"name": "Motorola One 5G Ace", "width": 412, "height": 915},
    {"name": "Nokia X20", "width": 412, "height": 915},
    {"name": "Nokia G50", "width": 412, "height": 915},
    {"name": "Oppo Find X4 Pro", "width": 412, "height": 915},
    {"name": "Oppo Reno 6 Pro", "width": 412, "height": 915},
    {"name": "LG Wing 2", "width": 412, "height": 915},
    {"name": "ZTE Axon 40 Ultra", "width": 412, "height": 915},
    {"name": "Razer Phone 4", "width": 412, "height": 915},
    {"name": "TCL 20 Pro 5G", "width": 412, "height": 915},
    {"name": "Microsoft Surface Duo 3", "width": 540, "height": 720},
    {"name": "Apple MacBook Pro 18", "width": 3072, "height": 1920},
    {"name": "Dell Alienware m17", "width": 1920, "height": 1080},
    {"name": "HP Omen 17", "width": 1920, "height": 1080},
    {"name": "Lenovo Legion 7", "width": 1920, "height": 1080},
    {"name": "Acer Predator Triton 500", "width": 1920, "height": 1080},
    {"name": "Asus TUF Gaming F15", "width": 1920, "height": 1080},
    {"name": "Razer Blade Pro 18", "width": 1920, "height": 1080},
    {"name": "Microsoft Surface Book 4", "width": 3000, "height": 2000},
    {"name": "Apple iPad Mini (2022)", "width": 1536, "height": 2048},
    {"name": "Samsung Galaxy Tab A8", "width": 2000, "height": 1200},
    {"name": "Amazon Fire 8", "width": 1280, "height": 800},
    {"name": "Huawei MediaPad M6", "width": 2560, "height": 1600},
    {"name": "Lenovo Tab P12 Pro", "width": 2560, "height": 1600},
    {"name": "Xiaomi Pad 6", "width": 2560, "height": 1600},
    {"name": "iPhone SE (2023)", "width": 375, "height": 667},
    {"name": "iPhone 16 Pro Max", "width": 430, "height": 932},
    {"name": "iPhone 16 Pro", "width": 390, "height": 844},
    {"name": "iPhone 16", "width": 390, "height": 844},
    {"name": "iPhone 16 Mini", "width": 375, "height": 812},
    {"name": "Samsung Galaxy S22", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S22+", "width": 360, "height": 800},
    {"name": "Samsung Galaxy S22 Ultra", "width": 412, "height": 915},
    {"name": "Google Pixel 8", "width": 412, "height": 915},
    {"name": "Google Pixel 8 Pro", "width": 412, "height": 915},
    {"name": "OnePlus 11", "width": 412, "height": 915},
    {"name": "OnePlus 11 Pro", "width": 412, "height": 915},
    {"name": "Sony Xperia 1 V", "width": 360, "height": 854},
    {"name": "Sony Xperia 5 IV", "width": 360, "height": 854},
    {"name": "Samsung Galaxy Z Fold 5", "width": 360, "height": 800},
    {"name": "Samsung Galaxy Z Flip 5", "width": 360, "height": 800},
    {"name": "Asus ROG Phone 7", "width": 412, "height": 915},
    {"name": "Motorola Edge 40", "width": 412, "height": 915},
    {"name": "Motorola One 5G Ace 2", "width": 412, "height": 915},
    {"name": "Nokia X30", "width": 412, "height": 915},
    {"name": "Nokia G60", "width": 412, "height": 915},
    {"name": "Oppo Find X5 Pro", "width": 412, "height": 915},
    {"name": "Oppo Reno 7 Pro", "width": 412, "height": 915},
    {"name": "LG Wing 3", "width": 412, "height": 915},
    {"name": "ZTE Axon 50 Ultra", "width": 412, "height": 915},
    {"name": "Razer Phone 5", "width": 412, "height": 915},
    {"name": "TCL 30 Pro 5G", "width": 412, "height": 915},
    {"name": "Microsoft Surface Duo 4", "width": 540, "height": 720},
    {"name": "Apple MacBook Pro 20", "width": 3072, "height": 1920},
    {"name": "Dell Alienware m19", "width": 1920, "height": 1080},
    {"name": "HP Omen 19", "width": 1920, "height": 1080},
    {"name": "Lenovo Legion 9", "width": 1920, "height": 1080},
    {"name": "Acer Predator Triton 700", "width": 1920, "height": 1080},
    {"name": "Asus TUF Gaming F17", "width": 1920, "height": 1080},
    {"name": "Razer Blade Pro 19", "width": 1920, "height": 1080},
    {"name": "Microsoft Surface Book 5", "width": 3000, "height": 2000},
    {"name": "Apple iPad Mini (2023)", "width": 1536, "height": 2048},
    {"name": "Samsung Galaxy Tab A9", "width": 2000, "height": 1200},
    {"name": "Amazon Fire 9", "width": 1280, "height": 800},
    {"name": "Huawei MediaPad M7", "width": 2560, "height": 1600},
    {"name": "Lenovo Tab P14 Pro", "width": 2560, "height": 1600},
    {"name": "Xiaomi Pad 7", "width": 2560, "height": 1600}
]

for device in viewports:
    try:
        username = 'dev'
        password = 'Su6niengiuGun1'
        chromedriver_path = '/Users/viktorushakov/PycharmProjects/screen_device/venv/bin/chromedriver'
        driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=chrome_options)
        driver.set_window_size(device['width'], device['height'])
        driver.get(f"https://{username}:{password}@preprod.intranet.airdropfactory.app/auth/login")
        time.sleep(2)
        screenshot_path = f'DevicesScreenshotsAirdrop/{device["name"]} {device["width"]}x{device["height"]} auth.png'
        driver.save_screenshot(screenshot_path)

        email_field = driver.find_element(By.CSS_SELECTOR, "#app > main > div > div > article > div > div:nth-child(1) > div > input[type=email]")
        email_field.send_keys(email)

        pass_field = driver.find_element(By.CSS_SELECTOR, "#app > main > div > div > article > div > div:nth-child(2) > div > input[type=password]")
        pass_field.send_keys(password)

        button = driver.find_element(By.CSS_SELECTOR, "#app > main > div > div > article > button")
        button.click()
        time.sleep(2)

        screenshot_path = f'DevicesScreenshotsAirdrop/{device["name"]} {device["width"]}x{device["height"]} modal.png'
        driver.save_screenshot(screenshot_path)
        time.sleep(2)

        button_cross = driver.find_element(By.CSS_SELECTOR, "#app > main > section > article.dashboard.page > div.modal > div > div.modal__header > div > svg")
        button_cross.click()
        time.sleep(2)

        screenshot_path = f'DevicesScreenshotsAirdrop/{device["name"]} {device["width"]}x{device["height"]} main.png'
        driver.save_screenshot(screenshot_path)
        time.sleep(2)

        if device["width"] > 1060:
            try:
                button_setting = driver.find_element(By.CSS_SELECTOR,"#app > main > section > article.sidebar > div > nav > ul > li:nth-child(7) > a > div > span")
                button_setting.click()
                time.sleep(2)

                button_2fa = driver.find_element(By.CSS_SELECTOR, "#app > main > section > article.settings.page.bg-\[\#0f0f13\] > div:nth-child(2) > div.settings__update > div:nth-child(1) > button")
                button_2fa.click()
                time.sleep(2)
                screenshot_path = f'DevicesScreenshotsAirdrop/{device["name"]} {device["width"]}x{device["height"]} 2fa.png'
                driver.save_screenshot(screenshot_path)
            except Exception as e:
                print(f"Error {device['name']}: {e}")

        else:
            try:
                button_menu = driver.find_element(By.CSS_SELECTOR, '#app > main > header > div > svg')
                button_menu.click()
                time.sleep(3)
                button_setting = driver.find_element(By.CSS_SELECTOR, "#app > main > section > article.sidebar.sidebar--open > div > nav > ul > li:nth-child(7) > a")
                button_setting.click()
                time.sleep(2)
                button_2fa = driver.find_element(By.CSS_SELECTOR, "#app > main > section > article.settings.page.bg-\[\#0f0f13\] > div:nth-child(2) > div.settings__update > div:nth-child(1) > button")
                button_2fa.click()
                time.sleep(2)
                screenshot_path = f'DevicesScreenshotsAirdrop/{device["name"]} {device["width"]}x{device["height"]} 2fa.png'
                driver.save_screenshot(screenshot_path)
                driver.quit()
            except Exception as e:
                print(f"Error {device['name']}: {e}")

    except Exception as e:
        print(f"Error {device['name']}: {e}")


end_time = time.time()
print(f"Конечное время: {end_time}")
execution_time = end_time - start_time

print(f"Время выполнения программы: {execution_time} секунд или {execution_time // 60} минут")