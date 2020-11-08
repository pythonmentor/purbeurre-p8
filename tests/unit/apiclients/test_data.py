VALID_PRODUCT = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "categories": "CategoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITHOUT_CODE = {
    "product_name": "Pizza margherita",
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITHOUT_NAME = {
    "code": 12345678,
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_NAME = {
    "code": 12345678,
    "product_name": "",
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_CATEGORIES = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_CATEGORIES = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "categories": "",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_NUTRISCORE = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_NUTRISCORE = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "",
    "generic_name": "pizza toute simple",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_GENERIC_NAME = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_GENERIC_NAME = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "categories": "categoryA,categoryB,categoryC",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "",
    "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_IMAGE_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_IMAGE_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": "",
    "image_nutrition_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_MISSING_IMAGE_NUTRITION_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    )
    # ...
}

INVALID_PRODUCT_WITH_EMPTY_IMAGE_NUTRITION_URL = {
    "code": 12345678,
    "product_name": "Pizza margherita",
    "nutriscore_grade": "a",
    "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
    "generic_name": "pizza toute simple",
    "image_url": (
        "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
    ),
    "image_nutrition_url": ""
    # ...
}


def get_valid_products():
    return [VALID_PRODUCT]


def get_invalid_products():
    return [
        INVALID_PRODUCT_WITHOUT_CODE,
        INVALID_PRODUCT_WITHOUT_NAME,
        INVALID_PRODUCT_WITH_EMPTY_NAME,
        INVALID_PRODUCT_WITH_MISSING_CATEGORIES,
        INVALID_PRODUCT_WITH_EMPTY_CATEGORIES,
        INVALID_PRODUCT_WITH_MISSING_URL,
        INVALID_PRODUCT_WITH_EMPTY_URL,
        INVALID_PRODUCT_WITH_MISSING_NUTRISCORE,
        INVALID_PRODUCT_WITH_EMPTY_NUTRISCORE,
        INVALID_PRODUCT_WITH_MISSING_GENERIC_NAME,
        INVALID_PRODUCT_WITH_EMPTY_GENERIC_NAME,
        INVALID_PRODUCT_WITH_MISSING_IMAGE_URL,
        INVALID_PRODUCT_WITH_EMPTY_IMAGE_URL,
        INVALID_PRODUCT_WITH_MISSING_IMAGE_NUTRITION_URL,
        INVALID_PRODUCT_WITH_EMPTY_IMAGE_NUTRITION_URL,
    ]


def get_invalid_with_one_valid_product():
    return get_valid_products() + get_invalid_products()