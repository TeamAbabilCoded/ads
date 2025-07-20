import requests, random, time, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load config
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["bot_token"]
CHAT_ID = config["chat_id"]
DELAY_MIN = config["min_delay"]
DELAY_MAX = config["max_delay"]

def kirim_telegram(pesan):
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID,
            "text": pesan
        })
    except:
        pass

def load_data():
    with open("direct_links.txt") as f:
        links = [x.strip() for x in f if x.strip()]
    with open("proxies.txt") as f:
        proxies = [x.strip() for x in f if x.strip()]
    with open("user_agents.json") as f:
        ua = json.load(f)
    return links, proxies, ua

def setup_driver(proxy, user_agent):
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def visit_link(driver, link):
    try:
        driver.get(link)
        time.sleep(random.uniform(5, 8))

        # Simulasi klik (opsional)
        if random.randint(1, 4) == 1:  # 25% klik
            try:
                iklan = driver.find_element(By.TAG_NAME, "a")
                iklan.click()
                return "VISIT + KLIK"
            except:
                return "VISIT ONLY"
        return "VISIT ONLY"
    except:
        return "FAILED"

def main():
    links, proxies, uas = load_data()
    total_visit, total_klik = 0, 0

    for proxy in proxies:
        try:
            ua_list = uas["android"] + uas["ios"]
            for _ in range(random.randint(3, 5)):  # random visit per proxy
                link = random.choice(links)
                ua = random.choice(ua_list)
                driver = setup_driver(proxy, ua)
                result = visit_link(driver, link)
                driver.quit()

                total_visit += 1
                if "KLIK" in result:
                    total_klik += 1

                kirim_telegram(f"✅ {result} | {link}\n🎯 IP: {proxy}\n📱 UA: {ua[:40]}...")
                time.sleep(random.randint(DELAY_MIN, DELAY_MAX))
        except Exception as e:
            print(f"Error: {e}")
            continue

    kirim_telegram(f"📊 JOB DONE\n🔁 Total Visit: {total_visit}\n🖱 Total Klik: {total_klik}")

if __name__ == "__main__":
    main()
