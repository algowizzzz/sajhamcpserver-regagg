# Clarifications about the non-retail data call

Information

Type of document

Instructions

Industry

Deposit-taking institutions

Table of contents

Related documents

* [Phase 3 non-retail transactional level data call (OSFI 965)](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/phase-3-non-retail-transactional-level-data-call-osfi-965)
* [Phase 3 988 non-retail transactional level data call](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/phase-3-988-non-retail-transactional-level-data-call)

Before submitting your response to our non-retail data call, please review the following clarifications.

## Resubmitting files

If you need to resubmit a filing to correct an issue with 1 or more tables, please resubmit all 4 tables (that is, Borrower, Facility, Collateral, Project).

## Exclusion from this data call

### RESL Loan Level Data Call

If you’ve reported a property under the real estate secured lending (RESL) Loan Level data call, do **not** report it in the non-retail data call.

### Off-balance sheet loans

Off-balance sheet loans such as secured by Canada Mortgage and Housing Corporation as part of a securitization or loans authorized but not yet funded are out of scope for the non-retail data call.

### Overdrafts

If the overdraft is not a separate facility, please do **not** include it in the non-retail data call.

## Reporting considerations

### Null values

Null values (that is, instances of no data in a field for a given record) should contain no characters or spaces of any kind. For example, do not provide “N/A”, “NULL”, “ “, “-“, and so on. The bracketing delimiters (pipes) of the data point within the file (“||”) for a null value should be next to each other with nothing between them.

### Level of detail

Report each facility at the most granular level available. That is, the level at which interest rates, facility terms, maturity dates, and so on, are defined.

## Field-specific clarifications

120 Borrower Loan-to-Value (LTV) (borrower\_crnt\_ltv)
:   For **total current market value**, use the most current valuation (could be an internal valuation). This is in accordance with our [Revised regulatory notice on Commercial Real Estate Lending](/en/guidance/guidance-library/commercial-real-estate-risk-management "Revised Regulatory Notice on Commercial Real Estate Lending").

    Only provide **borrower level LTV** when your institution calculates it. Leave this field blank if it’s not available.

220 Contractual Amortization (Current) (facility\_contractual\_amortization)
:   If a facility has no amortization (for example, an “interest only” payment loan which has only term but no amortization), you should report the **contractual amortization** field as **null** rather than 0.

221 Monthly Payment (facility\_monthly\_payment)
:   Voluntary/unscheduled payments such as prepayments are not included in the **monthly payment** field. Provide contractual payments only.

224 Capitalized Interest Flag (facility\_capitalized\_interest)
:   The **capitalized interest flag** should only reflect the interest that was capitalized during the reporting period and remains capitalized at time of reporting date cut off.

227 Syndicate/Participant Role (facility\_syndicate\_participant\_role)
:   Definitions of participation and syndication:

    * **Participation**: the participating lender is not a direct creditor of the borrower
      + It’s generally structured as a legal agreement directly between the originator and participating lender
    * **Syndication**: each lender is a direct creditor of the borrower

304 Collateral Appraisal Value (collateral\_appraisal\_value)
:   Prorate this field for both syndication and participation loans.

306 Estimated Collateral Value (collateral\_estimated\_value)
:   Prorate this field for both syndication and participation loans.

316 Primary Collateral Indicator (collateral\_primary\_ind) (for FULL version template OSFI988)
:   If there is only **1** collateral (not multiple) we expect this to be the primary collateral, enter “1”.

    When you have several collaterals on the loan, designate whichever collateral is considered primary in your internal systems and other regulatory reporting as primary.

    Note that OSFI will conduct reconciliations of the data from this data call to other reporting where breakdown by property type is provided, such as OSFI980 and E2.

414 Committed Amount (project\_committed\_amt)
:   Enter the maximum amount that the lender is contractually obligated to fund/advance when the terms and conditions of the agreement have been finalized and met. The financing is not on a demand basis.

    In a situation where there are 2 or more facilities, with multiple different syndication percentages, corresponding to the same single project, the project **committed amount** should reflect contractual obligation, prorated based on syndication percentages for each facility.

    If no amount was committed for the project, report zero (“0”).

    Prorate this field for both syndication and participation loans.

Report a problem or mistake on this page

Date modified:
:   2024-12-04