# Key validation rules for the H4 regulatory return

Information

Type of document

Validation rules

Industry

Deposit-taking institutions

Return

Collateral and Pledging Report (H4)

Last updated

2017

Return number

H4

Accompanying documents

* [Collateral and Pledging Report (H4)](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/collateral-pledging-report-h4)

## Context

Below is a listing of the key data validation rules of the H4 regulatory return for the purpose of a quick reference. A full list of all H4 data validation rules including simple add-up rules will be made available in the Regulatory Reporting System (RRS). For inquiries please contact James Younker ([jyounker@bankofcanada.ca](mailto:jyounker@bankofcanada.ca)).

## Key Intra-Return Rules

### Rules for Encumbered and Unencumbered Assets

Available Unencumbered Assets = Cash (unencumbered)
:   + Securities  
    + Loans  
    + Collateral In (rehypothecateable)  
    – Collateral out  
    + Adjustments

Encumbered Assets = Cash (encumbered)
:   + Cash Margin Given  
    + Collateral In (non-rehypothecateable)  
    + Collateral out  
    + Adjustments

### Rules for Collateral Movements Section to Reconcile with Part B

Part A: OTC Derivative Collateral Out = Part B: CMB Program - Sellers Swap -> Collateral Pledged + Sum of OTC Derivative -> Collateral Pledged (includes FIs only)

Part A: Pledged FMI/CCP = Part B: LVTS -> Collateral Pledged + Sum of FMIs -> All Transactions -> Collateral Pledged (includes FMIs only)

Part A: Collateral Swapped Out = Part B: Sum of Collateral Swaps -> Collateral Pledged (includes CBs and FIs)

Part A: Repo (Gross) Collateral = Part B: Sum of Repo -> Collateral Pledged (includes CBs and FIs) + CMHC/CHT On Balance Sheet Repos [Note repo collateral pledged to a CCP is recorded under 'Pledged FMI/CCP']

Part A: Security Lending (Gross) Collateral = Part B: Sum of Security Lending -> Collateral Pledged (includes CBs and FIs)

Part A: Other Collateral Out = Part B: Sum of Other -> Collateral Pledged (includes CBs and FIs)

Part A: Collateral Swapped IN = Part B: Sum of Collateral Swaps -> Collateral Received (includes CBs and FIs)

### Rules for Balance Sheet Section to Reconcile with Part B

Part A: Balance Sheet Repo (Gross) (Total) = Part B: Sum of Repo -> Cash Received (includes FMIs, CBs, and FIs)

Part A: Balance Sheet Security Lending (Gross) (Total) = Part B: Sum of Security Lending-> Cash Received (incl. FMIs, CBs, FIs)

Part A: Cash Margin Given OTC Derivative = Part B: Sum of OTC Derivative collateral pledged (cash cells only) (incl. FIs only)

Part A: Cash Margin Given FMI/CCP = Part B: Sum of FMI collateral pledged (cash cells only) (includes FMIs only)

Part A: Cash Margin Given other = Part B: Sum of other collateral pledged (cash cells only) (includes CBs and FIs)

## Key Cross Return Rules

### Rules to Reconcile with M4 Balance Sheet (accurate within 2% threshold)

Part A: Securities Long (adjustments: non-reported sub and other) = M4 Securities

Part A: Secured Lending (adjustments: netting, non-reported subs and other) = M4 Reverse Repos

Part A: Loans (adjustments: non-reported subs and other) = M4 Loans less Reverse Repos

Part A: Secured Funding (adjustments: netting, non-reported subs and other) = M4 Repos

Part A: Securities Short (adjustments: non-reported sub and other) = M4 Obligations related to borrowed securities

### Rules to Reconcile with LCR (accurate within 2% threshold)

Part A: Level 1 Available Unencumbered Assets = LCR market value of Level 1 assets

Part A: Level 2A Available Unencumbered Assets = LCR market value of Level 2A assets

Part A: Level 2B Available Unencumbered Assets = LCR market value of Level 2B assets

Report a problem or mistake on this page

Date modified:
:   2023-11-17