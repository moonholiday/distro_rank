# Linux Distribution Ranking Web App

## Overview

A full-stack web app to rank and compare Linux distributions using React, Django, and Chakra UI for styling.

## Features

- User-friendly interface for ranking and comparing Linux distributions.
- Details about distributions' features, popularity, and performance.
- User ratings and reviews.
- Integration with Django backend.
- Admin panel for data management.

## Tech Stack

- Frontend: React with Chakra UI.
- Backend: Django.
- Database: SQLite (for development).
- State Management: Redux (optional).
- API Requests: Axios.
- Authentication: Django Authentication (future enhancement).

## Components

- DistroList: Lists distributions.
- DistroDetail: Displays distribution details.
- DistroRating: Allows rating and reviewing.
- AdminPanel: Data management.
- Navigation & User Authentication (future enhancement).

## Data Flow

1. User interacts with the intuitive interface.
2. React fetches distribution data from Django API.
3. Users view info, rate distributions, and leave reviews.
4. Ratings and reviews are stored in the backend's database.
5. Admins manage data through the Django admin.

## Setup

1. Clone repo: `git clone <repository-url>`
2. Set up Django backend:
   - Install dependencies: `pip install -r requirements.txt`
   - Migrate: `python manage.py migrate`
   - Create superuser: `python manage.py createsuperuser`
   - Run server: `python manage.py runserver`
3. Set up React frontend:
   - Go to frontend dir: `cd frontend`
   - Install deps: `yarn install`
   - Run dev server: `yarn start`

## Future

- User auth and features.
- Enhanced UI with Chakra UI.
- Integration with external APIs.
- Search and filtering options.
- Performance optimization.

For the latest info, check the repository and documentation.

