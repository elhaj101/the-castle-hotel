
## **Incomplete Learning Objectives:**

### **LO1: Agile Methodology & UX Design**
❌ **1.3** - Provide evidence of refining **Epics to User Stories to Tasks** (Merit)
   - User stories exist, but no documented epics or task breakdowns
   
❌ **1.4** - Clear **user acceptance criteria** defined (Merit)
   - User stories have acceptance criteria in user_stories.md, but not all are detailed/testable
   
❌ **1.13** - Document **UX design work** (wireframes, mockups, diagrams) and demonstrate they were followed
   - README mentions wireframes but screenshots show incomplete/missing wireframe images

---

### **LO4: Testing**
❌ **4.1** - Document **all implemented testing** in README (Pass)
   - README mentions testing but doesn't document comprehensive test results
   
❌ **4.1** - **Fully document results** of automated testing with evaluation of bugs (Merit)
   - No documented test results, bug tracking, or fixes in README
   
❌ **4.1** - **Comprehensive testing** with good coverage (Distinction)
   - tests.py is empty (per report 1)
   - No evidence of comprehensive Python test suite

❌ **4.2** - Design and implement **JavaScript test procedures** (Pass)
   - Manual JS/UI tests mentioned in sprint plan but not documented or automated

---

### **LO5: Version Control**
❌ **5.2** - Commit **often** with small, well-defined commits and clear messages (Merit)
   - Need to verify Git history has descriptive, granular commits

---

### **LO6: Deployment**
❌ **6.2** - Ensure **no commented-out code** and **no broken internal links** (Pass)
   - Need to verify this systematically
   
❌ **6.1** - **Fully document deployment** with consistent markdown formatting (Merit)
   - Deployment section exists but may need polish for "well-structured, easy to follow"

---

### **LO7: Object-Based Software**
⚠️ **7.1** - Implement **efficient model code** (Merit)
   - Report 1 identifies critical flaw: room availability logic is broken
   - `Reservation.children` is CharField instead of IntegerField
   - No date-overlap validation in the model

---

### **Distinction Criteria (Multiple)**
❌ **Clean Code Standards:**
   - No evidence of HTML/CSS/JS validation documented (W3C, Jigsaw, JSLint)
   - Need to verify all files pass validators

❌ **Comprehensive Testing:**
   - Testing not comprehensive (comments tests missing)
   - No documented test coverage or bug reports

❌ **Security Best Practices:**
   - Report 1 notes `SECRET_KEY` and `DEBUG` were hardcoded (may be fixed now but needs verification)

❌ **Professional-Grade UI:**
   - Need to verify accessibility compliance (WCAG)
   - Need to verify all UX principles documented

---

## **Critical Issues from Report 1:**

1. **Room Availability Bug** - Rooms become permanently unavailable after one booking (breaks core business logic)
2. **Missing Comments Tests** - No automated tests for comment CRUD
3. **Data Type Issues** - `children` field should be IntegerField
4. **No Date Overlap Validation** - Multiple users can book same room for overlapping dates

