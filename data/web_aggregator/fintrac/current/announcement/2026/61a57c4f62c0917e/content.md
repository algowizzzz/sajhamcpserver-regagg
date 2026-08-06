# Module 1: General specifications

**Standard ASCII Batch Reporting Instructions and Specifications**  
**May 30, 2015**

## On this page

* [**Changes in this Version**](#s0)

1. **[General Information](#s1)**
2. **[Acceptance Procedures](#s2)**
3. **[Batch Submission, Acknowledgement and Modification](#s3)**
   * 3.1 [Batch type “A”: Add batch](#s3.1)
   * 3.2 [Batch acknowledgements](#s3.2)
     + 3.2.1 [Accepted batch](#s3.2.1)
     + 3.2.2 [Rejected batch](#s3.2.2)
   * 3.3 [Reports returned for further action (RRFA)](#s3.3)
   * 3.4 [Modification](#s3.4)
     + 4.4.1 [Batch type “C”: Correction Batch](#s3.4.1)
     + 3.4.2 [F2R](#s3.4.2)
4. **[General Specifications](#s4)**
   * 4.1 [General format requirements](#s4.1)
   * 4.2 [Mandatory and required fields](#s4.2)
   * 4.3 [Batch process](#s4.3)
5. **[Batch Report Formatting](#s5)**
   * 5.1 [Detailed specification layout – Batch header, sub-header and trailer](#s5.1)
     + 5.1.1 [Samples of batch headers, sub-headers and trailers](#s5.1.1)
   * 5.2 [Batch report format versions 03 and 04](#s5.2)
     + 5.2.1 [Detailed specification layout (format version 04) — STR](#s5.2.1)
     + 5.2.2 [Detailed specification layout (format version 03) — LCTR](#s5.2.2)
     + 5.2.3 [Detailed specification layout (format version 03) — non-SWIFT electronic funds transfer reports](#s5.2.3)
   * 6.3 [Report structure flowcharts](#s5.3)
6. **[Code Tables and Editing Instructions](#s6)**
   * 6.1 [Code tables](#s6.1)
   * 6.2 [Name editing instructions](#s6.2)
7. **[Acknowledgement Formatting](#s7)**
   * 7.1 [Detailed specification layout –batch acknowledgement](#s7.1)
     + 7.1.1 [General acknowledgement layout](#s7.1.1)
     + 7.1.2 [General acknowledgement examples](#s7.1.2)
       - 7.1.2.1 [Acknowledgement example for an accepted batch](#s7.1.2.1)
       - 7.1.2.2 [Acknowledgement example for a rejected batch](#s7.1.2.2)
8. **[Reports Returned for Further Action Message Formatting](#s8)**
   * 8.1 [Detailed specification layout – RRFA message](#s8.1)
     + 8.1.1 [General RRFA message layout](#s8.1.1)
     + 8.1.2 [RRFA Message Example](#s8.1.2)
9. **[Report Validation and Processing Error Codes](#s9)**
   * 9.1 [Report validation rules](#s9.1)
   * 9.2 [Batch error codes](#s9.2)
10. **[Batch File Naming Convention](#s10)**
    * 10.1 [Batch file naming standard](#s10.1)
    * 10.2 [FINTRAC batch acknowledgement file naming convention](#s10.2)
    * 10.3 [RRFA batch file naming convention](#s10.3)

## Changes in this Version

The file formatting specifications in Sections 7 and 8 have changed. The line length has increased from 80 characters to 132 characters. This may require programming changes on your part.

The acknowledgement file formatting specifications in Section 7 have changed to include the validation rule number. This may require programming changes on your part.

The specifications for the reject indicators in Section C6 and Section D2 of the batch acknowledgement message have been changed to reflect what is being generated in the actual message.

The Section 7 accepted batch acknowledgement has been corrected to match the specifications for section D:

* **Current output:**
* D D = SWIFT session number / Numéro de la séance SWIFT
* D E = SWIFT sequence number / Numéro de la séquence SWIFT

* **To be:**
* D D = Transaction / Opération
* D E = Disposition / Répartition

Section 9 has been amended to include information concerning the validation of reports submitted by batch.

## 1. General information

The purpose of this specification document is to provide reporting entities with the requirements and conditions for filing the following reports to the Financial Transactions and Reports Analysis Centre of Canada (FINTRAC) using the **electronic batch file transfer format:**

* Suspicious transaction reports (STR)
* Large cash transaction reports (LCTR)
* Outgoing international non-SWIFT electronic funds transfer reports (EFTO)
* Incoming international non-SWIFT electronic funds transfer reports (EFTI)

The specifications defined in Sections 4, 5 and 6 reflect the file characteristics acceptable for submission of electronic batch reports. These must be adhered to unless replaced by a revision to this specification document.

For module 1 only, rather than use a version number for each revision to the module, revisions will show the publishing date as well as the effective date for the specification change if different from the publishing date.

Each revision of modules 2, 3 and 4 will have a different version number. The change in version number will be according to the extent of changes made.

* **Change in batch report formats supported**  
  If the current version number of Module 2, 3 or 4 were to change by a whole number, for example, from 4.2 to 5.0, this would indicate that the batch report formats supported are being changed. This will signal programming changes for you if you are already submitting reports by batch, as the format you are using would no longer be supported.
* **Change due to legislative amendments**  
  If the revisions to Module 2, 3 or 4 were to contain changes in reporting requirements but none to format, the version number would change by “0.1”. For example, if the version number were to change from “4.2” to “4.3”, this would indicate changes to the reporting requirements based on amendments to the [Proceeds of Crime (Money Laundering) and Terrorist Financing Act](/act-loi/1-eng) (the Act) or the related Regulations. This would signal possible programming changes for you, if there were any changes to the reporting requirements applicable to you.
* **Change due to editorial revisions**  
  If the revisions to Module 2, 3, or 4 contain changes that are simply editorial, the version number would be changed by “0.0.1”, for example, going from “4.2.1” to “4.2.2”. This indicates changes to clarify text or correct any typographical errors. This type of change does not signal any programming changes for you, unless a legislative change or changes in format were also indicated.

If you need to report international electronic funds transfers (EFTs) sent or received as a SWIFT member or sub-member through the SWIFT network, refer to the specification document called [SWIFT Format EFT Transactions Batch Reporting Instructions and Specification](/reporting-declaration/swift/swift-eng) for requirements and conditions for filing those reports to FINTRAC.

This document reflects the provisions of the [Proceeds of Crime (Money Laundering) and Terrorist Financing Act (the Act) and associated Regulations](/act-loi/1-eng). This document is provided as general information only. It is not legal advice, and is not intended to replace the Act and Regulations. For more information about money laundering, terrorist financing or other requirements under the Act and Regulations, including what type of person or entity is a reporting entity, see FINTRAC’s [Obligations and guidance](/guidance-directives/guidance-directives-eng) page.

Throughout this document, any references to dollar amounts (such as $10,000) refer to the amount in Canadian dollars or its equivalent in foreign currency.

## 2. Acceptance procedures

Approval to participate in batch report filing under this version of these specifications is contingent upon the following:

* Enrolment with FINTRAC;
* Completion of the Public Key Infrastructure (PKI) registration process;
* Installation and configuration of the batch transmission software; and
* Successful completion of test submissions in the batch transmission software training channel for each report type to be submitted by batch.

More information about the PKI registration process and batch transmission software installation can be found in the reporting section of FINTRAC's website.

Each time the format changes for one or more report types that you submit by batch, you will need to go through the acceptance procedure of test submissions. For example, effective June 23, 2008, the format for STRs changed from “03” to “04”. This meant that if you submitted STRs by batch at that time, you would have needed to submit test submissions for that report type using the new format.

You (i.e., the transmitter of the batch files) will be asked to perform **test** submissions in the batch transmission software **training channel**, as follows:

* The test data will consist of a set of reports containing the data that you would normally supply. The test file must contain only one batch header, one to five sub-headers, between 25 and 100 reports and only one batch trailer. A minimum of five test files is required.
* The formatting of the batch records must adhere to the specifications explained in Sections 4 and 5. Otherwise, the batch and/or reports will be rejected. If files are unreadable for reasons such as format problems, error messages will be returned identifying the problem(s) through the batch transmission software process.
* Reporting entity location numbers used in test reports data must be valid for the reporting entity. See Part A of STR, Part A of LCTR, Part C of EFTO or Part E of EFTI for more information about these.
* Upon receipt of the test data by FINTRAC, it will be processed and an acknowledgement message, along with any error messages, will be returned to you within two working days.
* If all the reports in four out of five of your test batches are error-free (i.e., they contain the required fields, the file and data fields are formatted correctly and the location numbers are valid), FINTRAC will issue final acceptance for you to begin production submissions. Acceptance will be based on the last five batches submitted to FINTRAC.
* If a test file is incorrectly formatted or test reports contain mandatory field or field format errors, you will have to submit a new set of test data to FINTRAC. You have to correct these errors before FINTRAC will authorize you to submit production reports.

## 3. Batch submission, acknowledgement and modification

Currently, batches may be sent to FINTRAC at any time of the day and any day of the week. All batches received by FINTRAC will be acknowledged (see Section 3.2).

Batches can only contain reports of one type (STR, LCTR, etc.). Although a batch can contain up to 10,000 reports, the physical batch size cannot exceed 30 megabytes, uncompressed.

The batch file must be placed in the directory in which your batch transmission software is configured to look for files for transfer. Batch submissions can be made in one of the two following types:

* Batch type “**A**” — Add a new batch of reports (see Section 3.1)
* Batch type “**C**” — Correct or delete one or more reports from a previously accepted batch (see Section 3.4.1)

Instead of submitting correction batches, you can choose to process any corrections or deletions for STR, LCTR or EFTO and EFTI reports through F2R, FINTRAC's secure website. See Section 3.4.2 for more information.

### 3.1 Batch type “A”: add batch

The following circumstances require submission of batch type “A”:

* **New reports**  
  If you need to submit reports that were not previously included in a batch, submit them in a new batch (batch type “**A**”).
* **Rejected batch**  
  If you submitted a batch and it was **completely** rejected by FINTRAC, you have to make the required corrections and submit the reports from the rejected batch within a proper new batch (batch type “**A**”).

### 3.2 Batch acknowledgements

The batch transmission software will contain a log message that your batch file was sent along with an indication that it was successfully transferred to FINTRAC (although not necessarily processed). Once your batch file is processed by FINTRAC, an acknowledgement file will be returned to you through the batch transmission software. This file will contain an acknowledgement that your batch file was received, the number of reports accepted and any associated error messages. It will **not** include any report content; only batch identifying information and any applicable report error messages.

Any error messages will contain information referring to the report sequence number and your reporting entity report reference number. The error message will also contain the field reference number and the nature of the error. If the batch cannot be processed, a rejection message will be returned to you through the batch transmission software with batch identifying information and applicable error messages.

See Section 7 for more information about how FINTRAC's acknowledgement messages are formatted, including two examples of a general batch acknowledgement message.

#### 3.2.1 Accepted batch

If your batch is accepted, FINTRAC will indicate this in the batch status message (tag C2) in Section C of the acknowledgement file. Section C will also contain the number of reports accepted in your batch.

The acknowledgement will also alert you about any reports requiring correction, as follows:

* Rejected reports (tags C4, D and D2 of the acknowledgement file); or
* Reports that have been accepted but have errors (tags D and D2 of the acknowledgement file).

In this case, you will have to correct those reports, as explained in Section 3.4.

#### 3.2.2 Rejected batch

If your batch is rejected, it will be indicated in the batch status message (tag C2) in Part C of FINTRAC's acknowledgement. This means there are problems with that batch's header, sub-header, trailer or report format. It also means that the reports included in that batch have not been received by FINTRAC. You will have to re-submit them in a new batch, as explained in Section 3.1.

In the case of a rejected batch, FINTRAC will not have any information about the reports it contained. However, if any information is available at the report level, it will be reflected in Tag C6 of your acknowledgement message. A maximum of 40 such messages can be provided to help you correct the reports before you re-submit them in a new batch.

### 3.3 Reports returned for further action (RRFA)

If there are data quality issues with your accepted reports, FINTRAC may return those reports to you for adjustment. These are called reports returned for further action (RRFA).

For each LCTR or EFTO and EFTI report type that you submit by batch, you can choose to deal with RRFAs through either batch or F2R, as follows:

* If you choose to deal with **RRFA by batch**, you will receive an RRFA message through the batch transmission software, in a similar manner to how you receive your acknowledgement messages. See Section 8 for more information about how RRFA messages are formatted, including an example of an RRFA message. If an RRFA is sent to you in this manner, you will have to correct the affected reports and re-submit them to FINTRAC in a correction batch as explained in Section 3.4. Your F2R administrator will also be notified by email when an RRFA message has been sent by batch. These returned reports will appear in F2R along with additional messaging to assist you in understanding the data quality issue, but the reports must continue to be corrected and re-submitted by batch.
* If you choose to deal with **RRFA through F2R**, your F2R administrator will receive the RRFA notifications. These reports will be available in the RRFA report queue in F2R so that the required corrections can be made and the affected reports re-submitted to FINTRAC.

### 3.4 Modification

The following explains how you can make required modifications to reports that were submitted by batch to FINTRAC.

Modifications are required in the following instances:

* If your acknowledgement file indicates that a batch is accepted but that there were rejected reports or reports with errors, you will have to modify those reports.
* If FINTRAC sends you an RRFA, you will have to make the necessary modifications and re-submit that report as soon as possible.
* You may also need to correct or delete a report for other reasons. For example, if you were to discover that a report contained invalid data or was submitted in error.

How you modify reports depends on whether you wish to submit the modifications through correction batches (type “C”) or through F2R. You can only choose one of the two methods for a particular type of report, and it will apply to any modification required for all such reports.

#### 3.4.1 Batch type “C”: Correction batch

The following applies only if you do **not** choose to process modifications through F2R. This applies to a processed report with errors as well as a rejected report.

Only the reports being corrected or deleted are to be included in the correction batch. All previously accepted batches can be corrected, by submitting a correction batch with changes to the following:

1. Batch type set to “**C**”.
2. Sub-header count set to the number of sub-headers in the correction batch.
3. Report count set to the number of reports in the correction batch.
4. Sub-header report count in the applicable sub-headers set to the number of reports in the correction batch.

To **correct** one or more reports from a previously **accepted** batch, you must submit a correction batch (batch type “C”) with each complete corrected report. Include the reporting entity report reference number, as used in the original file. ALL FIELDS in each corrected report must be completed with the correct information, NOT JUST THE DATA FIELDS NEEDING CORRECTION. The action code for each report to be corrected has to be set to “C”.

To **delete** one or more reports from a previously **accepted** batch, you must also submit a correction batch (batch type “C”). Read the following instructions, depending on the type of report to be deleted:

**Deleting an STR or LCTR**  
To delete an STR or an LCTR from a previously accepted batch, you need not submit the complete report to be deleted in the correction batch. Only the following must be completed to delete a report:

* Part ID “A1”
* Report sequence number
* Reporting entity report reference number (as used in original file)
* Action code indicator (value “D”)
* Reporting entity's identifier number
* Immediately following those fields, delimit the deleted report with carriage return, line feed (<CRLF>).  
  Begin the next report to be corrected or deleted, as required.

**Deleting an EFTO or EFTI**  
To delete an EFTO or EFTI from a previously accepted batch, you have to include the complete report that is to be deleted in the correction batch. The action code for each report to be deleted has to be set to “D”.

#### 3.4.2 F2R

F2R is the interface with FINTRAC through which you will be able to administer your location number and user information and send non-batch reports to FINTRAC.

If you select this as an option upon your enrolment with FINTRAC for a particular report type (STR, LCTR or EFTO and EFTI reports), you can process modifications required to your reports of that type through F2R. If you choose this option, you will not send correction batches for those reports. Instead, you will have to make **any** changes required to accepted reports from previously accepted batches through F2R.

You will be able to access reports from an accepted batch in F2R using your reporting entity report reference number. You will access report content to process your corrections. This includes reports with errors and reports that were rejected from an accepted batch.

For more information about FINTRAC's enrolment process and use of F2R, contact FINTRAC.

## 4. General Specifications

### 4.1 General format requirements

The following table identifies the general formatting specifications for completing suspicious transaction reports (STR), large cash transaction reports (LCTR), Outgoing non-SWIFT International EFT Reports (EFTO) and Incoming Non-SWIFT International EFT Reports (EFTI) using the batch file transfer format.

Section 5 provides detailed formatting requirements for each report type. You also have to follow the abbreviations and code standards identified in Section 6.

**All records are to be fixed in length as specified in the format descriptions.** The physical batch size cannot exceed 30 megabytes, uncompressed.

The standard file characteristics must be in ASCII code page 850 (Western European), upper and lower characters, and English and/or French character set. EBCDIC data format will **not** be accepted. The code page format 850 must be indicated in the batch header.

All batch headers, sub-headers, report parts and batch trailers must be delimited with carriage return, line feed (<CRLF>). As these may be implicit in certain programs, please ensure that this does not cause blank lines to be inserted.

**GENERAL FORMAT REQUIREMENTS**

| Format Element | Comment |
| --- | --- |
| **Zero-filled** | Blank fields are to be filled with zero (0). |
| **Space-filled** | Blank fields are to be space-filled. |
| **LJ** | Left justified, space-filled. |
| **RJ** | Right justified, space-filled. |
| **RJZ** | Right justified, zero-filled. All amount fields are RJZ, no thousands separators allowed. |
| **X** | Alphanumeric character. |
| **9** | Numeric character. |
| **Field length** | Number shown in brackets next to alphanumeric character or numeric character. For example, X(2) or 9(5). |
| **d** | Decimal place — FINTRAC will accept ‘,' or ‘.' as a decimal place notation.  For an amount of money, the format requires a fixed decimal place, with two decimal places. For example, 000000012345.00 represents the amount of $12,345.00 for a field with X(15)d.  For an exchange rate, the format requires a floating decimal place, with as many decimal places as required. For example, 00000012.123 represents the exchange rate of 12.123 for a field with X(12)d. |
| **Report sequence number** | The first report in a batch type “A” (Add batch) within a sub-header must begin at 00001 and all following reports must be incremented by 1.  For reports in a batch type “C” (Correction batch), use the sequence numbers of the reports from the original accepted batch. |
| **Date** | YYYYMMDD (year/month/day)  If no date is applicable, space–fill |
| **Time** | HHMMSS — Use the 24-hour clock  Hour (from 00 to 23), minutes (from 00 to 59) and seconds (from 00 to 59).  Seconds should default to 00.  Examples: 1 o'clock PM = 130000 or 2:45 PM = 144500.  RJZ |
| **Name** | LJ, space–filled, alpha characters. |
| **Address** | LJ, space–filled, alpha and numeric mixed.  If there is an apartment, suite or unit number, place the number at the start of the street address.  Enter entire names or use codes from appropriate code tables in Section 6.  If the address is in Canada, the appropriate fields must contain a valid Canadian province or territory and a postal code. If the address is in the United States or Mexico, the appropriate field must contain a valid state, and in the case of an address in the United States, a valid zip code.Refer to the relevant code tables in Section 6 for valid provinces, territories and states.  If the address is outside Canada and the United States and has no province/state or postal/zip code, those fields can be space-filled. |
| **Postal codes** | X(9) — No embedded spaces or dashes (-).  Canada: X9X9X9  US: 99999 or 999999999 |
| **Account numbers** | No leading zeros, unless leading zeros are part of the account number.  RJ, space-filled |
| **Telephone numbers** | Must include area codes  Canada and US: 999-999-9999  For others, include country code, city code and local number: 999-9999-9999-9999 |
| **Reporting entity report reference number** | Can contain letters from A to Z and/or numbers from 0 to 9. Do not use any special characters, such as “-”, “#”, etc., in this reference number.  Each report submitted by the same reporting entity has to have a unique number. In this context, the upper case of any letter is considered the same as the lower case of that letter.  For example, a report reference number of ABC123 is considered the same as the report reference number abc123. |
| **\*** | Denotes a mandatory field as prescribed in the Regulations. |
| **±** | Denotes a required field for a batch report. |

### 4.2 Mandatory and required fields

The fields for all reports are established by Regulations. They are either mandatory, mandatory if applicable, or require reasonable efforts to complete, as follows:

* **Mandatory:** All fields of a report marked with an asterisk (\*) **have to be completed.**
* **Mandatory if applicable:** The fields that have both an asterisk and “if applicable” next to them have to be completed if they are applicable to you or the transaction being reported.
* **Reasonable efforts:** For all other fields that do not have an asterisk, you have to make reasonable efforts to get the information. For more information about “reasonable efforts” please refer to:
  + [Reporting suspicious transactions to FINTRAC](/guidance-directives/transaction-operation/str-dod/str-dod-eng)
  + [Reporting large cash transactions to FINTRAC](/guidance-directives/transaction-operation/lctr-doie/lctr-doie-eng)

Fields in the batch format indicated by “**±**” are required for processing purposes, such as those within the batch header, sub-header and trailer blocks.

In certain circumstances, only as directed in the detailed specification layout for each report type, if you need to indicate that a required field in a report is not applicable, enter “N/A” or “n/a”. Do not substitute any other abbreviations or special characters (e.g., “x”, “-” or “\*”).

Some parts of a report are only required if applicable. For example, Part C of the STR is only required if the transaction involved an account. The fields within those parts are not required, unless the part is in fact applicable. The parts that are to be excluded if they are not applicable are indicated in the detailed layout for each report in Section 5.2.

Where mandatory and required fields have not been completed, the report may be rejected.

### 4.3 Batch process

A batch must contain one batch header, at least one batch sub-header, and only one report type (STR, LCTR, EFTO or EFTI). It must also have one batch trailer.

## 5. Batch Report Formatting

A separate batch must be submitted for each report type. An individual batch file is limited to a **maximum of 10,000 reports**. The physical batch size cannot exceed 30 megabytes, uncompressed.

The following charts provide details on how to format reports for batch submission to FINTRAC. Section 5.1 provides information concerning a batch header, sub-header and trailer. Section 5.2 provides specifications for each report type, based on batch report format version 03.

### 5.1 Detailed specification layout – Batch header, sub-header and trailer

**Batch Header -** The batch header contains information identifying the individual or institution originating the transmission. There can be only one batch header for each transmitted file. The following elements are required in the batch header.

| Field No. | Field Name | Format | Comment |
| --- | --- | --- | --- |
| ± 0 | Record type | X(2) | Value "1A" |
| ± 1 | Code format | 9(3) | Value "850" |
| ± 2 | Report type | X(4)LJ | Value “STR ”, “LCTR”, “EFTO”, or “EFTI” |
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
| ± 14 | Format indicator | 9(2)RJZ | Batch report format version number “03” for LCTR, EFTO and EFTI.  Batch report format version number “04” for STR. |
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
| ± 1 | Record sequence number | 9(5)RJZ | Sequence number of the batch trailer should always be "00001". |
| Total characters in batch trailer: | | 7 | Every batch must have one trailer at the end, following the last report in the batch. |

#### 5.1.1 Samples of batch headers, sub-headers and trailers

As explained in Section 5.1, you must have one batch header, at least one sub-header, and one batch trailer for each batch you send to FINTRAC. Sub-headers are part of the batch format to allow you to group reports within a batch according to your organizational structure or any other grouping need. The use of different sub-headers is optional, but you must include at least one sub-header in a batch.

The following examples illustrate two possible scenarios regarding the use of batch headers and sub-headers.

##### Example 1

A reporting entity called “ABC and Company” is sending three suspicious transaction reports in a production batch. Their reporting entity identifier is 0004567 and their PKI certificate identifier is 1234567890. The contact person is John Smith and Mr. Smith's telephone number is 416-555-5555 (no extension). ABC and Company does not wish to group reports within a batch.

```

1A850STR 0004567SMITH     JOHN     416-555-5555     0000012345678902005071923155500001A000010000303P
1B00001ABC AND COMPANY 	  00003
       Report 1
       Report 2
       Report 3
1C00001
```

##### Example 2

A reporting entity called “Entity X” operates in several different geographical locations (Location A, Location B, etc.) and wishes to group their reports by location. In this case, the reporting entity would include a different sub-header for each location. Their reporting entity identifier is 0000567 and their PKI certificate identifier is 7771234567. The contact person is John Brown and Mr. Brown's telephone number is 416-666-6666 (no extension). To send a batch with a total of five LCTR reports (three from Location A and two from Location B), they would use two sub-headers, as follows:

```

1A850LCTR 0000567BROWN    JOHN    416-666-6666    0000077712345672005071923155500001A000020000503P
1B00001   LOCATION A      00003
          Report 1 from Location A
          Report 2 from Location A
          Report 3 from Location A
1B00002   LOCATION B      00002
          Report 1 from Location B
          Report 2 from Location B
1C00001
```

### 5.2 Batch report format versions 03 and 04

The specifications for LCTR, EFTI and EFTO are based on batch report format version “03”.The specifications for STR are based on batch format version “04”.

#### 5.2.1 Detailed specification layout (format version 04) — STR

These are published in Module 2.

#### 5.2.2 Detailed specification layout (format version 03) — LCTR

These are published in Module 3.

#### 5.2.3 Detailed specification layout (format version 03) — non-SWIFT electronic funds transfer reports

These are published in Module 4.

### 5.3 Report structure flowcharts

These are published in Modules 2, 3 and 4, according to the report type.

## 6. Code Tables and Editing Instructions

### 6.1 Code tables

The following code tables are available for download from the technical documentation area in [the batch documentation section of FINTRAC's website](/reporting-declaration/info/f2r-eng#y1). These apply to all reports submitted to FINTRAC through standard batch format reporting.

* Country codes based on ISO 3166
* Province/State codes:
  + Canadian province or territory codes
  + Mexican State codes
  + United States (U.S.) State codes
* Currency codes  
  The rows without shading (or without brackets in txt format) in this table contain current currency codes on ISO 4217. The shaded rows (or the rows with brackets in txt format) provide retired codes that are not on the current ISO 4217 list.
* Standard word abbreviations  
  All the abbreviations listed in this table are singular. They may be changed from singular to plural by the addition of the letter 's'
* Street type names and abbreviations

### 6.2 Name editing instructions

To enter the name of an individual, use the specific individual name fields (Surname, Given name, Other name/initial). When completing these fields, delete any titles, prefixes, suffixes or other descriptive information such as Mr., Mrs., Dr., Reverend, Partner, or Trustee. Do not delete suffixes that distinguish family members such as Jr., Sr., III or IV. Such suffixes should be included in the fields for “Other name/initial” (e.g., for an individual whose name includes the initial “S” as well as the suffix “Junior”, the “Other name/initial” field would be completed as follows: S JR). Do not include any punctuation (e.g. “JR.” would be submitted as “JR”).

For entity and business names, use the non-delimited entity name fields.

## 7. Acknowledgement Formatting

The following charts provide details on how FINTRAC's acknowledgement files are formatted for batches submitted to FINTRAC.

### 7.1 Detailed specification layout – batch acknowledgement

#### 7.1.1 General acknowledgement layout

The following tables outline the format for the acknowledgement messages returned to you once a batch has been processed by FINTRAC. All tag fields are three characters, left justified and space-filled.

**Section A: Information about the submitted batch file**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
| **A** | Acknowledgement title | X(129)LJ | "Your batch has been processed. / Votre lot a été traité. " |
| Separator | X(132) | Spaces |
| **A2** | Report type |  |  |
| Description | X(37)LJ | "Report type / Genre de déclaration" |
| Variable indicator | X(2)LJ | ": " |
| Report type value | X(4)LJ | “STR” Suspicious transaction report batch  “LCTR” Large cash transaction report batch  “EFTO” Non-SWIFT outgoing EFT report batch  “EFTI” Non-SWIFT incoming EFT report batch |
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

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **B** | Section title | X(129)LJ | "Batch ID / Identification du lot" |
| **B2** | Batch date |  |  |
| Description | X(65)LJ | "Date / Date" |
| Variable indicator | X(2)LJ | ": " |
| Batch date | 9(8) | YYYYMMDD |
| Filler | X(54)LJ | Spaces |
| **B3** | Batch time |  |  |
| Description | X(65)LJ | "Time / Heure" |
| Variable indicator | X(2)LJ | ": " |
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
| Description | X(65)LJ | "Reports deleted / Déclarations supprimées" |
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
| Variable indicator | X(2)LJ | ": " |
| Reports processed count | X(5)LJ | Number of reports successfully processed |
| Filler | X(57)LJ | Spaces |
| **C5** | Reject legend A | X(129)LJ | "A = Sub-header sequence number / Numéro séquentiel du sous-en-tête" (for a rejected batch only) |
| **C5** | Reject legend B | X(129)LJ | "B = Report sequence number / Numéro séquentiel de la déclaration" (for a rejected batch only) |
| **C5** | Reject legend C | X(129)LJ | "C = RE report reference number / Numéro de référence de la déclaration de l'ED" (for a rejected batch only) |
| **C5** | Reject legend D | X(129)LJ | “D = Transaction / Opération” (for a rejected batch only) |
| **C5** | Reject legend E | X(129)LJ | “E = Disposition / Répartition” (for a rejected batch only) |
| **C5** | Reject legend F | X(129)LJ | "F = Field / Champ" (for a rejected batch only) |
| **C5** | Reject legend G | X(129)LJ | "G = Reject code / Code de rejet" (for a rejected batch only) |
| **C5** | Reject legend | X(129)LJ | "\* = Reject indicator / Indicateur de rejet" (for a rejected batch only) |
| **C5** | Message header | X(129)LJ | "A    B    C    D    E    F    G" (for a rejected batch only) |
| **C6** | Validation message |  | **This is a repeating row.** (for a rejected batch only) |
| Variable indicator | X(2)LJ | " : " |
| Sub-header sequence number (A) | X(5)LJ | Sequence number of the sub-header within the batch file (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Report sequence number (B) | X(5)LJ | Sequence number of the report within the batch file (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Reporting entity report reference number (C) | X(20)LJ | Unique reference number assigned by the reporting entity to the report (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Transaction sequence number (D) | X(4)LJ | Transaction sequence number in a report to which the message relates (for a rejected batch only and does not apply to messages about EFT reports) |
| Variable indicator | X(3)LJ | " : " |
| Disposition sequence number (E) | X(6)LJ | Disposition sequence number in a report to which the message relates (for a rejected batch only and does not apply to messages about EFT reports) |
| Variable indicator | X(3)LJ | " : " |
| Field number (F) | X(6)LJ | Field number in the report resulting in the reject condition (for a rejected batch only) |
| Variable indicator | X(3)LJ | " : " |
| Reject message number (G) | 9(3)LJ | Message number identifying the reason the batch was rejected by FINTRAC (for a rejected batch only). See Section 9.2 for more information about these message codes. |
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
| **D** | Legend C | X(129)LJ | "C = RE report reference number / Numéro de référence de la déclaration de l'ED" |
| **D** | Legend D | X(129)LJ | “D = Transaction / Opération” |
| **D** | Legend E | X(129)LJ | “E = Disposition / Répartition” |
| **D** | Legend F | X(129)LJ | "F = Field / Champ" |
| **D** | Legend G | X(129)LJ | "G = Message code / Code de message" |
| **D** | Legend | X(129) | "\*  = Reject indicator / Indicateur de rejet" |
| **D** | Legend H | X(129)LJ | "H = Validation rule number / Numéro de la règle de validation" |
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
| Transaction sequence number (D) | X(4)LJ | Transaction sequence number in a report to which the message relates (does not apply to messages about EFT reports) |
| Variable indicator | X(3)LJ | " : " |
| Disposition sequence number (E) | X(6)LJ | Disposition sequence number in a report to which the message relates (does not apply to messages about EFT reports) |
| Variable indicator | X(3)LJ | " : " |
| Field number (F) | X(6)LJ | Field number identifier in a report to which the message relates |
| Variable indicator | X(3)LJ | " : " |
| Validation message (G) | 9(3)LJ | The validation message related to the identified field.  See section 9.2 for information about these message codes. |
| Reject indicator | X(1)LJ | "\*" |
| Variable indicator | X(3)LJ | " : " |
| Validation rule number (H) | 9(9)LJ | This is the validation rule number identifying the issue in the report. See section 9.1 for information about these rule numbers. |
| Filler | X(47)LJ | Spaces |

**Section E: Sub-header and report processing totals**  
(for accepted batches only)

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **E** | Section title | X(129)LJ | "Accepted sub-header and report processing totals" |
| **E** | Section title | X(129)LJ | "Nombre de sous-en-têtes acceptés et de déclarations traitées avec succès" |
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

| Tag No. | Field Description | Format | Comment |
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

**Note:** The legend will be sent with all acknowledgements.

#### 7.1.2 General acknowledgement examples

##### 7.1.2.1 Acknowledgement example for an accepted batch

**Note: Due to space constraints this example is not padded to 132 characters.**

```

A  Your batch has been processed. / Votre lot a été traité.

A2 Report type / Genre de déclaration       : LCTR 
A3 Batch type  / Catégorie de lot           : A 
A4 Operational mode / Mode opérationnel     : P
A5 Date batch processed by FINTRAC / Date de traitement par CANAFE  : 20050723
A6 Time batch processed by FINTRAC / Heure de traitement par CANAFE : 041733

B  Batch ID / Identification du lot				
B2 Date / Date                                                      : 20050722
B3 Time / Heure                                                     : 234527
B4 Batch sequence ID / Numéro séq. d'identification du lot          : 00003

C  Batch processing messages / Messages portant sur le traitement du lot
C2 Batch accepted / Lot accepté
C3 Sub-headers accepted / Sous-en-têtes de lot acceptés	            : 00001
C4 Reports rejected / Déclarations rejetées                         : 1
C4 Duplicate reports ignored / Déclarations en double mises de côté : 0
C4 Reports deleted / Déclarations supprimées                        : 0
C4 New reports accepted / Nouvelles déclarations acceptées          : 3
C4 Total reports processed / Nombre de déclarations traitées        : 4

D  Messages on accepted reports, reports in error and reports rejected
D  Messages portant sur les décl. acceptées, avec des erreurs et rejetées
D  A = Sub-header / Sous-en-tête
D  B = Report sequence / Séquence de la déclaration
D  C = RE report reference number / Numéro de référence de la déclaration de l'ED  
D  D = Transaction / Opération
D  E = Disposition / Répartition
D  F = Field / Champ
D  G = Message code / Code de message
D  * = Reject indicator / Indicateur de rejet
D  H = Validation rule number / Numéro de la règle de validation

D     A       B               C              D      E        F        G      H
D2 : 1     : 1     : Report97000000       : 1    : 1      : B1.7a  : 320* : 28765
D2 : 1     : 2     : Report97100000       : 1    : 1      : B1.7a  : 320  : 28765
D2 : 2     : 3     : Report97200000       : 1    : 1      : B1.7a  : 320  : 28765

E  Accepted sub-header and report processing totals
E  Nombre de sous-en-têtes acceptés et de déclarations traitées avec succès
E  Sub-header	      Report count
E  Sous-en-tête	      Nombre de déclarations
E2 : 1                : 4

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
C2  Batch acceptance or reject message / Message d'acceptation ou de rejet du lot 
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

##### 7.1.2.2 Acknowledgement example for a rejected batch

**Note: Due to space constraints this example is not padded to 132 characters.**

```

A  Your batch has been processed. / Votre lot a été traité.

A2 Report type / Genre de déclaration       : LCTR 
A3 Batch type  / Catégorie de lot           : A 
A4 Operational mode / Mode opérationnel     : P
A5 Date batch processed by FINTRAC / Date de traitement par CANAFE  : 20050723
A6 Time batch processed by FINTRAC / Heure de traitement par CANAFE : 014532

B  Batch ID / Identification du lot				
B2 Date / Date                                                      : 20050722
B3 Time / Heure                                                     : 234527
B4 Batch sequence ID / Numéro séq. d'identification du lot          : 00003

C  Batch processing messages / Messages portant sur le traitement du lot
C2 Batch accepted / Lot accepté
C3 Sub-headers accepted / Sous-en-têtes de lot acceptés	            : 00001
C4 Reports rejected / Déclarations rejetées                         : 3
C4 Duplicate reports ignored / Déclarations en double mises de côté : 0
C4 Reports deleted / Déclarations supprimées                        : 0
C4 New reports accepted / Nouvelles déclarations acceptées          : 0
C4 Total reports processed / Nombre de déclarations traitées        : 0
C5 A = Sub-header sequence number / Numéro séquentiel du sous-en-tête
C5 B = Report sequence number / Numéro séquentiel de la déclaration
C5 C = RE report reference number / Numéro de référence de déclaration de l'ED
C5 D = Transaction / Opération
C5 E = Disposition / Répartition
C5 F = Field / Champ
C5 G = Reject code / Code de rejet
C5 * = Reject indicator / Indicateur de rejet

C5    A       B               C              D      E        F        G  
C6 : 1     : 1     : 111111234567         : 1    :        : A.1A   : 411*
C6 : 1     : 2     : 111111234568         : 1    :        : A.1A   : 411*
C6 : 1     : 3     : 111111234569         : 1    :        : A.1A   : 411*

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
C2  Batch acceptance or reject message / Message d'acceptation ou de rejet du lot 
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

## 8. Reports Returned for Further Action Message Formatting

The following charts provide details on how the message files from FINTRAC about reports returned for further action (RRFA) are formatted.

### 8.1 Detailed specification layout – RRFA message

#### 8.1.1 General RRFA message layout

The following tables outline the format for RRFA messages that will be sent to you by FINTRAC if you choose to deal with RRFA by batch for reports that were originally submitted by batch. All tag fields are three characters, left justified and space-filled.

**Section A: Introduction of RRFA**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
| **A** | RRFA introduction | X(129)LJ | "Please review and correct the following report(s):" |
| RRFA introduction | X(129)LJ | "Veuillez réviser et corriger la ou les déclaration(s) suivante(s) :" |
| Separator | X(132) | Spaces |
| **A2** | Report type |  |  |
| Description | X(37)LJ | "Report type / Genre de déclaration" |
| Variable indicator | X(2)LJ | ": " |
| Report type value | X(4)LJ | “LCTR” Large cash transaction report  “EFTO” Non-SWIFT outgoing EFT report  “EFTI” Non-SWIFT incoming EFT report |
| Filler | X(86)LJ | Spaces |
| **A3** | Date RRFA issued |  |  |
| Description | X(65)LJ | "Date issued by FINTRAC / Date d'envoi par CANAFE" |
| Variable indicator | X(2)LJ | ": " |
| Processing date | 9(8)LJ | YYYYMMDD |
| Filler | X(54)LJ | Spaces |

**Section B: RRFA ID**

| Tag No. | Field Description | Format | Comment |
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
| **C** | Section title | X(129)LJ | "Data quality issues / Problèmes de qualité" |
| **C2** | Quality issue legend A | X(129)LJ | "A = RE's identifier number / Numéro d'identification de l'ED" |
| **C2** | Quality issue legend B | X(129)LJ | "B = Batch date / Date du lot" |
| **C2** | Quality issue legend C | X(129)LJ | "C = Batch time / Heure du lot" |
| **C2** | Quality issue legend D | X(129)LJ | "D = Batch sequence ID / Numéro séq. d'identification du lot |
| **C2** | Quality issue legend E | X(129)LJ | "E = RE report reference number / Numéro de référence de déclaration de l'ED" |
| **C2** | Quality issue legend F | X(129)LJ | “F = Report part and field number / Numéros de partie et du champ de la décl.” |
| **C2** | Quality issue legend G | X(129)LJ | “G = Transaction / Opération” |
| **C2** | Quality issue legend H | X(129)LJ | “H = Disposition / Répartition” |
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
| Report part and field number (F) | X(5)LJ | The part and field number of the returned report to which the data quality message relates |
| Variable indicator | X(3)LJ | " : " |
| Transaction sequence number (G) | X(4)LJ | Transaction sequence number in the returned report to which the data quality message relates |
| Variable indicator | X(3)LJ | " : " |
| Disposition sequence number (H) | X(6)LJ | Disposition sequence number in the returned report to which the data quality issue message relates |
| Variable indicator | X(3)LJ | " : " |
| Data quality message number (I) | 9(3)LJ | Message number identifying the quality issue applicable. See Section 9.2 for more information about the data quality issue messages. |
| Filler | X(38)LJ | Spaces |

**Section D: End of report**

| Tag No. | Field Description | Format | Comment |
| --- | --- | --- | --- |
|  | Separator | X(132) | Spaces |
| **D** | Section title | X(129)LJ | "End of report / Fin du rapport" |
| Filler | X(132)LJ | "==============================================================================================" |

#### 8.1.2 RRFA Message Example

**Note: Due to space constraints this example is not padded to 132 characters.**

```

A  Please review and correct the following report(s):
A  Veuillez réviser et corriger la ou les déclaration(s) suivante(s) :

A2 Report type / Genre de déclaration                : LCTR
A3 Date issued by FINTRAC / Date d'envoi par CANAFE  : 20060523

B  RRFA identification / Identification de la DRM
B2 RRFA number / Numéro de la DRM                                     : 99
B3 Number of batches involved / Nombre de lots impliqués              : 2
B4 Number of reports returned / Nombre de déclarations retournées     : 4
B5 Number of quality issues / Nombre de problèmes de qualité          : 5

C  Data quality issues / Problèmes de qualité 
C2 A = RE's identifier number / Numéro d'identification de l'ED
C2 B = Batch date / Date du lot 
C2 C = Batch time / Heure du lot 
C2 D = Batch sequence ID / Numéro séq. d'identification du lot
C2 E = RE report reference number / Numéro de référence de déclaration de l'ED
C2 F = Report part and field number / Numéros de partie et du champ de la décl.
C2 G = Transaction / Opération
C2 H = Disposition / Répartition
C2 I = Quality issue code / Code du problème de qualité

C3      A          B         C       D              E         F     G   H   I
C4 : 1211379 : 20061028 : 000523 : 00003 : XT007889944100 : B1.7  : 1 :   : 329
C4 : 1211379 : 20061028 : 000523 : 00003 : XT007889944100 : B2.8A : 1 : 1 : 442
C4 : 1211379 : 20061029 : 001725 : 00004 : 00QZ0078952123 : C.1   : 1 : 1 : 77
C4 : 1211379 : 20061029 : 001725 : 00004 : 00RG0078751167 : C.2   : 1 : 1 : 77 

D  End of report / Fin du rapport
=================================================================================================== 
```

## 9. Report Validation and Processing Error Codes

### 9.1 Report validation rules

Report validation rules apply at the field level to reports within an accepted batch to ensure that reports are error-free (i.e., they contain the required fields, the fields are formatted correctly, and the data is valid). Validation messages returned in Section D of the batch acknowledgement file identify rejected reports and provide warnings about accepted reports based on these validation rules.

A [report validation rules](/reporting-declaration/info/api/api-eng) table is available for download. The table provides a description of the validation applied to each field within the reports.

### 9.2 Batch error codes

Batch processing error codes are returned in Section C (for a rejected batch) and Section D (for an accepted batch) of the batch acknowledgement file. Error codes are also found in Section C of the RRFA message to identify quality issues. [A code table](/reporting-declaration/info/f2r-eng#y1) for these error messages is available for download in the technical documentation.

In the error code table, certain error codes (e.g., codes 400 to 439) are used when an entire batch file is **rejected**. In the case of a rejected batch, the error codes in the acknowledgement file will reflect our attempt to process the batch. It is possible that there were other errors that we did not get far enough to detect.

Other error codes (such as 9, 77, 300 to 372, 442, and 978 to 999) apply at the **field** level to reports within an **accepted** batch. These error codes explain why a report was rejected or a why a warning message was received about an accepted report.

## 10. Batch File Naming Convention

The following provides batch file naming recommendations to ensure all batch files for a reporting entity have a unique name.

### 10.1 Batch file naming standard

Use the following naming convention for your batch files: Date\_Time\_Report Type.FileExtension Each element of this naming convention is required, except for the report type, as follows:

* The date is required (YYYYMMDD).
* The time is required (HHMMSS).
* The report type is optional (STR, LCTR, EFTO or EFTI).
* One of the following file extensions is required: “.DAT”, “.DATA” or “.TXT”. The batch will be refused for any other file extension values.

Example:         20050722\_223915\_LCTR.DAT

File names may only include standard upper/lower case alphanumeric characters (A to Z and 0 to 9). The only separator allowed is the underscore character “\_”. The file name must only have one dot extension (e.g., .dat). File names containing spaces will cause the file to be rejected.

In this context, the upper case of any letter is considered the same as the lower case of that letter. For example, a batch file name of 20050722\_223915\_LCTR.DAT is considered the same as 20050722\_223915\_lctr.DAT.

All batch files that you submit to FINTRAC must have a unique file name, regardless of the file contents, or the file will be rejected. This is true even if the previously submitted file had been rejected or if you are submitting a correction batch.

### 10.2 FINTRAC batch acknowledgement file naming convention

FINTRAC's acknowledgement file returned to you will have the same name as your original batch file name, but with a different suffix. For batch files with no batch reject or report validation messages the suffix will be “.001”. For those files with reject or validation messages, the suffix will be as follows:

* **file\_name.002**: All reports accepted but some warning messages
* **file\_name.004**: Batch accepted but some rejected reports
* **file\_name.005**: Batch rejected for structural reasons (bad file name, invalid contents, report counts do not match, etc.)

### 10.3 RRFA batch file naming convention

The following naming convention will be used by FINTRAC for the RRFA notification file sent to you:

* **RRFA\_DRM\_999999999.txt**

The “999999999” represents the RRFA number reflected in Tag B2 of the RRFA message.

Date Modified:
:   2017-06-29