---
title: "Supervisory reporting - DPM and XBRL - European Insurance and Occupational Pensions Authority"
regulator: "eiopa"
doc_type: "announcement"
status: "final"
source_kind: "web"
source_url: "https://www.eiopa.europa.eu/tools-and-data/supervisory-reporting-dpm-and-xbrl_en"
version: "1"
---
Data reporting

DPM methodology and XBRL are the standard for reporting data submission between EIOPA and national competent authorities.

EIOPA implemented the DPM methodology and the XBRL as the standard for reporting data submission between EIOPA and national competent authorities following a [decision of the Board of Supervisors on Collection of Information by EIOPA](/document/download/96218705-55c7-44c9-92b8-4e86c806a5b3_en?filename=Decision%20of%20the%20Board%20of%20Supervisors%20on%20collection%20of%20information%20by%20EIOPA.pdf) and a [decision of the Board of Supervisors on the reporting of the pan-European Personal Pension Product key information document](/document/download/47809dc2-fd20-4748-8621-41b680fd6092_en?filename=Decision%20of%20the%20Board%20of%20Supervisors%20on%20the%20reporting%20of%20the%20pan-European%20Personal%20Pension%20Product%20key%20information%20document.pdf).

*Please subscribe to this*[*RSS feed*](https://dev.eiopa.europa.eu/RSS/S2_XBRL_RSS.xml)*to receive updates when the content of this page is updated.*

**For the current DPM and taxonomy packages please see this page below.**

**For additional information on supervisory reporting requirements and EIOPA's DPM and taxonomy please refer to the dedicated web page on** [**Supervisory reporting**](https://www.eiopa.europa.eu/tools-and-data/supervisory-reporting_en)**.**

![Adobestock_data_model](https://www.eiopa.europa.eu/sites/default/files/styles/oe_theme_medium_no_crop/public/2020-02/adobestock_data_model_0.jpeg?itok=ElQZwD4M)

## Information on the releases in production

**Important change:** **EIOPA announces that it will discontinue the support for “xBRL canonical files” with the NACE 2.1 optional hotfix releases and for all future releases, except for validation deactivation files.** In the context of xBRL taxonomies, canonical files refer to the individual XML and XSD files that make up the taxonomy, which are accessed directly from their official web addresses (URIs) on EIOPA’s servers, for example when xBRL tools access [this file](https://www.eiopa.europa.eu/eu/xbrl/s2md/fws/solvency/solvency2/2024-10-15/mod/aes-find-check.xml) directly. This method requires downloading several thousand files one by one over the internet each time the taxonomy is used. EIOPA has identified that this approach is almost never used, as nearly all users download the full taxonomy as a single xBRL taxonomy zip package from the EIOPA webpage and process it locally, which is faster and more reliable. Validation deactivation files will continue to be provided as before at dev.eiopa.europa.eu, as for example [this file](https://dev.eiopa.europa.eu/Taxonomy/Full/deactivations/282/aeb-ignore-val.xml), and as explained in Section VII.3.6.8 of the Taxonomy Documentation.

Therefore, the **few remaining users are requested to stop using xBRL taxonomy canonical files by 31 December 2025** and instead use the taxonomies in zip format as published on this EIOPA webpage.

**NACE 2.1 implementation**

For **Q1/Q2/Q3 2025 reporting reference periods** undertakings must continue to report according to the NACE 2.0 classification for all reporting frameworks (SII, IORPs, PEPP Prudential, FICOD). If not available by the data provider, the NACE 2.1 codes must be mapped to the 2.0 codes as it is not possible to report the NACE 2.1 codes under the current taxonomy releases.

Please see Q&A [2931 - NACE 2.1 - EIOPA](https://www.eiopa.europa.eu/qa-regulation/questions-and-answers-database/2931-nace-21_en)

**Relevant templates**:

|  |  |
| --- | --- |
| **Solvency II** | S.06.02.01.02 C0230; S.06.02.04.02 C0230; S.06.02.07.02 C0230; SE.06.02.16.02 C0230; SE.06.02.18.02 C0230; S.11.01.01.02 C0190; S.11.01.04.02 C0190; S.37.01.04.01 C0100; S.37.02.04.02 C0050 |
| **FICOD** | FC.06.01.36.01 FC0060; FC.07.01.36.02 FC0040 |
| **Pension Funds** | PF.06.02.24.02 C0170; PF.06.02.25.02 C0170; PF.06.02.26.02 C0170; PFE.06.02.30.02 C0170; PFE.06.02.31.02 C0170 |
| **PEPP PR** | PP.06.02.33.02 C0170 |

As **from Q4/Annual 2025** reporting reference periods, EIOPA published an “optional” hotfix for all the reporting frameworks (SII, IORPs, PEPP Prudential, FICOD) to allow reporting NACE 2.1 codes as well (besides the NACE 2.0 codes).

Technically, this hotfix maintains the same schemas and entry points as the current system (i.e. it is not a corrective release). It introduces new columns, metrics, and categories/hierarchies specifically for NACE 2.1 codes, with these enhancements added as new items in the xBRL dictionaries.

The update is instance backwards compatible, allowing entities that continue to use only NACE 2.0 to remain with the previous taxonomy release. Therefore, only those undertakings and pension funds that need to report using NACE 2.1 codes from the Q4/Annual 2025 reporting periods are required to implement this hotfix.

**2.8.2 (Solvency II minor release)**

EIOPA has been continuously monitoring the submissions under the 2.8.0 Solvency II taxonomy and the relevant issues and decided that the high number of issues that require additional workaround must be corrected. As the corrections are extended compared to a usual hotfix and the version is already in use, EIOPA decided to release it as 2.8.2 minor release, also due to IT implementation reasons.

2.8.2 has been published on 15 October 2024 and it is applicable from the Q42024 / annual 2024 reference periods until Q4/Annual 2026 included. (2.10.0 release will be applicable from Q1/2027 reporting reference period).

**2.9.0 (Pension Funds)**

The Pension Funds 2.9.0 taxonomy is applicable from Q1/2025 reporting reference period and applies only to Pension Funds (IORPs). 2.9.0 Hotfix was published on 16 July 2024.

**2.7.0 and 2.7.1 (PEPP and Pension Funds)**

The 2.7.0 release was the one to be used from the reference period Q4-2022 and includes the PEPP Prudential (PEPP PR) integration for Solvency II and Pension Funds frameworks, as well as PEPP PR standalone reporting. The release 2.7.1 includes only the reflection of Croatia entering the Euro-Zone. PEPP standalone reporting remains to use 2.7.0 release until new taxonomy is announced. Pension Funds (IORPs) 2.7.1 was applicable until Q4/2024 included (2.9.0 is from Q1/2025).

**2.8.1 (FICOD)**

Regarding the 2.8.1 release for FICOD (Financial Conglomerates), it is a standalone (not integrated) cross-sectoral version to be used for reporting of insurance led conglomerates until a new release is announced. The final version was published on 31 July 2023 and the Hotfix on 6 November 2023. The application date was 31 December 2023 with first reporting in 2024.

### XBRL Taxonomy Releases

For planning purposes, please refer to the [Governance of reporting taxonomy releases and reporting data management](https://www.eiopa.europa.eu/document/download/3876b480-0cb5-4132-b6b1-c460e7ea0f5c_en?filename=EIOPA-BoS-24-411_Governance%20of%20taxonomy%20releases_public.pdf) document.

![EIOPA Taxonomy Releases (updated on 26/06/2026)](/sites/default/files/2026-06/EIOPA_Taxonomy_Roadmap.png)

## Applicable taxonomy versions and reporting deadlines

*(last updated on 15 July 2026)*

The [EIOPA Taxonomy Roadmap](https://www.eiopa.europa.eu/document/download/1f49b6ff-0f27-4ce2-b6f1-89dc1fd61c20_en?filename=Eiopa_taxonomy_roadmap.xlsx) includes the reporting deadlines and the applicable taxonomy versions per reporting frameworks.

## The List of Known Issues (updated on 03/06/2026)

[The list](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_List_of_Known_Issues_Published.xlsx) describes issues and provides solutions to be taken into account during the technical implementation. It mainly includes corrections in relation to the DPM and XBRL taxonomies.

## XBRL Filing Rules

The [XBRL Filing Rules](//dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf) are common across all the reporting frameworks. They contain a modification history table with the validity start date of the change.

## Custom Margin validations for testing

EIOPA is publishing a [set of sample validations](/document/download/423c191c-9df5-47a8-8a96-21af9b495416_en?filename=val%20cmf.zip) using custom margin functions. These validations have been selected to demonstrate technical solutions. The exact assumptions regarding the tolerance level of the validation data will be analysed on a check-by-check basis and, as such, may differ from the examples presented.

## The IRRD Data Point Model and XBRL Taxonomy

IRRD Data Point Model and Taxonomy 2.11.0 (published on 27/07/2026) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [IRRD Release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_Release_Notes_2.11.0.pdf)

**DPM:**

The [*DPM Dictionary*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_DPM_Dictionary_2.11.0.xlsx) and [IRRD Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_DPM_Annotated_Templates_2.11.0.xlsx)

The [IRRD Annotated Templates template grouping](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_DPM_Annotated_Templates_2.11.0_table_group_arrangement.xlsx)

The [Change log between the 2.11.0 and 2.9.1 PWD 1](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/Change_log_between_EIOPA_IRRD_2.11.0_vs_2.9.1_PWD1.xlsx)

The [Change log between the 2.11.0 and 2.11.0 PWD 2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/Change_log_between_EIOPA_IRRD_2.11.0_vs_2.11.0_PWD2.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_DPM_Documentation.pdf)

**Validations:**

The [IRRD List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_Validations_2.11.0.xlsx)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_Validation_Syntax.pdf)

**Taxonomy:**

The [IRRD XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_XBRL_Taxonomy_2.11.0.zip), [IRRD XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_XBRL_Taxonomy_2.11.0_with_external_files.zip), [IRRD XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_XBRL_Instance_documents_2.11.0.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_XBRL_Taxonomy_Documentation.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [IRRD DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/irrd/EIOPA_IRRD_DPM_Database_2.11.0.zip)

The [*DPM database documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.11.0/Common/EIOPA_DPM_Database_Documentation.pdf)

Instructions:

The [Final report](https://www.eiopa.europa.eu/publications/final-report-implementing-technical-standards-regarding-resolution-reporting-irrd_en)

Please be informed that artefacts in *italics* are common between multiple frameworks.

## The Solvency II Data Point Models and XBRL Taxonomies

Insurance Data Point Model and Taxonomy 2.10.0 (published on 03/07/2026) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Solvency 2 Release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_SolvencyII_Release_Notes_2.10.0.pdf)

**DPM:**

The [*DPM Dictionary*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_DPM_Dictionary_2.10.0.xlsx) and [Solvency 2 Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.10.0.xlsx)

The [Solvency 2 Annotated Templates template grouping](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.10.0_table_group_arrangement.xlsx) and [Solvency 2 Annotated Templates legacy format](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.10.0_legacy_format.xlsx)

The [Change log between the 2.10.0 and 2.8.2 Hotfix](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/Change_log_between_EIOPA_SolvencyII_2.10.0_vs_2.8.2_Hotfix.xlsx)

The [Change log between the 2.10.0 and the 2.10.0 PWD 2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/Change_log_between_EIOPA_SolvencyII_2.10.0_vs_2.10.0_PWD2.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_DPM_Documentation.pdf)

**Validations:**

The [Solvency II List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_SolvencyII_Validations_2.10.0.xlsx)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_Validation_Syntax.pdf)

**Taxonomy:**

The [Solvency 2 XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.10.0.zip), [Solvency 2 XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.10.0_with_external_files.zip), [Solvency 2 XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_SolvencyII_XBRL_Instance_documents_2.10.0.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_XBRL_Taxonomy_Documentation.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Solvency II DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/EIOPA_Solvency_II_DPM_Database_2.10.0.zip)

The [DPM database documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/Common/EIOPA_DPM_Database_Documentation.pdf)

**Instructions:**

The [Final report](https://www.eiopa.europa.eu/publications/final-report-supervisory-reporting-and-public-disclosure-requirements-under-solvency-ii_en)

Technical instructions providing information on S.30.01 and S.30.02 reporting:

The [Technical instructions for S.30.01 and S.30.02](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/S.30.01%20and%20S.30.02%20technical%20instructions.pdf)

Technical instructions providing information on PEPP integrated reporting:

The [Technical instructions for EIOPA Solvency II reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.10.0/S2/Technical_instructions_solo_PEPP_integrated_reporting.zip)

Please be informed that artefacts in *italics* are common between multiple frameworks.

Insurance Data Point Model and Taxonomy 2.8.2 - Optional NACE 2.1 Hotfix (published on 30/06/2025, List of Validations updated on 03/06/2026) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Solvency 2 Release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_Release_Notes_2.8.2_Hotfix.pdf)

**DPM:**

The [*DPM Dictionary*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/Common/EIOPA_DPM_Dictionary_2.8.2_Hotfix.xlsx) and [Solvency 2 Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2_Hotfix.xlsx)

The [Solvency 2 Annotated Templates template grouping](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2_Hotfix_table_group_arrangement.xlsx) and [Solvency 2 Annotated Templates legacy format](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2_Hotfix_legacy_format.xlsx)

The [Change log between the 2.8.2 Hotfix and 2.8.2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Change_log_between_EIOPA_SolvencyII_2.8.2_Hotfix_vs_2.8.2.xlsx)

The [Change log between the 2.8.2 Hotfix and 2.8.2 Hotfix PWD](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Change_log_between_EIOPA_SolvencyII_2.8.2_Hotfix_vs_2.8.2_Hotfix_PWD.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Documentation_2.8.2.pdf)

**Validations:**

The [Solvency II List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_Validations_2.8.2_Hotfix.xlsx) (updated on 03/06/2026)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/Common/EIOPA_Validations_Syntax.pdf)

**Taxonomy:**

The [Solvency 2 XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.8.2_Hotfix.zip), [Solvency 2 XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.8.2_Hotfix_with_external_files.zip), [Solvency 2 XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_XBRL_Instance_documents_2.8.2_Hotfix.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Taxonomy_Documentation_2.8.2.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Solvency II DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/EIOPA_SolvencyII_DPM_Database_2.8.2_Hotfix.zip)

The [DPM database documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Database_Documentation.pdf)

**Instructions:**

The [Business package](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_Business_package_supporting_2.8.2.zip)

Technical instructions providing information on PEPP integrated reporting:

The [Technical instructions for EIOPA Solvency II reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.0/S2/Technical_LOG_Solvency_II_2.8.0.zip)

Please be informed that artefacts in *italics* are common between multiple frameworks.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified%20dictionary%20NACE.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified_Dictionary_NACE.zip)*.*

Insurance Data Point Model and Taxonomy 2.8.2 (published on 15/10/2024, List of Validations updated on 03/06/2026) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Solvency 2 Release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_Release_Notes_2.8.2.pdf)

The [introduction on SII Taxonomy 2.8.2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_PWD/Presentation/SII_2.8.2_PWD_presentation%20of%20the%20Q&A%20session.pptx) - presentation for the Industry during Q&A Session on 17 September 2024

**DPM:**

The[DPM Dictionary](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Dictionary_2.8.2.xlsx) and [Solvency 2 Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2.xlsx)

The [Solvency 2 Annotated Templates template grouping](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2_table_group_arrangement.xlsx) and [Solvency 2 Annotated Templates legacy format](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_Solvency_II_DPM_Annotated_Templates_2.8.2_legacy_format.xlsx)

The [Change log between the 2.8.0 Hotfix and 2.8.2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/Change_log_between_EIOPA_SolvencyII_2.8.0_Hotfix_vs_2.8.2.xlsx) (including the draft validation detailed change log), [Change log between the 2.8.2 PWD and 2.8.2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/Change_log_between_EIOPA_SolvencyII_2.8.2_PWD_vs_2.8.2.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Documentation_2.8.2.pdf)

**Validations:**

The [*Solvency II List of validations*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_Validations_2.8.2_Published.xlsx) (updated on 03/06/2026)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_Validations_Syntax_2.8.2.pdf)

**Taxonomy:**

The [Solvency 2 XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.8.2_Final.zip), [Solvency 2 XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.8.2_Final_with_external_files.zip) (if you're having troubles unzipping the file, we suggest to use the free software [7Zip](https://7-zip.org/download.html)), [Solvency 2 XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_XBRL_Instance_documents_2.8.2_final.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Taxonomy_Documentation_2.8.2.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Solvency II DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_DPM_Database_2.8.2.zip)

The [*Unified DPM database*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Unified_Database.zip)

The [DPM database documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_DPM_Database_Documentation.pdf)

**Instructions:**

The [Business package](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/S2/EIOPA_SolvencyII_Business_package_supporting_2.8.2.zip)

Technical instructions providing information on PEPP integrated reporting:

The [Technical instructions for EIOPA Solvency II reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.0/S2/Technical_LOG_Solvency_II_2.8.0.zip)

 Please be informed that artefacts in *italics* are common between multiple frameworks.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/Unified%20dictionary.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/eiopa.europa.eu.zip)*.*

Unofficial reporting including [ECB add-ons](https://www.ecb.europa.eu/stats/financial_corporations/insurance_corporations/html/data_reporting.en.html).

## The Pension Funds Data Point Models and XBRL Taxonomies

Pension Funds Data Point Model and Taxonomy 2.9.0 - 2nd Optional NACE 2.1 Hotfix (published on 30/06/2025, last deactivation of validation on 03/06/2026) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Pension Funds release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_Release_Notes_2.9.0_Hotfix2.pdf)

**DPM:**

The [*DPM Dictionary (ATOME output)*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/Common/EIOPA_DPM_Dictionary_2.9.0_Hotfix2(ATOME_output).xlsx) and [Pension Funds Annotated Templates *(*ATOME output)](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_DPM_Annotated_Templates_2.9.0_Hotfix2_ATOME_output.xlsx) workbooks

The [Pension Funds Annotated Templates *(*ATOME output) with table groups within single worksheet](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_DPM_Annotated_Templates_2.9.0_Hotfix2_ATOME_output_table_group_per_worksheet.xlsx) workbook

The [Detailed change log between the 2.9.0 Hotfix 2 and 2.9.0 Hotfix](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_DPM_Change_log_2.9.0_Hotfix2_vs_2.9.0_Hotfix.xlsx)

The [Detailed change log between the 2.9.0 Hotfix 2 and 2.9.0 Hotfix 2 PWD](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_DPM_Change_log_2.9.0_Hotfix2_vs_2.9.0_Hotfix2_PWD.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_DPM_Documentation_2.9.0_Hotfix.pdf)

**Validations:**

The [Pension Funds List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_Validations_2.9.0_Hotfix2.xlsx) (last updated on 03/06/2026)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/Common/EIOPA_Validations_Syntax.pdf)

**Taxonomy:**

The [Pension Funds XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_XBRL_Taxonomy_2.9.0_Hotfix2.zip), the [Pension Funds XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_XBRL_Taxonomy_2.9.0_Hotfix2_with_External_Files.zip)

The [Pension Funds XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_PensionFunds_XBRL_Instance_documents_2.9.0_Hotfix2.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_XBRL_Taxonomy_Documentation_2.9.0_Hotfix.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Pension Funds DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix2/PF/EIOPA_Pension_Funds_DPM_Database_2.9.0_Hotfix2.zip)

**Instructions:**

The [Technical instructions for EIOPA and ECB Pension Funds with integrated PEPP Prudential reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_Technical_Logs_2.9.0_Hotfix_ECB_add-on.pdf)

Please be informed that artefacts in *cursive* are common between Pan-European Personal Pension Products KID, Pan-European Personal Pension Products PR, Solvency II and Pension Funds.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified%20dictionary%20NACE.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified_Dictionary_NACE.zip)*.*

Pension Funds Data Point Model and Taxonomy 2.9.0 Hotfix (Published on 16/07/2024, last deactivations of validation 03/06/2026) 

The Pension Funds 2.9.0 Hotfix is to be used **from 01/01/2025 reference date** until a new version is announced.

**Introduction:**

The [*Taxonomy licence*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/common/EIOPA_DPM_and_Taxonomy_License.pdf)

The [Pension Funds release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_Release_Notes_2.9.0_Hotfix.pdf)

**DPM:**

The [DPM Dictionary *(*ATOME output)](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_DPM_Dictionary_2.9.0_Hotfix(ATOME_output).xlsx) and [Pension Funds Annotated Templates *(*ATOME output)](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Annotated_Templates_2.9.0_Hotfix_ATOME_output.xlsx) workbooks

The [Pension Funds Annotated Templates *(*ATOME output) with table groups within single worksheet](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Annotated_Templates_2.9.0_Hotfix_ATOME_output_table_group_per_worksheet.xlsx) workbook

The [DPM Dictionary](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_DPM_Dictionary_2.9.0_Hotfix.xlsx) and [Pension Funds Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Annotated_Templates_2.9.0_Hotfix.xlsx) legacy format workbooks

The [Detailed change log between the 2.9.0 Hotfix and 2.7.1](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Change_log_2.9.0_Hotfix_vs_2.7.1.xlsx)

The [Detailed change log between the 2.9.0 Hotfix and 2.9.0](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Change_log_2.9.0_Hotfix_vs_2.9.0.xlsx)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_DPM_Documentation_2.9.0_Hotfix.pdf)

**Validations:**

The [Pension Funds List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_Validations_2.9.0_Hotfix_Published.xlsx) (last updated on 03/06/2026)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_Validations_Syntax_2.8.0.pdf)

**Taxonomy:**

The [Pension Funds XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_XBRL_Taxonomy_2.9.0_hotfix.zip), the [Pension Funds XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_XBRL_Taxonomy_2.9.0_hotfix_with_External_Files.zip)

The [Pension Funds XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_XBRL_Instance_documents_2.9.0_hotfix.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_XBRL_Taxonomy_Documentation_2.9.0_Hotfix.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Pension Funds DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_DPM_Database_2.9.0_Hotfix.zip)

The [*EIOPA Unified DPM database with Solvency II, Pension Funds and PEPP Prudential*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/Common/EIOPA_Unified_DPM_Database_2.9.0_Hotfix.zip). Due to the fact that the various release periods of different frameworks are not aligned their dictionaries are also not fully aligned. Therefore, the created unified database is based on a dictionary which is a combination of the dictionaries of the base models, and thus should not be treated as reference.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/Unified%20dictionary.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/eiopa.europa.eu.zip)*.*

**Instructions:**

The [Technical instructions for EIOPA and ECB Pension Funds with integrated PEPP Prudential reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.9.0_hotfix/PF/EIOPA_PensionFunds_Technical_Logs_2.9.0_Hotfix_ECB_add-on.pdf) (updated 15/04/2025)

## The FICOD Data Point Models and XBRL Taxonomies

FICOD Data Point Model and Taxonomy 2.8.1 - 2nd Optional NACE 2.1 Hotfix - (published on 30/06/2025) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Financial conglomerates release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FinancialConglomerates_Release_Notes_2.8.1_Hotfix2.pdf)

**DPM:**

The [*DPM Dictionary*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/Common/EIOPA_DPM_Dictionary_2.8.1_Hotfix2.xlsx) and [Financial conglomerates Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_DPM_Annotated_Templates_2.8.1_Hotfix2.xlsx) workbooks

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_DPM_Documentation_2.8.1_Hotfix.pdf)

The [Detailed change log between the 2.8.1 Hotfix 2 and 2.8.1 Hotfix](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/Change_log_between_EIOPA_FICOD_2.8.1_Hotfix2_and_EIOPA_FICOD_2.8.1_Hotfix.xlsx)

The [Detailed change log between the 2.8.1 Hotfix 2 and 2.8.1 Hotfix 2 PWD](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/Change_log_between_EIOPA_FICOD_2.8.1_Hotfix2_and_EIOPA_FICOD_2.8.1_Hotfix2_PWD.xlsx)

**Validations:**

The [Financial conglomerates List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_Validations_2.8.1_Hotfix2.xlsx)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/Common/EIOPA_Validations_Syntax.pdf)

**Taxonomy:**

The [Financial conglomerates XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_XBRL_Taxonomy_2.8.1_Hotfix2.zip), the [Financial conglomerates XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_XBRL_Taxonomy_2.8.1_Hotfix2_with_External_Files.zip)

The [Financial conglomerates XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_XBRL_Instance_documents_2.8.1_Hotfix2.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_XBRL_Taxonomy_Documentation_2.8.1_Hotfix.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [Financial conglomerates DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FICOD_DPM_Database_2.8.1_Hotfix2.zip)

The [*DPM database documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_DPM_Database_Documentation.pdf)

**Instructions:**

The [Technical instructions for FICOD reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_hotfix2/FICOD/EIOPA_FinancialConglomerates_Technical_Logs_2.8.1_Hotfix2.pdf)

Please be informed that artefacts in *cursive* are common between Pan-European Personal Pension Products KID, Pan-European Personal Pension Products PR, Solvency II, Pension Funds and Financial Conglomerates.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified%20dictionary%20NACE.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified_Dictionary_NACE.zip)*.*

FICOD Data Point Model and Taxonomy 2.8.1 (published on 31/07/2023, Hotfix on 06/11/2023) 

**Introduction:**

The [*Taxonomy licence*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/common/EIOPA_DPM_and_Taxonomy_License.pdf)

The [Financial conglomerates release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FinancialConglomerates_Release_Notes_2.8.1_Hotfix.pdf)

**DPM:**

The [DPM Dictionary](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_DPM_Dictionary_2.8.1_Hotfix.xlsx) and [Financial conglomerates Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_DPM_Annotated_Templates_2.8.1_Hotfix.xlsx) workbooks

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_DPM_Documentation_2.8.1_Hotfix.pdf)

**Validations:**

The [Financial conglomerates List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_Validations_2.8.1_Hotfix.xlsx)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_Validations_Syntax_2.8.0.pdf)

**Taxonomy:**

The [Financial conglomerates XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_XBRL_Taxonomy_2.8.1_Hotfix.zip), the [Financial conglomerates XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_XBRL_Taxonomy_2.8.1_Hotfix_with_External_Files.zip)

The [Financial conglomerates XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_XBRL_Instance_documents_2.8.1_Hotfix.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_XBRL_Taxonomy_Documentation_2.8.1_Hotfix.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_XBRL_Filing_Rules_2.8.1_Hotfix.pdf)

The [Financial conglomerates DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FICOD_DPM_Database_2.8.1_Hotfix.zip)

The [*DPM Database documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/Common/EIOPA_DPM_Database_Documentation.pdf)

**Addition Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/Unified%20dictionary.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/eiopa.europa.eu.zip)*.*

**Instructions:**

The [Technical instructions for FICOD reporting using the XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.1_Hotfix/FICOD/EIOPA_FinancialConglomerates_Technical_Logs_2.8.1_Hotfix.pdf)

Please be informed that artefacts in cursive are common between Pan-European Personal Pension Products KID, Pan-European Personal Pension Products PR, Solvency II, Pension Funds and Financial Conglomerates.

## The PEPP Data Point Models and XBRL Taxonomies

PEPP PRUDENTIAL Data Point Model and Taxonomy 2.7.0 - 3rd Optional NACE 2.1 Hotfix - (published on 30/06/2025) 

**Introduction:**

The [*Taxonomy licence*](https://www.eiopa.europa.eu/system/files/2019-09/eiopa_dpm_and_taxonomy_license.pdf)

The [Pan-European Personal Pension Product PR release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_Release_Notes_2.7.0_Hotfix3.pdf)

**DPM:**

The [*DPM Dictionary*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/Common/EIOPA_DPM_Dictionary_2.7.0_Hotfix3.xlsx) and [Pan-European Personal Pension Product PR Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_DPM_Annotated_Templates_2.7.0_Hotfix3.xlsx) workbooks

The [Detailed change log between the 2.7.0 Hotfix 3 and 2.7.0\_Hotfix](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_DPM_Change_log_2.7.0_Hotfix3_vs_2.7.0_Hotfix.xls)

The [Detailed change log between the 2.7.0 Hotfix 3 and 2.7.0\_Hotfix 3 PWD](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_DPM_Change_log_2.7.0_Hotfix3_vs_2.7.0_Hotfix3PWD.xls)

The [*DPM documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_DPM_Documentation_2.7.0.pdf)

**Validations:**

The [PEPP PR List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_Validations_2.7.0_Hotfix3.xlsx)

The [*Validation syntax*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/Common/EIOPA_Validations_Syntax.pdf)

**Taxonomy:**

The [PEPP PR XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_XBRL_Taxonomy_2.7.0_Hotfix3.zip), the [PEPP PR XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_XBRL_Taxonomy_2.7.0_Hotfix3_with_External_Files.zip), [PEPP PR XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_XBRL_Instance_documents_2.7.0_hotfix3.zip)

The [*XBRL taxonomy documentation*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_XBRL_Taxonomy_Documentation_2.7.0.pdf)

The [*XBRL Filing Rules*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/EIOPA_XBRL_Filing_Rules.pdf)

The [PEPP PR DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0_hotfix3/PEPP/EIOPA_PEPP_PR_DPM_Database_2.7.0_Hotfix3.zip)

**Instructions:**

The [Technical instructions for EIOPA Pan-European Personal Pension Product Prudential reporting](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_Technical_Logs_2.7.0_hotfix.pdf)

Please be informed that artefacts in *cursive* are common between Pan-European Personal Pension Products KID, Pan-European Personal Pension Products PR , Solvency II and Pension Funds.

**Additional Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified%20dictionary%20NACE.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2_hotfix/S2/Unified_Dictionary_NACE.zip)*.*

PEPP PRUDENTIAL Data Point Model and Taxonomy 2.7.0 (published on 16/07/2022, Hotfix on 08/11/2022) 

**Introduction:**

The [Taxonomy licence](https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/Common/EIOPA_DPM_and_Taxonomy_License.pdf)

The [Pan-European Personal Pension Product PR release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_Release_Notes_2.7.0_hotfix.pdf) (updated on 08/11/2022)

**DPM:**

The [DPM Dictionary](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_DPM_Dictionary_2.7.0.xlsx) and [Pan-European Personal Pension Product PR Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_DPM_Annotated_Templates_2.7.0.xlsx) workbooks

The [Detailed change log between the 2.7.0 hotfix and 2.7.0\_PWD2](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_DPM_Change_log_2.7.0_hotfix_vs_2.7.0_PWD2.xls)

The [DPM documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_DPM_Documentation_2.7.0.pdf)

**Validations:**

The [PEPP PR List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_Validations_2.7.0.xlsx) (updated on 08/11/2022)

The [Validation syntax](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_Validations_Syntax_2.7.0.pdf)

**Taxonomy:**

The [PEPP PR XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_XBRL_Taxonomy_2.7.0_Hotfix.zip) (updated on 08/11/2022)

The [PEPP PR XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_XBRL_Taxonomy_2.7.0_Hotfix_with_External_Files.zip) (updated on 08/11/2022)

The [PEPP PR XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_XBRL_Instance_documents_2.7.0_hotfix.zip)

The [XBRL taxonomy documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_XBRL_Taxonomy_Documentation_2.7.0.pdf)

The [XBRL Filing Rules](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_XBRL_Filing_Rules_2.7.0.pdf)

The [PEPP PR DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_DPM_Database_2.7.0_Hotfix.zip) (updated on 08/11/2022)

The [EIOPA Unified DPM database with Solvency II, Pension Funds and PEPP Prudential](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_Unified_DPM_Database_2.7.0_Hotfix.zip) (updated on 08/11/2022)

The [EIOPA Unified XBRL taxonomy with Solvency II, Pension Funds and PEPP Prudential with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_XBRL_Unified_Taxonomy_2.7.0_Hotfix_with_External_Files.zip) (updated on 08/11/2022)

The [EIOPA Unified XBRL taxonomy with Solvency II, Pension Funds and PEPP Prudential](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/Common/EIOPA_XBRL_Unified_Taxonomy_2.7.0_Hotfix.zip) (updated on 08/11/2022)

**Addition Resources:**

The [*unified Taxonomy dictionary Excel file*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/Unified%20dictionary.xlsx) and the related [*taxonomy files Zip archive*](https://dev.eiopa.europa.eu/Taxonomy/Full/2.8.2/Common/eiopa.europa.eu.zip)*.*

**Instructions:**

The [Technical instructions for EIOPA Pan-European Personal Pension Product Prudential reporting](https://dev.eiopa.europa.eu/Taxonomy/Full/2.7.0/PEPP/EIOPA_PEPP_PR_Technical_Logs_2.7.0_hotfix.pdf) (updated on 08/11/2022)

PEPP KID Data Point Model and Taxonomy 2.6.1 (published on 06/08/2021, List of Validations updated on 08/11/2022) 

[Taxonomy licence](https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/common/EIOPA_DPM_and_Taxonomy_License.pdf)

[PEPP KID release notes](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_Release_Notes_2.6.1.pdf)

**DPM:**

[DPM Dictionary](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/Common/EIOPA_DPM_Dictionary_2.6.1.xlsx) and [PEPP KID Annotated Templates](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_DPM_Annotated_Templates_2.6.1.xlsx)

[DPM documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/Common/EIOPA_DPM_Documentation_2.6.1.pdf)

**Validations:**

[PEPP KID List of validations](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_Validations.xlsx)(Updated on 08/11/2022)

[Validation syntax](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.0/common/EIOPA_Validations_Syntax_2.6.0.pdf)

**Taxonomy:**

[PEPP KID XBRL taxonomy](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_XBRL_Taxonomy_2.6.1.zip)

[PEPP KID XBRL taxonomy with external files](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_XBRL_Taxonomy_with_External_Files_2.6.1.zip)

[PEPP KID XBRL instance examples](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_XBRL_Instance_documents_2.6.1.zip)

[Pension funds XBRL assertion test](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.0/PF/EIOPA_PensionFunds_XBRL_Assertions_Tests_2.6.0_Hotfix.zip) (updated on 10/12/2021)

[XBRL taxonomy documentation](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/Common/EIOPA_XBRL_Taxonomy_Documentation_2.6.1.pdf)

[XBRL Filing Rules](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/Common/EIOPA_XBRL_Filing_Rules_2.6.1.pdf)

[PEPP KID DPM database](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_DPM_Database_2.6.1.zip)

**Instructions:**

[Technical instructions for KID PEPP Data Point Model and Taxonomy 2.6.1](https://dev.eiopa.europa.eu/Taxonomy/Full/2.6.1/PEPP/EIOPA_PEPP_KID_Technical_Logs_2.6.1.pdf)

## Contact

**To contact us for support please use one of the below options:**

* Questions regarding the business package (supervisory reporting or public disclosure requirements) should be submitted on the regulatory [Q&A page](https://www.eiopa.europa.eu/tools-and-data/qa-regulation_en).
* Questions regarding DPM and XBRL technical issues: please contact xbrl![at](/modules/contrib/spamspan/image.gif)eiopa [dot] europa [dot] eu (xbrl[at]eiopa[dot]europa[dot]eu) identifying the Taxonomy Release of the DPM-XBRL implementation issue.
* Questions regarding the business validations (BV) and technical validations (TV): please contact validations![at](/modules/contrib/spamspan/image.gif)eiopa [dot] europa [dot] eu (validations[at]eiopa[dot]europa[dot]eu)

## Related resources

* [Deprecated versions](/deprecated-versions-data-point-model-and-xbrl_en)
