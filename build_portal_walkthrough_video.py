import os
import subprocess
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import imageio_ffmpeg

def main():
    print("=== Building Complete Student Portal Video Manual with Spoken Voiceover ===")
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"Using FFMPEG binary: {ffmpeg_exe}")
    
    os.makedirs('temp_portal_video', exist_ok=True)

    stages = [
        {
            "id": 1,
            "badge": "STEP 1: ONBOARDING",
            "title": "Student Account Registration & Demographics",
            "screenshot": "figures/guide_step1_registration.png",
            "voice": "Step 1: Student Account Registration. Students create their institutional profile with their Roll Number and password, while submitting eight demographic baseline attributes including engineering branch, living arrangement, first-generation status, and family income tier.",
            "metrics": [("Target User", "New Student", "#6366f1"), ("Demographics", "8 Attributes", "#10b981"), ("Quick Presets", "3 Modes", "#06b6d4")]
        },
        {
            "id": 2,
            "badge": "STEP 2: ASSESSMENT",
            "title": "1 to 5 Star Psychometric Self-Assessment",
            "screenshot": "figures/guide_step2_assessment.png",
            "voice": "Step 2: Psychometric Self-Assessment. The student completes a validated questionnaire across four structural pillars: Cognitive Mastery, Affective Wellness, Self-Regulation, and Socio-Contextual factors, using an intuitive one to five Likert rating scale.",
            "metrics": [("Scale", "1 to 5 Stars", "#f59e0b"), ("Pillars", "4 Clusters", "#10b981"), ("Inference Speed", "14.06 ms", "#38bdf8")]
        },
        {
            "id": 3,
            "badge": "STEP 3: STUDENT KUNDALI",
            "title": "360-Degree Psychological Radar & Predicted CGPA",
            "screenshot": "figures/guide_step3_kundali.png",
            "voice": "Step 3: Holistic Student Kundali. Upon submission, our multi-task neural network generates the Student Kundali dossier. It visualizes a 360-degree psychological radar, computes predicted graduation CGPA out of ten, and gauges the attrition hazard probability.",
            "metrics": [("Predicted CGPA", "5.64 / 10.0", "#818cf8"), ("Dropout Hazard", "68.4% Alert", "#ef4444"), ("Archetype", "5 Tiers", "#a855f7")]
        },
        {
            "id": 4,
            "badge": "STEP 4: EXPLAINABLE AI",
            "title": "Core Strengths vs. Critical Doshas (Weaknesses)",
            "screenshot": "figures/guide_step3_kundali.png",
            "voice": "Step 4: Strengths and Critical Doshas. Using game-theoretic SHAP explainability, the Kundali isolates the student's primary psychological assets while highlighting critical behavioral doshas, such as high exam panic, time deficits, or digital screen fatigue.",
            "metrics": [("Top Asset", "Digital Literacy", "#10b981"), ("Primary Dosha", "Exam Panic (4.2)", "#ef4444"), ("Time Deficit", "1.8 / 5.0", "#f59e0b")]
        },
        {
            "id": 5,
            "badge": "STEP 5: AI COUNSELING",
            "title": "Personalized 4-Stage Clinical Counseling Roadmap",
            "screenshot": "figures/guide_step8_counseling_center.png",
            "voice": "Step 5: Personalized AI Counseling Roadmap. The system formulates a four-stage structured intervention plan: immediate stabilization and sleep curfews in weeks one and two, habit restructuring in weeks three to six, peer coaching circles, and career mastery.",
            "metrics": [("Roadmap", "4 Stages", "#6366f1"), ("Triage Window", "Weeks 1-2", "#ef4444"), ("Mastery Goal", "Dean's List", "#10b981")]
        },
        {
            "id": 6,
            "badge": "STEP 6: ADMIN PORTAL",
            "title": "Institutional Command Center & Triage Roster",
            "screenshot": "figures/guide_step4_admin_portal.png",
            "voice": "Step 6: Institutional Admin Command Center. Deans, department heads, and academic advisors can review all registered student credentials, filter by risk level, inspect individual Kundalis with one click, and log official counseling session notes.",
            "metrics": [("Roster Size", "2,525 Records", "#38bdf8"), ("Credential Mgmt", "Active View", "#818cf8"), ("Export", "Instant CSV", "#10b981")]
        },
        {
            "id": 7,
            "badge": "STEP 7: DIAGNOSTICS",
            "title": "7 Behavioral Health Early Warning Indices",
            "screenshot": "figures/guide_step7_diagnostics.png",
            "voice": "Step 7: Seven Behavioral Health Diagnostics. The platform automatically monitors seven psychological indices, providing proactive alerts for test anxiety, chronic procrastination, imposter syndrome, and social isolation before grades suffer.",
            "metrics": [("Monitored Indices", "7 Flags", "#ec4899"), ("Panic Index", "EPI Screen", "#ef4444"), ("Fatigue Flag", "SICF Alert", "#f59e0b")]
        },
        {
            "id": 8,
            "badge": "STEP 8: PSYCHOMETRICS",
            "title": "Master 255-Question Database & CFA Loadings",
            "screenshot": "figures/guide_step9_255_questions.png",
            "voice": "Step 8: Master Psychometrics Explorer. Researchers and faculty can browse all two hundred fifty-five individual Likert questions, complete with construct mappings, standard deviations, and factor loadings confirming high statistical validity.",
            "metrics": [("Survey Scale", "255 Items", "#10b981"), ("Constructs", "17 Domains", "#6366f1"), ("CFA Loading", "λ > 0.70", "#06b6d4")]
        },
        {
            "id": 9,
            "badge": "STEP 9: CORRELATIONS",
            "title": "17x17 Pearson Inter-Construct Correlation Heatmap",
            "screenshot": "figures/guide_step10_correlation_heatmap.png",
            "voice": "Step 9: Correlation Heatmap. The seventeen-by-seventeen pairwise Pearson correlation matrix visualizes inter-construct dependencies, highlighting how time management directly reinforces focus and how resilience buffers against test anxiety.",
            "metrics": [("Matrix Size", "17 x 17", "#a855f7"), ("Key Synergy", "Time ↔ Focus (+0.76)", "#10b981"), ("Anxiety Buffer", "Grit ↔ Panic (-0.68)", "#06b6d4")]
        },
        {
            "id": 10,
            "badge": "STEP 10: CCRO RECOURSE",
            "title": "Paper 2 CCRO Decision Support & PGD-AFT Recourse",
            "screenshot": "figures/guide_step11_ccro_recourse.png",
            "voice": "Step 10: Actionable Recourse with CCRO. For Paper 2, our Projected Gradient Descent algorithm computes the exact minimal habit changes needed to safely guide at-risk students back to good standing, reducing dropout hazard from seventy-eight percent to eighteen percent.",
            "metrics": [("Recourse Shift", "78% → 18%", "#10b981"), ("Sparsity Bound", "K ≤ 3 Habits", "#38bdf8"), ("Audit Trail", "Human-in-Loop", "#f59e0b")]
        }
    ]

    stage_videos = []
    width, height = 1280, 720
    fps = 30

    for stage in stages:
        s_id = stage["id"]
        print(f"\n--- Generating Video for Step {s_id}: {stage['title']} ---")

        # 1. Synthesize Voice Audio via PowerShell System.Speech
        wav_path = f"temp_portal_video/voice_{s_id}.wav"
        escaped_script = stage["voice"].replace("'", "''")
        ps_cmd = f"""
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.Rate = 0
$synth.SetOutputToWaveFile('{os.path.abspath(wav_path)}')
$synth.Speak('{escaped_script}')
$synth.Dispose()
"""
        ps_file = f"temp_portal_video/synth_{s_id}.ps1"
        with open(ps_file, "w", encoding="utf-8") as pf:
            pf.write(ps_cmd)
        
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file], check=True)

        # 2. Measure Audio Length
        with wave.open(wav_path, "r") as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            duration = frames / float(rate)
        
        # Add 1.5s padding at end of stage
        stage_duration = duration + 1.5
        total_frames = int(stage_duration * fps)
        print(f"Step {s_id} Voice Duration: {duration:.2f}s | Stage Duration: {stage_duration:.2f}s ({total_frames} frames)")

        # 3. Create High-Quality Slide Image
        fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
        fig.patch.set_facecolor('#070a16')
        ax.set_facecolor('#070a16')
        ax.set_xlim(0, 1280)
        ax.set_ylim(0, 720)
        ax.axis('off')

        # Header Bar
        rect_head = patches.FancyBboxPatch((30, 630), 1220, 70, boxstyle="round,pad=5,rounding_size=12",
                                          facecolor='#0f172a', edgecolor='#312e81', linewidth=2)
        ax.add_patch(rect_head)

        # Badge
        ax.text(60, 665, stage["badge"], color='#a5b4fc', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1e1b4b', edgecolor='#6366f1', lw=1.5))

        # Title
        ax.text(280, 663, stage["title"], color='#ffffff', fontsize=16, fontweight='bold', va='center')

        # KPI Metrics Cards (Right Side of Header)
        mx_start = 820
        for m_label, m_val, m_col in stage["metrics"]:
            rect_m = patches.FancyBboxPatch((mx_start, 640), 130, 50, boxstyle="round,pad=3,rounding_size=8",
                                            facecolor='#111827', edgecolor=m_col, linewidth=1.5)
            ax.add_patch(rect_m)
            ax.text(mx_start + 65, 672, m_label.upper(), color='#94a3b8', fontsize=7.5, fontweight='bold', ha='center')
            ax.text(mx_start + 65, 652, m_val, color=m_col, fontsize=10.5, fontweight='bold', ha='center')
            mx_start += 140

        # Screenshot Embed in Center
        if os.path.exists(stage["screenshot"]):
            shot_img = Image.open(stage["screenshot"]).convert("RGB")
            # Target display area: (50, 105) to (1230, 615) -> 1180 x 510
            shot_resized = shot_img.resize((1180, 505), Image.Resampling.LANCZOS)
            shot_np = np.array(shot_resized)
            ax.imshow(shot_np, extent=[50, 1230, 110, 615], aspect='auto', zorder=2)
            
            # Frame Border around Screenshot
            rect_border = patches.Rectangle((50, 110), 1180, 505, linewidth=2, edgecolor='#3b82f6', facecolor='none', zorder=3)
            ax.add_patch(rect_border)

        # Bottom Voiceover Subtitle Bar
        rect_sub = patches.FancyBboxPatch((30, 15), 1220, 80, boxstyle="round,pad=5,rounding_size=10",
                                          facecolor='#0b1120', edgecolor='#1e293b', linewidth=1.5)
        ax.add_patch(rect_sub)
        
        ax.text(55, 65, f"🔊 SPOKEN NARRATION (STEP {s_id} OF 10):", color='#38bdf8', fontsize=9.5, fontweight='bold')
        ax.text(55, 38, stage["voice"], color='#e2e8f0', fontsize=10, fontweight='medium', wrap=True)

        slide_png = f"temp_portal_video/slide_{s_id}.png"
        plt.savefig(slide_png, dpi=100, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches=None, pad_inches=0)
        plt.close(fig)

        # 4. Render Stage Video with FFMPEG (Slide Image + Voice Audio)
        stage_mp4 = f"temp_portal_video/stage_{s_id}.mp4"
        cmd = [
            ffmpeg_exe,
            "-y",
            "-loop", "1",
            "-i", slide_png,
            "-i", wav_path,
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str(stage_duration),
            "-shortest",
            stage_mp4
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        stage_videos.append(stage_mp4)
        print(f"Step {s_id} video successfully compiled -> {stage_mp4}")

    # 5. Concatenate All Stages into Master Video
    print("\n--- Concatenating All 10 Steps into Master Video Manual ---")
    concat_list = "temp_portal_video/concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for sv in stage_videos:
            abs_v = os.path.abspath(sv).replace("\\", "/")
            f.write(f"file '{abs_v}'\n")

    master_mp4 = "Student_Portal_Video_Manual.mp4"
    cmd_concat = [
        ffmpeg_exe,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        master_mp4
    ]
    subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(master_mp4):
        size_mb = os.path.getsize(master_mp4) / (1024 * 1024)
        print(f"\n=======================================================")
        print(f"🎉 MASTER VIDEO MANUAL GENERATED SUCCESSFULLY!")
        print(f"File: {os.path.abspath(master_mp4)}")
        print(f"File Size: {size_mb:.2f} MB")
        print(f"=======================================================")

if __name__ == "__main__":
    main()
