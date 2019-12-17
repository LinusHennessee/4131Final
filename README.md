# 4131Final

1. Project Type: Plan B
2. Group Members Name: Linus Hennessee and Kelsey Frenzel
3. Link to live Application: https://app4131final.herokuapp.com/index
4. Link to Github Code Repository: https://github.com/LinusHennessee/4131Final
5. List of Technologies/API's Used: https://iro.js.org/, flask_table, WTForms, SQLAlchemy
6. Detailed Description of the project: Our project is a Band Generator. The user inputs an already existing band name or one that they make up themselves, then they will choose primary and secondary colors using the color picker api for the band's poster colors. After this, they will select from the drop down menus to choose a singer, bassist, drummer, and guitarist for their desired band. Once the user hits submit, the app will go to the next page where the user will be shown a small poster for their generated band and a table of previously generated bands from other users. Here the user can view the posters of the previously generated bands by clicking on the bands names. 
7. List of Controllers and their short description: 
	/index which is for the first page and sets the form fields using the BandForm class.
	/band which is for the second page that adds the current user's generated band to the sql database and creates a table of the sql database to display on the displayBand.html page of the app.
8. List of Views and their short description:
	nameGenerator.html is a form for the user to input their desired data into using a textbox, the color selector api, and some drop down menus.
	displayBand.html takes the user's data and generates a simple poster with the band name that the user came up with, the selected musicians, and the primary color for the background color and the secondary color for the text and border colors. There is also a table below this poster that displays the sql database and is interactive so it allows the user to select previously generated bands and display their posters.
9. List of Tables, their Structure and short description:
	'thebands': 7 columns holding user created band name, primary and secondary color as chosen with the color picker api, the singer, guitarist, bassist and drummer all stored in that order. 
10. References/Resources: flask-table.readthedocs.io/en/stable/, iro.js.org, w3schools.com, runestone.academy, flask-sqlalchemy.palletsprojects.com/en/2.x/
