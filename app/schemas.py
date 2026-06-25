from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

class TourPackageBase(BaseModel):
    name: str
    description: str
    price: float
    duration: str
    destination: str
    image_url: str

class TourPackageCreate(TourPackageBase):
    pass

class TourPackage(TourPackageBase):
    id: int
    available: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    travelers: int
    travel_date: datetime
    notes: Optional[str] = None

class BookingCreate(BookingBase):
    package_id: int

class Booking(BookingBase):
    id: int
    user_id: Optional[int]
    package_id: int
    status: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class BlogPostBase(BaseModel):
    title: str
    content: str
    image_url: str
    author: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True

class GalleryImageBase(BaseModel):
    title: str
    category: str
    image_url: str

class GalleryImage(GalleryImageBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class SubscriberBase(BaseModel):
    email: EmailStr

class Subscriber(SubscriberBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True