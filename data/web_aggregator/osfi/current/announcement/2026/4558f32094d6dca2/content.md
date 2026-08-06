# Net cumulative cash flow reporting manual

Information

Type of document

Instructions

Industry

Deposit-taking institutions

Return

Net cumulative cash flow reporting manual (NCCF)

Last updated

February 2026

Effective

January 2025

Table of contents

Related documents

* [Release of final 2023 liquidity returns and consultation on draft NCCF reporting instructions - Letter](/en/guidance/guidance-library/release-final-2023-liquidity-returns-consultation-draft-nccf-reporting-instructions)
* [Liquidity Adequacy Requirements - Guideline (2025)](/en/guidance/guidance-library/liquidity-adequacy-requirements-lar-guideline-2025)

## Return files

[Change control log](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/net-cumulative-cash-flow-change-control-log "Net cumulative cash flow – Change control log")

### Comprehensive NCCF return (DT2)

[DT2 - Comprehensive NCCF sample return (XLSX, 4.78 MB)](/sites/default/files/documents/nccf-dt2-return-releve-04-14-2026-en.xlsx "nccf-dt2-return-releve-04-14-2026-en.xlsx") [DT2 - Technical specification (XLSX, 1.42 MB)](/sites/default/files/documents/nccf-dt2-tech-spec-04-14-2026-en%20.xlsx "nccf-dt2-tech-spec-04-14-2026-en .xlsx") [DT2 - XML file (sample) (XML, 33.38 KB)](/sites/default/files/documents/nccf-dt2-xml-2026-03.xml "nccf-dt2-xml-2026-03.xml") [DT2 - XSD file (XSD, 452.47 KB)](/sites/default/files/documents/nccf-dt2-xsd-2026-03.xsd "nccf-dt2-xsd-2026-03.xsd")

### Comprehensive NCCF return (OSFI948)

[OSFI948 - Comprehensive NCCF sample return (XLSX, 4.79 MB)](/sites/default/files/documents/nccf-osfi948-return-releve-04-14-2026-en.xlsx "nccf-osfi948-return-releve-04-14-2026-en.xlsx")

### Streamlined NCCF return (DT5)

[DT5 - Streamlined NCCF sample return (XLSX, 816.27 KB)](/sites/default/files/documents/nccf-dt5-return-releve-04-14-2026-en.xlsx "nccf-dt5-return-releve-04-14-2026-en.xlsx") [DT5 - Technical specification (XLSX, 1.48 MB)](/sites/default/files/documents/nccf-dt5-tech-spec-2026-03-en.xlsx "nccf-dt5-tech-spec-2026-03-en.xlsx") [DT5 - XML file (sample) (XML, 113.22 KB)](/sites/default/files/documents/nccf-dt5-xml-2026-03.xml "nccf-dt5-xml-2026-03.xml") [DT5 - XSD file (XSD, 165.44 KB)](/sites/default/files/documents/nccf-dt5-xsd-2026-03.xsd "nccf-dt5-xsd-2026-03.xsd")

### Streamlined NCCF return (OSFI949)

[OSFI949 - Streamlined NCCF sample return (XLSX, 794.81 KB)](/sites/default/files/documents/nccf-osfi949-return-releve-04-14-2026-en.xlsx "nccf-osfi949-return-releve-04-14-2026-en.xlsx")

## Net cumulative cash flow (NCCF) return

### Purpose

This return provides the net cumulative cash flow of the reporting institution, as well as details of the calculation. This document covers the instructions for the Comprehensive NCCF and the Streamlined NCCF.

### Statutory

Section 628 and Section 950 of the Bank Act (banks and bank holding companies, respectively), Section 495 of the Trust and Loan Companies Act.

### Application

This return applies to select banks (including federal credit unions), bank holding companies and federally regulated trust and loan companies (collectively referred to as institutions).

In particular,

* the Comprehensive NCCF (DT2) applies to institutions that have been designated by OSFI as domestic systemically important banks (DSIBs) and Category I Small and Mid-sized Deposit-Taking Institutions (SMSBs); and
* the Streamlined NCCF (DT5) applies to Category II SMSBs.

Please refer to OSFI's SMBS Capital and Liquidity Requirements Guideline for the applicable category segmentation criteria.

### Frequency

Monthly unless increased frequency is requested by OSFI, as per the Liquidity Adequacy Requirements (LAR) Guideline.

### Reporting dates

The return must be completed on a monthly basis unless increased frequency is requested by OSFI. The time lag in reporting should not surpass 14 calendar days, which may be reduced to 3 business days in stress situations at OSFI's discretion.

### Where to submit

OSFI

## General instructions

The NCCF return is to be completed using the methodologies and calculations described in Chapter 4 of OSFI's Liquidity Adequacy Requirements (LAR) Guideline. Specific instructions for each required data item can be found below as well as in the 'Appx 2 Instructions' worksheet of the NCCF return. The purpose of these instructions is to ease completion of the NCCF return by referencing its components to the applicable paragraph(s) (para) of the LAR Guideline.

Generally, the NCCF return must be completed on a consolidated basis (reported in CAD-equivalent amounts).

For the "Comprehensive NCCF", the NCCF is to be reported on a Canadian currency basis and on an individual major foreign currency basis, which is defined as US dollar (USD), Euro (EUR), and British pound sterling (GBP), as well as any other currency determined to be necessary by OSFI. For the "Streamlined NCCF", the NCCF is only to be reported on a consolidated basis with all currencies aggregated and reported in Canadian dollars.

Reporting of a subsidiary's NCCF is required if the sum of all subsidiary balance sheets is 5% of consolidated notional assets, or as required by OSFI (LAR Chapter 4 para. 12). OSFI will notify an institution bilaterally should this requirement apply.

For institutions completing the Streamlined NCCF, completed unstructured NCCF returns should be submitted in Excel format via the Regulatory Reporting System (RRS).

The Comprehensive (DT2) and Streamlined (DT5) NCCF returns can be submitted through the Regulatory Reporting System (RRS) by uploading a data file in XML. An XSD file that outlines the structure of conforming XML files will be available for download from the RRS Portal Documents section.

These instructions should be read in conjunction with the [LAR Guideline](/en/guidance/guidance-library/liquidity-adequacy-requirements-lar-guideline-2025 "Liquidity Adequacy Requirements (LAR) - Guideline (2025)").

## 1. Introduction

### 1.0 Introduction

These instructions have been drafted as a supplement to Chapter 4 of OSFI's Liquidity Adequacy Requirements (LAR) Guideline. The LAR Guideline sets out definitions, haircuts, run-off rates and reporting requirements which are referenced in these instructions.

LAR Guideline references are made to the final version dated January 2022.

The NCCF template sets out to incorporate a financial institution's cash flows for assets, liabilities, and collateral movements. Should an FI's business model not include certain aspects captured by the NCCF, the FI should simply leave blank lines where items are not applicable.

#### Streamlined NCCF

Generally, the Streamlined NCCF is a simplified version of the Comprehensive NCCF, where more granularity is usually required for specific assets, liabilities and off-balance sheet items. Most of the instructions apply to both returns, however, where instructions for the Streamlined NCCF differ, those will be clearly indicated in these instructions.

### 1.1 Reporting format

The template format requires:

* Cash inflows (including Eligible Unencumbered Liquid Assets, or EULA, as defined in LAR Chapter 4) – Allocation of all eligible cash inflows from assets and collateral to the appropriate maturity buckets. Cash and security flow eligibility and treatments are discussed in Section 2 for cash inflows. Reporting of securities includes on-balance sheet securities and off-balance sheet collateral pledged/received.

  Relevant paragraphs in LAR Chapter 4 are 15-37.
* Cash outflows – Allocation of all eligible cash outflows from liabilities and collateral to the appropriate maturity buckets. Cash and security flow eligibility and treatments are discussed in Section 3 for cash outflows. Reporting of securities include on-balance sheet securities and off-balance sheet collateral pledged or received.

  Relevant paragraphs in LAR Chapter 4 are 38-75.

Maturity buckets used in the template include:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 1 | Week 2 | Week 3 | Week 4[Template note \*](#tmpfn1) | Month 2[Template note \*\*](#tmpfn2) | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >12 Months |

Template notes

Template note \*
:   Cash flows related to days 29, 30 and 31 of the first month should be reported in the week 4 bucket. For deposits, apply the equivalent monthly run-off rate assigned to week 4 cash flows (refer to LAR Chapter 4 para. 39 and Table 1).

    [Return to template note \* referrer](#tmpfn1-rf)

Template note \*\*
:   Cash flows related to the remaining days of week 5 should be reported in the month 2 bucket. For deposits, apply the monthly run-off rate assigned to Month 2 flows (refer to LAR Chapter 4 Table 1).

    [Return to template note \*\* referrer](#tmpfn2-rf)

### 1.2 General instructions

* The NCCF measures an institution's surplus or deficit at a given time period, calculated as the difference between the sum of eligible cash inflows and the sum of prescribed cash outflows from the reporting date up to the time period considered. Accordingly, an institution's survival horizon corresponds to the last period before which the NCCF turns negative and is expressed in weeks or in months.
* Cash flows associated with assets, liabilities, and collateral movements that have a contractual maturity should be considered based on their residual contractual maturity or earliest option date (refer to LAR Chapter 4 para. 25, 27, and 40) unless instructed otherwise.
* Outflows associated with liabilities that have no specific maturity, such as demand deposits, will be calculated in accordance with the LAR Guideline and allocated to the maturity buckets noted in section 1.1 above.
* Instructions related to collateral are embedded within the corresponding inflow and outflow sections.
* Reporting of balances is also required. Reconciliation to balance sheet balances should be done on a best-efforts basis. However, discrepancies with the balance sheet balances should be within reason and explainable.
* For loans with an amortization schedule, institutions may choose to recognize either blended mortgage amortization and interest payment inflows, or suppress reporting of interest payment and report mortgage amortization payment inflows only. If the institution chooses to recognize blended mortgage amortization and interest payment as inflows, it must do so for all loan types, and blended deposit balances and interest payment outflows must be reported for deposits. Otherwise, the institution can choose to report balances only for the outflows from deposits.
* The NCCF surplus and survival horizon will be calculated according to the calculations embedded in the Excel NCCF template available on OSFI's website.
* If reporting requirements cannot be met due to system limitations, reporting FIs are to discuss with OSFI bilaterally to determine remediating action plans and alternative interim reporting solutions.

### 1.3 Filing

The NCCF should be reported to OSFI monthly, with the operational capacity to increase the frequency to weekly or even daily (for DSIBs) in stressed situations at OSFI's discretion. The time lag for reporting should not surpass 14 calendar days and may be requested within 3 business days in stress situations.

Institutions should notify OSFI immediately if their NCCF has fallen, or is expected to fall, below the institution specific target communicated by OSFI to institutions.

### 1.4 Major foreign currency balance sheets

For the Comprehensive NCCF, the NCCF is to be reported in Canadian dollar (CAD) equivalent for each major foreign currency, defined as US dollar (USD), Euro (EUR), and British pound sterling (GBP), as well as other currencies determined to be eligible by OSFI, collectively referred as "Major Foreign Currencies". The CAD exchange rate in effect as of the reporting date should be used for conversion.

For Major Foreign Currency Balance Sheets and Combined Balance Sheet, cash flow information should be summarized from individual foreign currency and Canadian balance sheets.

#### Streamlined NCCF

For the Streamlined NCCF, the NCCF is only to be reported on a consolidated basis with all currencies aggregated and reported in Canadian dollars. Institutions completing the Streamlined NCCF return are only required to report on collateral inflows and outflows if they also file the regulatory return Collateral and Pledging (H4) or if they are otherwise directed to do so by OSFI.

### 1.5 Securities haircut table

To report the large number of security types in a consistent and comparable manner across currencies and jurisdictions, security types (including those qualified as Eligible Unencumbered Liquid Assets (EULA) as defined in Chapter 4 of the LAR Guideline) have been harmonized into broader security types based on their nature and credit rating.

Securities qualified as EULA under each currency have been assigned haircuts, which approximate haircuts prescribed by the corresponding central banks for each security type. Security types that are not qualified as EULA in a jurisdiction receive no liquidity value and are assigned 100% haircut in week 1; full liquidity value will be attributed upon maturity of the security.

Securities cash flows are determined based on market value of securities after application of the appropriate haircut as prescribed in the Securities Haircut Table. The Securities Haircut Table can be found in the Excel NCCF template available on OSFI's website, in the worksheet "Appx 1.Ref Rates".

The central bank eligible securities and haircuts have been streamlined into the Securities Haircut Table in the following aspects:

* Credit rating steps – Instead of adopting different credit rating bucketing schemes prescribed by individual central banks, security types are based on the following credit rating step methodology:

  Credit rating steps

  | Credit rating bucket | Credit rating |
  | --- | --- |
  | High rated | AA−/Aa3 to AAA/Aaa |
  | Medium rated | A−/A3 to A+/Aa1 |
  | Low/not rated | D to BBB+/Baa1, or not rated |
* This is based on BCBS' standardized approach to credit risk (Basel Consolidated Framework CRE20) and is consistent with the LCR HQLA leveling scheme (refer to LAR Chapter 2).
* Haircuts – To ease reporting efforts and ensure consistency, a single haircut rate has been selected from the range of haircuts assigned by central banks for each type of security and each major foreign currency in the Securities Haircut Table. While central banks generally prescribed haircuts based on the residual maturity of securities, haircuts were not directly comparable as different residual maturity buckets were adopted by different central banks, other things being equal. Other currencies determined to be eligible by OSFI are to be haircut using the Canadian dollar haircuts. Note that the haircuts are subject to change as central banks adjust their haircuts for standing liquidity facilities.

## 2. Cash inflows

### 2.0 Inflows overview

Cash inflows from assets which do not meet the criteria defined for EULA may be recorded at the time of maturity provided they meet the criteria defined in LAR Chapter 4 paragraphs 22 and 25-37.

Cash inflows should be recorded as positive amounts. Inflows should only be recorded for assets as prescribed. In exceptional situations where inflows are recorded from liabilities, institutions must provide in the "Comments" column an explanation and rationale to justify the resulting inflow.

The asset types for which inflows need to be reported are listed in the template. Granularity of reporting for inflows should be consistent across balance sheets (for each currency).

### 2.1 Inflow maturities

Unless instructed otherwise, inflows should always be allocated to maturity buckets corresponding with their contractual maturity or earliest option date (refer to LAR Chapter 4 para. 25, 27). Exceptions noted in Chapter 4 of the LAR Guideline include:

* Cash resources (deposits with central banks and other financial institutions) should be reported as inflows in the first week (LAR Chapter 4 para. 26).
* EULA should be reported as inflows in the first week after the appropriate haircut prescribed by the Securities Haircut Table (LAR Chapter 4 para. 16).
* Common equity holdings, which receive inflows in accordance with treatments presented in LAR Chapter 4 paragraphs 29-30.
* Loans with no specific maturity, which may only report inflows associated with minimum payments that are contractually due. These minimum payments are assumed to occur at the latest possible time band within that period (LAR Chapter 4 para. 32).
* Bankers' acceptances reported as assets (customer's liability under acceptance) should be reported as inflows at the latest contractual maturity date of the underlying facility (LAR Chapter 4 para. 28).
* Balances related to on-balance sheet assets which are not mentioned in Chapter 4 of the LAR Guideline are to be reported in the NCCF as "Other Assets – Other Assets – Other Assets", but no cash inflow value is attributed to them (LAR Chapter 4 para. 37).

### 2.2 Cash resources

Report cash balances currently held by the institution that are immediately available to meet obligations on line "Cash Resources – Coins and Bank Notes". They are treated as cash inflows in the first time bucket (i.e. week one).

#### Deposits with central banks

Report cash deposits placed at central banks to meet reserve requirements which cannot be drawn down in times of stress on line "Cash Resources – Deposits with Central Banks – Deposits with Central Banks – Mandatory". They are treated as cash inflows in the time bucket when they become unencumbered.

Report cash deposits placed at central banks which can be drawn down in times of stress on line "Cash Resources – Deposits with Central Banks – Deposits with Central Banks – Unencumbered". They are treated as cash inflows in the first time bucket (i.e. week one).

#### Deposits with FIs (LAR Chapter 4 para. 26)

Report demand deposits at FIs that can be drawn upon demand under "Cash Resources – Deposits with FIs – Demand Deposits at FIs". They are treated as cash inflows in the first time bucket (i.e. week one).

Report term deposits at FIs that cannot be drawn until term maturity under "Cash Resources – Deposits with FIs – Term Deposits at FIs". They are treated as cash inflows in the earliest contractual maturity time buckets.

Notice deposits with notice requirements shorter than 7 days should be reported on the line "Cash Resources – Deposits with FIs – Demand Deposits at FIs". Notice deposits with notice requirements longer than 7 days should be reported on the line "Cash Resources – Deposits with FIs – Term Deposits at FIs".

For cash deposits with FIs that are encumbered and pledged as collateral, refer to sections 2.7 (Derivative Related Assets) and 3.8 (Derivative Related Liabilities) below.

### 2.3 Securities

The NCCF aims to simulate an FI's ability to withstand a period of stress. One of the assumptions is that FIs will be able to generate funding by selling off certain securities in the secondary market at a discounted price. The discounted price is simulated through the haircuts on the market value of various securities.

For all securities, report balance (at market value, excluding accrued interest) and inflows (at contractual amounts) in the contractual maturity time buckets, or, for securities without maturity (e.g. common equity shares), only the balance is to be reported.

For securities qualifying as EULA, balances are treated as cash inflows in the first time bucket (i.e. week one) after applying the appropriate haircut as prescribed in the Securities Haircut Table (LAR Chapter 4 para. 16-21 and 23-24). Upon maturity of an EULA, the haircut amount of the maturing inflow would be recognized in the contractual maturity time bucket.

Refer to [Example 1 in the Appendix](#ex1).

For securities not eligible as EULA, contractual inflows are recognized under the appropriate time bucket based on contractual maturity (LAR Chapter 4 para. 27).

#### Fungibility of USD securities as CAD EULA

For the Comprehensive NCCF, U.S. liquid assets can be reported in the Canadian dollar balance sheet provided they meet the criteria of Canadian EULA, i.e. eligible at the Bank of Canada (LAR Chapter 4 para. 19).

To report fungible USD securities in the CAD balance sheet, report balances (at market value, excluding accrued interest) and inflows (at contractual amounts) in the corresponding categories after appropriate Canadian haircuts. In the "Comments" field for each category of securities transferred, report the amount of USD securities reported in the CAD balance sheet.

#### Exchange-Traded Notes (ETNs)

Report balance (at market value) and inflows (at contractual amounts) in the contractual maturity time buckets under:

* **Comprehensive NCCF:** "Securities – Corporate Bonds and Paper – FI Issued Corporate Bonds and Paper (Low rated) – FI issued unsecured bonds and paper (Low rated)"; or
* **Streamlined NCCF:** "FI & Non-FI Issued Corporate Bonds and Paper (Low/not rated)"

Inflows are recognized under the appropriate time bucket according to the original contractual maturity.

#### Eligible common equity shares

For common equity shares held by the financial institution, eligible non-financial equities are shares that meet the criteria set out in LAR Chapter 2 paragraph 47(c) and the operational requirements in LAR Chapter 2 section 2.2.A.2. Report the balance at market value under "Securities – Equities – Eligible Non-Financial Common Equity Shares". An inflow is recognized for 50% of the balance in week 4 (LAR Chapter 4 para. 29).

Refer to [Example 2 in the Appendix](#ex2).

Eligible financial institution common equity shares are shares that meet the operational requirements in LAR Chapter 2 section 2.2.A.2. Report the balance at market value under "Securities – Equities – Eligible Financial Common Equity Shares". Inflows are recognized according to the following schedule: 12.5% in month 2, 25% in month 3, and 12.5% in month 4 (LAR Chapter 4 para. 30).

Refer to [Example 3 in the Appendix](#ex3).

#### Other equities

For all other equities, report the balance at market value only under "Securities – Equities – Other Equities". No liquidity value will be attributed.

Units in pooled investment vehicles (e.g. exchange-traded funds) should also be reported under "Securities – Equities – Other Equities". Report only the balance at market value. Given the varying degree of ability to liquidate positions and the dependence on a liquid market (even though some of these units may be exchange-traded), no liquidity value will be attributed.

#### Look-through approach

For equity total return swaps (TRS), the assets linked to TRS exposures will be given the same treatment as in LCR (LAR Chapter 4 para. 17, and Chapter 2 para. 47(c)).

#### Own securities held by FI

For own securities held by the financial institution (e.g. banker's acceptances, commercial paper), report balance and inflows in the contractual maturity time buckets "Securities – Securities Bank's Own – Not Eliminated". Contractual inflows are recognized under the appropriate time bucket based on contractual maturity.

### 2.4 Loans – Mortgages

Inflows from mortgages should be reported under the appropriate time bucket based on contractual maturity (LAR Chapter 4 para. 25).

Securitised mortgages (and unsecuritised) are to be reported at market values. Unsecuritised mortgages should be reported at book value when the assumptions adopted reflect current market conditions.

#### Balance at maturity

Financial institutions should separately report mortgage balances at maturity and periodic amortization payments as inflows on lines "Balance at Maturity" and "Payments", respectively, under the appropriate mortgage type.

#### Payments

For "Payments", financial institutions have the choice to report blended mortgage amortization and interest payment inflows or suppress reporting of interest payment and report mortgage amortization payment inflows only FIs are to specify the alternative adopted in the "Comments" column of the appropriate rows.

#### Securitised mortgages

* For mortgages securitised and unsold, report balances at maturity and periodic amortization payments of the appropriate mortgage types under "Loans – Residential/Commercial Mortgages – Securitised Residential/Commercial Mortgages – EULA Securitised Res/Coml Mort (Balance at Maturity/Payments)".

  Balances at maturity and the balance of periodic amortization payments of mortgage securitised and unsold are treated as cash inflows in the first time bucket (i.e. week one) after applying the appropriate haircut (i.e. the Mortgage Backed Securities (MBS) – Agency MBS – Agency MBS (High rated) haircut).

  For mortgages securitised but unsold for an extended period of time, reporting of any structural declines in loan value under unfavourable market conditions may be requested by OSFI.
* For mortgages securitised and used to back Canada Housing Trust (CHT) swaps, report both "balance at maturity" and "periodic amortization payments" in the appropriate mortgage types under "Loans – Residential/Commercial Mortgages – Securitised Residential/Commercial Mortgages – Encumbered Securitised Res/Coml Mort (Balance at Maturity)" in time buckets corresponding to the CHT swaps contractual maturity.

  No cash inflow value will be received until maturity of CHT swaps. Balance at maturity inflows will be recognized as cash inflows in the contractual maturity time buckets.

  For mortgages securitised and encumbered, the corresponding liability is not assumed to roll over (LAR Chapter 4, para. 39).
* For mortgages securitised and sold to third parties, report balance at maturity and periodic amortization payments in the appropriate mortgage types under "Loans – Residential/Commercial Mortgages – Securitised Residential/Commercial Mortgages – Encumbered Securitised Res/Coml Mort (Balance at Maturity/Payments)".

  Periodic amortization payments and payments of balance at maturity are recognized inflows in payment time buckets.

  For mortgages securitised and encumbered, the corresponding liability is not assumed to roll over (LAR Chapter 4, para. 39).
* For Mortgage-Backed Securities purchased from third parties, report balance and periodic amortization payments of the appropriate mortgage type under "Securities – Mortgage-Backed Securities (MBS)".

  The balance is treated as a cash inflow in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. For MBS that are subject to a 100% haircut, periodic amortization payments are recognized in each time bucket.

#### Unsecuritised mortgages

For unsecuritised mortgages, report balance at maturity and periodic amortization payments in the appropriate mortgage types under "Loans – Residential/Commercial Mortgages – Residential/Commercial Mortgage Ins/Not Ins (Balance at Maturity/Payments)".

As mortgages are assumed to roll over, no cash inflow value is assigned to balances at maturity, and only contractual inflows (i.e. interest and amortization payments) are recognized as inflows (under "Payments" lines of each mortgage type) (LAR Chapter 4 para. 25).

As mortgages are assumed to roll over, monthly inflows reported in the "Payments" lines are assumed to continue at the same level. Financial institutions have the choice to recognize inflows weekly in month 1 and monthly in month 2 to 12 with either of the following alternatives:

1. Contractual periodic amortization payments for each period, or
2. Assuming monthly amortization payments will continue at the same level as amortization payment for the first month, i.e. inflows from payments for the first month will be recognized as inflows in each of the month 2-12 time buckets

FIs are to specify in the "Comments" field of the appropriate rows: "CONTRACTUAL" if alternative 1 from above is adopted, and "MONTH 1" if alternative 2 from above is adopted.

### 2.5 Loans – Other than mortgages

Inflows from loans should be reported under the appropriate time bucket based on contractual maturity (LAR Chapter 4 para. 25).

#### Loan interest inflows

Financial institutions have the choice to report blended loan amortization and interest payment inflows or suppress reporting of interest payment and report loan amortization payment inflows only under the appropriate type of loan. The alternative adopted must be consistent across all loan types. FIs are to specify the alternative adopted in the "Comments" field of the appropriate rows.

#### Fixed maturity loans

For loans with fixed maturities, report balance and maturing payments in the appropriate loan types under "Loans – Personal/Business and Government Loans – Personal/Bus and Gov Loans – Fixed Maturity". Maturing payments are recognized as inflows at a rate of 50% in the contractual maturity time buckets for business and government loans, and at 100% for personal loans.

Refer to [Example 17 in the Appendix](#ex17).

#### Open maturity loans (LAR Chapter 4 para. 32)

For loans with no specific maturity, report balance and contractual minimum payments in each period under "Loans – Personal/Business and Government Loans – Personal/Bus and Gov Loans – Open Maturity (with minimum payments)", "Loans – Call Loans – Call Loans (with minimum payment)", or "Loans – Other Loans – Credit Cards", depending on the loan type. Contractual payments are recognized as inflows at a rate of 50% in the contractual maturity time buckets for business and government loans, and at 100% for the other types of loans.

Refer to [Example 17 in the Appendix](#ex17).

For open maturity loans that have no contractual minimum payments, report balances only under "Loans – Personal/Business and Government Loans – Personal/Bus and Gov Loans – Open Maturity (with no minimum payments)" or "Loans – Call Loans – Call Loans (with no minimum payment)", depending on the loan type. No liquidity value will be attributed.

#### Swapped intrabank koans (LAR Chapter 4 para. 33)

Swapped intrabank loans are swaps within the same financial institution related to funding in one currency for lending or investing in another currency (e.g. Northbound or Southbound transactions).

Report balance and maturing inflows in each period under "Loans – Other Loans – Swapped Intrabank Loans" at gross swapped loan value:

* Intrabank inflows and outflows with the same subsidiary/entity can be netted provided they occur in the same time bucket.
* Intrabank inflows and outflows with different subsidiary/entities cannot be netted against each other, report inflows at gross swapped loan value.

#### Affiliated entity loans

Affiliated entity loans have the same characteristics as "Personal/Business and Government Loans", with the exception that they are made to a related entity (for example, to a subsidiary). For loans provided to an affiliated entity, report balance and contractual inflows in each period under "Other Loans – Loans to Affiliates".

#### Customer's liability under acceptance (LAR Chapter 4 para. 28)

The drawn part of an FI's guarantee for a customer under a banker's acceptance (BA) should be reported as a loan asset under "Customer's Liability under Acceptance". Report balance and inflows at the latest contractual maturity dates of the underlying facility under "Loans – Other Loans – Customer's Liability under Acceptance". Inflows are recognized in the latest contractual maturity time buckets of the underlying facility.

Similar liquidity treatment is to be applied for all products drawn under multiple products arrangements.

### 2.6 Reverse repurchase agreements and security financing transactions

Reverse repurchase agreements (reverse repos) and security financing transactions (SFTs) are treated similarly under the LAR, Chapter 4-NCCF. Relevant paragraphs in the LAR Chapter 4 are 21, 34, and 35.

For reverse repos and securities financing cash legs, report balance and maturing inflows in each period (both at loan value) under "Reverse Repo (R.Repo) and Securities Borrowed (SB)". Inflows are recognized in the contractual maturity time buckets.

#### Collateral

For securities (other than common equity shares) received as collateral for reverse repos and security financing transactions, report balance and outflows upon contractual maturity of the related reverse repo/security financing transaction (both at market value of rehypothecatable collateral) in the "Collateral – Reverse Repo (R.Repo) Collateral In" section. Collateral balances are treated as cash inflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral outflows are recognized in the contractual maturity buckets after the appropriate haircut.

For common equity shares received as collateral, report balance and outflows upon contractual maturity of the related reverse repo/security financing transaction (both at market value of rehypothecatable collateral) in the "Collateral – Reverse Repo (R.Repo) Collateral In" section. For equity collateral received, inflows are recognized in line with treatments described in section 2.3 (Securities – Common Equity Shares).

Where equity collateral is returned after the time buckets specified in section 2.3, the cumulative inflow (from week 1 up to the time period when the collateral is returned) is recognized in the period. For equity collateral returned, outflows are limited to the amount recognized as inflows.

Refer to [Example 12 in the Appendix](#ex12).

### 2.7 Other assets

#### Streamlined NCCF

For assets not reported in previous sections, institutions should report the balances of all these other assets under the "Other Assets". No liquidity value will be attributed (LAR Chapter 4 para. 37).

#### Comprehensive NCCF

##### Derivative-Related Assets (DRA)

###### Netting

Unless specified otherwise, derivative cash flows may be reported on a net basis by counterparty, only where a valid master netting agreement exists (LAR Chapter 4 para. 36).

###### Foreign exchange derivatives

For all foreign exchange (FX) related derivative assets (e.g. FX forward, cross currency swap), report the balance only at market value under "Other Assets – Derivative Related Assets (DRA) – FX and Cross Currency Swap Assets".

In the USD balance sheet only, report contractual cash flows (at nominal value) across all currencies in each period under "Other Assets – Derivative Related Assets (DRA) – FX and Cross Currency Swap Assets".

In all balance sheets other than USD, no liquidity value will be attributed. In the USD balance sheet, the sum of net contractual cash flow over all periods is recognized as a cash inflow in the first time bucket (i.e. week 1).

In the USD balance sheet, contractual cash flows (at nominal value) related to FX derivatives are to be reported in "FX Derivative" section in their contractual maturity buckets for each currency affected separately. They are for information purposes only and would not affect NCCF position of the financial institution.

Refer to [Example 13 in the Appendix](#ex13).

###### Option-related cash flows

Options should be assumed to be exercised when they are 'in the money' to the option buyer as at reporting date. Calculate, in accordance with the existing valuation methodologies, expected contractual cash flows related to options. Report the balance at market value and expected contractual cash inflows in each period under "Other Assets – Derivative Related Assets (DRA) – Other DRA". Expected contractual inflows are recognized in each time bucket.

###### DRA Adjusted for Qualifying Equity Futures

The "Other DRA" can be used to adjust offsetting cash flows for qualifying Delta One hedged equity futures. The liquidity value for the cash flows nets to 0. The full notional value of the position is realized at expiry of the future as a combination of any calculated equity value and the DRA entry.

Refer to [Example 14 in the Appendix](#ex14).

###### All other DRA

Report balance at market value and contractual inflows at nominal value in each period (LAR Chapter 4 para. 36) on the line "Other Assets – Derivative Related Assets (DRA) – Other DRA". Inflows are recognized in contractual maturity time buckets.

Refer to [Example 8](#ex8) and [9 in the Appendix](#ex9).

###### Collateral

Where securities have been received as collateral for DRAs, report balance and outflows upon contractual maturity of the related DRA (both at market value of rehypothecatable collateral) in the "Collateral – Pledging and Encumbrances – Derivative and Clearing (D/C)" section. Collateral balances are treated as cash inflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral outflows are recognized in the contractual maturity buckets after the appropriate haircut.

Where DRAs are collateralized with cash, report balance of net cash collateral received and outflows when the related DRA is settled under "Other Liabilities – Cash Collateral Received". The balance is recognized as an inflow in the first time bucket (i.e. week 1) and outflows are recognized in time buckets when related DRAs are settled.

Refer to [Example 8](#ex8) and [9 in the Appendix](#ex9).

###### Collateral swaps

Where collateral swaps meet the conditions set out in LAR Chapter 4 paragraph 22, for securities received as collateral, report balance and outflows upon contractual maturity of collateral swaps (both at market value of rehypothecatable collateral) in the "Collateral – Reverse Repo (R.Repo) Collateral In" section. Collateral balances are treated as cash inflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral outflows are recognized in the contractual maturity buckets after the appropriate haircut.

##### Other assets

###### Cash collateral pledged

For the instructions for the section "Cash Collateral Pledged", refer to sections 3.8 and 3.9 of these instructions.

###### Commodities

Report balances for precious metals, precious metal loans and other commodities under "Commodities". No liquidity value will be attributed.

###### Other assets

For all other assets not mentioned in Chapter 4 of the LAR Guideline, report balances under "Other Assets". No liquidity value will be attributed (LAR Chapter 4 para. 37).

## 3. Cash outflows

### 3.0 Outflow overview

Outflows comprise either of outflows related to existing liabilities, and outflows from off-balance sheet items. Cash outflows should be recorded as negative amounts.

Outflow treatments for liabilities differ depending on whether the liability has a contractual maturity or whether the liability has no specific maturity (non-defined or open maturity). Liabilities for which outflows need to be reported are listed in the template. Detailed definitions and treatments are described in Chapter 4, section 4.6 of the LAR Guideline.

Outflows resulting from draws against existing credit and liquidity facilities have to be reported in the earliest contractual time bucket. Definitions and treatments are described in Chapter 4, in the section 4.6 - "Off-balance sheet items".

### 3.1 Outflow maturities

Unless instructed otherwise, liabilities with contractual maturities are not assumed to roll over and cash outflows should be allocated to maturity buckets corresponding with their contractual maturity or earliest option date. Exceptions noted in Chapter 4 of the LAR Return include:

* Certain retail/small business customer and wholesale deposits are allowed to roll over at prescribed rates. Refer to Deposit sections below (section 3.2-3.5) for more details.
* Bank-sponsored acceptances are allowed to roll over at prescribed rates.
* Securities sold short and funding guarantees to subsidiaries and branches should all be assumed to have immediate cash outflows (i.e. first maturity bucket) of principal.
* Credit and Liquidity facilities to extend funds at a future date are presumed to be drawn according to the prescribed rates in the earliest contractual time bucket.
* Balances related to on-balance sheet liabilities which are not mentioned in Chapter 4 of the LAR Guideline are to be reported in the NCCF as Other Liabilities, but no cash outflow value is attributed to them.

### 3.2 Deposits

Outflows from deposits and funding liabilities should be reported under the appropriate time bucket based on contractual maturity. Unless instructed otherwise, deposits will generally run-off on a declining balance basis[Footnote 1](#fn1) according to the run-off schedules. Run-off rates are summarized in Chapter 4 of the LAR Guideline.

#### Deposit interest outflows

Financial institutions have the choice to report blended deposit repayment and interest payment outflows or suppress reporting of interest payment outflows.

### 3.3 Deposits – Retail and small business

Retail and small business deposits are assumed to renew, net of the portion that is assumed to run-off according to the specified run-off schedule. For select term deposits, run-offs occurring in the first four weeks are based on an equivalent monthly run-off rate, obtained by multiplying the weekly run-off rate by a factor of four. The tab "Appx 1.Ref Rates" specifies the term deposits to which this treatment applies.

The threshold for small business customer deposits is $5 million (CAD) or less, on an individual account basis (LAR Chapter 4 para. 5).

#### Deposit insurance

The treatment of insured deposits differs depending on the characteristics of the deposit insurance schemes. Two types are defined:

* **Type 1 insured** – defined as deposit insurance that meets criteria set out in the LAR Chapter 2 paragraph 59
* **Type 2 insured** – defined as deposit insurance that does not meet criteria set out in the LAR Chapter 2 paragraph 59

#### Demand deposits

Only the "Balance" field should be populated for each type of demand deposit. Demand deposits are assumed to be renewed weekly for the first month and monthly from month 2 to month 12 with a portion of the remaining balance to be run-off based on rates of the appropriate deposit type. Outflows are recognized based on the run-off rates in Table 1 of the LAR Chapter 4.

Refer to [Example 4 in the Appendix](#ex4).

Temporarily, the Liability placeholder 1 field should be used to populate balances of Demand deposits from a partnership agreement deemed stable according to LAR Chapter 4, para. 52.

Temporarily, for Exchange traded notes (ETNs) and partnership demand deposits categorized as less stable, include them in the balance of RSB demand deposits managed by an unaffiliated third-party. This will apply until new return templates can be operationalized as part of OSFI's regular data management updates.

#### Cashable term deposits

Cashable term products in which the customer has an option for early redemption should be treated as a demand deposit at the first customer option date (LAR Chapter 4 para. 40).

Report balance of maturing deposits in each period. Outflows are recognized for maturing deposits and are then treated like demand deposits in subsequent periods (i.e. run-off on a declining basis). Run-off rates that are applicable are generally aligned with those for demand deposits with the same deposit characteristics in Table 1 of the LAR Chapter 4.

Refer to [Example 5 in the Appendix](#ex5).

#### Term deposits

Round the original terms of retail and small business term deposits to original term buckets of 30 days, 60 days, 90 days, 180 days, 1 year, and more than 1 year. If the original term is less than 30 days, round to the 30-day term bucket; if the original term of a term deposit falls on the mid-point between two term buckets, assign it to the lower bucket.

Group and report balance and maturing deposits with the same characteristics and rounded original term in the appropriate line.

The remaining balance of the term deposits are assumed to renew at the same tenor as the rounded original term of the deposits. Outflows are recognized for maturing deposits and are then treated like demand deposits in subsequent periods (i.e. run-off on a declining basis)., based on run-off rates in Table 1 of the LAR Chapter 4 (LAR Chapter 4 para. 38, 39).

Refer to [Example 6](#ex6) and [7 in the Appendix](#ex7).

#### Structured notes

Structured notes are debt products with embedded derivatives that alter the risk and return profiles of the securities.

For retail and small business structured notes where the customer has an option to call, report balance at market value and outflows at nominal amounts. The maturity time bucket should align with the next available call date or be determined based on probability and expected market conditions, under line "Deposits – Retail and Small Business Structured Notes – RSB Structured Notes Cust Call". Outflows are recognized based on the next available call date or determined using probability and expected market conditions.

For all other retail and small business structured notes, report balance at market value and outflows at nominal amounts in the maturity time bucket under "Deposits – Retail and Small Business Structured Notes – RSB Structured Notes No Cust Call".

### 3.4 Deposits – Wholesale

Wholesale deposits, other than unsecured term deposits, are assumed to renew with a portion of the remaining deposit balance to be run off every time a renewal is to take place.

An exception to this treatment is for non-operational demand deposits from financial institutions (FIs), where the full balance is assumed to run-off evenly during the first 4 weeks (i.e. 25% of the original balance each week).

For select term deposits, run-offs occurring in the first four weeks should be based on an equivalent monthly run-off rate, obtained by multiplying the weekly run-off rate by a factor of four. (LAR Chapter 4 para. 38, 39).

Refer to [Example 16 in the Appendix](#ex16).

#### Approved jurisdiction

* Approved jurisdiction ("within approved jurisdiction") – defined as a jurisdiction that adopts a run-off factor of 3% on stable deposits that have "type 1" deposit insurance, as defined in section 3.3.
* Other jurisdiction ("outside of approved jurisdiction") – defined as a jurisdiction that doesn't adopt a run-off factor of 3% on stable deposits, irrespective of whether the jurisdiction's deposit insurance scheme is categorized as "type 1" or "type 2", as defined in section 3.3.

#### Demand deposits

Only the "Balance" field should be populated for each type of demand deposit. Accordingly, no amounts should be reported in the maturity buckets for demand deposits. Except for non-operational deposits from FIs, demand deposits are assumed to be renewed weekly for the first month and monthly from month 2 to month 12 with a portion of the remaining balance to be run off based on rates determined by deposit type (LAR Chapter 4 para. 59-63). Outflows are recognized based on the run-off rates in Table 1 of the LAR Chapter 4.

For demand deposits sourced from Non-Bank Financial Intermediaries (NBFIs) with underlying retail characteristics, populate the balances in the Liability Placeholder line 3.

#### CommCorp and wholesale notice deposits, where withdrawal notification has been provided

For deposits requiring a notification of withdrawal, and when this notification has been provided by the customer, report the amounts called in the earliest contractual time buckets for withdrawal by the customer.

Any portion of notice deposits where the customer has the option to make partial withdrawals without notice should be reported in the earliest contractual time bucket.

#### Commercial and corporate operational term deposits (with Less than 30 days original term)

Commercial and corporate operational term deposits with original term of 30 days or less are assumed to renew every 30 days at the same rate as commercial and corporate operational demand deposits. Report these deposits under the corresponding lines in the section "CommCorp and Wholesale Demand/Notice Deposits (Original Term ≤30 Days) – Operational". Outflows are recognized for maturing payments in the current period, as well as all renewal periods, based on the commercial and corporate operational demand deposit run off rates in Table 1 of the LAR Chapter 4.

#### All other term deposits

Term deposits from commercial, corporates, sovereigns, central banks, PSEs and MDBs are assumed to run-off according to the rate in Table 1 of Chapter 4 of the LAR Guideline and renew every 30 days. All other wholesale term deposits are not assumed to be renewed. Report balance and maturing outflows in each period. Outflows are recognized in the contractual maturity time buckets.

#### CommCorp and wholesale notice deposits (original term >30 days) - Operational & non-operational

Notice deposits from commercial, corporates, and wholesale clients where the notification requirement is longer than 30 days will be treated as term deposits for purposes of the NCCF.

### 3.5 Deposits – Other

#### Customers' Banker's Acceptances (BAs) issued

For BAs that the FI has guaranteed for its customers, report balance and contractual payments in each period under "Deposits – Other Deposits – Customers' BAs Issued". Outflows are recognized in contractual maturity time buckets (LAR Chapter 4 para. 45).

#### Swapped intrabank deposits

Swapped intrabank deposits are swaps within the same financial institution related to funding in one currency for lending/investing in another currency (e.g. Northbound/Southbound transactions). They are to be reported in "Deposits – Other Deposits – Swapped Intrabank Deposits".

Outflows are reported at gross swapped deposit value, where:

* Payments to different subsidiaries/entities are not to be netted against each other.
* Intrabank inflows and outflows with the same subsidiary/entity can be netted provided they occur in the same time bucket.

#### Affiliated entity deposits

Affiliated entity deposits have the same characteristics as "Wholesale Term Deposits", with the exception that they are received from a related entity (for example, from a subsidiary). For deposits received from an affiliated entity, report balance and contractual outflows in each period under "Other Deposits/Guarantees – Deposits from Affiliates".

### 3.6 Wholesale issuances

Liabilities related to wholesale issuances are not assumed to roll over unless otherwise specified, and cash outflows should be allocated to maturity buckets corresponding to their contractual maturity or earliest option date.

#### Banker's Acceptances (BAs)

Report balances at market value and maturing payments at nominal amounts of BAs issued by the reporting financial institution in its own name under "Wholesale Issuance – Wholesale Unsecured Debt Issuance – Banker's acceptances (BAs)".

Group and report BAs in the appropriate line corresponding to their original terms "1-/2-/3-month BA issued". For BAs with original terms shorter than one month, group and report them in the "1-month BA issued".

BAs are assumed to renew at the same tenor as the original term of the deposits. Outflows are recognized for maturing payments in the current period, as well as all renewal periods, based on a run-off rate of 100% (LAR Chapter 4 para. 45).

#### Wholesale/Commercial structured notes

For wholesale/commercial structured notes, where the customer has an option to call, report balance at market value and recognize outflows at nominal amounts. The maturity time bucket should align with the next available call date or be determined based on probability and expected market conditions, under line "Deposits – Wholesale Issuance – Wholesale Unsecured Debt Issuance – Other unsecured debt issuance – Wholesale/Commercial Structured Notes". Outflows are recognized based on the next available call date or determined using probability and expected market conditions.

For all other wholesale/commercial structured notes, report balance at market value and outflows at nominal amounts in the maturity time bucket under the same line. Outflows are recognized in the maturity time buckets.

#### Other FI-Owned securitizations

Report balance and outflows from other FI's own securitizations where the funding is arranged through structured investment vehicles is assumed to not roll over. Outflows are recognized in contractual maturity time buckets. (LAR Chapter 4 para. 41)

#### Other secured and unsecured wholesale issuance

For all other secured and unsecured wholesale issuances not discussed above, report balances and maturing outflows in each period in the corresponding rows of the relevant transaction types. Outflows are recognized in the contractual maturity time buckets. (LAR Chapter 4 para. 41).

### 3.7 Repurchase agreements and security financing transactions

Repurchase agreements (repos) and security financing transactions are treated similarly under the LAR Chapter 4 NCCF. Relevant paragraphs in the LAR Chapter 4 are 43 and 74.

For repos and securities financing cash legs, report balance and maturing outflows in each period (both at loan value) under "Repo and Securities Lent (SL)". Outflows are recognized in the contractual maturity time buckets.

#### Collateral

For securities (other than common equity shares) pledged as collateral for repos and security financing transactions, report balance and inflows upon contractual maturity of the related repo/security financing transaction (both at market value of collateral) in the "Collateral – Repo Collateral Out" section. Collateral balances are treated as cash outflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral inflows are recognized in the contractual maturity buckets after the appropriate haircut.

For common equity shares pledged as collateral, report balance and inflows upon contractual maturity of the related repo/security financing transaction (both at market value of collateral) in the "Collateral – Repo Collateral Out" section.

For equity collateral returned by the counterparty, inflows are recognized in line with treatments described in section 2.3 (Securities – Common Equity Shares). Where equity collateral is returned after the time buckets specified in section 2.3, the cumulative inflow (from week 1 up to the time period when the collateral is returned) is recognized in the time period when the collateral is returned.

Refer to [Example 11 in the Appendix](#ex11).

### 3.8 Securities sold short

For existing liabilities related to securities sold short, report balance at market value under "Securities Sold Short" with no haircuts applied to the nominal amounts to be paid back. The balance is recognized as an outflow in the first time bucket (i.e. week 1) (LAR Chapter 4 para. 44).

For reverse repo/security financing transactions related to short sales, report under the appropriate reverse repo/security financing lines.

Where cash margin is posted for short sales, report balance only of cash margin posted under "Other Assets – Cash Collateral Pledged – Cash collateral pledged for short sales". No liquidity value will be attributed.

Refer to [Example 10 in the Appendix](#ex10).

### 3.9 Other liabilities

#### Streamlined NCCF

For liabilities not reported in previous sections, institutions should report the balances of all these other liabilities under the "Other Liabilities". No liquidity value will be attributed.

#### Comprehensive NCCF

##### Derivative Related Liabilities (DRL)

###### Foreign exchange derivatives

For all foreign exchange (FX) related derivative liabilities (e.g. FX forward, cross currency swap), report the balance only at market value under "Other Liabilities – Derivative Related Liabilities (DRL) – FX and Cross Currency Swap Liabilities".

In the USD balance sheet only, report net contractual cash flows (at nominal value) across all currencies in each period under "Other Liabilities – Derivative Related Liabilities (DRL) – FX and Cross Currency Swap Liabilities".

In all balance sheets other than USD, no liquidity value will be attributed. In the USD balance sheet, the sum of net contractual cash flow over all periods is recognized as a cash outflow in the first time bucket (i.e. week 1).

In the USD balance sheet, cash flows related to FX derivatives are to be reported in"FX Derivative" section for each currency affected separately. They are for information purposes only.

###### Option-Related cash flows

Institutions should calculate, in accordance with their existing valuation methodologies, expected contractual cash flows related to options. Options should be assumed to be exercised when they are 'in the money' to the option buyer as at reporting date (LAR Chapter 4 para. 46). Report the balance at market value and expected contractual cash outflows in each period under "Other Liabilities – Derivative Related Liabilities (DRL) – Other DRL". Expected contractual outflows are recognized in each time bucket.

###### All other DRL

Report balance at market value and contractual outflows at nominal value in each period (LAR Chapter 4 para. 46) under "Other Liabilities – Derivative Related Liabilities (DRL) – Other DRL". Outflows are recognized in contractual maturity time buckets.

Unless specified otherwise, derivative cash flows may be reported on a net basis by counterparty, only where a valid master netting agreement exists (LAR Chapter 4 para. 46).

###### Collateral

Where securities have been pledged as collateral for DRLs, report balance and inflows upon contractual maturity of the related DRL (both at market value of collateral) in the "Collateral – Pledging and Encumbrances – Derivative and Clearing (D/C)" section. Collateral balances are treated as cash outflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral inflows are recognized in the contractual maturity buckets after the appropriate haircut.

Where DRLs are collateralized with cash, report balance of net cash collateral pledged and inflows when cash margins become unencumbered under "Other Assets – Cash Collateral Pledged". The balance is recognized as an outflow in the first time bucket (i.e. week 1) and inflows are recognized in time buckets when cash margins become unencumbered.

###### Collateral swaps

Where collateral swaps meet the conditions set out in LAR Chapter 4 paragraph 22, for securities pledged as collateral, report balance and inflows upon contractual maturity of collateral swaps (both at market value of collateral) in the "Collateral – Repo Collateral Out" section. Collateral balances are treated as cash outflows in the first time bucket (i.e. week one) after the appropriate haircut as prescribed in the Securities Haircut Table. Collateral inflows are recognized in the contractual maturity buckets after the appropriate haircut.

##### Other liabilities

###### Cash collateral received

For the instructions related to the section "Cash Collateral Received", refer to section 2.7 of these instructions.

###### Commodities short

Report balances for precious metal sold short, precious metal deposits and other commodities under "Commodities Short". No liquidity value will be attributed.

###### Other liabilities

For all other liabilities not mentioned in Chapter 4 of the LAR Guideline, report balances under "Other Liabilities". No liquidity value will be attributed (LAR Chapter 4 para. 74).

### 3.10 Off-Balance sheet commitments

#### Commitments

Report balances of credit or liquidity facilities that are committed (irrevocable or conditionally revocable) or uncommitted (revocable) by corresponding type in week 1 or in the earliest contractual time bucket. Where enforceable notification periods are required, the amounts should be reported in the time bucket upon expiry of the notice periods.

The applicable draw rates are available in Table 2 of Chapter 4 of the LAR Guideline.

Refer to [Example 15 in the Appendix](#ex15).

#### Streamlined NCCF

Regarding "Undrawn amounts related to credit and liquidity facilities to retail and small business customers", institutions may choose to not differentiate transactors from non-transactors; in such case, all balances should be reported in the non-transactor categories.

#### Committed credit facilities to non-financial corporates

Institutions subject to the Comprehensive NCCF must report undrawn amounts of committed credit facilities to non-financial corporates broken down to recognize the existence or absence of operational relationship with the client and to distinguish commercial vs. corporate clients. The definitions of these terms are available in the section Off-balance sheet items in section 4.6 of the LAR Guideline.

IG vs NIG for the balance of undrawn committed credit facilities to non-financial corporates can be reported if available. If unavailable, report these balances based on their relationship characteristic of operational/non-operational in rows 1390 or 1392 for NIG committed credit facilities to non-financial corporates. IG vs NIG reporting for the balance of undrawn committed credit facilities to non-financial corporates will be moved to the memo item section of the NCCF in a future release. The determination of the IG vs NIG classification must be consistent with the internal classification of clients used for risk management purposes (e.g. Borrower Risk Rating, or other internal metrics).

Liquidity facilities are considered drawn when external funding backed by the liquidity facilities has been raised by parties receiving the liquidity facilities.

#### Undrawn amounts related to liquidity facilities for ABCPs

Institutions having structured financing facilities that include the issuance of asset backed commercial paper should report the maturing debt in the corresponding time buckets on the line "Committed liquidity facilities to ABCPs - Maturing Balance". Only debt maturing in the first 4 weeks will be considered as outflows for the NCCF calculation.

Institutions must also report the unutilized capacity of these facilities under the line "Committed liquidity facilities to Unissued ABCPs (reported recognizing notice periods)", in the earliest contractual bucket where the capacity can be drawn. For example, unutilized capacity with a 35 days notice must be reported in month 2. Only unutilized that can be drawn in the first 4 weeks will be considered as outflows for the NCCF calculation.

#### Funding guarantee to subsidiaries

For funding guarantees to subsidiaries, report balance at total nominal amount under "Off Balance Sheet Commitments – Funding guarantee to subsidiaries". The balance is recognized as an outflow in the first time bucket (i.e. week 1) (LAR Chapter 4 para. 44).

## 4. Memo items

The items reported in this section are only for information purposes and do not impact the calculation of the NCCF.

### 4.1 Non-interest income/ expenses

Section 4.1 does not apply to DSIBs. Only Category I and II SMSBs are required to report forecasted cash flows for eligible non-interest income and non-interest expenses (LAR Chapter 1 para. 18 and LAR Chapter 6 section 6.1 OSFI Notes Box).

For both eligible non-interest income and operational expenses, OSFI expects a relatively high level of accuracy for the forecasts reported in the first four weeks. Institutions may be able to use appropriate estimation methods for months 2-12. The cash flows should reflect institutions' best estimates of non-interest income and operational expenses at the date of reporting.

#### Eligible non-interest income

Forecasted cash inflows from eligible non-interest income should be reported in the appropriate time buckets.

#### Non-interest expenses

Forecasted cash outflows from operational expenses should be reported in the appropriate time buckets.

Eligible non-interest income and non-interest expenses are defined in the following table. For further reference, see instructions for [OSFI Return P3 (Income Statement)](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/statement-comprehensive-income-retained-earnings-aoci-p3 "Statement of Comprehensive Income, Retained Earnings and AOCI (P3)") sections 19, 23 to 25 and 28.

##### Eligible non-interest income

* Service Charges on Deposit Accounts
* Fees for Other Payment Services
* Credit and Debit Card Service Fees
* Standby, Commitment and Other Loan Fees
* Income from Securitization of Assets
* Mortgage Fees
* Acceptance Fees
* Guarantees and Letters of Credit Fees
* Payroll Processing
* Investment Management and Custodial Services
* Mutual (Investment) Fund Fees
* Real Estate Commissions
* Underwriting Fees on New Issues
* Securities Commissions and Fees
* Other Commissions and Fees
* Any other income not itemized elsewhere.

##### Non-interest expenses

* Salaries
* Pension Contributions and Other Staff Benefits
* Rental of Real Estate
* Premises, Furniture and Fixtures
* Computers and Equipment
* Advertising, Public Relations and Business Development
* Office and General Expenses
* Capital and Business Taxes
* Directors' Fees and Related Expenses
* Deposit Insurance Premiums
* Association, Clearing and Regulatory Fees
* Professional Fees
* Income taxes
* Other expenses not elsewhere reported.

### 4.2 Expected lending activities

#### All institutions are required to report forecasted cash outflows related to future expected lending activities

These outflows should be reported under the appropriate time bucket based on institutions' best estimates, and where applicable, be representative of new business opportunities as part of going-concern operations (i.e. both contractual and non-contractual outflows). Obligations to extend funds should be reported on a gross basis and not be netted against expected loan paydown activities. Estimates should be representative of the information available at the reporting date, including the volumes in the different stages of the pipeline (factoring in assumptions of realization), fluctuations due to seasonality, and business growth plans and expectations.

For forecasted cash outflows related to future expected lending activities, no amounts are required to be reported in the "Balances" column (i.e. Column G). The ">365" column should report the cumulative forecast of loan outflows as far out into the future as is available.

Cash outflows that institutions should consider as future funding expectations arising from lending activities include, but are not limited to:

1. Residential and Commercial mortgages;
2. Commercial real estate – Interim Finance (Construction loans);
3. Other contractual obligations to extend funds to clients;
4. Other expected non-contractual cash flows related to lending activities.

Institutions should have processes in place to identify sources of significant discrepancy between estimates, including planned growth, and realized cash flows.

##### Residential and commercial mortgages

Renewals: Expected funding of residential and commercial mortgage renewals should be reported under the appropriate time bucket based on the contractual maturity/renewal dates. Renewal estimates may consider renewal rates based on past experience or expectation of realization.

Contractual obligations (commitment accepted by the borrower) excl. renewals: Expected outflows related to funding of new mortgage commitments where the borrower has accepted the commitment and the FI is contractually obligated to fund, should be reported under the appropriate time bucket based on the contractual funding date. Cash outflow estimates should consider applicable commitment funding rates. Where specific data is unavailable for contractual obligations excluding renewals, amounts can be aggregated with other expected funding of mortgages.

Pre-approvals and rate guarantees: Expected outflows related to funding resulting from mortgage pre-approvals and rate guarantees should be reported under the appropriate time bucket based on the projected funding date. Cash outflow estimates should consider applicable funding rates. Where specific data is unavailable for expected funding of pre-approvals and rate guarantees, amounts can be aggregated with other expected funding of mortgages.

Other expected funding of mortgages: Report all other expected contractual mortgage funding outflows not captured in above categories.

##### Commercial real estate – Interim finance (construction loans)

Construction loans include financing for lot servicing, construction or renovation of buildings of all types. Includes financing for the land being improved. This category includes loan types with construction and/or completion risk, regardless of the type of property being financed, except for an individual building a single-family home as his residence.

Expected cash outflows related to funding of construction loans should be reported under the appropriate time bucket based on the projected draw dates. FIs should estimate cash outflows to the best of their abilities, for example, by estimating the real cash outflows project by project, or for larger portfolios, to estimate the forward-looking draw rate for a given period, or another appropriate methodology.

Where specific data is unavailable for commercial real estate – interim finance (construction loans), amounts can be aggregated with other expected non-contractual cash flows related to lending activities.

##### Other contractual obligations to extend funds to clients

Expected cash outflows with respect to other contractual obligations to extend funds not captured elsewhere should be reported under the appropriate time bucket based on the projected funding dates. Where specific data is unavailable for other contractual obligations to extend funds to clients, amounts can be aggregated with other expected non-contractual cash flows related to lending activities.

##### Other expected non-contractual cash flows related to lending activities

Expected cash outflows with respect to other obligations to extend funds not captured elsewhere should be reported under the appropriate time bucket based on the projected funding dates. A future release of the NCCF template will remove the word "non-contractual" from the label to recognize the inclusion of some contractual amounts, where specific data is unavailable to the reporting FRFI.

## Appendix – Reporting examples

The lines starting with term "Input" correspond to the inputs by the reporting institution, and the lines starting with the term "Calculated Cash Flows" show the calculated cash flows following the calculations embedded in the "Calculated Cash Flows" section starts on line 857 of the 2023 Net Cumulative Cash Flow and line 530 of the Streamlined Net Cumulative Cash Flow. The details of the calculation are shown in the lines labeled "Calculation".

In the examples below, balances within parentheses ( ) demonstrate negative balances.

### Example 1: Asset - High rated provincial bond maturing in month 7

Reporting instructions: Report balance in column "balances" and again in the corresponding maturity bucket

Treatment: 1.5% haircut in week 1; 1.5% at maturity

Example 1: Asset - High rated provincial bond maturing in month 7

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: State, Provincial & Agency Government Securities (High rated) | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | 1,000 | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: State, Provincial & Agency Government Securities (High rated) | 1,000 | 985 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | 15 | -no data | -no data | -no data | -no data | -no data | -no data |
| Calculation | no data | =1000 \*(100% −1.5%) | no data | no data | no data | no data | no data | no data | no data | no data | =1000 \*1.5% | no data | no data | no data | no data | no data | no data |

### Example 2: Asset – Non-FI common equity shares

Reporting instructions: Report balance only in column "balances"

Treatment: Equity Non-FI (50% inflow in week 4)

Example 2: Asset – Non-FI common equity shares

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Eligible Non-Financial Common Equity shares | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Eligible Non-Financial Common Equity shares | 1,000 | no data | no data | no data | 500 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | 500 |
| Calculation | no data | no data | no data | no data | =1000 \*50% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 3: Asset – FI common equity shares

Reporting instructions: Report balance only in column "balances"

Treatment: Equity FI (12.5% in month 2, 25% in month 3, 12.5% in month 4)

Example 3: Asset – FI common equity shares

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Eligible Financial Common Equity | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Eligible Financial Common Equity | 1,000 | no data | no data | no data | no data | 125 | 250 | 125 | no data | no data | no data | no data | no data | no data | no data | no data | 500 |
| Calculation | no data | no data | no data | no data | no data | =1000 \*12.5% | =1000 \*25% | =1000 \*12.5% | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 4: Liability – RSB Type 1 insured, stable demand deposits

Reporting instructions: Report balance only in column "balances"

Treatment: RSB Type 1 insured, stable demand/cashable term (0.5% week 1-4; 0.75% month 2-12)

Example 4: Liability – RSB Type 1 insured, stable demand deposits

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | … | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: RSB Type 1 insured, stable demand deposits | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: RSB Type 1 insured, stable demand deposits | (1,000) | (5.00) | (4.98) | (4.95) | (4.93) | (7.35) | (7.30) | (7.24) | … | (6.82) | (902.25) |
| Calculation | no data | =−1000 \*0.5% | =(−1000 +5) \*0.5% | =(−1000 +5 +4.98) \*0.5% | =(−1000 +5 +4.98 +4.95) \*0.5% | =(−1000 +5 +4.98 +4.95 +4.93) \*0.75% | =(−1000 +5 +4.98 +4.95 +4.93 +7.35) \*0.75% | =(−1000 +5 +4.98 +4.95 +4.93 +7.35 +7.3) \*0.75% | … | =(−1000 +5 +4.98 +4.95 +4.93 +7.35 +7.3 +7.24 +7.19 +7.13 +7.08 +7.03 +6.97 +6.92 +6.87) \*0.75% | =−1000 +5 +4.98 +4.95 +4.93 +7.35 +7.3 +7.24 +7.19 +7.13 +7.08 +7.03 +6.97 +6.92 +6.87 +6.82 |

### Example 5: Liability – Cashable term deposit, first customer option date in week 3

Reporting instructions: Report balance in column "balances" and again in the corresponding maturity bucket (i.e. week 3)

Treatment: RSB Type 1 insured, stable demand/cashable term (0.5% week 1-4; 0.75% month 2-12)

Example 5: Liability – Cashable term deposit, first customer option date in week 3

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | … | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: RSB Type 1 insured, stable, cashable term deposit | (1,000) | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: RSB Type 1 insured, stable, cashable term deposit | (1,000) | -no data | -no data | (5.00) | (4.98) | (7.43) | (7.37) | (7.31) | … | (6.89) | (911) |
| Calculation | no data | no data | no data | =−1000 \*0.5% | =(−1000 +5) \*0.5% | =(−1000 +5 +4.98) \*0.75% | =(−1000 +5 +4.98 +7.43) \*0.75% | =(−1000 +5 +4.98 +7.43 +7.37) \*0.75% | … | =(−1000 +5 +4.98 +7.43 +7.37 +7.31 +7.26 +7.20 +7.15 +7.10 +7.04 +6.99 +6.94) \*0.75% | =−1000 +5 +4.98 +7.43 +7.37 +7.31 +7.26 +7.2 +7.15 +7.1 +7.04 +6.99 +6.94 +6.89 |

### Example 6: Liability – Type 1 insured stable fixed term (60-day) deposit maturing in week 2

Reporting instructions: Report balance in column "balances" and again in the corresponding maturity bucket (i.e. week 2)

Treatment: RSB Type 1 insured, stable demand/cashable term/term deposits (0.5% week 1-4 or 2% equivalent month 1;0.75% month 2-12)

Example 6: Liability – Type 1 insured stable fixed term (60-day) deposit maturing in week 2

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: RSB Type 1 insured, stable, fixed term (60-day) deposit | (1,000) | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: RSB Type 1 insured, stable, fixed term (60-day) deposit | (1,000) | -no data | (20) | -no data | -no data | -no data | (7.35) | -no data | (7.29) | -no data | (7.24) | -no data | (7.19) | -no data | (7.13) | -no data | (943.80) |
| Calculation | no data | no data | =−1000 \*2% | no data | no data | no data | =(−1000 +20) \*0.75% | no data | =(−1000 +20 +7.35) \*0.75% | no data | =(−1000 +20 +7.35 +7.29) \*0.75% | no data | =(−1000 +20 +7.35 +7.29 +7.24) \* 0.75% | no data | =(−1000 +20 +7.35 +7.29 +7.24 +7.19) \*0.75% | no data | =( −1000 +20 +7.35 +7.29 +7.24 +7.19 +7.13) |

### Example 7: Liability – Type 1 insured stable fixed term (1 year) maturing in week 4

Reporting instructions: Report balance in column "balances" and again in the corresponding maturity bucket (i.e. week 4)

Treatment: RSB Type 1 insured, stable demand/cashable term/term deposits (0.5% week 1-4 or 2% equivalent month 1;0.75% month 2-12)

Example 7: Liability – Type 1 insured stable fixed term (1 year) maturing in week 4

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: RSB Type 1 insured, stable, fixed term (1 year) deposit | (1,000) | no data | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: RSB Type 1 insured, stable, fixed term (1 year) deposit | (1,000) | -no data | -no data | -no data | (20) | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | (980) |
| Calculation | no data | no data | no data | no data | =−1000 \*2% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | =−1000 +20 |

### Example 8: DRA with cash collateral – DRA position marked to market at $1,000 at the reporting date; maturing in week 3

For this transaction, we consider a profit of $1,000 requiring that the counterparty posts cash collateral. The reporting institution deposits the cash collateral at another FI and the DRA position has therefore a value of $1,000. Accordingly, for this transaction:

* Assets = 2,000 (demand deposit at FIs + DRA Asset)
* Liabilities = 1,000 (cash collateral received)
* P&L = +1,000

#### Reporting instructions

1. Report under the line the "Demand Deposits at other FIs" the value of the collateral received and deposited at another FI (= 1,000) in the column "balances".
2. Report under the line "Other DRA" the market value of the DRA position (i.e. value of cash collateral received) in the column "balances" and again in the corresponding maturity bucket (week 3);
3. Report under the line "Cash collateral received for exchange-traded derivatives" the amount of cash collateral to be delivered in the "balances" column (= − 1,000), and again in the corresponding maturity bucket week 3 as an outflow.
4. Note that the P&L does not result in a reporting entry for NCCF purposes.

Example 8: Reporting DRA with cash collateral - Reporting example

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset - Demand Deposits at FIs | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Asset - Other DRA | 1,000 | -no data | -no data | 1,000 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Input: Liability - Cash collateral received for exchange-traded derivatives | (1,000) | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

#### Calculations

Example 8: DRA with cash collateral – Calculations

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Asset - Demand Deposits at FIs | 1,000 | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | -no data |
| Calculated Cash Flows: Asset - Other DRA | 1,000 | -no data | -no data | 1,000 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Calculated Cash Flows: Liability - Cash collateral received for exchange-traded derivatives | (1,000) | -no data | -no data | (1,000) | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Net Cumulative Cash Flows for the transaction | no data | 1,000 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |

### Example 9: DRA with security collateral – DRA position marked to market at $1,000 at the reporting date; maturing in week 3

For this transaction, we consider a profit of $1,000 requiring that the counterparty posts security collateral. The DRA position has a value of $1,000. Accordingly, for this transaction:

* Assets = 1,000 (DRA Asset)
* Liabilities = 0
* P&L = 1,000

The security collateral is an off-balance sheet item.

#### Reporting instructions

1. Report under the line "Other DRA" the market value of the DRA position in the column "balances" and again in the corresponding maturity bucket (i.e. week 3).
2. Report in the section "Pledging and Encumbrances - Derivative and Clearing (D/C)", under the line of the corresponding security, the market value in the column "balances" and again in the corresponding maturity bucket (i.e. week 3)

Example 9: DRA with security collateral - Reporting example

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset - Other DRA | 1,000 | -no data | -no data | 1,000 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Input: Pledging and Encumbrances - Derivative and Clearing (D/C) - State, Provincial & Agency Government Securities (High rated) | 1,000 | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

#### Calculated cash flows

Example 9: DRA with security collateral – Calculated cash flows

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Asset - Other DRA | 1,000 | -no data | -no data | 1,000 | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Calculated Cash Flows: Pledging and Encumbrances - Derivative and Clearing (D/C) - State, Provincial & Agency Government Securities (High rated) | 1,000 | 985 | no data | (985) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Net Cumulative Cash Flows for the transaction | no data | 985 | no data | 15 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 10: Short sale – Short sale for $1,000 cash; marked to market at $1,200 at reporting date

For this example, we consider a short sale for $1,000. Given the increase of the value of the security sold short, the reporting institution has posted the difference between $1,000 and the market value of the security, which corresponds to $200. At the reporting date, the reporting institution has a loss of $200. The remaining proceeds of the short sale has been deposited at another FI ($800):

* Assets = 1,000 (Demand deposit at FIs + Cash collateral pledged for short sales)
* Liabilities = 1,200 (Securities Sold Short)
* P&L = (200)

#### Reporting instructions

1. Report under the line "Demand Deposits at other FIs" in the column "balances" an amount of $800.
2. Report under the line "Cash collateral pledged for short sales" the amount of cash collateral posted following movements in the market value of the security sold short, $200 (=1,200 – 1,000)
3. Report under the corresponding line in the section "Securities Sold Short" the market value in the column "balances" (= – 1,200), and again in the corresponding maturity bucket

Example 10: Short sale - Reporting instructions

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset - Demand Deposits at FIs | 800 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Asset - Cash collateral pledged for short sales | 200 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Liabilities - Securities Sold Short - Sovereign & Central Bank Government Securities (High rated) | (1,200) | no data | no data | no data | no data | (1,200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

#### Calculated cash flows

Example 10: Short sale - Calculated cash flows

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Demand Deposits at FIs | 800 | 800 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Cash collateral pledged for short sales | 200 | 0 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Sovereign & Central Bank Government Securities (High rated) | (1,200) | (1,200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Net Cumulative Cash Flows for the transaction | no data | (400) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 11: Term repo – Term repo position maturing in 2 weeks

For this example, we consider a repurchase agreement where the underlying security is a "State, Provincial & Agency Government Securities (High rated)". The proceeds of the transaction are deposited by the reporting institution at another FI ($1,000). Given that the security needs to be repurchased in week 2, a cash outflow must be created:

#### Reporting instructions

1. Report under the line "Demand Deposits at other FIs" in the column "balances" an amount of $1,000.
2. Report under the line "Liabilities - Repo and Securities Lent (SL) - State, Provincial & Agency Government Securities (High rated)" the amount required to repurchase the security on week 2 ($1,000);
3. Report under the line "Collateral - Repo Collateral Out - State, Provincial & Agency Government Securities (High rated)" the value of the security on week 2 ($1,000);

Example 11: Term repo - Reporting instructions

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset - Demand Deposits at FIs | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Liabilities - Repo and Securities Lent (SL) - State, Provincial & Agency Government Securities (High rated) | (1,000) | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Collateral - Repo Collateral Out - State, Provincial & Agency Government Securities (High rated) | (1,000) | no data | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

#### Calculated cash flows

Example 11: Term repo - Calculated cash flows

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Asset - Demand Deposits at FIs | 1,000 | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Liabilities - Repo and Securities Lent (SL) - State, Provincial & Agency Government Securities (High rated) | (1,000) | 0 | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Collateral - Repo Collateral Out - State, Provincial & Agency Government Securities (High rated) | (1,000) | (985) | 985 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Net Cumulative Cash Flows for the transaction | no data | 15 | (15) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 12: Reverse term repo – Reverse term repo position maturing in 2 weeks

For this example, we consider a reverse repurchase agreement where the underlying security is a "State, Provincial & Agency Government Securities (High rated)". The security is to be repurchased by the counterparty in week 2:

#### Reporting instructions

1. Report under the line "Demand Deposits at other FIs" in the column "balances" a negative amount of $1,000.
2. Report under the line "Assets – Reverse Repo and Securities Borrowed (SB) - State, Provincial & Agency Government Securities (High rated)" the value of the security on week 2 ($1,000);
3. Report under the line "Collateral - Repo Collateral In - State, Provincial & Agency Government Securities (High rated)" the value of the security on week 2 ($1,000);

Example 12: Reverse term repo - Reporting instructions

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset[Example 12 table note \*](#ex12fn1) - Demand Deposits at FIs | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Asset – Reverse Repo and Securities Borrowed (SB) - State, Provincial & Agency Government Securities (High rated) | 1,000 | no data | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Collateral - Repo Collateral In - State, Provincial & Agency Government Securities (High rated) | 1,000 | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Example 12 table notes  Example 12 table note \*  While the template does not allow negative amounts for demand deposits, for this example, the negative amount shown above represents the change to demand deposits resulting from the transaction, assuming no other funding source.  [Return to example 12 table note \* referrer](#ex12fn1-rf) | | | | | | | | | | | | | | | | | |

#### Calculated cash flows

Example 12: Reverse term repo - Calculated cash flows

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Asset – Demand Deposits at FIs | (1,000) | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Asset – Reverse Repo and Securities Borrowed (SB) - State, Provincial & Agency Government Securities (High rated) | 1,000 | 0 | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Collateral - Repo Collateral In - State, Provincial & Agency Government Securities (High rated) | 1,000 | 985 | (985) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Net Cumulative Cash Flows for the transaction | no data | (15) | 15 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 13: FX Derivative

For reporting of the balance of FX derivatives at mark-to-market (MTM), it should only be reported in the balance column of one currency tab. The currency tab chosen for reporting the balance depends on which balance sheet the FX derivative was originally recorded in. If the MTM balance has already been reported in a currency balance sheet other than the USD tab, the balance should not be reported again the USD currency tab. For the reporting of cash flows related to the FX derivative, report all cash flows, regardless of currency, in the USD tab only.

For example, for a FX forward swapping EUR for $1,000 CAD on week 3, originally recorded in the Canadian balance sheet. Assuming as at the NCCF reporting date, the EUR pay leg is ($1,200) in Canadian Dollar Equivalent, and the CAD receive leg is $1,000, there is a mark-to-market loss of $200 for this position.

CAD balance sheet:

* Assets: 0
* Liability: 200 (DRL)
* P&L: −200

Report the following in the CAD balance sheet. Note that there are no resulting cash flows on the CAD balance sheet:

Example 13: FX Derivative - Balance sheet ($ CAD)

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Liability – Derivative Related Liabilities (DRL) - FX and Cross Currency Swap Liabilities | (200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

Report the following in the USD balance sheet:

Example 13: FX Derivative - Balance sheet ($ USD)

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Asset – Derivative Related Assets (DRA) - FX and Cross Currency Swap Assets | 0 | no data | no data | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Liability – Derivative Related Liabilities (DRL) - FX and Cross Currency Swap Liabilities | 0 | no data | no data | (1,200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

Use the memo item section "FX Derivatives" to include the details about the currencies:

Example 13: FX Derivative

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: FX and Cross Currency Swap Assets - CAD | 0 | no data | no data | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: FX and Cross Currency Swap Liabilities - CAD | (200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: FX and Cross Currency Swap Liabilities - EUR | 0 | no data | no data | (1,200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

Calculated cash flows (in the USD balance sheet):

Example 13: FX Derivative - Calculated cash flows ($ USD)

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Asset – Derivative Related Assets (DRA) - FX and Cross Currency Swap Assets | 0 | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Liability – Derivative Related Liabilities (DRL) - FX and Cross Currency Swap Liabilities | 0 | (1,200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Net Cumulative Cash Flows for the transaction | no data | (200) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 14: DRA adjustment for qualifying equity futures

3-month Delta one hedge equity future

In this example, the strategy considered is a delta one hedging using equity futures funded with unsecured funding (wholesale/commercial structured notes) due on month 3. As noted above, the liquidity value for the cash flows nets to 0; the full notional value of the position is realized at expiry of the future calculated as a combination of any calculated equity value and the DRA.

Eligible equities consist of 1,000 Non-FI Common Equity, 1,000 FI Common Equity, 1,000 Other Equities.

**Step 1:** Report Equities balances in column "balances" under corresponding lines

Example 14 – DRA adjustment for qualifying equity futures - Step 1

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Eligible Non-Financial Common Equity shares | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Eligible Financial Common Equity | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: Other Equities | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

**Step 2:** Report unsecured funding under corresponding lines: report balance in column "balances" and again in the corresponding maturity bucket

Example 14 – DRA adjustment for qualifying equity futures - Step 2

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Wholesale/Commercial Structured Notes | (3,000) | no data | no data | no data | no data | no data | (3,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

**Step 3:** Consider calculated cash flows from reported equities and unsecured funding from structured notes, and the corresponding total (calculated as the sum) of each maturity bucket

Example 14 – DRA adjustment for qualifying equity futures - Step 3

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Calculated Cash Flows: Eligible Non-Financial Common Equity shares | 1,000 | no data | no data | no data | 500 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | 500 |
| Calculation | no data | no data | no data | no data | =1000 \*50% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Eligible Financial Common Equity | 1,000 | no data | no data | no data | no data | 125 | 250 | 125 | no data | no data | no data | no data | no data | no data | no data | no data | 500 |
| Calculation | no data | no data | no data | no data | no data | =1000 \*12.5% | =1000 \*25% | =1000 \*12.5% | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Other Equities (no value attributed) | 1,000 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | 1,000 |
| Calculated Cash Flows: Wholesale/Commercial Structured Notes | (3,000) | -no data | -no data | -no data | -no data | -no data | (3,000) | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Calculation | no data | no data | no data | no data | no data | no data | =−3000 \*100% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Total of the transaction | -no data | no data | no data | no data | 50 | 125 | (2,750) | 125 | no data | no data | no data | no data | no data | no data | no data | no data | 2,000 |
| Calculation | =1000 +1000 +1000 −3000 | no data | no data | no data | =50 +0 +0 +0 | =0 +125 +0 +0 | =0 +250 +0 −3000 | =0 +125 +0 +0 | no data | no data | no data | no data | no data | no data | no data | no data | no data |

**Step 4:** Report in each maturity bucket of the line "Other DRA" the corresponding negative amounts of the line "Total of the transaction" (= -1 \* Amounts)

Example 14 – DRA adjustment for qualifying equity futures - Step 4

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Other DRA | -no data | no data | no data | no data | (50) | (125) | 2,750 | (125) | no data | no data | no data | no data | no data | no data | no data | no data | (2,000) |

### Example 15: Off-balance sheet items – Credit and liquidity facilities

1. Committed credit facilities to non-financial corporates without an operational relationship, $1,000 with earliest draw by the client available on week 1 and 1,000 available on week 4 (i.e. assumes that the notice is given by the client on week 1, which makes the funds available on week 4).

   Example 15 – Off-balance sheet items – Credit and liquidity facilities - Table A

   |  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Input: Committed credit facilities to non-financial corporates; of which: NIG; no operational relationship | (2,000) | (1,000) | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Calculated Cash Flows: Committed credit facilities to non-financial corporates; of which: NIG; no operational relationship | (2,000) | (150) | -no data | -no data | (150) | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | (835) |
   | Calculation | no data | =−1000 \*15% | no data | no data | =−1000 \*15% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
2. For the following example, we consider a committed liquidity facility backing ABCP. The current outstanding debt is 1,000 with 400 maturing in the first four weeks, 100 each week, and 600 maturing in month 2. Additionally, 1,000 of unutilized capacity is available, with 100 available with a 25 days notice and 900 with a 35 days notice.

   Example 15 – Off-balance sheet items – Credit and liquidity facilities - Table B

   |  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Input: Committed liquidity facilities to ABCPs - Maturing Balance | (1,000) | (100) | (100) | (100) | (100) | (600) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Calculated Cash Flows: Committed liquidity facilities to ABCPs - Maturing Balance | (1,000) | (100) | (100) | (100) | (100) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Calculation | no data | =−100 \*100% | =−100 \*100% | =−100 \*100% | =−100 \*100% | =−600 \*0 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Input: Committed liquidity facilities to Unissued ABCPs (reported recognizing notice periods) | (1,000) | no data | no data | no data | (100) | (900) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Calculated Cash Flows: Committed liquidity facilities to Unissued ABCPs (reported recognizing notice periods) | (1,000) | -no data | -no data | -no data | (100) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
   | Calculation | no data | no data | no data | no data | =−100 \*100% | =−900 \*0 | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 16: Wholesale deposits

For this example, we consider a deposit from a financial institution, totaling 1,100, of which 1,000 requires an advance notice of 35 days and 100 that is available on demand:

Example 16 – Wholesale deposits

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Wholesale Notice (All other counterparties, including other FIs and other legal entities) | (1,000) | no data | no data | no data | no data | (1,000) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: Wholesale Notice (All other counterparties, including other FIs and other legal entities) | (1,000) | -no data | -no data | -no data | -no data | (1,000) | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data | -no data |
| Calculation | no data | no data | no data | no data | no data | =−1000 \*100% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Input: CommCorp and Wholesale Non-Operational, Insured (FI) | (100) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |
| Calculated Cash Flows: CommCorp and Wholesale Non-Operational, Insured (FI) | (100) | (25) | (25) | (25) | (25) | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | -no data |
| Calculation | no data | = −100 \*25% | = −100 \*25% | = −100 \*25% | = −100 \*25% | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data | no data |

### Example 17: Business and government loans

For this example, we consider business and government loans, both with fixed maturities and open maturities. The balance of loans with fixed maturities for open maturities is 1,000 each. Payments and balances at maturities are reported in the corresponding maturity buckets when they are due:

Example 17 – Business and government loans

|  | Balances | Week 1 | Week 2 | Week 3 | Week 4 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 7 | Month 8 | Month 9 | Month 10 | Month 11 | Month 12 | >365 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input: Bus and Gov Loans - Fixed Maturity | 1,000 | 20 | 20 | 20 | 20 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 370 |
| Calculated Cash Flows: Bus and Gov Loans - Fixed Maturity | 1,000 | 10 | 10 | 10 | 10 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 685 |
| Calculation | no data | =20 \*50% | =20 \*50% | =20 \*50% | =20 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | no data |
| Input: Bus and Gov Loans - Open maturity (with minimum payment) | 1,000 | 10 | 10 | 10 | 10 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 50 | 410 |
| Calculated Cash Flows: Bus and Gov Loans - Open maturity (with minimum payment) | 1,000 | 5 | 5 | 5 | 5 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 25 | 705 |
| Calculation | no data | =10 \*50% | =10 \*50% | =10 \*50% | =10 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | =50 \*50% | no data |

## Footnotes

Footnote 1
:   Declining balance basis should be understood as run-off rates being applied to the resulting balance that has not been run-off in the previous corresponding time bucket.

    [Return to footnote 1 referrer](#fn1-rf)

Report a problem or mistake on this page

Date modified:
:   2026-04-16