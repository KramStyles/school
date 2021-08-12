import json
from requests import request

school_name = "Enugu State College of Education"
mobile = "+234 808 579 6361"
mail = "admin@escet.com"

details = {
    'name' : school_name,
    'mobile': mobile,
    'mail': mail
}

menu = {
    '.': ['home2', 'Home'],
    'about': ['address-book', 'About Us'],
    'campus': ['building', 'Our Campus', ['academics', 'news', 'our interns', 'our leadership', 'careers', 'human resources']],
    'courses': ['library_books', 'Our Courses', ['math', 'science & engineering', 'arts & humanities', 'economics & finance', 'business administration', 'computer science']],
    'contact': ['phone_android', 'Contact']
}
slide = [
    ['graduation', 'Graduate without stress!'],
    ['e-learning', 'Learn comfortably online!'],
    ['wifi', 'Enjoy Free Browsing!'],
    ['youth_forum', 'Join our Youths Forum!'],
]