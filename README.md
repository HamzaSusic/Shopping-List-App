# Python Shopping List Project

This web application is made usign Python, Flask, HTML, CSS, JS, and MySQL. It is a shopping list management tool. Users can create and save shopping lists for individual shoppers, adhering to the constraint that each item can be found in a maximum of three shopping lists.

## Table of Contents

- [Description](#description)
- [Installation](#installation)

## Description

This is a full-stack web application that displays a pre-populated list of shoppers (5) and shopping items (5). Users can create shopping lists for each shopper, with the limitation that each item can only appear in a maximum of three lists.


## Installation

To run the This application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/hamzasusic/Shopping-List-App
   ```
2. Navigate to the project directory:

   ```bash
   cd Shopping-List-App
   ```
3. Give the bash script permision to execute

   ```bash
   chmod +x setup.sh
   ```
4. Execute the script to install dependencies

   ```bash
   ./setup.sh
   ```
   It will run the following script

   ```bash
   #!/bin/bash

    # Create a virtual environment
    python3 -m venv .venv

    # Activate the virtual environment
    source .venv/bin/activate

    # Install Flask and Flask-Cors
    pip3 install Flask
    pip3 install Flask-Cors

    # Install mysql-connector-python
    pip3 install mysql-connector-python
   ```
5. Configure MySQL Database and edit the credentials at sql_connecter.py:

  Relationships:

  * Each Shopper can have multiple ShoppingLists.
  * Each ShoppingList is associated with one Shopper.
  * Each ShoppingList can have multiple ListItems.
  * Each ListItem is associated with one ShoppingList.
  * Each ListItem is associated with one Item.

6. Run the Flask application:

  ```bash
   FLASK_APP=server.py flask run
   ```

The application should now be running on http://localhost:4999












