<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">    
  </head>
  <body>
    <h2 style="color: #26f3ff">Homework 31</h2>
    <p style="color: darkblue">This is a simple Django application that provides CRUD methods to interact with
    user, ads, location, category and selection table.
</p>
    <p><b>There are some new features in this version:</b></p>
    <ul style="color: #c05000">      
      <li>unique "slug" field in the Category model</li>
      <li>"name" field of Ads model can't be less than 10 symbols and should not be blank</li>
      <li>from now a "price" value allowed only from 0 and above</li>
      <li>"is_published field initially should be false"</li>
      <li>User model have "birth_date" field and the registration restricted for users younger than 9 years old</li>
      <li>"email" field of User model have to be unique and 'rambler.ru' domain is restricted</li>
      <li>furthermore there were added some tests for ads and selections apps</li>
    </ul>
    <p><b>The new structure looks as follows:</b></p>
    <ul class="routes">
      <li>ads - A Django app including views, models</li>
      <li>users - A Django app for user table</li>
      <li>locations - A Django app for location table</li>
      <li>selections - A Django app for selection table</li>  
      <li>data - csv files with source data</li>
      <li>fixtures - prepared JSON files to upload data in the database</li>
      <li>media - uploaded images</li>
      <li>first_django - A main Django package</li>
      <li>tests - test package to test some features of the application</li>
      <li>constants.py - file containing constants such as paths to files</li>
      <li>manage.py - Django manage file</li>
      <li>poetry.lock - project's requirements</li>
      <li>pyproject.toml - the main poetry file</li>
      <li>utils.py - utility functions</li>
      <li>pytest.ini - pytest settings</li>
      <li>.gitignore - files and folders to exclude from git repository</li>
      <li>README.md - this file with project info</li>
    </ul>
    <p style="color: darkblue">The project was created on March 3, 2023 by Aleksey Mavrin</p>
  </body>
</html>