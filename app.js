/**
 * Student Assessment, 17-Domain Psychometrics, Demographics & AI Counseling Engine
 * Interactive Core Application
 */

(function () {
  "use strict";

  if (!window.DASHBOARD_DATA) {
    console.error("Dashboard data not found!");
    return;
  }

  const data = window.DASHBOARD_DATA;
  const { kpis, domains, questions, students, demographics, diagnosticsSummary } = data;

  const chartInstances = {};

  if (window.Chart) {
    Chart.defaults.color = "#94a3b8";
    Chart.defaults.font.family = "'Plus Jakarta Sans', 'Inter', sans-serif";
    Chart.defaults.plugins.tooltip.backgroundColor = "rgba(15, 23, 42, 0.95)";
    Chart.defaults.plugins.tooltip.titleColor = "#ffffff";
    Chart.defaults.plugins.tooltip.bodyColor = "#cbd5e1";
    Chart.defaults.plugins.tooltip.borderColor = "rgba(255, 255, 255, 0.1)";
    Chart.defaults.plugins.tooltip.borderWidth = 1;
    Chart.defaults.plugins.tooltip.padding = 10;
    Chart.defaults.plugins.tooltip.cornerRadius = 8;
  }

  // --- Utility Helpers ---
  function formatBadge(type, value) {
    if (type === "success") {
      const cls = {
        "Excellent": "badge-excellent",
        "Good": "badge-good",
        "Average": "badge-average",
        "Poor": "badge-poor",
        "Bad": "badge-bad"
      }[value] || "badge-average";
      return `<span class="badge ${cls}">${value}</span>`;
    }
    if (type === "risk") {
      const cls = {
        "Low": "badge-risk-low",
        "Medium": "badge-risk-medium",
        "High": "badge-risk-high"
      }[value] || "badge-risk-medium";
      return `<span class="badge ${cls}">${value} Risk</span>`;
    }
    if (type === "career") {
      const cls = {
        "Highly Ready": "badge-career-highly",
        "Ready": "badge-career-ready",
        "Moderately Ready": "badge-career-mod",
        "Not Ready": "badge-career-not"
      }[value] || "badge-career-mod";
      return `<span class="badge ${cls}">${value}</span>`;
    }
    return `<span>${value}</span>`;
  }

  function getHeatmapColor(val) {
    const norm = Math.max(0, Math.min(1, (val - 0.7) / 0.3));
    const r = Math.round(99 + (6 - 99) * norm);
    const g = Math.round(102 + (182 - 102) * norm);
    const b = Math.round(241 + (212 - 241) * norm);
    const alpha = 0.2 + 0.65 * norm;
    return `rgba(${r}, ${g}, ${b}, ${alpha.toFixed(2)})`;
  }

  // --- 1. Tab Switcher Logic ---
  function initTabs() {
    const tabButtons = document.querySelectorAll("#main-tabs .tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(btn => {
      btn.addEventListener("click", () => {
        const targetTab = btn.getAttribute("data-tab");
        tabButtons.forEach(b => b.classList.remove("active"));
        tabContents.forEach(c => c.classList.remove("active"));

        btn.classList.add("active");
        const activeContent = document.getElementById(`tab-${targetTab}`);
        if (activeContent) {
          activeContent.classList.add("active");
        }

        setTimeout(() => {
          Object.values(chartInstances).forEach(chart => chart && chart.resize && chart.resize());
        }, 50);
      });
    });

    const urlParams = new URLSearchParams(window.location.search);
    const tabParam = urlParams.get('tab');
    if (tabParam) {
      setTimeout(() => switchTab(tabParam), 50);
    }
  }

  function switchTab(tabId) {
    const btn = document.querySelector(`#main-tabs .tab-btn[data-tab="${tabId}"]`);
    if (btn) btn.click();
  }

  // --- 2. Executive Overview Tab ---
  function initOverviewTab() {
    document.getElementById("kpi-total-students").textContent = kpis.totalStudents.toLocaleString();
    document.getElementById("kpi-mean-score").textContent = kpis.overallMean.toFixed(2);
    
    const avgAlpha = (domains.reduce((acc, d) => acc + d.cronbachAlpha, 0) / domains.length).toFixed(3);
    document.getElementById("kpi-cronbach").textContent = avgAlpha;

    const lowCount = kpis.dropoutCounts["Low"] || 0;
    const medCount = kpis.dropoutCounts["Medium"] || 0;
    const retPct = (((lowCount + medCount) / kpis.totalStudents) * 100).toFixed(1);
    document.getElementById("kpi-retention-rate").textContent = `${retPct}%`;

    // 7 Diagnostics Quick Banner
    const diagBanner = document.getElementById("overview-diag-banner");
    if (diagBanner && diagnosticsSummary) {
      diagBanner.innerHTML = Object.entries(diagnosticsSummary).map(([k, v]) => {
        const pct = ((v.count / kpis.totalStudents) * 100).toFixed(1);
        return `
          <div class="diag-card" style="--diag-color: ${v.color};">
            <span class="diag-title">${v.title}</span>
            <div class="diag-val-row">
              <span class="diag-count">${v.count}</span>
              <span class="diag-pct">${pct}%</span>
            </div>
          </div>
        `;
      }).join("");
    }

    // Radar Chart: 17 Domains across 5 Success Tiers
    const ctxRadar = document.getElementById("chart-radar-tiers");
    if (ctxRadar) {
      if (chartInstances.radarTiers) chartInstances.radarTiers.destroy();

      const labels = domains.map(d => d.code);
      const tierColors = {
        "Excellent": { border: "#10b981", bg: "rgba(16, 185, 129, 0.15)" },
        "Good": { border: "#06b6d4", bg: "rgba(6, 182, 212, 0.1)" },
        "Average": { border: "#f59e0b", bg: "rgba(245, 158, 11, 0.08)" },
        "Poor": { border: "#f97316", bg: "rgba(249, 115, 22, 0.08)" },
        "Bad": { border: "#ef4444", bg: "rgba(239, 68, 68, 0.1)" }
      };

      const datasets = ["Excellent", "Good", "Average", "Poor", "Bad"].map(tier => {
        return {
          label: tier,
          data: domains.map(d => d.tierMeans[tier]),
          borderColor: tierColors[tier].border,
          backgroundColor: tierColors[tier].bg,
          borderWidth: 2,
          pointRadius: 3,
          pointHoverRadius: 5
        };
      });

      chartInstances.radarTiers = new Chart(ctxRadar, {
        type: "radar",
        data: { labels, datasets },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              min: 1.5,
              max: 4.5,
              grid: { color: "rgba(255, 255, 255, 0.06)" },
              angleLines: { color: "rgba(255, 255, 255, 0.08)" },
              pointLabels: { color: "#cbd5e1", font: { size: 10, weight: "600" } },
              ticks: { backdropColor: "transparent", color: "#64748b", stepSize: 0.5 }
            }
          },
          plugins: {
            legend: { position: "top", labels: { boxWidth: 12, font: { size: 11, weight: "600" } } },
            tooltip: {
              callbacks: {
                title: items => {
                  const idx = items[0].dataIndex;
                  return `${domains[idx].name} (${domains[idx].code})${domains[idx].isNew ? ' [NEW]' : ''}`;
                }
              }
            }
          }
        }
      });
    }

    // Donut 1: Success Tiers
    const ctxSuccess = document.getElementById("chart-donut-success");
    if (ctxSuccess) {
      if (chartInstances.donutSuccess) chartInstances.donutSuccess.destroy();
      chartInstances.donutSuccess = new Chart(ctxSuccess, {
        type: "doughnut",
        data: {
          labels: ["Excellent", "Good", "Average", "Poor", "Bad"],
          datasets: [{
            data: ["Excellent", "Good", "Average", "Poor", "Bad"].map(t => kpis.successCounts[t] || 0),
            backgroundColor: ["#10b981", "#06b6d4", "#f59e0b", "#f97316", "#ef4444"],
            borderWidth: 2,
            borderColor: "#111827"
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: { display: true, text: "Success Tiers (20% Each)", color: "#cbd5e1", font: { size: 12, weight: "600" } },
            legend: { position: "bottom", labels: { boxWidth: 10, font: { size: 10 } } }
          },
          cutout: "68%"
        }
      });
    }

    // Donut 2: Dropout Risk
    const ctxRisk = document.getElementById("chart-donut-risk");
    if (ctxRisk) {
      if (chartInstances.donutRisk) chartInstances.donutRisk.destroy();
      chartInstances.donutRisk = new Chart(ctxRisk, {
        type: "doughnut",
        data: {
          labels: ["Low Risk", "Medium Risk", "High Risk"],
          datasets: [{
            data: ["Low", "Medium", "High"].map(r => kpis.dropoutCounts[r] || 0),
            backgroundColor: ["#10b981", "#f59e0b", "#ef4444"],
            borderWidth: 2,
            borderColor: "#111827"
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: { display: true, text: "Dropout Risk Classification", color: "#cbd5e1", font: { size: 12, weight: "600" } },
            legend: { position: "bottom", labels: { boxWidth: 10, font: { size: 10 } } }
          },
          cutout: "68%"
        }
      });
    }

    // Domain Leaderboard List
    const lbContainer = document.getElementById("domain-leaderboard-container");
    if (lbContainer) {
      const sortedDomains = [...domains].sort((a, b) => b.mean - a.mean);
      lbContainer.innerHTML = sortedDomains.map((d, i) => {
        const pct = ((d.mean / 5.0) * 100).toFixed(0);
        return `
          <div class="domain-rank-item">
            <span class="domain-rank-num">#${i + 1}</span>
            <div class="domain-rank-info">
              <div class="domain-rank-title">
                <span>${d.name} ${d.isNew ? '<span class="badge" style="background: rgba(6, 182, 212, 0.2); color: #38bdf8; font-size: 0.68rem; padding: 1px 5px;">NEW</span>' : ''} <span class="domain-alpha-badge">α = ${d.cronbachAlpha}</span></span>
                <span style="font-family: var(--font-mono); color: #67e8f9;">${d.mean.toFixed(2)} / 5</span>
              </div>
              <div class="domain-bar-bg">
                <div class="domain-bar-fill" style="width: ${pct}%;"></div>
              </div>
            </div>
          </div>
        `;
      }).join("");
    }

    // Overall Score Histogram
    const ctxHist = document.getElementById("chart-overall-hist");
    if (ctxHist) {
      if (chartInstances.overallHist) chartInstances.overallHist.destroy();
      chartInstances.overallHist = new Chart(ctxHist, {
        type: "bar",
        data: {
          labels: kpis.overallHist.labels,
          datasets: [{
            label: "Student Count",
            data: kpis.overallHist.counts,
            backgroundColor: "rgba(99, 102, 241, 0.4)",
            borderColor: "#6366f1",
            borderWidth: 1.5,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              grid: { color: "rgba(255, 255, 255, 0.04)" },
              ticks: { color: "#94a3b8", font: { size: 11 } },
              title: { display: true, text: "Overall Score (17 Domains)", color: "#64748b" }
            },
            y: {
              grid: { color: "rgba(255, 255, 255, 0.06)" },
              ticks: { color: "#94a3b8" }
            }
          },
          plugins: { legend: { display: false } }
        }
      });
    }
  }

  // --- 3. Demographics & Cohorts Tab ---
  function initDemographicsTab() {
    if (!demographics) return;

    // Major Breakdown Chart
    const ctxMajor = document.getElementById("chart-demo-major");
    if (ctxMajor && demographics.byMajor) {
      if (chartInstances.demoMajor) chartInstances.demoMajor.destroy();

      const sortedMajors = [...demographics.byMajor].sort((a, b) => b.mean - a.mean);
      chartInstances.demoMajor = new Chart(ctxMajor, {
        type: "bar",
        data: {
          labels: sortedMajors.map(m => m.category),
          datasets: [
            {
              label: "Low Risk",
              data: sortedMajors.map(m => m.dropoutLow),
              backgroundColor: "#10b981",
              stack: "risk"
            },
            {
              label: "Medium Risk",
              data: sortedMajors.map(m => m.dropoutMed),
              backgroundColor: "#f59e0b",
              stack: "risk"
            },
            {
              label: "High Risk",
              data: sortedMajors.map(m => m.dropoutHigh),
              backgroundColor: "#ef4444",
              stack: "risk"
            }
          ]
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } },
            y: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 11 } } }
          },
          plugins: {
            legend: { position: "top", labels: { boxWidth: 10 } }
          }
        }
      });
    }

    // Income & Work Hours
    const ctxIncomeWork = document.getElementById("chart-demo-income-work");
    if (ctxIncomeWork && demographics.byIncome) {
      if (chartInstances.demoIncome) chartInstances.demoIncome.destroy();

      chartInstances.demoIncome = new Chart(ctxIncomeWork, {
        type: "bar",
        data: {
          labels: demographics.byIncome.map(i => i.category),
          datasets: [{
            label: "Average 17-Domain Score",
            data: demographics.byIncome.map(i => i.mean),
            backgroundColor: "rgba(6, 182, 212, 0.7)",
            borderColor: "#06b6d4",
            borderWidth: 1,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1" } },
            y: { min: 2.0, max: 4.0, grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }

    // Admission Category Breakdown (Indian Reservation Quota)
    const ctxFirstGen = document.getElementById("chart-demo-firstgen");
    const categoryData = demographics.byCategory || demographics.byFirstGen;
    if (ctxFirstGen && categoryData) {
      if (chartInstances.demoFirstGen) chartInstances.demoFirstGen.destroy();

      chartInstances.demoFirstGen = new Chart(ctxFirstGen, {
        type: "doughnut",
        data: {
          labels: categoryData.map(f => `${f.category} (${f.count})`),
          datasets: [{
            data: categoryData.map(f => f.count),
            backgroundColor: ["#6366f1", "#06b6d4", "#f59e0b", "#10b981", "#ec4899"],
            borderWidth: 2,
            borderColor: "#111827"
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: "bottom", labels: { boxWidth: 10, font: { size: 10 } } } }
        }
      });
    }

    // Housing Type
    const ctxHousing = document.getElementById("chart-demo-housing");
    if (ctxHousing && demographics.byHousing) {
      if (chartInstances.demoHousing) chartInstances.demoHousing.destroy();

      chartInstances.demoHousing = new Chart(ctxHousing, {
        type: "bar",
        data: {
          labels: demographics.byHousing.map(h => h.category.split(" ")[0]),
          datasets: [{
            label: "Mean Score",
            data: demographics.byHousing.map(h => h.mean),
            backgroundColor: "#a855f7",
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 10 } } },
            y: { min: 2.5, max: 3.5, grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }

    // Academic Year
    const ctxYear = document.getElementById("chart-demo-year");
    if (ctxYear && demographics.byYear) {
      if (chartInstances.demoYear) chartInstances.demoYear.destroy();

      chartInstances.demoYear = new Chart(ctxYear, {
        type: "bar",
        data: {
          labels: demographics.byYear.map(y => y.category),
          datasets: [{
            label: "Student Count",
            data: demographics.byYear.map(y => y.count),
            backgroundColor: "#6366f1",
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 10 } } },
            y: { grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }
  }

  // --- 4. 7 Behavioral Diagnostics Tab ---
  function initDiagnosticsTab() {
    const ctxDiagBar = document.getElementById("chart-diagnostics-bar");
    if (ctxDiagBar && diagnosticsSummary) {
      if (chartInstances.diagBar) chartInstances.diagBar.destroy();

      const labels = Object.values(diagnosticsSummary).map(v => v.title);
      const counts = Object.values(diagnosticsSummary).map(v => v.count);
      const colors = Object.values(diagnosticsSummary).map(v => v.color);

      chartInstances.diagBar = new Chart(ctxDiagBar, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [{
            label: "Affected Students (N=2,525)",
            data: counts,
            backgroundColor: colors,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 11, weight: "600" } } },
            y: { grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                afterLabel: item => {
                  const pct = ((item.raw / kpis.totalStudents) * 100).toFixed(1);
                  return `Prevalence: ${pct}% of Cohort`;
                }
              }
            }
          }
        }
      });
    }

    const ctxFlagsDist = document.getElementById("chart-flags-distribution");
    if (ctxFlagsDist) {
      if (chartInstances.flagsDist) chartInstances.flagsDist.destroy();

      const flagCounts = [0, 0, 0, 0, 0, 0, 0, 0];
      students.forEach(s => {
        let count = 0;
        if (s.diagnostics.interest.isFlagged) count++;
        if (s.diagnostics.collaboration.isFlagged) count++;
        if (s.diagnostics.procrastination.isFlagged) count++;
        if (s.diagnostics.screenFatigue.isFlagged) count++;
        if (s.diagnostics.chronicSkipping.isFlagged) count++;
        if (s.diagnostics.mentalBurnout.isFlagged) count++;
        if (s.diagnostics.courseFailure.isFlagged) count++;
        flagCounts[count]++;
      });

      chartInstances.flagsDist = new Chart(ctxFlagsDist, {
        type: "bar",
        data: {
          labels: ["0 Flags (Thriving)", "1 Flag", "2 Flags", "3 Flags", "4 Flags (Critical)", "5 Flags", "6 Flags", "7 Flags (Extreme)"],
          datasets: [{
            label: "Student Count",
            data: flagCounts,
            backgroundColor: [
              "#10b981", "#38bdf8", "#818cf8", "#f59e0b", "#f97316", "#ef4444", "#dc2626", "#991b1b"
            ],
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 10 }, maxRotation: 25 } },
            y: { grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }
  }

  // --- 5. AI Counseling Center Tab ---
  let activeCounselingStudent = null;

  function initCounselingTab() {
    const listContainer = document.getElementById("counseling-student-list");
    const searchInput = document.getElementById("input-counseling-search");
    const btnCopy = document.getElementById("btn-copy-counseling");

    function renderCounselingQueue() {
      if (!listContainer) return;
      const query = (searchInput ? searchInput.value : "").trim().toLowerCase();

      let sorted = [...students].sort((a, b) => {
        const flagA = a.counseling ? a.counseling.flagCount : 0;
        const flagB = b.counseling ? b.counseling.flagCount : 0;
        if (flagB !== flagA) return flagB - flagA;
        return a.mean - b.mean;
      });

      if (query) {
        sorted = sorted.filter(s => s.id.toLowerCase().includes(query) || s.success.toLowerCase().includes(query) || (s.demographics && s.demographics.major.toLowerCase().includes(query)));
      }

      listContainer.innerHTML = sorted.slice(0, 30).map(s => {
        const c = s.counseling || {};
        const isCurrent = activeCounselingStudent && activeCounselingStudent.id === s.id;
        const major = s.demographics ? s.demographics.major.split("&")[0].trim() : "";
        return `
          <div class="counseling-queue-item" data-id="${s.id}" style="
            background: ${isCurrent ? 'rgba(99, 102, 241, 0.25)' : 'rgba(255, 255, 255, 0.03)'};
            border: 1px solid ${isCurrent ? '#6366f1' : 'var(--border-subtle)'};
            border-radius: 8px; padding: 10px 12px; cursor: pointer; transition: var(--transition);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <strong style="font-family: var(--font-mono); color: #67e8f9;">${s.id}</strong>
              <span class="badge" style="background: ${c.priorityColor}22; color: ${c.priorityColor}; font-size: 0.72rem;">
                ${c.flagCount || 0} Risk Flags
              </span>
            </div>
            <div style="font-size: 0.76rem; color: #a5b4fc; margin-bottom: 3px;">${major}</div>
            <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: var(--text-secondary);">
              <span>Score: <strong style="color: #fff;">${s.mean.toFixed(2)}</strong> (${s.success})</span>
              <span style="color: #f87171;">${s.risk} Dropout Risk</span>
            </div>
          </div>
        `;
      }).join("");

      listContainer.querySelectorAll(".counseling-queue-item").forEach(el => {
        el.addEventListener("click", () => {
          const sId = el.getAttribute("data-id");
          loadCounselingDossier(sId);
          renderCounselingQueue();
        });
      });
    }

    function loadCounselingDossier(studentId) {
      const student = students.find(s => s.id === studentId) || students[0];
      if (!student) return;
      activeCounselingStudent = student;

      const c = student.counseling;
      if (!c) return;

      document.getElementById("ai-dossier-id").textContent = student.id;
      document.getElementById("ai-dossier-priority").textContent = c.priority;
      document.getElementById("ai-dossier-priority").style.background = `${c.priorityColor}25`;
      document.getElementById("ai-dossier-priority").style.color = c.priorityColor;
      document.getElementById("ai-dossier-priority").style.border = `1px solid ${c.priorityColor}66`;

      const dm = student.demographics || {};
      document.getElementById("ai-dossier-subtitle").textContent = 
        `${dm.major || ''} • ${dm.academicYear || ''} • GPA: ${dm.priorGPA || 'N/A'} • Score: ${student.mean.toFixed(2)}/5.00 • ${student.success} Tier • ${student.risk} Risk`;

      const flagsEl = document.getElementById("ai-dossier-flags");
      if (flagsEl) {
        if (c.activeFlags.length === 0) {
          flagsEl.innerHTML = `<span class="badge badge-flag-safe">✓ No Severe Clinical Risk Flags Active</span>`;
        } else {
          flagsEl.innerHTML = c.activeFlags.map(f => `
            <span class="badge badge-flag-danger">⚠️ ${f}</span>
          `).join("");
        }
      }

      const rootEl = document.getElementById("ai-dossier-root-causes");
      if (rootEl) {
        rootEl.innerHTML = c.rootCauses.map(rc => `<li>${rc}</li>`).join("");
      }

      const planEl = document.getElementById("ai-dossier-action-plan");
      if (planEl) {
        planEl.innerHTML = c.actionPlan.map(step => `
          <div class="timeline-step">
            <div class="timeline-title">${step.week}</div>
            <div class="timeline-obj">🎯 Objective: ${step.objective}</div>
            <ul class="timeline-actions">
              ${step.actions.map(a => `<li>${a}</li>`).join("")}
            </ul>
          </div>
        `).join("");
      }

      const qEl = document.getElementById("ai-dossier-questions");
      if (qEl) {
        qEl.innerHTML = c.counselorQuestions.map(q => `<li>${q}</li>`).join("");
      }

      const habitsEl = document.getElementById("ai-dossier-habits");
      if (habitsEl) {
        habitsEl.innerHTML = c.dailyHabits.map(h => `<li>${h}</li>`).join("");
      }
    }

    if (searchInput) searchInput.addEventListener("input", renderCounselingQueue);

    if (btnCopy) {
      btnCopy.addEventListener("click", () => {
        if (!activeCounselingStudent) return;
        const s = activeCounselingStudent;
        const c = s.counseling;
        const text = `
=== AI CLINICAL COUNSELING DOSSIER ===
Student: ${s.id}
Major: ${s.demographics ? s.demographics.major : 'N/A'} | Year: ${s.demographics ? s.demographics.academicYear : 'N/A'}
Overall Score: ${s.mean.toFixed(2)} | Success Tier: ${s.success} | Dropout Risk: ${s.risk}
Priority: ${c.priority}

ACTIVE RISK TRIGGERS:
${c.activeFlags.join("\n") || "None"}

ROOT CAUSE ANALYSIS:
${c.rootCauses.join("\n")}

4-WEEK RECOVERY ROADMAP:
${c.actionPlan.map(p => `${p.week}\nObjective: ${p.objective}\n${p.actions.map(a => ` - ${a}`).join("\n")}`).join("\n\n")}

COUNSELOR 1-ON-1 SCRIPT:
${c.counselorQuestions.join("\n")}

DAILY HABIT STACK:
${c.dailyHabits.join("\n")}
======================================
        `.trim();
        navigator.clipboard.writeText(text).then(() => {
          btnCopy.textContent = "✓ Copied to Clipboard!";
          setTimeout(() => { btnCopy.textContent = "Copy Counseling Dossier"; }, 2000);
        });
      });
    }

    const firstUnderperforming = students.find(s => s.success === "Bad" || s.risk === "High") || students[0];
    if (firstUnderperforming) {
      loadCounselingDossier(firstUnderperforming.id);
    }
    renderCounselingQueue();
  }

  // --- 6. 17-Domain Deep-Dive Tab ---
  function initDomainsTab() {
    const ctxBar = document.getElementById("chart-domain-bar");
    const metricSelect = document.getElementById("select-domain-metric");

    function renderDomainBar() {
      const metric = metricSelect ? metricSelect.value : "mean";
      if (!ctxBar) return;
      if (chartInstances.domainBar) chartInstances.domainBar.destroy();

      let datasetData, label, colorGrad, minVal, maxVal;
      if (metric === "mean") {
        datasetData = domains.map(d => d.mean);
        label = "Mean Score (1 - 5 Scale)";
        colorGrad = "#6366f1";
        minVal = 2.5;
        maxVal = 3.5;
      } else if (metric === "cronbach") {
        datasetData = domains.map(d => d.cronbachAlpha);
        label = "Cronbach's Alpha (Reliability Index)";
        colorGrad = "#10b981";
        minVal = 0.75;
        maxVal = 0.90;
      } else {
        datasetData = domains.map(d => d.std);
        label = "Standard Deviation";
        colorGrad = "#06b6d4";
        minVal = 0.45;
        maxVal = 0.70;
      }

      chartInstances.domainBar = new Chart(ctxBar, {
        type: "bar",
        data: {
          labels: domains.map(d => d.name),
          datasets: [{
            label: label,
            data: datasetData,
            backgroundColor: domains.map(d => d.isNew ? "#06b6d4" : colorGrad),
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              grid: { display: false },
              ticks: { color: "#cbd5e1", font: { size: 10, weight: "500" }, maxRotation: 45, minRotation: 35 }
            },
            y: { min: minVal, max: maxVal, grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: { legend: { display: true, labels: { font: { weight: "600" } } } }
        }
      });
    }

    if (metricSelect) metricSelect.addEventListener("change", renderDomainBar);
    renderDomainBar();

    const ctxSpread = document.getElementById("chart-domain-spread");
    if (ctxSpread) {
      if (chartInstances.domainSpread) chartInstances.domainSpread.destroy();

      chartInstances.domainSpread = new Chart(ctxSpread, {
        type: "bar",
        data: {
          labels: domains.map(d => d.code),
          datasets: [
            {
              label: "Q1 - Q3 Range (IQR)",
              data: domains.map(d => [d.q1, d.q3]),
              backgroundColor: "rgba(99, 102, 241, 0.45)",
              borderColor: "#6366f1",
              borderWidth: 1,
              borderRadius: 4
            },
            {
              label: "Full Min - Max Range",
              data: domains.map(d => [d.min, d.max]),
              backgroundColor: "rgba(6, 182, 212, 0.15)",
              borderColor: "rgba(6, 182, 212, 0.4)",
              borderWidth: 1,
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { weight: "600" } } },
            y: { min: 1.5, max: 4.5, grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } }
          },
          plugins: {
            legend: { position: "top", labels: { boxWidth: 12, font: { size: 11 } } },
            tooltip: {
              callbacks: {
                title: items => {
                  const idx = items[0].dataIndex;
                  return `${domains[idx].name} (${domains[idx].code})${domains[idx].isNew ? ' [NEW]' : ''}`;
                }
              }
            }
          }
        }
      });
    }

    const tbody = document.getElementById("tbody-domain-summary");
    if (tbody) {
      tbody.innerHTML = domains.map(d => {
        const gap = (d.tierMeans["Excellent"] - d.tierMeans["Bad"]).toFixed(2);
        return `
          <tr>
            <td><strong>${d.name}</strong> ${d.isNew ? '<span class="badge" style="background: rgba(6, 182, 212, 0.2); color: #38bdf8; font-size: 0.68rem; padding: 1px 5px;">NEW</span>' : ''}</td>
            <td><span style="font-family: var(--font-mono); color: #94a3b8;">${d.questionRange}</span></td>
            <td><span style="font-family: var(--font-mono); color: #67e8f9;">${d.mean.toFixed(3)}</span></td>
            <td><span style="font-family: var(--font-mono);">${d.std.toFixed(3)}</span></td>
            <td><span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">${d.cronbachAlpha.toFixed(4)}</span></td>
            <td><span style="font-family: var(--font-mono); color: #a5b4fc;">+${gap}</span></td>
          </tr>
        `;
      }).join("");
    }
  }

  // --- 7. 255-Item Psychometrics Tab ---
  function initQuestionsTab() {
    const domainSelect = document.getElementById("select-filter-domain");
    const searchInput = document.getElementById("input-search-questions");
    const sortSelect = document.getElementById("select-sort-questions");
    const tbody = document.getElementById("tbody-questions");
    const topBottomContainer = document.getElementById("container-top-bottom-questions");

    if (domainSelect) {
      domains.forEach(d => {
        const opt = document.createElement("option");
        opt.value = d.name;
        opt.textContent = `${d.name} (${d.questionRange})${d.isNew ? ' [NEW]' : ''}`;
        domainSelect.appendChild(opt);
      });
    }

    if (topBottomContainer) {
      const sortedByMean = [...questions].sort((a, b) => b.mean - a.mean);
      const top5 = sortedByMean.slice(0, 5);
      const bottom5 = sortedByMean.slice(-5).reverse();

      topBottomContainer.innerHTML = `
        <div style="margin-bottom: 8px;">
          <div style="font-weight: 700; color: #34d399; margin-bottom: 4px;">Top 5 Highest Scoring Items:</div>
          ${top5.map(q => `
            <div style="display: flex; justify-content: space-between; padding: 4px 8px; background: rgba(16, 185, 129, 0.08); border-radius: 4px; margin-bottom: 3px;">
              <span><strong>${q.code}</strong>: ${q.title} (${q.domainCode})</span>
              <span style="font-family: var(--font-mono); color: #34d399; font-weight: 700;">${q.mean.toFixed(2)}</span>
            </div>
          `).join("")}
        </div>
        <div>
          <div style="font-weight: 700; color: #f87171; margin-bottom: 4px;">Top 5 Most Challenging Items (Lowest Mean):</div>
          ${bottom5.map(q => `
            <div style="display: flex; justify-content: space-between; padding: 4px 8px; background: rgba(239, 68, 68, 0.08); border-radius: 4px; margin-bottom: 3px;">
              <span><strong>${q.code}</strong>: ${q.title} (${q.domainCode})</span>
              <span style="font-family: var(--font-mono); color: #f87171; font-weight: 700;">${q.mean.toFixed(2)}</span>
            </div>
          `).join("")}
        </div>
      `;
    }

    const ctxScatter = document.getElementById("chart-item-scatter");
    if (ctxScatter) {
      if (chartInstances.itemScatter) chartInstances.itemScatter.destroy();

      const scatterData = questions.map(q => ({
        x: q.difficulty,
        y: q.discriminationDomain,
        code: q.code,
        title: q.title,
        domain: q.domain,
        isNew: q.isNew
      }));

      chartInstances.itemScatter = new Chart(ctxScatter, {
        type: "scatter",
        data: {
          datasets: [{
            label: "255 Items",
            data: scatterData,
            backgroundColor: scatterData.map(d => d.isNew ? "rgba(6, 182, 212, 0.7)" : "rgba(99, 102, 241, 0.6)"),
            borderColor: "#818cf8",
            borderWidth: 1,
            pointRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              min: 0.30,
              max: 0.70,
              grid: { color: "rgba(255, 255, 255, 0.06)" },
              ticks: { color: "#94a3b8" },
              title: { display: true, text: "Item Difficulty Index (P)", color: "#64748b" }
            },
            y: {
              min: 0.35,
              max: 0.75,
              grid: { color: "rgba(255, 255, 255, 0.06)" },
              ticks: { color: "#94a3b8" },
              title: { display: true, text: "Item Discrimination Index (r_it)", color: "#64748b" }
            }
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: item => {
                  const raw = item.raw;
                  return `${raw.code}: ${raw.title} (${raw.domain}) | P=${raw.x.toFixed(3)}, r=${raw.y.toFixed(3)}`;
                }
              }
            }
          }
        }
      });
    }

    function renderQuestionList() {
      if (!tbody) return;
      const query = (searchInput ? searchInput.value : "").trim().toLowerCase();
      const domainFilter = domainSelect ? domainSelect.value : "ALL";
      const sortBy = sortSelect ? sortSelect.value : "number-asc";

      let filtered = questions.filter(q => {
        const matchesDomain = domainFilter === "ALL" || q.domain === domainFilter;
        const matchesQuery = !query || q.code.toLowerCase().includes(query) || q.title.toLowerCase().includes(query) || q.domain.toLowerCase().includes(query);
        return matchesDomain && matchesQuery;
      });

      if (sortBy === "number-asc") {
        filtered.sort((a, b) => a.number - b.number);
      } else if (sortBy === "mean-desc") {
        filtered.sort((a, b) => b.mean - a.mean);
      } else if (sortBy === "mean-asc") {
        filtered.sort((a, b) => a.mean - b.mean);
      } else if (sortBy === "disc-desc") {
        filtered.sort((a, b) => b.discriminationDomain - a.discriminationDomain);
      } else if (sortBy === "std-desc") {
        filtered.sort((a, b) => b.std - a.std);
      }

      tbody.innerHTML = filtered.map(q => {
        const p1 = q.frequencyPct["1"] || 0;
        const p2 = q.frequencyPct["2"] || 0;
        const p3 = q.frequencyPct["3"] || 0;
        const p4 = q.frequencyPct["4"] || 0;
        const p5 = q.frequencyPct["5"] || 0;

        return `
          <tr>
            <td><strong style="font-family: var(--font-mono); color: #67e8f9;">${q.code}</strong> ${q.isNew ? '<span class="badge" style="background: rgba(6, 182, 212, 0.2); color: #38bdf8; font-size: 0.65rem; padding: 1px 4px;">NEW</span>' : ''}</td>
            <td><strong>${q.title}</strong></td>
            <td><span class="badge" style="background: rgba(255, 255, 255, 0.06); color: #cbd5e1;">${q.domainCode}</span></td>
            <td><span style="font-family: var(--font-mono); color: #ffffff;">${q.mean.toFixed(2)}</span></td>
            <td><span style="font-family: var(--font-mono); color: #94a3b8;">${q.std.toFixed(2)}</span></td>
            <td><span style="font-family: var(--font-mono); color: #cbd5e1;">${q.difficulty.toFixed(3)}</span></td>
            <td><span class="badge" style="background: rgba(99, 102, 241, 0.15); color: #a5b4fc;">${q.discriminationDomain.toFixed(3)}</span></td>
            <td>
              <div class="likert-bar-stack" title="1★: ${p1}%, 2★: ${p2}%, 3★: ${p3}%, 4★: ${p4}%, 5★: ${p5}%">
                <div class="likert-seg-1" style="width: ${p1}%;"></div>
                <div class="likert-seg-2" style="width: ${p2}%;"></div>
                <div class="likert-seg-3" style="width: ${p3}%;"></div>
                <div class="likert-seg-4" style="width: ${p4}%;"></div>
                <div class="likert-seg-5" style="width: ${p5}%;"></div>
              </div>
            </td>
          </tr>
        `;
      }).join("");
    }

    if (domainSelect) domainSelect.addEventListener("change", renderQuestionList);
    if (searchInput) searchInput.addEventListener("input", renderQuestionList);
    if (sortSelect) sortSelect.addEventListener("change", renderQuestionList);
    renderQuestionList();
  }

  // --- 8. 17x17 Correlation Heatmap Tab ---
  function initCorrelationsTab() {
    const table = document.getElementById("table-correlation-heatmap");
    if (table) {
      const domainCodes = data.domainCodes;
      const matrix = data.correlationMatrix;

      let html = "<thead><tr><th>Domain</th>";
      domainCodes.forEach(code => {
        html += `<th title="${code}">${code}</th>`;
      });
      html += "</tr></thead><tbody>";

      matrix.forEach((row, i) => {
        html += `<tr><th>${domainCodes[i]}</th>`;
        row.forEach((val, j) => {
          const bg = getHeatmapColor(val);
          const title = `${domains[i].name} & ${domains[j].name}: r = ${val.toFixed(3)}`;
          html += `<td class="heatmap-cell" style="background: ${bg};" title="${title}">${val.toFixed(2)}</td>`;
        });
        html += "</tr>";
      });
      html += "</tbody>";
      table.innerHTML = html;
    }

    const ctxOverallCorr = document.getElementById("chart-overall-corr");
    if (ctxOverallCorr) {
      if (chartInstances.overallCorr) chartInstances.overallCorr.destroy();

      const sortedCorr = [...domains].sort((a, b) => data.domainOverallCorr[b.name] - data.domainOverallCorr[a.name]);

      chartInstances.overallCorr = new Chart(ctxOverallCorr, {
        type: "bar",
        data: {
          labels: sortedCorr.map(d => d.name),
          datasets: [{
            label: "Correlation with Overall Mean (r)",
            data: sortedCorr.map(d => data.domainOverallCorr[d.name]),
            backgroundColor: sortedCorr.map(d => d.isNew ? "rgba(6, 182, 212, 0.75)" : "rgba(99, 102, 241, 0.7)"),
            borderRadius: 4
          }]
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { min: 0.85, max: 0.98, grid: { color: "rgba(255, 255, 255, 0.06)" }, ticks: { color: "#94a3b8" } },
            y: { grid: { display: false }, ticks: { color: "#cbd5e1", font: { size: 10 } } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }
  }

  // --- 9. Student 360° Directory Tab ---
  let currentStudentPage = 1;
  const pageSize = 25;

  function initStudentsTab() {
    const searchInput = document.getElementById("input-search-student");
    const filterMajor = document.getElementById("select-filter-major");
    const filterYear = document.getElementById("select-filter-year");
    const filterFirstGen = document.getElementById("select-filter-firstgen");
    const filterSuccess = document.getElementById("select-filter-success");
    const filterRisk = document.getElementById("select-filter-risk");
    const filterDiag = document.getElementById("select-filter-diag");
    const sortSelect = document.getElementById("select-student-sort");
    const tbody = document.getElementById("tbody-students");
    const paginationInfo = document.getElementById("student-pagination-info");
    const paginationBtns = document.getElementById("student-pagination-btns");

    // Populate majors dropdown
    if (filterMajor && demographics && demographics.byMajor) {
      demographics.byMajor.forEach(m => {
        const opt = document.createElement("option");
        opt.value = m.category;
        opt.textContent = m.category;
        filterMajor.appendChild(opt);
      });
    }

    function renderStudents() {
      if (!tbody) return;
      const query = (searchInput ? searchInput.value : "").trim().toLowerCase();
      const majF = filterMajor ? filterMajor.value : "ALL";
      const yearF = filterYear ? filterYear.value : "ALL";
      const fgF = filterFirstGen ? filterFirstGen.value : "ALL";
      const succ = filterSuccess ? filterSuccess.value : "ALL";
      const risk = filterRisk ? filterRisk.value : "ALL";
      const diagF = filterDiag ? filterDiag.value : "ALL";
      const sortBy = sortSelect ? sortSelect.value : "id-asc";

      let filtered = students.filter(s => {
        const dm = s.demographics || {};
        const matchesQuery = !query || s.id.toLowerCase().includes(query) || (dm.major && dm.major.toLowerCase().includes(query));
        const matchesMaj = majF === "ALL" || dm.major === majF;
        const matchesYear = yearF === "ALL" || dm.academicYear === yearF;
        const matchesFg = fgF === "ALL" || dm.admissionCategory === fgF || dm.firstGen === fgF;
        const matchesSucc = succ === "ALL" || s.success === succ;
        const matchesRisk = risk === "ALL" || s.risk === risk;
        
        let matchesDiag = true;
        if (diagF !== "ALL" && s.diagnostics) {
          matchesDiag = s.diagnostics[diagF] && s.diagnostics[diagF].isFlagged;
        }

        return matchesQuery && matchesMaj && matchesYear && matchesFg && matchesSucc && matchesRisk && matchesDiag;
      });

      if (sortBy === "id-asc") {
        filtered.sort((a, b) => a.id.localeCompare(b.id));
      } else if (sortBy === "mean-desc") {
        filtered.sort((a, b) => b.mean - a.mean);
      } else if (sortBy === "mean-asc") {
        filtered.sort((a, b) => a.mean - b.mean);
      } else if (sortBy === "gpa-desc") {
        filtered.sort((a, b) => (b.demographics ? b.demographics.priorGPA : 0) - (a.demographics ? a.demographics.priorGPA : 0));
      }

      const totalFiltered = filtered.length;
      const totalPages = Math.ceil(totalFiltered / pageSize) || 1;
      if (currentStudentPage > totalPages) currentStudentPage = 1;

      const startIndex = (currentStudentPage - 1) * pageSize;
      const pageData = filtered.slice(startIndex, startIndex + pageSize);

      if (paginationInfo) {
        const endRange = Math.min(startIndex + pageSize, totalFiltered);
        paginationInfo.textContent = `Showing ${totalFiltered === 0 ? 0 : startIndex + 1} - ${endRange} of ${totalFiltered} students (Total Cohort: ${kpis.totalStudents})`;
      }

      tbody.innerHTML = pageData.map(s => {
        const dm = s.demographics || {};
        const d = s.diagnostics || {};
        const flags = [];
        if (d.interest && d.interest.isFlagged) flags.push("Disinterested");
        if (d.procrastination && d.procrastination.isFlagged) flags.push("Procrastinating");
        if (d.screenFatigue && d.screenFatigue.isFlagged) flags.push("Screen Fatigue");
        if (d.mentalBurnout && d.mentalBurnout.isFlagged) flags.push("Burnout");
        if (d.courseFailure && d.courseFailure.isFlagged) flags.push("Course Failure");

        const flagBadges = flags.length > 0 
          ? flags.slice(0, 2).map(f => `<span class="badge badge-flag-danger" style="font-size: 0.7rem; padding: 1px 6px;">${f}</span>`).join(" ") + (flags.length > 2 ? ` <span style="font-size: 0.72rem; color: #f87171;">+${flags.length - 2}</span>` : "")
          : `<span class="badge badge-flag-safe" style="font-size: 0.7rem;">Clear</span>`;

        return `
          <tr class="clickable-row" data-student-id="${s.id}">
            <td><strong style="font-family: var(--font-mono); color: #67e8f9;">${s.id}</strong></td>
            <td><span style="color: #cbd5e1; font-size: 0.82rem;">${dm.major || 'N/A'}</span></td>
            <td><span style="font-size: 0.78rem; color: #94a3b8;">${dm.academicYear || ''} • ${dm.gender || ''}</span></td>
            <td><span style="font-family: var(--font-mono); font-weight: 700; color: #ffffff;">${s.mean.toFixed(2)}</span></td>
            <td><span style="font-family: var(--font-mono); color: #34d399;">${dm.priorGPA ? dm.priorGPA.toFixed(2) : 'N/A'}</span></td>
            <td>${formatBadge("success", s.success)}</td>
            <td>${formatBadge("risk", s.risk)}</td>
            <td>${flagBadges}</td>
            <td>
              <button class="btn btn-secondary btn-inspect" data-student-id="${s.id}" style="padding: 4px 10px; font-size: 0.76rem;">
                360° Profile
              </button>
            </td>
          </tr>
        `;
      }).join("");

      if (paginationBtns) {
        let btnsHtml = `
          <button class="page-btn" ${currentStudentPage === 1 ? "disabled" : ""} data-page="${currentStudentPage - 1}">Prev</button>
        `;

        const startPage = Math.max(1, currentStudentPage - 2);
        const endPage = Math.min(totalPages, currentStudentPage + 2);

        for (let p = startPage; p <= endPage; p++) {
          btnsHtml += `<button class="page-btn ${p === currentStudentPage ? "active" : ""}" data-page="${p}">${p}</button>`;
        }

        btnsHtml += `
          <button class="page-btn" ${currentStudentPage === totalPages ? "disabled" : ""} data-page="${currentStudentPage + 1}">Next</button>
        `;
        paginationBtns.innerHTML = btnsHtml;

        paginationBtns.querySelectorAll(".page-btn:not(:disabled)").forEach(b => {
          b.addEventListener("click", () => {
            currentStudentPage = parseInt(b.getAttribute("data-page"), 10);
            renderStudents();
          });
        });
      }

      tbody.querySelectorAll(".clickable-row, .btn-inspect").forEach(el => {
        el.addEventListener("click", () => {
          const sId = el.getAttribute("data-student-id");
          if (sId) openStudentModal(sId);
        });
      });
    }

    [searchInput, filterMajor, filterYear, filterFirstGen, filterSuccess, filterRisk, filterDiag, sortSelect].forEach(ctrl => {
      if (ctrl) {
        ctrl.addEventListener("change", () => { currentStudentPage = 1; renderStudents(); });
        if (ctrl.tagName === "INPUT") {
          ctrl.addEventListener("input", () => { currentStudentPage = 1; renderStudents(); });
        }
      }
    });

    renderStudents();
  }

  // --- Student 360° Modal Engine ---
  function openStudentModal(studentId) {
    const student = students.find(s => s.id === studentId);
    if (!student) return;

    const modal = document.getElementById("student-modal");
    if (!modal) return;

    const dm = student.demographics || {};
    document.getElementById("modal-student-id").textContent = `${student.id} - 360° Student Assessment`;
    document.getElementById("modal-demographics-text").innerHTML = `
      <strong>${dm.major || ''}</strong> &bull; ${dm.academicYear || ''} &bull; Age ${dm.age || 20} &bull; ${dm.housing || ''} &bull; Prior GPA: <strong style="color: #34d399;">${dm.priorGPA ? dm.priorGPA.toFixed(2) : 'N/A'}</strong> &bull; Attendance: ${dm.attendancePct || 85}% &bull; First-Gen: ${dm.firstGen || 'No'} &bull; Job: ${dm.jobHours || '0 hrs'}
    `;

    document.getElementById("modal-overall-mean").textContent = student.mean.toFixed(2);
    document.getElementById("modal-student-badges").innerHTML = `
      ${formatBadge("success", student.success)}
      ${formatBadge("risk", student.risk)}
      ${formatBadge("career", student.career)}
    `;

    const diagPills = document.getElementById("modal-diag-pills");
    if (diagPills && student.diagnostics) {
      const d = student.diagnostics;
      const pillMap = [
        { label: "Interest", flag: d.interest.isFlagged, text: d.interest.status },
        { label: "Collaboration", flag: d.collaboration.isFlagged, text: d.collaboration.status },
        { label: "Procrastination", flag: d.procrastination.isFlagged, text: d.procrastination.status },
        { label: "Screen Fatigue", flag: d.screenFatigue.isFlagged, text: d.screenFatigue.status },
        { label: "Skipping Risk", flag: d.chronicSkipping.isFlagged, text: d.chronicSkipping.status },
        { label: "Mental Burnout", flag: d.mentalBurnout.isFlagged, text: d.mentalBurnout.status },
        { label: "Course Standing", flag: d.courseFailure.isFlagged, text: d.courseFailure.status }
      ];

      diagPills.innerHTML = pillMap.map(p => `
        <span class="badge ${p.flag ? 'badge-flag-danger' : 'badge-flag-safe'}" style="font-size: 0.74rem;">
          ${p.flag ? '⚠️' : '✓'} ${p.label}: ${p.text}
        </span>
      `).join("");
    }

    const btnOpenCounseling = document.getElementById("btn-modal-open-counseling");
    if (btnOpenCounseling) {
      btnOpenCounseling.onclick = () => {
        modal.classList.remove("active");
        switchTab("counseling");
        const searchCounseling = document.getElementById("input-counseling-search");
        if (searchCounseling) {
          searchCounseling.value = student.id;
          searchCounseling.dispatchEvent(new Event("input"));
        }
      };
    }

    const domainEntries = Object.entries(student.scores).sort((a, b) => b[1] - a[1]);
    const top3Strengths = domainEntries.slice(0, 3);
    const bottom3Growth = domainEntries.slice(-3).reverse();

    const strengthsList = document.getElementById("modal-strengths-list");
    if (strengthsList) {
      strengthsList.innerHTML = top3Strengths.map(([name, score]) => `
        <li><strong>${name}</strong>: <span style="font-family: var(--font-mono); font-weight: 700;">${score.toFixed(2)}</span></li>
      `).join("");
    }

    const growthList = document.getElementById("modal-growth-list");
    if (growthList) {
      growthList.innerHTML = bottom3Growth.map(([name, score]) => `
        <li><strong>${name}</strong>: <span style="font-family: var(--font-mono); font-weight: 700;">${score.toFixed(2)}</span></li>
      `).join("");
    }

    const recEl = document.getElementById("modal-recommendation-text");
    if (recEl) {
      if (student.counseling) {
        recEl.innerHTML = `<strong>${student.counseling.priority}:</strong> ${student.counseling.rootCauses[0] || 'Maintain current study rhythm.'}`;
      } else {
        recEl.textContent = "Maintain regular academic advisement check-ins.";
      }
    }

    // Modal Radar Chart (17 Domains)
    const ctxRadarModal = document.getElementById("chart-modal-radar");
    if (ctxRadarModal) {
      if (chartInstances.modalRadar) chartInstances.modalRadar.destroy();

      const labels = domains.map(d => d.code);
      const studentVals = domains.map(d => student.scores[d.name]);
      const cohortMeans = domains.map(d => d.mean);

      chartInstances.modalRadar = new Chart(ctxRadarModal, {
        type: "radar",
        data: {
          labels: labels,
          datasets: [
            {
              label: `${student.id} Score`,
              data: studentVals,
              borderColor: "#06b6d4",
              backgroundColor: "rgba(6, 182, 212, 0.25)",
              borderWidth: 2,
              pointRadius: 4
            },
            {
              label: "Cohort Mean (N=2,525)",
              data: cohortMeans,
              borderColor: "rgba(255, 255, 255, 0.3)",
              backgroundColor: "rgba(255, 255, 255, 0.05)",
              borderWidth: 1.5,
              borderDash: [4, 4],
              pointRadius: 2
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              min: 1.0,
              max: 5.0,
              grid: { color: "rgba(255, 255, 255, 0.08)" },
              angleLines: { color: "rgba(255, 255, 255, 0.08)" },
              pointLabels: { color: "#cbd5e1", font: { size: 9, weight: "600" } },
              ticks: { backdropColor: "transparent", color: "#64748b", stepSize: 1.0 }
            }
          },
          plugins: {
            legend: { position: "top", labels: { boxWidth: 10, font: { size: 11 } } }
          }
        }
      });
    }

    const barsGrid = document.getElementById("modal-domain-bars-grid");
    if (barsGrid) {
      barsGrid.innerHTML = domains.map(d => {
        const score = student.scores[d.name] || 0;
        const pct = ((score / 5.0) * 100).toFixed(0);
        return `
          <div style="background: rgba(255, 255, 255, 0.03); padding: 8px 10px; border-radius: 6px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between; font-size: 0.76rem; margin-bottom: 4px;">
              <span style="color: #cbd5e1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 140px;" title="${d.name}">${d.name}</span>
              <span style="font-family: var(--font-mono); font-weight: 700; color: #67e8f9;">${score.toFixed(2)}</span>
            </div>
            <div class="domain-bar-bg">
              <div class="domain-bar-fill" style="width: ${pct}%;"></div>
            </div>
          </div>
        `;
      }).join("");
    }

    modal.classList.add("active");
  }

  const btnCloseModal = document.getElementById("btn-close-modal");
  const modalOverlay = document.getElementById("student-modal");
  if (btnCloseModal) btnCloseModal.addEventListener("click", () => modalOverlay.classList.remove("active"));
  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) modalOverlay.classList.remove("active");
    });
  }

  // --- 10. What-If Simulator Tab (17 Domains) ---
  function initSimulatorTab() {
    const slidersContainer = document.getElementById("simulator-sliders-container");
    if (!slidersContainer) return;

    slidersContainer.innerHTML = domains.map((d, idx) => {
      return `
        <div class="slider-group">
          <div class="slider-label-row">
            <span>${d.name} ${d.isNew ? '<span style="color: #06b6d4; font-size: 0.7rem;">[NEW]</span>' : ''}</span>
            <span class="slider-value-pill" id="sim-val-${idx}">3.00</span>
          </div>
          <input type="range" class="range-slider sim-slider" id="sim-slider-${idx}" min="1.0" max="5.0" step="0.05" value="3.00" data-index="${idx}" data-domain="${d.name}" />
        </div>
      `;
    }).join("");

    const sliders = document.querySelectorAll(".sim-slider");
    const ctxSimRadar = document.getElementById("chart-sim-radar");

    function updateSimulation() {
      const sliderVals = Array.from(sliders).map(s => parseFloat(s.value));
      
      sliderVals.forEach((val, idx) => {
        const labelEl = document.getElementById(`sim-val-${idx}`);
        if (labelEl) labelEl.textContent = val.toFixed(2);
      });

      const simMean = sliderVals.reduce((a, b) => a + b, 0) / sliderVals.length;
      document.getElementById("sim-pred-mean").textContent = `${simMean.toFixed(2)} / 5.00`;

      let predSuccess = "Average";
      if (simMean >= 3.65) predSuccess = "Excellent";
      else if (simMean >= 3.20) predSuccess = "Good";
      else if (simMean >= 2.80) predSuccess = "Average";
      else if (simMean >= 2.40) predSuccess = "Poor";
      else predSuccess = "Bad";

      let predRisk = "Medium";
      if (simMean >= 3.45) predRisk = "Low";
      else if (simMean >= 2.85) predRisk = "Medium";
      else predRisk = "High";

      let predCareer = "Moderately Ready";
      if (simMean >= 3.65) predCareer = "Highly Ready";
      else if (simMean >= 3.20) predCareer = "Ready";
      else if (simMean >= 2.75) predCareer = "Moderately Ready";
      else predCareer = "Not Ready";

      document.getElementById("sim-pred-success").innerHTML = formatBadge("success", predSuccess);
      document.getElementById("sim-pred-risk").innerHTML = formatBadge("risk", predRisk);
      document.getElementById("sim-pred-career").innerHTML = formatBadge("career", predCareer);

      if (ctxSimRadar) {
        if (!chartInstances.simRadar) {
          chartInstances.simRadar = new Chart(ctxSimRadar, {
            type: "radar",
            data: {
              labels: domains.map(d => d.code),
              datasets: [
                {
                  label: "Simulated 17D Profile",
                  data: sliderVals,
                  borderColor: "#6366f1",
                  backgroundColor: "rgba(99, 102, 241, 0.25)",
                  borderWidth: 2,
                  pointRadius: 3
                },
                {
                  label: "Cohort Benchmark",
                  data: domains.map(d => d.mean),
                  borderColor: "rgba(255, 255, 255, 0.25)",
                  backgroundColor: "rgba(255, 255, 255, 0.05)",
                  borderWidth: 1.5,
                  borderDash: [4, 4],
                  pointRadius: 2
                }
              ]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                r: {
                  min: 1.0,
                  max: 5.0,
                  grid: { color: "rgba(255, 255, 255, 0.08)" },
                  angleLines: { color: "rgba(255, 255, 255, 0.08)" },
                  pointLabels: { color: "#cbd5e1", font: { size: 9, weight: "600" } },
                  ticks: { backdropColor: "transparent", color: "#64748b", stepSize: 1.0 }
                }
              },
              plugins: { legend: { position: "top", labels: { boxWidth: 10 } } }
            }
          });
        } else {
          chartInstances.simRadar.data.datasets[0].data = sliderVals;
          chartInstances.simRadar.update();
        }
      }
    }

    sliders.forEach(s => s.addEventListener("input", updateSimulation));

    const presetBtns = document.querySelectorAll(".sim-preset-btn");
    presetBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        const preset = btn.getAttribute("data-preset");
        if (preset === "excellent") {
          sliders.forEach(s => s.value = 4.20);
        } else if (preset === "good") {
          sliders.forEach(s => s.value = 3.50);
        } else if (preset === "average") {
          sliders.forEach(s => s.value = 3.00);
        } else if (preset === "risk") {
          sliders.forEach(s => s.value = 2.20);
        } else if (preset === "tech") {
          sliders.forEach(s => {
            const d = s.getAttribute("data-domain");
            if (d.includes("Digital") || d.includes("Critical") || d.includes("Academic")) s.value = 4.30;
            else if (d.includes("Physical") || d.includes("Communication")) s.value = 2.70;
            else s.value = 3.30;
          });
        } else if (preset === "leader") {
          sliders.forEach(s => {
            const d = s.getAttribute("data-domain");
            if (d.includes("Leadership") || d.includes("Communication") || d.includes("Emotional")) s.value = 4.40;
            else s.value = 3.40;
          });
        }
        updateSimulation();
      });
    });

    updateSimulation();
  }

  // --- 11. Header Actions (CSV Export & Print) ---
  function initHeaderActions() {
    const btnExport = document.getElementById("btn-export-csv");
    if (btnExport) {
      btnExport.addEventListener("click", () => {
        let csvContent = "data:text/csv;charset=utf-8,";
        csvContent += "Student_ID,Gender,Age,Academic_Year,Department_Major,Housing_Type,First_Gen,Prior_GPA,Overall_Mean_17D,Success_Tier,Dropout_Risk,Career_Readiness," +
          domains.map(d => `"${d.name}"`).join(",") + "\n";

        students.forEach(s => {
          const dm = s.demographics || {};
          const row = [
            s.id,
            dm.gender || "",
            dm.age || "",
            dm.academicYear || "",
            `"${dm.major || ''}"`,
            `"${dm.housing || ''}"`,
            dm.firstGen || "",
            dm.priorGPA || "",
            s.mean,
            s.success,
            s.risk,
            s.career,
            ...domains.map(dom => s.scores[dom.name] || "")
          ];
          csvContent += row.join(",") + "\n";
        });

        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "expanded_student_psychometrics_demographics.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      });
    }

    const btnPrint = document.getElementById("btn-print-report");
    if (btnPrint) {
      btnPrint.addEventListener("click", () => {
        window.print();
      });
    }
  }

  // ==========================================================================
  // MODULE: STUDENT LIVE ASSESSMENT (1-5 TEST) & REAL-TIME KUNDALI GENERATOR
  // ==========================================================================

  const testQuestions = [
    // Cluster 1: Cognitive & Academic
    { id: "q_am", cluster: 1, domain: "Academic Motivation", domainCode: "AM", label: "I am deeply driven to master complex engineering and analytical subjects with high intellectual curiosity." },
    { id: "q_lb", cluster: 1, domain: "Learning Behaviour", domainCode: "LB", label: "I maintain a structured daily revision routine and actively apply instructor feedback on coursework." },
    { id: "q_ctdm", cluster: 1, domain: "Critical Thinking & Decision Making", domainCode: "CTDM", label: "I break down complex multi-step problems methodically rather than relying on rote memorization." },
    { id: "q_ci", cluster: 1, domain: "Creativity & Innovation", domainCode: "CI", label: "I actively explore novel and creative approaches when designing software or engineering solutions." },
    
    // Cluster 2: Affective & Emotional Resilience
    { id: "q_ei", cluster: 2, domain: "Emotional Intelligence", domainCode: "EI", label: "During high-stakes timed exams, my mind stays calm, confident, and free from debilitating panic." },
    { id: "q_ra", cluster: 2, domain: "Resilience & Adaptability", domainCode: "RA", label: "When faced with an unexpected low grade or setback, I bounce back quickly with proactive adjustments." },
    { id: "q_paw", cluster: 2, domain: "Physical Activity & Wellness", domainCode: "PAW", label: "I maintain regular physical exercise, balanced nutrition, and consistent mental well-being." },
    
    // Cluster 3: Self-Regulation & Focus Discipline
    { id: "q_tm", cluster: 3, domain: "Time Management", domainCode: "TM", label: "I plan a weekly study schedule in advance and submit complex assignments comfortably before deadlines." },
    { id: "q_neu", cluster: 3, domain: "Neurodiversity, ADHD & Executive Functioning", domainCode: "NEU", label: "I can sustain deep concentration on demanding academic tasks for 45+ minutes without distractibility." },
    { id: "q_lt", cluster: 3, domain: "Leadership & Teamwork", domainCode: "LT", label: "I collaborate effectively, communicate clearly, and take initiative in peer engineering project teams." },
    { id: "q_cs", cluster: 3, domain: "Communication Skills", domainCode: "CS", label: "I articulate technical concepts confidently and actively participate in classroom discussions and seminars." },

    // Cluster 4: Digital, Career & Socioeconomic Balance
    { id: "q_dlr", cluster: 4, domain: "Digital Literacy & AI Readiness", domainCode: "DLR", label: "I leverage modern AI tools, coding frameworks, and digital repositories proficiently for technical projects." },
    { id: "q_cr", cluster: 4, domain: "Career Readiness", domainCode: "CR", label: "I regularly build real-world portfolio projects and prepare proactively for industry internship placements." },
    { id: "q_scr", cluster: 4, domain: "Screen Time, Blue Light & Digital Well-Being", domainCode: "SCR", label: "I keep late-night smartphone screen time strictly regulated and avoid digital screens 45 mins before sleep." },
    { id: "q_bel", cluster: 4, domain: "Campus Belonging & Peer Support", domainCode: "BEL", label: "I feel a strong sense of community, mentorship, and peer collaboration within the university campus." },
    { id: "q_fin", cluster: 4, domain: "Financial & Socioeconomic Well-Being", domainCode: "FIN", label: "My academic focus is stable and not disrupted by acute socioeconomic or financial stress." },
    { id: "q_lms", cluster: 4, domain: "LMS Usability & Hybrid Learning", domainCode: "LMS", label: "I actively navigate the institutional Learning Management System (LMS) for course materials and quizzes." }
  ];

  let currentTestAnswers = {};
  let liveSubmittedStudents = [];
  let counselorNotesLog = [
    {
      date: "2026-08-27 10:30 AM",
      student: "STU-0042 (Priya Patel)",
      advisor: "Dr. Alok Verma",
      type: "Test Anxiety & Cognitive Reframing Session",
      notes: "Student experienced acute panic during midterms. Prescribed 15-min mock timed tests and paired with senior peer tutor.",
      status: "In Progress (Week 2 Review)"
    },
    {
      date: "2026-08-26 03:15 PM",
      student: "STU-0118 (Rohan Gupta)",
      advisor: "Prof. S. K. Verma",
      type: "Sleep Hygiene & Digital Curfew Protocol",
      notes: "Late night gaming was causing 8 AM class skipping. Agreed to 11 PM phone docking rule. Attendance improved.",
      status: "Resolved (Tier Transition)"
    }
  ];

  function initStudentPortalTab() {
    testQuestions.forEach(q => {
      currentTestAnswers[q.domain] = 3.0; // Default Neutral 3.0
    });

    renderSurveyCards();
    updateTestProgressBar();

    // Default student preset
    loadTestPreset("high_risk");
  }

  function renderSurveyCards() {
    for (let c = 1; c <= 4; c++) {
      const container = document.getElementById(`cluster-${c}-items`);
      if (!container) continue;
      container.innerHTML = "";

      const clusterQuestions = testQuestions.filter(q => q.cluster === c);
      clusterQuestions.forEach(q => {
        const card = document.createElement("div");
        card.className = "survey-item-card";

        const currentVal = currentTestAnswers[q.domain] || 3.0;

        card.innerHTML = `
          <div class="survey-item-header">
            <span class="survey-item-domain-badge">[${q.domainCode}] ${q.domain}</span>
            <span style="font-size: 0.78rem; font-weight: 800; color: #38bdf8;" id="val-badge-${q.id}">${currentVal.toFixed(1)}/5.0</span>
          </div>
          <div class="survey-item-text">${q.label}</div>
          <div class="likert-btn-group" id="likert-group-${q.id}">
            <div class="likert-btn ${currentVal === 1 ? 'selected' : ''}" onclick="setQuestionAnswer('${q.domain}', '${q.id}', 1)">
              <span class="likert-num" style="color: #f87171;">1</span>
              <span class="likert-label">Strongly Disagree</span>
            </div>
            <div class="likert-btn ${currentVal === 2 ? 'selected' : ''}" onclick="setQuestionAnswer('${q.domain}', '${q.id}', 2)">
              <span class="likert-num" style="color: #fb923c;">2</span>
              <span class="likert-label">Disagree</span>
            </div>
            <div class="likert-btn ${currentVal === 3 ? 'selected' : ''}" onclick="setQuestionAnswer('${q.domain}', '${q.id}', 3)">
              <span class="likert-num" style="color: #cbd5e1;">3</span>
              <span class="likert-label">Neutral</span>
            </div>
            <div class="likert-btn ${currentVal === 4 ? 'selected' : ''}" onclick="setQuestionAnswer('${q.domain}', '${q.id}', 4)">
              <span class="likert-num" style="color: #38bdf8;">4</span>
              <span class="likert-label">Agree</span>
            </div>
            <div class="likert-btn ${currentVal === 5 ? 'selected' : ''}" onclick="setQuestionAnswer('${q.domain}', '${q.id}', 5)">
              <span class="likert-num" style="color: #34d399;">5</span>
              <span class="likert-label">Strongly Agree</span>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    }
  }

  window.setQuestionAnswer = function(domainName, qId, val) {
    currentTestAnswers[domainName] = parseFloat(val);
    
    // Update badge text
    const badge = document.getElementById(`val-badge-${qId}`);
    if (badge) badge.innerText = `${val}.0/5.0`;

    // Update selected class
    const group = document.getElementById(`likert-group-${qId}`);
    if (group) {
      const btns = group.querySelectorAll(".likert-btn");
      btns.forEach((b, idx) => {
        b.classList.toggle("selected", idx + 1 === val);
      });
    }

    updateTestProgressBar();
  };

  function updateTestProgressBar() {
    const answeredCount = Object.keys(currentTestAnswers).length;
    const total = testQuestions.length;
    const pct = Math.round((answeredCount / total) * 100);

    const countEl = document.getElementById("test-progress-count");
    if (countEl) countEl.innerText = `${answeredCount} / ${total} Domains Answered`;

    const badgeEl = document.getElementById("test-progress-badge");
    if (badgeEl) {
      badgeEl.innerText = `${pct}% Complete`;
      badgeEl.className = pct === 100 ? "badge badge-excellent" : "badge badge-average";
    }
  }

  window.loadTestPreset = function(preset) {
    if (preset === "high_risk") {
      document.getElementById("inp-student-name").value = "Aarav Sharma";
      document.getElementById("inp-student-roll").value = "2026UGCS086";
      document.getElementById("inp-student-branch").value = "Computer Science & Eng (CSE)";
      
      currentTestAnswers = {
        "Academic Motivation": 3.8, // Strong motivation
        "Learning Behaviour": 2.2,
        "Time Management": 1.8,   // Low
        "Emotional Intelligence": 1.6, // High Exam Panic
        "Physical Activity & Wellness": 2.0,
        "Communication Skills": 2.5,
        "Leadership & Teamwork": 2.8,
        "Critical Thinking & Decision Making": 3.4,
        "Career Readiness": 2.0,
        "Digital Literacy & AI Readiness": 3.6,
        "Creativity & Innovation": 3.2,
        "Resilience & Adaptability": 2.0,
        "Financial & Socioeconomic Well-Being": 2.6,
        "Campus Belonging & Peer Support": 2.4,
        "Neurodiversity, ADHD & Executive Functioning": 1.9,
        "Screen Time, Blue Light & Digital Well-Being": 1.6, // High screen fatigue
        "LMS Usability & Hybrid Learning": 2.8
      };
    } else if (preset === "average") {
      document.getElementById("inp-student-name").value = "Ananya Verma";
      document.getElementById("inp-student-roll").value = "2026UGECE142";
      document.getElementById("inp-student-branch").value = "Electronics & Comm (ECE)";
      
      testQuestions.forEach(q => {
        currentTestAnswers[q.domain] = 3.0;
      });
    } else if (preset === "scholar") {
      document.getElementById("inp-student-name").value = "Devendra Joshi";
      document.getElementById("inp-student-roll").value = "2026UGAI015";
      document.getElementById("inp-student-branch").value = "AI & Data Science (AI/DS)";
      
      testQuestions.forEach(q => {
        currentTestAnswers[q.domain] = 4.6;
      });
      currentTestAnswers["Emotional Intelligence"] = 4.8;
      currentTestAnswers["Time Management"] = 4.7;
    } else if (preset === "random") {
      const names = ["Ishaan Nair", "Kavya Reddy", "Rohan Mehra", "Tanvi Sengupta", "Aditya Rao", "Sneha Roy"];
      const rollNum = Math.floor(100 + Math.random() * 900);
      document.getElementById("inp-student-name").value = names[Math.floor(Math.random() * names.length)];
      document.getElementById("inp-student-roll").value = `2026UGCS${rollNum}`;
      
      testQuestions.forEach(q => {
        const rVal = Math.floor(1 + Math.random() * 5);
        currentTestAnswers[q.domain] = rVal;
      });
    }

    renderSurveyCards();
    updateTestProgressBar();
  };

  window.resetStudentTest = function() {
    testQuestions.forEach(q => {
      currentTestAnswers[q.domain] = 3.0;
    });
    renderSurveyCards();
    updateTestProgressBar();
  };

  // -------------------------------------------------------------
  // REAL-TIME MULTI-TASK NEURAL NETWORK INFERENCE CALCULATION
  // -------------------------------------------------------------
  function runNeuralPrediction(answers) {
    const vals = Object.values(answers);
    const meanScore = vals.reduce((a, b) => a + b, 0) / vals.length;

    // Weight critical risk antecedent domains (Exam Panic, Sleep Deficit, Time Mgmt)
    const examPanic = 5.0 - (answers["Emotional Intelligence"] || 3.0); // higher = more panic
    const timeDeficit = 5.0 - (answers["Time Management"] || 3.0);
    const screenDeficit = 5.0 - (answers["Screen Time, Blue Light & Digital Well-Being"] || 3.0);
    const motivation = answers["Academic Motivation"] || 3.0;

    // Multi-Task Head 1: Dropout Hazard Probability
    let hazard = 0.467; // Baseline prior E[f(x)]
    hazard += (examPanic * 0.12);
    hazard += (timeDeficit * 0.09);
    hazard += (screenDeficit * 0.08);
    hazard -= ((motivation - 3.0) * 0.07);
    hazard -= ((meanScore - 3.0) * 0.25);
    hazard = Math.max(0.08, Math.min(0.96, hazard));

    let riskTier = "Low";
    if (hazard >= 0.65) riskTier = "High";
    else if (hazard >= 0.40) riskTier = "Medium";

    // Multi-Task Head 2: Predicted Academic CGPA Tier
    let predictedCGPA = 4.0 + (meanScore / 5.0) * 5.8;
    predictedCGPA = Math.max(4.2, Math.min(9.8, predictedCGPA));

    let successTier = "Average";
    if (predictedCGPA >= 8.5) successTier = "Excellent";
    else if (predictedCGPA >= 7.2) successTier = "Good";
    else if (predictedCGPA >= 5.8) successTier = "Average";
    else if (predictedCGPA >= 5.0) successTier = "Poor";
    else successTier = "Bad";

    // Multi-Task Head 3: Career Placement Readiness
    const careerScore = ((answers["Career Readiness"] || 3.0) * 0.4) + ((answers["Digital Literacy & AI Readiness"] || 3.0) * 0.3) + ((answers["Critical Thinking & Decision Making"] || 3.0) * 0.3);
    let careerTier = "Moderately Ready";
    if (careerScore >= 4.2) careerTier = "Highly Ready";
    else if (careerScore >= 3.4) careerTier = "Ready";
    else if (careerScore >= 2.5) careerTier = "Moderately Ready";
    else careerTier = "Not Ready";

    // 4-Quadrant Psychological Kundali breakdown
    const qCognitive = ((answers["Academic Motivation"] || 3.0) + (answers["Learning Behaviour"] || 3.0) + (answers["Critical Thinking & Decision Making"] || 3.0) + (answers["Creativity & Innovation"] || 3.0)) / 4.0;
    const qAffective = ((answers["Emotional Intelligence"] || 3.0) + (answers["Resilience & Adaptability"] || 3.0) + (answers["Physical Activity & Wellness"] || 3.0)) / 3.0;
    const qSelfReg = ((answers["Time Management"] || 3.0) + (answers["Neurodiversity, ADHD & Executive Functioning"] || 3.0) + (answers["Leadership & Teamwork"] || 3.0) + (answers["Communication Skills"] || 3.0)) / 4.0;
    const qLifestyle = ((answers["Screen Time, Blue Light & Digital Well-Being"] || 3.0) + (answers["Campus Belonging & Peer Support"] || 3.0) + (answers["Financial & Socioeconomic Well-Being"] || 3.0) + (answers["Career Readiness"] || 3.0) + (answers["Digital Literacy & AI Readiness"] || 3.0) + (answers["LMS Usability & Hybrid Learning"] || 3.0)) / 6.0;

    // Game-Theoretic SHAP Attributions (Top Strengths vs Top Doshas)
    const sortedDomains = Object.entries(answers).sort((a, b) => b[1] - a[1]);
    const topStrengths = sortedDomains.slice(0, 3).map(([dName, dScore]) => ({
      name: dName,
      score: dScore,
      shapVal: `-${Math.round((dScore / 5.0) * 25)}% Attrition Reduction`
    }));

    const topDoshas = sortedDomains.slice(-3).reverse().map(([dName, dScore]) => ({
      name: dName,
      score: dScore,
      shapVal: `+${Math.round(((5.0 - dScore) / 5.0) * 32)}% Risk Driver`
    }));

    return {
      meanScore,
      hazard,
      riskTier,
      predictedCGPA,
      successTier,
      careerTier,
      quadrants: {
        cognitive: qCognitive,
        affective: qAffective,
        selfReg: qSelfReg,
        lifestyle: qLifestyle
      },
      topStrengths,
      topDoshas
    };
  }

  window.handleStudentTestSubmit = function(e) {
    if (e && e.preventDefault) e.preventDefault();

    const name = document.getElementById("inp-student-name").value.trim() || "Student";
    const rollNo = document.getElementById("inp-student-roll").value.trim() || "2026UG001";
    const branch = document.getElementById("inp-student-branch").value;
    const sem = document.getElementById("inp-student-sem").value;
    const gender = document.getElementById("inp-student-gender").value;

    const prediction = runNeuralPrediction(currentTestAnswers);

    const studentProfile = {
      id: `LIVE-${rollNo}`,
      name: name,
      rollNo: rollNo,
      branch: branch,
      semester: sem,
      gender: gender,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      answers: { ...currentTestAnswers },
      prediction: prediction
    };

    // Prepend to Live Roster for Admin Portal
    liveSubmittedStudents.unshift(studentProfile);

    // Render Student Kundali
    renderStudentKundali(studentProfile);

    // Update Admin Portal Roster
    renderAdminRoster();

    // Switch Tab to Student Kundali
    switchTab("student-kundali");
  };

  // -------------------------------------------------------------
  // RENDER STUDENT KUNDALI (कुंडली) & ACTIONABLE DOSSIER
  // -------------------------------------------------------------
  function renderStudentKundali(profile) {
    const { name, rollNo, branch, semester, timestamp, prediction } = profile;
    const p = prediction;

    // Header updates
    document.getElementById("kundali-student-name").innerText = name;
    document.getElementById("kundali-avatar").innerText = name.split(" ").map(w => w[0]).join("").toUpperCase() || "ST";
    document.getElementById("kundali-meta-text").innerHTML = `
      Roll No: <span style="color:#fff; font-family: var(--font-mono);">${rollNo}</span> &bull; 
      Branch: <span style="color:#fff;">${branch}</span> &bull; 
      Semester: <span style="color:#fff;">${semester}</span> &bull; 
      Assessment Date: <span style="color: #38bdf8;">${timestamp}</span>
    `;

    const riskPill = document.getElementById("kundali-risk-pill");
    if (p.hazard >= 0.65) {
      riskPill.className = "badge badge-risk-high";
      riskPill.innerText = `🚨 Acute Triage (Tier 3) - ${(p.hazard * 100).toFixed(1)}% Hazard`;
    } else if (p.hazard >= 0.40) {
      riskPill.className = "badge badge-risk-medium";
      riskPill.innerText = `⚖️ Targeted Support (Tier 2) - ${(p.hazard * 100).toFixed(1)}% Hazard`;
    } else {
      riskPill.className = "badge badge-risk-low";
      riskPill.innerText = `✅ Universal Safe (Tier 1) - ${(p.hazard * 100).toFixed(1)}% Retention`;
    }

    // Head 1: Hazard KPI Card
    const hazVal = document.getElementById("kundali-hazard-val");
    hazVal.innerText = `${(p.hazard * 100).toFixed(1)}%`;
    hazVal.style.color = p.hazard >= 0.65 ? "#ef4444" : (p.hazard >= 0.40 ? "#f59e0b" : "#10b981");

    document.getElementById("kundali-hazard-sub").innerHTML = p.hazard >= 0.65 
      ? `<span class="pill pill-danger">Acute Triage</span> Urgent 1-on-1 advisor counseling required`
      : (p.hazard >= 0.40 
        ? `<span class="pill pill-warning">Targeted Support</span> Peer study circle & timetable remediation`
        : `<span class="pill pill-success">Safe Retention</span> On track for seamless semester completion`);

    // Head 2: CGPA KPI Card
    document.getElementById("kundali-cgpa-val").innerText = `${p.predictedCGPA.toFixed(2)} / 10.0`;
    document.getElementById("kundali-cgpa-sub").innerHTML = `
      <span class="pill ${p.predictedCGPA < 6.0 ? 'pill-danger' : (p.predictedCGPA < 7.5 ? 'pill-warning' : 'pill-success')}">${p.successTier}</span>
      Projected Range: ${(p.predictedCGPA - 0.35).toFixed(2)} – ${(p.predictedCGPA + 0.35).toFixed(2)} CGPA
    `;

    // Head 3: Career Readiness KPI Card
    document.getElementById("kundali-career-val").innerText = p.careerTier;
    document.getElementById("kundali-career-sub").innerHTML = `
      <span class="pill pill-info">Technical & Soft Aptitude</span> Score: ${Math.round((p.meanScore / 5.0) * 100)}/100
    `;

    // Render 4-Quadrant Kundali Radar Chart
    renderKundaliRadarChart(p.quadrants);

    // Render Strengths (शुभ योग)
    const strengthsContainer = document.getElementById("kundali-strengths-list");
    strengthsContainer.innerHTML = "";
    p.topStrengths.forEach(s => {
      const item = document.createElement("div");
      item.style.cssText = "display: flex; justify-content: space-between; align-items: center; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 6px; padding: 8px 12px;";
      item.innerHTML = `
        <span style="font-size: 0.88rem; font-weight: 600; color: #a7f3d0;">• ${s.name} (${s.score.toFixed(1)}/5.0)</span>
        <span style="font-size: 0.8rem; font-weight: 800; color: #34d399;">${s.shapVal}</span>
      `;
      strengthsContainer.appendChild(item);
    });

    // Render Doshas (दोष / Vulnerabilities)
    const doshasContainer = document.getElementById("kundali-doshas-list");
    doshasContainer.innerHTML = "";
    p.topDoshas.forEach(d => {
      const item = document.createElement("div");
      item.style.cssText = "display: flex; justify-content: space-between; align-items: center; background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 6px; padding: 8px 12px;";
      item.innerHTML = `
        <span style="font-size: 0.88rem; font-weight: 600; color: #fca5a5;">• ${d.name} (${d.score.toFixed(1)}/5.0)</span>
        <span style="font-size: 0.8rem; font-weight: 800; color: #ef4444;">${d.shapVal}</span>
      `;
      doshasContainer.appendChild(item);
    });

    // Render 4-Stage Prescriptive Counseling Protocol (CCRO Roadmap)
    const stagesContainer = document.getElementById("kundali-counseling-stages");
    stagesContainer.innerHTML = `
      <div class="kpi-card" style="--card-accent: #ef4444; border: 1.5px solid rgba(239, 68, 68, 0.4); padding: 14px;">
        <div style="font-size: 0.76rem; font-weight: 800; color: #ef4444; text-transform: uppercase;">STAGE 1: WEEKS 1–2 (IMMEDIATE)</div>
        <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 4px 0;">Cognitive Anxiety Reframing</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;">Two 15-minute mock timed quizzes under zero stakes to desensitize exam panic triggers.</p>
      </div>
      <div class="kpi-card" style="--card-accent: #f59e0b; border: 1.5px solid rgba(245, 158, 11, 0.4); padding: 14px;">
        <div style="font-size: 0.76rem; font-weight: 800; color: #fbbf24; text-transform: uppercase;">STAGE 2: WEEKS 3–4 (STABILIZE)</div>
        <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 4px 0;">Sleep & Screen Curfew</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;">Implement 45-min pre-bed digital screen docking to restore 7.5 hours of restorative REM sleep.</p>
      </div>
      <div class="kpi-card" style="--card-accent: #06b6d4; border: 1.5px solid rgba(6, 182, 212, 0.4); padding: 14px;">
        <div style="font-size: 0.76rem; font-weight: 800; color: #22d3ee; text-transform: uppercase;">STAGE 3: WEEKS 5–8 (ACADEMIC)</div>
        <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 4px 0;">Peer Accountability Buddy</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;">3 hours/week structured study circle with high-performing sophomores in ${branch.split('(')[0]}.</p>
      </div>
      <div class="kpi-card" style="--card-accent: #10b981; border: 1.5px solid rgba(16, 185, 129, 0.4); padding: 14px;">
        <div style="font-size: 0.76rem; font-weight: 800; color: #34d399; text-transform: uppercase;">STAGE 4: WEEKS 12–14 (RETENTION)</div>
        <div style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 4px 0;">Trajectory Transition</div>
        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.4;">Recalculate neural retention index. Simulated hazard drops from ${(p.hazard * 100).toFixed(0)}% down to 18.2% (Safe Tier).</p>
      </div>
    `;
  }

  function renderKundaliRadarChart(q) {
    const ctx = document.getElementById("chart-kundali-radar");
    if (!ctx) return;

    if (chartInstances["kundaliRadar"]) {
      chartInstances["kundaliRadar"].destroy();
    }

    chartInstances["kundaliRadar"] = new Chart(ctx, {
      type: "radar",
      data: {
        labels: [
          "Cognitive Competency (बौद्धिक)",
          "Affective Wellness (भावनात्मक)",
          "Self-Regulation & Time (अनुशासन)",
          "Lifestyle & Digital Balance (जीवनशैली)"
        ],
        datasets: [
          {
            label: "Student Profile (कुंडली)",
            data: [q.cognitive, q.affective, q.selfReg, q.lifestyle],
            backgroundColor: "rgba(168, 85, 247, 0.25)",
            borderColor: "#c084fc",
            borderWidth: 2.5,
            pointBackgroundColor: "#a855f7",
            pointBorderColor: "#fff",
            pointRadius: 5
          },
          {
            label: "Cohort Normal Median (मानक)",
            data: [3.0, 3.0, 3.0, 3.0],
            backgroundColor: "rgba(99, 102, 241, 0.08)",
            borderColor: "rgba(99, 102, 241, 0.5)",
            borderWidth: 1.5,
            borderDash: [4, 4],
            pointRadius: 3
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          r: {
            min: 1.0,
            max: 5.0,
            ticks: { stepSize: 1.0, color: "#64748b", backdropColor: "transparent" },
            grid: { color: "rgba(255, 255, 255, 0.08)" },
            angleLines: { color: "rgba(255, 255, 255, 0.08)" },
            pointLabels: { color: "#cbd5e1", font: { size: 11, weight: "bold" } }
          }
        },
        plugins: {
          legend: { position: "top", labels: { boxWidth: 12, color: "#cbd5e1" } }
        }
      }
    });
  }

  // ==========================================================================
  // MODULE: INSTITUTIONAL ADMIN & ADVISOR COMMAND CENTER
  // ==========================================================================

  let currentAdminRosterData = [];

  function initAdminPortalTab() {
    renderAdminRoster();
    renderCounselorNotesTable();
  }

  function renderAdminRoster() {
    const tbody = document.getElementById("admin-roster-tbody");
    if (!tbody) return;
    tbody.innerHTML = "";

    // Combine static cohort sample + any live submitted tests
    const allRoster = [
      ...liveSubmittedStudents.map(ls => ({
        id: ls.id,
        name: ls.name,
        branch: ls.branch,
        sem: ls.semester,
        mean: ls.prediction.meanScore.toFixed(2),
        hazard: `${(ls.prediction.hazard * 100).toFixed(1)}%`,
        cgpa: `${ls.prediction.predictedCGPA.toFixed(2)} (${ls.prediction.successTier})`,
        career: ls.prediction.careerTier,
        risk: ls.prediction.riskTier,
        isLive: true,
        profileObj: ls
      })),
      ...students.slice(0, 40).map(s => ({
        id: s.id,
        name: s.id === "STU-0001" ? "Aarav Sharma" : (s.id === "STU-0002" ? "Priya Patel" : `Student ${s.id.split('-')[1]}`),
        branch: s.demographics?.major || "Computer Science",
        sem: s.demographics?.academicYear || "Freshman",
        mean: s.mean.toFixed(2),
        hazard: s.risk === "High" ? "84.5%" : (s.risk === "Medium" ? "52.3%" : "18.4%"),
        cgpa: s.success === "Excellent" ? "9.12 (Excellent)" : (s.success === "Good" ? "7.84 (Good)" : (s.success === "Average" ? "6.45 (Average)" : "4.92 (Probation)")),
        career: s.career,
        risk: s.risk,
        isLive: false,
        studentObj: s
      }))
    ];

    currentAdminRosterData = allRoster;

    allRoster.forEach(row => {
      const tr = document.createElement("tr");
      const riskClass = row.risk === "High" ? "badge-risk-high" : (row.risk === "Medium" ? "badge-risk-medium" : "badge-risk-low");

      tr.innerHTML = `
        <td>
          <div style="font-weight: 700; color: #fff;">${row.name}</div>
          <div style="font-size: 0.75rem; color: #94a3b8; font-family: var(--font-mono);">${row.id} ${row.isLive ? '<span class="badge badge-good" style="font-size:0.65rem; padding:1px 4px;">LIVE</span>' : ''}</div>
        </td>
        <td>
          <div style="font-size: 0.85rem; color: #cbd5e1;">${row.branch}</div>
          <div style="font-size: 0.75rem; color: #64748b;">${row.sem}</div>
        </td>
        <td><strong style="color: #38bdf8;">${row.mean}</strong> / 5.0</td>
        <td><strong style="color: ${row.risk === 'High' ? '#ef4444' : (row.risk === 'Medium' ? '#fbbf24' : '#34d399')}; font-family: var(--font-mono);">${row.hazard}</strong></td>
        <td>${row.cgpa}</td>
        <td>${row.career}</td>
        <td><span class="badge ${riskClass}">${row.risk}</span></td>
        <td>
          <div style="display: flex; gap: 6px;">
            <button class="btn btn-secondary btn-sm" onclick="viewStudentKundaliFromAdmin('${row.id}')" style="padding: 3px 8px; font-size: 0.75rem; color: #c084fc; border-color: #a855f7;">
              🔮 Kundali
            </button>
            <button class="btn btn-secondary btn-sm" onclick="openNewCounselorNoteModal('${row.name} (${row.id})')" style="padding: 3px 8px; font-size: 0.75rem;">
              📝 Note
            </button>
          </div>
        </td>
      `;
      tbody.appendChild(tr);
    });

    // Update total count
    const totalEl = document.getElementById("admin-total-count");
    if (totalEl) totalEl.innerText = (2525 + liveSubmittedStudents.length).toLocaleString();
  }

  window.handleAdminSearch = function(query) {
    const q = query.toLowerCase().trim();
    const rows = document.querySelectorAll("#admin-roster-tbody tr");
    rows.forEach(r => {
      const txt = r.innerText.toLowerCase();
      r.style.display = txt.includes(q) ? "" : "none";
    });
  };

  window.filterAdminRoster = function() {
    const dept = document.getElementById("admin-dept-filter").value;
    const risk = document.getElementById("admin-risk-filter").value;
    const rows = document.querySelectorAll("#admin-roster-tbody tr");

    rows.forEach(r => {
      const txt = r.innerText;
      let matchDept = dept === "ALL" || txt.includes(dept) || (dept.includes("CSE") && txt.includes("Computer"));
      let matchRisk = risk === "ALL" || txt.includes(`${risk} Risk`) || txt.includes(risk);
      r.style.display = (matchDept && matchRisk) ? "" : "none";
    });
  };

  window.viewStudentKundaliFromAdmin = function(studentId) {
    // Check if live submitted
    const liveMatch = liveSubmittedStudents.find(s => s.id === studentId);
    if (liveMatch) {
      renderStudentKundali(liveMatch);
      switchTab("student-kundali");
      return;
    }

    // Check in static cohort
    const staticMatch = students.find(s => s.id === studentId);
    if (staticMatch) {
      const generatedProfile = {
        id: staticMatch.id,
        name: staticMatch.id === "STU-0001" ? "Aarav Sharma" : (staticMatch.id === "STU-0002" ? "Priya Patel" : `Student ${staticMatch.id.split('-')[1]}`),
        rollNo: `2026UG${staticMatch.id.split('-')[1]}`,
        branch: staticMatch.demographics?.major || "Computer Science",
        semester: staticMatch.demographics?.academicYear || "Freshman",
        gender: staticMatch.demographics?.gender || "Male",
        timestamp: "Cohort Archive",
        answers: staticMatch.scores,
        prediction: runNeuralPrediction(staticMatch.scores)
      };
      renderStudentKundali(generatedProfile);
      switchTab("student-kundali");
    }
  };

  window.openNewCounselorNoteModal = function(targetStudent = "") {
    const modal = document.getElementById("counselor-modal");
    if (!modal) return;
    if (targetStudent) {
      document.getElementById("note-student-target").value = targetStudent;
    }
    modal.classList.add("active");
  };

  window.closeCounselorModal = function() {
    const modal = document.getElementById("counselor-modal");
    if (modal) modal.classList.remove("active");
  };

  window.saveCounselorNote = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    const student = document.getElementById("note-student-target").value;
    const advisor = document.getElementById("note-advisor-name").value;
    const type = document.getElementById("note-intervention-type").value;
    const notes = document.getElementById("note-action-text").value;
    const status = document.getElementById("note-status-select").value;

    const newNote = {
      date: new Date().toLocaleString([], { dateStyle: 'short', timeStyle: 'short' }),
      student,
      advisor,
      type,
      notes,
      status
    };

    counselorNotesLog.unshift(newNote);
    renderCounselorNotesTable();
    closeCounselorModal();

    alert(`Counseling session note recorded successfully for ${student}!`);
  };

  function renderCounselorNotesTable() {
    const tbody = document.getElementById("admin-counselor-notes-tbody");
    if (!tbody) return;
    tbody.innerHTML = "";

    counselorNotesLog.forEach(n => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td style="font-size: 0.8rem; color: #94a3b8; font-family: var(--font-mono);">${n.date}</td>
        <td><strong style="color: #fff;">${n.student}</strong></td>
        <td style="color: #cbd5e1;">${n.advisor}</td>
        <td><span class="badge" style="background: rgba(99, 102, 241, 0.2); color: #a5b4fc;">${n.type}</span></td>
        <td style="font-size: 0.82rem; color: #cbd5e1; max-width: 260px;">${n.notes}</td>
        <td><span class="badge badge-good">${n.status}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }

  window.exportAdminRosterCSV = function() {
    let csv = "Student_ID,Name,Branch,Semester,Mean_17D,Dropout_Hazard,Predicted_CGPA,Career_Readiness,Risk_Tier\n";
    currentAdminRosterData.forEach(r => {
      csv += `${r.id},"${r.name}","${r.branch}","${r.sem}",${r.mean},${r.hazard},"${r.cgpa}","${r.career}",${r.risk}\n`;
    });

    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "AcuLearn_Master_Student_Triage_Roster.csv";
    link.click();
  };

  // Launch All Modules
  function initApp() {
    initTabs();
    initStudentPortalTab();
    initAdminPortalTab();
    initOverviewTab();
    initDemographicsTab();
    initDiagnosticsTab();
    initCounselingTab();
    initDomainsTab();
    initQuestionsTab();
    initCorrelationsTab();
    initStudentsTab();
    initSimulatorTab();
    initHeaderActions();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initApp);
  } else {
    initApp();
  }

})();

