from datetime import datetime


class Book:
    def __init__(self, title, description, publish_date):
        self.title = title
        self.description = description
        self.publish_date = publish_date


    def print_book_details(book):
        print('Title: ' + item.title)
        print('Description: ' + item.description)
        print('Published: ' + item.ymdhm)


summary = 'Clean Code Is Great!'
description = 'Actually, writing Clean Code can be pretty fun. You\'ll see!'
new_date = datetime.now()
published_date = new_date.strftime('%Y-%m-%d %H:%M')

clean_code = Book(summary, description, published_date)

print_book_details(clean_code)
