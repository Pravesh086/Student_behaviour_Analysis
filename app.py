# -*- coding: utf-8 -*-
"""
Production-Ready Web Server with CCRO Survey-Driven Decision-Support REST APIs:
- /ccro-dashboard -> On-Demand Survey-Driven Mentor Decision-Support UI
- /api/v1/predict -> Survey-Based MT-DNN Risk & Calibration Prediction API
- /api/v1/recourse -> PGD-AFT Actionable Habit Recourse Optimizer API
- /api/v1/students -> De-identified survey cohort queue
- /api/v1/review -> Human-in-the-loop mentor decision logging
- /api/v1/audit-log -> Compliance & Governance Audit Trail
"""

import http.server
import json
import mimetypes
import os
import sys
import urllib.parse
from http import HTTPStatus
import ccro_engine

# Ensure analytics data is generated on startup
if not os.path.exists("dashboard_data.json") or not os.path.exists("dashboard_data.js"):
    print("[INIT] dashboard_data.json not found. Running analytics engine...")
    try:
        import analytics_engine
        analytics_engine.main()
    except Exception as e:
        print(f"[ERROR] Failed to run analytics engine: {e}")

DATA_CACHE = None
def get_data():
    global DATA_CACHE
    if DATA_CACHE is None:
        try:
            with open("dashboard_data.json", "r", encoding="utf-8") as f:
                DATA_CACHE = json.load(f)
        except Exception as e:
            print(f"[ERROR] Loading dashboard_data.json: {e}")
            DATA_CACHE = {}
    return DATA_CACHE

# Prototype De-Identified Survey Cohort
CCRO_STUDENTS = [
    {
        "student_reference": "STU-9F3A72",
        "department": "Computer Science & Engineering",
        "semester": 4,
        "survey_week": 7,
        "survey_completed_date": "2026-08-20 (Week 7)",
        "assessment_mode": "Point-in-Time Survey Response",
        "vector": [2.10, 2.20, 2.40, 3.10, 2.80, 2.00, 2.90, 2.80, 2.50, 2.40, 2.20, 2.60, 7.20] + [0]*11
    },
    {
        "student_reference": "STU-8B1C44",
        "department": "Electronics & Communication",
        "semester": 4,
        "survey_week": 7,
        "survey_completed_date": "2026-08-20 (Week 7)",
        "assessment_mode": "Point-in-Time Survey Response",
        "vector": [2.30, 2.10, 2.20, 2.80, 2.50, 1.80, 2.70, 2.60, 2.30, 2.10, 2.00, 2.40, 6.80] + [0]*11
    },
    {
        "student_reference": "STU-4D7E91",
        "department": "Mechanical Engineering",
        "semester": 4,
        "survey_week": 7,
        "survey_completed_date": "2026-08-21 (Week 7)",
        "assessment_mode": "Point-in-Time Survey Response",
        "vector": [2.50, 2.40, 2.50, 2.20, 2.40, 2.50, 2.80, 2.70, 2.60, 2.50, 2.40, 2.70, 7.50] + [0]*11
    },
    {
        "student_reference": "STU-3A6F28",
        "department": "Electrical Engineering",
        "semester": 4,
        "survey_week": 7,
        "survey_completed_date": "2026-08-22 (Week 7)",
        "assessment_mode": "Point-in-Time Survey Response",
        "vector": [2.50, 2.30, 2.10, 2.90, 2.70, 2.20, 2.60, 2.50, 2.40, 2.30, 2.20, 2.50, 7.10] + [0]*11
    }
]

class StudentAnalyticsRequestHandler(http.server.SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()

    def send_json_response(self, data, status_code=HTTPStatus.OK):
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # Health Check
        if path in ("/api/health", "/healthz", "/health"):
            data = get_data()
            self.send_json_response({
                "status": "healthy",
                "service": "student-survey-assessment-analytics",
                "studentsCount": data.get("metadata", {}).get("totalStudents", 2525)
            })
            return

        # Full Data Payload API
        if path == "/api/data":
            self.send_json_response(get_data())
            return

        # Diagnostics API
        if path == "/api/diagnostics":
            data = get_data()
            self.send_json_response({
                "diagnosticsSummary": data.get("diagnosticsSummary", {}),
                "totalStudents": data.get("kpis", {}).get("totalStudents", 2525)
            })
            return

        # CCRO Decision Support Dashboard View
        if path in ("/ccro", "/ccro-dashboard", "/advising-dashboard"):
            self.path = "/ccro_dashboard.html"
            return super().do_GET()

        # Student Registration & Assessment Portal
        if path in ("/register", "/registration", "/student-portal", "/student-registration"):
            self.path = "/student_portal.html"
            return super().do_GET()

        # Video Manual & Sound Walkthrough Portal
        if path in ("/video", "/video-manual", "/video-tour", "/video-guide"):
            self.path = "/portal_video_tour.html"
            return super().do_GET()

        # Presentation & Slides Portal
        if path in ("/presentation", "/slides", "/deck"):
            self.path = "/dashboard_presentation.html"
            return super().do_GET()

        # CCRO API: List De-Identified Survey Students
        if path == "/api/v1/students":
            student_list = []
            for s in CCRO_STUDENTS:
                pred = ccro_engine.predict_risk_mtdnn(s["vector"])
                student_list.append({
                    "student_reference": s["student_reference"],
                    "department": s["department"],
                    "semester": s["semester"],
                    "survey_week": s["survey_week"],
                    "survey_completed_date": s["survey_completed_date"],
                    "assessment_mode": s["assessment_mode"],
                    "risk_probability": pred["risk_probability"],
                    "risk_band": pred["risk_band"],
                    "projected_gpa": pred["projected_gpa"]
                })
            self.send_json_response({"students": student_list})
            return

        # CCRO API: Audit Log
        if path == "/api/v1/audit-log":
            self.send_json_response({"audit_trail": ccro_engine.get_audit_logs()})
            return

        # Individual Student Lookup API
        if path.startswith("/api/student/"):
            student_id = path.split("/api/student/")[1].strip().upper()
            data = get_data()
            students = data.get("students", [])
            matched = next((s for s in students if s["id"].upper() == student_id), None)
            if matched:
                self.send_json_response(matched)
            else:
                self.send_json_response({"error": f"Student {student_id} not found"}, status_code=HTTPStatus.NOT_FOUND)
            return

        if path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # CCRO API: Predict Risk
        if path == "/api/v1/predict":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                req_json = json.loads(body.decode("utf-8")) if length > 0 else {}
                stu_ref = req_json.get("student_reference", "STU-9F3A72")
                matched = next((s for s in CCRO_STUDENTS if s["student_reference"] == stu_ref), CCRO_STUDENTS[0])
                pred = ccro_engine.predict_risk_mtdnn(matched["vector"])
                
                resp = {
                    "student_reference": matched["student_reference"],
                    "model_version": "ccro-mtdnn-v2.1",
                    "assessment_mode": "Point-in-Time Survey Assessment",
                    "survey_completed_date": matched["survey_completed_date"],
                    "risk_probability": pred["risk_probability"],
                    "risk_band": pred["risk_band"],
                    "projected_gpa": pred["projected_gpa"],
                    "placement_tier": pred["placement_tier"],
                    "alert_threshold": 0.50,
                    "target_threshold": 0.20,
                    "requires_human_review": pred["risk_probability"] > 0.50
                }
                self.send_json_response(resp)
                return
            except Exception as e:
                self.send_json_response({"error": str(e)}, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

        # CCRO API: Generate Recourse
        if path == "/api/v1/recourse":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                req_json = json.loads(body.decode("utf-8")) if length > 0 else {}
                stu_ref = req_json.get("student_reference", "STU-9F3A72")
                matched = next((s for s in CCRO_STUDENTS if s["student_reference"] == stu_ref), CCRO_STUDENTS[0])
                
                recourse_out = ccro_engine.run_pgd_aft_recourse(matched)
                resp = {
                    "student_reference": matched["student_reference"],
                    "model_version": "ccro-mtdnn-v2.1",
                    "solver": "PGD-AFT",
                    "recourse_status": recourse_out["status"],
                    "initial_risk": recourse_out["initial_risk"],
                    "target_risk": recourse_out["target_risk"],
                    "sparsity_L0": recourse_out["sparsity_L0"],
                    "total_effort_cost": recourse_out["total_effort_cost"],
                    "violations": recourse_out["violations"],
                    "candidate_actions": recourse_out["candidate_actions"],
                    "locked_features_preserved": True,
                    "requires_human_review": True
                }
                self.send_json_response(resp)
                return
            except Exception as e:
                self.send_json_response({"error": str(e)}, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

        # CCRO API: Mentor Review Decision Logging
        if path == "/api/v1/review":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                req_json = json.loads(body.decode("utf-8")) if length > 0 else {}
                stu_ref = req_json.get("student_reference", "STU-9F3A72")
                action = req_json.get("action", "APPROVE")
                notes = req_json.get("notes", "Candidate study plan approved for advisor check-in.")
                
                entry = ccro_engine.record_audit(stu_ref, action, notes=notes)
                self.send_json_response({"status": "recorded", "entry": entry})
                return
            except Exception as e:
                self.send_json_response({"error": str(e)}, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

        # Simulation API
        if path == "/api/simulate":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                req_json = json.loads(body.decode("utf-8"))
                scores = req_json.get("scores", {})
                if not scores:
                    self.send_json_response({"error": "Missing domain scores"}, status_code=HTTPStatus.BAD_REQUEST)
                    return
                vals = list(scores.values())
                sim_mean = round(sum(vals) / len(vals), 3)
                sim_risk = round(max(0.05, min(0.95, 1.0 - (sim_mean / 5.0) * 1.1)), 3)
                self.send_json_response({"simulated_mean": sim_mean, "simulated_risk": sim_risk})
                return
            except Exception as e:
                self.send_json_response({"error": str(e)}, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

        self.send_json_response({"error": "Endpoint not found"}, status_code=HTTPStatus.NOT_FOUND)

def main():
    port = int(os.environ.get("PORT", 8080))
    server_address = ("0.0.0.0", port)
    httpd = http.server.HTTPServer(server_address, StudentAnalyticsRequestHandler)
    print(f"[*] AcuLearn & CCRO Survey Decision-Support Server online at http://localhost:{port}")
    print(f"[*] CCRO Mentor Dashboard available at: http://localhost:{port}/ccro-dashboard")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    main()
