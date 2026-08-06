# Standardized Institutions Credit Monitoring Data Call (BH)

Information

Type of document

Technical specification

Industry

Deposit-taking institutions

Return

Standardized Institutions Credit Monitoring Data Call (BH)

Last updated

August 2017

Version

2.2

Table of contents

## Return file

[BH - Sample return (XLS, 2.33 MB)](/sites/default/files/import-media/data_and_forms/sample-return/2023-03/en/BH.xls) [BH - Data definitions (XLS, 3.6 MB)](/sites/default/files/import-media/data_and_forms/data-definitions/2023-08/en/scmd_dd.xls) [BH - Validation rules (XLSX, 104.51 KB)](/sites/default/files/documents/bh-validation-en.xlsx "bh-validation-en.xlsx")

## Technical specification

**For data submissions effective Q1 2018**

### 1. Introduction

OSFI has specified a return for the Standardized Institutions Credit Monitoring data call. This return must be submitted to OSFI through the Regulatory Reporting System (RRS). The data definitions for the return are found in [1] and this document specifies the technical file layout and format for that file, as well as validation rules and associated errors and warnings. Note that the technical specification document should serve as the primary guideline whenever it is not completely 'in-synch' with the data definitions document [1].

#### 1.1. Bibliography

[1] OSFI, "Credit Monitoring Data Call; Business and Data Definitions, Standardized Approach", Unclassified OSFI Publication.

### 2. Basic Concepts and Terms

In this section, we explain a number of concepts and terms related to the way that Return data is organized within a Return data file. We begin with a description of "information categories", "dimensions" and "measurement records". Then these concepts are related to "record structures", which specify the set of fixed length measurement records that you will provide in your Return data file.

#### 2.1. Information Categories and Information Dimensions

OSFI is responsible for collecting and evaluating several general categories of information that are indicators of a financial institution's credit risk exposure. Each information category is defined by a set of information dimensions and measurements.

Taking an example from the Wholesale Portfolio Data schedule (i.e., the "Wholesale Schedule 2" worksheet in [1]):

* Data values for the set of measures, "Authorized", "Outstandings", "Write Offs", "Recoveries", "Individual Allowances for Credit Losses", "Individual Provisions for Credit Losses", "Credit Impaired Loans and Acceptances", "Additions to Credit Impaired Loans and Acceptances", "Credit Impaired Loans and Acceptances Returned to Accrual Status", "Collective Allowances for Credit Losses", "Other Changes in Credit Impaired Loans and Acceptances", "Collective Provisions for Credit Losses" and "Other Changes in Allowances for Credit Losses" will be collected for the information categories given by the single dimension, Wholesale Exposure Class.
* For the information category identified by the two dimensions, Geography and Wholesale Exposure Class, data will be collected for the single measurement, "Outstandings".
* Similarly, the single measurement, "Outstandings", will be collected for the information category given by the two dimensions, Industry Group and Wholesale Exposure Class.

The information categories and dimensions for this Return are fully detailed in Section 4, "Extract File Requirements".

#### 2.2. Measurement Records and Key Values

The individual dimensions that define an information category each have a set of associated "key values". For example, in the Wholesale Portfolio Data schedule, the Industry Group dimension has key values that represent categories of industries (e.g., "Agriculture", "Capital Goods", "Communications", etc.), while the Wholesale Exposure Class dimension has key values that represent classes of wholesale credit risk exposure (e.g., "Total Wholesale", "Sovereign", "Bank", "Other Corporate Excluding SME", etc.). The dimensions and associated key values for the Return associated with this document are described in Section 4.4, "Dimension Types".

OSFI requires that measurement data be reported for all valid combinations of these key values. Consequently, you will provide a "measurement record" (that contains reported data values for each measurement) for each valid combination of key values in an information category and for every information category. Note that the types of measurements that are reported for one information category may be different than those that are reported for another information category.

In more concrete terms, when you prepare a Return data file, you will report your data as a set of fixed-length, 380-character measurement records. Each record is separated from the next in the text data file by an ASCII carriage return (CR) character and line feed (LF) character (i.e., each record is on a separate line of the file). The measurement records in the data file will include a set of records for each information category, as described by the record structures introduced in Section 2.3, below. The measurement records for a particular information category will include one record for every valid combination of key values associated with dimensions in that information category. All the measurement records for a given information category will provide data values for the same types of measurements.

As an example, consider the Retail Portfolio Data schedule (i.e., the "Retail Schedule 1" worksheet in [1]):

* For the first information category defined by the single dimension, Retail Exposure Class, in Record Type 010, you will provide a measurement record for each of 11 dimension values (i.e., including totals and sub-totals). Each measurement record will contain data values for 9 measurements: "Authorized", Outstandings", "Write Offs", "Recoveries", "Individual Allowances for Credit Losses", "Individual Provisions for Credit Losses" and "Credit Impaired Loans and Acceptances", "Additions to Credit Impaired Loans and Acceptances", "Credit Impaired Loans & Acceptances Returned to Accrual Status".
* For the second information category defined by the single dimension, Retail Exposure Class, in Record Type 015, you will provide one measurement record for the grand total dimension value, "Total Retail". This record will contain values for the four measurements, "Collective Allowances for Credit Losses", "Collective Provisions for Credit Losses", "Other changes in Credit Impaired Loans and Acceptances", "Other Changes in Allowance for Credit Losses".
* When you report on the information category defined by the dimensions, Geography and Retail Exposure Class, in Record Type 020 (having respectively 18 and 8 key values), you will provide 144 measurement records – one for every combination of key values (i.e., 18 × 8 = 144 combinations). Each of these measurement records will provide a data value for the single measurement, "Outstandings".
* For the remaining two Retail information categories you will report 7 × 7 = 49 records (dimensions Delinquency Buckets and Retail Exposure Class, in Record Type 030) and 2 × 8 = 16 records (dimensions Securitization and Retail Exposure Class, in Record Type 040) respectively. All of these records will provide values for the single measurement, "Outstandings".

In a similar fashion, you will provide measurement records for each of the remaining information categories in the Return. The set of records that you must provide is fully determined by record structures, a concept that is introduced in Section 2.3, below.

#### 2.3. Measurement Records are specified by Record Structures

Return data files typically contain hundreds, or thousands of measurement records. Consequently, it is not practical to enumerate each individual record in this specification document. Instead, we will define a descriptive "record structure" for each information category. A record structure contains all the information about dimensions, key values and measurements that are needed to specify the full set of measurement records for an information category.

Section 3, Understanding Record Structures, will provide a more complete explanation of how to read and interpret a record structure. See Section 4.5, Record Structures, below, for a complete inventory of the record structures for this return type.

### 3. Understanding Record Structures

#### 3.1. The Format of a Measurement Record

Each line in the ASCII data file has a fixed length of 380 characters and represents one physical measurement record in your Return. The first part of this record, called the "Record Descriptor", identifies the information category dimensions and combination of key values that the record addresses. The second part of the record, called the "Measurement Segment", provides data values for each measurement associated with the information category.

In this Return, the decomposition of a measurement record into its Record Descriptor and Measurement Segment by character offsets is as follows:

Example Measurement Record Format

| start | end | Length | Measurement record |
| --- | --- | --- | --- |
| 1 | 27 | 27 | **Record Descriptor** |
| 28 | 370 | 343 | **Measurement Segment** |
| 371 | 378 | 8 | **Sequential Row Counter** |
| 379 | 380 | 2 | **CR + LF** |

Notice that an 8-character sequential row counter follows the Measurement Segment. This integer counter increases by 1 for each measurement record, from the first record in the file to the last. The row counter can be used to reconstruct the file order during downstream processing.

Finally, each measurement record terminates with carriage return and line feed characters.

#### 3.2. The Format of a Record Descriptor

To facilitate the data validation process, Record Descriptors begin with a three-character "Record Type" field that identifies the information category that the measurement record is for. The list of Record Types is given in Section 4.3 Record Types.

In addition, each Record Descriptor contains one four-character key value field for every dimension, including those dimensions that do not apply to the information category of the measurement record. Alpha-numeric codes are used to represent a dimension's key values. The list of the dimensions for the Return and each dimension's key values are given in Section 4.4 Dimension Types.

In this return, the mapping of a Record Descriptor into its constituent fields (where the possible dimensions are Industry Group, Geography, Retail Exposure Class, Securitization, Delinquency Bucket and Wholesale Exposure Class) is given as follows:

Example Record Descriptor Format

| start | end | Length | Data field |
| --- | --- | --- | --- |
| 1 | 3 | 3 | **Record Type** |
| 4 | 7 | 4 | **Industry Group** |
| 8 | 11 | 4 | **Geography** |
| 12 | 15 | 4 | **Retail Exposure Class** |
| 16 | 19 | 4 | **Securitization** |
| 20 | 23 | 4 | **Delinquency Bucket** |
| 24 | 27 | 4 | **Wholesale Exposure Class** |

The detailed formats of the Record Descriptors used in **this** Return are given by the record structures in Section 4.5, below.

#### 3.3. Identifying Dimensions and Valid Key Values

Each record structure identifies the dimensions that determine the number of measurement records needed for a given information category, as well as the dimensions that are not important for that category.

Within each record structure, special key values identify dimensions that do not apply to the information category. A range of valid key values is also specified for all other dimensions. Providing key values for all dimensions in every measurement record in this way ensures that all measurement records in the Return data file have Record Descriptors of the same length. This facilitates downstream processing of your Return.

You will provide a 380-character measurement record for every combination of valid key values specified in the record structure.

#### 3.4. The Format of a Measurement Segment

The Measurement Segment in the second part of a measurement record contains data fields for each of the measurements that you will report for the particular combination of key values given in the corresponding Record Descriptor. The Measurement Segment also contains a "filler" field that pads the measurement segment with space characters to the 370th character of the measurement record.

For example, the mapping of a Measurement Segment into its constituent 15 character data fields, for a Wholesale Portfolio Data schedule information category with the measurements "Authorized", "Outstandings", "Write Offs", "Recoveries", "Individual Allowances for Credit Losses", "Individual Provisions for Credit Losses", "Credit Impaired Loans and Acceptances", "Additions to Credit Impaired Loans and Acceptances" , "Credit Impaired Loans and Acceptances Returned to Accrual Status" and "Other changes in Credit Impaired Loans and Acceptances" is as follows:

Example Measurement Segment Format

| start | end | Length | Data field |
| --- | --- | --- | --- |
| 28 | 42 | 15 | **Authorized** |
| 43 | 57 | 15 | **Outstandings** |
| 58 | 72 | 15 | **Write Offs** |
| 73 | 87 | 15 | **Recoveries** |
| 88 | 102 | 15 | **Individual Allowances for Credit Losses** |
| 103 | 117 | 15 | **Individual Provisions for Credit Losses** |
| 118 | 132 | 15 | **Credit Impaired Loans and Acceptances** |
| 133 | 147 | 15 | **Additions to Credit Impaired Loans and Acceptances** |
| 148 | 162 | 15 | **Credit Impaired Loans and Acceptances Returned to Accrual Status** |
| 163 | 177 | 15 | **Other changes in Credit Impaired Loans and Acceptances** |
| 178 | 370 | 193 | **Filler** |

The record structure for a particular information category will specify the measurements that are being reported in all measurement records for that information category, as well as their field lengths.

#### 3.5. Header and Footer Records

Header and footer records are used to mark the beginning and end of a Return data file and provide meta-information about the Return itself. These records are also provided as 380-character lines and they follow the same general format as a measurement record. However, the dimension keys in the header and footer Record Descriptors are set to special values that indicate that the dimensions are not used. The Measurement Segments in the header and footer records contain the meta-data for the Return.

We will use the terms "data record" and "record" in the sequel to refer more generally to both measurement records and header and footer records.

The first row of the extract file must be a header record with Record Type "000" and the last one must be a footer record with Record Type "999". They must be the only "000" and "999" records in the file.

Apart from the header and footer, all the other (measurement) records may be in any order.

### 4. Extract File Requirements

The following sections describe the Return extract file layout for RRS Delivery. Throughout the extract file layout documentation, all primary key fields are printed in bold type and listed in the order in which they appear in the key.

#### 4.1. File Type and Naming Convention

Data destined for the Standardized Institutions Credit Monitoring database will be a fixed width text file, 380 bytes per line including a carriage return (CR) and line feed (LF) as record delimiters. Fields which are empty (i.e., have no value) must be indicated by blank spaces if data type is alphanumeric or zeros if data type is numeric. Mandatory fields must be populated as indicated in [1].

The fixed width text file will have the naming convention of FI\_BH\_MMYYYY.DAT, where FI represents the Institution ID (provided by OSFI), BH is a fixed string representing the two character identifying code for this return, MM represents the month and YYYY represents the year of the reporting date of information.

#### 4.2. File Structure

As previously described, the first row of the extract file must be a header record ("000") and the last one must be a footer record ("999"), and they must be the only "000" and "999" records in the file. Apart from the header and footer, all the other (measurement) records may be in any order.

Within the definitions for each record structure, the combination of all key values (Record Type, BIRR Type, Industry Type, Geography Type, Risk Rating System, and Exposure Class Type) must only be represented once in the Return data file and indicated with one measurement record (if supported by the data.)

#### 4.3. Record Types

Each line of your Return data file is one of the following types of data record: a header record, one of several different types of measurement record, or a footer record. The downstream Return-processing software must be able to identify the type of record in order to parse each into its constituent fields. To facilitate this process, every measurement record begins with a three-character "Record Type" field that identifies the record structure (and, therefore, the set of fields) that the measurement record provides data for. The following Record Types – one for each information category – have been defined for this Return:

Descriptions of record types

| Record Type | Description |
| --- | --- |
| 000 | Header Record |
| 010 | Retail Portfolio Performance |
| 015 | Retail Portfolio Performance; Collective Allowances & Provisions |
| 020 | Retail Outstandings by Geography |
| 030 | Retail Delinquency Buckets |
| 040 | Retail Outstandings by Securitization |
| 050 | Wholesale Portfolio Performance |
| 055 | Wholesale Portfolio Performance; Collective Allowances & Provisions |
| 060 | Wholesale Outstandings by Geography |
| 070 | Wholesale Outstandings by Industry |
| 080 | Retail CREF |
| 085 | Retail CREF; Authorized |
| 090 | Wholesale CREF |
| 095 | Wholesale CREF; Authorized |
| 999 | Footer Record |

#### 4.4. Dimension Types

In order to control the number of dimensions, to reduce errors and to support data validation, this return uses key values rather than the dimension names directly.

The Dimensions and key value ranges referenced in this Return are:

Key values for each dimension name

| Key Values | Dimension Name |
| --- | --- |
| 0001, 0010 – 0025, 0099 | Industry Group Type |
| 0300 – 0315, 0319, , 0399 | Geography Type |
| 0500 – 0518, 0599 | Retail Exposure Class Type |
| 0600, 0601, 0699 | Securitization Type |
| 0800 – 0805, 0899 | Delinquency Bucket Type |
| 1800 – 1803, 1810, 1817 – 1822, 1899 | Wholesale Exposure Class Type |

The remainder of this section enumerates the mapping between dimension keys and dimension value names. The roll-up hierarchy for each dimension is indicated by the indentation of dimension values within each table below. The roll-ups are also summarized in Section 5.4.2.

Industry Group Primary Key

| Numeric Key | Dimension Value |
| --- | --- |
| 0001 | Total Industry Group |
| 0010 | Communications |
| 0011 | Metals and Mining |
| 0012 | Resources & Basic Materials |
| 0013 | Transportation |
| 0014 | Agriculture |
| 0015 | Energy |
| 0016 | Financial Services |
| 0017 | Government & Sovereign |
| 0018 | Life Sciences |
| 0019 | Real Estate |
| 0020 | Manufacturing |
| 0021 | Services |
| 0022 | Technology |
| 0023 | Capital Goods |
| 0024 | Retail and Wholesale |
| 0025 | Other |
| 0099 | No Industry Group |

Geography Primary Key

| Numeric Key | Dimension Value |
| --- | --- |
| 0300 | Total Geography |
| 0301 | Total Canada |
| 0302 | Alberta |
| 0303 | British Columbia |
| 0304 | Manitoba |
| 0305 | New Brunswick |
| 0306 | Newfoundland and Labrador |
| 0307 | Northwest Territories |
| 0308 | Nova Scotia |
| 0309 | Nunavut |
| 0310 | Ontario |
| 0311 | Prince Edward Island |
| 0312 | Quebec |
| 0313 | Saskatchewan |
| 0314 | Yukon |
| 0315 | United States |
| 0319 | All Other |
| 0399 | No Geography |

Retail Exposure Class Primary Key

| Key Value | Description |
| --- | --- |
| 0500 | Total Retail |
| 0501 | Mortgage and HELOC |
| 0502 | Mortgage |
| 0510 | Residential Mortgage - CMHC Insured |
| 0511 | Residential Mortgage - Other Insured |
| 0512 | Residential Mortgage - Non-Insured |
| 0503 | HELOC |
| 0504 | Total Credit Card and LOC |
| 0505 | Credit Card |
| 0506 | LOC |
| 0507 | Other Retail |
| 0508 | SME Treated as Retail |
| 0513 | Non-CRE - SME Retail |
| 0514 | CRE - SME Retail |
| 0515 | Total Land-Banking - SME Retail |
| 0516 | Interim Finance - SME Retail |
| 0517 | Rev. Gen. Multi-Unit Residential - SME Retail |
| 0518 | Rev. Gen. - Other - SME Retail |
| 0509 | Other Retail Excluding SME |
| 0599 | No Exposure Class |

Securitization Primary Key

| Key Values | Description |
| --- | --- |
| 0600 | Before Securitization |
| 0601 | After Securitization |
| 0699 | No Securitization |

Delinquency Buckets Primary Key

| Key Values | Description |
| --- | --- |
| 0800 | Total Delinquency Buckets (Including Current) |
| 0801 | Current |
| 0802 | 1 to 30 days |
| 0803 | 31 to 60 days |
| 0804 | 61 to 90 days |
| 0805 | Over 90 days |
| 0899 | No Delinquency Bucket |

Wholesale Exposure Class Primary Key

| Key Values | Description |
| --- | --- |
| 1800 | Total Wholesale |
| 1801 | Total Corporate |
| 1810 | Other Corporate Excluding SME |
| 1817 | Non-CRE - Corporate Excl. SME |
| 1818 | CRE - Corporate Excl. SME |
| 1819 | Total Land-Banking - Corporate Excluding SME |
| 1820 | Interim Finance - Corporate Excluding SME |
| 1821 | Rev. Gen. Multi-Unit Residential - Corporate Excluding SME |
| 1822 | Rev. Gen. - Other - Corporate Excluding SME |
| 1802 | Bank |
| 1803 | Sovereign |
| 1899 | No Exposure Class |

#### 4.5. Record Structures

This section describes the record structures allowed in this return. Within the record structure layouts in this section, the first column refers to the Field ID, which should be used to link to the document [1]. The second and third columns refer to start and end positions of that field within the record. The following columns are length of the field, field name, "M" which refers to mandatory field, and finally the "notes" column, which provides extra information to assist with the planning of extracts and describes what field format/mask should be used. Bold field names indicate keys within the Record Descriptor of the measurement record.

The order of the fields in a measurement record must be the same as the order in which they are specified within the record structures. Field values must be formatted as specified in the record structures layouts.

The first 3 characters must describe the Record Type mapping for each line in the Return data file. Each record structure has been assigned a unique Record Type key value. These are enumerated in Section 4.3.

Note that key values of the form xx99 have been specified to indicate when there is no key value for the dimension in this record. Key values for all dimensions are enumerated in section 4.4.

##### Header Record (000)

The header record is a quality control mechanism that uniquely identifies each file sent to OSFI (i.e. who sent the file, the reporting date, the file name, etc). The information contained in the header field is checked against the file name and the actual details of the file to ensure that the file received by OSFI has not been corrupted.

The record structure layout of the header record is detailed below:

Record structure layout of the header record (000)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "000" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099" |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 0 | 28 | 31 | 4 | Institution ID | ✓mandatory | pic(X) - Right-padded with spaces |
| 28 | 32 | 39 | 8 | Reporting date of information | ✓mandatory | pic(9) - Format: YYYYMMDD |
| - | 40 | 46 | 7 | Return Name | ✓mandatory | pic(X) - Fixed string, BH, Right-padded with spaces |
| - | 47 | 52 | 6 | Return file layout version | ✓mandatory | pic(X) - Fixed string "02.0.0" |
| - | 53 | 370 | 318 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail Portfolio Performance (010)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for each Retail Exposure Class identified in the Notes column:

Record structure layout of the retail portfolio performance (010)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "010" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "0500", "0503", "0505", "0506" and  "0508" to "0514" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 1 | 28 | 42 | 15 | Authorized | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 2 | 43 | 57 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 3 | 58 | 72 | 15 | Write Offs | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 4 | 73 | 87 | 15 | Recoveries | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 5 | 88 | 102 | 15 | Individual Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 6 | 103 | 117 | 15 | Individual Provisions for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 7 | 118 | 132 | 15 | Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 8 | 133 | 147 | 15 | Additions to Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 9 | 148 | 162 | 15 | Credit Impaired Loans and Acceptances Returned to Accrual Status | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 163 | 370 | 208 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail Portfolio Performance; Collective Allowances & Provisions (015)

The record structure layout for this information category is detailed as follows. A single measurement record must be completed for the Retail Exposure Class total identified in the Notes column:

Record structure layout of the retail portfolio performance; collective allowances & provisions (015)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "015" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0500" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 10 | 28 | 42 | 15 | Collective Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 11 | 43 | 57 | 15 | Collective Provisions for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 12 | 58 | 72 | 15 | Other changes in Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 13 | 73 | 87 | 15 | Other changes in Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 88 | 370 | 283 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail Outstandings by Geography (020)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Retail Exposure Class and Geography, as identified in the Notes column:

Record structure layout of the retail outstandings by geography (020)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "020" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed Strings "0300" to "0315", and "0319" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "0503", "0505", "0506" and  "0509" to "0513" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail Delinquency Buckets (030)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Retail Exposure Class and Delinquency Bucket, as identified in the Notes column:

Record structure layout of the retail delinquency buckets (030)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "030" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0503", "0505", "0506" and  "0509" to "0512" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed Strings "0800" to "0805" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail Outstandings by Securitization (040)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Retail Exposure Class and Securitization Category, as identified in the Notes column:

Record structure layout of the retail outstandings by securitization (040)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "040" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0503", "0505", "0506" and  "0509" to "0512" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed Strings "0600" and "0601" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale Portfolio Performance (050)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for each Wholesale Exposure Class identified in the Notes column:

Record structure layout of the wholesale portfolio performance (050)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "050" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "1800", "1802", "1803", "1817 " and "1818" |
| 1 | 28 | 42 | 15 | Authorized | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 2 | 43 | 57 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 3 | 58 | 72 | 15 | Write Offs | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 4 | 73 | 87 | 15 | Recoveries | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 5 | 88 | 102 | 15 | Individual Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 6 | 103 | 117 | 15 | Individual Provisions for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 7 | 118 | 132 | 15 | Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 8 | 133 | 147 | 15 | Additions to Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 9 | 148 | 162 | 15 | Credit Impaired Loans and Acceptances Returned to Accrual Status | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 12 | 163 | 177 | 15 | Other Changes in Credit Impaired Loans and Acceptances | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 178 | 370 | 193 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale Portfolio Performance; Collective Allowances & Provisions (055)

The record structure layout for this information category is detailed as follows. A single measurement record must be completed for the Wholesale Exposure Class identified in the Notes column:

Record structure layout of the wholesale portfolio performance; collective allowances & provisions (055)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "055" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1800" |
| 10 | 28 | 42 | 15 | Collective Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 11 | 43 | 57 | 15 | Collective Provisions for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| 13 | 58 | 72 | 15 | Other changes in Allowances for Credit Losses | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 73 | 370 | 298 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale Outstandings by Geography (060)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Wholesale Exposure Class and Geography, as identified in the Notes column:

Record structure layout of the wholesale outstandings by geography (060)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "060" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed Strings "0300" to "0315", "0319" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "1802", "1803" and "1817" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale Outstandings by Industry (070)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for the specified range of key values for Geography and the single Wholesale Exposure Class total, as identified in the Notes column:

Record structure layout of the wholesale outstandings by industry (070)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "070" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed strings "0001" and "0010" to "0025" |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1800" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail CREF (080)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Retail Exposure Class and Geography, as identified in the Notes column:

Record structure layout of the retail CREF (080)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "080" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed Strings "0300" to "0315" and "0319" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "0515" to "0518" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Retail CREF; Authorized (085)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for the specified range of key values for Retail Exposure Class and the single Geography total, as identified in the Notes column:

Record structure layout of the retail CREF; authorized (085)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "085" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0300" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "0515" to "0518" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| 1 | 28 | 42 | 15 | Authorized | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale CREF (090)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for all combinations of the specified range of key values for Wholesale Exposure Class and Geography, as identified in the Notes column:

Record structure layout of the wholesale CREF (090)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "090" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed Strings "0300" to "0315" and "0319" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "1819" to "1822" |
| 2 | 28 | 42 | 15 | Outstandings | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Wholesale CREF; Authorized (095)

The record structure layout for this information category is detailed as follows. A new measurement record must be completed for the specified range of key values for Wholesale Exposure Class and the single Geography total, as identified in the Notes column:

Record structure layout of the wholesale CREF; authorized (095)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "095" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0300" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed Strings "1819" to "1822" |
| 1 | 28 | 42 | 15 | Authorized | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 43 | 370 | 328 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Footer Record (999)

The record structure layout of the Footer Record is detailed below.

Record structure layout of the footer record (999)

| Field ID | Start | End | Length | Field Name | M | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Record Type** | ✓mandatory | pic(9) – Fixed string "999" |
| - | 4 | 7 | 4 | **Industry Group** | ✓mandatory | pic(9) – Fixed string "0099 " |
| - | 8 | 11 | 4 | **Geography** | ✓mandatory | pic(9) – Fixed String "0399" |
| - | 12 | 15 | 4 | **Retail Exposure Class** | ✓mandatory | pic(9) – Fixed String "0599" |
| - | 16 | 19 | 4 | **Securitization** | ✓mandatory | pic(9) – Fixed String "0699" |
| - | 20 | 23 | 4 | **Delinquency Bucket** | ✓mandatory | pic(9) – Fixed String "0899" |
| - | 24 | 27 | 4 | **Wholesale Exposure Class** | ✓mandatory | pic(9) – Fixed String "1899" |
| - | 28 | 36 | 9 | Number of body records | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 37 | 48 | 12 | File Size (Bytes) | ✓mandatory | pic(9) – no commas/dots, left-padded with zeros |
| - | 49 | 108 | 60 | File Name | ✓mandatory | pic(X) - Fixed string, Name of this return data file, Right-padded with spaces |
| - | 109 | 116 | 8 | File Creation Date | ✓mandatory | pic(9) - Format: YYYYMMDD |
| - | 117 | 370 | 254 | Filler | ✓mandatory | pic(X) - Blank spaces |
| - | 371 | 378 | 8 | Sequential row counter | ✓mandatory | pic(9) - Left-padded with zeros |
| - | 379 | 380 | 2 | CR + LF | ✓mandatory | pix(X) - Hexadecimal: 0D + 0A |

##### Additional Important Notes

The sequential row counter field that appears in every record must start at "00000001" in the header record and be incremented by 1 in every row. Therefore, the footer will show the total number of records in the file.

### 5. Data Validation Rules

#### 5.1. Error Handling

The error handling philosophy is to trap the maximum number of possible errors and warnings. The file will be entirely rejected if errors are detected and no data will be uploaded to the database. Warnings are irrelevant errors that will not stop the database from accepting the file.

#### 5.2. Pre-processing Checks

Pre-processing is performed to ensure that the extract files received are formatted correctly, and that the header and footer records match the actual contents of the file. A program checks extract files for header and formatting errors. The following pre-processing checks are made:

1. Each record in the file has valid record types
2. Each record in the file is 378 characters plus 2 ASCII characters (Carriage Return and Line Feed)
3. Each record has the correct number of fields for its record type
4. Each record has a sequential counter that starts at 00000001 at the header record and is incremented by 1 in each record in the file
5. The type of return exactly matches the information in the header record
6. The name of the data file exactly matches the information in the footer record
7. The extension of file is \*.DAT
8. The institution in the file name and header record is a valid Bank of Canada code (provided by OSFI)
9. The composite key given by each Record Descriptor is unique for all records in the data file.
10. Every submitted field value should be formatted according to the specifications. (E.g. left-padded with spaces is not acceptable if "left-padded with zeros" was specified, even if the "meaningful" part of the field is identical.)

#### 5.3. Field Value Rules

Field value rules ensure that the data given in each field conforms to the data types described in [1]. The following general rules shall be applied in your return data file. Other field value rules may be given in the data definitions document, [1].

##### 5.3.1. Dollar Amount Rules

All dollar amounts are reported and validated according to the following rules:

1. All dollar amounts shall be reported in units of "thousands of dollars".
2. All dollar amounts shall be rounded to the nearest thousand dollars.
3. Dollar amounts shall only contain numeric digits (with the exception of the negative sign). No comma or decimal separators shall be used.
4. Negative dollar amounts should be reported with the hyphen sign before the first "meaningful" digit, in other words report the negative number left-padded with zeros.
5. All dollar amounts shall be reported in a 15-character field that is left padded with zeros.

For example, $2,183,624.68 will be reported as the string 000000000002184, and -$34,892.45 will be reported as the string 000000000000-35

##### 5.3.2. Date Value Rules

Date values are reported and validated according to the following rules:

1. The width of a date field is 8 characters.
2. Dates shall only contain numeric digits (e.g., alphabetic month names, special characters or spaces are not allowed).
3. Dates shall follow the format YYYYMMDD, where YYYY is the year, MM is the month and DD is the day.

For example, the string 20100608 represents June 8th, 2010.

#### 5.4. Aggregation Rules

In some cases, the dollar measurements reported for a given key value in a dimension may be related in a hierarchical fashion to these measurements for other key values in the same dimension. The rules below describe how these measurements are related and validated in your return.

##### 5.4.1. Aggregation By Summation

Currently, the dollar measurements reported for higher-level key values in a dimensional hierarchy are actually the summation of the corresponding measurements reported for lower level key values. Summing lower level key value measurements to produce higher-level key value measurements is referred to as "aggregating" the measurements (or, alternatively, "rolling up" the measurements) from one level of the dimension to another.

Aggregate values for every measure at each level should be calculated in an "intelligent way", meaning the calculation follows the natural aggregation pattern of that particular measure and the result truly reflects the measurement value at the higher level – independent of how the supporting values are reported.

Note that there is a 5% tolerance level defined (to account for potential rounding issues), however, a discrepancy of more than 5% will generate an error message and the data will be rejected. The 5% tolerance is applied the following way: the sum of the details should always fall within the 95% and the 105% range of the total value.

###### Example of Aggregation by Summation

As an example, consider the Geography dimension. In this dimension, measurements for key value 0300 (Total Geography) are aggregated as the sum of the corresponding measurements for the key values 0301, 0315, 0319 representing countries (Total Canada, United States and All Other countries respectively). Similarly, measurements for the key value 0301 (Total Canada) are aggregated as the sum of the corresponding measurements for the province and territory key values 0302, 0303, up to 0314 (representing Alberta, British Columbia, etc. up to Yukon Territory).

To continue the example, further consider the case where a record structure requires that an additive measure ABC is reported over combinations of key values of the Geography and Retail Exposure Class dimensions. If we look at all the records that have the same key value for Retail Exposure Class (say, 0510, representing "Residential Mortgage - CMHC Insured"), then the value of measurement ABC in the record with Geography key value 0300 will equal the sum of the ABC measurements in all the records with Geography key values 0301, 0315 and 0319. Similarly, at the next level down the aggregation hierarchy, the value of measurement ABC in the record with Geography key value 0301 will equal the sum of the ABC measurements in all the records with Geography key values 0302, 0303, up to 0314.

###### Variations on Aggregation by Summation

Some record structures might require that you only report the total measurements, and not the lower level measurements. In this case, the aggregation between these levels cannot be validated by OSFI.

In other cases a record structure will only ask you to report measurements for lower-level key values, and will not ask for the total key values at the next higher value of the hierarchy. In this case, the total values are not validated by OSFI.

#### 5.4.2. Aggregation by Summation Rules for Dimensions Used in this Return

The following aggregation-by-summation rules are used for dimensions that appear in this return data file. In these rule descriptions, the term "measurements" refers to dollar measurements that are additive by nature for the specified dimension.

Industry Group Aggregation Rules
:   Measures for key value 0001 (Total Industry Group) are the sum of measures for consecutive key values 0010 to 0025 (16 Industry Group classifications).

Geography Aggregation Rules
:   Measures for key value 0301 (Total Canada) are the sum of measures for consecutive key values 0302 to 0314 (the provinces and territories).
:   Measures for key value 0300 (Total Geography) are the sum of measures for key values 0301 (Total Canada), 0315 to 0319 (geographic regions, other than Canada).

Securitization Aggregation Rules
:   No rule is defined, as this dimension does not currently aggregate.

Delinquency Bucket Aggregation Rules
:   Measures for key value 0800 (Total Current and Delinquency Buckets) are the sum of measures for consecutive key values 0801 to 0805 (known bucket ranges).

Retail Exposure Class Aggregation Rules
:   Total measure values and corresponding lower-level measure values are not **both** reported for Retail Exposure Classes in this return. Therefore, aggregation rules are not applied to measures across Retail Exposure Class by OSFI. However, the following rules do express a **purely conceptual** aggregation hierarchy for Retail Exposure Classes.
:   Measures for key value 0502 (Mortgage) are the sum of measures for consecutive key values 0510 (Residential Mortgage - CMHC Insured), 0511 (Residential Mortgage - Other Insured) and 0512 (Residential Mortgage - Non-Insured).
:   Measures for key value 0501 (Mortgage and HELOC) are the sum of measures for consecutive key values 0502 (Mortgage) and 0503 (HELOC).
:   Measures for key value 0504 (Total Credit Card and LOC) are the sum of measures for consecutive key values 0505 (Credit Card) and 0506 (LOC).
:   Measures for key value 0514 (CRE - SME Retail) are the sum of measures for consecutive key values 0515 (Total Land-Banking - SME Retail), 0516 (Interim Finance - SME Retail), 0517 (Re. Gen. Multi-Unit Residential - SME Retail) and 0518 (Rev. Gen. - Other - SME Retail).
:   Measures for key value 0508 (SME Treated as Retail) are the sum of measures for key values 0513 (Non-CRE - SME Retail) and 0514 (CRE - SME Retail).
:   Measures for key value 0507 (Other Retail) are the sum of measures for consecutive key values 0508 (SME Treated as Retail) and 0509 (Other Retail Excl. SME).
:   Measures for key value 0500 (Total Retail) are the sum of measures for key values 0501 (Mortgage and HELOC), 0504 (Total Credit Card and LOC) and 0507 (Other Retail).

Wholesale Exposure Class Aggregation Rules
:   Total measure values and corresponding lower-level measure values are **not** both reported for Wholesale Exposure Classes in this return. Therefore, aggregation rules are not applied to measures across Retail Exposure Class by OSFI. However, the following rules do express a **purely conceptual** aggregation hierarchy for Wholesale Exposure Classes.
:   Measures for key value 1818 (CRE - Corporate Excl. SME) are the sum of measures for consecutive key values 1819 (Total Land-Banking - Corporate Excluding SME), 1820 (Interim Finance - Corporate Excluding SME), 1821 (Re. Gen. Multi-Unit Residential - Corporate Excluding SME) and 1822 (Rev. Gen. - Other - Corporate Excluding SME).
:   Measures for key value 1810 (Other Corporate Excluding SME) are the sum of measures for key values 1817 (Non-CRE - Corporate Excl. SME) and 1818 (CRE - Corporate Excl. SME).
:   Measures for key value 1801 (Total Corporate) are the same as measures for consecutive key values 1810 (Other Corporate Excluding SME).
:   Measures for key value 1800 (Total Wholesale) are the sum of measures for key values 1801 (Total Corporate), 1802 (Bank) and 1803 (Sovereign).

#### 5.5. Data Redundancy Rules

There are several measures in the return that are reported in more than one record type. It is expected that the values reported in each type of record are consistent for each such measure. E.g. the Outstandings measure value reported in Record Type 050, for a given Wholesale Exposure Class dimension key value, should be equal to the measure value reported in Record Type 060 for the same Wholesale Exposure Class dimension key value and the Geography key value 0300 (Total Geography). The same expectation applies when comparing the total of reported Outstandings measure values (summed across Wholesale Exposure Class dimension key values) for Record Type 050 with the total of reported Outstandings measure values (summed across Industry Group key values) for Record Type 070.

Note that a tolerance of 5% is accepted for any such data redundancy (to account for potential rounding issues), however, a discrepancy of more than 5% will generate an error message and the data will be rejected.

The 5% tolerance is applied the following way: for any two comparable numbers (described in the equations below) the ratio of the two (in either direction) should always fall within the range of 0.95 and 1.05.

This section describes the "Redundancy Rules" that apply in this Return. The following notation will be used to refer to a specific value for measure, m, in records with record type 0XX, and dimension key values dimension\_key1, dimension\_key2, etc.:

Math formula 1

![Math formula 1. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math1.gif)

Text version

RT xx   m,dimension\_key1,dimension\_key2,etc.

##### 5.5.1. Data Redundancy Group 1

Data Redundancy Group 1 includes the "Redundancy Rules" that apply to the following record types in the "Retail Portfolio Data" schedule of [1]: 010, 020, 030 and 040.

![Retail Portfolio Data - Math formula 1. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math2.gif)

Text version

1.     RT 10   Outstandings, Ret.Ex.C.    =    RT 20   Outstandings,0300,Ret.Ex.C.

Retail Portfolio Data - Math formula 1: Where "Ret.Ex.C" refers to any valid Retail Exposure Class dimension key that applies to both record types and 0300 is the total key for the Geography dimension.

![Retail Portfolio Data - Math formula 2. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math3.gif)

Text version

2.     RT 10   Outstandings, Ret.Ex.C.    =    RT 30   Outstandings,0800,Ret.Ex.C.

Retail Portfolio Data - Math formula 2: where "Ret.Ex.C" refers to any valid Retail Exposure Class dimension key that applies to both record types and 0800 is the total key for the Delinquency Bucket dimension.

![Retail Portfolio Data - Math formula 3. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math4.gif)

Text version

3.     RT 10   Outstandings, Ret.Ex.C.    =    RT 40   Outstandings,0601,Ret.Ex.C.

Retail Portfolio Data - Math formula 3: where "Ret.Ex.C" refers to any valid Retail Exposure Class dimension key that applies to both record types and 0601 is the "After Securitization" key for the Securitization dimension.

Note: The Redundancy Group 1 Rules are only applicable to the "additive" measure, Outstandings (Field ID 2):

##### 5.5.2. Data Redundancy Group 2

Data Redundancy Group 2 includes the 'Redundancy Rules' that apply to the following record types in the "Wholesale Portfolio Data" schedule of [1]: 050, 060 and 070.

![Wholesale Portfolio Data - Math formula 1. Text version follows.](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math5.gif)

Text version

1.     RT 50   Outstandings, Who.Ex.C .    =    RT 60   Outstandings,0601,Who.Ex.C.

Wholesale Portfolio Data - Math formula 1: where "Who.Ex.C" refers to any valid Wholesale Exposure Class dimension key that applies to both record types and 0300 is the total key for the Geography dimension.

![Wholesale Portfolio Data - Formula 2](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math6.gif)

Wholesale Portfolio Data - Math formula 2: where 1800 is the total key for the Wholesale Exposure Class dimension, 'i' is a summation variable taking on the sixteen consecutive Industry Group dimension key values 0010 (Communications) to 0025 (Other) and 'e' is a summation variable taking on the six Wholesale Exposure Class dimension key values 1802 (Bank), 1803 (Sovereign), 1817 (Non-CRE - Corporate Excl. SME) and 1818 (CRE - Corporate Excl. SME).

##### 5.5.3. Data Redundancy Group 3

Data Redundancy Group 3 includes the 'Redundancy Rules' that apply to the following record types in the "Commercial Real Estate Exposure" schedule of [1]: 80, 85, 90 and 95.

![Commercial Real Estate Exposure - Math formula 1](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math7.gif)

Commercial Real Estate Exposure - Math formula 1: where 0300 is the Total Geography key for the Geography dimension, 0514 is the "CRE - SME Retail" key for the Retail Exposure Class dimension and 'e' is a summation variable taking on the four Retail Exposure Class dimension key values 0515 (Total Land-Banking - SME Retail), 0516 (Interim Finance - SME Retail), 0517 (Re. Gen. Multi-Unit Residential - SME Retail) and 0518 (Rev. Gen. - Other - SME Retail).

![Commercial Real Estate Exposure - Math formula 2](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math8.gif)

Commercial Real Estate Exposure - Math formula 2: where 0300 is the Total Geography key for the Geography dimension, 0514 is the "CRE - SME Retail" key for the Retail Exposure Class dimension and 'e' is a summation variable taking on the four Retail Exposure Class dimension key values 0515 (Total Land-Banking - SME Retail), 0516 (Interim Finance - SME Retail), 0517 (Re. Gen. Multi-Unit Residential - SME Retail) and 0518 (Rev. Gen. - Other - SME Retail).

![Commercial Real Estate Exposure - Math formula 3](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math9.gif)

Commercial Real Estate Exposure - Math formula 3: where 0300 is the Total Geography key for the Geography dimension, 1818 is the "CRE - Corporate Excl. SME" key for the Wholesale Exposure Class dimension and 'e' is a summation variable taking on the four Wholesale Exposure Class dimension key values 1819 (Total Land-Banking – Corporate Excluding SME), 1820 (Interim Finance – Corporate Excluding SME), 1821 (Re. Gen. Multi-Unit Residential - Corporate Excluding SME) and 1822 (Rev. Gen. - Other - Corporate Excluding SME).

![Commercial Real Estate Exposure - Math formula 4](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2018-12/en/scmd_ts_math10.gif)

Commercial Real Estate Exposure - Math formula 4: where 0300 is the Total Geography key for the Geography dimension, 1818 is the "CRE - Corporate Excl. SME" key for the Wholesale Exposure Class dimension and 'e' is a summation variable taking on the four Wholesale Exposure Class dimension key values 1819 (Total Land-Banking – Corporate Excluding SME), 1820 (Interim Finance – Corporate Excluding SME), 1821 (Re. Gen. Multi-Unit Residential - Corporate Excluding SME) and 1822 (Rev. Gen. - Other - Corporate Excluding SME).

NOTE: The period prior to September 1, 2008 is considered a "tolerance period". During this tolerance period, some data redundancy validation rules (described in this section), that normally produce error messages and reject return data files, will only generate warnings, allowing the file to be accepted if no other hard errors are detected.

#### 5.6. Other Business Rules

##### 5.6.1. Dollar Amounts

The Dollar Amounts validation rule section describes the "cross-measure" rules that are applicable in the return. Please, note that every comparison between measures should apply for any combination of dimension keys within the same record type and at the same hierarchical level. (In other words, all the dimension keys should be equal.) Both "cross-level" validations and "cross-record type" validations are handled in a separate section of this document. (Section 5.4 - Aggregation Rules and 5.5 - Data Redundancy Rules, respectively)

* Outstandings (ID #2) must be less than or equal to the Authorized value (ID #1) within a tolerance of 1% for Retail values and 5% for Wholesale values. Otherwise, the data will be rejected.
* Individual Provisions for Loan Losses value (ID #6) must be less than or equal to the Credit Impaired Loans and Acceptances value (ID #7) within a tolerance of 1% for both Retail and Wholesale values. Otherwise, the data will be rejected.
* Credit Impaired Loans and Acceptances value (ID#7) must be less than or equal to the Outstandings (ID #2) value with no tolerance for both Retail and Wholesale values. Otherwise, the data will be rejected.

##### 5.6.2. Negative values

Submitting negative values in the return will cause rejection, with the following exceptions: Retail and Wholesale Write offs (ID #3), Retail and Wholesale Recoveries (ID #4) and Retail and Wholesale Individual Provisions for Loan Losses (ID #6), Other Changes in Credit Impaired Loans and Acceptances (ID#12), Other Changes in Allowances for Credit Losses (ID#13), where negative values are considered acceptable under certain circumstances.

#### 5.7. Mandatory Data Elements

Mandatory fields are data points that **must** be reported by **all** Financial Institutions. Otherwise, the data will be rejected. All fields used in this return are mandatory.

#### 5.8. Error Report

If any of these validation rules fails an Error Report will be created and the input file will be rejected. The contents of the Error Report will vary depending upon the types of errors found in the input file. This report will have enough information to help troubleshoot and correct the inconsistencies. However, if the Error Report contains only Warnings, the input file will be accepted by OSFI. Please, note that you are still required to correct the erroneous/ inconsistent data (in other words to eliminate the "warnings") for the following data submission.

This report will be e-mailed to the Financial Institution in question indicating whether or not the file was successfully uploaded in the database. If problems were detected, the Error Report will be attached to this e-mail including both 'errors' and 'warnings'.

### Changes in version 2.0

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 1.0 of this document on hand when reviewing this change log. Note, that there might be a number of small, "cosmetic-type" corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 1.0 of this Technical Specification Document do not need to use this change log.

#### General

1. Renamed measurement "Specific Allowances for Loan Losses" to "Specific Allowances for **Credit** Losses" (Sections 2.1, 2.2, 3.4, 4.5)
2. Renamed measurement "Specific Provisions for **Loan** Losses" to "Specific Provisions for **Credit** Losses" (Sections 2.1, 2.2, 3.4, 4.5)
3. Renamed measurement "General Allowances" to "General Allowances for **Credit Losses"** (Sections 2.1, 2.2, 4.5)
4. Renamed measurement "Credit Impaired Loans Returned to Accrual Status" to "Credit Impaired Loans and **Acceptances** Returned to Accrual Status"
5. Remove "Unknown" values from all dimension keys – 0398 and 0898 (section 4.4, 4.5, 5.4.1, 5.4.2)
6. Added 2 exceptions for Negative rules (section 5.6.2)
   * Other Changes in Credit Impaired Loans and Acceptances
   * Other Changes in Allowances for Credit Losses
7. Deleted references to the following wholesale exposure classes (All)
   * 1809 - SMEs Treated as Corporate
   * 1811 - Non-CRE - SME Corporate
   * 1812 - CRE - SME Corporate
   * 1813 - Total Land-Banking - SME Corporate
   * 1814 - Interim Finance - SME Corporate
   * 1815 - Re. Gen. Multi-Unit Residential - SME Corporate
   * 1816 - Rev. Gen. - Other - SME Corporate

#### Section 2.2 changes

8. For record type 010, changed the number of dimension values to 11 from 9. This is the result of adding 2 exposure classes.
9. For record type 015, changed from "single" measurement to "four" measurements

#### Section 4.4 changes

10. Changed Whole Exposure Class Type Key value ranges by dropping "1809", "1811" to "1816"
11. Changed the following key descriptions in Geography Primary Key table:
    * 0306 – renamed "Newfoundland" to "Newfoundland and Labrador"
    * 0308 – renamed "Northwest Territory" to "Northwest Territories'
    * 0314 – renamed "Yukon Territory" to "Yukon"
12. Deleted the following key values and descriptions in Wholesale Exposure Class Primary Key table:
    * 1809 - SMEs Treated as Corporate
    * 1811 - Non-CRE - SME Corporate
    * 1812 - CRE - SME Corporate
    * 1813 - Total Land-Banking - SME Corporate
    * 1814 - Interim Finance - SME Corporate
    * 1815 - Re. Gen. Multi-Unit Residential - SME Corporate
    * 1816 - Rev. Gen. - Other - SME Corporate

#### Section 4.5 changes

13. Record Type 000 - Header Record
    * Return file layout version was changed to "2.0.0" from "1.0.0"
14. Record Type 010 – Retail Portfolio Performance
    * Added 2 exposure classes
    * Total Retail [0500]
    * SME Treated as Retail [0508]
    * Added 2 new measurements (section 2.2)
    * Additions to Credit Impaired Loans and Acceptances (position 133 to 147)
    * Credit Impaired Loans and Acceptances Returned to Accrual Status (position 148 to 162)
    * "Filler" starting position was changed to 163 from 133
    * Renamed Write-Off to Write Offs
15. Record Type 015 – Retail Portfolio Performance, General Allowances
    * Renamed Record Type Description "Retail Portfolio Performance, General Allowances (015)" to "Retail Portfolio Performance, General Allowances & Provisions (015)"
    * Added 3 new measurements (sections 2.2, 4.3)
    * General Provisions for Credit Losses (position 43 to 57)
    * Other changes in Credit Impaired Loans and Acceptances (position 58 to 72)
    * Other changes in Allowances for Credit Losses (position 73 to 87)
    * "Filler" starting position was changed to 88 from 43
16. Record Type 040 – Retail Outstandings by Securitization
    * Removed "Unknown" delinquency bucket (0898)
17. Record Type 040 – Retail Outstandings by Securitization
    * Added Exposure class Total Retail [0500]
18. Record Type 050 – Wholesale Portfolio Performance
    * Added 1 new measurement
    * Other changes in Credit Impaired Loans and Acceptances (sections 2.1 and 3.4) (position 163 to 177)
    * Added 1 exposure class
    * Total Wholesale [1800]
    * Dropped 2 exposure classes
    * Non-CRE – SME Corporate [1811]
    * CRE – SME Corporate [1812]
    * "Filler" starting position was changed to 178 from 163
19. Record Type 055 – Wholesale Portfolio Performance, General Allowances
    * Renamed Record Type Description "Wholesale Portfolio Performance, General Allowances (050) " to "Wholesale Portfolio Performance, General Allowances **& Provisions** (055) " (section 4.3)
      + Added 2 new measurements (section 2.1)
      + General Provisions for Credit Losses (position 43 to 57)
    * Other changes in Allowances for Credit Losses (position 58 to 72)
    * "Filler" starting position was changed to 73 from 43
20. Record Type 060 – Wholesale Outstandings by Geography
    * Dropped 1 exposure class
    * Non-CRE – SME Corporate [1811]
21. Record Type 080 – Retail CREF
    * Removed "Unknown" geography (0398)
22. 22. Record Type 090 – Wholesale CREF
    * Dropped 4 exposure classes
      + Total Land-Banking - Corporate Excluding SME [1813]
      + Interim Finance - Corporate Excluding SME [1814]
      + Rev. Gen. Multi-Unit Residential - Corporate Excluding SME [1815]
      + Rev. Gen. - Other - Corporate Excluding SME [1816]
    * Removed "Unknown" geography (0398)

#### Section 5.4.2 changes

23. Removed aggregation rule for 1812 (CRE – SME Corporate)
24. Removed aggregation rule for 1809 (SME Treated as Corporate)
25. Changed aggregation rule for Measures for key value 1801 (Total Corporate) to be the same as measures for consecutive key values 1809 (Other Corporate Excluding SME).).

#### Section 5.5.2 changes

26. Data Redundancy Rule # 2
    * Dropped 1811 (Non-CRE - SME Corporate), 1812 (CRE - SME Corporate)

#### Section 5.5.3 changes

27. Dropped Data Redundancy Rules #3
    * RT90(Outstandings, e, 0300) = RT50 (Outstandings, 1812)
28. Dropped Data Redundancy Rules #4
    * RT95(Authorized, e, 0300) = RT50 (Authorized, 1812)

### Changes in version 2.1

These entries highlight changes made since the last release of this document. This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 2.0 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 2.0 of this Technical Specification Document do not need to use this change log.

#### General

1. Changed all reference of '**Specific** Provisions for Credit Losses' to '**Individual** Provisions for Credit Losses'
2. Changed all reference of '**General** Provisions for Credit Losses' to '**Collective** Provisions for Credit Losses'
3. Changed all reference of '**Specific** Allowances for Credit Losses' to '**Individual** Allowances for Credit Losses'
4. Changed all reference of '**General** Allowances for Credit Losses' to '**Collective** Allowances for Credit Losses'

### Changes in version 2.2

These entries highlight changes made since the last release of this document.  This log has been written for the technical audience who is already familiar with the previous release of this document and needs to know what changes have been made to it. Readers should have Version 2.1 of this document on hand when reviewing this change log. Note, that there might be a number of small, 'cosmetic-type' corrections in the document that are not listed here. (They should not have an impact on development.)

Those not already working with Version 2.1 of this Technical Specification Document do not need to use this change log.

#### General

1. Changed all reference of '**Gross Impaired Loans & Acceptances**' to '**Credit Impaired Loans & Acceptances**'
2. Changed all reference of '**Additions to Gross Impaired Loans and Acceptances**' to '**Additions to Credit Impaired Loans and Acceptances**'
3. Changed all reference of '**Gross Impaired Loans and Acceptances Returned to Accrual Status**' to '**Credit Impaired Loans and Acceptances Returns to Accrual Status'**
4. Changed all reference of '**Other Changes in Gross Impaired Loans and Acceptances**' to '**Other Changes in Credit Impaired Loans and Acceptances**'

Report a problem or mistake on this page

Date modified:
:   2018-12-18