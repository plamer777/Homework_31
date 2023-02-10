<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">    
  </head>
  <body>
    <h2 style="color: #26f3ff">Homework 27</h2>
    <p style="color: darkblue">This is a simple Django application that provides CRUD methods to interact with
    user, ads and category table.
</p>
    <p><b>There were some routes in the previous version of the application:</b></p>
    <ul style="color: #c05000">
      <li>/ - main route with application's status</li>
      <li>ad/ - get all advertisements or place new one</li>
      <li>ad/{id} - get an advertisement by its id</li>
      <li>cat/ - get all categories or add new one</li>
      <li>cat/{id} - get single category by its id</li>
    </ul>
    <p><b>And there are some new routes as follows:</b></p>
    <ul style="color: #c05000">
      <li>/ad/create - creates new advertisement by provided data </li>
      <li>ad/{id}/update - updates existing advertisement</li>
      <li>ad/{id}/delete - allows to delete ad</li>
      <li>ad/{id}/upload_image/ - update an image of the existing advertisement</li>
      <li>cat/create - the same function but for categories</li>
      <li>cat/{id}/update - update category</li>
      <li>cat/{id}/delete - delete category</li>
      <li>user/ - get all users</li>
      <li>user/{id} - get users by id</li>
      <li>user/create - add new user in the database</li>
      <li>user/{id}/update - update existing user's data</li>
      <li>user/{id}/delete - delete user from database</li>
    </ul>
    <p><b>The project's structure:</b></p>
    <ul class="routes">
      <li>ads - A Django app including views, models</li>
      <li>users - A Django app for user and location tables</li>
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
    <p style="color: darkblue">The project was created on February 10, 2023.</p>
  </body>
</html>