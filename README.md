# Django AdminLTE

This project is a Django starter based on the AdminLTE theme, with custom modifications. It provides a ready-to-use admin interface with improved authentication flows and a customized landing page.

## Recent Changes

1. **New INDEX App**: 
   - Handles the default landing page display
   - Includes common website templates for developers to easily populate with their own content
   - Created a base template langding_base.html for the website's frontend
   - Facilitates the development of additional pages for the website's public-facing side

2. **Code Reorganization**:
   - Example code moved from the virtual environment to the project directory
   - Allows developers to more easily modify and learn from the code

3. **Optimized APP Structure**:
   - Original HOME app split into accounts app and adminlte app
   - accounts app: Manages user login, registration, profile editing, etc.
   - adminlte app: Showcases various AdminLTE component examples

4. **Enhanced User Management**:
   - New personal information editing page
   - Rewritten password reset process
   - For easier debugging, email operations are displayed in the terminal
   - Developers can configure email servers based on their needs


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

This project is based on work by AppSeed, with modifications and improvements by TPSTUDY. For more information about licensing and usage, please refer to the LICENSE file.
