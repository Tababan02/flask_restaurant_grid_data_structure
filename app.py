from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Isabela",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/18823964/pexels-photo-18823964/free-photo-of-lamps-on-restaurant-terrace.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 2,
        "location": "Makati",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1307698/pexels-photo-1307698.jpeg"
   }, {
        "id": 3,
        "location": "Pasig",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Mandaluyong City",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1055054/pexels-photo-1055054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14713414/pexels-photo-14713414.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Makati",
        "restaurant_name": "Restaurant Six",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5490830/pexels-photo-5490830.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 7,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2788792/pexels-photo-2788792.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 8,
        "location": "Taguig",
        "restaurant_name": "Restaurant Eight",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/3465604/pexels-photo-3465604.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 9,
        "location": "Makati",
        "restaurant_name": "Restaurant Nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2196722/pexels-photo-2196722.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 10,
        "location": "caloocan",
        "restaurant_name": "Restaurant Ten",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/11439363/pexels-photo-11439363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
   
    }, {"id": 11,
        "location": "Bagong Silang",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/10084716/pexels-photo-10084716.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 12,
        "location": "Tala",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5864548/pexels-photo-5864548.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    
    }, {
        "id": 13,
        "location": "Pasig",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16997158/pexels-photo-16997158/free-photo-of-empty-seats-in-restaurant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    
    }, {
        "id": 14,
        "location": "Makati",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/776538/pexels-photo-776538.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {

        "id": 15,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/260922/pexels-photo-260922.jpeg"

    }, {
        "id": 16,
        "location": "Alabang",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/11808194/pexels-photo-11808194.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 17,
        "location": "Makati",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/18823964/pexels-photo-18823964/free-photo-of-lamps-on-restaurant-terrace.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 18,
        "location": "Ilocos Norte",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1307698/pexels-photo-1307698.jpeg"
   }, {
        "id": 19,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 20, 
        "location": "Roxas City",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1055054/pexels-photo-1055054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 21,
        "location": "Siargao",
        "restaurant_name": "Restaurant Twenty One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14713414/pexels-photo-14713414.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 22,
        "location": "Bohol",
        "restaurant_name": "Restaurant Twenty Two",
        "status": "Close",
        "image_url": "https://images.pexels.com/photos/5490830/pexels-photo-5490830.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 23,
        "location": "Vigan",
        "restaurant_name": "Restaurant Twenty Three",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2788792/pexels-photo-2788792.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 24,
        "location": "Davao",
        "restaurant_name": "Restaurant Twenty Four",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/3465604/pexels-photo-3465604.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 25,
        "location": "Baguio",
        "restaurant_name": "Restaurant Twenty Five",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2196722/pexels-photo-2196722.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 26,
        "location": "Boracay",
        "restaurant_name": "Restaurant  Twenty Six",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/11439363/pexels-photo-11439363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
   
    }, {"id": 27,
        "location": "Palawan",
        "restaurant_name": "Restaurant Twenty Seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/10084716/pexels-photo-10084716.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 28,
        "location": "Manila",
        "restaurant_name": "Restaurant Twenty Eight",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/5864548/pexels-photo-5864548.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    
    }, {
        "id": 29,
        "location": "Vertis North",
        "restaurant_name": "Restaurant Twenty Nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16997158/pexels-photo-16997158/free-photo-of-empty-seats-in-restaurant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    
    }, {
        "id": 30,
        "location": "Pasig",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/776538/pexels-photo-776538.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 31,
        "location": "Makati",
        "restaurant_name": "Restaurant Thirty One",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5490830/pexels-photo-5490830.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{ 
        "id": 32,
        "location": "Manila",
        "restaurant_name": "Restaurant Thirty Two",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/5864548/pexels-photo-5864548.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, { 
        "id": 33,
        "location": "Boracay",
        "restaurant_name": "Restaurant  Thirty Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/11439363/pexels-photo-11439363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
   }, {
        "id": 34,
        "location": "Alabang",
        "restaurant_name": "Restaurant Thirty Four",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/11808194/pexels-photo-11808194.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 36,
        "location": "Tala",
        "restaurant_name": "Restaurant Thirty Seven",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16997158/pexels-photo-16997158/free-photo-of-empty-seats-in-restaurant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 37,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Thirty Eight",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5864548/pexels-photo-5864548.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 38,
        "location": "Makati",
        "restaurant_name": "Restaurant Thirty Nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5864548/pexels-photo-5864548.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 40,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Fourty",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/761854/pexels-photo-761854.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {  
         "id": 41,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fourty One",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12317827/pexels-photo-12317827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, { 
         "id": 42,
        "location": "Tala",
        "restaurant_name": "Restaurant Fourty Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12876503/pexels-photo-12876503.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, { 
         "id": 43,
        "location": "Makati",
        "restaurant_name": "Restaurant Fourty Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/17001738/pexels-photo-17001738/free-photo-of-decorated-tables-for-wedding-in-luxury-restaurant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, { 
        "id": 44,
        "location": "Laguna",
        "restaurant_name": "Restaurant Fourty Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/28617375/pexels-photo-28617375/free-photo-of-contemporary-game-table-in-dubai-apartment.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 45,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Fourty Five",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/28593083/pexels-photo-28593083/free-photo-of-cozy-restaurant-in-dubai-with-elegant-decor.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 46,
        "location": "Tala",
        "restaurant_name": "Restaurant Fourty Six",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/28442306/pexels-photo-28442306/free-photo-of-charming-outdoor-cafe-seating-at-mokador.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
        "id": 47,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fourty Seven",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/15268897/pexels-photo-15268897/free-photo-of-aesthetic-coffee-shop-wallpaper.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
         "id": 48,
        "location": "Rizal",
        "restaurant_name": "Restaurant Fourty Eight",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/18854710/pexels-photo-18854710/free-photo-of-woman-browsing-the-menu-at-an-outdoor-restaurant-table.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
         "id": 49,
        "location": "Baguio",
        "restaurant_name": "Restaurant Fourty Nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }, {
         "id": 50,
        "location": "Boracay",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16997158/pexels-photo-16997158/free-photo-of-empty-seats-in-restaurant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    }
    
]



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
