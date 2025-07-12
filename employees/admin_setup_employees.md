# Django Admin Configuration for Employees Model

## Registration
The `Employees` model is registered in `bookshelf/admin.py` using the `@admin.register(Employees)` decorator.

## Admin Customizations

### `list_display`
Displays these fields in the admin list view:
- sur_name
- first_name
- other_name
- date_of_birth 
- phone_number
- email
- address

### `search_fields`
Allows searching employees by:
- Name fields
- Email
- Phone number

### `list_filter`
Provides filter sidebar by:
- date_of_birth

## Admin Access
To manage employee records:
1. Run the server: `python manage.py runserver`
2. Visit `/admin`
3. Log in with your superuser credentials
