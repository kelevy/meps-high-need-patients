# Who gets missed? Predicting high-need patients in MEPS, and whether spending is the right target

A reproducible analysis of the US Medical Expenditure Panel Survey (MEPS, AHRQ). Care-management
programs enrol a limited number of patients and often pick them by predicted *cost*. This project asks
who that approach misses, and whether a different target does better.

## Why it matters

Health systems use risk scores to decide who receives extra care coordination. A well-known 2019
study of a commercial algorithm found that using healthcare cost as a stand-in for health need
under-identified Black patients who were as sick as others (Obermeyer et al., Science 2019). This
project checks whether the same pattern can be examined, and improved on, with fully open national
survey data.

## Questions

1. **Prediction.** How well can next-year high need be predicted from this year's information?
2. **Target choice (core question).** At the same enrolment budget, who is captured when patients are
   ranked by predicted *spending* compared with predicted *health need* (for example hospital stays,
   emergency visits, chronic-condition burden)? Are the differences larger for some groups?
3. **Association (secondary).** Is having a usual source of care associated with fewer later
   emergency visits after adjustment? This is observational, and confounding is discussed in the plan.
4. **Programme design (secondary).** What enrolment budget makes sense under stated cost assumptions,
   and how large would a trial of the programme need to be? Simulated, and labelled as simulated.

## Data

MEPS Household Component public use files from AHRQ: person-level full-year files, event files
(office visits, ER, inpatient, outpatient, prescriptions, dental, home health, other supplies), a
conditions file, and two-year longitudinal files, linked by the person identifier. The data use terms
restrict use to statistical analysis and prohibit re-identification, so raw files are not committed.
