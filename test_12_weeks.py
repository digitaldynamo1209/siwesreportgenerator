import os
from app.models import SIWESReportPayload, StudentPlacementInfo, WeeklyActivity, ProblemResolution, ReferenceItem
from app.ai_generator import SIWESAIEngine
from app.docx_generator import create_siwes_document

def test_12_week_report():
    print("Testing 12-Week (SIWES I / 300 Level) Report Generation...")
    payload = SIWESReportPayload(
        student_info=StudentPlacementInfo(
            full_name="OGUNDELE, Boluwatife David",
            matric_number="22/ENG05/019",
            department="Mechanical Engineering",
            college="College of Engineering",
            institution="Landmark University, Omu-Aran, Kwara State",
            level="300 Level",
            org_name="Nigerian Breweries Plc",
            org_address="Abebe Village Road, Iganmu, Lagos State",
            org_industry="Industrial Brewing, Packaging & Utilities Engineering",
            industry_supervisor="Engr. Charles Nwosu (Senior Packaging Engineer)",
            academic_supervisor="Dr. M. A. Adebayo",
            siwes_officer="Engr. (Mrs.) F. E. Babatunde",
            hod_name="Prof. J. K. Adewumi",
            start_date="June 2026",
            end_date="September 2026",
            siwes_type="SIWES I",
            duration_weeks=12
        ),
        org_history_raw="Nigerian Breweries Plc is the pioneer and largest brewing company in Nigeria.",
        department_placed="Plant Utilities & Packaging Maintenance Unit",
        reporting_line="Reported to the Shift Operations Engineer and Packaging Line Superintendent",
        weekly_activities=[
            WeeklyActivity(
                week_number=1,
                date_range="1st June - 5th June 2026",
                department_unit="HSE & Induction",
                activities="Completed statutory safety induction, LOTO procedures, PPE fitting, and plant familiarization.",
                skills_tools="PPE, LOTO safety padlocks, hazard inspection sheets"
            )
        ],
        problems_resolutions=[
            ProblemResolution(
                problem="Severe cavitation on boiler feedwater pump BFP-02 during peak production.",
                resolution="Conducted suction pressure audit, unclogged strainer mesh, cleared vapor lock."
            )
        ],
        dedication="Dedicated to God Almighty and my wonderful family.",
        acknowledgement_bullets="Thanks to God Almighty, Landmark University leadership, host company, and mentors."
    )

    engine = SIWESAIEngine()
    generated_content = engine.generate_all_sections(payload)
    doc = create_siwes_document(payload, generated_content)
    output_filename = "test_12_weeks_report.docx"
    doc.save(output_filename)
    print(f"Generated '{output_filename}' ({os.path.getsize(output_filename)} bytes).")

if __name__ == "__main__":
    test_12_week_report()
