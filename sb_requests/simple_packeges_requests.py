import requests
import simple_books_auth as sba

token = sba.get_token()
headers = {'Authorization': token}
URL = 'https://simple-books-api.glitch.me'


def get_status():  # definim metoda, folosim request ul GET
    response = requests.get(URL + '/status')  # folosim constanta creata(URL)+cerinta din API(link)
    # return response                                                  # ne va returna cod 200 (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
    return response.json()  # folosind .json vom primi mesajul text


print(get_status())

'''type: fiction or non-fiction
limit: a number between 1 and 20.
https://simple-books-api.glitch.me/books?type=fiction&limit=2
'''


def get_books():  # definim metoda, folosim request-ul GET
    response = requests.get(URL + "/books")
    return response.json()


# print(get_books())


def get_books_filter(book_type, book_limit):  # definim o metoda de cautare dupa: type
    response = requests.get(URL + f'/books?type={book_type}&limit={book_limit}')
    return response.json()


print(get_books_filter('fiction', 0))  # chiar daca este limitat la "0" ne returneaza toate cartile de tipul cerut


# TEMA, incearca definierea unei metode - type, ID, limit
def get_a_book(book_id):
    return requests.get(URL + f"/books/{book_id}").json()


print(get_a_book('6'))  # cifra reprezinta ID ul cartii din baza de date


def submit_an_order():
    body = {
        "bookId": 1,
        "customerName": "John"
    }

    return requests.post(URL + '/orders', json=body, headers=headers).json()


# print(submit_an_order())
order_id = (submit_an_order())


def get_all_orders():
    return requests.get(URL + "/orders", headers=headers).json()


print(get_all_orders())


def get_books_filter(book_type, book_limit):  # metoda este repetata, am schimbat genul(type) cartii cautate
    response = requests.get(URL + f"/books?type={book_type}&limit={book_limit}")
    return response.json()


print(get_books_filter('non-fiction', 1))


def update_an_order():
    body = {
        "customerName": "John"
    }
    return requests.patch(URL + f'/orders/{order_id}', headers=headers, json=body).json()


# print(order_id)
print(update_an_order())

# TEMA! Recuperati orderid din dictionarul oreder id
