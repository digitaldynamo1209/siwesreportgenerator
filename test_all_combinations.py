import copy
from app.models import SIWESReportPayload, StudentPlacementInfo, WeeklyActivity, ProblemResolution, ReferenceItem
from app.ai_generator import SIWESAIEngine
from app.docx_generator import create_siwes_document
import os

base_student = StudentPlacementInfo(
    full_name="ADEKUNLE, Oluwaseun Emmanuel",
    matric_number="21/ENG05/042",
    department="Mechanical Engineering",
    college="College of Engineering",
    institution="Landmark University, Omu-Aran, Kwara State",
    level="400 Level",
    org_name="Dangote Sugar Refinery Plc",
    org_address="Shed 20, NPA Wharf Complex, Apapa, Lagos State",
    org_industry="Agro-Industrial Food Processing & Process Plant Engineering",
    industry_supervisor="Engr. Babatunde Balogun, MNSE (Chief Plant Engineer)",
    academic_supervisor="Dr. A. O. Oladipo",
    siwes_officer="Engr. (Mrs.) F. E. Babatunde",
    hod_name="Prof. J. K. Adewumi",
    start_date="1st July 2026",
    end_date="18th December 2026"
)

base_problems = [
    ProblemResolution(
        problem="Severe cavitation on boiler feedwater pump BFP-02 during peak production.",
        resolution="Conducted suction pressure audit, unclogged strainer mesh, cleared vapor lock."
    )
]

base_references = [
    ReferenceItem(
        source_type="book",
        authors="Shigley, J. E., & Mischke, C. R.",
        year="2020",
        title="Mechanical Engineering Design (11th ed.)",
        source_name="McGraw-Hill Education"
    )
]

engine = SIWESAIEngine()

combos = [
    ("combo_siwes1_12w.docx", "SIWES I", 12, "300 Level"),
    ("combo_siwes1_24w.docx", "SIWES I", 24, "300 Level"),
    ("combo_siwes2_12w.docx", "SIWES II", 12, "400 Level"),
    ("combo_siwes2_24w.docx", "SIWES II", 24, "400 Level"),
]

for filename, s_type, weeks, lvl in combos:
    print(f"\n--- Testing: {s_type} with {weeks} Weeks ({lvl}) -> {filename} ---")
    st = copy.deepcopy(base_student)
    st.siwes_type = s_type
    st.duration_weeks = weeks
    st.level = lvl
    if weeks == 12:
        st.end_date = "25th September 2026"
    else:
        st.end_date = "18th December 2026"
        
    payload = SIWESReportPayload(
        student_info=st,
        org_history_raw="Dangote Sugar Refinery Plc is the largest sugar refinery in Sub-Saharan Africa.",
        department_placed="Mechanical Maintenance & Process Plant Engineering Division",
        reporting_line="Reported to the Lead Maintenance Engineer and Shift Plant Superintendent",
        weekly_activities=[],
        problems_resolutions=base_problems,
        dedication="Dedicated to God Almighty and my loving parents.",
        acknowledgement_bullets="- Gratitude to God\n- Landmark University Leadership\n- Host Company",
        references=base_references
    )
    
    generated_content = engine.generate_all_sections(payload)
    doc = create_siwes_document(payload, generated_content)
    doc.save(filename)
    print(f"Generated {filename} ({os.path.getsize(filename)} bytes)")

print("\nAll 4 combinations created successfully!")
