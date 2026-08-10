---
title: "Validation rules for the submission of Casino Disbursement Report by API"
regulator: "fintrac"
doc_type: "announcement"
status: "final"
source_kind: "web"
source_url: "https://fintrac-canafe.canada.ca/reporting-declaration/info/api/validation/cdr-ddc-eng.php"
version: "1"
---

# Validation rules for the submission of Casino Disbursement Report by API

Updated on June 23, 2026

Provides reporting entities with the rules used to validate reports of casino disbursements submitted through API to the Financial Transactions and Reports Analysis Centre of Canada (FINTRAC).

[![](/images/download.png)

Casino Disbursement Report validations rules  (XLS, 283 kb)](cdr-ddc-eng.xls)

## Field name: Date/time of disbursement

Field ID: cdr.disbursement.casinoDisbursementDetails.dateTimeOfDisbursement

### **Rule:** 151020

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151021

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the format yyyy-mm-ddThh:mm:ss-zz:zz.

**Message:** Invalid format. (362)

  

### **Rule:** 151022

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before now.

**Message:** The field cannot contain a future date. (304)

  

### **Rule:** 151023

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not between cdr.reportDetails.twentyFourHourRule.periodStart and cdr.reportDetails.twentyFourHourRule.periodEnd.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

### **Rule:** 151024

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not after 2009-09-28.

**Message:** The date in the field is too far in the past. (308)

  

## Field name: Method of disbursement - other

Field ID: cdr.disbursement.casinoDisbursementDetails.methodOther

### **Rule:** 151040

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.methodTypeCode is Other (7).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 151041

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.casinoDisbursementDetails.methodTypeCode is not Other (7).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 151042

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: Method of disbursement

Field ID: cdr.disbursement.casinoDisbursementDetails.methodTypeCode

### **Rule:** 151050

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151051

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=In person
- 2=Automated banking machine
- 3=Armoured car
- 4=Courier
- 5=Mail deposit
- 6=Telephone
- 7=Other
- 8=Night deposit
- 9=Quick drop
- 10=Self-redemption kiosk
- 11=Virtual currency ATM
- 12=Online

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Reporting entity transaction reference number

Field ID: cdr.disbursement.casinoDisbursementDetails.reportingEntityTransactionReference

### **Rule:** 151030

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151031

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: Threshold indicator

Field ID: cdr.disbursement.casinoDisbursementDetails.thresholdIndicator

### **Rule:** 151010

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151011

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and the amount of the disbursement is less than $ 10000 CAD or the user provided 'false' and the amount of the disbursement is greater than or equal to $ 10000 CAD. Disbursements containing foreign currency will have a $ 1000 CAD buffer (above and below) applied to the threshold calculation. A Ministerial Directive is not set.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

### **Rule:** 151012

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the user provided 'true' and the amount of the disbursement is less than $ 10000 CAD or the user provided 'false' and the amount of the disbursement is greater than or equal to $ 10000 CAD. Disbursements containing foreign currency will have a $ 1000 CAD buffer (above and below) applied to the threshold calculation. A Ministerial Directive is set.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Rule note:** Added June 23, 2026

  

## Field name: Completing action list

Field ID: cdr.disbursement.completingActions

### **Rule:** 152830

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 50.

**Message:** The list must be within the specified size. (332)

  

## Field name: Account information type

Field ID: cdr.disbursement.completingActions.details.account.accountTypeCode

### **Rule:** 152905

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account

  

### **Rule:** 154930

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account

  

### **Rule:** 155090

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Non-account based (reference numbers)

  

## Field name: Branch number

Field ID: cdr.disbursement.completingActions.details.account.branchNumber

### **Rule:** 154953

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 50 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Account currency type

Field ID: cdr.disbursement.completingActions.details.account.currencyCode

### **Rule:** 152940

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154990

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 152944

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Casino account

  

### **Rule:** 154994

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Financial institution account

  

## Field name: Date account opened

Field ID: cdr.disbursement.completingActions.details.account.dateOpened

### **Rule:** 152953

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 155003

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

### **Rule:** 152954

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Casino account

  

### **Rule:** 155004

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Financial institution account

  

## Field name: Financial institution number

Field ID: cdr.disbursement.completingActions.details.account.financialInstitutionNumber

### **Rule:** 154943

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 50 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Casino identifier number where the account is held

Field ID: cdr.disbursement.completingActions.details.account.heldAtLocationIdentifier

### **Rule:** 152960

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 152963

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 30 characters, containing only alpha and numeric characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 152964

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a branch location that is invalid for the reporting entity given the constraint to make sure this branch is valid and is in Canada.

**Message:** FINTRAC does not have this location on file for the reporting entity. (320)

**Condition:** Casino account

  

## Field name: Account holder list

Field ID: cdr.disbursement.completingActions.details.account.holders

### **Rule:** 152970

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Casino account

  

### **Rule:** 155010

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Financial institution account

  

## Field name: Name of entity

Field ID: cdr.disbursement.completingActions.details.account.holders.entityName.nameOfEntity

### **Rule:** 153040

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 155080

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Entity

  

### **Rule:** 153043

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 155083

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.details.account.holders.entityName.typeCode

### **Rule:** 153030

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 155070

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.details.account.holders.personName.givenName

### **Rule:** 153010

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155050

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Person

  

### **Rule:** 153013

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155053

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.details.account.holders.personName.otherNameInitial

### **Rule:** 153023

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155063

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.details.account.holders.personName.surname

### **Rule:** 153000

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155040

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Person

  

### **Rule:** 153003

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155043

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.details.account.holders.personName.typeCode

### **Rule:** 152990

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 155030

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.details.account.holders.typeCode

### **Rule:** 152980

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Casino account / Holder

  

### **Rule:** 155020

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Financial institution account / Holder

  

### **Rule:** 152981

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person name (1), Entity name (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder

  

### **Rule:** 155021

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person name (1), Entity name (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder

  

## Field name: Account number

Field ID: cdr.disbursement.completingActions.details.account.number

### **Rule:** 152910

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154960

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 152913

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 154963

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Other number related to reference number

Field ID: cdr.disbursement.completingActions.details.account.otherRelatedReferenceNumber

### **Rule:** 155110

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.account.referenceNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Non-account based (reference numbers)

  

### **Rule:** 155113

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Non-account based (reference numbers)

  

## Field name: Reference number

Field ID: cdr.disbursement.completingActions.details.account.referenceNumber

### **Rule:** 155100

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Non-account based (reference numbers)

  

### **Rule:** 155103

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Non-account based (reference numbers)

  

## Field name: Account type

Field ID: cdr.disbursement.completingActions.details.account.typeCode

### **Rule:** 152920

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154970

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value into this field.

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Financial institution account

  

### **Rule:** 152923

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 2=Front money
- 3=Other
- 4=Advance on credit
- 5=Safekeeping

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Casino account

  

### **Rule:** 154971

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Personal
- 2=Business
- 3=Trust
- 4=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Financial institution account

  

## Field name: Account type - other

Field ID: cdr.disbursement.completingActions.details.account.typeOther

### **Rule:** 152930

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.account.typeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 152931

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.account.typeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Casino account

  

### **Rule:** 154980

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.account.typeCode is Other (4).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 154981

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.account.typeCode is not Other (4).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Financial institution account

  

### **Rule:** 152932

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 154982

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Account information type

Field ID: cdr.disbursement.completingActions.details.accountCategoryCode

### **Rule:** 152900

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 152901

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Casino account
- 2=Financial institution account
- 3=Non-account based (reference numbers)
- 4=Not applicable

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

### **Rule:** 152902

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not 4 and cdr.disbursement.completingActions.details.account.accountTypeCode is blank or missing.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

## Field name: Amount

Field ID: cdr.disbursement.completingActions.details.amount

### **Rule:** 152860

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.valueInCanadianDollars is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 152861

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.valueInCanadianDollars is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 152864

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided an amount that is not the correct format:
- 17 digits (max), decimal separator and 10 digits (max).
- If a decimal separator is used, one digit before and two decimal places must be provided.

**Message:** Invalid format. (362)

  

### **Rule:** 152865

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if after currency conversion, the Canadian equivalent amount is not less than the reasonable upper limit of $ 1,000,000,000,000.

**Message:** After currency conversion, the Canadian equivalent amount must be less than the reasonable upper limit of $1,000,000,000,000. (341)

  

## Field name: Currency type

Field ID: cdr.disbursement.completingActions.details.currencyCode

### **Rule:** 152870

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.valueInCanadianDollars is blank and cdr.disbursement.completingActions.details.amount is not blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 152875

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Type of disbursement - other

Field ID: cdr.disbursement.completingActions.details.disbursementOther

### **Rule:** 152850

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.disbursementTypeCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 152851

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.disbursementTypeCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 152852

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: Type of disbursement

Field ID: cdr.disbursement.completingActions.details.disbursementTypeCode

### **Rule:** 152840

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 152843

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Applied to credit card
- 2=Added to a casino stored value card
- 3=Deposited to account - financial inst.
- 4=Issued a cheque
- 5=Sent international funds transfer
- 6=Sent domestic funds transfer
- 7=Paid out in cash
- 8=Transferred to another casino
- 9=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Was there any other person or entity involved in the disbursement?

Field ID: cdr.disbursement.completingActions.details.involvementsIndicator

### **Rule:** 152890

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 152891

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and involvements is empty or the user provided 'false' and involvements is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

## Field name: Value in Canadian dollars

Field ID: cdr.disbursement.completingActions.details.valueInCanadianDollars

### **Rule:** 152880

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.details.amount is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 152881

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.details.amount is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 152884

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided an amount that is not the correct format:
- 17 digits (max), decimal separator and 10 digits (max).
- If a decimal separator is used, one digit before and two decimal places must be provided.

**Message:** Invalid format. (362)

  

## Field name: Account number

Field ID: cdr.disbursement.completingActions.involvements.details.accountNumber

### **Rule:** 154700

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.involvements.details.identifyingNumber, cdr.disbursement.completingActions.involvements.details.policyNumber are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Involvement

  

### **Rule:** 154703

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement

  

## Field name: Identifying number

Field ID: cdr.disbursement.completingActions.involvements.details.identifyingNumber

### **Rule:** 154720

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.involvements.details.accountNumber, cdr.disbursement.completingActions.involvements.details.policyNumber are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Involvement

  

### **Rule:** 154723

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement

  

## Field name: Policy number

Field ID: cdr.disbursement.completingActions.involvements.details.policyNumber

### **Rule:** 154710

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.involvements.details.accountNumber, cdr.disbursement.completingActions.involvements.details.identifyingNumber are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Involvement

  

### **Rule:** 154713

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement

  

## Field name: Name of entity

Field ID: cdr.disbursement.completingActions.involvements.entityName.nameOfEntity

### **Rule:** 154691

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Involvement / Entity

  

### **Rule:** 154693

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.involvements.entityName.typeCode

### **Rule:** 154680

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.involvements.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Involvement / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.involvements.personName.givenName

### **Rule:** 154651

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Involvement / Person

  

### **Rule:** 154653

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.involvements.personName.otherNameInitial

### **Rule:** 154673

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement / Person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.involvements.personName.surname

### **Rule:** 154661

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Involvement / Person

  

### **Rule:** 154663

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Involvement / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.involvements.personName.typeCode

### **Rule:** 154640

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.involvements.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Involvement / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.involvements.typeCode

### **Rule:** 154630

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Involvement

  

### **Rule:** 154631

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person name (1), Entity name (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Involvement

  

## Field name: Receiver list

Field ID: cdr.disbursement.completingActions.receivers

### **Rule:** 153090

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

  

### **Rule:** 153091

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

  

## Field name: Client number

Field ID: cdr.disbursement.completingActions.receivers.details.clientNumber

### **Rule:** 153783

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

  

## Field name: Email address

Field ID: cdr.disbursement.completingActions.receivers.details.emailAddress

### **Rule:** 153793

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that does not adhere to the RFC5322 Internet Message Format or exceeded the maximum length of 200.

**Message:** Invalid format. (362)

  

## Field name: Was this transaction conducted on behalf of another person or entity?

Field ID: cdr.disbursement.completingActions.receivers.details.onBehalfOfIndicator

### **Rule:** 153850

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 153851

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs is empty or the user provided 'false' and cdr.disbursement.completingActions.receivers.onBehalfOfs is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

## Field name: Relationship

Field ID: cdr.disbursement.completingActions.receivers.details.relationshipWithRequestedOnBehalfOfCode

### **Rule:** 153833

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Accountant
- 2=Agent
- 3=Borrower
- 4=Broker
- 5=Customer
- 6=Employee
- 7=Friend
- 8=Relative
- 9=Other
- 10=Legal counsel
- 11=Employer
- 12=Joint/Secondary owner
- 13=Power of attorney
- 14=Vendor/Supplier

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Relationship - other

Field ID: cdr.disbursement.completingActions.receivers.details.relationshipWithRequestedOnBehalfOfOther

### **Rule:** 153840

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.details.relationshipWithRequestedOnBehalfOfCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 153841

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.details.relationshipWithRequestedOnBehalfOfCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 153842

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: Relationship

Field ID: cdr.disbursement.completingActions.receivers.details.relationshipWithRequesterCode

### **Rule:** 153812

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 153813

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Accountant
- 2=Agent
- 3=Borrower
- 4=Broker
- 5=Customer
- 6=Employee
- 7=Friend
- 8=Relative
- 9=Other
- 10=Legal counsel
- 11=Employer
- 12=Joint/Secondary owner
- 13=Power of attorney
- 14=Vendor/Supplier
- 15=Self

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Relationship - other

Field ID: cdr.disbursement.completingActions.receivers.details.relationshipWithRequesterOther

### **Rule:** 153820

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.details.relationshipWithRequesterCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 153821

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.details.relationshipWithRequesterCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 153822

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: User name

Field ID: cdr.disbursement.completingActions.receivers.details.username

### **Rule:** 153803

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

  

## Field name: House/Building number

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.buildingNumber

### **Rule:** 153470

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153473

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: City

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.city

### **Rule:** 153490

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153491

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153492

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153493

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Country

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode

### **Rule:** 153552

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153553

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153554

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity

  

## Field name: District

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.district

### **Rule:** 153500

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153503

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.postalZipCode

### **Rule:** 153540

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153541

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured is blank and cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153542

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

### **Rule:** 153543

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Entity

  

## Field name: Province or state code

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.provinceStateCode

### **Rule:** 153511

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153512

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153513

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153516

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153515

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity

  

## Field name: Province or state name

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.provinceStateName

### **Rule:** 153520

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153523

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153524

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Street address

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.streetAddress

### **Rule:** 153480

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153481

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153482

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153483

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.subProvinceSubLocality

### **Rule:** 153530

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153533

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.typeCode

### **Rule:** 153450

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Entity

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.unitNumber

### **Rule:** 153460

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153461

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.address.unstructured

### **Rule:** 153560

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153561

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.entityDetails.address.unitNumber, cdr.disbursement.completingActions.receivers.entityDetails.address.buildingNumber, cdr.disbursement.completingActions.receivers.entityDetails.address.streetAddress, cdr.disbursement.completingActions.receivers.entityDetails.address.city, cdr.disbursement.completingActions.receivers.entityDetails.address.district, cdr.disbursement.completingActions.receivers.entityDetails.address.provinceStateCode, cdr.disbursement.completingActions.receivers.entityDetails.address.provinceStateName, cdr.disbursement.completingActions.receivers.entityDetails.address.subProvinceSubLocality, cdr.disbursement.completingActions.receivers.entityDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153562

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153563

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.addressTypeCode

### **Rule:** 153440

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153441

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153442

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Entity

  

## Field name: Authorized person list

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.authorizedPersons

### **Rule:** 153740

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 0 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Entity

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.authorizedPersons.givenName

### **Rule:** 153753

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Authorized person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.authorizedPersons.otherNameInitial

### **Rule:** 153773

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Authorized person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.authorizedPersons.surname

### **Rule:** 153763

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Authorized person

  

## Field name: Extension

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.extensionNumber

### **Rule:** 153580

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity

  

### **Rule:** 153581

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Identification type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.identifierTypeCode

### **Rule:** 153680

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity / Identification

  

### **Rule:** 153681

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Articles of association
- 2=Certificate of corporate status
- 3=Certificate of incorporation
- 4=Letter/Notice of assessment
- 5=Partnership agreement
- 6=Annual report
- 7=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.identifierTypeOther

### **Rule:** 153690

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.entityDetails.identifications.identifierTypeCode is Other (7).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity / Identification

  

### **Rule:** 153691

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.identifications.identifierTypeCode is not Other (7).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Identification

  

### **Rule:** 153692

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 153710

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity / Identification

  

### **Rule:** 153714

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 153720

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Identification

  

### **Rule:** 153721

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.entityDetails.identifications.identifierTypeCode is one of Certificate of corporate status (2), Certificate of incorporation (3), Letter/Notice of assessment (4) and cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity / Identification

  

### **Rule:** 153724

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 153730

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Identification

  

### **Rule:** 153733

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.identifications.number

### **Rule:** 153700

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value into this field.

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity / Identification

  

### **Rule:** 153703

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Identification

  

## Field name: Name of entity

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.nameOfEntity

### **Rule:** 153431

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity

  

### **Rule:** 153433

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153434

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Nature of entity's principal business

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.natureOfPrincipalBusiness

### **Rule:** 153592

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Entity

  

### **Rule:** 153593

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Is the entity registered or incorporated?

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationIncorporationIndicator

### **Rule:** 153600

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Entity

  

### **Rule:** 153601

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and registrationsIncorporations is empty or the user provided 'false' and registrationsIncorporations is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Condition:** Entity

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode

### **Rule:** 153640

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153641

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153644

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateCode

### **Rule:** 153650

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153651

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153654

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateName

### **Rule:** 153660

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153661

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153663

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Registration or incorporation

  

## Field name: Registration or incorporation number

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.number

### **Rule:** 153630

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153631

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153633

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Entity / Registration or incorporation

  

## Field name: Registration/incorporation type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.registrationsIncorporations.typeCode

### **Rule:** 153620

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Entity / Registration or incorporation

  

### **Rule:** 153621

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Registered
- 2=Incorporated
- 4=Registered and incorporated
- 5=Unknown

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Entity / Registration or incorporation

  

## Field name: Telephone number

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.telephoneNumber

### **Rule:** 153573

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.entityDetails.typeCode

### **Rule:** 153420

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Entity

  

## Field name: Client number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.clientNumber

### **Rule:** 154553

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of

  

## Field name: Email address

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.emailAddress

### **Rule:** 154563

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that does not adhere to the RFC5322 Internet Message Format or exceeded the maximum length of 200.

**Message:** Invalid format. (362)

**Condition:** On behalf of

  

## Field name: Relationship

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithReceiverCode

### **Rule:** 154572

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of

  

### **Rule:** 154573

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Accountant
- 2=Agent
- 3=Borrower
- 4=Broker
- 5=Customer
- 6=Employee
- 7=Friend
- 8=Relative
- 9=Other
- 10=Legal counsel
- 11=Employer
- 12=Joint/Secondary owner
- 13=Power of attorney
- 14=Vendor/Supplier
- 15=Self

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of

  

## Field name: Relationship - other

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithReceiverOther

### **Rule:** 154580

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithReceiverCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of

  

### **Rule:** 154581

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithReceiverCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of

  

### **Rule:** 154582

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of

  

## Field name: Relationship

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithRequesterCode

### **Rule:** 154593

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Accountant
- 2=Agent
- 3=Borrower
- 4=Broker
- 5=Customer
- 6=Employee
- 7=Friend
- 8=Relative
- 9=Other
- 10=Legal counsel
- 11=Employer
- 12=Joint/Secondary owner
- 13=Power of attorney
- 14=Vendor/Supplier

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of

  

## Field name: Relationship - other

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithRequesterOther

### **Rule:** 154600

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithRequesterCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of

  

### **Rule:** 154601

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.details.relationshipWithRequesterCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of

  

### **Rule:** 154602

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of

  

## Field name: User name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.details.username

### **Rule:** 154613

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of

  

## Field name: House/Building number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.buildingNumber

### **Rule:** 154240

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154243

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: City

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.city

### **Rule:** 154260

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154262

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154263

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Country

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode

### **Rule:** 154322

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154324

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity

  

## Field name: District

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.district

### **Rule:** 154270

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154273

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.postalZipCode

### **Rule:** 154310

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154311

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured is blank and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** On behalf of / Entity

  

### **Rule:** 154312

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

### **Rule:** 154313

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** On behalf of / Entity

  

## Field name: Province or state code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.provinceStateCode

### **Rule:** 154280

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154282

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154283

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154285

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity

  

## Field name: Province or state name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.provinceStateName

### **Rule:** 154290

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154293

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154294

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Street address

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.streetAddress

### **Rule:** 154250

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154252

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154253

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.subProvinceSubLocality

### **Rule:** 154300

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154303

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.typeCode

### **Rule:** 154220

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Entity

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unitNumber

### **Rule:** 154230

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154233

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unstructured

### **Rule:** 154330

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154332

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.unitNumber, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.buildingNumber, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.streetAddress, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.city, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.district, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.provinceStateCode, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.provinceStateName, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.subProvinceSubLocality, cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154333

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.addressTypeCode

### **Rule:** 154210

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154212

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Entity

  

## Field name: Authorized person list

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.authorizedPersons

### **Rule:** 154510

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 0 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** On behalf of / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.authorizedPersons.givenName

### **Rule:** 154523

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Authorized person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.authorizedPersons.otherNameInitial

### **Rule:** 154543

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Authorized person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.authorizedPersons.surname

### **Rule:** 154533

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Authorized person

  

## Field name: Extension

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.extensionNumber

### **Rule:** 154350

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity

  

### **Rule:** 154351

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Identification type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.identifierTypeCode

### **Rule:** 154450

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154451

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Articles of association
- 2=Certificate of corporate status
- 3=Certificate of incorporation
- 4=Letter/Notice of assessment
- 5=Partnership agreement
- 6=Annual report
- 7=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.identifierTypeOther

### **Rule:** 154460

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.identifierTypeCode is Other (7).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154461

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.identifierTypeCode is not Other (7).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154462

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 154480

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154484

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 154490

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154491

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.identifierTypeCode is one of Certificate of corporate status (2), Certificate of incorporation (3), Letter/Notice of assessment (4) and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154494

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 154500

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154503

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.identifications.number

### **Rule:** 154470

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value into this field.

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** On behalf of / Entity / Identification

  

### **Rule:** 154473

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Identification

  

## Field name: Name of entity

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.nameOfEntity

### **Rule:** 154201

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity

  

### **Rule:** 154203

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Nature of entity's principal business

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.natureOfPrincipalBusiness

### **Rule:** 154363

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Is the entity registered or incorporated?

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationIncorporationIndicator

### **Rule:** 154370

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** On behalf of / Entity

  

### **Rule:** 154371

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations is empty or the user provided 'false' and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Condition:** On behalf of / Entity

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode

### **Rule:** 154410

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154411

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154414

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateCode

### **Rule:** 154420

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154422

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154424

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateName

### **Rule:** 154430

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154431

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154433

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Registration or incorporation

  

## Field name: Registration or incorporation number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.number

### **Rule:** 154400

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154401

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154403

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity / Registration or incorporation

  

## Field name: Registration/incorporation type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode

### **Rule:** 154390

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** On behalf of / Entity / Registration or incorporation

  

### **Rule:** 154391

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Registered
- 2=Incorporated
- 4=Registered and incorporated
- 5=Unknown

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Entity / Registration or incorporation

  

## Field name: Telephone number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.telephoneNumber

### **Rule:** 154343

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.entityDetails.typeCode

### **Rule:** 154190

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.onBehalfOfs.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Entity

  

## Field name: House/Building number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.buildingNumber

### **Rule:** 153960

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 153963

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: City

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.city

### **Rule:** 153980

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 153982

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 153983

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Country

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode

### **Rule:** 154042

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 154044

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person

  

## Field name: District

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.district

### **Rule:** 153990

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 153993

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.postalZipCode

### **Rule:** 154030

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154032

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured is blank and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** On behalf of / Person

  

### **Rule:** 154033

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

### **Rule:** 154034

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** On behalf of / Person

  

## Field name: Province or state code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.provinceStateCode

### **Rule:** 154000

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154002

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 154003

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154005

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person

  

## Field name: Province or state name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.provinceStateName

### **Rule:** 154010

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154013

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154014

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Street address

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.streetAddress

### **Rule:** 153970

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 153972

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 153973

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.subProvinceSubLocality

### **Rule:** 154020

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154023

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.typeCode

### **Rule:** 153940

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Person

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unitNumber

### **Rule:** 153950

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 153953

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unstructured

### **Rule:** 154050

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.unitNumber, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.buildingNumber, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.streetAddress, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.city, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.district, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.provinceStateCode, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.provinceStateName, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.subProvinceSubLocality, cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154052

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 154053

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.addressTypeCode

### **Rule:** 153930

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 153932

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Person

  

## Field name: Alias

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.alias

### **Rule:** 153923

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Country of residence

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.countryOfResidenceCode

### **Rule:** 154094

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person

  

## Field name: Date of birth

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.dateOfBirth

### **Rule:** 154083

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

### **Rule:** 154084

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** On behalf of / Person

  

### **Rule:** 154085

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not within the last -120 years.

**Message:** The date in the field is too far in the past. (308)

**Condition:** On behalf of / Person

  

## Field name: Extension

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.extensionNumber

### **Rule:** 154070

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person

  

### **Rule:** 154071

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.givenName

### **Rule:** 153892

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 153893

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Identification type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode

### **Rule:** 154130

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154131

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Birth certificate
- 2=Passport
- 3=Other
- 4=Driver's licence
- 5=Provincial health card
- 14=Citizenship card
- 15=Certificate of Indian Status
- 27=Social Insurance Number card
- 32=Permanent resident card
- 33=Record of landing
- 34=Credit file
- 35=Government issued identification
- 36=Insurance documents
- 37=Provincial or territorial identity card
- 38=Record of employment
- 39=Travel visa
- 40=Utility statement

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeOther

### **Rule:** 154140

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154141

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154142

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 154161

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Passport (2), Driver's licence (4), Provincial health card (5), Citizenship card (14), Certificate of Indian Status (15), Permanent resident card (32), Record of landing (33), Government issued identification (35), Provincial or territorial identity card (37), Travel visa (39).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154164

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 154170

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154171

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Driver's licence (4), Provincial health card (5), Government issued identification (35), Provincial or territorial identity card (37) and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154174

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 154180

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154183

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.number

### **Rule:** 154150

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is not Social Insurance Number card (27).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154151

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.identifications.identifierTypeCode is Social Insurance Number card (27).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** On behalf of / Person / Identification

  

### **Rule:** 154153

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person / Identification

  

## Field name: Name of employer

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.nameOfEmployer

### **Rule:** 154113

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Occupation

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.occupation

### **Rule:** 154103

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.otherNameInitial

### **Rule:** 153913

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.surname

### **Rule:** 153904

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** On behalf of / Person

  

### **Rule:** 153903

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Telephone number

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.telephoneNumber

### **Rule:** 154063

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** On behalf of / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.personDetails.typeCode

### **Rule:** 153880

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.onBehalfOfs.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.onBehalfOfs.typeCode

### **Rule:** 153870

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** On behalf of

  

### **Rule:** 153871

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person details (3), Entity details (4).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** On behalf of

  

## Field name: House/Building number

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.buildingNumber

### **Rule:** 153190

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153193

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: City

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.city

### **Rule:** 153210

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153211

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153212

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153213

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Country

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.countryCode

### **Rule:** 153271

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153272

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153274

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person

  

## Field name: District

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.district

### **Rule:** 153220

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153223

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.postalZipCode

### **Rule:** 153260

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153261

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.personDetails.address.unstructured is blank and cdr.disbursement.completingActions.receivers.personDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153262

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

### **Rule:** 153263

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.completingActions.receivers.personDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Person

  

## Field name: Province or state code

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.provinceStateCode

### **Rule:** 153230

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153231

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153233

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153232

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153235

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.personDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person

  

## Field name: Province or state name

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.provinceStateName

### **Rule:** 153240

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153243

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153244

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Street address

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.streetAddress

### **Rule:** 153200

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153201

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153202

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153203

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.subProvinceSubLocality

### **Rule:** 153250

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153253

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.typeCode

### **Rule:** 153170

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Person

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.unitNumber

### **Rule:** 153180

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153183

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.completingActions.receivers.personDetails.address.unstructured

### **Rule:** 153280

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.completingActions.receivers.personDetails.address.unitNumber, cdr.disbursement.completingActions.receivers.personDetails.address.buildingNumber, cdr.disbursement.completingActions.receivers.personDetails.address.streetAddress, cdr.disbursement.completingActions.receivers.personDetails.address.city, cdr.disbursement.completingActions.receivers.personDetails.address.district, cdr.disbursement.completingActions.receivers.personDetails.address.provinceStateCode, cdr.disbursement.completingActions.receivers.personDetails.address.provinceStateName, cdr.disbursement.completingActions.receivers.personDetails.address.subProvinceSubLocality, cdr.disbursement.completingActions.receivers.personDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153281

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153282

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153283

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Address type

Field ID: cdr.disbursement.completingActions.receivers.personDetails.addressTypeCode

### **Rule:** 153160

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153161

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153162

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Person

  

## Field name: Alias

Field ID: cdr.disbursement.completingActions.receivers.personDetails.alias

### **Rule:** 153153

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Country of residence

Field ID: cdr.disbursement.completingActions.receivers.personDetails.countryOfResidenceCode

### **Rule:** 153324

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person

  

## Field name: Date of birth

Field ID: cdr.disbursement.completingActions.receivers.personDetails.dateOfBirth

### **Rule:** 153317

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153313

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Person

  

### **Rule:** 153314

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Person

  

### **Rule:** 153315

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not within the last -120 years.

**Message:** The date in the field is too far in the past. (308)

**Condition:** Person

  

## Field name: Extension

Field ID: cdr.disbursement.completingActions.receivers.personDetails.extensionNumber

### **Rule:** 153300

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person

  

### **Rule:** 153301

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Given name

Field ID: cdr.disbursement.completingActions.receivers.personDetails.givenName

### **Rule:** 153121

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153122

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153123

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Identification type

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode

### **Rule:** 153360

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person / Identification

  

### **Rule:** 153361

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Birth certificate
- 2=Passport
- 3=Other
- 4=Driver's licence
- 5=Provincial health card
- 14=Citizenship card
- 15=Certificate of Indian Status
- 27=Social Insurance Number card
- 32=Permanent resident card
- 33=Record of landing
- 34=Credit file
- 35=Government issued identification
- 36=Insurance documents
- 37=Provincial or territorial identity card
- 38=Record of employment
- 39=Travel visa
- 40=Utility statement

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeOther

### **Rule:** 153370

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person / Identification

  

### **Rule:** 153371

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person / Identification

  

### **Rule:** 153372

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Person / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 153392

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Passport (2), Driver's licence (4), Provincial health card (5), Citizenship card (14), Certificate of Indian Status (15), Permanent resident card (32), Record of landing (33), Government issued identification (35), Provincial or territorial identity card (37), Travel visa (39).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person / Identification

  

### **Rule:** 153394

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 153400

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person / Identification

  

### **Rule:** 153401

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Driver's licence (4), Provincial health card (5), Government issued identification (35), Provincial or territorial identity card (37) and cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person / Identification

  

### **Rule:** 153404

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Person / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 153410

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person / Identification

  

### **Rule:** 153413

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.completingActions.receivers.personDetails.identifications.number

### **Rule:** 153380

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is not Social Insurance Number card (27).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person / Identification

  

### **Rule:** 153381

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.completingActions.receivers.personDetails.identifications.identifierTypeCode is Social Insurance Number card (27).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Person / Identification

  

### **Rule:** 153383

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person / Identification

  

## Field name: Name of employer

Field ID: cdr.disbursement.completingActions.receivers.personDetails.nameOfEmployer

### **Rule:** 153343

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Occupation

Field ID: cdr.disbursement.completingActions.receivers.personDetails.occupation

### **Rule:** 153332

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153333

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.completingActions.receivers.personDetails.otherNameInitial

### **Rule:** 153143

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Surname

Field ID: cdr.disbursement.completingActions.receivers.personDetails.surname

### **Rule:** 153131

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Person

  

### **Rule:** 153132

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.completingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Person

  

### **Rule:** 153133

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Telephone number

Field ID: cdr.disbursement.completingActions.receivers.personDetails.telephoneNumber

### **Rule:** 153293

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.personDetails.typeCode

### **Rule:** 153110

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.completingActions.receivers.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Person

  

## Field name: Subject type

Field ID: cdr.disbursement.completingActions.receivers.typeCode

### **Rule:** 153100

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 153101

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person details (3), Entity details (4).

**Message:** The value entered for the field does not provide what is required. (301)

  

## Field name: Reporting entity location number

Field ID: cdr.disbursement.reportingEntityLocationId

### **Rule:** 151000

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151001

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 30 characters, containing only alpha and numeric characters.

**Message:** Invalid format. (362)

  

### **Rule:** 151002

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a branch location that is invalid for the reporting entity given the constraint to make sure this branch is valid and is in Canada.

**Message:** FINTRAC does not have this location on file for the reporting entity. (320)

  

## Field name: Starting action list

Field ID: cdr.disbursement.startingActions

### **Rule:** 151060

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 50.

**Message:** The list must be within the specified size. (332)

  

## Field name: Account information type

Field ID: cdr.disbursement.startingActions.details.account.accountTypeCode

### **Rule:** 151125

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account

  

### **Rule:** 154750

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account

  

### **Rule:** 154900

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.accountCategoryCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Non-account based (reference numbers)

  

## Field name: Branch number

Field ID: cdr.disbursement.startingActions.details.account.branchNumber

### **Rule:** 154773

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 50 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Account currency type

Field ID: cdr.disbursement.startingActions.details.account.currencyCode

### **Rule:** 151160

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154810

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 151164

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Casino account

  

### **Rule:** 154814

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Financial institution account

  

## Field name: Date account opened

Field ID: cdr.disbursement.startingActions.details.account.dateOpened

### **Rule:** 151173

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 154823

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

### **Rule:** 151174

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Casino account

  

### **Rule:** 154824

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Financial institution account

  

## Field name: Financial institution number

Field ID: cdr.disbursement.startingActions.details.account.financialInstitutionNumber

### **Rule:** 154763

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 50 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Casino identifier number where the account is held

Field ID: cdr.disbursement.startingActions.details.account.heldAtLocationIdentifier

### **Rule:** 151180

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 151183

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 30 characters, containing only alpha and numeric characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 151184

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a branch location that is invalid for the reporting entity given the constraint to make sure this branch is valid and is in Canada.

**Message:** FINTRAC does not have this location on file for the reporting entity. (320)

**Condition:** Casino account

  

## Field name: Account holder list

Field ID: cdr.disbursement.startingActions.details.account.holders

### **Rule:** 151210

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 3.

**Message:** The list must be within the specified size. (332)

  

### **Rule:** 154820

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Financial institution account

  

## Field name: Name of entity

Field ID: cdr.disbursement.startingActions.details.account.holders.entityName.nameOfEntity

### **Rule:** 151280

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 154890

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Entity

  

### **Rule:** 151283

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 154893

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.details.account.holders.entityName.typeCode

### **Rule:** 151270

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder / Entity

  

### **Rule:** 154880

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.startingActions.details.account.holders.personName.givenName

### **Rule:** 151250

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154860

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Person

  

### **Rule:** 151253

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154863

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.startingActions.details.account.holders.personName.otherNameInitial

### **Rule:** 151263

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154873

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Surname

Field ID: cdr.disbursement.startingActions.details.account.holders.personName.surname

### **Rule:** 151240

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154850

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account / Holder / Person

  

### **Rule:** 151243

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154853

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.details.account.holders.personName.typeCode

### **Rule:** 151230

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder / Person

  

### **Rule:** 154840

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.details.account.holders.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.details.account.holders.typeCode

### **Rule:** 151220

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Casino account / Holder

  

### **Rule:** 154830

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Financial institution account / Holder

  

### **Rule:** 151221

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person name (1), Entity name (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Casino account / Holder

  

### **Rule:** 154831

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person name (1), Entity name (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Financial institution account / Holder

  

## Field name: Account number

Field ID: cdr.disbursement.startingActions.details.account.number

### **Rule:** 151130

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154780

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 151133

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 154783

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Other number related to reference number

Field ID: cdr.disbursement.startingActions.details.account.otherRelatedReferenceNumber

### **Rule:** 154920

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.account.referenceNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Non-account based (reference numbers)

  

### **Rule:** 154923

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Non-account based (reference numbers)

  

## Field name: Reference number

Field ID: cdr.disbursement.startingActions.details.account.referenceNumber

### **Rule:** 154910

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Non-account based (reference numbers)

  

### **Rule:** 154913

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Non-account based (reference numbers)

  

## Field name: Account type

Field ID: cdr.disbursement.startingActions.details.account.typeCode

### **Rule:** 151140

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 154790

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 151141

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 2=Front money
- 3=Other
- 4=Advance on credit
- 5=Safekeeping

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Casino account

  

### **Rule:** 154793

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Personal
- 2=Business
- 3=Trust
- 4=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Financial institution account

  

## Field name: Account type - other

Field ID: cdr.disbursement.startingActions.details.account.typeOther

### **Rule:** 151150

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.account.typeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Casino account

  

### **Rule:** 151152

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.account.typeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Casino account

  

### **Rule:** 154800

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.account.typeCode is Other (4).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Financial institution account

  

### **Rule:** 154801

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.account.typeCode is not Other (4).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Financial institution account

  

### **Rule:** 151153

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Casino account

  

### **Rule:** 154802

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Financial institution account

  

## Field name: Account information type

Field ID: cdr.disbursement.startingActions.details.accountCategoryCode

### **Rule:** 151120

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151121

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Casino account
- 2=Financial institution account
- 3=Non-account based (reference numbers)
- 4=Not applicable

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

### **Rule:** 151122

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not 4 and cdr.disbursement.startingActions.details.account.accountTypeCode is blank or missing.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

## Field name: Amount

Field ID: cdr.disbursement.startingActions.details.amount

### **Rule:** 151092

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.valueInCanadianDollars is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 151093

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.valueInCanadianDollars is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 151094

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided an amount that is not the correct format:
- 17 digits (max), decimal separator and 10 digits (max).
- If a decimal separator is used, one digit before and two decimal places must be provided.

**Message:** Invalid format. (362)

  

### **Rule:** 151095

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if after currency conversion, the Canadian equivalent amount is not less than the reasonable upper limit of $ 1,000,000,000,000.

**Message:** After currency conversion, the Canadian equivalent amount must be less than the reasonable upper limit of $1,000,000,000,000. (341)

  

## Field name: Currency type

Field ID: cdr.disbursement.startingActions.details.currencyCode

### **Rule:** 151100

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.valueInCanadianDollars is blank and cdr.disbursement.startingActions.details.amount is not blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 151105

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Currencies

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Reason of disbursement

Field ID: cdr.disbursement.startingActions.details.reasonTypeCode

### **Rule:** 151073

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 151074

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Redemption - slot tickets
- 2=Redemption - chips or tokens
- 3=Redemption - plaques
- 4=Front cash withdrawal
- 5=Safekeeping withdrawal
- 6=Advance on credit - counter cheque
- 7=Advance on credit - casino credit acct.
- 8=Advance on credit - marker issued
- 10=Payment - bets
- 11=Payment - casino stored value card
- 12=Payment - slot jackpots (not tickets)
- 13=Payment - table jackpot
- 14=Payment - tournament payout
- 15=Payment - draw or prize payout
- 16=Payment - of credit for recipient
- 17=Payment - of credit, other than recip.
- 18=Cash. negotiable instr. - bank draft
- 19=Cash. negotiable instr. - casino cheque
- 20=Cash. negotiable instr. - cheque other
- 21=Cash. negotiable instr. - money order
- 22=Cash. negotiable instr. - travel. cheque
- 23=Reimbursement - entertainment expenses
- 24=Reimbursement - travel expenses
- 26=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

## Field name: Reason of disbursement - other

Field ID: cdr.disbursement.startingActions.details.reasonTypeOther

### **Rule:** 151080

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.reasonTypeCode is Other (26).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 151081

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.reasonTypeCode is not Other (26).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 151082

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

  

## Field name: Value in Canadian dollars

Field ID: cdr.disbursement.startingActions.details.valueInCanadianDollars

### **Rule:** 151110

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.details.amount is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

  

### **Rule:** 151111

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.details.amount is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

  

### **Rule:** 151114

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided an amount that is not the correct format:
- 17 digits (max), decimal separator and 10 digits (max).
- If a decimal separator is used, one digit before and two decimal places must be provided.

**Message:** Invalid format. (362)

  

## Field name: Requester list

Field ID: cdr.disbursement.startingActions.requesters

### **Rule:** 151310

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

  

### **Rule:** 151311

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

  

## Field name: Client number

Field ID: cdr.disbursement.startingActions.requesters.details.clientNumber

### **Rule:** 152743

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: Date/time of online session

Field ID: cdr.disbursement.startingActions.requesters.details.dateTimeOfOnlineSession

### **Rule:** 152813

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the format yyyy-mm-ddThh:mm:ss-zz:zz.

**Message:** Invalid format. (362)

**Condition:** Requester

  

### **Rule:** 152812

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not after 2009-09-28.

**Message:** The date in the field is too far in the past. (308)

**Condition:** Requester

  

### **Rule:** 152814

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before now.

**Message:** The field cannot contain a future date. (304)

**Condition:** Requester

  

## Field name: Device identifier

Field ID: cdr.disbursement.startingActions.requesters.details.deviceIdentifierNumber

### **Rule:** 152793

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: Email address

Field ID: cdr.disbursement.startingActions.requesters.details.emailAddress

### **Rule:** 152753

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that does not adhere to the RFC5322 Internet Message Format or exceeded the maximum length of 200.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: IP address

Field ID: cdr.disbursement.startingActions.requesters.details.internetProtocolAddress

### **Rule:** 152803

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: Was this transaction conducted on behalf of another person or entity?

Field ID: cdr.disbursement.startingActions.requesters.details.onBehalfOfIndicator

### **Rule:** 152820

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester

  

### **Rule:** 152821

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs is empty or the user provided 'false' and cdr.disbursement.startingActions.requesters.onBehalfOfs is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Condition:** Requester

  

## Field name: Device type

Field ID: cdr.disbursement.startingActions.requesters.details.typeOfDeviceCode

### **Rule:** 152772

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.casinoDisbursementDetails.methodTypeCode is not one of Other (7), Online (12).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester

  

### **Rule:** 152773

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Computer/Laptop
- 2=Mobile phone
- 3=Tablet
- 4=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester

  

## Field name: Device type - other

Field ID: cdr.disbursement.startingActions.requesters.details.typeOfDeviceOther

### **Rule:** 152780

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.details.typeOfDeviceCode is Other (4).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester

  

### **Rule:** 152781

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.details.typeOfDeviceCode is not Other (4).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester

  

### **Rule:** 152782

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: User name

Field ID: cdr.disbursement.startingActions.requesters.details.username

### **Rule:** 152763

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester

  

## Field name: House/Building number

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.buildingNumber

### **Rule:** 151690

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151693

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: City

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.city

### **Rule:** 151710

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151711

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151712

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151713

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Country

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode

### **Rule:** 151771

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151772

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151774

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity

  

## Field name: District

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.district

### **Rule:** 151720

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151723

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.postalZipCode

### **Rule:** 151760

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151761

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured is blank and cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151762

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

### **Rule:** 151763

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Requester / Entity

  

## Field name: Province or state code

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.provinceStateCode

### **Rule:** 151730

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151731

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151732

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151733

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151735

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity

  

## Field name: Province or state name

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.provinceStateName

### **Rule:** 151740

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151742

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151743

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Street address

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.streetAddress

### **Rule:** 151700

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151702

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151703

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151704

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.subProvinceSubLocality

### **Rule:** 151750

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151753

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.typeCode

### **Rule:** 151670

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Entity

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.unitNumber

### **Rule:** 151680

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151683

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.address.unstructured

### **Rule:** 151780

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.entityDetails.address.unitNumber, cdr.disbursement.startingActions.requesters.entityDetails.address.buildingNumber, cdr.disbursement.startingActions.requesters.entityDetails.address.streetAddress, cdr.disbursement.startingActions.requesters.entityDetails.address.city, cdr.disbursement.startingActions.requesters.entityDetails.address.district, cdr.disbursement.startingActions.requesters.entityDetails.address.provinceStateCode, cdr.disbursement.startingActions.requesters.entityDetails.address.provinceStateName, cdr.disbursement.startingActions.requesters.entityDetails.address.subProvinceSubLocality, cdr.disbursement.startingActions.requesters.entityDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151782

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is 2.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151783

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151784

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.addressTypeCode

### **Rule:** 151660

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151661

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151662

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Entity

  

## Field name: Authorized person list

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.authorizedPersons

### **Rule:** 151960

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 0 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Requester / Entity

  

### **Rule:** 151961

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 3 and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

**Condition:** Requester / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.authorizedPersons.givenName

### **Rule:** 151972

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Authorized person

  

### **Rule:** 151973

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Authorized person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.authorizedPersons.otherNameInitial

### **Rule:** 151993

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Authorized person

  

## Field name: Surname

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.authorizedPersons.surname

### **Rule:** 151982

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Authorized person

  

### **Rule:** 151983

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Authorized person

  

## Field name: Extension

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.extensionNumber

### **Rule:** 151800

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity

  

### **Rule:** 151801

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Identification list

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications

### **Rule:** 151890

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

**Condition:** Requester / Entity

  

## Field name: Identification type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.identifierTypeCode

### **Rule:** 151900

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151901

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Articles of association
- 2=Certificate of corporate status
- 3=Certificate of incorporation
- 4=Letter/Notice of assessment
- 5=Partnership agreement
- 6=Annual report
- 7=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.identifierTypeOther

### **Rule:** 151910

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.entityDetails.identifications.identifierTypeCode is Other (7).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151911

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.identifications.identifierTypeCode is not Other (7).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151912

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 151932

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151934

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 151940

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151941

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.entityDetails.identifications.identifierTypeCode is one of Certificate of corporate status (2), Certificate of incorporation (3), Letter/Notice of assessment (4) and cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151944

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 151950

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151953

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.identifications.number

### **Rule:** 151922

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value into this field.

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity / Identification

  

### **Rule:** 151923

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Identification

  

## Field name: Name of entity

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.nameOfEntity

### **Rule:** 151650

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151652

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151653

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Nature of entity's principal business

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.natureOfPrincipalBusiness

### **Rule:** 151811

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity

  

### **Rule:** 151812

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Entity

  

### **Rule:** 151813

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Is the entity registered or incorporated?

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationIncorporationIndicator

### **Rule:** 151820

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester / Entity

  

### **Rule:** 151821

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations is empty or the user provided 'false' and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Condition:** Requester / Entity

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode

### **Rule:** 151860

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151861

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151863

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateCode

### **Rule:** 151870

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151871

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151873

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateName

### **Rule:** 151880

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151882

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151883

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Registration or incorporation

  

## Field name: Registration or incorporation number

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.number

### **Rule:** 151850

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151851

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151853

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity / Registration or incorporation

  

## Field name: Registration/incorporation type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.registrationsIncorporations.typeCode

### **Rule:** 151840

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester / Entity / Registration or incorporation

  

### **Rule:** 151841

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Registered
- 2=Incorporated
- 4=Registered and incorporated
- 5=Unknown

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Entity / Registration or incorporation

  

## Field name: Telephone number

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.telephoneNumber

### **Rule:** 151793

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.entityDetails.typeCode

### **Rule:** 151640

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Entity

  

## Field name: Client number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.details.clientNumber

### **Rule:** 152703

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of

  

## Field name: Email address

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.details.emailAddress

### **Rule:** 152713

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that does not adhere to the RFC5322 Internet Message Format or exceeded the maximum length of 200.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of

  

## Field name: Relationship

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.details.relationshipWithRequesterCode

### **Rule:** 152722

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of

  

### **Rule:** 152723

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Accountant
- 2=Agent
- 3=Borrower
- 4=Broker
- 5=Customer
- 6=Employee
- 7=Friend
- 8=Relative
- 9=Other
- 10=Legal counsel
- 11=Employer
- 12=Joint/Secondary owner
- 13=Power of attorney
- 14=Vendor/Supplier

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of

  

## Field name: Relationship - other

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.details.relationshipWithRequesterOther

### **Rule:** 152731

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.details.relationshipWithRequesterCode is Other (9).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of

  

### **Rule:** 152732

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.details.relationshipWithRequesterCode is not Other (9).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of

  

### **Rule:** 152733

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of

  

## Field name: House/Building number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.buildingNumber

### **Rule:** 152390

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152393

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: City

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.city

### **Rule:** 152410

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152412

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152413

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Country

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode

### **Rule:** 152472

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152474

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity

  

## Field name: District

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.district

### **Rule:** 152420

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152423

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.postalZipCode

### **Rule:** 152460

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152461

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured is blank and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152463

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152464

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Province or state code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.provinceStateCode

### **Rule:** 152430

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152432

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152433

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152435

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Province or state name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.provinceStateName

### **Rule:** 152440

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152443

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152444

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Street address

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.streetAddress

### **Rule:** 152400

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152402

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152403

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.subProvinceSubLocality

### **Rule:** 152450

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152453

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.typeCode

### **Rule:** 152370

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unitNumber

### **Rule:** 152380

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152383

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unstructured

### **Rule:** 152480

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152482

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.unitNumber, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.buildingNumber, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.streetAddress, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.city, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.district, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.provinceStateCode, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.provinceStateName, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.subProvinceSubLocality, cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152483

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.addressTypeCode

### **Rule:** 152360

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152362

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Authorized person list

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.authorizedPersons

### **Rule:** 152660

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 0 and 3.

**Message:** The list must be within the specified size. (332)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Given name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.authorizedPersons.givenName

### **Rule:** 152673

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Authorized person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.authorizedPersons.otherNameInitial

### **Rule:** 152693

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Authorized person

  

## Field name: Surname

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.authorizedPersons.surname

### **Rule:** 152683

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Authorized person

  

## Field name: Extension

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.extensionNumber

### **Rule:** 152500

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152501

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Identification type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.identifierTypeCode

### **Rule:** 152600

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152601

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Articles of association
- 2=Certificate of corporate status
- 3=Certificate of incorporation
- 4=Letter/Notice of assessment
- 5=Partnership agreement
- 6=Annual report
- 7=Other

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.identifierTypeOther

### **Rule:** 152610

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.identifierTypeCode is Other (7).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152611

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.identifierTypeCode is not Other (7).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152612

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 152630

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152634

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 152640

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152641

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.identifierTypeCode is one of Certificate of corporate status (2), Certificate of incorporation (3), Letter/Notice of assessment (4) and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152644

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 152650

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152653

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.identifications.number

### **Rule:** 152620

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value into this field.

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / On behalf of / Entity / Identification

  

### **Rule:** 152623

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Identification

  

## Field name: Name of entity

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.nameOfEntity

### **Rule:** 152351

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152353

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Nature of entity's principal business

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.natureOfPrincipalBusiness

### **Rule:** 152512

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152513

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Is the entity registered or incorporated?

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationIncorporationIndicator

### **Rule:** 152520

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester / On behalf of / Entity

  

### **Rule:** 152521

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations is empty or the user provided 'false' and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations is not empty.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode

### **Rule:** 152560

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152561

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152564

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateCode

### **Rule:** 152570

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152571

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152573

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueProvinceStateName

### **Rule:** 152580

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152581

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152583

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

## Field name: Registration or incorporation number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.number

### **Rule:** 152550

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is Unknown (5).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152551

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode is not Unknown (5).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152553

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

## Field name: Registration/incorporation type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.registrationsIncorporations.typeCode

### **Rule:** 152540

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

### **Rule:** 152541

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Registered
- 2=Incorporated
- 4=Registered and incorporated
- 5=Unknown

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Entity / Registration or incorporation

  

## Field name: Telephone number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.telephoneNumber

### **Rule:** 152493

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Entity

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.entityDetails.typeCode

### **Rule:** 152340

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.onBehalfOfs.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Entity

  

## Field name: House/Building number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.buildingNumber

### **Rule:** 152110

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152113

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: City

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.city

### **Rule:** 152130

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152132

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152133

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Country

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode

### **Rule:** 152192

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152194

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person

  

## Field name: District

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.district

### **Rule:** 152140

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152143

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.postalZipCode

### **Rule:** 152180

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152181

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured is blank and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152183

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152184

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Requester / On behalf of / Person

  

## Field name: Province or state code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.provinceStateCode

### **Rule:** 152150

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152151

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152153

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152155

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person

  

## Field name: Province or state name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.provinceStateName

### **Rule:** 152160

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152163

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152164

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Street address

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.streetAddress

### **Rule:** 152120

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152122

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152123

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.subProvinceSubLocality

### **Rule:** 152170

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152173

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.typeCode

### **Rule:** 152090

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Person

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unitNumber

### **Rule:** 152100

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152103

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unstructured

### **Rule:** 152200

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.unitNumber, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.buildingNumber, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.streetAddress, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.city, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.district, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.provinceStateCode, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.provinceStateName, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.subProvinceSubLocality, cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152202

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152203

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.addressTypeCode

### **Rule:** 152080

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152082

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Person

  

## Field name: Alias

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.alias

### **Rule:** 152073

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Country of residence

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.countryOfResidenceCode

### **Rule:** 152244

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person

  

## Field name: Date of birth

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.dateOfBirth

### **Rule:** 152233

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152234

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152235

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not within the last -120 years.

**Message:** The date in the field is too far in the past. (308)

**Condition:** Requester / On behalf of / Person

  

## Field name: Extension

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.extensionNumber

### **Rule:** 152220

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152221

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Given name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.givenName

### **Rule:** 152042

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152043

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Identification type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode

### **Rule:** 152280

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152281

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Birth certificate
- 2=Passport
- 3=Other
- 4=Driver's licence
- 5=Provincial health card
- 14=Citizenship card
- 15=Certificate of Indian Status
- 27=Social Insurance Number card
- 32=Permanent resident card
- 33=Record of landing
- 34=Credit file
- 35=Government issued identification
- 36=Insurance documents
- 37=Provincial or territorial identity card
- 38=Record of employment
- 39=Travel visa
- 40=Utility statement

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeOther

### **Rule:** 152290

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152291

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152292

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 152312

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Passport (2), Driver's licence (4), Provincial health card (5), Citizenship card (14), Certificate of Indian Status (15), Permanent resident card (32), Record of landing (33), Government issued identification (35), Provincial or territorial identity card (37), Travel visa (39).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152314

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 152320

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152321

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Driver's licence (4), Provincial health card (5), Government issued identification (35), Provincial or territorial identity card (37) and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152324

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 152330

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152333

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.number

### **Rule:** 152300

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is not Social Insurance Number card (27).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152301

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.identifications.identifierTypeCode is Social Insurance Number card (27).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / On behalf of / Person / Identification

  

### **Rule:** 152303

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person / Identification

  

## Field name: Name of employer

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.nameOfEmployer

### **Rule:** 152263

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Occupation

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.occupation

### **Rule:** 152252

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152253

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.otherNameInitial

### **Rule:** 152063

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Surname

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.surname

### **Rule:** 152052

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / On behalf of / Person

  

### **Rule:** 152053

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Telephone number

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.telephoneNumber

### **Rule:** 152213

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / On behalf of / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.personDetails.typeCode

### **Rule:** 152030

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.onBehalfOfs.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.onBehalfOfs.typeCode

### **Rule:** 152020

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester / On behalf of

  

### **Rule:** 152021

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person details (3), Entity details (4).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / On behalf of

  

## Field name: House/Building number

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.buildingNumber

### **Rule:** 151410

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151413

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: City

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.city

### **Rule:** 151430

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151431

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151432

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151433

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Country

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.countryCode

### **Rule:** 151491

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151492

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151494

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person

  

## Field name: District

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.district

### **Rule:** 151440

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151443

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Postal or zip code

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.postalZipCode

### **Rule:** 151480

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151481

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.personDetails.address.unstructured is blank and cdr.disbursement.startingActions.requesters.personDetails.address.countryCode is one of Canada (CA), United States (US).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151483

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 20 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

### **Rule:** 151484

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the postal code provided is not a valid Canadian postal code OR if the ZIP code provided is not a valid US ZIP code OR if the postal code provided is not alphanumeric for countries entered in cdr.disbursement.startingActions.requesters.personDetails.address.countryCode other than Canada and the United States.

**Message:** The value entered for this field is not a valid format for a Postal Code / Zip Code. (363)

**Condition:** Requester / Person

  

## Field name: Province or state code

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.provinceStateCode

### **Rule:** 151450

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true' and cdr.disbursement.startingActions.requesters.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151452

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151453

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.address.countryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151451

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.personDetails.address.countryCode is one of Canada (CA), United States (US), Mexico (MX) and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151456

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.personDetails.address.countryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person

  

## Field name: Province or state name

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.provinceStateName

### **Rule:** 151460

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151463

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.address.countryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151464

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Street address

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.streetAddress

### **Rule:** 151420

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is 1.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151421

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151422

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is Structured address (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151423

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Sub-province and/or sub-locality

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.subProvinceSubLocality

### **Rule:** 151470

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151473

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.typeCode

### **Rule:** 151390

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Person

  

## Field name: Apt/Room/Suite/Unit number

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.unitNumber

### **Rule:** 151400

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unstructured are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151403

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Unstructured address details

Field ID: cdr.disbursement.startingActions.requesters.personDetails.address.unstructured

### **Rule:** 151500

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and any of cdr.disbursement.startingActions.requesters.personDetails.address.unitNumber, cdr.disbursement.startingActions.requesters.personDetails.address.buildingNumber, cdr.disbursement.startingActions.requesters.personDetails.address.streetAddress, cdr.disbursement.startingActions.requesters.personDetails.address.city, cdr.disbursement.startingActions.requesters.personDetails.address.district, cdr.disbursement.startingActions.requesters.personDetails.address.provinceStateCode, cdr.disbursement.startingActions.requesters.personDetails.address.provinceStateName, cdr.disbursement.startingActions.requesters.personDetails.address.subProvinceSubLocality, cdr.disbursement.startingActions.requesters.personDetails.address.postalZipCode are not empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151501

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is true and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is 2.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151503

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1) and cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode is Unstructured address (2).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151504

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 500 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Address type

Field ID: cdr.disbursement.startingActions.requesters.personDetails.addressTypeCode

### **Rule:** 151380

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151381

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151382

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Structured address (1), Unstructured address (2).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Person

  

## Field name: Alias

Field ID: cdr.disbursement.startingActions.requesters.personDetails.alias

### **Rule:** 151373

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Country of residence

Field ID: cdr.disbursement.startingActions.requesters.personDetails.countryOfResidenceCode

### **Rule:** 151544

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person

  

## Field name: Date of birth

Field ID: cdr.disbursement.startingActions.requesters.personDetails.dateOfBirth

### **Rule:** 151532

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151537

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151533

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the following format: yyyy-MM-dd.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

### **Rule:** 151534

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before today.

**Message:** The field cannot contain a future date. (304)

**Condition:** Requester / Person

  

### **Rule:** 151535

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not within the last -120 years.

**Message:** The date in the field is too far in the past. (308)

**Condition:** Requester / Person

  

## Field name: Extension

Field ID: cdr.disbursement.startingActions.requesters.personDetails.extensionNumber

### **Rule:** 151520

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.telephoneNumber is empty.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person

  

### **Rule:** 151521

**Rule type:** Format

**Action:** Warning

**Description:** Send a warning if the user provided a value that does not contain up to 10 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Given name

Field ID: cdr.disbursement.startingActions.requesters.personDetails.givenName

### **Rule:** 151341

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151342

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151343

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Identification list

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications

### **Rule:** 151570

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and \* and if cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** The list cannot be empty, but is required based on the value entered elsewhere in the report. (331)

**Condition:** Requester / Person

  

## Field name: Identification type

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode

### **Rule:** 151580

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151581

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=Birth certificate
- 2=Passport
- 3=Other
- 4=Driver's licence
- 5=Provincial health card
- 14=Citizenship card
- 15=Certificate of Indian Status
- 27=Social Insurance Number card
- 32=Permanent resident card
- 33=Record of landing
- 34=Credit file
- 35=Government issued identification
- 36=Insurance documents
- 37=Provincial or territorial identity card
- 38=Record of employment
- 39=Travel visa
- 40=Utility statement

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person / Identification

  

## Field name: Identification type - other

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeOther

### **Rule:** 151590

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is Other (3).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151591

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is not Other (3).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151592

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person / Identification

  

## Field name: Jurisdiction of issue (country)

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueCountryCode

### **Rule:** 151612

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Passport (2), Driver's licence (4), Provincial health card (5), Citizenship card (14), Certificate of Indian Status (15), Permanent resident card (32), Record of landing (33), Government issued identification (35), Provincial or territorial identity card (37), Travel visa (39).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151614

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- All ISO Countries

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) code

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueProvinceStateCode

### **Rule:** 151620

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueCountryCode is not in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151621

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is one of Birth certificate (1), Driver's licence (4), Provincial health card (5), Government issued identification (35), Provincial or territorial identity card (37) and cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueCountryCode is one of Canada (CA), United States (US), Mexico (MX).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151623

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the province/state code does not correspond with the country provided OR is not a valid Canadian, US or Mexican province/state code given the country cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueCountryCode.

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Condition:** Requester / Person / Identification

  

## Field name: Jurisdiction of issue (province or state) name

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueProvinceStateName

### **Rule:** 151630

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.jurisdictionOfIssueCountryCode is in CA, US, MX.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151633

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person / Identification

  

## Field name: Number associated with identifier type

Field ID: cdr.disbursement.startingActions.requesters.personDetails.identifications.number

### **Rule:** 151601

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is not Social Insurance Number card (27).

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151602

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.disbursement.startingActions.requesters.personDetails.identifications.identifierTypeCode is Social Insurance Number card (27).

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Condition:** Requester / Person / Identification

  

### **Rule:** 151603

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person / Identification

  

## Field name: Name of employer

Field ID: cdr.disbursement.startingActions.requesters.personDetails.nameOfEmployer

### **Rule:** 151563

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Occupation

Field ID: cdr.disbursement.startingActions.requesters.personDetails.occupation

### **Rule:** 151551

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151552

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151553

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 200 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Other name/initial

Field ID: cdr.disbursement.startingActions.requesters.personDetails.otherNameInitial

### **Rule:** 151363

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Surname

Field ID: cdr.disbursement.startingActions.requesters.personDetails.surname

### **Rule:** 151351

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'true'.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Condition:** Requester / Person

  

### **Rule:** 151352

**Rule type:** Presence

**Action:** Warning

**Description:** Send a warning if the user did not provide a value and cdr.disbursement.casinoDisbursementDetails.thresholdIndicator is 'false' and cdr.disbursement.startingActions.details.accountCategoryCode is Casino account (1).

**Message:** This field was not completed, but may be required based on the value entered elsewhere in the report. (375)

**Condition:** Requester / Person

  

### **Rule:** 151353

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 100 characters.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Telephone number

Field ID: cdr.disbursement.startingActions.requesters.personDetails.telephoneNumber

### **Rule:** 151513

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a value that did not contain 0 to 20 numbers, dashes, commas, periods, spaces or round brackets.

**Message:** Invalid format. (362)

**Condition:** Requester / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.personDetails.typeCode

### **Rule:** 151330

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the value the user provided is not equal to the value in cdr.disbursement.startingActions.requesters.typeCode.

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester / Person

  

## Field name: Subject type

Field ID: cdr.disbursement.startingActions.requesters.typeCode

### **Rule:** 151320

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

**Condition:** Requester

  

### **Rule:** 151321

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not one of Person details (3), Entity details (4).

**Message:** The value entered for the field does not provide what is required. (301)

**Condition:** Requester

  

## Field name: Disbursement

Field ID: cdr.disbursements

### **Rule:** 150070

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a disbursement reference number which is not unique for this report.

**Message:** The number must be unique for the report. (336)

  

### **Rule:** 150072

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list is empty.

**Message:** The list must be within the specified size. (332)

  

### **Rule:** 150075

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the list of values is not between 1 and 5000.

**Message:** The list must be within the specified size. (332)

  

### **Rule:** 150071

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the total amount of the report is less than $ 10000 CAD. Disbursements containing foreign currency will have a $ 1000 CAD buffer (above and below) applied to the threshold calculation.

**Message:** The total amount of the report is under the reporting threshold. (334)

  

## Field name: Ministerial directive

Field ID: cdr.reportDetails.ministerialDirectiveCode

### **Rule:** 150080

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that is not between 1 and 10 characters.

**Message:** Invalid format. (362)

**Rule note:** Added June 23, 2026

  

### **Rule:** 150081

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 1=IR2020

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

**Rule note:** Added June 23, 2026

  

### **Rule:** 150082

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value and there is more than one transaction or the criteria of the particular Ministerial Directive are not met.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Rule note:** Added June 23, 2026

  

### **Rule:** 150084

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the user provided a value and the transaction is above threshold.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Rule note:** Added June 23, 2026

  

## Field name: Contact identifier

Field ID: cdr.reportDetails.reportingEntityContactId

### **Rule:** 150060

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 150061

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not between 0 and 9999999.

**Message:** Invalid format. (362)

  

### **Rule:** 150062

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a contact number that is invalid for the reporting entity.

**Message:** FINTRAC does not have this contact on file for the reporting entity. (324)

  

## Field name: Reporting entity number

Field ID: cdr.reportDetails.reportingEntityNumber

### **Rule:** 150000

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 150001

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not between 0 and 9999999.

**Message:** Invalid format. (362)

  

## Field name: Reporting entity report reference

Field ID: cdr.reportDetails.reportingEntityReportReference

### **Rule:** 150020

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 150021

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided text that did not contain only alpha character, numbers, dashes or underscores up to 100 characters.

**Message:** Invalid format. (362)

  

### **Rule:** 150022

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a report reference number which is not unique for this RE.

**Message:** The number must be unique for the reporting entity. (997)

  

## Field name: Submitting reporting entity number

Field ID: cdr.reportDetails.submittingReportingEntityNumber

### **Rule:** 150010

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 150011

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value that is not between 0 and 9999999.

**Message:** Invalid format. (362)

  

## Field name: Aggregation type

Field ID: cdr.reportDetails.twentyFourHourRule.aggregationTypeCode

### **Rule:** 150030

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value into this field.

**Message:** Field is mandatory. (329)

  

### **Rule:** 150032

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a value not in the list:
- 4=Not applicable
- 6=Received by
- 7=Received on behalf of
- 8=Requested by
- 9=Requested on behalf of

**Message:** The value entered is not in FINTRAC's list of values for the field. (300)

  

### **Rule:** 150033

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided aggregation type Received by, Received on behalf of, Requested by, or Requested on behalf of and Ministerial Directive was chosen. Reject this report if the user provided aggregation type 4-Not applicable and there was either no single above threshold transaction provided or Ministerial Directive was not chosen.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

**Rule note:** Changed June 23, 2026

  

### **Rule:** 150034

**Rule type:** Content

**Action:** Warning

**Description:** Send a warning if the user provided aggregation type Received by, Received on behalf of, Requested by, or Requested on behalf of and there was a single above threshold transaction provided.

**Message:** The value entered for this field is inaccurate, based on the value shown in one or more other fields. (302)

  

## Field name: End of period

Field ID: cdr.reportDetails.twentyFourHourRule.periodEnd

### **Rule:** 150050

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.reportDetails.ministerialDirectiveCode is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Rule note:** Changed June 23, 2026

  

### **Rule:** 150051

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.reportDetails.ministerialDirectiveCode is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Rule note:** Added June 23, 2026

  

### **Rule:** 150052

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the format yyyy-mm-ddThh:mm:ss-zz:zz.

**Message:** Invalid format. (362)

  

### **Rule:** 150053

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not 24 hours from cdr.reportDetails.twentyFourHourRule.periodStart.

**Message:** The value entered for the field does not provide what is required. (301)

  

### **Rule:** 150054

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before now.

**Message:** The field cannot contain a future date. (304)

  

## Field name: Start of period

Field ID: cdr.reportDetails.twentyFourHourRule.periodStart

### **Rule:** 150040

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user did not provide a value and cdr.reportDetails.ministerialDirectiveCode is blank.

**Message:** This field was not completed, but is required based on the value entered elsewhere in the report. (330)

**Rule note:** Changed June 23, 2026

  

### **Rule:** 150041

**Rule type:** Presence

**Action:** Reject

**Description:** Reject this report if the user provided a value and cdr.reportDetails.ministerialDirectiveCode is not blank.

**Message:** This field is not required based on the value shown in one or more other fields. (364)

**Rule note:** Added June 23, 2026

  

### **Rule:** 150042

**Rule type:** Format

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not in the format yyyy-mm-ddThh:mm:ss-zz:zz.

**Message:** Invalid format. (362)

  

### **Rule:** 150043

**Rule type:** Content

**Action:** Reject

**Description:** Reject this report if the user provided a date that is not before now.

**Message:** The field cannot contain a future date. (304)

  
  

Date Modified:
:   2026-06-23