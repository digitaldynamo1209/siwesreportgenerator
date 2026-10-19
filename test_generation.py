"""
End-to-end automated test for SIWES Report Word Generation.
"""

import os
from app.models import SIWESReportPayload, StudentPlacementInfo, WeeklyActivity, ProblemResolution, ReferenceItem
from app.ai_generator import SIWESAIEngine
from app.docx_generator import create_siwes_document

def run_test():
    print("1. Creating test payload...")
    payload = SIWESReportPayload(
        student_info=StudentPlacementInfo(
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
        ),
        org_history_raw="Dangote Sugar Refinery Plc is the largest sugar refinery in Sub-Saharan Africa and second largest globally. Commissioned in March 2000, it operates an initial refining capacity of 600,000 metric tons per annum, now expanded to over 1.44 million MT/year.",
        department_placed="Mechanical Maintenance & Process Plant Engineering Division",
        reporting_line="Reported to the Lead Maintenance Engineer and Shift Plant Superintendent",
        weekly_activities=[
            WeeklyActivity(
                week_number=1,
                date_range="1st July - 5th July 2026",
                department_unit="HSE & Safety Induction",
                activities="Underwent occupational safety induction, LOTO procedures, plant evacuation protocols.",
                skills_tools="LOTO safety kit, gas monitors, PPE"
            ),
            WeeklyActivity(
                week_number=2,
                date_range="8th July - 12th July 2026",
                department_unit="Turbine & Power Station",
                activities="Monitored 16MW Siemens turbo-generator vibration, bearing temperatures, and steam flow.",
                skills_tools="Vibration analyzer, infrared thermometer, SCADA console"
            )
        ],
        problems_resolutions=[
            ProblemResolution(
                problem="Severe cavitation on boiler feedwater pump BFP-02 during peak production.",
                resolution="Conducted suction pressure audit, unclogged strainer mesh, cleared vapor lock."
            )
        ],
        dedication="Dedicated to God Almighty and my loving parents.",
        acknowledgement_bullets="- Gratitude to God for divine protection\n- Landmark University Chancellor and academic leadership\n- Host company and industry supervisor",
        references=[
            ReferenceItem(
                source_type="book",
                authors="Shigley, J. E., & Mischke, C. R.",
                year="2020",
                title="Mechanical Engineering Design (11th ed.)",
                source_name="McGraw-Hill Education"
            )
        ]
    )

    print("2. Generating AI content (simulated / fallback or Gemini)...")
    engine = SIWESAIEngine()
    generated_content = engine.generate_all_sections(payload)
    print(f"   Generated abstract: {len(generated_content['abstract'])} chars")
    print(f"   Generated acknowledgement: {len(generated_content['acknowledgement'])} chars")
    print(f"   Acronyms found: {list(generated_content['acronyms'].keys())}")

    print("3. Building Word Document (.docx)...")
    doc = create_siwes_document(payload, generated_content)
    output_filename = "test_siwes_report.docx"
    doc.save(output_filename)
    
    file_size = os.path.getsize(output_filename)
    print(f"4. Success! Generated '{output_filename}' ({file_size} bytes).")
    assert file_size > 5000, "Document size should be larger than 5KB"
    print("All verification checks PASSED!")

if __name__ == "__main__":
    run_test()
