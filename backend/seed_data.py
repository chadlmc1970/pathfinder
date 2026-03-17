"""Seed database with Louisiana career data"""
import asyncio
from app.core.database import SessionLocal
from app.models.career import Career
from app.models.video import Video

LOUISIANA_CAREERS = [
    {
        "title": "Petroleum Engineer",
        "industry_sector": "Energy",
        "description": "Design and develop methods for extracting oil and gas from Louisiana's offshore and onshore deposits",
        "salary_range_min": 85000,
        "salary_range_max": 150000,
        "education_required": "Bachelor's in Petroleum Engineering",
        "skills": ["Mathematics", "Physics", "Problem-solving", "Computer modeling"],
        "pathway": {
            "high_school": ["Advanced Math", "Physics", "Chemistry"],
            "college": "Louisiana State University - Pete Department",
            "certifications": ["PE License (after 4 years experience)"]
        }
    },
    {
        "title": "Chef / Culinary Artist",
        "industry_sector": "Hospitality",
        "description": "Create authentic Louisiana cuisine in restaurants, hotels, or catering. Preserve Creole and Cajun food traditions",
        "salary_range_min": 35000,
        "salary_range_max": 75000,
        "education_required": "Culinary School or Apprenticeship",
        "skills": ["Cooking", "Creativity", "Time management", "Food safety"],
        "pathway": {
            "high_school": ["Culinary Arts programs", "Family & Consumer Sciences"],
            "college": "Delgado Culinary Arts or Nicholls State",
            "certifications": ["ServSafe", "ACF Certification"]
        }
    },
    {
        "title": "Marine Biologist",
        "industry_sector": "Science",
        "description": "Study Louisiana's unique coastal ecosystems, wetlands restoration, and Gulf marine life",
        "salary_range_min": 50000,
        "salary_range_max": 95000,
        "education_required": "Bachelor's or Master's in Marine Biology",
        "skills": ["Research", "Data analysis", "Scuba diving", "Field work"],
        "pathway": {
            "high_school": ["Biology", "Chemistry", "Environmental Science"],
            "college": "LSU, Tulane, or UNO Marine Sciences",
            "certifications": ["AAUS Scientific Diver"]
        }
    },
    {
        "title": "Nurse Practitioner",
        "industry_sector": "Healthcare",
        "description": "Provide primary care in Louisiana's hospitals, clinics, and rural communities",
        "salary_range_min": 95000,
        "salary_range_max": 125000,
        "education_required": "Master's in Nursing",
        "skills": ["Patient care", "Diagnosis", "Communication", "Empathy"],
        "pathway": {
            "high_school": ["Biology", "Health Science programs"],
            "college": "LSU Health, Tulane, or Xavier Nursing",
            "certifications": ["RN License", "NP Certification"]
        }
    },
    {
        "title": "Port Operations Manager",
        "industry_sector": "Logistics",
        "description": "Oversee cargo operations at Port of New Orleans or Port of South Louisiana",
        "salary_range_min": 70000,
        "salary_range_max": 110000,
        "education_required": "Bachelor's in Logistics or Business",
        "skills": ["Leadership", "Logistics", "Problem-solving", "Safety protocols"],
        "pathway": {
            "high_school": ["Business", "Math", "Leadership programs"],
            "college": "UNO Maritime Transportation or LSU Business",
            "certifications": ["OSHA Safety", "Customs certifications"]
        }
    },
    {
        "title": "Oil Rig Technician",
        "industry_sector": "Energy",
        "description": "Maintain and repair drilling equipment on offshore rigs in the Gulf of Mexico",
        "salary_range_min": 55000,
        "salary_range_max": 90000,
        "education_required": "High School + Technical training",
        "skills": ["Mechanical repair", "Safety awareness", "Physical stamina", "Teamwork"],
        "pathway": {
            "high_school": ["Industrial Tech", "Welding", "Mechanical courses"],
            "college": "Louisiana Delta Community College - Petroleum Tech",
            "certifications": ["OSHA 30", "H2S Alive", "Rigging"]
        }
    },
    {
        "title": "Jazz Musician",
        "industry_sector": "Arts",
        "description": "Perform in New Orleans' world-famous music scene - clubs, festivals, studio sessions",
        "salary_range_min": 25000,
        "salary_range_max": 80000,
        "education_required": "Music training or self-taught",
        "skills": ["Instrument mastery", "Improvisation", "Collaboration", "Performance"],
        "pathway": {
            "high_school": ["Band", "Music theory", "Private lessons"],
            "college": "UNO Jazz Studies or Loyola Music",
            "certifications": ["None - talent and network matter most"]
        }
    },
    {
        "title": "Coastal Restoration Engineer",
        "industry_sector": "Environment",
        "description": "Design projects to rebuild Louisiana's disappearing coastline and protect communities",
        "salary_range_min": 65000,
        "salary_range_max": 105000,
        "education_required": "Bachelor's in Civil or Environmental Engineering",
        "skills": ["Engineering design", "Environmental science", "Project management", "GIS"],
        "pathway": {
            "high_school": ["Advanced Math", "Physics", "Environmental Science"],
            "college": "LSU, UL Lafayette, or Tulane Engineering",
            "certifications": ["PE License", "Wetland delineation"]
        }
    },
    {
        "title": "Casino Dealer",
        "industry_sector": "Gaming",
        "description": "Work in Louisiana's riverboat casinos dealing blackjack, poker, or craps",
        "salary_range_min": 25000,
        "salary_range_max": 45000,
        "education_required": "High School + Dealer training",
        "skills": ["Math", "Customer service", "Focus", "Hand dexterity"],
        "pathway": {
            "high_school": ["Math", "Customer service jobs"],
            "college": "Dealer school (4-8 weeks)",
            "certifications": ["Louisiana Gaming License"]
        }
    },
    {
        "title": "Fisheries Manager",
        "industry_sector": "Agriculture",
        "description": "Manage Louisiana's commercial fishing industry and sustainable seafood practices",
        "salary_range_min": 48000,
        "salary_range_max": 75000,
        "education_required": "Bachelor's in Marine Biology or Fisheries Science",
        "skills": ["Biology", "Data analysis", "Regulation knowledge", "Communication"],
        "pathway": {
            "high_school": ["Biology", "Environmental Science", "Math"],
            "college": "LSU School of Renewable Natural Resources",
            "certifications": ["Louisiana Master Naturalist"]
        }
    },
    {
        "title": "Chemical Plant Operator",
        "industry_sector": "Manufacturing",
        "description": "Operate processing equipment at petrochemical plants along the Mississippi River",
        "salary_range_min": 60000,
        "salary_range_max": 95000,
        "education_required": "High School + Plant training",
        "skills": ["Technical aptitude", "Safety protocols", "Problem-solving", "Attention to detail"],
        "pathway": {
            "high_school": ["Chemistry", "Math", "Industrial Tech"],
            "college": "Louisiana Delta or Baton Rouge Community College - Process Tech",
            "certifications": ["OSHA 30", "Process Safety Management"]
        }
    },
    {
        "title": "Tourism Marketing Specialist",
        "industry_sector": "Hospitality",
        "description": "Promote Louisiana tourism - festivals, cuisine, culture, and heritage sites",
        "salary_range_min": 42000,
        "salary_range_max": 70000,
        "education_required": "Bachelor's in Marketing or Communications",
        "skills": ["Marketing", "Social media", "Creativity", "Cultural knowledge"],
        "pathway": {
            "high_school": ["Business", "Marketing", "Communications"],
            "college": "LSU, UL Lafayette, or Loyola Marketing",
            "certifications": ["Google Analytics", "HubSpot certifications"]
        }
    },
    {
        "title": "Paramedic",
        "industry_sector": "Healthcare",
        "description": "Provide emergency medical care in ambulances and emergency scenes across Louisiana",
        "salary_range_min": 38000,
        "salary_range_max": 58000,
        "education_required": "Paramedic certification program",
        "skills": ["Emergency medicine", "Quick thinking", "Physical fitness", "Compassion"],
        "pathway": {
            "high_school": ["Biology", "Health Science", "EMT training"],
            "college": "Delgado or BPCC Paramedic program (1-2 years)",
            "certifications": ["EMT-Paramedic License"]
        }
    },
    {
        "title": "Video Game Developer",
        "industry_sector": "Technology",
        "description": "Create games and software at Louisiana's growing tech companies (tax incentives attract studios)",
        "salary_range_min": 55000,
        "salary_range_max": 110000,
        "education_required": "Bachelor's in Computer Science or Game Design",
        "skills": ["Programming", "Creativity", "Problem-solving", "Teamwork"],
        "pathway": {
            "high_school": ["Computer Science", "Math", "Digital Media"],
            "college": "LSU, Tulane, or Louisiana Tech Computer Science",
            "certifications": ["Unity", "Unreal Engine certifications"]
        }
    },
    {
        "title": "Shrimp Boat Captain",
        "industry_sector": "Agriculture",
        "description": "Captain a commercial shrimping vessel in Louisiana's coastal waters",
        "salary_range_min": 40000,
        "salary_range_max": 80000,
        "education_required": "High School + Maritime experience",
        "skills": ["Navigation", "Mechanical repair", "Fishing techniques", "Business management"],
        "pathway": {
            "high_school": ["Work on family boats", "Vocational maritime programs"],
            "college": "USCG Captain's License courses",
            "certifications": ["USCG Captain's License", "Commercial Fishing License"]
        }
    },
    {
        "title": "Elementary School Teacher",
        "industry_sector": "Education",
        "description": "Teach K-5 students in Louisiana public or charter schools",
        "salary_range_min": 45000,
        "salary_range_max": 65000,
        "education_required": "Bachelor's in Education + Teaching certification",
        "skills": ["Patience", "Communication", "Creativity", "Classroom management"],
        "pathway": {
            "high_school": ["Education programs", "Volunteer tutoring"],
            "college": "Any Louisiana university - Education major",
            "certifications": ["Louisiana Teaching Certificate"]
        }
    },
    {
        "title": "Electrician",
        "industry_sector": "Skilled Trades",
        "description": "Install and maintain electrical systems in homes, businesses, and industrial sites",
        "salary_range_min": 48000,
        "salary_range_max": 85000,
        "education_required": "Apprenticeship program",
        "skills": ["Electrical theory", "Problem-solving", "Safety", "Manual dexterity"],
        "pathway": {
            "high_school": ["Physics", "Math", "Industrial Tech"],
            "college": "Apprenticeship (4 years) with IBEW or ABC",
            "certifications": ["Journeyman License", "Master Electrician"]
        }
    },
    {
        "title": "Wildlife Biologist",
        "industry_sector": "Science",
        "description": "Study and protect Louisiana's unique wildlife - alligators, pelicans, black bears",
        "salary_range_min": 45000,
        "salary_range_max": 75000,
        "education_required": "Bachelor's in Wildlife Biology",
        "skills": ["Research", "Field work", "Data analysis", "Conservation"],
        "pathway": {
            "high_school": ["Biology", "Environmental Science", "Statistics"],
            "college": "LSU, UL Lafayette, or Southeastern Wildlife",
            "certifications": ["IACUC certification", "Wilderness First Aid"]
        }
    },
    {
        "title": "Cybersecurity Analyst",
        "industry_sector": "Technology",
        "description": "Protect Louisiana businesses and government from cyber threats",
        "salary_range_min": 65000,
        "salary_range_max": 115000,
        "education_required": "Bachelor's in Cybersecurity or IT",
        "skills": ["Network security", "Threat analysis", "Problem-solving", "Continuous learning"],
        "pathway": {
            "high_school": ["Computer Science", "Math", "Coding clubs"],
            "college": "LSU, Louisiana Tech, or UL Lafayette Cyber",
            "certifications": ["Security+", "CEH", "CISSP"]
        }
    },
    {
        "title": "Construction Manager",
        "industry_sector": "Construction",
        "description": "Oversee building projects - homes, schools, hurricane recovery, infrastructure",
        "salary_range_min": 72000,
        "salary_range_max": 125000,
        "education_required": "Bachelor's in Construction Management",
        "skills": ["Leadership", "Project management", "Problem-solving", "Communication"],
        "pathway": {
            "high_school": ["Math", "Business", "Drafting"],
            "college": "LSU, Louisiana Tech, or UL Monroe Construction",
            "certifications": ["OSHA 30", "PMP"]
        }
    }
]

def seed_careers():
    """Insert careers into database"""
    db = SessionLocal()
    try:
        # Clear existing data
        db.query(Career).delete()
        db.commit()

        # Insert careers
        for career_data in LOUISIANA_CAREERS:
            career = Career(**career_data)
            db.add(career)

        db.commit()
        print(f"✅ Seeded {len(LOUISIANA_CAREERS)} Louisiana careers")

        # Create placeholder videos
        careers = db.query(Career).all()
        for career in careers[:5]:  # First 5 get videos
            video = Video(
                career_id=career.id,
                blob_url=f"https://placeholder.com/video/{career.id}",
                thumbnail_url=f"https://placeholder.com/thumb/{career.id}.jpg",
                duration_seconds=45
            )
            db.add(video)

        db.commit()
        print(f"✅ Added 5 placeholder videos")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_careers()
