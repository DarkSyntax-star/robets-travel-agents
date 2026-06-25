from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os

from app import models, database

# Create FastAPI app
app = FastAPI(title="SafariQuest Tours & Travel")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# ---------- Page Routes ----------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(database.get_db)):
    try:
        packages = db.query(models.TourPackage).all()
        return templates.TemplateResponse("index.html", {
            "request": request,
            "packages": packages,
            "page": "home"
        })
    except Exception as e:
        print(f"Error: {e}")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "packages": [],
            "page": "home"
        })

@app.get("/tours", response_class=HTMLResponse)
async def tours_page(request: Request, db: Session = Depends(database.get_db)):
    packages = db.query(models.TourPackage).all()
    return templates.TemplateResponse("tours.html", {
        "request": request,
        "packages": packages,
        "page": "tours"
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "page": "about"})

@app.get("/gallery", response_class=HTMLResponse)
async def gallery_page(request: Request):
    return templates.TemplateResponse("gallery.html", {"request": request, "page": "gallery"})

@app.get("/services", response_class=HTMLResponse)
async def services_page(request: Request):
    return templates.TemplateResponse("services.html", {"request": request, "page": "services"})

@app.get("/blog", response_class=HTMLResponse)
async def blog_page(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, "page": "blog"})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "page": "contact"})

@app.get("/booking", response_class=HTMLResponse)
async def booking_page(request: Request, db: Session = Depends(database.get_db)):
    packages = db.query(models.TourPackage).all()
    return templates.TemplateResponse("booking.html", {
        "request": request,
        "packages": packages,
        "page": "booking"
    })

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "page": "login"})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "page": "register"})

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request, db: Session = Depends(database.get_db)):
    packages = db.query(models.TourPackage).all()
    bookings = db.query(models.Booking).all()
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request,
        "packages": packages,
        "bookings": bookings
    })

# ---------- API Endpoints ----------
@app.post("/api/subscribe")
async def subscribe(request: Request, db: Session = Depends(database.get_db)):
    try:
        data = await request.json()
        email = data.get("email")
        if email:
            # Check if already subscribed
            existing = db.query(models.Subscriber).filter(models.Subscriber.email == email).first()
            if not existing:
                new_subscriber = models.Subscriber(email=email)
                db.add(new_subscriber)
                db.commit()
                return {"message": "Subscribed successfully!"}
            return {"message": "Already subscribed!"}
        return {"message": "Email is required"}, 400
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500

# ---------- Error Handlers ----------
@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.exception_handler(500)
async def server_error(request: Request, exc):
    return templates.TemplateResponse("500.html", {"request": request}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    