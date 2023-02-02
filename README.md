<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Homework 27</title>
    <style>
      h2 {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
      }
      p {
        font-size: 18px;
        line-height: 1.5;
        text-align: justify;
        margin: 20px 0;
      }
      ul {
        list-style: none;
        margin: 0;
        padding: 0;
      }
      li {
        font-size: 18px;
        line-height: 1.5;
        margin: 10px 0;
      }
      .routes {
        margin-left: 40px;
      color: darkgoldenrod;  
      }
    </style>
  </head>
  <body>
    <h2 style="color: #26f3ff">Homework 27</h2>
    <p style="color: darkblue">This is a simple Django application that allows to interact with DB by using GET and POST requests.</p>
    <p><b>There are some routes in the application:</b></p>
    <ul style="color: #c05000">
      <li>/ - main route with application's status</li>
      <li>ad/ - get all advertisements or place new one</li>
      <li>ad/{id} - get an advertisement by its id</li>
      <li>cat/ - get all categories or add new one</li>
      <li>cat/{id} - get single category by its id</li>
    </ul>
    <p><b>The project's structure:</b></p>
    <ul class="routes">
      <li>ads - A Django app including views, models</li>
      <li>data - csv files with source data</li>
      <li>first_django - A main Django package</li>
      <li>constants.py - file containing constants such as paths to files</li>
      <li>manage.py - Django manage file</li>
      <li>poetry.lock - project's requirements</li>
      <li>pyproject.toml - the main poetry file</li>
      <li>utils.py - utility functions</li>
      <li>.gitignore - files and folders to exclude from git repository</li>
      <li>README.md - this file with project info</li>
    </ul>
    <p style="color: darkblue">The project was created on February 2, 2023.</p>
  </body>
</html>