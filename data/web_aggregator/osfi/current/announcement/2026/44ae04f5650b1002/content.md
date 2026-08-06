# H4 – Frequently Asked Questions

Information

Type of document

FAQs

Industry

Deposit-taking institutions

Return

Collateral and Pledging Report (H4)

Last updated

May 2023

Return number

H4

Accompanying documents

* [Collateral and Pledging Report (H4)](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/collateral-pledging-report-h4)

## Reporting and methodology

1. What is the appropriate classification for OTC derivatives with Foreign Governments and Central Banks – Part B Section 2?

**Answer**: To maintain consistency with H4 reporting standards and rule validations, please allocate OTC derivative transactions with foreign central bank and governments in Other Counterparties – Part B Section 6 - Foreign Counterparties (b155).

2. What is the appropriate classification for OTC derivatives with Canadian Government & Agencies – Part B Section 1?

**Answer**: To maintain consistency with H4 reporting standards and rule validations, please allocate OTC derivative transactions with the Canadian government and/or agencies in Other Counterparties – Part B Section 6 – Other Domestic Counterparties (b147).

3. What is the appropriate reporting practice for National Housing Act – Mortgage Backed Securities (NHA-MBS) & Canadian Mortgage Bond (CMB)?

**Answer**:

* For Balance Sheet portion
  + Own-originated NHA-MBS are to be reported in the Loans section (a11-a14)
  + NHA-MBS purchased in the secondary market are to be reported in Securities (Long) (a5) row
* For the Balance Sheet portion, NHA-MBS that are pledged to the CMB program are reported in the ‘Loans – Financed by Securitised Financing’ (a13)
* For the Collateral Movements section, collateral pledged to the CMB program are reported in ‘Other Secured Financing Securities Collateral’ (a70) or ‘Other Collateral OUT’ (a71)

4. What is the appropriate allocation for CLS related transactions?

**Answer**: CLS transactions are settled through the LVTS which is under the supervision of Bank of Canada. Pledging activity with the CLS for Canadian Federally regulated banks flow through the Bank of Canada, and thus should be reported under Canadian Government and Agencies - Part B Section 1: Bank of Canada: LVTS (b1). Foreign subsidiaries of Canadian banks pledging for CLS activities must allocate the respective amount to the appropriate counterparty of their jurisdiction.

5. Why does RRS display a different reporting deadline than the instructions?

**Answer**: RRS’s system limitations prevent the alignment of actual submission date relative to RRS prompt end dates. All business days of a reference month are due 35 calendar days after the last business day of the reference month.

EX: July 1st to 31st, 2017 H4 submissions were due on September 05, 2017 (35 days after the last business day of the month). Since September 04, 2017 was an Ontario holiday, the due date became September 05, 2017. If the due date falls on a Ontario holiday, the due date is pushed one day forward.

## RRS submissions

1. XML-File Type: May data-point addresses (DPA) be removed from the XML file if the value is zero or blank?

**Answer**: DPAs may be removed if they are zero or blank. Please ensure to remove all related XML tags to the reference DPA. A screenshot is provided below for convenience. The code that has been highlighted below in black may be removed when deleting DPAs.

![Screenshot showing xml code that may be removed when deleting the data-point addresses](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2023-05/en/H4_FAQ_img1.png)

2. XML-File Type: May Section-B be removed if it is inapplicable?

**Answer**: Section B may be removed if it is inapplicable to the filing institution. Please ensure to remove all related XML tags to Section B. Refer to screenshots below. All code in between <B type =“group”> and </B> may be removed if section B is inapplicable.

![Screenshot showing xml code that maybe be removed if section B is inapplicable](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2023-05/en/H4_FAQ_img2.png)

3. XML-File Type: May amendments be applied to the structure of the DPA groups from the XML template?

**Answer**: The XML template does not follow a specific logic, however; it is mandatory for DPAs within a group to be organized as presented in the template. The rationale is due to the fact that the DPAs have been registered to the groups as per the template.

4. What is the reporting frequency?

**Answer**: For the Unstructured Test Phase, the expectation is for 1 XML file or 1 Excel Worksheet per Workbook should be submitted per RRS Return End Date. When the return is Structured only 1 XML file may be submitted for the corresponding RRS Return End Date.

5. What is the significance of RRS Return End Date for the H4?

**Answer**: The data reported on the submission is to correspond with the RRS Return End Date data. For example, August 1, 2017 submission data should align with an RRS Return End Date of August 1, 2017. The sole exception is for the Unstructured Test Phase, where financial institutions are permitted to submit any 3 days + the month end date.

6. Is it possible to submit test XML submission files?

**Answer**: Testing for structural validation and validation rules for an XML submission, a financial institution may submit an e-mail request. Supplemental information for the reporting period (the date for which the submission corresponds to) is mandatory to test the XML test file.

7. How to troubleshoot validation rules for the Structured H4 Return?

**Answer**: The most effective method is to cross-reference the Rule ID from the RRS Portal with the Rule Validation Spreadsheet provided by the Bank of Canada.

Report a problem or mistake on this page

Date modified:
:   2023-11-17