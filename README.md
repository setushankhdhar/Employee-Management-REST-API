# Employee-Management-REST-API
This project is a Django REST Framework–based backend application for managing companies and their employees.
It provides clean REST APIs along with the Django Admin panel and DRF’s browsable API, making it easy to manage and test data directly from the browser.

The project was built to understand real-world backend concepts like relational models, RESTful design, and API versioning.

# What this project does
-Stores company information (name, location, type, etc.)
-Stores employee information and links each employee to a company
-Allows viewing and managing data through:
  -Django Admin panel
  -Django REST Framework browsable API
-Provides structured and versioned REST endpoints

# Features
-Create, read, update, and delete companies
-Create, read, update, and delete employees
-Each employee is linked to a company
-Nested API to view all employees of a specific company
-Django Admin dashboard for easy management
-DRF browsable API for interactive testing
-Clean and simple API structure using /api/v1/

# API Endpoints
## Companies
GET /api/v1/companies/ – list all companies
POST /api/v1/companies/ – create a company
GET /api/v1/companies/{id}/ – get company details
PUT /api/v1/companies/{id}/ – update company
DELETE /api/v1/companies/{id}/ – delete company

## Employees
GET /api/v1/employees/ – list all employees
POST /api/v1/employees/ – create an employee
GET /api/v1/employees/{id}/ – employee details
PUT /api/v1/employees/{id}/ – update employee
DELETE /api/v1/employees/{id}/ – delete employee

Nested Route
GET /api/v1/companies/{id}/employees/ – employees of a company

# Clone the repository
git clone https://github.com/setushankhdhar/Employee-Management-REST-API.git

# Move into the project directory
cd Employee-Management-REST-API

# (Optional but recommended) Create virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver


# output
<img width="1910" height="915" alt="screenshot-1767953941197" src="https://github.com/user-attachments/assets/38d8ccc5-3189-4e9d-ab93-1e244daa1750" />
<img width="1910" height="915" alt="screenshot-1767953629654" src="https://github.com/user-attachments/assets/bb2190f3-0982-4b0c-9276-6ac3806ae41c" />
<img width="1910" height="915" alt="screenshot-1767953650717" src="https://github.com/user-attachments/assets/66707505-bc7c-4edb-8130-32e24cfda87c" />
<img width="1910" height="915" alt="screenshot-1767953721806" src="https://github.com/user-attachments/assets/7f361481-6d4c-42a0-ad1c-381b0e0b7c06" />

