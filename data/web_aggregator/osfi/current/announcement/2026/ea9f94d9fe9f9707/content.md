# Phase 3 988 non-retail transactional level data call

Information

Type of document

Instructions

Industry

Deposit-taking institutions

Last updated

March 21, 2025

Related documents

* [Clarifications about the non-retail data call](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/clarifications-about-non-retail-data-call)

## Return file

[OSFI 988 - Non-Retail Phase 3 - Submission Template (XLSX, 224.98 KB)](/sites/default/files/documents/OSFI988-BSIF988-nrp-pae-tpl-en.xlsx "OSFI988-BSIF988-nrp-pae-tpl-en.xlsx")

## General instructions

Phase 3 of the 988 non-retail data call is expanded to include wholesale lending (including corporate, sovereign, bank and commercial assets).

The first submission is required by February 25th, 2025. This submission should reflect reporting as of January 31, 2025.

The 988 non-retail data call is to be submitted to OSFI on or before the 25th of each month. If submission date falls on a holiday or weekend, the submission is due the next available business day.

Submissions should adhere to the standardized format as prescribed in the document “OSFI 988 - Non-Retail Phase 3 – Submission Template”.

### Updated data scope

#### Geography

All geographies (US, Canada, and International)

#### Asset classes

* Commercial Real Estate (CRE)
* Corporate, Sovereign, Bank, and Commercial

### Data call format

The data provided should:

* be contained in a plain-text Pipe Delimiter Separated file format
* include all data elements provided in the Non-Retail Phase 3 - Submission Template, in the order they appear within the template
* be null[Footnote 1](#fn1) where a data element is not available or not applicable, unless otherwise specified
* be the current value of that data element, unless otherwise specified

The data provided should **not**:

* contain the pipe character in any field value
* contain carriage returns in any field value
* be encrypted

### File specifications

|  |  |
| --- | --- |
| Format | Delimiter Separated File |
| Header | Variable names as described in the data template column Submission Key must appear on row 1 of each submission file in the order listed.Variable names must match exactly as shown in the template. |
| Separator Character / Delimiter | ASCII #124: | |
| Filename | {Reporting Date}\_NR\_{File number}\_{FRFI Code}\_{Submission Date}.txt |
| Reporting Date | Last day for Reporting month (Format yyyymmdd) |
| Data call Name | NR (fixed string) |
| File number | code options:   * 01 – Borrower file * 02 – Facility file * 03 – Collateral file * 04 – Project file |
| FRFI Code | OSFI-issued FRFI Code |
| Submission Date | Submission date (Format yyyymmdd) |
| Example for February submission | * 20250131\_NR\_01\_AZ\_20250225.txt * 20250131\_NR\_02\_AZ\_20250225.txt * 20250131\_NR\_03\_AZ\_20250225.txt * 20250131\_NR\_04\_AZ\_20250225.txt |

### Data transmission

The data call is to be submitted in the Regulatory Reporting System (RRS) using the return code **OSFI 988**.

The filing instructions may be obtained on the OSFI website at following location: [Regulatory Reporting System (RRS) - Manage Financial Returns User Guide (PDF)](/sites/default/files/documents/rrs_mcr_EN.pdf "rrs_mcr_EN.pdf").

The return will accommodate 4 file uploads. The submission files should be attached to the available upload slots in following order from first to last:

* 01 – Borrower
* 02 – Facility
* 03 – Collateral
* 04 – Project

All files must be submitted to provide a complete submission. If there is no relevant information to report in an individual file, please still include that file in the submission with the corresponding column headers and formatting but with no data rows included.

### File details description

The data call is divided into four (4) distinct files which are described in Non-Retail Phase 3 – Submission Template and are to be transmitted as part of the data call submission each month.

01 – Borrower
:   Report all in-scope borrowers for Phase 3 as of the end of each reporting period.

02 – Facility
:   Report all in-scope facilities associated to a borrower included in 01–Borrower.

    * Each Facility Borrower Number (#202) must match to a unique Borrower Number (#101) value in 01 – Borrower.
    * Each Non-Blank Facility Project ID (#203) must match to a unique Project ID (#401) value in 04 – Project.

03 – Collateral
:   Report all collateral associated to each facility in 02 – Facility. Each distinct collateral must be reported on a separate row (i.e. do not report multiple collateral on a single record). Identify the single primary collateral for each facility with the Primary Collateral Indicator (#316).

    * Each Collateral Facility Number (#302) must match to a unique Facility Number (#201) value in 02 – Facility.

04 – Project
:   Report the details of the Real Estate Development or Construction project associated to each facility in 02 – Facility, if applicable (CRE only.)

### Data quality

Financial Institutions (FIs) are responsible for ensuring that the data submitted aligns with prescribed definitions and formats. While there are differences in definitions on various regulatory returns, each FI should ensure that aggregate totals in the data call reasonably align to portfolio totals reported in other regulatory returns.

### Data quality exception reports

FI submissions are processed by an automated system to validate compliance with the template specifications and identify potential anomalies. If an issue is identified with a submission, we will send a data quality report to the FI detailing the issue and request an action plan or explanation.

Depending on the severity of certain issues, we may require correction through resubmissions. If a resubmission is requested, regardless of the filing period, the resubmission must adhere to the latest version of the data template and include all files.

In all cases, we require that a response to the data quality report be returned to the support email ([nonretail.support-soutien.pretsauxentreprises@osfi-bsif.gc.ca](mailto:nonretail.support-soutien.pretsauxentreprises@osfi-bsif.gc.ca)) in order that any feedback can be processed by the Data Quality system.

Please direct any questions regarding this data call to: [nonretail.support-soutien.pretsauxentreprises@osfi-bsif.gc.ca](mailto:nonretail.support-soutien.pretsauxentreprises@osfi-bsif.gc.ca).

## Footnotes

Footnote 1
:   A null value contains no characters or symbols. Please do not include values such as “NULL”, “N/A” or a space etc...

    [Return to footnote 1  referrer](#fn1-rf)

Report a problem or mistake on this page

Date modified:
:   2025-03-21