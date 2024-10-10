# Django AdminLTE

This project is a Django starter based on the AdminLTE theme, with custom modifications. It provides a ready-to-use admin interface with improved authentication flows and a customized landing page.

## Recent Changes

1. Restructured the project, renaming the `home` app to `adminlte` app.
2. Added a new `index` app to handle the landing page and other custom pages.
3. Customized the landing page (`landing.html`) with new design and content.
4. Added a reusable footer in `landing_base.html` to improve code reusability.
5. Updated account-related templates, including login and registration pages.
6. Added new static resources, including images and style files.
7. Updated the project's URL configuration to accommodate the new structure.
8. Modified `settings.py`, adjusting the app list and other configurations.
9. Improved password reset functionality with custom views and templates.
10. Unified the style across all authentication pages (login, registration, password reset).

## How to Run the Project

1. Clone the repository:
   ```
   git clone https://github.com/tpstudy/django-adminlte.git
   cd django-adminlte
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and set the appropriate values for your environment.

5. Run database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Visit http://127.0.0.1:8000 in your browser

## Notes

- This project is a customized version of the Django starter based on the AdminLTE theme.
- The original `home` app has been renamed to `adminlte` app to better reflect its purpose.
- Authentication pages (login, registration, password reset) now have a consistent style.
- Make sure to change the `SECRET_KEY` and disable debug mode before deploying to a production environment.
- Email settings need to be configured for password reset functionality to work properly.

## Contributing

If you have any suggestions or find a bug, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project is based on work by AppSeed, with modifications and improvements by TideP. For more information about licensing and usage, please refer to the LICENSE file.
