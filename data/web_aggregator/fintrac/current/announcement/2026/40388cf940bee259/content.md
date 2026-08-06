# Guidance on Tag: 50

## Guidance on Tag :50: (Ordering Customer) of the SWIFT Electronic Funds Transfer Report

As per paragraphs 12(1)(b) and 12(1)(c) of the *Proceeds of Crime (Money Laundering) and Terrorist Financing (PCMLTF) Regulations*, financial entities are required to report the sending out of Canada and the receipt from outside Canada, at the request of a client, of an electronic funds transfer (EFT) of $10,000 or more in the course of a single transaction. This report must contain, among other things, the following information on the client ordering the payment of the EFT (i.e., tag :50:) referred to in Schedules 2 and 3 of the *PCMLTF Regulations*:

1. Client's full name;
2. Client's full address;
3. Client's account number, if applicable.

Although the Society for Worldwide Interbank Financial Telecommunication (SWIFT) allows its members to choose between three options to fill out tag :50:, i.e., options A, F and K, only options F and K do provide the information that is mandatory for these reports.

Given option F can also contain information that is not set out in Schedules 2 and 3, if your financial entity sends out or receives a MT 103 message in which option F was used, we recommend that you follow these guidelines when providing information to FINTRAC:

1. **When subfield 1 (Party Identifier) is used with the (Code)(Identifier) format, you should provide one of the following codes followed by the "/" character:**

   ARNU
   :   Alien Registration Number

   CCPT
   :   Passport Number

   CUST
   :   Customer Identification Number

   DRLC
   :   Driver's License Number

   EMPL
   :   Employer Number

   IBEI
   :   International Business Entity Identifier (no country code allowed)

   NIDN
   :   National Identity Number

   SOSE
   :   Social Security Number

   TXID
   :   Tax Identification Number

   CORP
   :   Corporate Identification, that is, Identification Number of the Customer in a Corporation:

   OTHR
   :   Other identification

   However, **DO NOT** provide the values that follow the "/"" character. Please space-fill the remainder of the tag.
2. **For subfield 2 (Name & Address), you should only provide the following codes on the lines:**

   * **Name of the ordering customer**

     The number followed by a slash, '/' must be followed by the name of the ordering customer (where it is recommended that the surname precedes given name(s)).
   * **Address Line**

     The number followed by a slash, '/' must be followed by an Address Line (Address Line can be used to provide for example, street name and number, or building name).
   * **Country and Town**

     The number followed by a slash, '/' must be followed by the ISO country code, a slash '/' and Town (Town can be complemented by postal code (for example zip), country subdivision (for example state, province, or county).

   **DO NOT** provide other codes such as:

   * **Date of Birth**

     The number followed by a slash, '/' must be followed by the Date of Birth in the YYYYMMDD format.
   * **Place of Birth**

     The number followed by a slash, '/' must be followed by the ISO country code, a slash '/' and the Place of Birth.
   * **Customer Identification Number**

     The number followed by a slash, '/' must be followed by the ISO country code, a slash, '/', the issuer of the number, a slash, '/' and the Customer Identification Number.
   * **National Identity Number**

     The number followed by a slash, '/' must be followed by the ISO country code, a slash, '/' and the National Identity Number.
   * **Additional Information**

     The number followed by a slash, '/' is followed by information completing the Identifier provided in subfield 1 (Party Identifier) used with the (Code)(Identifier) format.

#### Example 1 - Alien Registration Number

If you receive the following SWIFT message:

`:50F:ARNU/XR123414  
1/JOHN SMITH  
2/123 MAIN STREET  
4/19640829  
5/DE/FRANKFURT` 

You should provide the aforementioned message to FINTRAC in the following format:

`:50K:ARNU/  
1/JOHN SMITH  
2/123 MAIN STREET`

#### Example 2 - Passport

If you receive the following SWIFT message:

`:50F:CCPT/GB/123456789012345  
1/JOHN SMITH  
2/123 MAIN STREET  
3/GB/LIVERPOOL` 

You should provide the aforementioned message to FINTRAC in the following format:

`:50K:CCPT/  
1/JOHN SMITH  
2/123 MAIN STREET  
3/GB/LIVERPOOL`

#### Example 3 - National Identifier

If you receive the following SWIFT message:

`:50F:NIDN/SE/1234567890124567  
1/JOHN SMITH  
2/123 MAIN STREET  
7/SE/1234567890124567`

You should provide the aforementioned message to FINTRAC in the following format:

`:50K:NIDN/  
1/JOHN SMITH  
2/123 MAIN STREET`

Date Modified:
:   2022-03-12