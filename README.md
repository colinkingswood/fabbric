## Running the app
I set up a docker compose file in the top level directory, so it should be a case of running
(make sure you don't have anything running on ports `8000` or `3000` as this may cause problems)


```sh
docker compose up -- build
```

You should be able to go to [http://localhost:3000/](http://localhost:3000/) to see the simple web app.  I tested in on Firefox and Chromium on Linux. 

You should be able to run the tests by opening another terminal 

```sh
docker compose up -- build
```

for the backend tests
```sh
docker exec -it fabbric-backend-1 python manage.py test
```

for the frontend tests
```sh
docker exec -it fabbric-frontend-1 npm test
```


## Discusion

Initially I had thought of storing images as some kind of vector format (SVG came to mind) in the database, that way we could have multiple parts or layers, and changing colour of each of the items would be fairly straight forward. I looked about for some examples, but after sepnding a  bit of time I didn't find much suitable.

I ended up asking for some example data, which was white / greyscale png format, with transparent background. 

I looked into converting the color on the frontend, but it looked more complicated than doing it in Python and pillow, and I am more comfortable with backend code in general. Doing it in the backend would also allow for saving customized versions, given more time, though there is a small delay.

### backend
I did this in Django, with Django Rest Framework and uses SQLite as the database for simplicity.

The code is in `prototype` directory.  

There is one model at present in `models.py` `ClothingItem`. This could be expanded into a one-to-many `ItemImages`, if we want different version, such as side images and reverse etc. This is teh sort of thing I would usually discuss in advance, to clarify the requirements.

I used DjangoRestFramework with a viewset for the list view - to get all the items and an extra endpoint `customize_color`, where the request takes a hex color and returns a customized version of the image in that color as base64 encoded image. This is in `views.py`. 

I added thumbnails for the list view using the sorl-thubnail package. This will generate and cache thumbnails. This is done in `seralizers.py.`

There are some tests to check the list view. And the customize_color endpoint. More detailed tests could be added to check the color of the customzed item, but that was likeley to quite time consuming 

### frontend

I made a very basic React application, with the list of items (it still need pagination, or the ability to deal with larger lists added). 
The user can select an item, then select a color, this will make a request to the backend and return the customized.

The frontend code is in the `frontend/` directory, in `src/App.js`, the tests ate in `src/App.test.js`


Obviously there is a lot more that could be added, the obvious one being pagination  for larger datasets. 



