# SWIFT®[Footnote 1](#fn1) Batch Reporting Instructions and Specification

Version 3.2

November 22, 2015

Includes specifications for SWIFT Electronic Funds Transfer Reports

## On this page

[Changes in this Version](#changes)

1. [General Information](#s1)
2. [Acceptance Procedures](#s2)
3. [Batch Submission, Acknowledgement and Modification](#s3)
   * 3.1 [Batch type "A": Add batch](#s3.1)
   * 3.2 [Batch acknowledgements](#s3.2)
     + 3.2.1 [Accepted batch](#s3.2.1)
     + 3.2.2 [Rejected batch](#s3.2.2)
   * 3.3 [Reports returned for further action (RRFA)](#s3.3)
   * 3.4 [Modification](#s3.4)
     + 3.4.1 [Batch type "C": Correction batch](#s3.4.1)
4. [General Specifications](#s4)
   * 4.1 [General format requirements](#s4.1)
   * 4.2 [Mandatory and required fields](#s4.2)
   * 4.3 [Batch process](#s4.3)
5. [Batch Report Formatting](#s5)
   * 5.1 [Detailed specification layout – Batch header, sub-header and trailer](#s5.1)
     + 5.1.1 [Samples of batch headers, sub-headers and trailers](#s5.1.1)
   * 5.2 [Detailed specification layout – SWIFT EFT reports (EFTS)](#s5.2)
     + 5.2.1 [Outgoing SWIFT message report](#s5.2.1)
     + 5.2.2 [Incoming SWIFT message report](#s5.2.2)
     + 5.2.3 [Example of an outgoing SWIFT EFT report submitted by batch](#s5.2.3)
     + 5.2.4 [Example of an incoming SWIFT EFT report submitted by batch](#s5.2.4)
6. [Acknowledgement Formatting](#s6)
   * 6.1 [Detailed specification layout –Batch acknowledgement](#s6.1)
     + 6.1.1 [Acknowledgement layout](#s6.1.1)
     + 6.1.2 [Acknowledgement examples](#s6.1.2)
7. [Reports Returned for Further Action Message Formatting](#s7)
   * 7.1 [Detailed specification layout – RRFA message](#s7.1)
     + 7.1.1 [General RRFA message layout](#s7.1.1)
     + 7.1.2 [RRFA message example](#s7.1.2)
8. [Report Validation and Processing Error Codes.](#s8) 
   * 8.1 [Report validation rules](#s8.1)
   * 8.2 [Batch error codes](#s8.2)
9. [Batch File Naming Convention](#s9)
   * 9.1 [Batch file naming standard](#s9.1)
   * 9.2 [FINTRAC batch acknowledgement file naming convention](#s9.2)
   * 9.3 [RRFA batch file naming convention](#s9.3)
10. [Appendix 1: Outgoing SWIFT Electronic Funds Transfer Report](#app1)
11. [Appendix 2: Incoming SWIFT Electronic Funds Transfer Report](#app2)

[![](/images/download.png)

SWIFT Batch Reporting Instructions and Specification (PDF version, 453 KB)](swift-v3_2-eng.pdf)

## Changes in this Version

**Tag :59: - Beneficiary Customer**

The specifications for Tag: 59: in Sections 5.2.1 – Outgoing SWIFT message and 5.2.2 – Incoming SWIFT messages have been changed to include the new Option F. This may require programming changes on your part.

## 1 General Information

The purpose of this specification document is to provide reporting entities with the requirements and conditions for filing the following reports to the Financial Transactions and Reports Analysis Centre of Canada (FINTRAC) using the **electronic** **batch file transfer format**:

* SWIFT electronic funds transfer reports (EFTS)

This document is for you if you are need to report international electronic funds transfers (EFTs) sent or received as a SWIFT member or sub-member through the SWIFT network. For information about sending any other type of report to FINTRAC by batch, refer to the specification document called *Standard* *Batch Reporting Instructions and Specification.* Revisions to those specifications are also being published as version 3.0.

The specifications defined in Sections 4 and 5 reflect the file characteristics acceptable for submission of electronic batch SWIFT reports. These must be adhered to unless replaced by a revision to this specification document.

Each revision will have a different version number. The change in version number will be according to the following types of changes made.

* **Change in batch report formats supported**  
  If the current version number of this document were to change by a whole number, for example, from 3.0.5 to 4.0, this would indicate that the SWIFT batch report format supported is being changed. This would signal programming changes for you if you are already submitting reports by batch, as the format you are using would no longer be supported.
* **Change due to legislative amendments**  
  If the revisions to this document were to contain changes in reporting requirements but none to format, the version number would be changed by "0.1". For example, if the version number were to change from "3.0.5" to "3.1", this would indicate changes to the reporting requirements based on amendments to the *Proceeds of Crime (Money Laundering) and Terrorist Financing Act* (the Act) or the related Regulations. This would signal programming changes for you.
* **Change due to editorial revisions**  
  If the revisions to this document contain changes that are simply editorial, the version number would be changed by "0.0.1". For example, moving from "3.0.5" to "3.0.6". This indicates changes to clarify text or correct any typographical errors. This type of change does not signal any programming changes for you, unless a legislative change or changes in format were also indicated.

This document reflects the provisions of the *Proceeds of Crime (Money Laundering) and Terrorist Financing Act* (the Act) and the related Regulations, i.e., the *Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations* and the *Regulations Amending the Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations*. This document is provided as general information only. It is not legal advice, and is not intended to replace the Act and Regulations. For more information about money laundering, terrorist financing or other requirements under the Act and Regulations, including what type of person or entity is a reporting entity, see the appropriate guideline from the guidelines page of FINTRAC's website athttps://fintrac-canafe.canada.ca.

Throughout this document, any references to dollar amounts (such as $10,000) refer to the amount in Canadian dollars or its equivalent in foreign currency.

If you have a question about batch reporting that is not answered in this document, refer to the batch questions and answers in the reporting section on FINTRAC's website at https://fintrac-canafe.canada.ca.

## 2 Acceptance Procedures

Approval to participate in batch report filing under this version of these specifications is contingent upon the following:

* Enrolment with FINTRAC
* Completion of the Public Key Infrastructure (PKI) registration process;
* Installation and configuration of the batch transmission software; and
* Successful completion of test submissions in a batch transmission software training channel.

More information about the PKI registration process and batch transmission software installation can be found in the reporting section of FINTRAC's website.

You (i.e., the transmitter of the batch files) will be asked to perform **test** submissions in **a** batch transmission software **training channel**, as follows:

* The test data will consist of a set of reports containing the data that you would normally supply. The test file must contain only one batch header, one to five sub-headers, between 25 and 100 reports and only one batch trailer. A minimum of five test files is required.
* The formatting of the batch records must adhere to the specifications explained in Sections 4 and 5. Otherwise, the batch and/or reports will be rejected. If files are unreadable for reasons such as format problems, error messages will be returned identifying the problem(s) through the batch transmission software process.
* Reporting entity location numbers used in test reports data must be valid for the reporting entity. See the FINTRAC header in either the outgoing or incoming reports for more information about these.
* Upon receipt of the test data by FINTRAC, it will be processed and an acknowledgement message, along with any error messages, will be returned to you within two working days.
* If all the reports in four out of five of your test batches are error-free (i.e., they contain the required fields, the file and data fields are formatted correctly and the location numbers are valid), FINTRAC will issue final acceptance for you to begin production submissions. Acceptance will be based on the last 5 batches submitted to FINTRAC.
* If a test file is incorrectly formatted or test reports contain mandatory field or field format errors, you will have to submit a new set of test data to FINTRAC. You have to correct these errors before FINTRAC will authorize you to submit production reports.

## 3 Batch Submission, Acknowledgement and Modification

Currently, batches may be sent to FINTRAC at any time of the day and any day of the week. All batches received by FINTRAC will be acknowledged (see Section 3.2).

Batches can only contain reports of one type (EFTS). Although a batch can contain up to 10,000 reports, the physical batch size cannot exceed 30 megabytes, uncompressed.

The batch file must be placed in the directory in which your batch transmission software is configured to look for files for transfer. Batch submissions can be made in one of the two following types:

* Batch type "**A**" — Add a new batch of reports (see Section 3.1)
* Batch type "**C**" — Correct or delete one or more reports from a previously accepted batch (see Section 3.4)

Corrections or deletions to SWIFT EFT reports can only be processed by submitting a correction batch. See Section 3.4 for more information. Unlike other types of reports, SWIFT EFT reports cannot be sent or changed through F2R, FINTRAC's secure website.

### 3.1 Batch type "A": Add batch

The following circumstances require submission of batch type "A":

* **New reports**– If you need to submit reports that were not previously included in a batch, submit them in a new batch (batch type "**A**").
* **Rejected batch**– If you submitted a batch and it was **completely** rejected by FINTRAC, you have to make the required corrections and submit the reports from the rejected batch within a proper new batch (batch type "**A**").

### 3.2 Batch acknowledgements

The batch transmission software will contain a log message that your batch file was sent along with an indication that it was successfully transferred to FINTRAC (although not necessarily processed). Once your batch file is processed by FINTRAC, an acknowledgement file will be returned to you through the batch transmission software. This file will contain an acknowledgement that your batch file was received, the number of reports accepted and any associated error messages. It will **not** include any report content; only batch identifying information and any applicable report error messages.

Any error messages will contain information referring to the report sequence number and your reporting entity report reference number. The error message will also contain the field reference number and the nature of the error. If the batch cannot be processed, a rejection message will be returned to you through the batch transmission software with batch identifying information and applicable error messages.

See Section 6 for more information about how FINTRAC's acknowledgement messages are formatted, including two examples of a general batch acknowledgement message.

#### 3.2.1 Accepted batch

If your batch is accepted, FINTRAC will indicate this in the batch status message (tag C2) in Section C of the acknowledgement file. Section C will also contain the number of reports accepted in your batch.

The acknowledgement will also alert you about any reports requiring correction, as follows:

* Rejected reports (tags C4, D and D2 of the acknowledgement file); or
* Reports that have been accepted but have errors (tags D and D2 of the acknowledgement file).

In this case, you will have to correct those reports, as explained in Section 3.4.

#### 3.2.2 Rejected batch

If your batch is rejected, it will be indicated in the batch status message (tag C2) in Part C of FINTRAC's acknowledgement. This means there are problems with that batch's header, sub-header, trailer or report format. It also means that the reports included in that batch have not been received by FINTRAC. You will have to resubmit them in a new batch, as explained in Section 3.1.

In the case of a rejected batch, FINTRAC may not have any information about the reports it contained. However, if any information is available at the report level, it will be reflected in Tag C6 of your acknowledgement message. A maximum of 40 such messages can be provided to help you correct them before you resubmit them in a new batch.

### 3.3 Reports returned for further action (RRFA)

If there are data quality issues with your accepted reports, FINTRAC may return those reports to you for adjustment. These are called reports returned for further action (RRFA).

RRFAs for the SWIFT electronic funds transfer (EFTS) report type are handled through batch.

You will receive an RRFA message through the batch transmission software, in a similar manner to how you receive your acknowledgement messages. See Section 7 for more information about how RRFA messages are formatted, including an example of an RRFA message. If an RRFA is sent to you in this manner, you will have to correct the affected reports and re-submit them to FINTRAC in a correction batch as explained in Section 3.4. These returned reports will not appear in F2R, but your F2R administrator will be advised by email when a batch RRFA has been sent by batch.

### 3.4 Modification

The following explains how you can make required modifications to reports that were submitted by batch to FINTRAC.

Modifications are required in the following instances:

* If your acknowledgement file indicates that a batch is accepted but that there were rejected reports or reports with errors, you will have to modify those reports.
* If FINTRAC sends you an RRFA, you will have to make the necessary modifications and resubmit the corrected report as soon as possible.
* You may also need to correct or delete a report for other reasons. For example, if you were to discover that a report contained invalid data or was submitted in error.

Modifications to SWIFT EFT reports can only be done through correction batches (type "C"). There are no SWIFT EFT reports in F2R.

#### 3.4.1 Batch type "C": Correction batch

The following applies to a processed report with errors as well as a rejected report.

Only the reports being corrected or deleted are to be included in the correction batch. All previously accepted batches can be corrected, by submitting a correction batch:

1. Batch type set to "**C**" (correction batch).
2. Sub-header count set to the number of sub-headers in the correction batch.
3. Report count set to the number of reports in the correction batch.
4. Sub-header report count in the applicable sub-headers set to the number of reports in the correction batch.

To **correct** one or more reports from a previously **accepted** batch, you must submit a correction batch (batch type "C") with each complete corrected report. ALL FIELDS in each corrected report must be completed with the correct information, NOT JUST THE DATA FIELDS NEEDING CORRECTION***.*** The action code for each report to be corrected has to be set to "C".

To **delete** one or more reports from a previously **accepted** batch, you must also submit a correction batch (batch type "C"). In this case, you need not submit the complete report to be deleted. Only the FINTRAC header (tag 0:) must be completed. Also, the action code value must be "D". Immediately following the FINTRAC header, delimit the deleted report with carriage return, line feed (<CRLF>). Begin the next report to be corrected or deleted, as required.

## 4 General Specifications

### 4.1 General format requirements

The following table identifies the general formatting specifications for completing SWIFT electronic funds transfer reports (EFTS) using the batch file transfer format.

Section 5 provides detailed formatting requirements for each report (i.e., incoming or outgoing SWIFT EFT).

**All batch header records are to be fixed in length as specified in the format descriptions**. The physical batch size cannot exceed 30 megabytes, uncompressed.

The standard file characteristics must be in ASCII code page 850 (Western European), upper and lower characters, and English and/or French character set. EBCDIC data format will **not** be accepted. The code page format ASCII 850 must be indicated in the batch header.

All batch headers, sub-headers, report parts and batch trailers must be delimited with carriage return, line feed (<CRLF>). As these may be implicit in certain programs, please ensure that this does not cause blank lines to be inserted.

All SWIFT message data must be variable length and delimited as specified in Section 5.2.

**GENERAL FORMAT REQUIREMENTS**

| Format Element | Comment |
| --- | --- |
| **Zero-filled** | Blank fields are to be filled with zero (0). |
| **Space-filled** | Blank fields are to be space-filled. |
| **LJ** | Left justified, space-filled |
| **RJ** | Right justified, space-filled |
| **RJZ** | Right justified, zero-filled  All amount fields are RJZ, no thousands separators allowed. |
| **X** | Alphanumeric character |
| **9** | Numeric character |
| **Field length** | Number shown in brackets next to alphanumeric character or numeric character. For example, X**(2)** or 9**(5)**. |
| **d** | Decimal place — FINTRAC will accept ',' or '.' as a decimal place notation.  For an amount of money, the format requires a fixed decimal place, with two decimal places. For example, 000000012345,00 represents the amount of $12,345.00 for a field with X(15)d.  For an exchange rate, the format requires a floating decimal place, with as many decimal places as required. For example, 00000012.123 represents the exchange rate of 12.123 for a field with X(12)d. The SWIFT standard currently uses ',' to denote a decimal place. |
| **Report sequence number** | The first report in a batch type "A" (Add batch) within a sub-header must begin at 00001 and all following reports must be incremented by 1.  For reports in a batch type "C" (correction batch), use the sequence numbers of the reports from the original accepted batch. |
| **Date** | Year/month/day (YYYYMMDD) |
| **Time** | HHMMSS — Use the 24-hour clock: hour (from 00 to 23), minutes (from 00 to 59) and seconds (from 00 to 59).  Seconds should default to 00.  Examples: 1 o'clock PM = 130000 or 2:45 PM = 144500.  RJZ |
| **Telephone Numbers** | Must include area codes  Canada and US: 999-999-9999  For others, include country code, city code and local number: 999-9999-9999-9999 |
| **Reporting entity report reference number** | Can contain letters from A to Z and/or numbers from 0 to 9. Do **not** use any special characters, such as "-", "#", etc., in this reference number.  Each report submitted by the same reporting entity has to have a unique number. In this context, the upper case of any letter is considered the same as the lower case of that letter. For example, a report reference number of ABC123 is considered the same as the report reference number abc123. This unique number means that you do not need a FINTRAC-generated report number for a batch report. |
| **±** | Denotes a mandatory field required for a batch report |

### 4.2 Mandatory and required fields

Fields in the batch format indicated by "**±**" are required for processing purposes, such as those within the batch header, sub-header and trailer blocks.

Appendices 1 and 2 provide the fields for SWIFT reports as established by the Regulations.

The fields are either mandatory, mandatory if applicable, or require reasonable efforts to complete, as follows:

* **Mandatory:** All fields marked with an asterisk (**\***) **have to be completed.**
* **Mandatory if applicable:** The fields that have both an asterisk and "if applicable" next to them have to be completed if they are applicable to you or the transaction being reported.
* **Reasonable efforts:** For all other fields that do not have an asterisk, you have to make reasonable efforts to get the information. For more information about "reasonable efforts" please refer to *Guideline 8: Submitting Electronic Funds Transfer Reports to FINTRAC* available from the Guidelines area of FINTRAC's website.

Where mandatory and required fields have not been completed, the report may be rejected.

### 4.3 Batch process

A SWIFT batch must contain one batch header, at least one batch sub-header, and only SWIFT EFT message type MT103. It must also have one batch trailer.

## 5 Batch Report Formatting

The following charts provide details on how to format reports for batch submission to FINTRAC. An individual batch file is limited to a **maximum of 10,000 reports**. The physical batch size cannot exceed 30 megabytes, uncompressed.

### 5.1 Detailed specification layout – Batch header, sub-header and trailer

**Batch Header -** The batch header contains information identifying the individual or institution originating the transmission. There can be only one batch header for each transmitted file. The following elements are required in the batch header.

| Field No. | Field Name | Format | Comment |
| --- | --- | --- | --- |
| ± 0 | Record type | X(2) | Value "1A" |
| ± 1 | Code format | 9(3) | Value "850" |
| ± 2 | Report type | X(4)LJ | Value "EFTS" indicating SWIFT electronic funds transfer reports |
| ± 3 | Reporting entity's identifier number | 9(7)RJZ | This is your seven-digit identifier number assigned to you by FINTRAC at enrolment.  This field is required. If it is invalid, the batch will be rejected. |
| ± 4 | Contact surname | X(20)LJ | Surname (i.e., family name) of contact individual |
| ± 5 | Contact given name | X(15)LJ | Given name of contact individual. |
| ± 6 | Contact telephone number | X(20)LJ | Telephone number of contact individual |
| ± 6A | Contact telephone number extension | 9(5)RJZ | Telephone extension number of contact individual, if there is an extension |
| ± 7 | PKI certificate ID | 9(10)RJZ | This is your ten-digit PKI certificate identifier number assigned to you by FINTRAC |
| ± 8 | Batch date | 9(8) | Date the batch was created: YYYYMMDD. |
| ± 9 | Batch time | 9(6) | Time the batch was created: HHMMSS |
| ± 10 | Batch sequence ID | 9(5)RJZ | This is a numeric sequence identifier created by you for the batch. The combination of batch date, time and sequence identifier must be unique for each of your batches. For example, if you were to send two batches in a day, use 00001 for the first batch sequence identifier and 00002 for the second. |
| ± 11 | Batch type | X(1) | "A" – Add a new batch of reports  "C" – Correction batch to correct or delete one or more reports from a previously **accepted** batch |
| ± 12 | Sub-header count | 9(5)RJZ | Number of sub-headers in batch |
| ± 13 | Report count | 9(5)RJZ | Total number of reports included in the batch (maximum 10000) |
| ± 14 | Format indicator | 9(2)RJZ | Batch report format version number "03" |
| ± 15 | Operational mode | X(1) | "P" – Production  "T" – Test (in a batch transmission software training channel) |
| Total characters in batch header: | | 119 | Every batch must have a batch header. |

**Batch Sub-Header -** The batch sub-header contains information that allows you to group reports included in the batch according to your organizational structure or any other grouping need. The use of different sub-headers is optional, but you must include at least one sub-header in a batch. The following elements are required in each batch sub-header.

| Field No. | Field Name | Format | Comment |
| --- | --- | --- | --- |
| ± 0 | Record type | X(2) | Value "1B" |
| ± 1 | Sequence number | 9(5)RJZ | Sub-header sequence number |
| ± 2 | Reporting entity report group ID | X(25)LJ | This can be any value you choose to identify the grouping of the reports included in the batch. If you do not use this value, space-fill this field. |
| ± 3 | Report count | 9(5)RJZ | Enter the total number of reports included for the sub-header |
| Total characters in batch sub-header: | | 37 | Every batch must have at least one sub-header. |

**Batch Trailer –** The batch trailer identifies the end of the records in the file.

| Field No. | Field Name | Format | Comment |
| --- | --- | --- | --- |
| ± 0 | Record type | X(2) | Value "1C" |
| ± 1 | Sequence number | 9(5)RJZ | Sequence number of the batch trailer should always be "00001". |
| Total characters in batch trailer: | | 7 | Every batch must have one trailer at the end, following the last report in the batch. |

#### 5.1.1 Samples of batch headers, sub-headers and trailers

As explained in Section 5.1, you must have one batch header, at least one sub-header, and one batch trailer for each batch you send to FINTRAC. Sub-headers are part of the batch format to allow you to group reports within a batch according to your organizational structure or any other grouping need. The use of different sub-headers is optional, but you must include at least one sub-header in a batch.

The following examples illustrate two possible scenarios regarding the use of batch headers and sub-headers.

**Example 1**

A reporting entity called "ABC and Company" is sending three SWIFT EFT reports in a production batch. Their reporting entity identifier is 0004567 and their PKI certificate identifier is 1234567890. The contact person is John Smith and Mr. Smith's telephone number is 416-555-5555 (no extension). ABC and Company does not wish to group reports within a batch.

```

1A850EFTS0004567SMITH               JOHN           416-555-5555        0000012345678902005071923155500001A000010000303P
1B00001ABC AND COMPANY 			00003
     Report 1
     Report 2
     Report 3
1C00001
```

**Example 2**

A reporting entity called "Entity X" operates in several different geographical locations (Location A, Location B, etc.) and wishes to group their reports by location. In this case, the reporting entity would include a different sub-header for each location. Their reporting entity identifier is 0000567 and their PKI certificate identifier is 7771234567. The contact person is John Brown and Mr. Brown's telephone number is 416-666-6666 (no extension). To send a batch with a total of five SWIFT EFT reports (three from Location A and two from Location B), they would use two sub-headers, as follows:

```

1A850EFTS0000567BROWN               JOHN           416-666-6666        0000077712345672005071923155500001A000020000503P
1B00001LOCATION A               00003
		Report 1 from Location A
		Report 2 from Location A
		Report 3 from Location A
1B00002LOCATION B               00002
		Report 1 from Location B
		Report 2 from Location B
1C00001
```

### 5.2 Detailed specification layout – SWIFT EFT reports (EFTS)

As a SWIFT member or sub-member, you can include a copy of the SWIFT electronic funds transfer information according to the SWIFT format, as long as all your SWIFT EFT report's field requirements are met. If the information for any of your report's mandatory fields is not contained in the SWIFT format, you must add the information for those fields in the report. The same is true for any reasonable efforts fields that you are required to provide.

Before you can include the SWIFT message format information in your report to FINTRAC, any – ":5 trailer block" fields and all "SWIFT ACK header block" fields must be stripped from the message.

The following notation standards are contained in the layouts in Sections 5.2.1 and 5.2.2.

**NOTATION STANDARDS**

| Element | Comment |
| --- | --- |
| **[  ]** | Values inside square brackets are optional |
| **{  }** | Curly brackets are used to indicate message block and field tag delimiters |
| **16x** | Field is 16 alphanumeric characters (SWIFT "X" character set) |
| **6!n** | Field is fixed 6 numeric characters (0 through 9 only) |
| **3!a** | Field is fixed 3 alpha characters (A through Z, upper case only) |
| **3!c** | Field is fixed 3 alphanumeric (upper case only) |
| **15d** | Field is 15 numeric characters (0 through 9) including decimal place ("," only) |
| **20z** | Field is 20 alphanumeric characters (SWIFT "Z" character set) |
| **!** | Designated fixed field size |

#### SWIFT message rules

The following SWIFT rules apply when structuring message fields (tag lines) in your reports to FINTRAC.

Each field is identified by a tag that consists of two digits, or two digits followed by a letter option, i.e., "**:nn[a]:**". This tag consists of a delimiter colon (":"), followed by a field tag number ("nn") and a letter option ("a"), if applicable, followed by a colon ':' and the field content.

The following character restrictions apply to field content:

* The field content must not start with a carriage return, line feed (<CRLF>);
* The field content must not be entirely composed of blank characters;
* Within field content, a colon ":" or hyphen "-" must never be used as the first character of a line (this is apart from the delimiter ":" used in the tag); and
* A field must consist of at least one meaningful character (except for fields 15a and 77E).

The "carriage return, line feed" character must always appear as a sequence. This sequence shall only be used to indicate start of text, as a field separation within text, to indicate a new line, and to indicate the end of text.

Fields are separated by a "field separator within text" (<**CRLF:>**). The first field in a message is preceded by a "start of text" (<**CRLF:>**) and the last field in a message is followed by an "end of text" (<**CRLF->**).

Field content may be composed of one or several sub-fields. When sub-fields appear on separate lines, the "<CRLF>", which is not included in the number of characters for the length of the sub-field, serves as the sub-field separator. The following character restrictions apply to sub-field content:

* Sub-fields may themselves be of fixed or variable length;
* The order of sub-fields is fixed;
* When necessary, sub-fields are separated by special symbols, e.g., "/" or "//";
* Sub-fields must not be entirely composed of blank characters; and
* Sub-fields or components must consist of at least one meaningful character.

Whenever a field contains mandatory and optional sub-fields, at least all of the mandatory sub-fields must appear when that field is used.

#### 5.2.1  Outgoing SWIFT message report

**SWIFT MT103 – Single Customer Credit Transfer**  
**Batch format 03: Outgoing EFTS**

| Tag | Field Name | Format | Comment |
| --- | --- | --- | --- |
| 0: | **FINTRAC HEADER** |  | This header does not apply to the SWIFT message, but is required in the report to FINTRAC. If it is not included, the report will be rejected. |
| Report sequence number | 9(5)RJZ | Report sequence number within the preceding sub-header. |
| Reporting entity report reference number | X(20)LJ | A unique report reference number is required for each report submitted from the same reporting entity. |
| Action code | X(1) | If you are submitting a new batch (batch type "A"), enter "A" to indicate there is no change or deletion as this is a new report.  If you are submitting a correction batch (batch type "C"), indicate whether this report is to be changed or deleted from a previously accepted batch.  To **change** a report, use the action code "C" and complete the rest of the report.  To **delete** a report, use the action code "D". After you have provided the rest of the information in the FINTRAC header, immediately delimit that report with a carriage return, line feed (<CRLF>). Continue with the next report or the batch trailer, as appropriate. |
| Reporting entity's identifier number | 9(7)RJZ | Enter your seven-digit identifier number assigned to you by FINTRAC at enrolment. For more information about this, contact your F2R administrator.  In the case of an outgoing EFTS, this provides FINTRAC with your full name information, as the person or entity sending the payment instructions.  This field is mandatory. If it is invalid, the report will be rejected. |
| Reporting entity's location number | X(15)LJ | This represents the full address of the person or entity sending the payment instructions. Location numbers are assigned during the FINTRAC enrolment process and maintained by your F2R administrator. For more information about this, contact your F2R administrator.  For deposit taking institutions, this number is the branch portion of your transit number with leading zeroes. For example, the location number for branch 02831 of bank number 0004 would be 02831.  For other types of reporting persons or reporting entities, this number will be created and assigned to you by FINTRAC.  This field is mandatory. If it is invalid, the report will be rejected. |
| 24-hour rule indicator | 9(1) | If a report is about an EFT of less than $10,000 that is one of two or more EFTs of less than $10,000 made within 24 consecutive hours of each other that total $10,000 or more, use the 24-hour rule indicator of "1". Each such EFT is submitted on a separate report.  If the transaction being reported is of $10,000 or more, enter "0".  This field is required. If it is invalid, the report will be rejected. |
| **Total for Tag 0:** | 49 | Total characters required in FINTRAC HEADER |
| 1: | **BASIC HEADER**  Block identifier ({1:)  Application ID (F = FIN)  Service ID (01 only)  Canadian SWIFT LT  (BANKCACCAXXX)  Session number (0030)  Sequence number (123456)  End (}) | 29X | {1:<variable data>} which must include the **sending** SWIFT LT. For example, {1:F01BANKCACCAXXX0030123456}, where BANKCACCAXXX is the Canadian SWIFT LT  This header is required for a SWIFT network transmission.  If this header is added by a remote process prior to your connection to the SWIFT network, refer to the instructions in Section 5.2.1.1.  Your report to FINTRAC must include information about the individual or entity sending the EFT. This means either the bank identification code (BIC) or the full name and address of the individual or entity sending the payment instructions for the EFT. |
| 2: | **APPLICATION HEADER**  **Input** to SWIFT  Block identifier ({2:)  I/O identifier (I)  Message type (103)  Receiver's address      (BANKBEBBAXXX)  Message priority (S) (S, N, U)  Delivery monitoring (2) (1, 2, 3)  Obsolescence period (003)  If Priority = U, 003 represents 15 minutes  If Priority = N, 020 represents 100 minutes)  End (}) | 51X | {2:<variable data>}  Input to SWIFT. Fixed length, continuous with no field separators. For example, {2:I103BANKBEBBAXXXS2003}, where BANKBEBBAXXX is the receiver's SWIFT LT. Obsolescence period may not be present in the application header.  This header is required for a SWIFT network transmission.  If this header is added by a remote process prior to your connection to the SWIFT network, refer to the instructions in Section 5.2.1.1.  Your report to FINTRAC must include information about the individual or entity receiving the EFT. This means **either** the bank identification code (BIC) **or** the full name and address of the individual or entity receiving the payment instructions for the EFT. |
| 3: | **USER HEADER**  Block identifier ({3:)  Optional priority code     ({113:xxxx})  Message user ref. – MUR  ({108:abcdefgh12345678})  MT103+ identifier ({119:STP})  End (}) | See Comment column for applicable format | **MT03**  Format  36X (MT103 max.)  Example  {3:{113:xxxx}{108:abcdefgh12345678}}  **MT03+**  Format  45X (MT103+ max.)  Example  {3:{113:xxxx}{108:abcdefgh12345678}{119:STP}}  If this header is added by a remote process prior to your connection to the SWIFT network, refer to the instructions in Section 5.2.1.1.  The user header is an optional field for a SWIFT network transmission. The information it contains is not required for processing your report to FINTRAC. |
|  | Begin message text | 2X | {4:  This is required for a SWIFT network transmission and is used to signal the beginning of the message text in your report to FINTRAC. |
| :20: | Transaction reference number | 16X | Reference assigned by the sender to unambiguously identify the message  The transaction reference number is required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as this information is a reasonable efforts field in the EFTS report. |
| :13C: | Time indication | /8c/4!n1!x4!n | This repetitive field specifies one or several time indications related to the processing of the payment instructions.  Codes within the slashes are as follows:   * SNDTIME * RNCTIME * CLSTIME   Time indication must be a valid time expressed as HHMM.  Sign is either "+" or "–",  Time offset is expressed as HHMM, where the hour component (HH) must be in the range of 00 through 13. The minute component, (MM) must be in the range of 00 through 59.  Time is to be expressed by means of the offset against the Universal Standard Time (UST). For example :13C:/CLSTIME/0915+0100.  As time indication is optional for a SWIFT network transmission, the time of processing of the transaction is a reasonable efforts field in your report to FINTRAC. |
| :23B: | Bank operation code | 4!c | This identifies the type of operation. Codes are as follows:   * CRED * CRTS * SPAY * SSTD * SPRI   This field is required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as it is a reasonable efforts field in the EFTS report. |
| :23E: | Instruction code | 4!c[/30x] | This repetitive field specifies an instruction that will include a four-character instruction code. It also includes account or narrative information.  The instruction code is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :26T: | Transaction type code | 3!a | This identifies the nature of the individual transaction or the reason for it. For example, the transaction is to transmit a salary, a pension, or a dividend.  The transaction type code is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :32A: | Value date/Currency/Interbank settlement amount | 6!n3!a15d | The settlement amount is the amount to be booked or reconciled at interbank level. For example, it might be presented as follows:   * 011122USD3614,33 * 011217CAD17539,   This field is required for a SWIFT network transmission and the information is mandatory in the EFTS report. |
| :33B: | Currency code, instructed amount | 3!a15d | This specifies the currency and amount of the instruction, for information purposes. It is required when a currency conversion or exchange has occurred on the sender's side.  For example, it might be presented as follows:   * USD3614,33 * CAD17539,   This currency code is optional for a SWIFT network transmission. |
| :36: | Exchange rate | 12d | This is to provide the exchange rate used to convert the original ordered amounts specified in tag :33B:.  The exchange rate is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :50: | Ordering customer | See Comment column for applicable format | This specifies the customer ordering the transaction.  **Option K**  Line  (Account)  (Name and address)  Name  Street information (including suite, apartment, etc.)  Street information (including suite, apartment, etc.) (if required)  City and province or state code, country code and postal/zip code  Format  [/34x]    35X  35X  35X  35X  The SWIFT format for name and address is 4\*35x. However, the FINTRAC report format requires four lines with no more than 35 characters per line. Explicitly end lines with carriage return, line feeds (<CRLF>). Do not use automatic wrapping of lines at 35.  If information for street takes only one line, provide only three lines for name and address.  If information for a given target line is not available, leave that line blank.  Name information cannot be on the same line as any address information.  Use a space to separate words and do not use periods or commas.  Street information must be separate from city, province/state and country code. Preferred format for street information is:  <appt#> <street number> <street name> <street type> <direction>. Use single letters or two single letter combinations for street direction (i.e., N S E W NE SW). For example, 3 99 Norman St SE.  Use ISO two-character codes for province/state and country codes.  There is another option in the SWIFT network transmission for ordering customer: Option A (account and BEI). However, only **Option K** provides the information that is mandatory for your report to FINTRAC, i.e., the ordering client's full name and address and account number (if an account is applicable). |
| :51A: | Sending institution | See Comment column for applicable format | This identifies the sender of the message.  Option A in the SWIFT network transmission for sending institution includes the following:  Line  Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  The sending institution is optional on the SWIFT network transmission. For your report to FINTRAC, either the bank identification code (BIC) or the full name and address of the individual or entity sending the payment instructions for the EFT is mandatory.  In the case of an outgoing EFT, you provide this information in the FINTRAC header, as you are the sender. |
| :52: | Ordering institution | See Comment column for applicable format | There are two options for ordering institution in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Nom et adresse  Format  [/1!a][/34x]  4\*35x  The ordering institution is optional on the SWIFT network transmission. However, if there is an ordering institution for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the individual or entity ordering the payment instructions for the EFT on behalf of a client. |
| :53: | Sender's correspondent | See Comment column for applicable format | There are three options for sender's correspondent in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The sender's correspondent is optional on the SWIFT network transmission. However, if there is a sender's correspondent for the EFT, part of the information in either **option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the individual or entity (other than the sender) acting as reimbursement bank for the sender of the EFT (if applicable). |
| :54: | Receiver's correspondent | See Comment column for applicable format | There are three options for receiver's correspondent in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The receiver's correspondent is optional on the SWIFT network transmission. However, if there is a receiver's correspondent for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the individual or entity acting as reimbursement bank for the receiver of the EFT (if applicable). |
| :55: | Third reimbursement institution | See Comment column for applicable format | There are three options for third reimbursement institution in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The third reimbursement institution is optional on the SWIFT network transmission. However, if there is a third reimbursement institution for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC.  You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the EFT receiver's branch, if the funds are made available to the receiver's branch through a financial institution other than the sender's correspondent (if applicable). |
| :56: | Intermediary | See Comment column for applicable format | There are three options for intermediary in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The intermediary is optional on the SWIFT network transmission. However, if there is an intermediary for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the financial institution through which the transaction must pass (the financial institution between the receiver and the financial institution where the account is held) (if applicable). |
| :57: | Account with institution | See Comment column for applicable format | There are four options for account with institution in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The account with institution is optional on the SWIFT network transmission. However, if there is a beneficiary customer account institution for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the financial institution that services the account for the beneficiary customer (if this financial institution is not the receiver) (if applicable). |
| :59: | Beneficiary customer | See Comment column for applicable format | There are two options for beneficiary customer in the SWIFT network transmission as follows:  **No letter option**  Line  Account  Name and address  Name  Street information (including suite, apartment, etc.)  Street information (including suite, apartment, etc.) (if required)  City and province or state code, country code and postal/zip code  Format  [/34x]    35X  35X  35X  35X  **Option F**  Line  Account  Name and address  Format  [/34x]  4 \* 1!n/33x  FINTRAC's report format requires four lines with no more than 35 characters per line. Explicitly end lines with carriage return, line feeds (<CRLF>). Do not use automatic wrapping of lines at 35.  There is another option for beneficiary customer in the SWIFT network transmission: Option A (national clearing system code, account and BEI). However, only the **no letter** **option and option F** provide the information that is mandatory for your report to FINTRAC, i.e., the beneficiary client's full name and address and account number (if an account is applicable). |
| :70: | Remittance information | 4\*35x | This contains transaction detail narrative for the beneficiary customer.  The remittance information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :71A: | Details of charges | 3!a | This identifies the type of operation. Codes are as follows:   * BEN – Charges borne by beneficiary * OUR – Charges borne by sender * SHA – Ordering customer for sender's charges or beneficiary customer for the receiver's charges   Details of charges are required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as this information is a reasonable efforts field in the EFTS report. |
| :71F: | Sender's charges | 3!a15d | This repetitive field specifies the currency and amount of the transaction charges due to the sender.  The sender's charges are optional for a SWIFT network transmission and are a reasonable efforts field in your report to FINTRAC. |
| :71G: | Receiver's charges | 3!a15d | This specifies the currency and amount of the transaction charges due to the receiver.  The receiver's charges are optional for a SWIFT network transmission and are a reasonable efforts field in your report to FINTRAC. |
| :72: | Sender-to-receiver information | 6\*35x. See Comment column for additional details | This specifies additional information for the receiver or another party specified.  Line  Line 1 – (Code)(Narrative)  Lines 2 to 6 – (Narrative) or (Code)(Narrative)  Format  /8a/[additionnal]  [//more info] or [/8a/[additional]]  /8a/ contains codes for:   * Account with institution * Instructing institution to sending institution * Intermediary institution * Receiver institution   The sender-to-receiver information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :77B: | Regulatory reporting | 3\*35x. See Comment column for additional details | This specifies the codes for the statutory or regulatory information required by the authorities in the country of the receiver or the sender.  Line  Line 1 – (Code)(Country)(Narrative)  Lines 2 to 3 – (Narrative)  Format  /8a/2!a[//info]  [//more info]  The regulatory reporting information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :77T: | Envelope contents | 9000z | This contains extended remittance information in different formats. One of the following codes may be used between slashes:   * /UEDI/ - message in UN-EDIFACT format * /ANSI/ - message in ANSI/X12 format * /SWIF/ - message matches structure proposed in field 70 * /NARR/ - message is narrative text   The envelope contents are optional for a SWIFT network transmission. This information is a reasonable efforts field in your report to FINTRAC. |
|  | Group terminator | 2x | -}<CRLF> |

##### 5.2.1.1 Unavailable data for SWIFT basic header, application header and user header

It is possible that you do not have the SWIFT header message blocks (i.e., the basic header, application header and user header) for outgoing SWIFT messages because these are added during a remote process prior your connection to the SWIFT network. If this is your situation, you will have to create similar header blocks for your outgoing SWIFT reports to include the basic header (block 1) and the application header (block 2) only. In this case, the user header (block 3) is not required in your report to FINTRAC.

The headers you create to replicate the two missing SWIFT headers must follow the same format and length as a SWIFT header block and must provide the following:

* Include information to identify the sender and receiver
* In the basic header (block 1:), include a proper session number (e.g., 0001) and a proper sequence number (e.g., 000001) for each SWIFT message in the batch. For each file created, either increase each sequence number by "1"or increase each session number by "1". The acknowledgement and error messages returned to you by FINTRAC will refer to SWIFT reports by these two fields. These numbers can be duplicated from batch to batch.
* In the application header (block 2), provide the block identifier, the I/O identifier, the message type and the receiver's address.

The information in all other parts of these header blocks can be any values you choose to insert, but must still follow the SWIFT format rules.

Each SWIFT message must be preceded with a properly formatted {4: message block.

#### 5.2.2 Incoming SWIFT message report

**SWIFT MT103 – Single Customer Credit Transfer**  
**Batch format 03: Incoming EFTS**

| Tag | Field Name | Format | Comment |
| --- | --- | --- | --- |
| 0: | **FINTRAC HEADER** |  | This header does not apply to the SWIFT message, but is required in the report to FINTRAC. If it is not included, the report will be rejected. |
| Report sequence number | 9(5)RJZ | Sequence number within the preceding sub-header. |
| RE report reference number | X(20)LJ | A unique report reference number is required for each report submitted from the same reporting entity. |
| Action code | X(1) | If you are submitting a new batch (batch type "A"), enter "A" to indicate there is no change or deletion as this is a new report.  If you are submitting a correction batch (batch type "C"), indicate whether this report is to be changed or deleted from the accepted batch.  To **change** a previously accepted report, use the action code "C" and complete the rest of the report.  To **delete** a previously accepted report, use the action code "D". After you have provided the rest of the information in the FINTRAC header, immediately delimit that report with a carriage return, line feed <CRLF>. Continue with the next report or the batch trailer, as appropriate. |
| Reporting entity's identifier number | 9(7)RJZ | Enter your seven-digit identifier number assigned to you by FINTRAC at enrolment. For more information about this, contact your F2R administrator.  In the case of an incoming EFT, this provides FINTRAC with your full name information, as the receiver of the EFT payment instructions. This field is mandatory. If it is not included or if it is invalid, the report will be rejected. |
| Reporting entity's location number | X(15)LJ | This represents the full address of the person or entity receiving the payment instructions. Location numbers are assigned during the FINTRAC enrolment process and maintained by your F2R administrator. For more information about this, contact your F2R administrator.  For deposit taking institutions, this number is the branch portion of your transit number with leading zeroes. For example, the location number for branch 02831 of bank number 0004 would be 02831.  For other types of reporting persons or reporting entities, this number will be created and assigned to you by FINTRAC.  In the case of an incoming EFT, this provides FINTRAC with your full address information, as the receiver of the EFT payment instructions. This field is mandatory. If it is not included or if it is invalid, the report will be rejected. |
| 24-hour rule indicator | 9(1) | If a report is about an EFT of less than $10,000 that is one of two or more EFTs of less than $10,000 made within 24 consecutive hours of each other that total $10,000 or more, use the 24-hour rule indicator of "1". Each such EFT is submitted on a separate report.  If the transaction being reported is of $10,000 or more, enter "0".  This field is required. If it is not included, the report will be rejected. |
| **Total for Tag 0:** | 49 | Total characters required in FINTRAC HEADER |
| 1: | **BASIC HEADER**  Block identifier ({1:)  Application ID (F = FIN)  Service ID (01 only)  Canadian SWIFT LT   (BANKCACCAXXX)  Session number (0030)  Sequence number (123456)  End (}) | 29X | {1:<variable data>} which must include the **receiving** SWIFT LT. For example, {1:F01BANKCACCAXXX0030123456}, where BANKCACCAXXX is the Canadian SWIFT LT.  This header is required for a SWIFT network transmission.  Your report to FINTRAC must include information about the individual or entity receiving the EFT. This means either the bank identification code (BIC) or the full name and address of the individual or entity receiving the payment instructions for the EFT. In the case of an incoming SWIFT EFT report, this information is provided in the FINTRAC header. |
| 2: | **APPLICATION HEADER**  **Output** from SWIFT  Block identifier ({2:)  I/O identifier (O)  Message type (103)  Input time sender (1200)  Message input ref. (MIR)  Input date (970103)  Input LT (BANKBEBBAXXX)  Input session number (2222)       Input sequence number (123456)  Receiver output date (970103)  Receiver output time (1201)  Message priority (N)  End (}) | 51X | {2:<variable data>}  Output from SWIFT. Fixed length, continuous with no field separators.  {2:O1031200970103BANKBEBBAXXX22221234569701031201N}   where BANKBEBBAXXX is the sender's SWIFT LT inputting a message into SWIFT network.  This header is required for a SWIFT network transmission.  Your report to FINTRAC must include information about the individual or entity sending the EFT. This means either the bank identification code (BIC) or the full name and address of the individual or entity sending the payment instructions for the EFT. This information may also be provided at tag :51:. |
| 3: | **USER HEADER**  Block identifier ({3:)  Optional priority code ({113:xxxx})  Message user ref. – MUR  ({108:abcdefgh12345678})  MT103+ identifier ({119:STP})  End (}) | See Comment column for applicable format | **MT103**  Format  36X (MT103 max.)  Example  {3:{113:xxxx}{108:abcdefgh12345678}}  **MT103+**  Format  45X (MT103+ max.)  Example  {3:{113:xxxx}{108:abcdefgh12345678}{119:STP}}  The user header is an optional field for a SWIFT network transmission. The information it contains is not required for processing your report to FINTRAC. |
|  | Begin Message Text | 2X | {4:  This is required for a SWIFT network transmission and is used to signal the beginning of the message text in your report to FINTRAC. |
| :20: | Transaction reference number | 16X | Reference assigned by the sender to unambiguously identify the message  The transaction reference number is required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as this information is a reasonable efforts field in the EFTS report. |
| :13C: | Time indication | /8c/4!n1!x4!n | This repetitive field specifies one or several time indications related to the processing of the payment instructions. Codes within the slashes are:   * SNDTIME * RNCTIME * CLSTIME   Time indication must be a valid time expressed as HHMM.  Sign is either "+" or "–",  Time offset is expressed as HHMM, where the hour component (HH) must be in the range of 00 through 13.  The minute component (MM) must be in the range of 00 through 59.  Time is to be expressed by means of the offset against the Universal Standard Time (UST). For example: 13C:/CLSTIME/0915+0100.  As time indication is optional for a SWIFT network transmission, the time of processing of the transaction is a reasonable efforts field in your report to FINTRAC. |
| :23B: | Bank operation code | 4!c | This identifies the type of operation. Codes are as follows:   * CRED * CRTS * SPAY * SSTD * SPRI   This field is required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as it is a reasonable efforts field in the EFTS report. |
| :23E: | Instruction code | 4!c[/30x] | This repetitive field specifies an instruction that will include a four-character instruction code. It also includes account or narrative information.  The instruction code is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :26T: | Transaction type code | 3!a | This identifies the nature of the individual transaction or the reason for it. For example, the transaction is to transmit a salary, a pension, or a dividend.  The transaction type code is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :32A: | Value date/Currency/Interbank settlement amount | 6!n3!a15d | The settlement amount is the amount to be booked or reconciled at interbank level. For example, it might be presented as follows:   * 011122USD3614,33 or * 011217CAD17539,   This field is required for a SWIFT network transmission and the information is mandatory in the EFTS report. |
| :33B: | Currency code, instructed amount | 3!a15d | This specifies the currency and amount of the instruction, for information purposes. It is required when a currency conversion or exchange has occurred on the sender's side.  For example, it might be presented as follows:   * USD3614,33 or * CAD17539,   This currency code is optional for a SWIFT network transmission. |
| :36: | Exchange rate | 12d | This is to provide the exchange rate used to convert the original ordered amounts specified in 33B.  The exchange rate is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :50: | Ordering customer | See Comment column for applicable format | This specifies the customer ordering the transaction. There are two options in the SWIFT network transmission for ordering customer as follows:  **Option K**  Line  Account  Name and address  Format  [/34x]  4\*35x  Only **Option K** provides the information that you have to make reasonable efforts to provide in your report to FINTRAC, i.e., the ordering client's full name and address and account number (if an account is applicable). |
| :51A: | Sending institution | See Comment column for applicable format | This identifies the sender of the message.  Option A in the SWIFT network transmission for sending institution includes the following:  Line  Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  The sending institution is optional on the SWIFT network transmission. For your report to FINTRAC, you have to make reasonable efforts to provide either the bank identification code (BIC) or the full name and address of the individual or entity sending the payment instructions for the EFT. |
| :52: | Ordering institution | See Comment column for applicable format | There are two options for ordering institution in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The ordering institution is optional on the SWIFT network transmission. However, if there is an ordering institution for the EFT, you have to make reasonable efforts to provide part of the information in **either option A or D** for your report to FINTRAC. The information required in your report is **either** the bank identification code (BIC) **or** the full name and address of the individual or entity ordering the payment instructions for the EFT on behalf of a client. |
| :53: | Sender's correspondent | See Comment column for applicable format | There are three options for sender's correspondent in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The sender's correspondent is optional on the SWIFT network transmission. However, if there is a sender's correspondent for the EFT, you have to make reasonable efforts to provide part of the information in **either option A or D** for your report to FINTRAC. The information required in your report is **either** the bank identification code (BIC) **or** the full name and address of the individual or entity (other than the sender) acting as reimbursement bank for the sender of the EFT (if applicable). |
| :54: | Receiver's correspondent | See Comment column for applicable format | There are three options for receiver's correspondent in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The receiver's correspondent is optional on the SWIFT network transmission. However, if there is a receiver's correspondent for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC.  You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the individual or entity acting as reimbursement bank for the receiver of the EFT (if applicable). |
| :55: | Third reimbursement institution | See Comment column for applicable format | There are three options for third reimbursement institution in the SWIFT network transmission as follows:  **Option A**  Line  Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The third reimbursement institution is optional on the SWIFT network transmission. However, if there is a third reimbursement institution for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the EFT receiver's branch, if the funds are made available to the receiver's branch through a financial institution other than the sender's correspondent (if applicable). |
| :56: | Intermediary | See Comment column for applicable format | There are three options for intermediary in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The intermediary is optional on the SWIFT network transmission. However, if there is an intermediary for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the financial institution through which the transaction must pass (the financial institution between the receiver and the financial institution where the account is held) (if applicable). |
| :57: | Account with institution | See Comment column for applicable format | There are four options for account with institution in the SWIFT network transmission as follows:  **Option A**  Line  [//national clearing system code] Party identifier  BIC  Format  [/1!a][/34x]  4!a2!a2!c[3!c]  **Option D**  Line  [//national clearing system code] Party identifier  Name and address  Format  [/1!a][/34x]  4\*35x  The account with institution is optional on the SWIFT network transmission. However, if there is a beneficiary customer account institution for the EFT, part of the information in **either option A or D** is mandatory for your report to FINTRAC. You must provide in your report **either** the bank identification code (BIC) **or** the full name and address of the financial institution that services the account for the beneficiary customer (if this financial institution is not the receiver) (if applicable). |
| :59: | Beneficiary customer | See Comment column for applicable format | There are two options for beneficiary customer in the SWIFT network transmission as follows:  **Option sans lettre**  Line  [//national clearing system code] Account  Name and address  Format  [/34x]  4\*35x  **Option F**  Line  [//national clearing system code] Account  Name and address  Format  [/34x]  4 \* 1!n/33x  FINTRAC's report format requires four lines with no more than 35 characters per line. Explicitly end lines with carriage return, line feeds (<CRLF>). Do not use automatic wrapping of lines at 35.  There is another option for beneficiary customer in the SWIFT network transmission: Option A (national clearing system code, account and BEI). However, only the **no letter** **option and option F** provide the information that is mandatory for your report to FINTRAC, i.e., the beneficiary client's full name and address and account number (if an account is applicable). |
| :70: | Remittance information | 4\*35x | This contains transaction detail narrative for the beneficiary customer.  The remittance information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :71A: | Details of charges | 3!a | This identifies the type of operation. Codes are as follows:   * BEN – Charges borne by beneficiary * OUR – Charges borne by sender * SHA – Ordering customer for sender's charges or beneficiary customer for the receiver's charges   Details of charges are required for a SWIFT network transmission and therefore must be provided in your report to FINTRAC, as this information is a reasonable efforts field in the EFTS report. |
| :71F: | Sender's charges | 3!a15d | This repetitive field specifies the currency and amount of the transaction charges due to the sender.  The sender's charges are optional for a SWIFT network transmission and are a reasonable efforts field in your report to FINTRAC. |
| :71G: | Receiver's charges | 3!a15d | This specifies the currency and amount of the transaction charges due to the receiver.  The receiver's charges are optional for a SWIFT network transmission and are a reasonable efforts field in your report to FINTRAC. |
| :72: | Sender-to-receiver information | 6\*35x. See Comment column for additional details | This specifies additional information for the receiver or another party specified:  Line  Line 1 – (Code)(Narrative)  Lines 2 to 6 – (Narrative) or (Code)(Narrative)  Format  /8a/[additional]  [//more info] or [/8a/[additional]]  /8a/ contains codes for:   * Account with institution * Instructing institution to sending institution * Intermediary institution * Receiver institution   The sender-to-receiver information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :77B: | Regulatory reporting | 3\*35x. See Comment column for additional details | This specifies the codes for the statutory or regulatory information required by the authorities in the country of the receiver or the sender.  Line  Line 1 – (Code)(Country)(Narrative)  Lines 2 to 6 – (Narrative)  Format  /8a/2!a[//info]  [//more info]  The regulatory reporting information is optional for a SWIFT network transmission and is a reasonable efforts field in your report to FINTRAC. |
| :77T: | Envelope contents | 9000z | This contains extended remittance information in different formats. One of the following codes may be used between slashes:   * /UEDI/ - message in UN-EDIFACT format * /ANSI/ - message in ANSI/X12 format * /SWIF/ - message matches structure proposed in field 70 * /NARR/ - message is narrative text   The envelope contents are optional for a SWIFT network transmission. This is a reasonable efforts field in your report to FINTRAC. |
|  | Group terminator | 2x | -}<CRLF> |

#### 5.2.3 Example of an outgoing SWIFT EFT report submitted by batch

```

1A850EFTS0004567SMITH               JOHN           416-555-5555        0000012345678902005071923155500001A000010000103P¶
1B00001ABC AND COMPANY          00001¶
0:0000112345678901234567890A0001234A02831         0¶
{1:F01FIOMCATTATOR3745200184}{2:I103FISXHKSSAXXXN2020}{4:¶
:20:3952232095012¶
:23B:CRED¶
:32A:021027USD12461,4¶
:33B:CAD15327,03¶
:50K:/12345678¶
COMPANY XYZ¶
333 RIVER ROAD W¶
TORONTO ON CA M5N2W7¶
:52:FINANCIAL INSTITUTION NAME¶
123 MAIN ST¶
SWIFT CURRENT MB CA R6S7G4¶
:57D:/FW999999999¶
FOREIGN BANK NAME¶
1301 25 EMPIRE ROAD¶
FEDERATION SQARE¶
NY NY 12345¶
:59F:/33555-232¶
1/MR SOMEONE¶
2/229 WINDMILL ST NW¶
3/US/NEW YORK, NY 10017¶
:70:INVOICE SJ6633344¶
:71A:SHA¶
-}¶
1C00001¶
```

In the example above, the symbol "**¶**" represents the required carriage return, line feed (<CRLF>).

The presentation shown above for the SWIFT headers information has the basic header, application header and the signal for the beginning of the message text on the same line ({1:F01FIOMCATTATOR3745200184}{2:I103FISXHKSSAXXXN2020}{4:**¶**). That part of your report can also be presented with <CRLF> between each of those fields (see the example in Section 5.2.4).

#### 5.2.4 Example of an incoming SWIFT EFT report submitted by batch

```

1A850EFTS0004567SMITH               JOHN           416-555-5555        0000012345678902005071923155500001A000010000103P¶
1B00001ABC AND COMPANY          00001¶
0:00001EFT2734             A00123452355           0¶
{1:F01BANKCABBAXXX1234123456}¶
{2:O1032056050813BANKUSNYAXXX12341234560508131201N}¶
{4: ¶
:20:AB123456789¶
:23B:CRED¶
:32A:050812CAD15750,00¶
:33B:USD12915,¶
:36:1,2195¶
:50K:COMPANY NAME INC¶
123 MAIN STREET W¶
MIAMI FL USA 12345-1234¶
:52D:/FW123 456 789¶
US BANK NAME¶
CONSTITUTION SQUARE¶
55 MAIN STREET¶
PHILIDELPHIA PA USA 12345¶
:57D:CANADIAN BANK NAME¶
1700 RIVERSIDE DRIVE NW¶
WINNIPEG MB CANADA X0X0X0¶
:59F:/1234567¶
1/JOHN DOE¶
2/306 222 MAIN ST¶
3/CA/BRANDON, MB X0X0X0¶
:71A:SHA¶
:72:/REC/REF:INVOICE 12345¶
//DATED 20050713¶
-}¶
1C00001¶
```

In the example above, the symbol " **¶** " represents the required carriage return, line feed (<CRLF>).

The presentation shown above for the SWIFT header information separates the basic header, application header and the signal for the beginning of the message text (i.e., the three lines beginning with "{1:", "{2:" and "{4:").  That part of your report can also be presented without the carriage return, line feed between each of those fields (see the example in Section 5.2.3).

## 6 Acknowledgement Formatting

The following charts provide details on how FINTRAC acknowledgement files are formatted for SWIFT batches submitted to FINTRAC.

### 6.1 Detailed specification layout –Batch acknowledgement

#### 6.1.1 Acknowledgement layout

The following tables outline the format for the acknowledgement messages returned to you once a batch has been processed by FINTRAC. All tag fields are three characters, left justified and space-filled.

**Section A: Information about the submitted batch file**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
| **A** | Acknowledgement title | X(129)LJ | "Your batch has been processed. / Votre lot a été traité. " |
| Separator | X(132) | Spaces |
| **A2** | Report type |  |  |
| Description | X(37)LJ | "Report type / Genre de déclaration" |
| Variable indicator | X(2)LJ | ": " |
| Report type value | X(4)LJ | "EFTS" SWIFT EFT report batch |
| Filler | X(86)LJ | Spaces |
| **A3** | Batch type |  |  |
| Description | X(37)LJ | "Batch type / Catégorie de lot" |
| Variable indicator | X(2)LJ | ": " |
| Batch type value | X(1)LJ | "A"  Add batch  "C"  Correction batch |
| Filler | X(89)LJ | Spaces |
| **A4** | Operational mode |  |  |
| Description | X(37)LJ | "Operational mode / Mode opérationnel" |
| Variable indicator | X(2)LJ | ": " |
| Mode value | X(1)LJ | "P"  Production  "T"  Test |
| Filler | X(89)LJ | Spaces |
| **A5** | Date batch processed |  |  |
| Description | X(65)LJ | "Date processed by FINTRAC / Date de traitement par CANAFE" |
| Variable indicator | X(2)LJ | ": " |
| Processing date | 9(8)LJ | YYYYMMDD |
| Filler | X(54)LJ | Spaces |
| **A6** | Time batch processed |  |  |
| Description | X(65)LJ | "Time batch processed by FINTRAC / Heure de traitement par CANAFE" |
| Variable indicator | X(2)LJ | ": " |
| Processing time | 9(6)LJ | HHMMSS |
| Filler | X(56)LJ | Spaces |

**Section B: Batch ID messages**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **B** | Section title | X(129)LJ | "Batch ID / Identification du lot" |
| **B2** | Batch date |  |  |
| Description | X(65)LJ | "Date / Date" |
| Variable indicator | X(2)LJ | ":" |
| Batch date | 9(8) | YYYYMMDD |
| Filler | X(54)LJ | Spaces |
| **B3** | Batch time |  |  |
| Description | X(65)LJ | "Time / Heure" |
| Variable indicator | X(2)LJ | ":" |
| Batch time | 9(6) | HHMMSS |
| Filler | X(56)LJ | Spaces |
| **B4** | Batch sequence ID |  |  |
| Description | X(65)LJ | "Batch sequence ID / Numéro séq. d'identification du lot" |
| Variable indicator | X(2)LJ | ": " |
| Batch sequence ID | 9(5)RJZ | The unique and entity-created numeric sequence ID for the batch (unique to the reporting entity) |
| Filler | X(57)LJ | Spaces |

**Section C: Batch processing messages**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **C** | Section title | X(129)LJ | "Batch processing messages / Messages portant sur le traitement du lot" |
| **C2** | Batch status message | X(129) | "Batch accepted / Lot accepté"  or  "Batch rejected – invalid format / Lot rejeté – format incorrect" |
| **C3** | Sub-headers accepted |  |  |
| Description | X(65)LJ | "Sub-headers accepted / Sous-en-têtes de lot acceptés" |
| Variable indicator | X(2)LJ | ": " |
| Sub-header accepted count | 9(5)RJZ | Number of sub-headers successfully processed |
| Filler | X(57)LJ | Spaces |
| **C4** | Reports rejected |  |  |
| Description | X(65)LJ | "Reports rejected / Déclarations rejetées" |
| Variable indicator | X(2)LJ | ": " |
| Reports rejected count | X(5)LJ | Number of reports rejected |
| Filler | X(57)LJ | Spaces |
| **C4** | Duplicate reports ignored |  |  |
| Description | X(65)LJ | "Duplicate reports ignored / Déclarations en double mises de côté" |
| Variable indicator | X(2)LJ | ": " |
| Duplicate reports count | X(5)LJ | Number of duplicate reports ignored |
| Filler | X(57)LJ | Spaces |
| **C4** | Reports deleted |  | This applies only for a batch type "C" acknowledgement if reports have been deleted. |
| Description | X(65)LJ | "Reports deleted / Déclarations supprimées " |
| Variable indicator | X(2)LJ | ": " |
| Reports deleted count | X(5)LJ | Number of reports deleted |
| Filler | X(57)LJ | Spaces |
| **C4** | New reports accepted |  |  |
| Description | X(65)LJ | "New reports accepted / Nouvelles déclarations acceptées" |
| Variable indicator | X(2)LJ | ": " |
| New reports count | X(5)LJ | Number of new reports accepted |
| Filler | X(57)LJ | Spaces |
| **C4** | Total reports processed |  | For a batch type "C" acknowledgement, this would include the number of reports changed and the number of reports deleted. |
| Description | X(65)LJ | "Total reports processed / Nombre de déclarations traitées" |
| Variable indicator | X(2)LJ | ":" |
| Reports processed count | X(5)LJ | Number of reports successfully processed |
| Filler | X(57)LJ | Spaces |
| **C5** | Reject legend A | X(129)LJ | "A = Sub-header sequence number / Numéro séquentiel du sous-en-tête" (for a rejected batch only) |
| **C5** | Reject legend B | X(129)LJ | "B = Report sequence number / Numéro séquentiel de la déclaration" (for a rejected batch only) |
| **C5** | Reject legend C | X(129)LJ | "C = RE report reference number / Numéro de référence de la déclaration de l'ED" (for a rejected batch only) |
| **C5** | Reject legend D | X(129)LJ | "D = SWIFT session number / Numéro de la séance SWIFT" (for a rejected batch only) |
| **C5** | Reject legend E | X(129)LJ | "E = SWIFT sequence number / Numéro de la séquence SWIFT" (for a rejected batch only) |
| **C5** | Reject legend F | X(129)LJ | "F = Field / Champ" (for a rejected batch only) |
| **C5** | Reject legend G | X(129)LJ | "G = Reject code / Code de rejet" (for a rejected batch only) |
| **C5** | Reject legend | X(129)LJ | "\* = Reject indicator / Indicateur de rejet" (for a rejected batch only) |
| **C5** | Message header | X(129)LJ | "   A       B               C              D      E        F        G" (for a rejected batch only) |
| **C6** | Validation message |  | **This is a repeating row.** (for a rejected batch only) |
| Variable indicator | X(2)LJ | ": " |
| Sub-header sequence number (A) | X(5)LJ | Sequence number of the sub-header within the batch file (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Report sequence number (B) | X(5)LJ | Sequence number of the report within the batch file (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Reporting entity report reference number (C) | X(20)LJ | Unique reference number assigned by the reporting entity to the report (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| SWIFT session number (D) | X(4)LJ | Session number for the SWIFT message in the report (from the SWIFT basic header) (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| SWIFT session sequence number (E) | X(6)LJ | Session sequence number for the SWIFT message in the report (from the SWIFT basic header) (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Field number (F) | X(6)LJ | Field number in the report resulting in the reject condition (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Reject message number (G) | 9(3)LJ | Message number identifying the reason the batch was rejected by FINTRAC (for a rejected batch only). See Section 8 for more information about these message codes. |
| Reject indicator | X(1)LJ | "\*" |
| Filler | X(59)LJ | Spaces |

**Section D: Messages on accepted reports, reports in error and reports rejected**  
(for accepted batches only)

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **D** | Section title | X(129)LJ | "Messages on accepted reports, reports in error and reports rejected" |
| **D** | Section title | X(129)LJ | "Messages portant sur les décl. acceptées, avec des erreurs et rejetées" |
| **D** | Legend A | X(129)LJ | "A = Sub-header / Sous-en-tête" |
| **D** | Legend B | X(129)LJ | "B = Report sequence / Séquence de la déclaration" |
| **D** | Legend C | X(129)LJ | "C = RE report reference number/Numéro de référence de la déclaration de l'ED" |
| **D** | Legend D | X(129)LJ | "D = SWIFT session number / Numéro de la séance SWIFT" |
| **D** | Legend E | X(129)LJ | "E =SWIFT sequence number / Numéro de la séquence SWIFT" |
| **D** | Legend F | X(129)LJ | "F = Field / Champ" |
| **D** | Legend G | X(129)LJ | "G = Message code / Code de message" |
| **D** | Legend | X(129) | "\*  = Reject indicator / Indicateur de rejet" |
| **D** | Legend H | X(129)LJ | "H = Validation rule number / Numéro de la règle de validation " |
|  | Separator | X(132) | Spaces |
| **D** | Message header | X(129)LJ | "   A       B               C              D      E        F        G      H" |
| **D2** | Validation message |  | **This is a repeating row.** |
| Variable indicator | X(2)LJ | ": " |
| Sub-header number (A) | X(5)LJ | Sub-header to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| Report sequence number (B) | X(5)LJ | Report sequence number to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| Reporting entity report reference number (C) | X(20)LJ | Reporting entity report reference number to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| SWIFT session number (D) | X(4)LJ | SWIFT session number in a report to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| SWIFT session sequence number (E) | X(6)LJ | SWIFT session sequence number in a report to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| Field number (F) | X(6)LJ | Field number identifier in a report to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| Validation message (G) | 9(3)LJ | The validation message related to the identified field.  See section 8.2 for information about these message codes. |
| Reject indicator | X(1)LJ | "\*" |
| Variable indicator | X(3)LJ | " : " |
| Validation rule number (H) | 9(9)LJ | This is the validation rule number identifying the issue in the report. See section 8.1 for information about these rule numbers. |
| Filler | X(47)LJ | Spaces |

**Section E: Sub-header and report processing totals**  
(for accepted batches only)

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **E** | Section title | X(129)LJ | "Accepted sub-header and report processing totals" |
| **E** | Section title | X(129)LJ | "Nombre de sous-en-têtes acceptés et de déclarations traitées avec succès " |
| **E** | Section title | X(129)LJ | "Sub-header           Report count" |
| **E** | Section title | X(129)LJ | "Sous-en-tête         Nombre de déclarations" |
| **E2** | Sub-header and report counts |  | **This is a repeating row.** |
| Variable indicator | X(2)LJ | ": " |
| Sub-header sequence number | X(5)LJ | Sequence of the sub-header in the batch successfully processed |
| Filler | X(12)LJ |  |
| Variable indicator | X(2)LJ | ": " |
| Reports in sub-header count | X(5)LJ | Number of reports in sub-header successfully processed |
| Filler | X(103)LJ | Spaces |

**Section F: End of report**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **F** | Section title | X(129)LJ | "End of report / Fin du rapport" |
| Filler | X(132)LJ | "============================================================================" |
| Filler | X(132)LJ | "Legend / Légende" |
| Filler | X(132)LJ | "A   Section contains summary of the batch processed" |
| Filler | X(132)LJ | "A   Cette section présente des renseignements sur le traitement du lot" |
| Filler | X(132)LJ | "A2  Report type contained in the batch / Genre de décl. comprises dans le lot" |
| Filler | X(132)LJ | "A3  Batch type / Catégorie de lot" |
| Filler | X(132)LJ | "A4  Operational mode / Mode opérationnel" |
| Filler | X(132)LJ | "A5  Date processed by FINTRAC / Date de traitement par CANAFE" |
| Filler | X(132)LJ | "A6  Time processed by FINTRAC / Heure de traitement par CANAFE" |
| Filler | X(132)LJ | Spaces |
| Filler | X(132)LJ | "B   Section contains batch identification details" |
| Filler | X(132)LJ | "B   Cette section présente des renseignements sur l'identification du lot" |
| Filler | X(132)LJ | "B2  Date provided in the batch header / Date indiquée dans l'en-tête de lot" |
| Filler | X(132)LJ | "B3  Time provided in the batch header / Heure indiquée dans l'en-tête de lot" |
| Filler | X(132)LJ | "B4  Seq. provided in the batch header / Séq. indiquée dans l'en-tête de lot" |
| Filler | X(132)LJ | Spaces |
| Filler | X(132)LJ | "C   Section contains batch processing results" |
| Filler | X(132)LJ | "C   Cette section présente les résultats du traitement du lot" |
| Filler | X(132)LJ | "C2  Batch acceptance or reject message / Message d'acceptation ou de rejet du lot" |
| Filler | X(132)LJ | "C3  Number of sub-headers accepted / Nombre de sous-en-têtes acceptés" |
| Filler | X(132)LJ | "C4  Number of reports rejected / Nombre de déclarations rejetées" |
| Filler | X(132)LJ | "C4  Number of duplicate reports ignored / Nombre de décl. en double mises de côté" |
| Filler | X(132)LJ | "C4  Number of reports deleted / Nombre de déclarations supprimées" |
| Filler | X(132)LJ | "C4  Number of new reports accepted / Nombre de nouvelles déclarations acceptées" |
| Filler | X(132)LJ | "C4  Number of reports processed / Nombre de déclarations traitées" |
| Filler | X(132)LJ | "C5  Rejected batch legend / Légende de rejet de lot" |
| Filler | X(132)LJ | "C6  Rejected batch messages / Messages de rejet de lot" |
| Filler | X(132)LJ | Spaces |
| Filler | X(132)LJ | "D   Section contains validation messages for reports" |
| Filler | X(132)LJ | "D   Cette section présente les messages de validation des déclarations" |
| Filler | X(132)LJ | "D2  Validation messages for report fields (repeating message line)" |
| Filler | X(132)LJ | "D2  Messages de validation des champs de la décl. (ligne répétitive du message)" |
| Filler | X(132)LJ | Spaces |
| Filler | X(132)LJ | "E   Section contains the total number of reports per sub-header in the batch" |
| Filler | X(132)LJ | "E   Cette section présente le nombre total de déclarations incluses dans chaque" |
| Filler | X(132)LJ | "E     sous-en-tête de lot" |
| Filler | X(132)LJ | "E2  For each sub-header, the number of reports (repeating message line)" |
| Filler | X(132)LJ | "E2  Nombre de déclarations par sous-en-tête (ligne répétitive du message)" |
| Filler | X(132)LJ | Spaces |
| Filler | X(132)LJ | "F   Section indicates the end of the acknowledgement messages" |
| Filler | X(132)LJ | "F   Cette section indique la fin des messages de l'accusé de réception" |
| Filler | X(132)LJ | "============================================================================" |

Note: The legend will be sent with all acknowledgements.

#### 6.1.2 Acknowledgement examples

##### 6.1.2.1 Acknowledgement example for an accepted batch

Note: Due to space constraints this example is not padded to 132 characters.

```

A  Your batch has been processed. / Votre lot a été traité.

A2 Report type / Genre de déclaration	: EFTS 
A3 Batch type  / Catégorie de lot		: A 
A4 Operational mode / Mode opérationnel	: P
A5 Date batch processed by FINTRAC / Date de traitement par CANAFE  : 20050723
A6 Time batch processed by FINTRAC / Heure de traitement par CANAFE : 041733

B  Batch ID / Identification du lot				
B2 Date / Date									  : 20050722
B3 Time / Heure									  : 234527
B4 Batch sequence ID / Numéro séq. d'identification du lot		  : 00003

C  Batch processing messages / Messages portant sur le traitement du lot
C2 Batch accepted / Lot accepté
C3 Sub-headers accepted / Sous-en-têtes de lot acceptés		  : 00001
C4 Reports rejected / Déclarations rejetées				  : 1
C4 Duplicate reports ignored / Déclarations en double mises de côté : 0
C4 Reports deleted / Déclarations supprimées				  : 0
C4 New reports accepted / Nouvelles déclarations acceptées		  : 3
C4 Total reports processed / Nombre de déclarations traitées	  : 4

D  Messages on accepted reports, reports in error and reports rejected
D  Messages portant sur les décl. acceptées, avec des erreurs et rejetées
D  A = Sub-header / Sous-en-tête
D  B = Report sequence / Séquence de la déclaration
D  C = RE report reference number/Numéro de référence de la déclaration de l'ED  
D  D = SWIFT session number / Numéro de la séance SWIFT
D  E = SWIFT sequence number / Numéro de la séquence SWIFT
D  F = Field / Champ
D  G = Message code / Code de message
D  * = Reject indicator / Indicateur de rejet
D  H = Validation rule number / Numéro de la règle de validation

D     A       B               C              D      E        F        G      H                                                    
D2 : 1     : 1     : Report97000000       : 1    : 2      : 51a.1  : 320* : 92345

E  Accepted sub-header and report processing totals
E  Nombre de sous-en-têtes acceptés et de déclarations traitées avec succès
E  Sub-header	      Report count
E  Sous-en-tête	      Nombre de déclarations
E2 : 1		      : 3

F  End of report / Fin du rapport
============================================================================ 
Legend / Légende

A   Section contains summary of the batch processed
A   Cette section présente des renseignements sur le traitement du lot 
A2  Report type contained in the batch / Genre de décl. comprises dans le lot
A3  Batch type / Catégorie de lot
A4  Operational mode / Mode opérationnel
A5  Date processed by FINTRAC / Date de traitement par CANAFE
A6  Time processed by FINTRAC / Heure de traitement par CANAFE

B   Section contains batch identification details
B   Cette section présente des renseignements sur l'identification du lot
B2  Date provided in the batch header / Date indiquée dans l'en-tête de lot
B3  Time provided in the batch header / Heure indiquée dans l'en-tête de lot
B4  Seq. provided in the batch header / Séq. indiquée dans l'en-tête de lot

C   Section contains batch processing results
C   Cette section présente les résultats du traitement du lot 
C2  Batch acceptance or reject message/Message d'acceptation ou de rejet du lot 
C3  Number of sub-headers accepted / Nombre de sous-en-têtes acceptés
C4  Number of reports rejected / Nombre de déclarations rejetées
C4  Number of duplicate reports ignored / Nombre de décl. en double mises de côté
C4  Number of reports deleted / Nombre de décl. supprimées 
C4  Number of new reports accepted / Nombre de nouvelles déclarations acceptées
C4  Number of reports processed / Nombre de déclarations traitées
C5  Rejected batch legend / Légende de rejet de lot
C6  Rejected batch messages / Messages de rejet de lot

D   Section contains validation messages for reports
D   Cette section présente les messages de validation des déclarations
D2  Validation messages for report fields (repeating message line)
D2  Messages de validation des champs de la décl.(ligne répétitive du message)

E   Section contains the total number of reports per sub-header in the batch
E   Cette section présente le nombre total de déclarations incluses dans chaque
E     sous-en-tête de lot
E2  For each sub-header, the number of reports (repeating message line)
E2  Nombre de déclarations par sous-en-tête (ligne répétitive du message)

F   Section indicates end of the acknowledgement messages
F   Cette section indique la fin des messages de l'accusé de réception

```

## 7 Reports Returned for Further Action Message Formatting

The following charts provide details on how the message files from FINTRAC about reports returned for further action (RRFA) are formatted.

### 7.1 Detailed specification layout – RRFA message

#### 7.1.1 General RRFA message layout

The following tables outline the format for RRFA messages that will be sent to you by FINTRAC if you choose to deal with RRFA by batch for reports that were originally submitted by batch. All tag fields are three characters, left justified and space-filled.

**Section A: Introduction of RRFA**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
| **A** | RRFA introduction | X(129)LJ | "Please review and correct the following report(s):" |
| RRFA introduction | X(129)LJ | "Veuillez réviser et corriger la ou les déclaration(s) suivante(s) :" |
| Separator | X(132) | Spaces |
| **A2** | Report type |  |  |
| Description | X(37)LJ | "Report type / Genre de déclaration" |
| Variable indicator | X(2)LJ | ": " |
| Report type value | X(4)LJ | "EFTS" SWIFT EFT report |
| Filler | X(86)LJ | Spaces |
| **A3** | Date RRFA issued |  |  |
| Description | X(65)LJ | "Date issued by FINTRAC / Date d'envoi par CANAFE" |
| Variable indicator | X(2)LJ | ": " |
| Processing date | 9(8)LJ | YYYYMMDD |
| Filler | X(54)LJ | Spaces |

**Section B: RRFA ID**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **B** | Section title | X(129)LJ | "RRFA identification / Identification de la DRM" |
| **B2** | RRFA ID number |  |  |
| Description | X(65)LJ | "RRFA number / Numéro de la DRM" |
| Variable indicator | X(2)LJ | ": " |
| RRFA ID number | 9(9)LJ | FINTRAC's numeric ID for the RRFA |
| Filler | X(53)LJ | Spaces |
| **B3** | Number of batches involved |  |  |
| Description | X(65)LJ | "Number of batches involved / Nombre de lots impliqués" |
| Variable indicator | X(2)LJ | ": " |
| Number of batches involved | 9(5)LJ | The number of batches across which reports are returned in this RRFA |
| Filler | X(57)LJ | Spaces |
| **B4** | Number of reports returned |  |  |
| Description | X(65)LJ | "Number of reports returned / Nombre de déclarations retournées" |
| Variable indicator | X(2)LJ | ": " |
| Number of reports returned | 9(5)LJZ | The number of reports included in this RRFA |
| Filler | X(57)LJ | Spaces |
| **B5** | Number of quality issues |  |  |
| Description | X(65)LJ | "Number of quality issues / Nombre de problèmes de qualité" |
| Variable indicator | X(2)LJ | ": " |
| Number of quality issues | 9(9)LJZ | The total number of data quality issues for all reports included in this RRFA |
| Filler | X(53)LJ | Spaces |

**Section C: Data quality issues messages**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **C** | Section title | X(129)LJ | "Data quality issues / Problèmes de qualité " |
| **C2** | Quality issue legend A | X(129)LJ | "A = RE's identifier number / Numéro d'identification de l'ED" |
| **C2** | Quality issue legend B | X(129)LJ | "B = Batch date / Date du lot" |
| **C2** | Quality issue legend C | X(129)LJ | "C = Batch time / Heure du lot" |
| **C2** | Quality issue legend D | X(129)LJ | "D = Batch sequence ID / Numéro séq. d'identification du lot |
| **C2** | Quality issue legend E | X(129)LJ | "E = RE report reference number / Numéro de référence de déclaration de l'ED" |
| **C2** | Quality issue legend F | X(129)LJ | "F = Field / Champ " |
| **C2** | Quality issue legend G | X(129)LJ | "G = SWIFT session number / Numéro de la séance SWIFT" |
| **C2** | Quality issue legend H | X(129)LJ | "H = SWIFT sequence number / Numéro de la séquence SWIFT" |
| **C2** | Quality issue legend I | X(129)LJ | "I  = Quality issue code / Code du problème de qualité" |
|  | Separator | X(132) | Spaces |
| **C3** | Message header | X(129)LJ | "      A          B         C       D              E               F      G       H       I" |
| **C4** | RRFA message |  | **This is a repeating row.** |
| Variable indicator | X(3)LJ | " : " |
| Reporting entity's identifier number (A) | 9(7)LJ | Reporting entity's identifier number |
| Variable indicator | X(3)LJ | " : " |
| Batch date (B) | 9(8) | Batch date |
| Variable indicator | X(3)LJ | " : " |
| Batch time (C) | 9(6) | Batch time |
| Variable indicator | X(3)LJ | " : " |
| Batch sequence ID (D) | 9(5)RJZ | The unique and entity-created numeric sequence ID for the batch in which the returned report was originally submitted |
| Variable indicator | X(3)LJ | " : " |
| Reporting entity report reference number (E) | X(20) | Unique reference number assigned by the reporting entity to the report returned |
| Variable indicator | X(3)LJ | " : " |
| Field number (F) | X(5)LJ | Field number in the returned report to which the data quality issue message relates |
| Variable indicator | X(3)LJ | " : " |
| SWIFT session number (G) | X(4)LJ | The SWIFT  session number of the returned report to which the data quality message relates |
| Variable indicator | X(3)LJ | " : " |
| SWIFT sequence number (H) | X(6)LJ | SWIFT sequence number of the returned report to which the data quality message relates |
| Variable indicator | X(3)LJ | " : " |
| Data quality message number (I) | 9(3)LJ | Message number identifying the quality issue applicable. See Section 8 for more information about the data quality issue messages. |
| Filler | X(38)LJ | Spaces |

**Section D: End of report**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **D** | Section title | X(129)LJ | "End of report / Fin du rapport" |
| Filler | X(132)LJ | "==============================================================================================" |

#### 7.1.2 RRFA message example

Note: Due to space constraints this example is not padded to 132 characters.

```

A  Please review and correct the following report(s):
A  Veuillez réviser et corriger la ou les déclaration(s) suivante(s) :

A2 Report type / Genre de déclaration		     : EFTS
A3 Date issued by FINTRAC / Date d'envoi par CANAFE  : 20060523

B  RRFA identification / Identification de la DRM
B2 RRFA number / Numéro de la DRM						  : 99
B3 Number of batches involved / Nombre de lots impliqués		  : 2
B4 Number of reports returned / Nombre de déclarations retournées	  : 4
B5 Number of corrections required / Modifications à apporter	  : 5

C  Data quality issues / Problèmes de qualité 
C2 A = RE's identifier number / Numéro d'identification de l'ED
C2 B = Batch date / Date du lot 
C2 C = Batch time / Heure du lot 
C2 D = Batch sequence ID / Numéro séq. d'identification du lot
C2 E = RE report reference number / Numéro de référence de déclaration de l'ED
C2 F = Field number / Numéro de champ
C2 G = SWIFT session number / Numéro de la séance SWIFT
C2 H = SWIFT sequence number / Numéro de la séquence SWIFT
C2 I = Quality issue code / Code du problème de qualité

C3       A          B         C       D              E               F      G       H       I
C4  : 1211379 : 20061028 : 000523 : 00003 : XT007889944100       : :50:   : 0001 : 000002 : 329

D  End of report / Fin du rapport
=================================================================================================== 

```

## 8 Report Validation and Processing Error Codes

### 8.1 Report validation rules

Report validation rules apply at the field level to reports within an accepted batch to ensure that reports are error-free (i.e., they contain the required fields, the fields are formatted correctly, and the data is valid). Validation messages returned in Section D of the batch acknowledgement file identify rejected reports or provide warnings about accepted reports based on these validation rules.

A report validation rules table is available for download in the technical documentation area of the publications section of FINTRAC's website at [https://fintrac-canafe.canada.ca](/intro-eng). The table provides a description of the validation applied to each field within the reports.

### 8.2 Batch error codes

Batch processing error codes are returned in Section C (for a rejected batch) and Section D (for an accepted batch) of the batch acknowledgement file. Error codes are also found in Section C of the RRFA message to identify quality issues. A code table for these error messages is available for download in the technical documentation area of the publications section of FINTRAC's website at https://fintrac-canafe.canada.ca.

In the error code table, certain error codes (e.g., codes 400 to 439) are used when an entire batch file is **rejected**. In the case of a rejected batch, the error codes in the acknowledgement file will reflect the issues found during our attempt to process the batch. It is possible that there were other errors in the rejected batch that we did not get far enough to detect.

Other error codes (such as 9, 77, 300 to 372, 442 and 978 to 999) apply at the **field** level to reports within an **accepted** batch. These error codes explain why a report was rejected or why a warning message was received about an accepted report.

## 9 Batch File Naming Convention

The following provides batch file naming recommendations to ensure all batch files for a reporting entity have a unique name.

### 9.1 Batch file naming standard

Use the following naming convention for your batch files: Date\_Time\_Report Type.FileExtension

Each element of this naming convention is required, except for the report type, as follows:

* The date is required (YYYYMMDD).
* The time is required (HHMMSS).
* The report type is optional (EFTS).
* The following file extension is required: ".DAT".

Example:         20050722\_223915\_EFTS.DAT

File names may only include standard upper/lower case alphanumeric characters (A to Z and 0 to 9). The only separator allowed is the underscore character "\_".  The file name must only have one dot extension (i.e., .DAT). File names containing spaces will cause the file to be rejected.

In this context, the upper case of any letter is considered the same as the lower case of that letter. For example, a batch file name of 20050722\_223915\_EFTS.DAT is considered the same as 20050722\_223915\_efts.DAT.

All batch files that you submit to FINTRAC must have a unique file name, regardless of the file contents, or the file will be rejected. This is true even if the previously submitted file had been rejected or if you are submitting a correction batch.

### 9.2 FINTRAC batch acknowledgement file naming convention

FINTRAC's acknowledgement file returned to you will be the same name as your original batch file name, but with a different suffix. For batch files with no batch reject or report validation messages the suffix will be ".001". For those files with reject or validation messages, the suffix will be as follows:

* **File\_name.002**: All reports accepted but some warning messages
* **File\_name.004**: Batch accepted but some rejected reports
* **File\_name.005**: Batch rejected for structural reasons (bad file name, invalid contents, report counts do not match, etc.)

### 9.3 RRFA batch file naming convention

The following naming convention will be used by FINTRAC for the RRFA notification file sent to you:

* **RRFA\_DRM\_999999999.txt**

The "999999999" represents the RRFA number reflected in Tag B2 of the RRFA message.

## Appendix 1: Outgoing SWIFT Electronic Funds Transfer Report

Table for Outgoing SWIFT Electronic Funds Transfer Report

| *Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations*   Schedule 2 | Report Tag  (see Section 5.2.1) |
| --- | --- |
| **PART A — Information about the transaction** |  |
| 1.  Time of processing of the transaction | :13C: |
| 2. \*Value date | :32A: |
| 3. \*Amount of the EFT | :32A: |
| 4. \*Currency of the EFT | :32A: |
| 5.  Exchange rate | :36: |
| 6.  Transaction type code | :26T: |
| **PART B — Information about the client ordering the EFT** |  |
| 1. \*Client's full name | :50: |
| 2. \*Client's full address | :50: |
| 3. \*Client's account number, if applicable | :50: |
| **PART C — Information about the individual or entity sending the EFT** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity sending the payment instructions for the EFT | :51A: , FINTRAC header and basic header (block 1) |
| **PART D — Information about the individual or entity ordering an EFT on behalf of a client (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the ordering institution (if applicable) | :52: |
| **PART E — Information about the sender's correspondent (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity (other than the sender) acting as reimbursement bank for the sender of the EFT (if applicable) | :53: |
| **PART F — Information about the receiver's correspondent (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity acting as reimbursement bank for the receiver of the EFT (if applicable) | :54: |
| **PART G — Information about the third reimbursement institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the EFT receiver's branch, if the funds are made available to the receiver's branch through a financial institution other than the sender's correspondent (if applicable) | :55: |
| **PART H — Information about the intermediary institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the financial institution through which the transaction must pass (the financial institution between the receiver and the financial institution where the account is held) (if applicable) | :56: |
| **PART I — Information about the beneficiary customer account institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the financial institution that services the account for the beneficiary customer (if this financial institution is not the receiver) (if applicable) | :57: |
| **PART J — Information about the individual or entity receiving the EFT** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity receiving the payment instructions | Application header (block 2) |
| **PART K — Information about the client to whose benefit payment is made** |  |
| 1. \*Client's full name | :59: |
| 2. \*Client's full address | :59: |
| 3. \*Client's account number, if applicable | :59: |
| **PART L — Additional payment information** |  |
| 1. Remittance information | :70: |
| 2. Details of charges | :71A: and :71G: |
| 3. Sender's charges | :71F: |
| 4. Sender's reference | :20: |
| 5. Bank operation code | :23B: |
| 6. Instruction code | :23E: |
| 7. Sender-to-receiver information | :72: |
| 8. Regulatory reporting | :77B: |
| 9. Envelope contents | :77T: |

**Note**: If the 24-hour rule applies to a SWIFT EFT, and, because of this, information that is mandatory (as indicated in the chart above) was not obtained at the time of the transaction (and is not available from the SWIFT message or your records), you can leave the information out of your report to FINTRAC.

## Appendix 2: Incoming SWIFT Electronic Funds Transfer Report

Table for Incoming SWIFT Electronic Funds Transfer Report

| *Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations*   Schedule 3 | Report Tag  (see Section 5.2.2) |
| --- | --- |
| **PART A — Information about the transaction** |  |
| 1.  Time of processing of the transaction | :13C: |
| 2. \*Value date | :32A: |
| 3. \*Amount of the EFT | :32A: |
| 4. \*Currency of the EFT | :32A:: |
| 5.  Exchange rate | :36: |
| 6.  Transaction type code | :26T: |
| **PART B — Information about the client ordering the EFT** |  |
| 1. Client's full name | :50: |
| 2. Client's full address | :50: |
| 3. Client's account number, if applicable | :50: |
| **PART C — Information about the individual or entity sending the EFT** |  |
| 1. Bank identification code (BIC) or full name and address of the individual or entity sending the payment instructions for the EFT | :51A: and application header (block 2) |
| **PART D — Information about the individual or entity ordering an EFT on behalf of a client**  **(if applicable)** |  |
| 1. Bank identification code (BIC) or full name and address of the ordering institution (if applicable) | :52: |
| **PART E — Information about the sender's correspondent (if applicable)** |  |
| 1. Bank identification code (BIC) or full name and address of the individual or entity (other than the sender) acting as reimbursement bank for the sender of the EFT (if applicable) | :53: |
| **PART F — Information about the receiver's correspondent (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity acting as reimbursement bank for the receiver of the EFT (if applicable) | :54: |
| **PART G — Information about the third reimbursement institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the EFT receiver's branch, if the funds are made available to the receiver's branch through a financial institution other than the sender's correspondent (if applicable) | :55: |
| **PART H — Information about the intermediary institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the financial institution through which the transaction must pass (the financial institution between the receiver and the financial institution where the account is held) (if applicable) | :56: |
| **PART I — Information about the beneficiary customer account institution (if applicable)** |  |
| 1. \*Bank identification code (BIC) or full name and address of the financial institution that services the account for the beneficiary customer (if this financial institution is not the receiver) (if applicable) | :57: |
| **PART J — Information about the individual or entity receiving the EFT** |  |
| 1. \*Bank identification code (BIC) or full name and address of the individual or entity receiving the payment instructions | Basic header (block 1) and FINTRAC header |
| **PART K — Information about the client to whose benefit payment is made** |  |
| 1. Client's full name | :59: |
| 2. Client's full address | :59: |
| 3. Client's account number, if applicable | :59: |
| **PART L — Additional payment information** |  |
| 1. Remittance information | :70: |
| 2. Details of charges | :71A: and :71G: |
| 3. Sender's charges | :71F: |
| 4. Sender's reference | :20: |
| 5. Bank operation code | :23B: |
| 6. Instruction code | :23E: |
| 7. Sender-to-receiver information | :72: |
| 8. Regulatory reporting | :77B: |
| 9. Envelope contents | :77T: |

**Note**: If the 24-hour rule applies to a SWIFT EFT, and, because of this, information that is mandatory (as indicated in the chart above) was not obtained at the time of the transaction (and is not available from the SWIFT message or your records), you can leave the information out of your report to FINTRAC.

### Footnotes

Footnote 1
:   Copyright © S.W.I.F.T. SCRL ("S.W.I.F.T."), Avenue Adèle 1, B-1310 La Hulpe, Belgium

    [Return to footnote 1 referrer](#fn1-rf)

Date Modified:
:   2015-12-03