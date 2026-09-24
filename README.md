# AcademiX Toolkit: Multi-Purpose Student & Engineering CLI Suite

An all-in-one console application written in Python to consolidate daily academic tracking, mathematical/engineering conversions, and hardware diagnostics into a clean, zero-dependency terminal interface.

---

## The Motivation

As engineering students, our day-to-day workflow is often fragmented:
- Checking attendance thresholds against university limits across disparate spreadsheets.
- Calculating semester grades and SGPA while accounting for relative grading curves and exam weightages (CATs vs. FAT).
- Performing engineering base conversions, scientific calculations, and checking system runtime metrics.

**AcademiX Toolkit** brings all of these utilities into a single modular CLI suite with zero external third-party dependencies—everything runs out of the box using Python's standard libraries and raw algorithmic logic.

---

## Project Structure

```text
VITYARTHIPROJECT/
│
├── main.py                  # Primary application driver & terminal interface
├── sci_cal_f1.py            # Scientific calculator, base conversions & utility tools
├── student_management_f2.py # Attendance manager & relative grading (CAT/FAT/SGPA)
└── system_dig_f3.py         # Hardware & environment diagnostic suite