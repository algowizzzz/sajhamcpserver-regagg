# Standardized Institutions Risk Asset Portfolio Information (RAPID1)

Information

Type of document

Technical specification

Industry

Deposit-taking institutions

Return

Standardized Institutions Risk Asset Portfolio Information (RAPID1)

Last updated

May 2022

Version

4.2

Table of contents

OSFI cannot redistribute the concordance tables provided by Statistics Canada. To purchase a copy of the concordance tables for the new NAICS codes, please consult [Stats Canada's website](https://www.statcan.gc.ca/en/reference/refcentre/index). Online requests can also be made directly at [infostats@statcan.gc.ca](mailto:infostats@statcan.gc.ca)

**For data submissions effective Q1 2022**

## Return files

[RAPCORP - Data definitions (XLSX, 240 KB)](/sites/default/files/documents/rapcorp-rapid1-dd-en.xlsx "rapcorp-rapid1-dd-en.xlsx") [RAPCORP - Validation rules (XLSX, 72.14 KB)](/sites/default/files/documents/rapid1-validation-en.xlsx "rapid1-validation-en.xlsx")

## Technical specification

### 1. Introduction

This document describes the layout and format of files to be provided to OSFI to populate the Risk Asset Portfolio Information Database. Data validation rules, errors and warnings are also described.

#### 1.1. RAPID documents

The RAPID Data Field Definitions, Version 3.0 lists the code values and definitions for each field in RAPID. This document also provides examples, and background information about the data collected to populate RAPID.

The RAPID Technical Specification, Version 3.0 identifies the layout and format of files to be provided to OSFI to populate RAPID.

These two documents should be read in conjunction with each other.

### 2. Extract File Requirements

The following sections describe the extract file layout for RAPID. Throughout the extract file layout documentation, all primary key fields are printed in bold type and listed in the order in which they appear in the key.

Within the record layout in each section (sections 2.5 to 2.11), the first column refers to the Field ID, which should be used to link to the RAPID Data Field Definitions, Version 2.02 document. The second and third columns refer to start and end positions of that field within the record. The following columns are length of the field, field name, "M" which refers to mandatory field, and finally the "Notes" column provides extra information to assist with the planning of extracts and describes what field format/mask should be used.

#### 2.1. File Type and Naming Convention

Data destined for the RAPID database will be a fixed width text file, 368 bytes per line, and with a Carriage Return (CR) and Line Feed (LF) as record delimiters. Fields which are empty (i.e. have no value) must be indicated by blank spaces if the data type is alphanumeric [PIC(X)] or zeroes if data type is numeric [PIC(9)]. Mandatory fields must be populated as indicated on the RAPID Data Field Definitions, Version 3.0.

The fixed width text file will have the naming convention of FI\_RAPCORP\_MMYYYY.DAT, where FI represents the Institution ID (provided by OSFI), RAPCORP is a fixed string, MM represents the month and YYYY represents the year of the reporting date of information.

#### 2.2. Record Type

The first field in each row must be the record type or row identifier. Valid values are:

Descriptions of record types

| Record Type | Description |
| --- | --- |
| 00 | Header Record |
| 10 | Common Risk header record |
| 20 | Borrower header record |
| 30 | Facility detail record |
| 21 | Borrower sub-footer record |
| 11 | Common Risk sub-footer record |
| 99 | Footer record |

#### 2.3. File Structure

The first row of the extract file must be a Header record ("00") and the last one must be a Footer record ("99"), and they must be the only "00" and "99" records in the file.

Apart from the Header and Footer, all the other (data) records may be in any order. Referential integrity is established by checking for the existence of parent records by using the primary keys (Common Risk ID, Borrower ID and Facility ID).

For example, every Facility record must have a Borrower record and each Borrower record must have a Common Risk record. The order of the records is irrelevant, as long as the logical data hierarchy structure is respected.

Also note that every Common Risk record must have a Common Risk sub-footer. The same applies for Borrower records: every Borrower record needs a Borrower sub-footer record.

OSFI suggests the following file structure:

File structure diagram

![Diagram showing structure of records in a file. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2022-05/en/rpd_ts_fs.png)

File structure - Text version

* Header Record ("00")
  + Common Risk Header Record ("10")
    - Borrower Header Record ("20")
      * Facility Record ("30")

        Different facilities within the same borrower record
    - Borrower Footer Record ("21")

      Repeat the above structure for different borrowers with in the same Common Risk record
  + Common Risk Footer ("11")

    Repeat the above structure for different Common Risk records
* Footer Record ("99")

#### 2.4. Record Field Order

The order of the fields in a record must be the same as the order they are specified in the following record layouts (sections 2.5 to 2.11). Field values must be formatted as specified in the record layouts.

#### 2.5. Header Record (00)

The Header record is a quality control mechanism that uniquely identifies each file sent to OSFI (i.e. who sent the file, the reporting date, the file name, etc). The information contained in the Header field is checked against the file name and the actual details of the file to ensure that the file received by OSFI has not been corrupted.

The record layout of the Header is detailed below:

Layout of the header record (00)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "00" |
| 1 | 3 | 6 | 4 | Institution ID | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 2 | 7 | 14 | 8 | Reporting date of information | ✓mandatory | pic(9) - Format: YYYYMMDD |
| 98 | 15 | 21 | 7 | File type | ✓mandatory | pic(X) - Fixed string "RAPCORP" |
| 99 | 22 | 27 | 6 | File layout version | ✓mandatory | pic(X) - Fixed string "02.0.0", left justified |
| 100 | 28 | 28 | 1 | File processing instruction | ✓mandatory | pic(9) - 1 or 2 |
| - | 29 | 360 | 332 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.6. Common Risk Record (10)

The record layout of the Common Risk is detailed as follows:

Layout of the common risk record (10)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "10" |
| 3 | 3 | 17 | 15 | **Common Risk number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 5 | 18 | 117 | 100 | Common Risk name | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 9 | 118 | 119 | 2 | Common Risk country code of Incorporation | ✓mandatory | pix(X) |
| - | 120 | 360 | 241 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.7. Borrower Record (20)

The record layout of the Borrower is detailed below:

Layout of the borrower record (20)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "20" |
| 3 | 3 | 17 | 15 | **Common Risk number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 10 | 18 | 32 | 15 | **Borrower number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 13 | 33 | 132 | 100 | Borrower name | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 14 | 133 | 136 | 4 | Borrower risk rating | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 103 | 137 | 140 | 4 | NAICS Version | ✓mandatory | pic(9) - 2007 version |
| 19 | 141 | 146 | 6 | NAICS code | ✓mandatory | pic(X) - All Canadian NAICS codes up to 2017 accepted - Left justified, right-padded with spaces |
| 21 | 147 | 148 | 2 | Borrower country of residence | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 22 | 149 | 150 | 2 | Borrower province/state code | not mandatory | pic(X) - Left justified, right-padded with spaces |
| 25 | 151 | 151 | 1 | Watch list | ✓mandatory | pic(9) - 1, 2 or 9 |
| 29 | 152 | 166 | 15 | Allowance for Expected Credit Losses | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 30 | 182 | 196 | 15 | Write-offs | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 32 | 197 | 211 | 15 | Recoveries | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 109 | 212 | 212 | 1 | Impairment Status | ✓mandatory | pic(9) - 1, 2 or 9 |
| 110 | 213 | 213 | 1 | IFRS 9 Stage of Exposure | ✓mandatory | pic(9) - 1, 2, 3 or 9 |
| - | 214 | 360 | 147 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.8. Facility Record (30)

The record layout of the Facility is detailed below:

Layout of the facility record (30)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "30" |
| 3 | 3 | 17 | 15 | **Common Risk number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 10 | 18 | 32 | 15 | **Borrower number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 34 | 33 | 47 | 15 | **Facility number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 35 | 48 | 55 | 8 | **Primary facility type** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 37 | 56 | 57 | 2 | Facility country of risk | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 38 | 58 | 59 | 2 | Booking point country | not mandatory | pic(X) - Left justified, right-padded with spaces |
| 40 | 60 | 63 | 4 | Facility risk rating | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 41 | 64 | 66 | 3 | Facility currency | ✓mandatory | pic(X) |
| 42 | 67 | 81 | 15 | Facility total authorized (orig currency) | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 43 | 82 | 96 | 15 | Facility total outstanding (orig currency) | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 44 | 97 | 111 | 15 | Facility total authorized in CAD | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 45 | 112 | 126 | 15 | Facility potential exposure in CAD | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 46 | 127 | 141 | 15 | Facility total outstanding in CAD | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 106 | 142 | 156 | 15 | Notional Amount Authorized | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 107 | 157 | 171 | 15 | Notional Amount Outstanding | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 49 | 172 | 172 | 1 | Exposure type | ✓mandatory | pic(9) - 1, 2, 3 or 9 |
| 50 | 173 | 173 | 1 | Shared and/or linked facility | ✓mandatory | pic(9) - 1, 2, 3, 4 or 9 |
| 51 | 174 | 188 | 15 | Maximum amount draw | not mandatory | pic(9) - No commas/dots, left-padded with zeroes |
| 52 | 189 | 191 | 3 | Percentage draw | not mandatory | pic(9) - No commas/dots, left-padded with zeroes |
| 56 | 192 | 193 | 2 | Facility status | ✓mandatory | pic(9) - No commas/dots, left-padded with zeroes |
| 62 | 194 | 201 | 8 | Primary collateral | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 63 | 202 | 203 | 2 | Seniority profile | ✓mandatory | pic(9) - Left-padded with zeroes |
| 64 | 204 | 204 | 1 | Participated facilities | ✓mandatory | pic(9) - 1, 2 or 9 |
| 65 | 205 | 205 | 1 | Syndicate role | ✓mandatory | pic(9) - 1, 2, 3 or 9 |
| 66 | 206 | 220 | 15 | Allowance for Expected Credit Losses | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 67 | 221 | 235 | 15 | Write-offs | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 68 | 236 | 350 | 15 | Filler | ✓mandatory | pic(X) - Blank spaces |
| 69 | 251 | 265 | 15 | Recoveries | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 70 | 266 | 266 | 1 | IFRS 9 Stage of Exposure | ✓mandatory | Pic(9) - 1, 2, 3 or 9 |
| - | 267 | 360 | 94 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.9. Borrower Footer Record (21)

The record layout of the Borrower footer is detailed below:

Layout of the borrower footer record (21)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "21" |
| 3 | 3 | 17 | 15 | **Common Risk number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 10 | 18 | 32 | 15 | **Borrower number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 15 | 33 | 47 | 15 | Borrower total authorized in CAD | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 16 | 48 | 62 | 15 | Borrower potential exposure in CAD | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 17 | 63 | 77 | 15 | Borrower total outstanding in CAD | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| - | 78 | 82 | 5 | Total number of facilities in this borrower | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 102 | 83 | 97 | 15 | Borrower total outstanding in CAD insured | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| - | 98 | 360 | 263 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.10. Common Risk Footer Record (11)

The record layout of the Common Risk footer is detailed below:

Layout of the common risk footer record (11)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "11" |
| 3 | 3 | 17 | 15 | **Common Risk number** | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 6 | 18 | 32 | 15 | Common Risk total authorized | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 7 | 33 | 47 | 15 | Common Risk potential exposure | not mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| 8 | 48 | 62 | 15 | Common Risk total outstanding | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| - | 63 | 67 | 5 | Number of borrowers in this Common Risk | ✓mandatory | pic(9) - no commas/dots, left-padded with zeroes |
| - | 68 | 360 | 293 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.11. Footer Record (99)

The record layout of the Footer is detailed below:

Layout of the footer record (99)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 2 | 2 | **Record Type** | ✓mandatory | pic(9) - Fixed string "99" |
| 1 | 3 | 6 | 4 | Institution ID | ✓mandatory | pic(X) - Left justified, right-padded with spaces |
| 2 | 7 | 14 | 8 | Reporting date of information | ✓mandatory | pic(9) - Format: YYYYMMDD |
| 98 | 15 | 21 | 7 | File type | ✓mandatory | pic(X) - Fixed string "RAPCORP" |
| 99 | 22 | 27 | 6 | Layout version | ✓mandatory | pic(X) - Format:02.0.0, left justified |
| 100 | 28 | 28 | 1 | File processing instruction | ✓mandatory | pic(9) - 1 or 2 |
| - | 29 | 360 | 332 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 361 | 368 | 8 | Sequential row counter | ✓mandatory | pic(9) - left-padded with zeroes |
| - | 369 | 370 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

#### 2.12. Additional Important Notes

* All dates are to be reported according to the following format: YYYYMMDD Where, YYYY represents the year, MM represents the month and DD represents the day. E.g. "19990105" represents January 5, 1999. All non-mandatory dates that cannot be provided should be zeroes.
* All percentages and dollar amount fields are to be rounded to the nearest percent/dollar; in other words, no decimal digits should be reported.
* The sequential row counter field that appears in every record must start at "00000001" in the header record and be incremented by 1 in every row. Therefore, the footer will show the total number of records in the file.

### 3. Data Validation Rules

#### 3.1. Error Handling

The error handling philosophy is to trap the maximum number of possible errors and warnings. The file will be entirely rejected if errors are detected, and no data will be uploaded to the database. Warnings are exceptions that will not stop the database from accepting the file.

Processing of the file will proceed as detailed below:

##### 3.1.1. Pre-processing Checks

Pre-processing is performed to ensure that the extract files received are formatted correctly, and that the header and footer records match the actual contents of the file. A program checks extract files for header and formatting errors. The following pre-processing checks are made:

* Each record in the file has a valid record type (00, 10, 20, 30, 21, 11, 99).
* Each record in the file is 368 byte long plus 2 ASCII characters (Carriage Return and Line Feed).
* Each record has the correct number of fields for its record type.
* Each record has a sequential counter that starts at 00000001 at the header record and is incremented by 1 in each record in the file.
* The name of the file exactly matches the information of the Header and Footer records.
* The extension of the file is .DAT.
* The institution ID in the file name, header and footer records is a valid Bank of Canada code (provided by OSFI).
* The 4th field of the Header and Footer records must be a valid file type ("RAPCORP").

##### 3.1.2. Data Hierarchy Checks

* Each Facility record must have a Borrower record and each Borrower record must have a Common Risk record.
* Each Common Risk header record must have a matching Common Risk footer record. Similarly, each Borrower header record must have a matching Borrower footer record.
* Each Common Risk must have a unique combination of record type ("10") and Common Risk number as highlighted on section 2.6 and 2.10 of this document.
* Each Borrower must have a unique combination of record type, ("20") Common Risk number and Borrower number as highlighted on section 2.7 and 2.9 of this document.
* Each Facility must have a unique combination of record type ("30"), Common Risk number, Borrower number, Facility number and primary facility type as highlighted on section 2.8 of this document.
* The total number of borrowers in the Common Risk footer must match the count of Borrower records with the same Common Risk number.
* The total number of facilities in the Borrower footer must match the actual count of Facility records with the same Common Risk and Borrower number.

##### 3.1.3. Field Value Checking

Field value checking ensures that a field has valid values as specified in the RAPID Data Field Definitions, Version 2.02.

#### 3.2. Business Rules

The term "business rules" usually refers to a set of conditions that can be used to determine the validity of data. Each rule specifies criteria that certain data elements (or a number of elements) have to meet to be valid. Business rules are used in the RAPID context to identity data that has potentially been entered incorrectly. Sending these records back to the Financial Institutions for correction leads to greater integrity of information in Risk Asset Portfolios.

##### 3.2.1. Industry Classification Codes

OSFI will validate the submitted NAICS codes (ID #19) against Industry Classification lookup tables provided by Statistics Canada. The submitted code will be rejected if it does not exist in the appropriate table.

##### 3.2.2. Countries

Country codes (ID #s 9, 21, 37 and 38) will be validated against International Organization for Standardization (ISO) standards (ISO# 3166-1).

##### 3.2.3. Currencies

Currency codes (ID #41) will be validated against ISO standards (ISO# 4217). Pre-euro currencies and other old currencies are still used and will be accepted.

##### 3.2.4. Province/State (Warning)

If the country (ID #21) is Canada or USA, province or state (ID #22) data will be validated against the last two (2) characters of the ISO# 3166-2 standard.

##### 3.2.5. Dollar Amounts

For the following validation rules, thresholds have been established to account for acceptable levels of data inconsistencies, including rounding errors:

* Each Common Risk total authorized (ID #6) must be equal to or greater than $10 Million. Otherwise, an error will occur.
* Negative values should be reported with the hyphen sign before the first 'meaningful' digit, in other words report the negative number left-padded with zeros. For example, 000000000073654 and 0000000-7900000 are valid 15 character numeric values representing 73,654 and -7,900,000, respectively.
* Each Facility authorized in Canadian dollars (ID #44) must not exceed its Borrower authorized (ID #15) by more than 1% of Borrower authorized. Otherwise, an error will occur. Differences of less than 1% will be shown as warnings.
* Each Borrower authorized in Canadian dollars (ID #15) must not exceed its Common Risk authorized (ID #6) by more than 1% of Common Risk authorized. Otherwise, an error will occur. Differences of less than 1% will be shown as warnings.
* On a portfolio-wide basis, total potential exposure at the Common Risk level (ID #7) must not exceed total Common Risk authorized (ID #6) by more than 10% of total Common Risk authorized. Otherwise, an error will occur.
* On a portfolio-wide basis, total potential exposure at the Borrower level (ID #16) must not exceed total Borrower authorized (ID #15) by more than 10% of total Borrower authorized. Otherwise, an error will occur.
* On a portfolio-wide basis, total potential exposure at the Facility level (ID #45) must not exceed total Facility authorized (ID #44) by more than 10% of total Facility authorized. Otherwise, an error will occur.
* On a portfolio-wide basis, total outstanding at the Borrower level (ID #17) must not exceed total Common Risk authorized (ID #6) by more than 10% of total Common Risk authorized. Otherwise, an error will occur. Differences of less than 10% will be shown as warnings.
* On a portfolio-wide basis, total outstanding at the Facility level (ID #46) must not exceed total Borrower authorized (ID #15) by more than 10% of total Borrower authorized. Otherwise, an error will occur. Differences of less than 10% will be shown as warnings.
* The Common Risk outstanding (ID #8) must not differ from the sum of all its Borrowers' outstanding beyond the range of +/- 1% of common risk outstanding. Otherwise, an error will occur. Discrepancies within the +/- 1% range will be shown as warnings.
* The Borrower outstanding (ID #17) must not differ from the sum of all its Facilities' outstanding beyond the range of +/- 1% of Borrower outstanding. Otherwise, an error will occur. Discrepancies within the +/- 1% range will be shown as warnings.
* If a Common Risk has only 1 Borrower, the Common Risk authorized (ID #6) must be greater than or equal to its Borrower authorized (ID #15). Otherwise, an error will occur. This validation rule does not have a threshold for data inconsistencies.
* If a borrower has only 1 Facility, the Borrower authorized (ID #15) must be greater than or equal to its Facility authorized in Canadian dollars (ID #44). Otherwise, an error will occur. This validation rule does not have a threshold for data inconsistencies.
* For facilities with the same Common Risk ID (ID #3), Borrower ID (ID #10), and Facility ID (ID #34), they must have:

  + The same Facility risk rating (ID #40)
  + The same Facility total authorized (ID #42)
  + The same Facility total outstanding (ID #43)
  + The same Facility total authorized - CAD equivalent (ID #44)
  + The same Facility total outstanding - CAD equivalent (ID #46)
  + The same Allowance for Expected Credit Losses (ID #66)
  + The same write-offs (ID #67)
  + The same recoveries (ID #69)

  Otherwise, an error will occur.
* Warnings are issued if:
  + Common Risk potential exposure (ID #7) is greater than Common Risk authorized (ID #6)
  + Borrower potential exposure (ID #16) is greater than Borrower authorized (ID #15)
  + Facility potential exposure (ID #45) is greater than Facility authorized (ID #44)
  + A Borrower individual allowance (ID #29) is less than the sum of all its Facilities' individual allowance (ID #66)
  + A Common Risk authorized (ID #6) is less than the sum of all its Borrowers' outstanding (ID #17)
  + A Borrower authorized (ID #15) is less than the sum of all its Facilities' outstanding (ID #46)

##### 3.2.6. Borrower Risk Rating

Borrower risk rating (ID #14) will be validated against the list of Borrower risk ratings provided by the Financial Institutions as stated in note #8 of the RAPID Data Field Definitions, Version 2.02.

##### 3.2.7. Foreign Currency Check (Warning)

If facility currency (ID #41) is not "CAD", then

* Facility total authorized (ID #42) should not equal Facility total authorized CAD equivalent (ID #44)
* Facility total outstanding (ID #43) should not equal Facility total outstanding CAD equivalent (ID #46)

Otherwise, a warning will occur.

##### 3.2.8. Notional Amounts

If the Primary Facility Type (ID #35) is a not trading line, then Notional Amount Authorized (ID #106) must be equal to Facility Total Authorized (ID# 42), and Notional Amount Outstanding (ID #107) must be equal to Facility Total Outstanding (ID# 43). Otherwise, an error will occur.

The following codes from Table A in the RAPID Data Field Definitions, Version 2.02 document are trading lines:

* 08: Derivative - FX, Futures, Interest/Cross Currency Swap
* 09: Derivative - Credit
* 10: Derivative - Other
* 13: Other off-balance sheet facilities
* 18: Other trading facility

##### 3.2.9. Other Business Validation Rules

The submitted value for certain fields must come from a set of pre-defined options specified in the RAPID Data Field Definitions, Version 2.02. The submission of a value outside of the pre-defined set will cause rejection of the data file. The RAPID Data Field Definitions, Version 2.02 specifies options for the following fields:

* File Processing Instruction (ID #100)
* Watch List (ID #25)
* Impairment Status (ID #109)
* Primary Facility Type (ID #35)
* Exposure Type (ID #49)
* Shared And/Or Linked Facility (ID #50)
* Facility Status (ID #56)
* Primary Collateral (ID #62)
* Seniority Profile (ID #63)
* Participated Facilities (ID #64)
* Syndicate Role (ID #65)
* IFRS 9 Stage of Exposure

#### 3.3. Optional Versus Mandatory Data Elements

Where data points are cited as "optional", this is to accommodate instances where the data point may not exist for all Financial Institutions. If, however, a Financial Institution has the data for an "optional" field, the data **must** be reported in the return.

Mandatory fields are data points that **must** be reported by **all** Financial Institutions. Otherwise, the data will be rejected.

#### 3.4. Error Report

If any of these validation checks fail, an Error Report will be created and the input file will be rejected. The contents of the Error Report will vary depending upon the types of errors found in the input file. This report will have enough information to help troubleshoot and correct the inconsistencies. However, if the Error Report contains only Warnings, the input file will be accepted by OSFI. Please, note that you are still required to correct the erroneous/inconsistent data (in other words to eliminate the 'warnings') for the following data submission.

This report will be e-mailed to the Financial Institution in question indicating whether or not the file was successfully uploaded in the database. If problems were detected, the error report will be attached to this e-mail including both 'errors' and 'warnings'.

### Change Control Log

#### Changes in version 2.0

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 1.9 of this document on hand when reviewing this change log. Note that there may be a number of grammatical and formatting changes in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 1.9 of this Technical Specification Document do not need to use this change log.

1. Renamed 'Revisions' section to 'Change Control Log' and moved to the end of the document.
2. Section 2.5 - Header Record (00): Field ID 98 assigned to the <File type> field.
3. Section 2.5 - Header Record (00): <File layout version> Notes changed to "pic(X) - Fixed String "02.0.0"." Also assigned Field ID 99 to the data point.
4. Section 2.5 - Header Record (00): Added Field ID 100 <File processing instruction>. (Start/End positions and field Length are adjusted accordingly.)
5. Section 2.5 - Header Record (00): Added <CR + LF>.
6. Section 2.6 - Common Risk Record (10): Removed Field ID 4 <Common Risk KMV ID>. (Start/End positions and field Length are adjusted accordingly.)
7. Section 2.6 - Common Risk Record (10): Added <CR + LF>.
8. Section 2.7 - Borrower Record (20): Removed Field ID 11 <Borrower KMV ID>. (Start/End positions and field Length are adjusted accordingly.)
9. Section 2.7 - Borrower Record (20): Removed Field ID 12 < Borrower ticker symbol>. (Start/End positions and field Length are adjusted accordingly.)
10. Section 2.7 - Borrower Record (20): Removed Field ID 18 <Industry classification system>. (Start/End positions and field Length are adjusted accordingly.)
11. Section 2.7 - Borrower Record (20): Replaced Field ID 19 <Primary industry classification code> with <NAICS code>.
12. Section 2.7 - Borrower Record (20): Removed Field ID 20 <Secondary industry classification code>. (Start/End positions and field Length are adjusted accordingly.)
13. Section 2.7 - Borrower Record (20): Added Field ID 103 <Industry Code Standard Version>. (Start/End positions and field Length are adjusted accordingly.)
14. Section 2.7 - Borrower Record (20): Removed Field ID 23 <Contact name>. (Start/End positions and field Length are adjusted accordingly.)
15. Section 2.7 - Borrower Record (20): Removed Field ID 24 <Contact phone number>. (Start/End positions and field Length are adjusted accordingly.)
16. Section 2.7 - Borrower Record (20): Removed Field ID 26 <Borrower portfolio>. (Start/End positions and field Length are adjusted accordingly.)
17. Section 2.7 - Borrower Record (20): Removed Field ID 27 <Borrower annual revenues>. (Start/End positions and field Length are adjusted accordingly.)
18. Section 2.7 - Borrower Record (20): Removed Field ID 28 <Industry portfolio classification>. (Start/End positions and field Length are adjusted accordingly.)
19. Section 2.7 - Borrower Record (20): Removed Field ID 31 <Date of bank's write-off>. (Start/End positions and field Length are adjusted accordingly.)
20. Section 2.7 - Borrower Record (20): Removed Field ID 33 <Date of recovery>. (Start/End positions and field Length are adjusted accordingly.)
21. Section 2.7 - Borrower Record (20): Added Field ID 109 <Impairment Status>. (Start/End positions and field Length are adjusted accordingly.)
22. Section 2.7 - Borrower Record (20): Added <CR + LF>.
23. Section 2.8 - Facility Record (30): Removed Field ID 36 <Secondary facility type>. (Start/End positions and field Length are adjusted accordingly.)
24. Section 2.8 - Facility Record (30): Removed Field ID 39 <Booking point transit>. (Start/End positions and field Length are adjusted accordingly.)
25. Section 2.8 - Facility Record (30): Added Field ID 106 <Notional Amount Authorized>. (Start/End positions and field Length are adjusted accordingly.)
26. Section 2.8 - Facility Record (30): Added Field ID 107 < Notional Amount Outstanding>. (Start/End positions and field Length are adjusted accordingly.)
27. Section 2.8 - Facility Record (30): Mandatory check added to Field ID 45 < Facility potential exposure in CAD>.
28. Section 2.8 - Facility Record (30): Removed Field ID 47 <Facility total outstanding in CAD on B/S>. (Start/End positions and field Length are adjusted accordingly.)
29. Section 2.8 - Facility Record (30): Removed Field ID 48 <Facility total outstanding in CAD off B/S>. (Start/End positions and field Length are adjusted accordingly.)
30. Section 2.8 - Facility Record (30): Removed Field ID 53 <Origination date>. (Start/End positions and field Length are adjusted accordingly.)
31. Section 2.8 - Facility Record (30): Removed Field ID 54 <Maturity date>. (Start/End positions and field Length are adjusted accordingly.)
32. Section 2.8 - Facility Record (30): Removed Field ID 55 <Review date>. (Start/End positions and field Length are adjusted accordingly.)
33. Section 2.8 - Facility Record (30): Removed Field ID 57 <Default date>. (Start/End positions and field Length are adjusted accordingly.)
34. Section 2.8 - Facility Record (30): Removed Field ID 58 <Performing product >. (Start/End positions and field Length are adjusted accordingly.)
35. Section 2.8 - Facility Record (30): Removed Field ID 59 <Hedging status>. (Start/End positions and field Length are adjusted accordingly.)
36. Section 2.8 - Facility Record (30): Removed Field ID 60 <Hedging percentage>. (Start/End positions and field Length are adjusted accordingly.)
37. Section 2.8 - Facility Record (30): Removed Field ID 61 <Cash and/or marketable security>. (Start/End positions and field Length are adjusted accordingly.)
38. Section 2.8 - Facility Record (30): Modified Field ID 64 from <Syndicated Facilities> to <Participated Facilities> and updated definition.
39. Section 2.8 - Facility Record (30): Removed Field ID 68 <Date of bank's write-off>. (Start/End positions and field Length are adjusted accordingly.)
40. Section 2.8 - Facility Record (30): Removed Field ID 70 <Date of recovery>. (Start/End positions and field Length are adjusted accordingly.)
41. Section 2.8 - Facility Record (30): Added Field ID 108 <Specific Provisions>. (Start/End positions and field Length are adjusted accordingly.)
42. Section 2.8 - Facility Record (30): Added <CR + LF>.
43. Section 2.9 - Borrower Footer Record (21): Added Field ID 102 <Borrower Total Outstanding - Canadian dollar equivalent - Insured>. (Start/End positions and field Length are adjusted accordingly.)
44. Section 2.9 - Borrower Footer Record (21): Added <CR + LF>.
45. Section 2.10 - Common Risk Footer Record (11): Added <CR + LF>.
46. Section 2.11 - Footer Record (99): Removed Field ID 71 <Total loans under CAD 10 Million>. (Start/End positions and field Length are adjusted accordingly.)
47. Section 2.11 - Footer Record (99): Removed Field ID 72 <Total loans on B/S this Quarter>. (Start/End positions and field Length are adjusted accordingly.)
48. Section 2.11 - Footer Record (99): Field ID 98 assigned to the <File type> field.
49. Section 2.11 - Footer Record (99): <File layout version> Notes changed to "pic(X) - Fixed String "02.0.0"." Also assigned Field ID 99 to the data point.
50. Section 2.11 - Footer Record (99): Added <CR + LF>.
51. Section 3.2.1 - Industry Classification Codes: Removed references to SIC and FI specific industry classification codes, and any secondary industry classification.
52. Section 3.2.2 - Performing Product vs. Facility Status: Removed business rule "(A) loan can be reported as 'performing' (ID #58), provided that its status (ID #56) is not 'in default'." Subsequent Business Rule ID's have been renumbered accordingly.
53. Section 3.2.4 - Modified data source of validation rule from Statistics Canada to ISO 3166-2.
54. Section 3.2.5 - Added rule on reporting thresholds at the Common Risk level.
55. Section 3.2.6 - Date Checks (Warning): Removed business rule "(R)eview date (ID #55) and maturity date (ID #54) must be greater than origination date (ID #53)." Subsequent Business Rule ID's have been renumbered accordingly.
56. Section 3.2.7 - Dollar Amounts: Removed business rule "(T)he same facility total outstanding - CAD equivalent, on-balance sheet (ID #47)."
57. Section 3.2.7 - Dollar Amounts: Removed business rule "(T)he same facility total outstanding - CAD equivalent, off-balance sheet (ID #48)."
58. Section 3.2.8 - Facility Types and Collateral: Removed Business Rule "(F)acility type IDs (ID #35 and 36) and collateral ID (ID #62) will be validated against the data provided by the Financial Institutions as stated on notes 8 and 9 in the RAPID Data Field Definitions, Version 1.9, February 2004. OSFI will use these data to map against internal definitions of facility types and collateral."
59. Section 3.2.9 - Notional Amounts: Added business rules. Subsequent Business Rule ID's have been renumbered accordingly.
60. Section 3.2.10 - Performing Product and Specific Allowance: Removed business rule "(I)f Specific Allowance (ID #66) is greater than zero, then Performing Product (ID #58) must be 2 (non-performing). This validation rule does not apply where performing product status is 9 (unknown) - warning is raised instead." Subsequent Business Rule ID's have been renumbered accordingly.
61. Section 3.2.10 - Other Business Validation Rules: Added business rules. Subsequent Business Rule ID's have been renumbered accordingly.
62. Section 3.3 - Optional Versus Mandatory Data Elements: Added business rules. Subsequent Business Rule ID's have been renumbered accordingly.
63. Section 3.4 - Error Reporting: Expanded business rule to clarify the role of warnings in the error reports.

#### Changes in version 2.01

1. Correction to Section 2.8 - Removed ID #39 and ID #68.

#### Changes in version 2.02

1. Correction to Section 2.8 - Reference to ID #57 changed to ID #62.
2. Correction to Section 3.2.9 - Reference to ID #57 changed to ID #62. Reference to ID# 106 changed to ID #109.
3. Section 3.2.5 - Negative number formatting for ID# 105 and #108.
4. Section 2.7 - Starting position of ID#22 changed to 149.
5. Section 3.2.9 - File processing Instruction (ID #100) added to the list.

#### Changes in version 2.03

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 2.02 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 2.01 of this Technical Specification Document do not need to use this change log.

##### General

1. Changed all reference of 'Specific Provisions' to 'Individual Provisions for Credit Losses'
2. Changed all reference of 'Specific Allowances' to 'Individual Allowances for Credit Losses'

#### Changes in version 3.0

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 2.03 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 2.03 of this Technical Specification Document do not need to use this change log.

##### General

1. Changed all reference of 'Individual Allowances for Credit Losses'' to 'Allowances for Expected Credit Losses''
2. Removed 'Individual Provision for Credit Losses' in record type '20' and '30'
3. Added new field 'IFRS 9 Stage of Exposure' to record type '20'
4. Removed business rules in section 3.2.5
5. Added business validation rule in section 3.2.9

#### Changes in version 3.1

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 3.0 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 3.0 of this Technical Specification Document do not need to use this change log.

##### General

1. Correction to field "IFRS 9 Stage of Exposure" in record type '20' to include 'Pic(9) - 1, 2, 3 or 9'

#### Changes in version 4.0

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 3.1 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 3.1 of this Technical Specification Document do not need to use this change log.

##### General

1. Section 2.7: Correction under field "NAICS Version" in record type '20'
2. Section 2.8: Adding of field "IFRS 9 Stage of Exposure" in record type '30' to include 'Pic(9) - 1, 2, 3 or 9'
3. Section 2.8: Correction under field "Filler" in record type '30'

#### Changes in version 4.1

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 4.0 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 4.0 of this Technical Specification Document do not need to use this change log.

##### General

1. Section 2.7: Correction under fields "NAICS Version" and "NAICS code" in record type '20'

#### Changes in version 4.2

These entries highlight changes made since the last release of this document.  This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 4.1 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 4.1 of this Technical Specification Document do not need to use this change log.

##### General

1. Section 2.8: Adding of Field ID 68 "Filler" in record type '30'

Report a problem or mistake on this page

Date modified:
:   2022-05-25