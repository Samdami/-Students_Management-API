# Students_Management-API
<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">


<!-- Project Name -->
<div align="center">
  <h1>Student API</h1>
</div>

<div>
  <p align="center">

  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-Student API">About Student API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>    
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Project -->
## About

It is a REST API which enables school staff to register accounts and manage student data on the Heroku-powered web app. CRUD operations can be carried out on the student data, with an easy-to-use Swagger UI setup for testing and integration with the front end.

Students have limited access to the app, as a student can only change their profile details and view their profile, courses, grades and CGPA.

This student management API was built with Python's Flask-RESTX

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Lessons Learned

Creating this API helped me learn and practice:
* API Development with Python
* App Deployment
* Testing
* Documentation
* Debugging
* Routing
* Database Management
* Internet Security
* User Authentication
* User Authorization

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- GETTING STARTED -->
## Usage

To use this API, follow these steps:

1. Create a heroku account

2. Create an admin or student account:
    - Click 'admin' to reveal a dropdown menu of administration routes, then register an admin account via the '/admin/register' route
    - Click 'students' to reveal a dropdown menu of student routes, then register a student account via the '/students/register' route

3. Sign in via the '/auth/login' route to generate a JWT token. Copy this access token without the quotation marks

4. Scroll up to click 'Authorize' at top right. Enter the JWT token 
   ```

5. Click 'Authorize' and then 'Close'

6. Now authorized, you can create, view, update and delete students, courses, grades and admins via the many routes in 'students', 'courses' and 'admin'. You can also get:
    - All students taking a course
    - All courses taken by a student
    - A student's grades in percentage (eg: 70%) and letters (eg: A)
    - A student's CGPA, calculated based on all grades from all courses they are taking

7. When you're done, click 'Authorize' at top right again to then 'Logout'



<p align="right"><a href="#readme-top">back to top</a></p>

---


<br />


---



<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)

<p align="right"><a href="#readme-top">back to top</a></p>

---

