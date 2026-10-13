# Who gets missed? Predicting high-need patients in MEPS, and whether spending is the right target

A reproducible analysis of the US Medical Expenditure Panel Survey (MEPS, AHRQ). Care-management
programs enrol a limited number of patients and often pick them by predicted *cost*. This project asks
which patients will need acute care next year, and whether ranking by predicted cost or by predicted
clinical need finds them better.

## Why it matters

Clinics and health plans have limited care-management capacity (nurse outreach, care coordination,
medication review) and must decide whom to contact. Many rank patients by predicted cost, but cost is
only a proxy for clinical need. This project asks which patients will need acute care next year, and
whether ranking by predicted cost or by predicted need identifies them better, using fully open national
survey data.

## Questions

1. **Prediction.** How well can next-year high need be predicted from this year's information?
2. **Target choice (core question).** At the same enrolment budget, which patients who go on to need
   acute care (a hospital stay or repeated ER visits) are captured when patients are ranked by
   predicted *spending* compared with predicted *health need*? Does the answer hold across age bands
   and insurance types?
3. **Association (secondary).** Is having a usual source of care associated with fewer later
   emergency visits after adjustment? This is observational, and confounding is discussed in the plan.
4. **Programme design (secondary).** What enrolment budget makes sense under stated cost assumptions,
   and how large would a trial of the programme need to be? Simulated, and labelled as simulated.

## Data

MEPS Household Component public use files from AHRQ: person-level full-year files, event files
(office visits, ER, inpatient, outpatient, prescriptions, dental, home health, other supplies), a
conditions file, and two-year longitudinal files, linked by the person identifier. The data use terms
restrict use to statistical analysis and prohibit re-identification, so raw files are not committed.
Health content includes chronic conditions, visits, ER use, hospital stays, prescribed medicines, and
self-rated health. Spending is one variable among these and defines one of the two targets.
