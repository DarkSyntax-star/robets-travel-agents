"""
seed_data.py - Add sample tour packages to the database
Run this file once to populate your database with example tours
"""

from app.database import SessionLocal, engine
from app.models import TourPackage, Base
from datetime import datetime

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create a database session
db = SessionLocal()

def seed_tours():
    """Add sample tour packages"""
    
    # Sample tour packages
    tours = [
        TourPackage(
            name="Gorilla Trekking",
            description="Bwindi Impenetrable Forest - encounter mountain gorillas in their natural habitat. This once-in-a-lifetime experience includes guided trekking through the rainforest.",
            price=2450.00,
            duration="4 days",
            destination="Bwindi, Uganda",
            image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Murchison Falls Safari",
            description="Experience the mighty Nile River and the powerful Murchison Falls. Enjoy game drives, boat cruises, and spectacular wildlife viewing.",
            price=1890.00,
            duration="3 days",
            destination="Murchison Falls, Uganda",
            image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Queen Elizabeth National Park Tour",
            description="Explore Uganda's most popular savannah park. Famous for tree-climbing lions, hippos, and over 600 bird species.",
            price=2100.00,
            duration="5 days",
            destination="Queen Elizabeth, Uganda",
            image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Bwindi Adventure",
            description="Deep jungle trekking in Bwindi Impenetrable Forest to see the endangered mountain gorillas. Includes accommodation and expert guides.",
            price=2800.00,
            duration="3 days",
            destination="Bwindi, Uganda",
            image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Nile River Cruise",
            description="Relaxing boat safari on the Nile River. See crocodiles, hippos, and colorful birds while enjoying the scenic river views.",
            price=950.00,
            duration="2 days",
            destination="Jinja, Uganda",
            image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Kidepo Valley Safari",
            description="Visit Uganda's most remote and spectacular national park. Home to large herds of elephants, lions, and unique bird species.",
            price=3200.00,
            duration="6 days",
            destination="Kidepo, Uganda",
            image_url="https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Lake Mburo Safari",
            description="Explore the only park in Uganda with zebras. Enjoy boat rides, game drives, and walking safaris in this scenic park.",
            price=1200.00,
            duration="2 days",
            destination="Lake Mburo, Uganda",
            image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&q=80",
            available=True
        ),
        TourPackage(
            name="Sipi Falls Trek",
            description="Hike through the beautiful Sipi Falls region. Experience stunning waterfalls, coffee plantations, and local village life.",
            price=750.00,
            duration="3 days",
            destination="Kapchorwa, Uganda",
            image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600&q=80",
            available=True
        )
    ]
    
    # Add all tours to the database
    for tour in tours:
        # Check if tour already exists (by name)
        existing = db.query(TourPackage).filter(TourPackage.name == tour.name).first()
        if not existing:
            db.add(tour)
            print(f"✅ Added: {tour.name}")
        else:
            print(f"⏭️ Skipped (already exists): {tour.name}")
    
    # Commit the changes
    db.commit()
    print(f"\n🎉 Sample tours added successfully!")
    print(f"📊 Total tours in database: {db.query(TourPackage).count()}")

def clear_tours():
    """Remove all tours from database (use with caution)"""
    confirm = input("⚠️ This will delete ALL tours. Are you sure? (yes/no): ")
    if confirm.lower() == 'yes':
        db.query(TourPackage).delete()
        db.commit()
        print("🗑️ All tours deleted!")

if __name__ == "__main__":
    print("🌍 SafariQuest - Database Seeder")
    print("=" * 40)
    print("1. Add sample tours")
    print("2. Clear all tours")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ")
    
    if choice == "1":
        seed_tours()
    elif choice == "2":
        clear_tours()
    else:
        print("👋 Goodbye!")
    
    # Close the database connection
    db.close()