---

### `statement.md`

```markdown
# Problem Statement & System Design Specification

## 1. Problem Statement

University engineering students encounter recurring friction when balancing day-to-day academic tracking and routine computational tasks:
1. **Academic Non-Compliance Risks:** Course guidelines enforce a strict 75% attendance threshold. Manually estimating attendance margins or running mental checks after absent days frequently leads to debarment risks due to calculation errors.
2. **Complex Relative Grading Schemes:** Semester evaluations are rarely raw percentages; they rely on fractional component weightages (15% per CAT, 30% internals, 40% FAT) measured against dynamic class averages. Calculating projected course grades and weighted SGPA manually is cumbersome and prone to mistakes.
3. **Fragmented CLI Utilities:** Students frequently need quick base conversions, arithmetic calculators, and local environment diagnostics while coding or debugging in terminal environments, requiring them to switch away from their workflow to browsers or separate GUI apps.

The objective of this project is to develop **AcademiX Toolkit**, a unified, lightweight, modular Command-Line Interface (CLI) application in Python that centralizes student compliance management, mathematical transformations, and system diagnostics inside a single executable shell session.

---

## 2. Functional Requirements

### Module 1: Central Shell (`main.py`)
* Shall provide a clean terminal dashboard with structured options and navigational error trapping.
* Shall gracefully invoke child modules and maintain the active execution loop until explicit exit instructions are given.

### Module 2: Computational Utilities (`sci_cal_f1.py`)
* **Mathematical Operations:** Handle basic arithmetic, logarithmic bounds checking, trigonometric radian evaluations, power computations, and compound interest calculations.
* **Base Transformations:** Must convert between Decimal, Binary, Octal, and Hexadecimal representations using fundamental arithmetic operators (`%`, `//`) rather than high-level format specifiers.
* **Utility Generation:** Must generate variable-length secure alphanumeric strings and numeric PINs using pure set operations without relying on `random`.

### Module 3: Academic Administration (`student_management_f2.py`)
* **Attendance Tracking:**
  - Maintain class-by-class attendance records across enrolled courses.
  - Dynamically compute attendance percentages against a 75% cutoff threshold and provide actionable status remarks.
  - Allow sequential logging of present (`P`) or absent (`A`) lectures.
* **Grade Evaluation & SGPA Calculation:**
  - Scale heterogeneous exam assessments: CAT 1 (15%), CAT 2 (15%), Internals (30%), and FAT (40%).
  - Map final scaled aggregate scores to letter grades (`S`, `A`, `B`, `C`, `D`, `F`) based on offsets from the user-input class average.
  - Compute weighted SGPA based on assigned course credit allocations:
    $$\text{SGPA} = \frac{\sum (\text{Credits}_i \times \text{GradePoints}_i)}{\sum \text{Credits}_i}$$

### Module 4: System Telemetry (`system_dig_f3.py`)
* Access system parameters to provide platform type, OS version, architecture, CPU details, and Python environment data.
* Compute storage consumption in gigabytes with proper path inspection and fallback handling.

---

## 3. Engineering & Edge-Case Safeguards

| Feature / Module | Potential Point of Failure | Handled Solution |
| :--- | :--- | :--- |
| **Arithmetic / Division** | Zero denominator entered (`b = 0`) | Guarded branch intercepts input and flags `INFINITY` instead of throwing `ZeroDivisionError`[cite: 2]. |
| **Logarithms** | Arguments $x \le 0$ or Base $\le 0$, Base $= 1$ | Value validation intercepts input and outputs explicit domain error guidance[cite: 2]. |
| **Trigonometry** | Tan values at undefined asymptotes ($90^\circ, 270^\circ$) | Modular check `deg % 180 == 90` flags output as `UNDEFINED` before `math.tan()` execution[cite: 2]. |
| **Base Conversion** | Invalid character inputs in binary strings | String character set filtering (`all(ch in "01")`) ensures algorithm does not corrupt on malformed data. |
| **Attendance Module** | Zero total classes entered | Guarded ternary check prevents division-by-zero when evaluating subject percentage[cite: 3]. |

---

## 4. Conclusion & Planned Roadmap

AcademiX Toolkit provides a robust terminal application engineered to streamline routine academic and developer tasks. Planned future extensions include:
1. **Local State Persistence:** Moving attendance and grade parameters from volatile in-memory variables to a localized JSON datastore to persist state between runs.
2. **Attendance Deficit / Bunk Calculator:** An analytical projection algorithm calculating the exact number of classes required to reach 75% or the safe threshold of classes that can be missed.
3. **Hardware Monitoring Expansion:** Integrating real-time CPU thermal loads, memory usage, and ping latency checks using system sockets.