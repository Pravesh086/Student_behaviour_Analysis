#!/usr/bin/env python3
"""
Student Psychometric & Behavioral Diagnostics Analytics Application
Production-Ready Web Server for Render & Local Environments
Run Command on Render: python3 app.py
"""

import http.server
import json
import mimetypes
import os
import sys
import urllib.parse
from http import HTTPStatus

# Ensure analytics data is generated on startup
if not os.path.exists("dashboard_data.json") or not os.path.exists("dashboard_data.js"):
    print("[INIT] dashboard_data.json not found. Running analytics engine...")
    try:
        import analytics_engine
        analytics_engine.main()
    except Exception as e:
        print(f"[ERROR] Failed to run analytics engine: {e}")

# Load cached data in memory for sub-millisecond API responses
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

class StudentAnalyticsRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    High-performance HTTP Request Handler providing:
    1. Static file delivery (HTML5, CSS3, JS, JSON)
    2. Zero-latency REST API endpoints (/api/health, /api/data, /api/student/<id>, /api/diagnostics, /api/simulate)
    """

    def end_headers(self):
        # Add CORS and security headers
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
        query = urllib.parse.parse_qs(parsed.query)

        # Health Check (Render readiness probe)
        if path in ("/api/health", "/healthz", "/health"):
            data = get_data()
            self.send_json_response({
                "status": "healthy",
                "service": "student-assessment-analytics",
                "studentsCount": data.get("metadata", {}).get("totalStudents", 2525),
                "totalDomains": data.get("metadata", {}).get("totalDomains", 17),
                "totalQuestions": data.get("metadata", {}).get("totalQuestions", 255)
            })
            return

        # Full Data Payload API
        if path == "/api/data":
            self.send_json_response(get_data())
            return

        # 7 Behavioral Diagnostics Summary API
        if path == "/api/diagnostics":
            data = get_data()
            self.send_json_response({
                "diagnosticsSummary": data.get("diagnosticsSummary", {}),
                "totalStudents": data.get("kpis", {}).get("totalStudents", 2525)
            })
            return

        # Proposed Questionnaire Expansion API
        if path == "/api/questionnaire-expansion":
            data = get_data()
            self.send_json_response({
                "proposedExpansion": data.get("proposedExpansion", [])
            })
            return

        # Individual Student 360 & AI Counseling API: /api/student/<student_id>
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

        # Default static routing
        if path == "/":
            self.path = "/index.html"

        # Serve static assets
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # Interactive Simulation Inference API
        if path == "/api/simulate":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                req_json = json.loads(body.decode("utf-8"))
                scores = req_json.get("scores", {}) # Dict of domain names -> float

                if not scores:
                    self.send_json_response({"error": "Missing domain scores in payload"}, status_code=HTTPStatus.BAD_REQUEST)
                    return

                vals = list(scores.values())
                sim_mean = round(sum(vals) / len(vals), 3)

                # Predictive Inference Logic
                if sim_mean >= 3.65:
                    pred_success = "Excellent"
                    pred_risk = "Low"
                    pred_career = "Highly Ready"
                elif sim_mean >= 3.20:
                    pred_success = "Good"
                    pred_risk = "Low" if sim_mean >= 3.45 else "Medium"
                    pred_career = "Ready"
                elif sim_mean >= 2.80:
                    pred_success = "Average"
                    pred_risk = "Medium"
                    pred_career = "Moderately Ready"
                elif sim_mean >= 2.40:
                    pred_success = "Poor"
                    pred_risk = "High"
                    pred_career = "Not Ready"
                else:
                    pred_success = "Bad"
                    pred_risk = "High"
                    pred_career = "Not Ready"

                self.send_json_response({
                    "simulatedMean": sim_mean,
                    "predictedSuccessTier": pred_success,
                    "predictedDropoutRisk": pred_risk,
                    "predictedCareerReadiness": pred_career
                })
            except Exception as e:
                self.send_json_response({"error": str(e)}, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
            return

        self.send_json_response({"error": "Endpoint not found"}, status_code=HTTPStatus.NOT_FOUND)

def run():
    # Render binds the port using the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"

    # Make sure mimetypes are properly configured
    mimetypes.init()
    mimetypes.add_type("application/javascript", ".js")
    mimetypes.add_type("text/css", ".css")
    mimetypes.add_type("application/json", ".json")
    mimetypes.add_type("text/html", ".html")

    server_address = (host, port)
    
    # Use ThreadingHTTPServer for concurrent client handling
    httpd = http.server.ThreadingHTTPServer(server_address, StudentAnalyticsRequestHandler)

    print("=" * 70)
    print(" 🚀 STUDENT PSYCHOMETRIC & BEHAVIORAL ANALYTICS DASHBOARD")
    print(f" 🌐 Host: {host} | Port: {port}")
    print(f" 🔗 Local Preview URL: http://localhost:{port}/index.html")
    print(f" 🩺 Health Probe:     http://localhost:{port}/api/health")
    print(f" 📊 Dataset API:      http://localhost:{port}/api/data")
    print("=" * 70)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[STOP] Shutting down server gracefully...")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run()
