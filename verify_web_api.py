import json
import urllib.request
import urllib.error
import os

def test_api_generate(payload, output_filename):
    url = "http://127.0.0.1:8000/api/generate-docx"
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    body = []
    body.append(f"--{boundary}".encode())
    body.append(b'Content-Disposition: form-data; name="payload_json"')
    body.append(b'')
    body.append(json.dumps(payload).encode("utf-8"))
    body.append(f"--{boundary}--".encode())
    body.append(b'')
    
    data = b"\r\n".join(body)
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    
    print(f"Sending POST request to {url} for '{output_filename}'...")
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            status = response.status
            content_type = response.headers.get("Content-Type")
            content = response.read()
            print(f"Response Status: {status}")
            print(f"Content-Type: {content_type}")
            print(f"Received bytes: {len(content)}")
            
            with open(output_filename, "wb") as f:
                f.write(content)
            print(f"Successfully saved '{output_filename}' ({len(content)} bytes).")
            return True
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # Base sample data
    base_student = {
        "full_name": "ADEKUNLE, Oluwaseun Emmanuel",
        "matric_number": "21/ENG05/042",
        "department": "Mechanical Engineering",
        "college": "College of Engineering",
        "institution": "Landmark University, Omu-Aran, Kwara State",
        "level": "400 Level",
        "org_name": "Dangote Sugar Refinery Plc",
        "org_address": "Shed 20, NPA Wharf Complex, Apapa, Lagos State",
        "org_industry": "Agro-Industrial Food Processing & Process Plant Engineering",
        "industry_supervisor": "Engr. Babatunde Balogun, MNSE (Chief Plant Engineer)",
        "academic_supervisor": "Dr. A. O. Oladipo",
        "siwes_officer": "Engr. (Mrs.) F. E. Babatunde",
        "hod_name": "Prof. J. K. Adewumi",
        "start_date": "1st July 2026",
        "end_date": "18th December 2026",
        "siwes_type": "SIWES II",
        "duration_weeks": 24
    }

    base_problems = [
        {
            "problem": "Severe cavitation and excessive high-frequency vibration detected on boiler feedwater pump BFP-02 during peak production load.",
            "resolution": "Executed systematic suction line pressure inspection. Discovered clogging at the suction strainer causing net positive suction head (NPSH) deficiency. Cleaned filter mesh, cleared suction air pockets, and re-torqued casing bolts, restoring smooth laminar flow and reducing vibration to within ISO 10816 limits."
        },
        {
            "problem": "Repeated premature thermal failure of deep-groove ball bearings on crystallizer drive gearbox input shaft.",
            "resolution": "Conducted root-cause failure analysis (RCFA). Determined incorrect lubricant grade with insufficient high-temperature viscosity. Flushed old grease, replaced bearings with C3-clearance SKF units, and switched to synthetic polyurea high-temp lubricant with scheduled ultrasonic re-greasing."
        }
    ]

    base_references = [
        {
            "source_type": "book",
            "authors": "Shigley, J. E., & Mischke, C. R.",
            "year": "2020",
            "title": "Mechanical Engineering Design (11th ed.)",
            "source_name": "McGraw-Hill Education"
        }
    ]

    # 1. 12-Week Payload (SIWES I / 300 Level)
    student_12 = dict(base_student)
    student_12.update({
        "full_name": "OGUNDELE, Boluwatife David",
        "matric_number": "22/ENG05/019",
        "level": "300 Level",
        "siwes_type": "SIWES I",
        "duration_weeks": 12,
        "start_date": "1st June 2026",
        "end_date": "25th September 2026"
    })

    payload_12 = {
        "student_info": student_12,
        "org_history_raw": "Dangote Sugar Refinery Plc is the largest sugar refinery in Sub-Saharan Africa and second largest globally. Commissioned in March 2000, it operates an initial refining capacity of 600,000 metric tons per annum.",
        "department_placed": "Mechanical Maintenance & Process Plant Engineering Division",
        "reporting_line": "Reported to the Lead Maintenance Engineer and Shift Plant Superintendent",
        "weekly_activities": [
            {
                "week_number": 1,
                "date_range": "1st June - 5th June 2026",
                "department_unit": "HSE & Induction Unit",
                "activities": "Underwent occupational safety induction, LOTO procedures, plant evacuation protocols.",
                "skills_tools": "LOTO safety kit, gas monitors, PPE"
            }
        ],
        "problems_resolutions": base_problems,
        "dedication": "Dedicated to God Almighty and my loving parents.",
        "acknowledgement_bullets": "- Gratitude to God for divine protection\n- Landmark University Chancellor and academic leadership\n- Host company and industry supervisor",
        "references": base_references,
        "student_recommendations": "1. Host regular hands-on CAD workshops.\n2. Expand predictive maintenance internships."
    }

    # 2. 24-Week Payload (SIWES II / 400 Level)
    payload_24 = {
        "student_info": base_student,
        "org_history_raw": "Dangote Sugar Refinery Plc is the largest sugar refinery in Sub-Saharan Africa and second largest globally. Commissioned in March 2000, it operates an initial refining capacity of 600,000 metric tons per annum, now expanded to over 1.44 million MT/year.",
        "department_placed": "Mechanical Maintenance & Process Plant Engineering Division",
        "reporting_line": "Reported to the Lead Maintenance Engineer and Shift Plant Superintendent",
        "weekly_activities": [
            {
                "week_number": 1,
                "date_range": "1st July - 5th July 2026",
                "department_unit": "HSE & Technical Induction Unit",
                "activities": "Underwent comprehensive site occupational health and safety induction. Trained on industrial hazard identification, PPE compliance, and plant evacuation drills.",
                "skills_tools": "LOTO safety kits, multi-gas monitors, industrial hazard matrices, PPE equipment"
            }
        ],
        "problems_resolutions": base_problems,
        "dedication": "Dedicated to God Almighty, my parents, and the faculty of Landmark University.",
        "acknowledgement_bullets": "- Praise to the Lord God Almighty for sound health.\n- Landmark University Chancellor Dr. David Oyedepo and faculty.\n- Host organization Dangote Sugar Refinery Plc.",
        "references": base_references,
        "student_recommendations": "1. Increase student exposure to SCADA telemetry systems.\n2. Rotate students through industrial QA laboratories."
    }

    print("=== Testing Live Web API for 12-Week (SIWES I / 300L) ===")
    ok_12 = test_api_generate(payload_12, "api_test_12_weeks.docx")

    print("\n=== Testing Live Web API for 24-Week (SIWES II / 400L) ===")
    ok_24 = test_api_generate(payload_24, "api_test_24_weeks.docx")

    print(f"\nFinal Summary: 12-Week OK = {ok_12}, 24-Week OK = {ok_24}")
