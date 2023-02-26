<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">    
  </head>
  <body>
    <h2 style="color: #26f3ff">Homework 30</h2>
    <p style="color: darkblue">This is a simple Django application that provides CRUD methods to interact with
    user, ads, location, category and selection table.
</p>    
    <p><b>In this version were added new routes such as:</b></p>
    <ul style="color: #c05000">      
      <li>selection/ - get all selections</li>
      <li>selection/{id} - get selection by id</li>
      <li>selection/ (POST request) - add new selection</li>
      <li>selection/{id} (PUT request) - update existing selection</li>
      <li>selection/{id} (PATCH request) - partial update existing selection's data</li>
      <li>selection/{id} (DELETE request) - delete selection from database</li>
    </ul>
    <p><b>The project's structure:</b></p>
    <ul class="routes">
      <li>ads - A Django app including views, models</li>
      <li>users - A Django app for user table</li>
      <li>locations - A Django app for location table</li>
      <li>selections - A Django app for selection table</li>  
      <li>data - csv files with source data</li>
      <li>fixtures - prepared JSON files to upload data in the database</li>
      <li>media - uploaded images</li>
      <li>first_django - A main Django package</li>
      <li>constants.py - file containing constants such as paths to files</li>
      <li>manage.py - Django manage file</li>
      <li>poetry.lock - project's requirements</li>
      <li>pyproject.toml - the main poetry file</li>
      <li>utils.py - utility functions</li>
      <li>.gitignore - files and folders to exclude from git repository</li>
      <li>README.md - this file with project info</li>
    </ul>
    <p style="color: darkblue">The project was created on February 26, 2023 by Aleksey Mavrin</p>
  </body>
</html>