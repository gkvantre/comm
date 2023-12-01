from tinydb import TinyDB, Query

db = TinyDB("parsed_cars.json")
Car = Query()


def add_database(car_dict: dict):
    """
    ემატებს მონაცემთა ბაზას მანქანის მონაცემები
    """
    db.insert(car_dict)  # ვამატებთ მანქანას ბაზაში


def search_id(car_id: int):
    """
    ეძებს მონაცემთა ბაზაში მანქანას
    """
    one_car = db.search(Car.car_id == car_id)  # myauto.ge ID ვეძებთ მანქანას
    return one_car  # ვაბრუნებ მანქანას


def search_many(car_dict: dict):
    """
    ფილტრავს ძიების შედეგებს man_id, model_id, prod_year
    """
    search_result = db.search(
        Car.fragment(
            {
                "man_id": car_dict["man_id"],  # 42 - TOYOTA (მაგალითად)
                "model_id": car_dict["model_id"],  # 4112 - PRIUS (მაგალითად)
                "prod_year": car_dict["prod_year"],  # 2010
            }
        )
    )
    return search_result
