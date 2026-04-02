Issue Tracking System (Backend)

A simple Issue Tracking System built using FastAPI and SQLAlchemy, similar to a lightweight version of Jira or GitHub Issues.

Features
Create and manage projects
Create and manage issues within projects
Assign issues to users
Update issue status
Add comments to issues
Retrieve project and issue details

Tech Stack
Backend Framework: FastAPI
Database: SQLite (can be replaced with PostgreSQL)
ORM: SQLAlchemy
Validation: Pydantic


Project Structure

backend/
├── main.py
├── database.py
├── models.py
├── schemas.py


API Endpoints
Project APIs
POST /projects → Create project
GET /projects → Get all projects
Issue APIs
POST /issues → Create issue
GET /projects/{project_id}/issues → Get issues by project
PUT /issues/{issue_id}/status → Update issue status
PUT /issues/{issue_id}/assign → Assign issue
Comment APIs
POST /issues/{issue_id}/comments → Add comment
GET /issues/{issue_id}/comments → Get comments
