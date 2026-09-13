# Publication system project

# Publishing System

## Overview
Publishing System is a web platform designed to manage academic articles and the peer review process.  
It supports the full publication cycle: from article submission by authors, through review by peers, to editorial decisions and final publishing.  
The functionality is described in general terms and can be extended with new modules in the future.

## General Features
- User registration and profiles.
- User roles: Authors, Reviewers, Editors.
- Article submission and status management.
- Assignment of reviewers to publications.
- Collection of comments and revisions.
- User activity log (ChangeLog).

## Project Structure
- `publication_system/` — main Django module and configuration.
- `accounts/` — user profiles, roles, activity log.
- `publications/` — article models, statuses, revisions.
- `staticfiles/` — collected static assets.

## Launch Instructions
1. Clone the repository:
```bash
git clone https://github.com/NaniGabber/dp_publication_system.git
cd publication_system
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the web interface at:
```bash
http://localhost:8000
```

## Technologies
- Backend: Django (Python)
- Database: PostgreSQL
- Containerization: Docker, Docker Compose
- Frontend: Django templates (extendable)