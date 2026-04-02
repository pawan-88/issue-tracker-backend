from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import model, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)


# db dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create project thorugh this api
@app.post("/projects")
def create_project(project: schemas.ProjectCreate, db:Session = Depends(get_db)):
    db_project = model.project()
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# get all the project through api
@app.get("/projects")
def get_projects(db:Session = Depends(get_db)):
    return db.query(model.Project).all()

# create issue using this api
@app.post("/issues")
def create_issues(issue:schemas.IssueCreated, db:Session=Depends(get_db)):
    db_issue = model.Issue(**issue.dict())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

# get issue by project
@app.get("/project/{project_id}/issues")
def get_issues(project_id:int, db:Session = Depends(get_db)):
    return db.query(model.Issue).filter(model.Issue.project_id==project_id.all())


# update Issue Status
@app.put("/issues/{issue_id}/status")
def update_status(issue_id: int, status: str, db: Session = Depends(get_db)):
    issue = db.query(model.Issue).get(issue_id)
    issue.status = status
    db.commit()
    return issue

# Assign Issue
@app.put("/issues/{issue_id}/assign")
def assign_issue(issue_id: int, user_id: int, db: Session = Depends(get_db)):
    issue = db.query(model.Issue).get(issue_id)
    issue.assigned_to = user_id
    db.commit()
    return issue

# add Comment
@app.post("/issues/{issue_id}/comments")
def add_comment(issue_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = model.Comment(
        issue_id=issue_id,
        user_id=comment.user_id,
        message=comment.message
    )
    db.add(db_comment)
    db.commit()
    return db_comment

# get Comments
@app.get("/issues/{issue_id}/comments")
def get_comments(issue_id: int, db: Session = Depends(get_db)):
    return db.query(model.Comment).filter(model.Comment.issue_id == issue_id).all()