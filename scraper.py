import requests
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
}

base_url = "https://api2.myauto.ge/ka/products/"  # myauto.ge api-ს მისამართი


def scrape_car(car_id: int) -> dict:
    """
    აბრუნებს მანქანის მონაცემებს დიქტში.

    """
    # მაგ. https://api2.myauto.ge/ka/products/98917719
    car_url = f"{base_url}{car_id}"
    time.sleep(5)  # დაპაუზება 5 წამით
    response = requests.get(car_url, headers=headers)  # ფასუხი myauto.ge-დან
    if response.status_code == 200:  # სატუს კოდი 200, OK
        json_data = (
            response.json().get("data").get("info")
        )  # ვიღებთ მხოლოდ მანქანის მონამემები
        car_dict = {
            "car_id": json_data["car_id"],  # 98917719
            "man_id": json_data["man_id"],  # 42 - TOYOTA (მაგალითად)
            "model_id": json_data["model_id"],  # 4112 - PRIUS (მაგალითად)
            "prod_year": json_data["prod_year"],  # 2010
            "price_usd": json_data["price_usd"],  # 10000
        }
        return car_dict  # ვაბრუნებთ მონაცემებს
