# PROJECT sundry

A multi-feature application with a Flask backend and a Vue 3 + TypeScript frontend. 

#### Description:
This project is pretty self explanatory once you run the program.
So, I'll describe it in simple language.

## Features 

At first it will show a page with a tab menu of functions it can perform: 

1 color effect on photo
2 book suggestion as per genre of book
3 match two texts for similarity
4 generate qrcode for some data or a site

## Technologies
- Backend: Python, Flask
- Frontend: Vue 3, Vite, TypeScript
- Other: Axios, CORS, Pillow, fuzzywuzzy, BeautifulSoup

## Folder Structure 
PROJECT-sentry/
├── backend/          # Flask app and Python logic
├── frontend/         # Vue 3 + Vite frontend
├── .gitignore 
└── README.md

## setup 

 backend:

cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt 
cp .env.example .env (for environment setup, update values as needed) 
python app.py 
(to come out of venv after stopping the code, run: deactivate)

 frontend: 

cd frontend 
cp .env.example .env (for environment setup, update or set your URL for backend if needed) 
npm install
npm run dev


| Method | Endpoint         | Description                     |
|--------|------------------|---------------------------------|
| POST   | `/compare`       | Compare two text strings        |
| POST   | `/books`         | Book recommendation by genre    |
| POST   | `/color-filter`  | Apply image color filters       |
| POST   | `/qrcode`        | Generate QR codes               | 

# screenshots of ui design 

PROJECT-sundry/frontend/src/assets/designs/ 

# contributing? 

Thank you for thinking to contribute. 
If you want to contribute, fork the main branch (not master), make a different branch based on the main branch, make your changes, check if everything is working correctly, and then raise a pull request (to main, not master) 

# possible debugs 
- if showing any warnings related to python-Levenshtein and you don't want it, run: 
  pip install python-Levenshtein 
- if you are running in github codespaces and there are cors issues, run in local or made the ports public 
- if some generated image in new tab not loading or showing 404 error, just reload the page  



# Functions:

color effect

This function again provides a menu of the effects available to choose from.

e.g.
1 green
2 blue
3 grey
4 purple

also, upload the image and choose a name for your newly generated image and hit thr button generate. 

The function includes a filter numpy array. The filter array is then applied on the image array.
The new filtered image is then showed. 


book suggestion as per genre

It asks the user for a genre they want books suggested on.
Then requests Goodreads for the books. Then provides the book names.


match two texts for similarity

It asks the users for two texts that they want to match respectively.
It then makes three types of ratio (ratio, partial ratio, token sort ratio) from the texts and provides them as percentage for better understanding. It can be used in case of plagiarism in case one thinks two texts are similar.


generate qr code for data or a site

It asks the user for the data or site.
Then it asks the user if they want particular colors for the qr code, asks the user for fill color and back color and generates qr code. 
