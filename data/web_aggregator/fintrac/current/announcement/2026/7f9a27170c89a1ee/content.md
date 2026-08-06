# XML Batch Reporting Instructions and Specifications

**MODULE 1**

**May 30, 2015**

## On this page

[Changes in this Version](#changes)

1. [**General Information**](#s1)
2. [**Acceptance Procedures**](#s2)
3. [**Batch Submission, Acknowledgement and Modification**](#s3)
   * 3.1 [Batch acknowledgements](#s3-1)
     + 3.1.1 [Accepted batch](#s3-1-1)
     + 3.1.2 [Rejected batch](#s3-1-2)
   * 3.2 [Reports returned for further action (RRFA)](#s3-2)
   * 3.3 [Modification](#s3-3)
     + 3.3.1 [Corrections by batch](#s3-3-1)
     + 3.3.2 [Corrections in F2R](#s3-3-2)
4. [**General Specifications**](#s4)
   * 4.1 [General format requirements](#s4-1)
     + 4.1.1 [Prerequisites](#s4-1-1)
     + 4.1.2 [Character sets](#s4-1-2)
     + 4.1.3 [Schema versioning](#s4-1-3)
     + 4.1.4 [Conventions used in XML specifications documents](#s4-1-4)
5. [**Code Tables**](#s5)
6. [**Acknowledgement from FINTRAC**](#s6)
   * 6.1 [General acknowledgment layout](#s6-1)
   * 6.2 [General acknowledgement examples](#s6-2)
     + 6.2.1 [Acknowledgement example for an accepted batch](#s6-2-1)
     + 6.2.2 [Acknowledgement example for a rejected batch](#s6-2-2)
7. [**Reports returned for further action (RRFA)**](#s7)
   * 7.1 [RRFA Message Formatting](#s7-1)
   * 7.2 [RRFA message example](#s7-2)
8. [**Report Validation and Processing Error Codes**](#s8)
   * 8.1 [Report validation rules](#s8-1)
   * 8.2 [Batch error codes](#s8-2)
9. [**External File Name**](#s9)
   * 9.1 [Batch file naming standard](#s9-1)
   * 9.2 [FINTRAC batch acknowledgement naming convention](#s9-2)
   * 9.3 [RRFA batch file naming convention](#s9-3)

## Changes in this Version

**Validation rules**

The acknowledgment file formatting specifications in Section 6 has changed to include the validation rule number. This may require programming changes on your part.

Section 8 of this module has been amended to include information concerning the validation of reports submitted by batch.

## 1 General Information

The purpose of this specification document is to provide reporting entities with the requirements and conditions for filing the following reports to the Financial Transactions and Reports Analysis Centre of Canada (FINTRAC) using the **XML batch file transfer format**:

* Casino disbursement reports (CDR)

The specifications defined in sections 4 and 5 reflect the file characteristics acceptable for submission of XML batch reports. These must be adhered to unless replaced by a revision to this specification document.

Rather than use a version number for each revision to this module, revisions will show the publishing date, as well as the effective date for the specification change if different from the publishing date.

This document reflects the provisions of the *Proceeds of Crime (Money
Laundering) and Terrorist Financing Act* (the Act) and the related Regulations, that is, the *Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations*. This document is provided as general information only. It is not legal advice, and is not intended to replace the Act and Regulations. For more information about money laundering, terrorist financing or other requirements under the Act and Regulations, including what type of person or entity is a reporting entity, see the appropriate guideline from the Guidelines page of FINTRAC's website.

Throughout this document, any references to dollar amounts (such as $10,000) refer to the amount in Canadian dollars or its equivalent in foreign currency.

## 2 Acceptance Procedures

Approval to participate in batch report filing under this version of these specifications is contingent upon the following:

* Enrolment with FINTRAC
* Completion of the Public Key Infrastructure (PKI) registration process;
* Installation and configuration of the batch transmission software; and
* Successful completion of test submissions in the batch transmission software training channel for each report type to be submitted by batch.

More information about the PKI registration process and batch transmission software installation can be found in the reporting section of FINTRAC's website  
(https://fintrac-canafe.canada.ca).

Each time the format changes for one or more report types that you submit by batch, you will need to go through the acceptance procedure of test submissions. For example, if the format for CDRs changes from "1.0" to "2.0" and you submit CDRs by batch, you will need to submit test submissions for that report type using the new format.

You (i.e., the transmitter of the batch files) will be asked to perform **test** submissions in a batch transmission software **training channel**, as follows:

* The test data will consist of a set of reports containing the data that you would normally supply. The test file must contain only one batch header, between 25 and 100 reports and only one batch trailer. A minimum of five test files is required.
* The formatting of the batch records must adhere to the specifications explained in sections 4 and 5. Otherwise, the batch and/or reports will be rejected. If files are unreadable for reasons such as format problems, error messages will be returned identifying the problem(s) through the batch transmission software process.
* Reporting entity location numbers used in test reports data must be valid for the reporting entity.
* Upon receipt of the test data by FINTRAC, it will be processed and an acknowledgement message, along with any error messages, will be returned to you within two working days.
* If all the reports in four out of five of your test batches are error-free (i.e., they contain the required fields, the file and data fields are formatted correctly and the location numbers are valid), FINTRAC will issue final acceptance for you to begin production submissions. Acceptance will be based on the last five batches submitted to FINTRAC.
* If a test file is incorrectly formatted or test reports contain a format error or an error in a field that is "mandatory for processing", you will have to submit a new set of test data to FINTRAC. You have to correct these errors before FINTRAC will authorize you to submit production reports.

## 3 Batch Submission, Acknowledgement and Modification

Currently, batches may be sent to FINTRAC at any time of the day and any day of the week. All batches received by FINTRAC will be acknowledged (see subsection 3.1).

A separate batch must be submitted for each report type. The physical batch size cannot exceed 5 megabytes, uncompressed.

The batch file must be placed in the directory in which your batch transmission software is configured to look for files for transfer.

To submit a new batch of CDRs, see module 2. To respond to a report returned by FINTRAC, see subsection 3.2. To submit a modification, see subsection 3.3. Even if you submit reports by batch, you can choose to process any corrections or deletions for reports through F2R, FINTRAC's secure website. See Section 3.3.2 for more information.

### 3.1 Batch acknowledgements

The batch transmission software will contain a log message that your batch file was sent along with an indication that it was successfully transferred to FINTRAC (although not necessarily processed). Once your batch file is processed by FINTRAC, an acknowledgement file will be returned to you through the batch transmission software. This file will contain an acknowledgement that your batch file was received, the number of reports accepted and any associated error messages. It will **not** include any report content; only batch identifying information and any applicable report error messages.

Any error messages will contain information referring to the reporting entity report reference number (**OrganizationReportReferenceIdentifier**). The error message will also contain the data element and the associated error code. If the batch cannot be processed, a rejection message will be returned to you through the batch transmission software with batch identifying information and applicable error messages.

See section 6 for more information about how FINTRAC's acknowledgement messages are formatted, including two examples of a general Batch acknowledgement message.

#### 3.1.1 Accepted batch

If your batch is accepted, FINTRAC will indicate this in the batch status message (**ExternalFileProcessStatusCode**) in the **ReportSubmissionResponseXmlFile**. The acknowledgement will also contain the number of reports accepted in your batch.

The acknowledgement will also alert you about any reports requiring correction, as follows:

* Rejected reports (**ReportRejectCount** and **ReportSubmissionResponseLineItem** of the acknowledgement); or
* Reports that have been accepted but have errors (**ReportSubmissionResponseLineItem** of the acknowledgement).

In this case, you will have to correct those reports, as explained in subsection 3.3.

#### 3.1.2 Rejected batch

If your batch is rejected, it will be indicated in the batch status message (**ExternalFileProcessStatusCode**) in the **ReportSubmissionResponseXmlFile**. This means there are problems with that batch's header, trailer or report format. It also means that the reports included in that batch have not been received by FINTRAC. You will have to resubmit them in a new batch.

In the case of a rejected batch, FINTRAC will not have any information about the reports it contained. However, if any information is available at the report level, it will be reflected in the **ReportSubmissionResponseLineItem** of your acknowledgement.

### 3.2 Reports returned for further action (RRFA)

If there are data quality issues with your accepted reports, FINTRAC can return those reports to you for adjustment. These are called reports returned for further action (RRFA).

For each report type that you submit by batch, you can choose to deal with RRFAs through either batch or F2R, as follows:

* If you choose to deal with **RRFA by batch**, you will receive an RRFA message through the batch transmission software, in a similar manner to how you receive your acknowledgements. See section 7 for more information about how RRFA acknowledgements are formatted, including an example of an RRFA acknowledgement. If an RRFA is sent to you in this manner, you will have to correct the affected reports and re-submit them to FINTRAC as explained in subsection 3.3. Your F2R administrator will also be notified by email when an RRFA message has been sent by batch. These returned reports will appear in F2R along with additional messaging to assist you in understanding the data quality issue, but the reports must continue to be corrected and re-submitted by batch.
* If you choose to deal with **RRFA through F2R**, your F2R administrator will receive the RRFA notifications. These reports will be available in the RRFA report queue in F2R so that the required corrections can be made and the affected reports re-submitted to FINTRAC.

### 3.3 Modification

The following explains how you can make required modifications to reports that were submitted by batch to FINTRAC.

Modifications are required in the following instances:

* If your acknowledgement indicates that a batch is accepted but that there were rejected reports or reports with errors, you will have to modify those reports.
* If FINTRAC sends you an RRFA, you will have to make the necessary modifications and resubmit that report as soon as possible.
* You may also need to correct or delete a report for other reasons. For example, if you were to discover that a report contained invalid data or was submitted in error.

How you modify reports depends on whether you wish to submit the modifications through correction batches or through F2R. You can only choose one of the two methods for a particular type of report, and it will apply to any modification required for all such reports.

Subsection 3.3.1 applies only if you do **not** choose to process modifications through F2R. This applies to a processed report with errors as well as a rejected report.

#### 3.3.1 Corrections by batch

To **correct** one or more reports from a previously **accepted** batch, you must submit the complete corrected report with the **ActionCode** = "2" (Change). ALL FIELDS in each corrected report must be completed with the correct information, NOT JUST THE DATA ELEMENTS NEEDING CORRECTION***.***

To **delete** one or more reports from a previously **accepted** batch, you must submit the report with the **ActionCode** = "5" (Delete). Read the following instructions, depending on the type of report to be deleted:

##### Deleting a CDR

To delete a CDR from a previously accepted batch, you need not submit the complete report to be deleted in the correction batch. Only the following elements are to be completed to delete a report:

* **CasinoDisbursementReportXmlFile**
* **ReportSubmissionFileHeader**
* **CasinoDisbursementReport**
  + **ReportHeader**
* **ReportSubmissionFileTrailer**

##### Example of a batch file to delete a report

```

<?xml version="1.0" encoding="UTF-8"?>
<CasinoDisbursementReportXmlFile ModelVersionNumber="1.0">
 <ReportSubmissionFileHeader>
  <SubmitOrganizationNumber>10090</SubmitOrganizationNumber> 
  <ExternalFileName>20091010_1101112_CDR.xml </ExternalFileName> 
  <ReportTypeCode>13</ReportTypeCode> 
  <OperationModeCode>2</OperationModeCode> 
  <PkiCertificateNumber>1211379999</PkiCertificateNumber> 
 </ReportSubmissionFileHeader>
 <CasinoDisbursementReport ActionCode="5" 
 CasinoDisbursementReportSequenceNumber="1">
  <ReportHeader>
   <OrganizationNumber>10090</OrganizationNumber> 
   <OrganizationReportReferenceIdentifier> Report01
   </OrganizationReportReferenceIdentifier> 
   <TwentyFourHourRuleCode>0</TwentyFourHourRuleCode> 
   <ReportContactInformation>
    <IndividualName>
     <Surname>Le Caré</Surname> 
     <GivenName>John</GivenName> 
    </IndividualName>
    <BusinessTelephone>
     <TelephoneNumber>613-888-8888</TelephoneNumber> 
    </BusinessTelephone>
   </ReportContactInformation>
  </ReportHeader>
 </CasinoDisbursementReport>
 <ReportSubmissionFileTrailer>
  <ReportCount>1</ReportCount> 
 </ReportSubmissionFileTrailer>
</CasinoDisbursementReportXmlFile>
	
```

#### 3.3.2 Corrections in F2R

F2R is the interface through which you will be able to administer your locations and user information and send non-batch reports to FINTRAC.

If you select this as an option upon your enrolment with FINTRAC for a particular report type (CDR, STR, LCTR or EFTO and EFTI reports), you can process modifications required to your reports of that type through F2R. If you choose this option, reports returned for further action (RRFAs) will be sent to you via F2R.

You will be able to access previously accepted reports in F2R using the reporting entity report reference number. You will access report content to process your corrections.

For more information about FINTRAC's enrolment process and use of F2R, contact FINTRAC.

## 4 General Specifications

### 4.1 General format requirements

The following information describes the general formatting specifications for completing reports using the XML batch file transfer format.

#### 4.1.1 Prerequisites

The reader of this document should have the following:

* in-depth knowledge of XML (http://www.w3.org)
* in-depth knowledge of XML schemas

Submitting your information to FINTRAC via batch involves creating an XML file formatted according to FINTRAC's XML schema. The schema is a file that defines rules by which the XML file must be constructed. It specifies which fields are required and which are optional. To some extent, it constrains the makeup of the data that can be included in the XML file. The schema file will be provided to you by FINTRAC. Use it to validate your XML batch files prior to submitting them to FINTRAC.

#### 4.1.2 Character sets

FINTRAC XML specification documents use the UTF-8 charset using code page 10646 as the default character encoding mechanism.

#### 4.1.3 Schema versioning

The version number is an integral part of the message name.

#### 4.1.4 Conventions used in XML specifications documents

The following conventions are used in FINTRAC's XML specifications documents:

##### GENERAL FORMAT REQUIREMENTS

GENERAL FORMAT REQUIREMENTS

| Format Element | Comment |
| sequence with mandatory and optional elements | Indicates a sequence with mandatory and optional elements |
| required element | Required element |
| optional element | Optional element |
| required sub node | Required sub node |
| optional sub node | Optional sub node, 0 to N values |
| optional | Optional, but one of the two nodes should be provided |
| **Date** | YYYYMMDD (year/month/day) |
| **Time** | HHMMSS - Use the 24-hour clock  Hour (from 00 to 23), minutes (from 00 to 59) and seconds (from 00 to 59).  Examples: 1 o'clock PM = 130000 or 2:45 PM = 144500. |
| **Address** | If there is an apartment, suite or unit number, place the number at the start of the street address.  Enter entire names or use codes from appropriate code tables (see section 5).  If the address is in Canada, the appropriate fields must contain a valid Canadian province or territory and a postal code. If the address is in the United States or Mexico, the appropriate field must contain a valid state, and in the case of an address in the United States, a valid zip code. Refer to the relevant code tables (see section 5) for provinces, territories and states.   If the address is outside Canada and the United States and has no province/state or postal/zip code, those elements can be empty. |
| **Postal codes** | No embedded spaces or dashes (-).  Canada: X9X9X9  US: 99999 or 999999999 |
| **Telephone numbers** | Must include area codes  Canada and US: 999-999-9999  For others, include country code, city code and local number: 999-9999-9999-9999 |
| **Reporting entity report reference number** | Can contain letters from A to Z and numbers from 0 to 9. Do **not** use any special characters, such as "-", "#", etc., in this reference number.  Each report submitted by the same reporting entity has to have a unique number. In this context, the upper case of any letter is considered the same as the lower case of that letter. For example, a report reference number of ABC123 is considered the same as the report reference number abc123. |
| **Decimal place** | For an amount of money, the format requires a fixed decimal place, with two decimal places.  Do not include currency indicator (such as, "£", "€" or "$").  FINTRAC will only accept '.' as a decimal place notation.  For example, 12345.00 represents the amount of $12,345.00 |
| **Alpha character** | Upper case and lower case letters |
| **Numeric character** | Numbers from 0 to 9 |
| **Character** | Any character accepted under the UTF-8 charset can be used except for the following five predeclared entities that must be escaped:  **&** or "ampersand" &amp;  **<** or "less than" &lt;  **>** or "greater than" &gt;  **'** or "apostrophe" &apos;  **"** or "quotation mark" &quot; |
| **SequenceNumber** | The first sequence number for a particular element should begin at "1". Use "2" for the second sequence number, etc. |
| **\*** | Denotes a mandatory field as prescribed in the Regulations. |

  

## 5 Code Tables

The following code tables are available for download from the technical documentation area in the publications section of FINTRAC's website:

* Country codes based on ISO 3166
* Province/territory or state codes
  + Canadian province or territory codes
  + Mexican State codes
  + United States (U.S.) State codes
* Currency codes  
  The rows without shading (or without brackets in txt format) in this table contain current currency codes on ISO 4217. The shaded rows (or the rows with brackets in txt format) provide retired codes that are not on the current ISO 4217 list.
* Commonly used terms  
  All the abbreviations listed in this table are singular. They may be changed from singular to plural by the addition of the letter 's'
* Commonly used address terms

## 6 Acknowledgement from FINTRAC

### 6.1 General acknowledgment layout

The following tables outline the format for the acknowledgement files sent to you once a batch has been processed by FINTRAC.

#### ?xml (XML declaration)

Acknowledgement from FINTRAC

| Definition: | This is the top level XML declaration which specifies the version of XML being used. |
| Attributes: | **version**:  fixed: "1.0"  **encoding**:  fixed: "UTF-8" |
| Limits: | Mandatory for processing  One per submission instance |
| Example: | `<?xml version="1.0" encoding="UTF-8" ?>` |
| Remarks: | This declaration is required to be **alone** on the first line of the file. The version number and encoding are fixed to the version of the schema. |

#### ReportSubmissionResponseXmlFile (Root element)

![ReportSubmissionResponseXmlFile](images/Mod1/image007.gif)

ReportSubmissionResponseXmlFile (Root element)

| Definition: | This is the container for the following batch file contents:  **ReportSubmissionResponseFileHeader**  **ReportSubmissionResponseLineItem**  **ReportSubmissionResponseFileTrailer** |
| Attributes: |  |
| Limits: | Mandatory for processing  One per submission instance |
| Example: | `<ReportSubmissionResponseXmlFile>…</ReportSubmissionResponseXmlFile>` |
| Remarks: |  |

#### ReportSubmissionResponseFileHeader (Batch header)

![ReportSubmissionResponseFileHeader](images/Mod1/image008.gif)

Batch header

| Definition: | This is the container for the report acknowledgement file contents. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per **ReportSubmissionResponseXmlFile** |
| Example: | ``` <ReportSubmissionResponseFileHeader>                  <SubmitOrganizationNumber>987654</SubmitOrganizationNumber>                  <ExternalFileName>20090928_223915_CDR.XML</ExternalFileName>                  <ExternalFileSequenceNumber>1</ExternalFileSequenceNumber>                  <ReportTypeCode>13</ReportTypeCode>                  <OperationModeCode>2</OperationModeCode>                  <PkiCertificateNumber>1211379999</PkiCertificateNumber>                  <ExternalFileStatusCode>1</ExternalFileStatusCode>                  <ReportAcceptCount>750</ReportAcceptCount>                  <ReportRejectCount>0</ReportRejectCount>                 </ReportSubmissionResponseFileHeader> 			 ``` |
| Remarks: | This element uniquely identifies the XML batch file submitted to FINTRAC that is the subject of the acknowledgement file from FINTRAC. |

#### SubmitOrganizationNumber (Organization's identifier number)

![SubmitOrganizationNumber](images/Mod1/image009.gif)

Organization's identifier number

| Definition: | This is the identifier number assigned to the individual or institution who transmitted the file being acknowledged. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 7 numeric characters  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<SubmitOrganizationNumber>987654</SubmitOrganizationNumber>` |
| Remarks: |  |

#### ExternalFileName (Batch file name)

![ExternalFileName](images/Mod1/image010.gif)

Batch file name

| Definition: | This is the identifier for the batch report file being acknowledged. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 80 characters  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<ExternalFileName>20091010_1101112_CDR.xml</ExternalFileName>` |
| Remarks: | Names should not contain spaces or dashes |

#### ExternalFileSequenceNumber (Batch sequence number)

![ExternalFileSequenceNumber](images/Mod1/image011.gif)

Batch sequence number

| Definition: | This number represents the "nth" time the external file name was submitted to FINTRAC. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 80 characters  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<ExternalFileSequenceNumber>1</ExternalFileSequenceNumber>` |
| Remarks: |  |

#### ReportTypeCode (Report type)

![ReportTypeCode](images/Mod1/image012.gif)

Report type

| Definition: | This is the code used to identify the type of report. |
| Attributes: |  |
| Limits: | Mandatory for processing  2 numeric characters  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<ReportTypeCode>13</ReportTypeCode>` |
| Remarks: | Code:  13 - Casino Disbursement Report |

#### OperationModeCode (Operational mode)

![OperationModeCode](images/Mod1/image013.gif)

Operational mode

| Definition: | This is the code used to identify which transmission channel was used to submit the file being acknowledged. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 numeric character  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<OperationModeCode>2</OperationModeCode>` |
| Remarks: | Codes:  2 - Production  1 - Test (in a batch transmission software training channel) |

#### PKICertificateNumber (PKI certificate ID)

![PKICertificateNumber](images/Mod1/image014.gif)

PKI certificate ID

| Definition: | This is the PKI certificate identifier number used to submit the file being acknowledged. |
| Attributes: |  |
| Limits: | Mandatory for processing  10 numeric characters  One per **ReportSubmissionResponseFileHeader** |
| Example: | `<PkiCertificateNumber>1211379999</PkiCertificateNumber>` |
| Remarks: |  |

#### ExternalFileStatusCode (Batch status message)

![ExternalFileStatusCode](images/Mod1/image015.gif)

Batch status message

| Definition: | This is the processing status code to indicate whether the batch file has been accepted or rejected. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 numeric character  One per **ReportSubmissionResponseFileHeader** |
| Example: | `ExternalFileStatusCode>1</ExternalFileStatusCode>` |
| Remarks: | Codes:  1 - Accepted  2 - Rejected |

#### ReportAcceptCount (Reports accepted)

![ReportAcceptCount](images/Mod1/image016.gif)

Reports accepted

| Definition: | This is the number of reports accepted. |
| Attributes: |  |
| Limits: | Mandatory for processing  0 to 999999999 numeric characters  One per **ReportSubmissionReportResponseFileHeader** |
| Example: | `<ReportAcceptCount>750</ReportAcceptCount>` |
| Remarks: |  |

#### ReportRejectCount (Reports rejected)

![ReportRejectCount](images/Mod1/image017.gif)

Reports rejected

| Definition: | This is the number of reports rejected. |
| Attributes: |  |
| Limits: | Mandatory for processing  0 to 999999999 numeric characters  One per **ReportSubmissionReportResponseFileHeader** |
| Example: | `<ReportRejectCount>0</ReportRejectCount>` |
| Remarks: |  |

#### ReportSubmissionResponseLineItem (Messages on accepted reports, reports in error and reports rejected (for accepted batches only))

![ReportSubmissionResponseLineItem](images/Mod1/image018.gif)

Messages on accepted reports, reports in error and reports rejected (for accepted batches only)

| Definition: | This is the container for information about the error or warning messages for a report. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per **ReportSubmissionResponseXmlFile** |
| Example: | ``` <ReportSubmissionResponseLineItem>  <XmlDataElementName>CasinoDisbursementReportXMLFile/  CasinoDisbursementReport[2]/CasinoTransaction[1]/ CasinoTransactionDetail/TransactionDate</XmlDataElementName>  <MessageNumber>303</MessageNumber>  <OrganizationReportReferenceIdentifier>Report02  </OrganizationReportReferenceIdentifier> </ReportSubmissionResponseLineItem> 			 ``` |
| Remarks: |  |

#### XmlDataElementName (XML element name)

![XmlDataElementName](images/Mod1/image019.gif)

XML element name

| Definition: | This is the name of the element to which the message relates. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 400 characters  One per **ReportSubmissionResponseLineItem** |
| Example: | `<XmlDataElementName>CasinoDisbursementReportXMLFile/  CasinoDisbursementReport[2]/CasinoTransaction[1]/CasinoTransactionDetail/  TransactionDate</XmlDataElementName>` |
| Remarks: | The number with the square brackets indicates the index of the element within the XML. In the example, the error was caused by the first transaction within the second report. |

#### MessageNumber (Validation message)

![MessageNumber](images/Mod1/image020.gif)

Validation message

| Definition: | This is the error message code identifying the applicable issue. See section 8 for information about these messages. |
| Attributes: |  |
| Limits: | Mandatory for processing  3 numeric characters  One per **ReportSubmissionResponseLineItem** |
| Example: | `<MessageNumber>303</MessageNumber>` |
| Remarks: |  |

#### OrganizationReportReferenceIdentifier (Reporting entity report reference number)

![OrganizationReportReferenceIdentifier](images/Mod1/image021.gif)

Reporting entity report reference number

| Definition: | This is the unique report reference number of the report. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 20 characters  One per **ReportSubmissionResponseLineItem** |
| Example: | `<OrganizationReportReferenceIdentifier>Report02  </OrganizationReportReferenceIdentifier>` |
| Remarks: |  |

#### ValidationRuleNumber (Validation rule that caused the validation message)

![ValidationRuleNumber](images/Mod1/validation.gif)

Validation rule that caused the validation message

| Definition: | This is the validation rule number identifying the applicable issue. See section 8.1 for information about these message rules. |
| Attributes: |  |
| Limits: | Mandatory for processing   9 numeric characters  One per **ReportSubmissionResponseLineItem** |
| Example: | `<ValidationRuleNumber>200030</ValidationRuleNumber>` |
| Remarks: |  |

#### ReportSubmissionResponseFileTrailer (Batch file trailer)

![ReportSubmissionResponseFileTrailer](images/Mod1/image022.gif)

Batch file trailer

| Definition: | This is the container for the acknowledgement file trailer. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per **ReportSubmissionResponseXmlFile** |
| Example: | ```  <ReportSubmissionResponseFileTrailer>  <ResponseLineItemCount>1</ResponseLineItemCount> </ReportSubmissionResponseFileTrailer> ``` |
| Remarks: |  |

#### ResponseLineItemCount (Message count)

![ResponseLineItemCount](images/Mod1/image023.gif)

Message count

| Definition: | This is the total number of **ReportSubmissionLineItem** records contained in the acknowledgement file. |
| Attributes: |  |
| Limits: | Mandatory for processing  0 to 999999999 numeric characters  One per **ReportSubmissionResponseFileTrailer** |
| Example: | `<ResponseLineItemCount>1</ResponseLineItemCount>` |
| Remarks: |  |

### 6.2 General acknowledgement example

#### 6.2.1 Acknowledgement example for an accepted batch

```

<?xml version="1.0" encoding="UTF-8"?>
<ReportSubmissionResponseXmlFile>
 <ReportSubmissionResponseFileHeader>
  <SubmitOrganizationNumber>987654</SubmitOrganizationNumber>
  <ExternalFileName>20090928_223915_CDR.XML</ExternalFileName>
  <ExternalFileSequenceNumber>1</ExternalFileSequenceNumber>
  <ReportTypeCode>13</ReportTypeCode>
  <OperationModeCode>2</OperationModeCode>
  <PkiCertificateNumber>1211379999</PkiCertificateNumber>
  <ExternalFileStatusCode>1</ExternalFileStatusCode>
  <ReportAcceptCount>750</ReportAcceptCount>
  <ReportRejectCount>0</ReportRejectCount>
 </ReportSubmissionResponseFileHeader>
 <ReportSubmissionResponseLineItem>
  <XmlDataElementName>CasinoDisbursementReportXMLFile/
  CasinoDisbursementReport[2]/CasinoTransaction[1]/
CasinoTransactionDetail/TransactionDate</XmlDataElementName>
  <MessageNumber>303</MessageNumber>
  <OrganizationReportReferenceIdentifier>Report02
  </OrganizationReportReferenceIdentifier>
 </ReportSubmissionResponseLineItem>
 <ReportSubmissionResponseFileTrailer>
  <ResponseLineItemCount>1</ResponseLineItemCount>
 </ReportSubmissionResponseFileTrailer>
</ReportSubmissionResponseXmlFile> 
	
```

#### 6.2.2 Acknowledgement example for a rejected batch

```

<?xml version="1.0" encoding="UTF-8"?>
<ReportSubmissionResponseXmlFile>
 <ReportSubmissionResponseFileHeader>
  <SubmitOrganizationNumber>987654</SubmitOrganizationNumber>
  <ExternalFileName>20090928_223915_CDR.XML</ExternalFileName>
  <ExternalFileSequenceNumber>1</ExternalFileSequenceNumber>
  <ReportTypeCode>13</ReportTypeCode>
  <OperationModeCode>2</OperationModeCode>
  <PkiCertificateNumber>1211379999</PkiCertificateNumber>
  <ExternalFileStatusCode>2</ExternalFileStatusCode>
  <ReportAcceptCount>0</ReportAcceptCount>
  <ReportRejectCount>1</ReportRejectCount>
 </ReportSubmissionResponseFileHeader>
 <ReportSubmissionResponseLineItem>
  <XmlDataElementName>CasinoDisbursementReportXMLFile</XmlDataElementName>
  <MessageNumber>412</MessageNumber>
  <OrganizationReportReferenceIdentifier></OrganizationReportReferenceIdentifier>1
 </ReportSubmissionResponseLineItem>
 <ReportSubmissionResponseFileTrailer>
  <ResponseLineItemCount>1</ResponseLineItemCount>
 </ReportSubmissionResponseFileTrailer>
</ReportSubmissionResponseXmlFile>
	
```

## 7 Reports Returned for Further Action (RRFA)

### 7.1 RRFA Message Formatting

The following tables outline the format for RRFA files that will be sent to you by FINTRAC if you choose to deal with RRFA by batch for reports that were originally submitted by batch.

#### ?xml (XML declaration)

XML declaration

| Definition: | This is the top level XML declaration which specifies the version of XML being used. |
| Attributes: | **version**:  fixed: "1.0"  **encoding**:  fixed: "UTF-8" |
| Limits: | Mandatory for processing  One per submission instance |
| Example: | `<?xml version="1.0" encoding="UTF-8" ?>` |
| Remarks: | This declaration is required to be **alone** on the first line of the file. The version number and encoding are fixed to the version of the schema. |

#### ReportReturnForFurtherActionXmlFile (Root element)

![ReportReturnForFurtherActionXmlFile](images/Mod1/image024.gif)

Root element

| Definition: | This is the container for the following batch file contents:  **ReportReturnForFurtherActionFileHeader**  **ReportReturnForFurtherActionLineItem**  **ReportReturnForFurtherActionFileTrailer** |
| Attributes: |  |
| Limits: | Mandatory for processing  One per submission instance |
| Example: | `<ReportReturnForFurtherActionXmlFile>…</ReportReturnForFurtherActionXmlFile>` |
| Remarks: |  |

#### ReportReturnForFurtherActionFileHeader (Batch header)

![ReportReturnForFurtherActionFileHeader](images/Mod1/image025.gif)

Batch header

| Definition: | This is the container for the RRFA file contents. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per **ReportForFurtherActionXmlFile** |
| Example: | ``` <ReportReturnForFurtherActionFileHeader>  <SubmitOrganizationNumber>987654</SubmitOrganizationNumber>  <ReportTypeCode>13</ReportTypeCode>  <PkiCertificateNumber>1211379999</PkiCertificateNumber>  <ReturnReportForFurtherActionIdentifierNumber>125  </ReturnReportForFurtherActionIdentifierNumber>  <ReturnReportSummaryText>Please correct the following information …  </ReturnReportSummaryText>  <ReturnReportDueDate>20091112</ReturnReportDueDate>  <ReturnReportCount>20</ReturnReportCount>  <QualityIssueCount>45</QualityIssueCount>  <ExternalFileInvolveCount>45</ExternalFileInvolveCount> </ReportReturnForFurtherActionFileHeader> 			 ``` |
| Remarks: | This element uniquely identifies the XML RRFA batch file submitted to you from FINTRAC. |

#### SubmitOrganizationNumber (Reporting entity's identifier number)

![SubmitOrganizationNumber](images/Mod1/image009.gif)

Reporting entity's identifier number

| Definition: | This is the identifier number assigned to the individual or institution who transmitted the file with the reports being returned. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 7 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<SubmitOrganizationNumber>987654</SubmitOrganizationNumber>` |
| Remarks: |  |

#### ReportTypeCode (Report type)

![ReportTypeCode](images/Mod1/image012.gif)

Report type

| Definition: | This is the code used to identify the type of report. |
| Attributes: |  |
| Limits: | Mandatory for processing  2 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ReportTypeCode>13</ReportTypeCode>` |
| Remarks: | Code:  13 - Casino Disbursement Report |

#### PkiCertificateNumber (PKI certificate ID)

![PkiCertificateNumber](images/Mod1/image014.gif)

PKI certificate ID

| Definition: | This is the PKI certificate identifier number used to submit the reports being returned. |
| Attributes: |  |
| Limits: | Mandatory for processing  10 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<PkiCertificateNumber>1211379999</PkiCertificateNumber>` |
| Remarks: |  |

#### ReturnReportForFurtherActionIdentifierNumber (RRFA ID number)

![ReturnReportForFurtherActionIdentifierNumber](images/Mod1/image026.gif)

RRFA ID number

| Definition: | FINTRAC's numeric identifier for the RRFA. |
| Attributes: |  |
| Limits: | Mandatory for processing  9 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ReturnReportForFurtherActionIdentifierNumber>125  </ReturnReportForFurtherActionIdentifierNumber>` |
| Remarks: |  |

#### ReturnReportSummaryText (RRFA summary text)

![ReturnReportSummaryText](images/Mod1/image027.gif)

RRFA summary text

| Definition: | This is the explanation of what issues need to be addressed. |
| Attributes: |  |
| Limits: | Mandatory for processing  unlimited  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ReturnReportSummaryText>Please correct the following information …</ReturnReportSummaryText>` |
| Remarks: |  |

#### ReturnReportDueDate (RRFA due date)

![ReturnReportDueDate](images/Mod1/image028.gif)

RRFA due date

| Definition: | This is the date by which the corrected reports should be submitted to FINTRAC. |
| Attributes: |  |
| Limits: | Mandatory for processing  8 characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ReturnReportDueDate>20091112</ReturnReportDueDate>` |
| Remarks: |  |

#### ReturnReportCount (Number of reports returned)

![ReturnReportCount](images/Mod1/image029.gif)

Number of reports returned

| Definition: | This is the total number of reports returned. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 999999999 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ReturnReportCount>20</ReturnReportCount>` |
| Remarks: |  |

#### QualityIssueCount (Number of quality issues)

![QualityIssueCount](images/Mod1/image030.gif)

Number of quality issues

| Definition: | This is the total number of data quality issues for all reports included in the RRFA. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 999999999 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<QualityIssueCount>45</QualityIssueCount>` |
| Remarks: |  |

#### ExternalFileInvolveCount (Number of batches involved)

![ExternalFileInvolveCount](images/Mod1/image031.gif)

Number of batches involved

| Definition: | The total number of batches involved. |
| Attributes: |  |
| Limits: | Mandatory for processing  0 to 999999999 numeric characters  One per **ReportReturnForFurtherActionFileHeader** |
| Example: | `<ExternalFileInvolveCount>45</ExternalFileInvolveCount>` |
| Remarks: |  |

#### ReportReturnForFurtherActionLineItem (Data quality issues messages)

![ReportReturnForFurtherActionLineItem](images/Mod1/image032.gif)

Data quality issues messages

| Definition: | The container for information related to the individual data quality issue. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per **ReportForFurtherActionXmlFile** |
| Example: | ``` <ReportReturnForFurtherActionLineItem>  <ExternalFileName>20090928_223915_CDR.XML</ExternalFileName>  <ExternalFileNameSequenceNumber>21  </ExternalFileNameSequenceNumber>  <OrganizationReportReferenceIdentifier>Report04  </OrganizationReportReferenceIdentifier>           <XmlDataElementName>CasinoDisbursementReportXMLFile/  CasinoDisbursementReport[4]/CasinoTransaction[1]/ CasinoTransactionDetail/TransactionDate</XmlDataElementName>  <MessageNumber>306</MessageNumber> </ReportReturnForFurtherActionLineItem> 			 ``` |
| Remarks: |  |

#### ExternalFileName (Batch file name)

![ExternalFileName](images/Mod1/image010.gif)

Batch file name

| Definition: | This is the identifier for the batch report file to which the returned report belonged. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 80 characters  One per **ReportReturnForFurtherActionLineItem** |
| Example: | `<ExternalFileName>20091010_1101112_CDR.xml</ExternalFileName>` |
| Remarks: | Names should not contain spaces or dashes |

#### ExternalFileNameSequenceNumber (Batch sequence number)

![ExternalFileNameSequenceNumber](images/Mod1/image033.gif)

Batch sequence number

| Definition: | This number represents the nth time the external file was submitted to FINTRAC. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 999999999 numeric characters  One per **ReportReturnForFurtherActionLineItem** |
| Example: | `<ExternalFileNameSequenceNumber>21</ExternalFileNameSequenceNumber>` |
| Remarks: |  |

#### OrganizationReportReferenceIdentifier (Reporting entity report reference number)

![OrganizationReportReferenceIdentifier](images/Mod1/image021.gif)

Reporting entity report reference number

| Definition: | This is the unique report reference number of report the report. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 20 characters  One per **ReportReturnForFurtherActionLineItem** |
| Example: | `<OrganizationReportReferenceIdentifier>Report04  </OrganizationReportReferenceIdentifier>` |
| Remarks: |  |

#### XmlDataElementName (XML element name)

![XmlDataElementName](images/Mod1/image019.gif)

XML element name

| Definition: | This is the name of the element to which the message relates. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 400 characters  One per **ReportReturnForFurtherActionLineItem** |
| Example: | `<XmlDataElementName>CasinoDisbursementReportXMLFile/  CasinoDisbursementReport[4]/CasinoTransaction[1]/CasinoTransactionDetail/  TransactionDate</XmlDataElementName>` |
| Remarks: | The number with the square brackets indicates the index of the element within the XML. In the example, the data quality issue can be found in the first transaction within the fourth report. |

#### MessageNumber (Data quality message number)

![MessageNumber](images/Mod1/image020.gif)

Data quality message number

| Definition: | This is the error message code identifying the applicable issue. See section 8 for information about these messages. |
| Attributes: |  |
| Limits: | Mandatory for processing  3 numeric characters  One per **ReportReturnForFurtherActionLineItem** |
| Example: | `<MessageNumber>306</MessageNumber>` |
| Remarks: |  |

#### ReportReturnForFurtherActionFileTrailer (Batch trailer)

![ReportReturnForFurtherActionFileTrailer](images/Mod1/image034.gif)

Batch trailer

| Definition: | This is the container for the RRFA file trailer. |
| Attributes: |  |
| Limits: | Mandatory for processing  One per**ReportForFurtherActionXmlFile** |
| Example: | ```  <ReportReturnForFurtherActionFileTrailer>  <ResponseLineItemCount>1</ResponseLineItemCount> </ReportReturnForFurtherActionFileTrailer> 			 ``` |
| Remarks: |  |

#### ReportLineItemCount (Message count)

![ReportLineItemCount](images/Mod1/image035.gif)

Message count

| Definition: | This is the total number of **ResponseLineItem** records contained in the RRFA file. |
| Attributes: |  |
| Limits: | Mandatory for processing  1 to 999999999 numeric characters  One per **ReportReturnForFurtherActionFileTrailer** |
| Example: | `<ReportLineItemCount>1</ReportLineItemCount>` |
| Remarks: |  |

### 7.2 RRFA message example

```

        <?xml version="1.0" encoding="UTF-8"?>
        <ReportReturnForFurtherActionXmlFile>
         <ReportReturnForFurtherActionFileHeader>
          <SubmitOrganizationNumber>987654</SubmitOrganizationNumber>
          <ReportTypeCode>13</ReportTypeCode>
          <PkiCertificateNumber>1211379999</PkiCertificateNumber>
          <ReturnReportForFurtherActionIdentifierNumber>125
          </ReturnReportForFurtherActionIdentifierNumber>
          <ReturnReportSummaryText>Please correct the following information …
          </ReturnReportSummaryText>
          <ReturnReportDueDate>20091112</ReturnReportDueDate>
          <ReturnReportCount>20</ReturnReportCount>
          <QualityIssueCount>45</QualityIssueCount>
          <ExternalFileInvolveCount>45</ExternalFileInvolveCount>
         </ReportReturnForFurtherActionFileHeader>
         <ReportReturnForFurtherActionLineItem>
          <ExternalFileName>20090928_223915_CDR.XML</ExternalFileName>
          <ExternalFileNameSequenceNumber>21</ExternalFileNameSequenceNumber>
          <OrganizationReportReferenceIdentifier>Report04
          </OrganizationReportReferenceIdentifier> 
          <XmlDataElementName>CasinoDisbursementReportXMLFile/
          CasinoDisbursementReport[4]/CasinoTransaction[1]/
        CasinoTransactionDetail/TransactionDate</XmlDataElementName>
          <MessageNumber>306</MessageNumber>
         </ReportReturnForFurtherActionLineItem>
         <ReportReturnForFurtherActionFileTrailer>
          <ResponseLineItemCount>1</ResponseLineItemCount>
         </ReportReturnForFurtherActionFileTrailer>
        </ReportReturnForFurtherActionXmlFile>
```

## 8 8 Report Validation and Processing Error Codes

### 8.1 Report validation rules

Report validation rules apply at the field level to reports within an accepted batch to ensure that reports are error-free (i.e., they contain the required fields, the fields are formatted correctly, and the data is valid). Validation rule messages (**ValidationRuleNumber**) are included as part of the **ReportSubmissionResponseLineItem** in the batch acknowledgement file to identify rejected reports and provide warnings about accepted reports based on these validation rules.

A report validation rules table is available for download in the technical documentation area of FINTRAC's website at https://fintrac-canafe.canada.ca. The table provides a description of the validation applied to each field within the reports.

### 8.2 Batch error codes

Batch processing error codes (**MessageNumber**) are included as part of the **ReportSubmissionResponseLineItem** in the batch acknowledgement file from FINTRAC. Error codes are also as part of the **MessageNumber** of the RRFA file to identify quality issues. A code table for these error messages is available for download, along with other code tables, in the technical publications area of the publications section of FINTRAC's website at https://fintrac-canafe.canada.ca.

In the error code table, certain error codes such as 9, 77, 300 to 362, 442 and 986 to 993 apply at the **element** level to reports within an **accepted** batch. These error codes apply to explain why a report was rejected or to provide a warning message concerning an accepted report.

The rest of the error codes (e.g., codes 400 to 436) are used when an entire batch file is **rejected**. In the case of a rejected batch, the error codes in the acknowledgement file will reflect FINTRAC's attempt to process the batch. It is possible that there were other errors that processing did not get far enough to detect.

## 9 External File Name

The following provides batch file naming recommendations to ensure all batch files for an organization have a unique name.

### 9.1 Batch file naming standard

Use the following naming convention for your batch files: Date\_Time\_Report Type.FileExtension

Each element of this naming convention is required, except for the report type, as follows:

* The date is required (YYYYMMDD).
* The time is required (HHMMSS).
* The report type is optional (CDR).
* The following file extension is required: ".XML" The batch will be refused for any other file extension values.

Example: 20090928\_223915\_CDR.XML

File names may only include standard upper/lower case alphanumeric characters (A to Z and 0 to 9). The only separator allowed is the underscore character "\_". The file name must only have one dot extension (e.g., .xml). File names containing spaces will cause the file to be rejected.

In this context, the upper case of any letter is considered the same as the lower case of that letter. For example, a batch file name of 20090928\_223915\_CDR.XML is considered the same as 20090928\_223915\_cdr.xml.

All new batch files that you submit to FINTRAC must have a unique file name, regardless of the file contents, or the file will be rejected.

### 9.2 FINTRAC batch acknowledgement naming convention

The acknowledgement file sent to you by FINTRAC will have the same name as your original batch file name, but with a different suffix. For batch files with no batch reject or report validation messages the suffix will be ".001". For those files with reject or validation messages, the suffix will be as follows:

* File\_name.002: All reports accepted but some warning messages
* File\_name.004: Batch accepted but some rejected reports
* File\_name.005: Batch rejected for structural reasons (bad file name, invalid contents, report counts do not match, etc.)

### 9.3 RRFA batch file naming convention

The following naming convention will be used by FINTRAC for the RRFA notification file sent to you:

* **RRFA\_DRM\_999999999.xml**

The "999999999" represents the RRFA number reflected in **ReturnReportForFurtherActionIdentifierNumber** of the RRFA message.

[1](#n2) The **OrganizationReportReferenceIdentifier** element will be empty as the entire batch has been rejected.

Date Modified:
:   2017-06-29