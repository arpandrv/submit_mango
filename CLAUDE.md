# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Run Commands
- Start development server: `python mango_project/manage.py runserver`
- Run all tests: `python mango_project/manage.py test mango_app`
- Run single test: `python mango_project/manage.py test mango_app.tests.MangoAppViewTests.test_home_view`
- Collect static files: `python mango_project/manage.py collectstatic`
- Make migrations: `python mango_project/manage.py makemigrations`
- Apply migrations: `python mango_project/manage.py migrate`

## Code Style Guidelines
- **Imports**: Standard library first, Django imports second, local imports third
- **Indentation**: 4 spaces
- **Naming**: Classes use PascalCase, functions/variables use snake_case
- **Docstrings**: Every function should have a docstring explaining purpose and parameters
- **Error handling**: Use try/except blocks with specific exceptions
- Use Django's built-in test client for view testing
- Follow the Django template inheritance pattern using base.html
- Keep view logic separate from data models
- Follow existing patterns in similar files when creating new code
- Maintain consistent active menu tracking in context processors