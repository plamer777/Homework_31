<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">    
  </head>
  <body>
    <h2 style="color: #26f3ff">Homework 29</h2>
    <p style="color: darkblue">This is a simple Django application that provides CRUD methods to interact with
    user, ads, location and category table.
</p>    
    <p><b>There are some newly added routes as follows:</b></p>
    <ul style="color: #c05000">      
      <li>location/ - get all location</li>
      <li>location/{id} - get location by id</li>
      <li>location/ (POST request) - add new location</li>
      <li>location/{id} (PUT request) - update existing location's data</li>
      <li>location/{id} (PATCH request) - partial update existing location's data</li>
      <li>location/{id} (DELETE request) - delete location from database</li>
    </ul>
    <p><b>The project's structure:</b></p>
    <ul class="routes">
      <li>ads - A Django app including views, models</li>
      <li>users - A Django app for user table</li>
      <li>locations - A Django app for location table</li>  
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
    <p style="color: darkblue">The project was created on February 16, 2023.</p>
  </body>
</html>