from fastapi import FastAPI, BackgroundTasks
from scraper import scrape_car
from database import add_database, search_id, search_many


app = FastAPI()


@app.get("/")
def root():
    return {"შეტყობინება": "Hello World"}


@app.post("/api/product/")
def post_car(car_id: int, background_tasks: BackgroundTasks):
    """
    ამატებს ერთ მანქანას მონაცემთა ბაზაში background-ში
    """

    #  სკრაპავს მანქანას და ამატებს ბაზაში
    def car_add(car_id):
        car_dict: dict = scrape_car(car_id)  # მანაქანის დასკრაპვა
        add_database(car_dict)  # ბაზაში დამატაება

    background_tasks.add_task(car_add, car_id)  # background task-ში დამატება
    return {"შეტყობინება": "მანქანა დაიმატა მონაცემთა ბაზაში"}


@app.get("/api/product/")
def get_car(car_id: int):
    """
    ეზებს მანქანას მონაცემთა ბაზიდან
    """
    search_car = search_id(car_id)  # მანქანის ძებდა myauto id-ს მიხედვით
    return {"შეტყობინება": search_car}


@app.get("/api/appraisal/")
def get_average_price(car_id: int):
    """
    ვაბრუნებს საშუალო ფასს
    """
    car_dict: dict = scrape_car(car_id)  # მანაქანის დასკრაპვა
    seach_price = search_many(car_dict)  # ბაზაში ძებნა ფილტრის მიხდევით
    average_price_list = []  # ცარიელი სია სადაც ჩავსვათ მოძებნილი მანქ. ფასებს
    for item in seach_price:
        average_price_list.append(
            item["price_usd"]
        )  # ვამატებთ სიაში თითოული მანქანის ფასი
    average_price = sum(average_price_list) / len(
        average_price_list
    )  # საშუალო ფასის გამოთვლა
    return {"საშუალო ფასი": average_price}
