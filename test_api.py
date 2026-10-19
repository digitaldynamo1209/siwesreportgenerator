import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_endpoints():
    print("Testing GET /api/health...")
    res = client.get("/api/health")
    assert res.status_code == 200, f"Health check failed: {res.text}"
    print("Health check response:", res.json())

    print("Testing GET / (Static UI)...")
    res_ui = client.get("/")
    assert res_ui.status_code == 200
    assert "SIWES Report AI" in res_ui.text
    print("Static UI served successfully!")

    print("Testing POST /api/generate-docx with sample payload...")
    from app.models import SIWESReportPayload, StudentPlacementInfo, WeeklyActivity, ProblemResolution, ReferenceItem
    test_payload = SIWESReportPayload(
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
            industry_supervisor="Engr. Babatunde Balogun, MNSE",
            academic_supervisor="Dr. A. O. Oladipo",
            siwes_officer="Engr. (Mrs.) F. E. Babatunde",
            hod_name="Prof. J. K. Adewumi",
            start_date="1st July 2026",
            end_date="18th December 2026"
        ),
        org_history_raw="Dangote Sugar Refinery Plc is a leading sugar refinery in Sub-Saharan Africa.",
        department_placed="Mechanical Maintenance Division",
        reporting_line="Reported to Lead Plant Engineer",
        weekly_activities=[
            WeeklyActivity(
                week_number=1,
                date_range="1st July - 5th July 2026",
                department_unit="HSE & Safety",
                activities="Occupational safety induction and plant overview.",
                skills_tools="PPE, LOTO"
            )
        ],
        problems_resolutions=[
            ProblemResolution(
                problem="Feed pump cavitation.",
                resolution="Cleaned suction strainer mesh."
            )
        ],
        acknowledgement_bullets="Thanks to God and Landmark University leadership."
    )
    payload_dict = test_payload.model_dump()
    res_docx = client.post(
        "/api/generate-docx",
        data={"payload_json": json.dumps(payload_dict)}
    )
    assert res_docx.status_code == 200
    assert len(res_docx.content) > 10000
    print(f"POST /api/generate-docx returned {len(res_docx.content)} bytes of .docx binary!")
    print("All API tests PASSED!")

if __name__ == "__main__":
    from test_generation import run_test
    test_endpoints()
