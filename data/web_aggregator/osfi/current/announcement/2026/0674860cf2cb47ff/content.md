# Instructions – Life Appointed Actuary’s Report (AAR) Supplementary Tables

Information

Type of document

Instructions

Industry

Insurance companies

Return

Memorandum to the Appointed Actuary

Last updated

June 9, 2025

Table of contents

Related documents

* [2025 Appointed Actuary’s Report Supplementary Tables for Life, Property and Casualty and Mortgage Insurers - Letter](/en/2025-appointed-actuarys-report-supplementary-tables-life-property-casualty-mortgage-insurers)
* [2024 Memorandum to the Appointed Actuary - Supplementary tables](/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/2024-memorandum-appointed-actuary-supplementary-tables)

## Return file

[OSFI605-OSFI1008 – 2025 Supplementary tables – Appointed Actuary’s Report (Life) (XLSX, 984 KB)](/sites/default/files/documents/OSFI1008-BSIF1008-2025-memo-life-supplementary-tables-supplementaire-vie-en.xlsx "OSFI1008-BSIF1008-2025-memo-life-supplementary-tables-supplementaire-vie-en.xlsx")

Each Life insurer must submit a workbook containing supplemental data (Supplementary Tables) in addition to the Appointed Actuary’s Report (AAR). The Supplementary Tables must contain specific data elements presented in specific formats. This workbook is a template for the Supplementary Tables.

This workbook includes:

* List of Supplementary Tables
* Data dictionary
* Comment
* Supplementary tables
* Drop down lists
* Validation rules

## General Instructions

Prepare the Supplementary Tables in accordance with the general instructions provided in this section. Instructions and guidance specific to the individual workbook tabs are provided in the following sections:

### Filing

The Supplementary Tables (this workbook) should be submitted as a structured return in the Regulatory Reporting System (RRS) no later than 60 days after the end of the insurer’s fiscal year.

### Basis

Information entered in this workbook should be

* determined as of the insurer’s fiscal year-end unless instructed otherwise
* prepared on a consolidated basis
* expressed in thousands of Canadian dollars unless instructed otherwise
* determined for insurance contract liabilities measured under IFRS 17 except for table 25010
* entered as positive numbers if they are liabilities and negative numbers if they are assets

Insurance contract liabilities are the sum of LRC and LIC.

An insurer should provide additional information to add understanding of the input in the ‘Comment’ tab.

### Workbook modifications

The workbook should not be modified in any way including

* adding or deleting columns
* renaming, adding, or deleting tabs
* changing the format of cells

Tables 00001, 00011 to 00015, 21021, 41310, 51010 and 86010 should not be modified in any way other than the entry of values. These tables have a fixed structure. Other tables will have a variable structure depending on how many of sets of entries the insurer has. In these cases, the first set of entries is an example to show what is expected and should be replaced by actual entries.

### Granularity

Insurers should allocate values where they are requested at a more granular level than the level of aggregation at which the insurer has determined the amount. Where the insurer has allocated an amount, describe the allocation approach in the ‘Comment’ tab.

If a portfolio contains more than one product type, insurers should include one row per product type in the tables that request product type information.

### Data entry

* Blue cells are for manual entry.
* Green cells indicate that drop down lists should be used.
* White cells have fixed text.

Please note that all colored cells are made accessible in the Excel spreadsheet through tooltips and locked cells.

Refer to the ‘data dictionary’ tab for further description of what is expected in each column in a table including drop down list, column type and data type.

Cells should not be left “blank” unless there is no input for the cell. “0” should be entered if the amount is zero.

Where cells contain a drop down list, insurers should enter one of the values provided in the drop down list.

### Machine readable data entry

This workbook has been updated to support ingestion of the data into OSFI’s databases. Data entry in this workbook follows certain general principles.

Each tab in the workbook collects data on a certain topic (for example, tab 00011 collects the names of insurer entities). Refer to the tab ‘List of Supplementary Tables’ for a complete overview of the tables.

The numeric codes assigned in tabs 00011-00015 define codes for entities, portfolios, liquidity categories, asset segments, and participating sub-accounts that are used throughout the Supplementary Tables. For example, if the entity name “Branch 1” is assigned the code “Entity (Subsidiary/Branch)#1” in tab 00011, all data related to “Branch 1” in other tables must be entered using the code “Entity (Subsidiary/Branch)#1” not the name “Branch 1”. Users must ensure that they consistently use the numeric codes throughout the workbook for proper data mapping and accuracy.

Within each tab, each distinct data value (referenced as value) is entered in a separate row (for example, each entity name is entered in a separate row in tab 00011).

Each value may be described by a value\_category and one or more descriptors depending on the tab and the nature of the data collected.

In some tabs, values are described by descriptors in addition to the value\_category. For example, in tab 21020, insurers provide insurance contract liabilities (value) broken down into the present value of future cash flows (excl. cost of guarantees), cost of guarantees, risk adjustment, and contractual service margin (value\_category). These values are further broken down by

* Country
* Entity
* Par indicator
* Portfolio
* Contract type
* Product type

The entry for each of these additional descriptors must be chosen from a set of allowable entries from the corresponding drop down list.

Please see the data dictionary, drop down lists, and validation rules for additional information on permitted values and limitations on the values that may be entered.

When “other” is selected from the drop down lists (for examples, product type, assumption and methodology changes, reinsurance product type or type of reinsurance) in certain tabs, the column immediate to the right provides space to elaborate on what “other” refers to.

### Data quality

Insurers should conduct a quality check of the Supplementary Tables prior to submission. In particular, insurers should ensure:

* values are selected exclusively from the options provided in drop down lists in all green cells
* values are expressed in thousands for dollar amounts or percentages as instructed
* information is consistent throughout the workbook
* values are consistent with the validation rules presented in the ‘Validation Rules’ tab

We may ask insurers to refile Supplementary Tables to correct errors including the failure to follow these instructions.

#### Table 21021 Confidence Level of Risk Adjustment for Non-Financial Risk

If an insurer only determines confidence level at the entity level, then the same confidence level should be reported at the Canadian level.

#### Table 22010 Risk Adjustment for Non-Financial Risk by Risk Type where Margin Approach is Used and Table 22020 Risk Adjustment for Non-Financial Risk Where Other[Footnote 1](#fn1) Approaches Are Used

If diversification benefits are not explicitly determined and cannot be allocated at the requested level of granularity, provide detail on that inability in the ‘Comment’ tab.

#### Table 23010, 23020 Assumption and Methodology Changes and Table 23030 Changes Related to Market Impact

Impacts arising from assumption changes, methodology changes and other sources should be included.

Report each change separately. Do not offset material changes against each other.

#### Table 32010 Discount Rates Used to Discount Cash Flows That Do Not Vary Based on the Returns on Underlying Items as at the End of Current Fiscal Year

Report discount rates for each distinct liquidity category that the insurer has identified. Liquidity categories should be coded in order of decreasing illiquidity with the most illiquid category being labelled 1. For example, an insurer with two liquidity categories would label the more illiquid category as 1 and the more liquid category as 2.

Provide a description of any characteristics other than country, currency, and liquidity category that distinguishes the insurer’s discount rates in the ‘Comment’ tab.

#### Table 32020 Risk Free Rates by Year

Risk free rates may be omitted for currencies where the insurer uses a top down approach and does not reference risk free rates in the development of its discount rates. Provide an explanation of the omission in the ‘Comment’ tab.

Express risk free rates as spot rates or forward rates consistent with the form for the corresponding discount rates in Table 32010. If the insurer expresses discount rates in both forms and the associated spot and forward risk free rates are not equivalent, provide risk free rates in both forms.

#### Table 41310 Risk Adjustment – Cost of Capital Approach

Leave the table blank if the insurer does not use the cost of capital approach to determine risk adjustment.

The average capital should be aggregated across all insurance contracts included in the cost of capital risk adjustment calculation.

#### Table 42110 Product data

Provide face amounts for life insurance contracts. Face amount for all other insurance contracts should be “blank”.

Provide account values for all insurance contracts that report an account value to the policyholder including universal life, segregated funds, and annuity contracts. The account values for all other insurance contracts should be “blank”.

Combine information from all cohorts arising from a calendar year if the insurer establishes cohorts for shorter periods than a year. For example, when using quarterly cohorts, the entity should report the sum of the four quarters’ numbers in the table.

If a product type is immaterial and the insurer wishes to omit it, contact [AARinquirylife-RADinfoVie@osfi-bsif.gc.ca](mailto:AARinquirylife-RADinfoVie@osfi-bsif.gc.ca) for further discussion of the specific circumstances.

#### Table 42120 Insurance Revenue by Portfolio

Total insurance revenue should reconcile with the value in LF1 (schedule 20022, row 099, column 01). Provide an explanation in the ‘Comment’ tab if these amounts do not reconcile.

#### Table 51010 Discount Rate Sensitivities

Provide the impact on liabilities of replacing the insurer’s discount rates with the following:

* discount rates 50 basis points lower than the insurer’s discount rates at all durations
* discount rates 50 basis points higher than the insurer’s discount rates at all durations
* discount rates equal to the CIA curve for the first 30 years and the 30-year rate for later years
* the CIA reference curves (Canadian business only)
* discount rates constructed using the CIA reference curve parameters in the unobservable period instead of the insurers parameters (Canadian business only)

Shock each scenario by 50 basis points (for the up and down sensitivities) where the business is valued stochastically.

The above shocks are defined on a spot rate basis. If the insurer expresses its discount rates as forward rates the shocks should be adjusted to represent the forward rate equivalent.

The CIA Curves can be found at [Fiera Capital’s CIA Method Accounting Discount Rate Curve](https://www.fieracapital.com/en/institutional-markets/cia-accounting-curve#goto-curves).

The Canadian Institute of Actuaries’ Educational Note IFRS 17 Discount Rates for Life and Health Insurance Contracts describes the reference curve parameters (chapter 2 section 2 Defining the Reference Curves). Please visit the CIA website to access the most up-to-date version.

Contracts in which substantially all cash flows vary with an underlying item (for example, participating life insurance), should be classified as cash flows that do vary with returns on underlying items. Contracts in which substantially all cash flows do not vary with an underlying item (for example, payout annuities and term life insurance) should be classified as cash flows that do not vary with returns on underlying items. Other contracts (for example, universal life) should be classified as other.

#### Table 54010 Assets/Liabilities for Reinsurance Contracts Held – Top 10 Reinsurance Companies

Reinsurer group size is based on the aggregate asset held in relation to insurance ceded to that reinsurer group.

Reinsurance contracts held assets should be a negative amount, and reinsurance contract held liabilities should be a positive amount.

#### Table 61010 Asset Segment – Assets (Balance Sheet Values at Fiscal Year End)

Enter the balance sheet value of assets for each asset segment broken down by asset class and accounting basis as required by the table. Balance sheet values should be consistent with the information reported in LF1.

Do not provide information on asset segments that do not support liabilities (that is, surplus segments).

Describe the composition of material amounts of other assets, if selected, in the ‘Comment’ tab.

#### Table 62010 Asset Yield or Expected Returns by Asset Type

Enter actual yields on fixed income assets for the most recent fiscal year. Enter actual returns or expected returns (if actual returns are not possible) by source (income or growth) and in total for non-fixed income assets. Indicate whether non-fixed income returns are actual or expected in the ‘Comment’ tab.

#### Table 71110 Payments to Shareholders from Participating Account in Accordance with Insurance Company Act Section 461

Table reference notes:

\*Some companies include the Section 462(a) transfer in Net Income while other companies show them as a transfer from par account surplus.

\*\*Disclose in detail the cause of any such other transfers.

\*\*\*The surplus of the total par account must be reconciled to the amount in the Annual Returns LIFE Quarterly Return Page 20.040 Line 199 for the Canadian Life Insurance Companies.

\*\*\*\*The residual interest of the total par account must be reconciled to the amount in the Annual Returns LIFE Quarterly Return Page 20.040 Line 599 for the Canadian Life Insurance Companies.

#### Table 86010 Peer Review of the Work of the Appointed Actuary

If there is no capital peer review in the current fiscal year, please leave the entries “blank” in the ‘value’ column related to capital.

## Footnotes

Footnote 1
:   other than margin approach

    [Return to footnote 1  referrer](#fn1-rf)

Report a problem or mistake on this page

Date modified:
:   2025-06-09