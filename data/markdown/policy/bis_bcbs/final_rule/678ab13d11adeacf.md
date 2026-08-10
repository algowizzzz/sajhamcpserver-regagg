---
title: "d604"
regulator: "bis_bcbs"
doc_type: "final_rule"
status: "final"
source_kind: "policy_pdf"
source_url: "https://www.bis.org/bcbs/publ/d604.pdf"
published: "2025-12-05"
version: "1"
---

Basel Committee 
on Banking Supervision 
  
 
 
 
Consultative Document 
Machine-readable 
Pillar 3 disclosure 
Issued for comment by 5 March 2026. 
 
December 2025

This publication is available on the BIS website (www.bis.org). 
 
 
© Bank for International Settlements 2025. All rights reserved. Brief excerpts may be reproduced or 
translated provided the source is stated. 
 
 
 
ISBN 978-92-9259-913-3 (online)

Machine-readable Pillar 3 disclosure iii 
 
 
Contents 
1. Introduction and background ............................................................................................................................................. 1 
2. Disclosure access points ........................................................................................................................................................ 2 
3. Scope ............................................................................................................................................................................................ 4 
3.1 Qualitative disclosure .................................................................................................................................................... 4 
3.2 Quantitative and mixed disclosure .......................................................................................................................... 4 
3.3 General requirements .................................................................................................................................................... 5 
4. Technical standards ................................................................................................................................................................. 5 
4.1 Data formats and data exchange standards ........................................................................................................ 5 
4.2 Taxonomies ....................................................................................................................................................................... 7 
4.3 API URL paths ................................................................................................................................................................... 7 
5. Data assurance ........................................................................................................................................................................ 13 
6. Information to be provided on the BCBS’s website ................................................................................................. 14 
6.1 Minimum information required .............................................................................................................................. 14 
6.2 Global database and visualisation .......................................................................................................................... 17 
7. Implementation ...................................................................................................................................................................... 18 
7.1 Implementation of machine-readable Pillar 3 disclosure ............................................................................. 18 
7.2 Possible phase-out of document-based Pillar 3 disclosure ......................................................................... 19 
7.3 Overview of project phases....................................................................................................................................... 19 
8. Consultation questions ........................................................................................................................................................ 19 
Annex 1: Proposed edits to the Basel Framework .............................................................................................................. 21 
Amendments to DIS10 ......................................................................................................................................................... 21 
New DIS11 – Standard for the technical format for machine-readable disclosure ..................................... 22 
Amendments to DIS20 to capture metadata .............................................................................................................. 28 
General changes to existing disclosure standards .................................................................................................... 30 
New DIS90 – Transitional arrangements....................................................................................................................... 30 
Annex 2: Templates in scope for machine-readable Pillar 3 disclosure .................................................................... 31 
Annex 3: Examples of various data formats and data exchange standards ............................................................. 36 
Annex 4: Taxonomy and mapping examples ....................................................................................................................... 42 
DIS templates, data structure definition (DSD) and related IDs .......................................................................... 42 
BCBS taxonomy, field IDs and mapping to IDs in member jurisdictions ......................................................... 47

Machine-readable Pillar 3 disclosure 1 
 
 
Machine-readable Pillar 3 disclosure 
1. Introduction and background 
Availability to market participants of information about common key risk metrics is a fundamental tenet 
of a sound banking system. Pillar 3 disclosures by internationally active banks under the Basel Committee 
on Banking Supervision ’s (BCBS) standards are an important source of such information. Banks’ Pillar  3 
disclosures reduce information asymmetry and help promote comparability  of banks’ risk profiles within 
and across jurisdictions. 1 The disclosure requirements enable market participants to access key 
information relating to a bank’s regulatory capital, liquidity parameters and other risk exposures, which in 
turn help s increase transparency about a bank’s affairs and reinforce s market participants’ confidence 
therein. While data in any format can be processed, availability of machine-readable data – defined as data 
in a format that can be easily processed by a computer without human intervention while ensuring no 
semantic meaning is lost
2 – enhances the speed and ease of data processing. It also provides scalability 
and flexibility to data users. Thus, availability of Pillar  3 disclosures  in machine-readable standardised 
formats is important for strengthening market discipline and efficiency. The BCBS believes that the 
usefulness of Pillar 3 disclosures would be improved by a requirement across all BCBS member jurisdictions 
that they be provided in a machine-readable format either by banks directly and/or via a central repository 
at the national or regional level that is approved by the supervisor for all banks in a jurisdiction. Making 
disclosure data more easily accessible would provide a valuable public good.  
In view of the foregoing, the BCBS is proposing to move towards Pillar  3 disclosures in 
machine-readable standardised formats across its member jurisdictions. The proposed standard would 
introduce a requirement and technical specifications to produce machine -readable quantitative Pillar  3 
disclosures, without changing the material disclosure requirem ents for banks. However, the proposed 
standard would require additional technical templates for furnishing metadata such as the identity of the 
bank, the reporting currency and unit that were previously included in the qualitative part of the Pillar  3 
disclosure report  in a formal way, a s well as  a uniform resource locator (URL) of the human- readable 
disclosure report(s). B anks publish ing Pillar 3 disclosures on their own website s would be required to 
provide their supervisor with the base URL of the webpage hosting the disclosure data. In jurisdictions 
where the supervisor opts for Pillar  3 disclosure via a centralised repository, the proposed changes and 
additions to the standard would be applicable to the centralised repository rather th an to banks. 
It is also envisaged that the proposed standard would not increase  the burden on banks in 
jurisdictions where machine-readable Pillar 3 disclosures are already required. Rather, existing approaches 
would be integrated into the proposed global standard. 
In the following sections of this consultative document, the proposed concept is explained in 
more detail, while Annex 1 presents the amendments to existing disclosure standards and a new standard 
for machine-readable disclosure. The BCBS welcomes comments from stakeholders on all aspects of the 
proposed amendments to the Pillar  3 disclosure standard. Comments should be submitted b y 5 March 
2026 using the following link: www.bis.org/bcbs/commentupload.htm. All comments will be published on 
the Bank for International Settlements ’ website unless a respondent specifically requests confidential 
treatment. 
 
1  See DIS10.1 of the Basel Framework. 
2  See the definition of “machine-readable” in 44 US Code §3502(18), available at www.law.cornell.edu/uscode/text/44/3502.

2 Machine-readable Pillar 3 disclosure 
 
 
2. Disclosure access points 
Supervisory authorities that already require machine -readable Pillar 3 disclosures currently take varying 
approaches regarding the placement of this information. In some cases, Pillar  3 disclosures are provided 
on the reporting banks’ websites themselves (decentralised approach),3 and the supervisor may provide a 
repository of URLs of these websites.4 In other cases, supervisors may collect Pillar 3 disclosure information 
from banks and republish it in a centralised repository (centralised approach).5 Graph 1 illustrates the two 
approaches.  
Decentralised versus centralised approach to publication of Pillar 3 information Graph 1 
Decentralised approach 
 
Centralised approach 
     
 
 
 
Dashed arrow: provision of URLs by banks; solid arrow: data push by banks or pull by data users. 
Under the decentralised approach, banks publish machine -readable Pillar 3 disclosures on their 
own websites, as is currently the case for PDF disclosure documents. Under the proposed standard, with a 
view to allowing automatic retrieval of the machine -readable disclosures, such banks would have to 
provide the base URLs of their Pillar 3 disclosure websites to their supervisor. 6 The supervisor would in 
turn need to maintain a machine-readable list of bank names, Legal Entity Identifiers (LEIs)7 or other unique 
national identifiers where banks do not have LEIs, and the base URLs of the Pillar 3 disclosure websites of 
the banks in its jurisdiction. These base URLs would point to the application programming interface (API) 
 
3  See for example Australian Prudential Regulation Authority and Central Bank of Brazil. 
4  See for example Central Bank of Brazil. 
5  For example, the European Banking Authority, the Swiss Financial Market Supervisory Authority (FINMA) and the US authorities 
have different scopes and processes for collecting various aspects of Pillar 3 information. The disclosure data may be collected 
directly from banks or from regulatory reporting where this corresponds to some of the Pillar  3 disclosure data points. 
Additionally, some jurisdictions may publish some of these data. 
6  While providing a  base URL of the machine -readable Pillar 3 disclosure at the top consolidated level would be mandatory 
under the proposed standard in line with DIS10.2, national supervisors could allow or require banks to provide them with the 
base URLs of Pillar 3 disclosures for more than one legal entity or at different levels of consolidation. 
7  See www.gleif.org/en/organizational-identity/introducing-the-legal-entity-identifier-lei. 
Data at banks 
List of URLs at 
supervisor 
Data users 
Data at banks 
Database at 
supervisor 
Data users

Machine-readable Pillar 3 disclosure 3 
 
 
for an entity’s disclosure rather than the disclosure for a particular reporting date,8 so updates would only 
be required on an infrequent basis if the structure of a bank’s website changed. 
Both banks’ disclosure websites and  supervisory repositories would be required to provide the 
Pillar 3 disclosures in one of the specific machine -readable formats that would be defined by the BCBS 
under the proposed standard. I n addition, banks and supervisors would be free to provide the same 
information in other formats, for example in a more human-readable way, as they deemed appropriate. 
Under the current centralised approach, banks submit Pillar  3 disclosure information to a 
centralised repository at the national or regional level that is approved by the supervisor for all banks in 
that jurisdiction.9 The repositories are either operated by the supervisory authority or another (usually 
public sector) authority. Under the proposed standards, data retrieval from such centralised repositories 
should be possible in at least one of the formats specified by the BCBS. 
Advantages of decentralised and centralised publication 
under the proposed standards Table 1 
Decentralised publication Centralised publication 
• The supervisory community continues to rely on the 
publication of disclosure information by banks 
instead of spending resources on collecting and 
disseminating data. 
• Updates can be posted by banks, which means data 
updates are available for consumption almost 
immediately. 
• Disclosure information is more accessible for data 
users, in particular non-professional data users. 
• There is a lower risk of URLs becoming outdated or 
system outages. 
• This is favourable to smaller banks, which do not 
have to set up their own machine-readable websites. 
The BCBS believes that, at this stage, it is neither feasible nor necessary to require changes to the 
access points for publication in jurisdictions that already have a machine -readable Pillar  3 disclosure 
requirement in place. Therefore, supervisors in member jurisdictions should have national discretion to 
adopt one of the above approaches for the banks in their jurisdictions. To reduce the burden on data 
users, the chosen approach should apply equally to all banks in a jurisdiction that are subject to the BCBS’s 
disclosure standards (ie all internationally active banks). 
The proposed standards would require, among other things, the adoption of a standardised data 
format and taxonomy10 by all jurisdictions to ensure standardisation in banks’ reporting of key parameters. 
However, such standardisation of data formats and taxonomies to be used for machine -readable Pillar 3 
disclosures would only be mandatory for owners of the disclosure access points, ie banks under the 
decentralised approach and the operators of the centralised database under the centralised approach. The 
standardised formats and taxonomies would not  be mandatory for the exchange of data between banks 
and the operators of the centralised database under the centralised approach. For this purpose, operators 
may use the formats and taxonomies proposed by the BCBS and just pass through the information they 
receive from banks. Alternatively, they could consider using other data exchange formats and taxonomies, 
for example those that are currently used for regulatory reporting in their jurisdiction. 
 
8  For example, https://example.com/documents/regulatory -disclosure/v1 rather than https://example.com/ documents/
regulatory-disclosure/v1/2025-06-30/example.pdf. 
9  While providing Pillar 3 disclosure data at the top consolidated level would be mandatory under the proposed standard in line 
with DIS10.2, national supervisors could allow or require banks to provide Pillar 3 disclosure data for other legal entities or at 
different levels of consolidation. 
10  A data taxonomy is a structured way o f naming data elements and organis ing and classify ing them into categories and 
subcategories, often forming a hierarchical structure. It groups related data elements based on shared characteristics and 
relationships.

4 Machine-readable Pillar 3 disclosure 
 
 
3. Scope 
The current DIS standard includes 82 templates: 15 for qualitative information only and 67 for quantitative 
data or a mix of both (often with accompanying narratives explaining the figures). Within these templates, 
the BCBS identified three types of qualitative information that are part of the current disclosure 
requirements: (i) actual qualitative disclosure requirements , as for example in DIS35 template REMA – 
Remuneration policy; (ii) technical footnotes alongside quantitative data; and (iii) accompanying narratives 
as described in the disclosure standard.  
3.1 Qualitative disclosure 
The BCBS proposes not to introduce a mandatory requirement for structured machine-readable disclosure 
of qualitative information in this consultation. Feedback from initial stakeholder outreach events suggests 
that the provision of qualitative information in a structured format is more cumbersome for data providers. 
At the same time, the additional value for data users seems to be limited as the tools they currently use 
for text analysis would benefit only marginally from additional structural information within a document.  
To ensure that automated tools can be used efficiently to analyse qualitative disclosure, the BCBS 
proposes to clarify that all required human-readable Pillar 3 disclosures should be provided in PDF format 
and in a way that allows for the search for and extraction of words contained in the document by a 
machine. At the same time, the document must be human -readable. The document must not contain 
textual information in picture format , such as in a scanned document, and it must not be 
password-protected. Human- readable Pillar  3 disclosures could also be publish ed in one or more 
additional formats on a voluntary basis, provided the content is consistent. The BCBS believes that these 
requirements are in line with current practice in most banks, and it should be possible for banks to comply 
with them with minimal effort where these requirements are not yet met. 
Under the proposed standards, banks would, as part of the quantitative machine -readable 
disclosures, only be required to provide a URL of the full PDF disclosure document including qualitative 
disclosure information, or a list of several URLs of such docum ents if applicable. Aside from that, the 
minimum requirements for the full Pillar  3 reports would remain as they currently are. T here would also 
be an option for banks to directly include qualitative information in the quantitative machine -readable 
disclosure format in the form of footnotes to individual data items, columns, rows or tables. T his ensures 
that banks can keep their current approach where such an option already exists under their extant 
jurisdictional requirements.
11 
The BCBS would not require multilingual disclosures or disclosures in a specific language. 
However, any formats proposed in this document have been specified such that multilingual qualitative 
disclosure is supported where banks choose to provide it or are required  to do so by their national 
supervisor. 
Please refer to Annex 1 for the proposed amendments to DIS10 of the Basel Framework.  
3.2 Quantitative and mixed disclosure 
The BCBS believes that, in principle, all quantitative disclosure templates should be subject to the proposed 
standard for machine-readable Pillar 3 disclosures. Annex 2 summarises the specific templates proposed 
for inclusion. Under the proposed revision, at least 60 of the 67 templates for quantitative data or a mix of 
qualitative and quantitative data should be provided in a machine -readable format, covering 73 % of all 
 
11  To the BCBS’s knowledge, this is currently the case only in Brazil.

Machine-readable Pillar 3 disclosure 5 
 
 
current disclosure requirements. For the seven templates for which the standard does not currently 
prescribe an explicit form for the quantitative information, the BCBS asks for feedback on whether 
disclosing this information in a machine-readable form adds significant value. 
3.3 General requirements 
Access to all human-readable and machine-readable disclosure data must be provided to the public free 
of charge and without authentication12 either on banks’ websites or in a centralised repository designated 
by a bank’s supervisor for all banks in its jurisdiction. There must be no restrictions on copying, publishing, 
distributing, transmitting, processing, citing or adapting these data, in particular in other commercial or 
non-commercial repositories, aside from a requirement to provide a reference to the original source of 
the data. 
4. Technical standards 
4.1 Data formats and data exchange standards 
To make it easier for data users to access Pillar  3 disclosure data, the data would have to be provided at 
the data access points in at least one of the formats specified by the BCBS . This section explains the 
proposed data formats and data exchange standards for machine-readable Pillar 3 disclosure. 
Data formats, such as character -separated values ( CSV) and JavaScript Object Notation (JSON ), 
are primarily used to organise and store data in a structured way. These formats are simple and flexible 
but typically lack built -in validation mechanisms, which means they do not ensure data integrity or 
contextual meaning. In contrast,  data exchange standards , like eXtensible Business Reporting 
Language (XBRL), Statistical Data and Metadata eXchange (SDMX) and JSON Schema, go beyond structure 
by emphasising what the data represent. These standards include validation rules and are designed to 
ensure consistent interpretation . In the case of Pillar  3 disclosure, this helps ensur e consistency across 
different jurisdictions and banks. For example, while a CSV file might list numbers without context, XBRL 
ensures those numbers are understood as specific financial metrics like risk-weighted assets (RWA). 
JSON is a lightweight data format which is easy for humans to read and write. It is simple for 
machines to parse and generate and it is widely adopted by the industry.
13 A CSV file is  a plain text file 
format used to store tabular data. This data format separates data fields using one or more specific 
characters (eg comma, semicolon or tab).
14 CSV files usually use the file extension “ *.csv” and are 
commonly referred to as “flat files” due to their simplistic structure. For the purposes of the proposed DIS 
standard, CSV files should comply with RFC 4180 (ie in particular use the comma as a field separator) and 
use the decimal point to separate the integer and fraction parts of a number.  
Even though data in JSON and CSV formats can be processed by computers, features such as 
structural validation and interoperability across banks and jurisdictions require the use of specific 
standards.
  
XBRL is an open source global standard which is widely adopted by the industry and within the 
supervisory community. It allows users who adopt it as a specification to enhance the creation, exchange 
 
12  This means that in order to get access to the disclosure data users must not be required to log in or prove their identity. 
13  See definition in ISO/IEC 21778:2017 and at www.json.org/json-en.html. 
14  The specification for files using commas as field separators is provided in RFC 4180; see datatracker.ietf.org/doc/html/rfc4180.

6 Machine-readable Pillar 3 disclosure 
 
 
and comparison of business reporting information.15 XBRL is like a single, universal alphabet and grammar 
for digital reporting and acts as a validation layer for the technical structure (not content) of JSON and 
CSV files.  
Another standard which could be useful in th is context is SDMX .16 It is designed to describe 
statistical data and metadata, normalise their exchange and improve their efficient sharing across statistical 
and similar organisations.  
A third – and the simplest –  option is JSON Schema, which is an open standard used to define 
the structure and validation rules of JSON data. It enables developers and data providers to formally 
describe the expected format, types and constraints of JSON documents, facilitating automated validation 
and interoperability across systems. JSON Schema acts as a blueprint for JSON files, ensuring that data 
exchanged through APIs
17 or other channels adhere to a consistent and predictable structure.  
Table 2 summarises the key differences between the concepts of data formats and data exchange 
standards. 
Key differences between data formats and data exchange standards Table 2 
Aspect Data formats (CSV/JSON) Data exchange standards (XBRL/SDMX/JSON 
Schema) 
Purpose Organise and store data in a 
structured way 
Ensure consistency, structural validation and context 
Role Focus on the “how” (how data are 
stored) 
Focus on the “what and why” (what the data mean 
and how they are interpreted) 
Validation Have no built-in validation Include rules to check data integrity 
Cross-bank/cross-
jurisdictional use 
Limited, as interpretation varies Designed to ensure consistent interpretation across 
banks and regions 
Example A CSV file listing numbers without 
context 
XBRL ensures those numbers represent disclosure 
metrics like RWA 
Initially, the BCBS would require disclosure in JSON Schema, SDMX-CSV, XBRL-JSON or XBRL-
CSV format. Ideally, supervisors should make one of these options mandatory in their jurisdiction in order 
to reduce the burden on data users. Data could also be disclosed in one or more additional formats  on a 
voluntary basis, provided the data are consistent. The BCBS acknowledges that the technical formats and 
standards for data disclosure are subject to change . Therefore, it  will periodically consult with its 
stakeholders on whether they feel there is a need t o provid e any additional options for formats and 
standards or phas e out extant formats  and standards . This approach ensure s that the formats and 
standards are periodically updated, without burdening  data users with supporting more than a small 
number of different formats and standards for a given reporting date. 
Please refer to Annex 1 for the proposed edits to the Basel Framework regarding the introduction 
of a new DIS11 standard for the technical details for quantitative information. Annex 3 compares various 
combinations of data formats and standards for a small part of the KM1 template, using an exemplary 
taxonomy. 
 
15  For technical details , see www.xbrl.org/Specification/XBRL-2.1/REC-2003-12-31/XBRL-2.1-REC-2003-12-31+corrected-errata-
2013-02-20.html. 
16  See definition in ISO 17369:2013.  SDMX is sponsored by eight international organisations ; Bank for International 
Settlements (BIS), European Central Bank (ECB), Eurostat (Statistical Office of the European Union), International Labour 
Organization (ILO), International Monetary Fund (IMF), Organisation for Economic Co -operation and Development (OECD), 
United Nations Statistics Division (UNSD) and World Bank. 
17  See Section 4.3.

Machine-readable Pillar 3 disclosure 7 
 
 
4.2 Taxonomies 
A standardised taxonomy is essential for enhancing the usability of Pillar  3 disclosures in analyses. 
Quantitative Pillar  3 disclosures published in a machine -readable format on a bank’s website must be 
provided under the taxonomy that w ill be developed by the BCBS . The BCBS’s full taxonomy will be 
published on the BCBS’s website in a machine-readable format in parallel with the publication of the final 
policy standard. The taxonomy will be updated when required by amendments to the DIS standard.  
The BCBS’s work on taxonom y will specify unique identifiers for each of the data element s 
included in the current disclosure standard. However, it will not aim at redefining or harmonising the data 
elements over and above the level of harmonisation in the existing DIS standard. Therefore, differences in 
the meaning or interpretation of high-level data items – if any – due to national implementation of policy 
standards will remain. For example, the meaning of total RWA  can be economically different across 
countries to the extent that their calculation is different due to national implementation of policy 
standards, but the taxonomy for it would be the same across jurisdictions under the proposed standard.  
The BCBS is aware that peculiarities in national implementation of its policy standards (eg  the 
introduction of an additional risk weight bucket under the standardised approach for credit risk) may have 
led to follow-up adjustments to the format of the disclosure tables, resulting in additional items on top of 
those prescribed in the disclosure stand ard. In such cases, the relevant national supervisor will work with 
the BCBS Secretariat to include such items in the standardised taxonomy and in a mapping that shows the 
country-specific additional items across jurisdictions , both of which will be published on the BCBS’s 
website. While this process will help data users compare disclosures across jurisdictions, it will not result 
in additional or revised disclosure requirements for banks. 
In countries where banks are already required to publish machine -readable Pillar 3 disclosures 
on their websites under the taxonomies prescribed by their national jurisdictions, banks will be allowed or 
required to use the existing taxonomy. In such cases, the BCBS will work with its members to compare 
such national taxonomies with the BCBS’s taxonomy, identify differences across countries and develop a 
comparison table across jurisdictions.  The mapping table will be published on the BCBS’s website in a 
machine-readable format and updated when required by amendments to the DIS standard or 
implementations in member jurisdictions.  
In other countries, and if banks are not allowed or required to use the existing taxonomy,  banks 
should follow the BCBS’s taxonomy. The BCBS will work with its members to compare national disclosure 
requirements with the BCBS’s standard and will reflect additional requirements across countries in its 
taxonomy. National supervisors will then provide guidance on which items that are included in the 
taxonomy but are not part of the DIS standard are relevant in their jurisdiction. This information will also 
be included in the BCBS’s mapping table. Importantly, the taxonomy should neither be changed nor 
translated for data items that are reflected in the BCBS’s taxonomy.  
For banks that use plain JSON as the format for Pillar 3 disclosures, the BCBS will also maintain a 
structured mapping between the JSON attributes and the BCBS data elements in the taxonomy. The BCBS 
will provide the JSON Schema like it provides the data model for XBRL and SDMX.  
Examples of a taxonomy for disclosure templates KM1 and CR6 are included in Table 6 to Table 8 
of Annex 4. Annex 4 also includes an example of a mapping table (Table 9 and Table 10). 
4.3 API URL paths 
While standardised data formats, data exchange standards and a common taxonomy help data users to 
compare disclosure data across banks and jurisdictions, such comparisons can only be done in an efficient 
way if data retrieval by the end user is also standardised across banks and jurisdictions. Therefore, the 
BCBS proposes a standardised API.

8 Machine-readable Pillar 3 disclosure 
 
 
An API generally is used as a way of communicating with a particular computer program me or 
internet service. An API URL is a regular URL, but with a stricter naming convention. It consists of a base  
URL (“ https://example.com/documents/regulatory-disclosure”), the API version (eg “/v1”) , path 
parameters (for example the reporting date “/2025-06 -30”) and query parameters ( which typically come 
after a “?” in a URL, eg “format=xbrl-json”). The full API URL will combine these elements into a complete 
URL, eg “https://example.com/documents/regulatory-disclosure/v1/template/KM1/2025-06-30?format=
xbrl-json”. A standardised API URL path structure will enable data users to effortlessly access and query 
machine-readable disclosure information across various banks and jurisdictions.  
The standardised API described in Section 4.3 .1 must be implemented by banks if the 
decentralised approach to publication of machine-readable disclosure data is used in their jurisdiction. In 
this case, the standardised structure of the API calls ensures that supervisors only have to provide the base 
URLs of the banks in their jurisdictions that are typically stable over time. In contrast, the standardised API 
described in Section 4.3.2 could be implemented by the centralised repository if the centralised approach 
is used by a jurisdiction. The API specification could also be used to retrieve data from a possible global 
database (see Section 6.2). 
To allow for a consistent user experience across banks and countries, the elements of the API 
described in this section must not be altered through translation or format  changes, eg for dates.  The 
BCBS welcomes feedback on the proposed API structure, including the idea to allow for the OpenAPI 18 
specification. OpenAPI is a widely used framework for defining and documenting RESTful APIs 19 in a 
machine-readable format, enabling seamless integration across systems and jurisdictions.  
4.3.1 Machine-readable information provided by banks 
Minimum requirement 
Banks across BCBS member countries have different financial year-ends and may start providing machine-
readable disclosure at different reporting dates. Also, some banks may provide disclosure in additional 
languages or reporting currencies. Therefore, at 
/v1/disclosures 
banks should provide a list , in JSON format, of reporting dates  for which machine -readable Pillar  3 
disclosure can be retrieved through the API. The list should include the reporting date, whether the 
reporting date is an intermediate reporting date or corresponds to the bank’s fiscal year -end, the date of 
the last data revision, a list of formats (combination of data format and exchange standard) supported for 
that reporting date, a list of language and currency combinations in which disclosure is provided  for that 
reporting date and a list of disclosure templates available for that reporting date. If a bank revises the data 
for a reporting date, it may continue to provide older data on the website and list the revision dates for 
each revision of the data. Alternatively, a bank may provide only the most recent data with the latest 
revision date. The JSON file could be structured as follows: 
 
18  See www.openapis.org. 
19  A REST API is an API that conforms to the design principles of the representational state transfer (REST) architectural style, a 
style used to connect distributed hypermedia systems. REST APIs are sometimes referred to as RESTful APIs or RESTful web 
APIs. See more details at www.ibm.com/think/topics/rest-apis.

Machine-readable Pillar 3 disclosure 9 
 
 
{ 
  "data": [ 
    { 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          } 
        ] 
    }, 
    { 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          } 
        ] 
    } 
  ] 
} 
Whereby: 
• {ReportingAsOfDate} refers to the reporting date in ISO 8601 notation (“yyyy-mm-dd”); 
• the word “intermediate” or “yearend” specifies the report type depending on whether the 
reporting date is an intermediate reporting date or corresponds to the bank’s fiscal year -end; 
• {RevisionDate} refers to the date o n which the data were  revised, in ISO  8601 notation  
(“yyyy-mm-dd”); 
• {lc}-{ccc} denotes the two-letter ISO 639-1 language code and the three-letter ISO 4217 currency 
code; 
• {Format} specifies one of the data formats specified by the BCBS (“schema-json”, “xbrl-csv”, “xbrl-
json”, “sdmx-csv”); 
• {Template} denotes the template’s short name as specified in the DIS standard; and 
• {TemplateVersion} denotes the template version as specified in the DIS standard.

10 Machine-readable Pillar 3 disclosure 
 
 
Entries for reporting dates should be added when disclosure for that date becomes available on 
the bank’s website, and they should be removed when disclosure is no longer available after the relevant 
retention period. 
For banks that would like to provide additional filters in this query, the final standard will specify 
optional query parameters to narrow down the set of results. 
A particular disclosure template for a particular reporting date in a bank’s default (or single) data 
format, reporting currency and language should be available at  
/v1/template/{Template}/{ReportingAsOfDate} 
whereby {Template} denotes the template ’s short name as specified in the DIS standard  and 
{ReportingAsOfDate} specifies the reporting date in ISO 8601 notation.20  
The API has been structured such  that banks can meet the minimum requirements even if they 
provide only the list of available disclosures in JSON format and one file per reporting date and disclosure 
template in one of the required formats on their websites. For example, a bank that decides to disclose in 
XBRL-CSV format with the minimum set of required files could publish the following files on its website to 
comply with all disclosure requirements for 2025: 
/v1/disclosures 
/v1/template/KM1/2025-03-31 
/v1/template/KM1/2025-06-30 
/v1/template/KM1/2025-09-30 
/v1/template/KM1/2025-12-31 
… (similar for other disclosure templates) … 
The file “disclosures” is a JSON  file with the structure specified at the beginning of this section , 
which will have to be updated every quarter, while the reporting date  files are CSV files in this example 
that have to be added each quarter and contain the quarterly disclosure data for a specific template. 
Optional query parameters 
The following optional query parameters can be added after a question mark, with several query 
parameters separated by an ampersand: 
• format={Format} can be used to request disclosure data in one of the data formats and standards 
specified by the BCBS (“schema-json”, “xbrl-csv”, “xbrl-json”, “sdmx-csv”).21 If the parameter is not 
provided, data will be returned in a bank’s default format. Only the formats supported by the 
bank as per the list of disclosures are permitted. 
• revision_date=[{RevisionDate}|latest] specifies the date of the revision to be retrieved; if the 
parameter is not provided or set to “latest”, the latest revision for a reporting date will be 
returned. Only revision dates provided by the bank as per the list of disclosures are permitted.  
• language_currency={lc}-{ccc} specifies a combination of language and currency if banks provide 
machine-readable disclosure in more than one combination of language  and currency, whereby 
 
20  See www.iso.org/iso-8601-date-and-time-format.html. 
21  For example, if the base URL is https://example.com/documents/regulatory-disclosure/ as suggested above, the KM1 template 
for the second quarter of 2025 in XBRL -CSV format can be retrieved at https://example.com/documents/regulatory -
disclosure/v1/template/KM1/2025-06-30?format=xbrl-csv.

Machine-readable Pillar 3 disclosure 11 
 
 
{lc} denotes the two-letter ISO 639-1 language code22 and {ccc} denotes the three-letter ISO 4217 
currency code.23,24 If the parameter is not provided or supported, data will be returned in a bank’s 
default or only combination of language  and currency . Only the language and currency 
combinations provided by the bank as per the list of disclosures are permitted. 
If a bank does not support an optional query parameter, data can only be retrieved for the 
respective default option. 
Optional API extensions 
The final standard would include  an option for banks to provide additional functions in their APIs.  While 
these would not be mandatory, standardisation will improve the user experience as the API calls would be 
the same for all banks that decide to implement these optional elements.  For example, banks may allow 
users to retrieve individual data points for one or all available reporting dates in the bank’s default (or 
single) reporting currency and language at  
/v1/datapoint/{DatapointName}/[{ReportingAsOfDate}|all] 
whereby {DatapointName} denotes the name of the data point according to the taxonomy of the relevant 
supervisor and {ReportingAsOfDate} specifies the reporting date in ISO  8601 notation. If “all” is provided 
instead, the longest available time series for the data point will be provided. The optional query parameters 
defined above could also be used. 
4.3.2 Machine-readable information provided in a centralised repository 
While data consumption by the end user would also benefit from standardised retrieval in jurisdictions 
with a centralised repository, the added complexity of different APIs across jurisdictions is lower given that 
the number of centralised repositories is expected to be significantly lower than the number of banks 
providing data directly on their websites. Jurisdictions with existing  systems that allow the public to 
automatically access  disclosure or related data from supervisory websites may choose to retain  the se 
systems. These systems, with the ir APIs in place before 1 January 2029, must provide the following 
minimum functions: 
• retrieve a list of reporters (identified by their bank ID) and reporting dates for which 
machine-readable Pillar 3 disclosure can be retrieved through the API; and 
• retrieve specific disclosure templates for a specific reporter and reporting date. 
For other centralised repositories , the BCBS proposes a standardised API as described in the 
remainder of this section. Additional APIs could be supported at different base URLs.  
The central repository should provide a list of reporters (identified by their LEI or another unique 
national identifier where a bank does not have an LEI) and reporting dates for which machine -readable 
Pillar 3 disclosure can be retrieved through the API in JSON format at 
/v1/bankdisclosures 
 
22  See www.iso.org/iso-639-language-code. 
23  See www.iso.org/iso-4217-currency-codes.html. 
24  In the above example, the KM1 template for the second quarter of 2025 in XBRL-CSV format, Spanish language and reporting 
currency euro could be retrieved at https://example.com/documents/regulatory -disclosure/v1/template/KM1/2025-06-
30?format=xbrl-csv&language_currency=es-EUR.

12 Machine-readable Pillar 3 disclosure 
 
 
If a bank revises the data for a reporting date, the central repository may continue to provide 
older data and list the revision dates for each revision of the data. Alternatively, only the most recent data 
with the latest revision date can be provided. The JSON file could have the following structure: 
{ 
  "data": [ 
    { 
      "bank_id": "{BankID}", 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          } 
        ] 
    }, 
    { 
      "bank_id": "{BankID}", 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version: {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          } 
        ] 
    } 
  ] 
} 
Where an LEI is available, the bank ID should consist of the letters “XL -“ followed by the LEI; 
otherwise, the bank ID should consist of the two -letter ISO 3166 country code ,25 a dash and a unique 
national ID. The final standard will specify optional query parameters to narrow down the set of results.  
A specific template for a particular reporting date in a bank’s default (or single) reporting currency 
and language should be available at 
/v1/banktemplate/{BankID}/{Template}/{ReportingAsOfDate} 
 
25  See www.iso.org/iso-3166-country-codes.html.

Machine-readable Pillar 3 disclosure 13 
 
 
whereby {BankID} specifies the ID of the bank (LEI or otherwise) at the relevant level of consolidation. The 
optional API extensions would be the same as for individual banks: 
/v1/bankdatapoint/{BankID}/[{DatapointName}|all]/[{ReportingAsOfDate}|all]  
Furthermore, the optional query parameters could be supported in the same way as in the 
specification of the API for individual banks. 
If machine-readable Pillar  3 disclosure is not provided in such a centralised repository, the 
supervisor must provide a list of base URLs and IDs for all banks in its jurisdiction that provide 
machine-readable Pillar 3 disclosure according to this standard. The list should be provided at “/v1/list” in 
JSON format in the following structure: 
{ 
  "data": [ 
    { 
      "bank_id": "{BankID}", 
      "bank_name": "{BankName}", 
      "disclosure_base_url": "{BaseURL}" 
    }, 
    { 
      "bank_id": "{BankID}", 
      "bank_name": "{BankName}", 
      "disclosure_base_url": "{BaseURL}" 
    } 
  ] 
} 
whereby {BankName} refers to the name of the bank. 
4.3.3 Provision of optional templates that are not defined in the DIS standard 
Supervisory authorities or individual banks may find it useful to define additional templates that are not 
prescribed in the DIS standard. These can be provided to data users through API requests for individual 
templates. However, in order not to interfere with possible future extensions of the DIS standard, all 
jurisdictional templates must use the prefix “XJ-{cc}_”, with {cc} being the two-letter ISO 3166 country code, 
and all bank-specific templates should use the prefix “XB_”.
26 Banks and national supervisors must not use 
any template names that do not start with these prefixes in the API URL path described in this section. 
5. Data assurance 
The BCBS believes that the requirements for assurance of Pillar 3 data as set out in DIS10.10 and DIS10.11 
should not be changed. Therefore, irrespective of whether the machine-readable Pillar 3 disclosures are to 
be provided on a bank’s own website or in a centralised repository, responsibility for data accuracy shall 
remain with the relevant bank. Banks would be required to provide an email address where data users 
could report issues. 
 
26  In the above example, a new jurisdiction-specific template for Swiss banks for the second quarter of 2025 could be retrieved in 
XBRL-CSV format at https://example.com/documents/regulatory-disclosure/v1/template/XJ-CH_template/2025-06-
30?format=xbrl-csv, and a new bank -specific template could be retrieved at https://example.com/documents/regulatory-
disclosure/v1/template/XB_template/2025-06-30?format=xbrl-csv.

14 Machine-readable Pillar 3 disclosure 
 
 
However, in the centralised approach, the operator of the centralised repository may perform 
technical validations to ensure compliance with naming conventions and file format specifications. This is 
in line with the approaches taken in jurisdictions where requireme nts for machine-readable disclosure or 
public regulatory reporting already exist. If machine -readable disclosures are provided on a bank’s own 
website, they will typically be subject to supervisory processes similar to those for the current publication 
of PDF disclosure reports.  Supervisors may also decide to review the data quality of machine -readable 
disclosures in more detail using automatic processes. 
6. Information to be provided on the BCBS’s website 
6.1 Minimum information required  
To make Pillar 3 data of all reporting banks across jurisdictions globally accessible, the BCBS Secretariat 
would maintain a machine-readable list of base URLs. For each jurisdiction, this would consist of either: (i) 
a base URL of a jurisdictional disclosure data repository (if the centralised approach is adopted) or (ii) a 
base URL of a machine -readable repository of URLs o f banks’ Pillar  3 disclosure websites (if the 
decentralised approach is adopted). Graph 2 illustrates this approach , which would make it possible for 
data users to locate relevant information automatically.

Machine-readable Pillar 3 disclosure 15 
 
 
Data access without data repository at the global level Graph 2 
 
Dashed arrow: provision of base URLs by banks and national supervisors; solid arrow: data push by banks or pull by data users. 
For example, at 
/v1/supervisors/[csv|json] 
the Secretariat could provide API endpoint s returning CSV or JSON files listing the URLs of bank lists or 
Pillar 3 disclosure databases at supervisory authorities.  For example, a CSV file could have  the following 
structure: 
supervisor_name, type, base_url 
{SupervisorName}, [list|database], {BaseURL} 
{SupervisorName}, [list|database], {BaseURL} 
whereby {SupervisorName} refers to the name of the supervisory authority, the word “ list” or “database” 
indicates whether the supervisor provides a list of banks or a centralised Pillar  3 database, and {BaseURL} 
is the base URL of the list or database API. Alternatively, a JSON file could have the following structure: 
List of base 
URLs at 
supervisor 
Data users 
Data at banks 
Data at banks 
List of base URLs of 
supervisory resources at 
the Secretariat 
Database at 
supervisor

16 Machine-readable Pillar 3 disclosure 
 
 
{ 
  "data": [ 
    { 
      "supervisor_name": "{SupervisorName}", 
      "type": "[list|database]", 
      "base_url": "{BaseURL}" 
    }, 
    { 
      "supervisor_name": "{SupervisorName}", 
      "type": "[list|database]", 
      "base_url": "{BaseURL}" 
    } 
  ] 
} 
In a variant of this approach, the Secretariat would consolidate the individual base URLs of banks 
from the supervisory repositories to create a global list of base URLs of bank disclosures. This approach 
would be similar to the list of URLs the Secretariat maintains for its disclosure of G -SIB indicators. For 
example, at 
/v1/banks/[csv|json] 
the Secretariat could provide API endpoints returning a CSV or JSON file with the base URLs of individual 
banks’ disclosures. For example, a CSV file could have the following structure: 
bank_name, bank_id, country, disclosure_accesspoint, base_url 
{BankName}, {BankID}, {cc}, [centralised|decentralised], {BaseURL} 
{BankName}, {BankID}, {cc}, [centralised|decentralised], {BaseURL} 
whereby { BankName} refers to the name of the bank, {BankID } specifies the I D of the bank (LEI or 
otherwise) at the relevant level of consolidation, {cc} is the two-letter ISO 3166 country code of the country 
that provided the data for the bank, a flag indicates whether the data are provided at a centralised or 
decentralised access point, and {BaseURL} is the base URL of the bank’s or centralised repository’s API for 
providing disclosure data according to this standard . Alternatively, a JSON file could have the following 
structure:

Machine-readable Pillar 3 disclosure 17 
 
 
{ 
  "data": [ 
    { 
      "bank_name": "{BankName}", 
      "bank_id": "{BankID}", 
      "country": "{cc}", 
      "disclosure_accesspoint": "[centralised|decentralised]", 
      "base_url": "{BaseURL}" 
    }, 
    { 
      "bank_name": "{BankName}", 
      "bank_id": "{BankID}", 
      "country": "{cc}", 
      "disclosure_accesspoint": "[centralised|decentralised]", 
      "base_url": "{BaseURL}" 
    } 
  ] 
} 
The Secretariat will also provide dedicated endpoints for accessing the taxonomy mapping table, 
as well as a human-readable version of the mapping table. This resource will enable data consumers and 
integrators to automatically retrieve the correspondence between the elements used in disclosures and 
their respective representations in the BCBS’s taxonomy. The existence and ongoing maintenance of the 
mapping table will ensure semantic consistency between the disclosed data and the reference models.  
6.2 G lobal database and visualisation 
A benefit of machine-readable Pillar 3 disclosure is that it would allow for the BCBS or another public or 
private data aggregator to host a global database of Pillar  3 disclosure data for all banks where such 
machine-readable Pillar 3 information is available. While the creation of such a global database is not a 
necessary part of the proposed standard on a structured data format and taxonomy, data collection for a 
global database would be much easier than is currently the case. Such a database would provi de a 
convenient single access point to data users who do not want or know how to retrieve machine- readable 
data from multiple distributed sources.  
Importantly, the data aggregator would retrieve the individual data from existing jurisdictional 
centralised repositories where they exist and from banks’ websites in all other cases, using the process 
described in Section 6.1. Therefore, a global repository would not result in additional burden on individual 
banks as they would not have to actively submit the data to that database . Graph 3 illustrates this 
approach.

18 Machine-readable Pillar 3 disclosure 
 
 
Data access with centralised database Graph 3 
 
Dashed arrow: provision of base URLs by banks and national supervisors; solid arrow: data push by banks or pull by the Secretariat or other 
data aggregator and by data users. 
Data from the global  database could then be provided in a machine -readable format like the 
formats proposed for disclosure by banks. Moreover, data could also be visualised in a format that 
resembles the BCBS’s human-readable templates in the current DIS standard. 
While more technically  enabled and sophisticated data users might use their own systems for 
data processing and aggregation based on the data in a global  database, the BCBS or another data 
aggregator might at some point decide to provide some high-level aggregates across banks for the public. 
At this time, the BCBS has not made any decisions regarding hosting a global database of Pillar 3 disclosure 
data on its website, but welcomes feedback on the potential benefits or drawbacks.  
7. Implementation 
7.1 Implementation of machine-readable Pillar 3 disclosure 
The BCBS suggests that the requirement for machine -readable Pillar  3 disclosure become effective for 
reporting dates that begin on or after 1 January 2029. The publication of the final standard and 
List of base 
URLs at 
supervisor 
Database at 
supervisor 
Data at banks 
 Data at banks 
Data users 
Secretariat or other data 
aggregator

Machine-readable Pillar 3 disclosure 19 
 
 
standardised taxonomy and APIs is envisaged for end-2026, allowing supervisors and banks two years for 
implementation. Based on initial feedback received, the BCBS does not envisage a phased approach for 
individual quantitative tables in the DIS standard. Instead, machine -readable Pillar  3 disclosure could 
become mandatory for all quantitative tables as described in this document. However, the BCBS is 
interested in stakeholders’ views as to whether a longer lead time is required, for example for smaller 
internationally active banks in some jurisdictions.  
The BCBS currently does not envisage a requirement for mandatory  backfilling of 
machine-readable Pillar 3 disclosure for earlier reporting dates. However, the machine- readable Pillar 3 
disclosure at the first reporting date would include data for one or more previous periods as already 
specified in the current DIS standard.27 
7.2 Possible phase-out of document-based Pillar 3 disclosure 
The BCBS considered whether machine -readable Pillar  3 disclosures should be in addition to or in 
replacement of the current document -based Pillar  3 disclosures. While replacing the current 
document-based disclosures would be more in line with the idea of  reducing the burden on industry, a 
prerequisite for such an approach would be the availability of adequate tools facilitating human 
comprehension of the quantitative data to ensure transparency, as well as appropriate integration of 
qualitative content into machin e-readable formats. Given that qualitative information will not be within 
the mandatory scope of the project in the initial implementation phase, the BCBS suggests maintaining 
the requirement for disclosure in the current formats for the time being. This a voids creating an 
arrangement in which users find quantitative information in one place while related footnotes and 
explanations are included in a separate document. The BCBS could then reconsider phasing out document-
based reporting once machine-readable disclosure for qualitative information is in place and any systems 
for visualisation of this information are operational. 
7.3 Overview of project phases 
Phased approach to machine-readable Pillar 3 disclosure Table 3 
Initial project phase Potential later project phases 
• Machine-readable disclosures for quantitative data 
as proposed in this document are mandatory. 
• The BCBS provides minimum information as 
described in Section 6.1. 
• The BCBS is considering providing a centralised 
database with the Pillar 3 disclosure data. 
• Mandatory document-based Pillar 3 disclosures 
could be phased out when qualitative content has 
been integrated into machine-readable formats. 
8. Consultation questions 
Stakeholders, in particular banks and users of Pillar 3 disclosures, are welcome to provide feedback on the 
full content of this consultative document. In addition, the BCBS has highlighted specific questions which 
will assist in further developing its standard for machine-readable Pillar 3 disclosure, as detailed below. 
 
27  For example, the KM1 template requires data for the current reporting date and the previous four quarter-ends.

20 Machine-readable Pillar 3 disclosure 
 
 
Q1. What are your views on the scope of the requirement for machine-readable Pillar 3 disclosure, in 
particular the proposed initial focus on quantitative disclosure regarding the templates marked as 
“Maybe” in Table 4? 
Q2. Do you have any comments on the technical data formats and standards, the API structure and the 
general concept of the taxonomy proposed for quantitative machine-readable Pillar 3 disclosure? 
Are there other formats and solutions that should be considered? 
Q3. Are there formats other than PDF that should be considered for human-readable disclosure? 
Q4. In your view, which are the main operational benefits and challenges that this project would bring to 
banks? Would you see any other positive or negative impacts on your current disclosure process? 
Q5. Do you believe the proposed effective date would provide sufficient time for implementation of 
machine-readable Pillar 3 disclosure? Would smaller internationally active banks need additional 
time? 
Q6. How useful would data users consider a global database on the BCBS’s website? Would visualisation 
tools and industry aggregates make a global repository meaningfully more useful?

Machine-readable Pillar 3 disclosure 21 
 
 
Annex 1: Proposed edits to the Basel Framework 
Amendments to DIS10 
10.3 
Banks must publish their Pillar 3 report in a standalone document that provides a readily accessible source 
of prudential measures for users. The Pillar 3 report may be appended to, or form a discrete section of, a 
bank’s financial reporting, but it must be easily identifiable to users. Signposting of disclosure 
requirements is permitted in certain circumstances, as set out in DIS10.25 to DIS10.27. The quantitative 
disclosure requirements in this standard must also be provided  in at least one of the  common machine-
readable format s specified in DIS11  that would facilitate the use of the data.  Banks or supervisor y 
authorities must also make available on their websites an archive (for a suitable retention period to be 
determined by the relevant supervisor) of Pillar 3 reports (quarterly, semiannual and annual) relating to 
prior reporting periods. To the extent human-readable or machine-readable Pillar 3 disclosure is provided 
on the website of a centralised rep ository that is designated by a bank’s supervisor for all banks in its 
jurisdiction and meets the requirements set out in DIS 11.16 to DIS11.18, the bank can include a uniform 
resource locator (URL) of these reports on its own website, rather than provide the Pillar  3 disclosure on 
its own website. 
10.21 
The disclosure requirements are presented either in the form of templates or tables. Templates must be 
completed with quantitative data in accordance with the definitions provided. Tables generally relate to 
qualitative requirements, but quantitative infor mation is also required in some instances. Except for the 
machine-readable formats, b Banks may choose the format they prefer when presenting the information 
requested in tables. 
10.23 
For templates, the format is designated as either fixed or flexible: 
(1) Where the format of a template is pr described as fixed, banks must complete the fields in 
accordance with the instructions given. If a row/column is not considered to be relevant to a 
bank’s activities or the required information would not be meaningful to users (eg immaterial 
from a quantitative perspective), the bank may delete the specific row/column from the template 
in the human-readable report, but the numbering of the subsequent rows and columns must not 
be altered. In the machine -readable disclosure, the data points for the specific row/column 
should be marked as “na” following the specifications of the technical format chosen. Banks may 
add extra rows and columns to fixed format templates in the human-readable report if they wish 
to provide additional detail to a disclosure requirement by adding subrows or columnscategories 
of the disclosed items, but the numbering of prescribed rows and columns in the template must 
not be altered. Banks may also add subcategories to fixed format templates in the machine -
readable report provided the taxonomy for  such subcategories of the disclosed items is agreed 
with the supervisory authority and the taxonomy for the prescribed rows and columns remains 
unaltered. 
(2) Where the format of a template is described as flexible, banks may present the required 
information either in the format provided in this document or in one that better suits the bank. 
The format for the presentation of qualitative information in tables i s not prescribed. 
Notwithstanding, banks should comply with the restrictions in presentation, should such 
restrictions be prescribed in the template (eg Template CCR5 in DIS42). In addition, when a 
customised presentation of the information is used, the bank must provide information

22 Machine-readable Pillar 3 disclosure 
 
 
comparable with that required in the disclosure requirement (ie at a similar level of granularity as 
if the template/table were completed as presented in this document). 
10.24 
Where mandatory disclosure data are provided in human-readable form, they should be provided in PDF 
format in a way that allows for the search for and extraction of words contained in the document by a 
machine while at the same time being human -readable. The document must not contain textual 
information in picture format , such as in a scanned document, and it must not be password -protected. 
This does not apply to any human -readable visualisations of machine -readable disclosure banks may 
provide on a voluntary basis.  Banks are encouraged to engage with their national supervisors on the 
provision of the quantitative disclosure requirements in this standard in a common electronic format that 
would facilitate the use of the data.  
Access to disclosure data 
10.31 
Access to all human-readable and machine-readable disclosure data must be provided to the public free 
of charge and without authentication either on banks’ websites or in a centralised repository designated 
by a bank’s supervisory authority for all banks in its jurisdiction. There must be no restrictions on copying, 
publishing, distributing, transmitting, processing, citing or adapting these data, in particular  in other 
commercial or non -commercial repositories , aside from  a requirement to provide a reference to the 
original source of the data.  
New DIS11 – Standard for the technical format for machine-readable disclosure 
General 
11.1 
A machine-readable format, when used with respect to data, means data in a format that can be easily 
processed by a computer without human intervention while ensuring no semantic meaning is lost.   
11.2 
Quantitative Pillar 3 disclosure for banks must be available in at least one of the machine -readable data 
exchange formats and taxonomies specified in DIS11.8 to DIS11.9 and DIS11.6 to DIS11.7 of this standard, 
respectively. At the discretion of the supervisor, machine -readable disclosure can be published by a bank 
on its own website or in a centralised repository designated by a bank’s supervisor for all banks in a 
jurisdiction. If a bank revises the data for a reporting date, the central repository or the bank may continue 
to provide older data on the website and list the revision dates for each revision of the data. Alternatively, 
only the most recent data with the latest revision date can be provided. 
11.3 
If machine-readable Pillar 3 disclosure is published on banks’ websites, users must be able to retrieve the 
data using the application programming interface (API) specified in DIS11.11 to DIS11.15 and banks must 
report the base URLs to their supervisor. The supervisor will maintain a machine -readable repository of 
base URLs of banks’ Pillar 3 disclosures in its jurisdiction. The API and format of this repository are specified 
in DIS11.20. In addition, the repository should also be made available to the public through a human -
readable interface. Supervisors should aim to  also provid e an English language version of the data 
repository’s user interface.

Machine-readable Pillar 3 disclosure 23 
 
 
11.4 
If a centralised repository is used, supervisors have the discretion to mandate banks in their jurisdiction to 
use one of the data exchange formats and taxonomies specified in this standard for provision of disclosure 
data to the repository or to allow for different data exchange formats and taxonomies, provided that the 
public can retrieve the data from the repository in at least one of the data exchange formats and 
taxonomies specified in this standard both through a human- readable interface and through an API as 
specified in DIS11.16 to DIS11.18. Supervisors should aim to also provide an English language version of 
the data repository’s user interface. 
11.5 
Supervisors will provide the Secretariat of the Committee with the base URL of the repository of base URLs 
of websites according to DIS11.3 or the base URL of  the data repository according to DIS11.4, as 
appropriate. The Committee will maintain a list of these base  URLs on its public website  in both 
machine-readable and human-readable formats. 
Taxonomy 
11.6 
Quantitative Pillar  3 disclosure published in a machine -readable format on a bank’s website must be 
provided following a taxonomy specified by the relevant supervisor that should generally be based on the 
global taxonomy maintained by the Basel Committee Secretariat as published on the Committee’s website. 
For data items that are reflected in the Committee’s taxonomy, the taxonomy must not be changed, 
including by translation. 
11.7 
Where the national implementation of the DIS standard includes additional items on top of those 
prescribed in the standard, the relevant national supervisor will work with the Secretariat of the Committee 
to include these items in the global taxonomy and in a mapping that shows the country-specific additional 
items across jurisdictions. Both will be published on the Committee’s website. 
Data formats and exchange standards 
11.8 
Quantitative Pillar 3 disclosure must be provided in at least one of the following combinations of data 
exchange formats and standards: 
(1) eXtensible Business Reporting Language (XBRL) in combination with JSON or CSV formats ; 
(2) Statistical Data and Metadata eXchange (SDMX) in combination with CSV format; or 
(3) JSON Schema. 
Data formats must follow the definition in DIS11.9. At national discretion, supervisors may allow 
one or several of these combinations. Data can also be disclosed in additional formats on a voluntary basis, 
provided the data are consistent across all formats. 
11.9 
Data must be provided in one of the following formats: 
(1) JavaScript Object Notation (JSON) – Such files should comply with ISO/IEC 21778:2017  and in 
particular use the decimal point to separate the integer and fraction parts of a number. 
(2) Character-separated values (CSV) – Such files should comply with RFC 4180 and use the decimal 
point to separate the integer and fraction parts of a number.

24 Machine-readable Pillar 3 disclosure 
 
 
API parameter definitions 
11.10 
In the following API specification, parameters are defined as follows: 
• {ReportingAsOfDate} refers to the reporting date in ISO 8601 notation (“yyyy-mm-dd”); 
• {RevisionDate} refers to the date on which the data were  revised, in ISO  8601 notation  
(“yyyy-mm-dd”); 
• {lc} denotes the two-letter ISO 639-1 language code; 
• {ccc} denotes the three-letter ISO 4217 currency code; 
• {BankID} specifies the ID  of the bank at the relevant level of consolidation : where a Legal Entity 
Identifier (LEI) is available, the ID should consist of the letters “XL-” followed by the LEI; otherwise, 
the bank ID should consist of the two-letter ISO 3166 country code, a dash and a unique national 
ID;  
• {BankName} refers to the name of the bank; 
• {Template} denotes the template’s short name as specified in the DIS standard;  
• {DatapointName} denotes the name of a data  point according to the taxonomy of the relevant 
supervisor;  
• {Format} specifies one of the data formats specified by the Committee (“schema-json”, “xbrl-csv”, 
“xbrl-json”, “sdmx-csv”); and 
• {BaseURL} specifies the URL o f the website of the  bank or supervisory authority at which the 
relevant API as specified in this standard is available. 
API for banks’ websites providing machine-readable Pillar 3 disclosure  
11.11 
To allow for a consistent user experience across banks and jurisdictions, the elements of the API described 
in this section must not be altered through translation or change of formats, eg for dates.  
11.12 
Banks should provide a list of reporting dates for which machine -readable Pillar  3 disclosure can be 
retrieved through the API at 
/v1/disclosures 
The response should be in JSON format and structured as follows:

Machine-readable Pillar 3 disclosure 25 
 
 
{ 
  "data": [ 
    { 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
        } 
      ] 
    }, 
    { 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
        } 
      ] 
    } 
  ] 
} 
whereby the word “intermediate” or “yearend” indicates whether the reporting date is an intermediate 
reporting date or corresponds to the bank’s fiscal year -end. The remaining parameters are defined in 
DIS11.10. 
11.13 
Individual disclosure templates for a particular reporting date in the bank’s default (or single) reporting 
currency and language as well as format in their latest revision must be available at 
/v1/template/{Template}/{ReportingAsOfDate} 
with the parameters as defined in DIS11.10. 
11.14 
The following optional query parameters can be added after a question mark, with several query 
parameters separated by an ampersand:

26 Machine-readable Pillar 3 disclosure 
 
 
• format={Format} can be used to request disclosure data in one of the data formats specified by 
the Committee as defined in DIS 11.10. If the parameter is not provided, data will be returned in 
a bank’s default format.  
• revision_date=[{RevisionDate}|latest] specifies the date of the revision to be retrieved; if the 
parameter is not provided or set to “latest”, the latest revision for a reporting date will be 
returned.  
• language_currency={lc}-{ccc} specifies a combination of language and currency as defined in 
DIS11.10 if banks provide machine -readable disclosure in more than one combination of 
language and currency. If the parameter is not provided or supported, data will be returned in a 
bank’s default or only combination of language and currency. 
If a bank does not support an optional query parameter, data can only be retrieved for the 
respective default option. 
11.15 
Individual data points in the bank’s default (or single) reporting currency and language can be made 
available at 
/v1/datapoint/{DatapointName}/[{ReportingAsOfDate}|all] 
with the parameters as defined in DIS11.10. The optional query parameters defined in DIS11.14 could also 
be used. 
API for centralised repositories providing machine-readable Pillar 3 disclosure  
11.16 
The centralised repository should provide a documented API that allows users to: 
• retrieve a list of reporters (identified by their ID) and reporting dates for which machine-readable 
Pillar 3 disclosure can be retrieved through the API in JSON format; and 
• retrieve specific disclosure templates for a specific reporter and reporting date. 
Centralised repositories should generally support the API calls specified in DIS.11.17 to DIS11.18. 
Additional APIs could be supported at different base URLs . However, jurisdictions with existing systems 
that allow the public to automatically access  disclosure or related data from supervisory websites may 
choose to retain these systems. These systems, with their APIs in place before 1 January 2029, must provide 
the minimum functions specified in this paragraph. 
11.17 
The central repository  should provide a list of reporters (identified by their ID) and reporting dates for 
which machine-readable Pillar 3 disclosure can be retrieved through the API in JSON format at 
/v1/bankdisclosures

Machine-readable Pillar 3 disclosure 27 
 
 
The response should be in JSON format and structured as follows: 
{ 
  "data": [ 
    { 
      "bank_id": "{BankID}", 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
        } 
      ] 
    }, 
    { 
      "bank_id": "{BankID}", 
      "reporting_asof_date": "{ReportingAsOfDate}", 
      "report_type": "[intermediate|yearend]", 
      "revision_date": "{RevisionDate}", 
      "format": "{Format}", 
      "language_currency": ["{lc}-{ccc}", …], 
      "templates": [ 
          { 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
          }, 
            "template_name": "{Template}", 
            "template_version": {TemplateVersion} 
        } 
      ] 
    } 
  ] 
} 
whereby the word “intermediate” or “yearend” indicates whether the reporting date is an intermediate 
reporting date or corresponds to the bank’s fiscal year -end. The remaining parameters are defined in 
DIS11.10. 
11.18 
A specific template  for a particular reporting date in a bank’s default (or single) reporting currency and 
language should be available at 
/v1/banktemplate/{BankID}/{Template}/{ReportingAsOfDate} 
with the parameters as defined in DIS11.10 and optional query parameters as specified in DIS11.14.  
11.19 
Individual data points in the bank’s default (or single) reporting currency and language can be made 
available at

28 Machine-readable Pillar 3 disclosure 
 
 
/v1/bankdatapoint/{BankID}/{DatapointName}/[{ReportingAsOfDate}|all] 
with the parameters as defined in DIS11.10 and optional query parameters as specified in DIS11.14. 
API for machine-readable supervisory repository providing URLs of banks’ machine-readable 
Pillar 3 disclosure  
11.20 
Unless a centralised repository is used that meets the requirements set out in DIS 11.16 to DIS11.18, the 
supervisor must provide a  list of bank names, bank IDs and base URLs o f all banks in its jurisdiction that 
provide machine -readable Pillar  3 disclosure according to this standard . The list must be provided at 
“/v1/list” in JSON format in the following structure: 
{ 
  "data": [ 
    { 
      "bank_id": "{BankID}", 
      "bank_name": "{BankName}", 
      "disclosure_base_url": "{BaseURL}" 
    }, 
    { 
      "bank_id": "{BankID}", 
      "bank_name": "{BankName}", 
      "disclosure_base_url": "{BaseURL}" 
    } 
  ] 
} 
with the parameters as defined in DIS11.10. 
Provision of optional templates that are not defined in the DIS standard 
11.21 
National supervisors or individual banks must not provide any data in the API URL path described in this 
section for template names that are not specified in the DIS standard, unless the prefix set out in this 
paragraph is used for those templates. National supervisors can define templates that are only allowed or 
required in their jurisdiction by using the prefix “XJ -{cc}_” for the template name, with {cc} being the 
two-letter ISO  3166 country code. Similarly, supervisors can allow banks to provide bank- specific 
templates using the prefix “XB_”. 
Amendments to DIS20 to capture metadata 
20.1 
The disclosure requirements under this section are: 
(1)  Template KM1 – Key metrics (at consolidated level) 
(2)  Template KM2 – Key metrics – total loss-absorbing capacity (TLAC) requirements (at resolution 
group level) 
(3)  Table OVA – Bank risk management approach 
(4)  Template OV1 – Overview of risk-weighted assets (RWA)

Machine-readable Pillar 3 disclosure 29 
 
 
(5) Template MD1 – Metadata 
(6) Template MD2 – Metadata – References to human-readable disclosure 
20.6 
In machine -readable disclosure only, template MD1 provides users of Pillar 3 data with the metadata 
relevant to the bank, including the name of the entity, the jurisdiction, a unique bank ID, the name of the 
primary supervisory authority, the reporting date, currency and unit used in the quantitative templates, an 
email address which can be used for data inquiries and the revision date. 
20.7 
In machine-readable disclosure only, template MD 2 provides the URL of the document containing the 
complete Pillar 3 disclosure, including both quantitative and qualitative information, either on the bank’s 
website or in the centralised repository. Where information is provided in more than one document per 
combination of language and currency, multiple URLs with a short descriptio n of the scope of each 
document in English language can be provided. 
Template MD1: Metadata 
Purpose: Provide metadata relevant to the bank. 
Scope of application: The template is mandatory for all banks, but only in machine-readable disclosure. 
Content: Name of the entity, jurisdiction, unique bank ID, name of the primary supervisory authority, reporting as of date, 
currency and unit used in the quantitative templates, language of the qualitative information (including the documents 
linked through template MD2), an email address which can be used for data inquiries and the revision date. 
Frequency: Quarterly. 
Format: Fixed. 
Accompanying narrative: None. 
1 Name of the entity  
2 Jurisdiction (ISO code)  
3 ID  
4 Name of primary supervisory 
authority 
 
5 ReportingAsOfDate  
6 Currency (ISO code)  
7 Unit (eg 1, 1000, 1000000)  
8 Language (ISO code)  
9 Email address for data inquiries  
10 Revision date  
Instructions 
For the content of rows 3, 5, 6, 8 and 10 see the definitions of { BankID}, {ReportingAsOfDate}, {ccc}, {lc} 
and {RevisionDate} in DIS11.10. Row 2 must include the two-letter ISO 3166 country code of the country 
in which the entity is located.

30 Machine-readable Pillar 3 disclosure 
 
 
Template MD2: Metadata – References to human-readable disclosure 
Purpose: Provide metadata references to human-readable disclosure for the same combination of currency and language 
as specified in template MD1. 
Scope of application: The template is mandatory for all banks, but only in machine-readable disclosure. 
Content: References to human-readable disclosure for the same combination of currency and language as specified in 
template MD1.  
Frequency: Quarterly. 
Format: Variable number of rows. 
Accompanying narrative: None. 
  a b 
  Description URL 
1 URL of full Pillar 3 report where applicable   
… URL and description of additional Pillar 3 
disclosure documents 
  
 
General changes to existing disclosure standards 
To allow for versioning in machine -readable disclosure, all template headers in DIS20 to DIS85 will be 
amended to include a “ Version: 1.0” row for all templates that apply when the requirement for 
machine-readable disclosure enters into force. The template version will be increased whenever the BCBS 
amends the structure of a template in the future to the extent it affects the data items covered by the new 
standard. 
New DIS90 – Transitional arrangements 
90.1 
In jurisdictions in which machine -readable disclosure was already required before the publication of the 
DIS11 standard, national supervisors can require the banks in their jurisdiction to continue using their 
existing taxonomy for DIS templates effective before 1 January 2029. The taxonomy must be the same for 
all banks in a jurisdiction at a given reporting date. If such an alternative taxonomy is used, the relevant 
supervisor will work with the Secretariat of the Committee to prepare and maintain a mapping between 
the national and Basel Committee taxonomies.

Machine-readable Pillar 3 disclosure 31 
 
 
Annex 2: Templates in scope for machine-readable Pillar 3 disclosure 
The DIS standard includes templates for both quantitative data and qualitative information, such as business details or explanations supporting the 
quantitative data. Table 4 outlines the structure of the DIS templates and proposes which templates and sections should be included in machine -readable 
Pillar 3 disclosures. 
DIS – Disclosure requirements Table 4 
Chapter Template Name Frequency Format Main type of 
information 
required 
Proposed to be in scope of 
MRP3D during initial 
phase28 
DIS20: 
Overview of risk 
management, 
key prudential 
metrics and 
RWA 
KM1 Key metrics (at consolidated group level) Quarterly Fixed Quantitative Yes 
KM2 Key metrics – total loss-absorbing capacity (TLAC) requirements (at 
resolution group level) 
Quarterly Fixed Quantitative Yes 
OVA Bank risk management approach Annual Flexible Qualitative No 
OV1 Overview of risk-weighted assets (RWA) Quarterly Fixed Quantitative Yes 
DIS21: 
Comparison of 
modelled and 
standardised 
RWA 
CMS1 Comparison of modelled and standardised RWA at risk level Quarterly Fixed Quantitative Yes 
CMS2 Comparison of modelled and standardised RWA for credit risk at asset 
class level 
Semiannual Fixed Quantitative Yes 
 
28  Templates marked as “Maybe” currently either lack a prescribed format for quantitative information or are required, under the current standard, to align with the presentation of a  bank’s 
financial report. The BCBS  welcomes feedback on whether providing a machine- readable version of these templates would offer significant value and on potential designs for structured 
templates that include this type of quantitative information.

32 Machine-readable Pillar 3 disclosure 
 
 
DIS25: 
Composition of 
capital and 
TLAC 
CCA Main features of regulatory capital instruments and of other total 
loss-absorbing capacity (TLAC) – eligible instruments 
Ad hoc/ 
Semiannual 
Flexible Quantitative Yes 
CC1 Composition of regulatory capital Semiannual Fixed Quantitative Yes 
CC2 Reconciliation of regulatory capital to balance sheet Semiannual Flexible Quantitative Maybe 
TLAC1 TLAC composition for global systemically important banks (G-SIBs) (at 
resolution group level) 
Semiannual Fixed Quantitative Yes 
TLAC2 Material subgroup entity – creditor ranking at legal entity level Semiannual Fixed Quantitative Yes 
TLAC3 Resolution entity – creditor ranking at legal entity level Semiannual Fixed Quantitative Yes 
DIS26: Capital 
distribution 
constraints 
CDC Capital distribution constraints Annual Fixed Quantitative Yes 
DIS30: Links 
between 
financial 
statements and 
regulatory 
exposures 
LIA Explanations of differences between accounting and regulatory exposure 
amounts 
Annual Flexible Qualitative No 
LI1 Differences between accounting and regulatory scopes of consolidation 
and mapping of financial statement categories with regulatory risk 
categories 
Annual Flexible Quantitative Maybe 
LI2 Main sources of differences between regulatory exposure amounts and 
carrying values in financial statements 
Annual Flexible Quantitative Maybe 
PV1 Prudent valuation adjustments (PVAs) Annual Fixed Quantitative Yes 
DIS31: Asset 
encumbrance 
ENC Asset encumbrance Semiannual Fixed Quantitative Yes 
DIS35: 
Remuneration 
REMA Remuneration policy Annual Flexible Qualitative No 
REM1 Remuneration awarded during financial year Annual Flexible Quantitative Yes 
REM2 Special payments Annual Flexible Quantitative Yes 
REM3 Deferred remuneration Annual Flexible Quantitative Yes 
DIS40: Credit 
risk 
CRA General qualitative information about credit risk Annual Flexible Qualitative No 
CR1 Credit quality of assets Semiannual Fixed Quantitative Yes 
CR2 Changes in stock of defaulted loans and debt securities Semiannual Fixed Quantitative Yes 
CRB Additional disclosure related to the credit quality of assets Annual Flexible Quantitative Maybe 
CRB-A Additional disclosure related to prudential treatment of problem assets Annual Flexible Quantitative Maybe 
CRC Qualitative disclosure related to credit risk mitigation techniques Annual Flexible Qualitative No

Machine-readable Pillar 3 disclosure 33 
 
 
CR3 Credit risk mitigation techniques – overview Semiannual Fixed Quantitative Yes 
CRD Qualitative disclosure on banks’ use of external credit ratings under the 
standardised approach for credit risk 
Annual Flexible Qualitative No 
CR4 Standardised approach – Credit risk exposure and credit risk mitigation 
effects 
Semiannual Fixed Quantitative Yes 
CR5 Standardised approach – Exposures by asset classes and risk weights Semiannual Fixed Quantitative Yes 
CRE Qualitative disclosure related to internal ratings-based (IRB) models Annual Flexible Qualitative No 
CR6 IRB – Credit risk exposures by portfolio and probability of default (PD) 
range 
Semiannual Fixed Quantitative Yes 
CR7 IRB – Effect on RWA of credit derivatives used as credit risk mitigation 
(CRM) techniques 
Semiannual Fixed Quantitative Yes 
CR8 RWA flow statements of credit risk exposures under IRB Quarterly Fixed Quantitative Yes 
CR9 IRB – Backtesting of probability of default (PD) per portfolio Annual Flexible Quantitative Yes 
CR10 IRB (specialised lending under the slotting approach) Semiannual Flexible Quantitative Yes 
DIS42: 
Counterparty 
credit risk 
CCRA Qualitative disclosure related to CCR Annual Flexible Qualitative No 
CCR1 Analysis of CCR exposures by approach Semiannual Fixed Quantitative Yes 
CCR3 Standardised approach – CCR exposures by regulatory portfolio and risk 
weights 
Semiannual Fixed Quantitative Yes 
CCR4 IRB – CCR exposures by portfolio and probability-of-default (PD) scale Semiannual Fixed Quantitative Yes 
CCR5 Composition of collateral for CCR exposures Semiannual Flexible Quantitative Yes 
CCR6 Credit derivatives exposures Semiannual Flexible Quantitative Yes 
CCR7 RWA flow statements of CCR exposures under the internal models method 
(IMM) 
Quarterly Fixed Quantitative Yes 
CCR8 Exposures to central counterparties Semiannual Fixed Quantitative Yes 
DIS43: 
Securitisation 
SECA Qualitative disclosure requirements related to securitisation exposures Annual Flexible Qualitative No 
SEC1 Securitisation exposures in the banking book Semiannual Flexible Quantitative Yes 
SEC2 Securitisation exposures in the trading book Semiannual Flexible Quantitative Yes 
SEC3 Securitisation exposures in the banking book and associated regulatory 
capital requirements – bank acting as originator or as sponsor 
Semiannual Fixed Quantitative Yes 
SEC4 Securitisation exposures in the banking book and associated capital 
requirements – bank acting as investor 
Semiannual Fixed Quantitative Yes

34 Machine-readable Pillar 3 disclosure 
 
 
DIS45: 
Sovereign 
exposures 
SOV1 Exposures to sovereign entities – country  Semiannual Fixed Quantitative Yes 
SOV2 Exposures to sovereign entities – currency denomination breakdown Semiannual Fixed Quantitative Yes 
SOV3 Exposures to sovereign entities – accounting classification breakdown Semiannual Fixed Quantitative Yes 
DIS50: Market 
risk 
MRA General qualitative disclosure requirements related to market risk Annual Flexible Qualitative No 
MR1 Market risk under the standardised approach Semiannual Fixed Quantitative Yes 
MRB Qualitative disclosures for banks using the IMA Annual Flexible Qualitative No 
MR2 Market risk for banks using the IMA Quarterly Fixed Quantitative Yes 
MR3 Market risk under the simplified standardised approach Semiannual Fixed Quantitative Yes 
DIS51: Credit 
valuation 
adjustment risk 
CVAA General qualitative disclosure requirements related to CVA Annual Flexible Qualitative No 
CVA1 The reduced basic approach for CVA (BA-CVA) Semiannual Fixed Quantitative Yes 
CVA2 The full basic approach for CVA (BA-CVA) Semiannual Fixed Quantitative Yes 
CVAB Qualitative disclosures for banks using the SA-CVA Annual Flexible Qualitative No 
CVA3 The standardised approach for CVA (SA-CVA) Semiannual Fixed Quantitative Yes 
CVA4 RWA flow statements of CVA risk exposures under SA-CVA Quarterly Fixed Quantitative Yes

Machine-readable Pillar 3 disclosure 35 
 
 
DIS55: 
Cryptoasset 
exposures 
CAEA Qualitative disclosure on a bank’s activities related to cryptoassets and the 
approach used in assessing the classification conditions 
Annual Flexible Qualitative No 
CAE1 Cryptoasset exposures and capital requirements Semiannual Flexible Quantitative Yes 
CAE2 Accounting classification of exposures to cryptoassets and cryptoliabilities Semiannual Flexible Quantitative Maybe 
CAE3 Liquidity requirements for exposures to cryptoassets and cryptoliabilities Semiannual Fixed Quantitative Yes 
DIS60: 
Operational risk 
ORA General qualitative information on a bank’s operational risk framework Annual Flexible Qualitative No 
OR1 Historical losses Annual Fixed Quantitative Yes 
OR2 Business indicator and subcomponents Annual Fixed Quantitative Yes 
OR3 Minimum required operational risk capital Annual Fixed Quantitative Yes 
DIS70: Interest 
rate risk in the 
banking book 
IRRBBA Interest rate risk in the banking book (IRRBB) risk management objective 
and policies 
Annual Flexible Quantitative Yes 
IRRBB1 Quantitative information on IRRBB Annual Fixed Quantitative Yes 
DIS75: 
Macroprudential 
supervisory 
measures 
GSIB1 Disclosure of global systemically important bank (G-SIB) indicators Annual Flexible Quantitative Yes 
CCyB1 Geographical distribution of credit exposures used in the calculation of the 
bank-specific countercyclical capital buffer requirement 
Semiannual Flexible Quantitative Yes 
DIS80: Leverage 
ratio 
LR1 Summary comparison of accounting assets vs leverage ratio exposure 
measure 
Quarterly Fixed Quantitative Yes 
LR2 Leverage ratio common disclosure template Quarterly Fixed Quantitative Yes 
DIS85: Liquidity LIQA Liquidity risk management Annual Flexible Quantitative Maybe 
LIQ1 Liquidity coverage ratio (LCR) Quarterly Fixed Quantitative Yes 
LIQ2 Net stable funding ratio (NSFR) Semiannual Fixed Quantitative Yes

36 Machine-readable Pillar 3 disclosure 
 
 
Annex 3: Examples of various data formats and data exchange standards 
KM1 excerpt with data for use in the examples Table 5 
  T T-1 T-2 T-3 T-4 
 Available capital (amounts) 
1 Common Equity Tier 1 (CET1) 240000 239814 239485 239231 238776 
1a Fully loaded ECL accounting model CET1 235000 234962 234577 234130 233752 
An XBRL-CSV file following the specifications in the proposed standard would look as follows:  
Id, concept, decimals, entity, period, unit, bas3_CBReservesExemptions, bas3_Category, bas3_Framework, 
bas3_OutputFloor, bas3_RelativePeriod, bas3_Tier, value 
f1, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:Current, bas3:na, bas3:T, bas3:CET1, 240000 
f2, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:FullyLoaded, bas3:na, bas3:T, bas3:CET1, 235000 
f35, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:Current, bas3:na, bas3:T-1, bas3:CET1, 239814 
f36, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:FullyLoaded, bas3:na, bas3:T-1, bas3:CET1, 234962 
f69, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:Current, bas3:na, bas3:T-2, bas3:CET1, 239485 
f70, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:FullyLoaded, bas3:na, bas3:T-2, bas3:CET1, 234577 
f103, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:Current, bas3:na, bas3:T-3, bas3:CET1, 239231 
f104, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:FullyLoaded, bas3:na, bas3:T-3, bas3:CET1, 234130 
f137, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:Current, bas3:na, bas3:T-4, bas3:CET1, 238776 
f138, bas3:AvailableCapital, 0, scheme:DummyBank, 2022-01-01T00:00:00/2022-04-01T00:00:00, iso4217:USD, 
bas3:na, bas3:Capital, bas3:FullyLoaded, bas3:na, bas3:T-4, bas3:CET1, 233752 
An XBRL-JSON file following the specifications in the proposed standard would look as follows:  
{ 
 "documentInfo": { 
  "documentType": "https://xbrl.org/2021/xbrl-json", 
  "features": { 
   "xbrl:canonicalValues": true 
  }, 
  "namespaces": { 
   "bas3": "http://bis.org/basel3/km1", 
   "iso4217": "http://www.xbrl.org/2003/iso4217", 
   "scheme": "http://standards.iso.org/iso/17442",

Machine-readable Pillar 3 disclosure 37 
 
 
   "xbrl": "https://xbrl.org/2021", 
   "xbrli": "http://www.xbrl.org/2003/instance" 
  }, 
  "linkTypes": { 
   "footnote": "http://www.xbrl.org/2003/arcrole/fact-footnote" 
  }, 
  "linkGroups": { 
   "_": "http://www.xbrl.org/2003/role/link" 
  }, 
  "taxonomy": [ 
   "bas3-km1.xsd" 
  ] 
 }, 
 "facts": { 
  "f1": { 
   "value": "240000.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:Current", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f2": { 
   "value": "235000.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:FullyLoaded", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f35": { 
   "value": "239814.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:Current", 
    "bas3:OutputFloor": "bas3:na",

38 Machine-readable Pillar 3 disclosure 
 
 
    "bas3:RelativePeriod": "bas3:T-1", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f36": { 
   "value": "234962.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:FullyLoaded", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-1", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f69": { 
   "value": "239485.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:Current", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-2", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f70": { 
   "value": "234577.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:FullyLoaded", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-2", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f103": { 
   "value": "239231.0", 
   "decimals": 0, 
   "dimensions": {

Machine-readable Pillar 3 disclosure 39 
 
 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:Current", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-3", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f104": { 
   "value": "234130.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:FullyLoaded", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-3", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f137": { 
   "value": "238776.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:Current", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-4", 
    "bas3:Tier": "bas3:CET1", 
    "unit": "iso4217:USD" 
   } 
  }, 
  "f138": { 
   "value": "233752.0", 
   "decimals": 0, 
   "dimensions": { 
    "concept": "bas3:AvailableCapital", 
    "entity": "scheme:DummyBank", 
    "period": "2022-01-01T00:00:00/2022-04-01T00:00:00", 
    "bas3:CBReservesExemptions": "bas3:na", 
    "bas3:Category": "bas3:Capital", 
    "bas3:Framework": "bas3:FullyLoaded", 
    "bas3:OutputFloor": "bas3:na", 
    "bas3:RelativePeriod": "bas3:T-4", 
    "bas3:Tier": "bas3:CET1",

40 Machine-readable Pillar 3 disclosure 
 
 
    "unit": "iso4217:USD" 
   } 
  } 
 } 
} 
An SDMX-CSV file following the specifications in the proposed standard would look as follows:  
STRUCTURE, STRUCTURE_ID, ACTION, Template, Reporter, TIME_PERIOD, RelativePeriod, Category, Measure, 
Framework, Tier, OutputFloor, CBReservesExemptions, UnitForValue, OBS_VALUE 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T, Capital, AvailableCapital, Current, CET1, na, na, 
$, 240000 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T, Capital, AvailableCapital, FullyLoaded, CET1, na, 
na, $, 235000 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T-1, Capital, AvailableCapital, Current, CET1, na, na, 
$, 239814 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T -1, Capital, AvailableCapital, FullyLoaded, CET1, 
na, na, $, 234962 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T-2, Capital, AvailableCapital, Current, CET1, na, na, 
$, 239485 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T -2, Capital, AvailableCapital, FullyLoaded, CET1, 
na, na, $, 234577 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T-3, Capital, AvailableCapital, Current, CET1, na, na, 
$, 239231 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T -3, Capital, AvailableCapital, FullyLoaded, CET1, 
na, na, $, 234130 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T-4, Capital, AvailableCapital, Current, CET1, na, na, 
$, 238776 
dataflow, BIS.MRD3P:KM1(2.0), I, KM1, DummyBank, 2022-Q1, T -4, Capital, AvailableCapital, FullyLoaded, CET1, 
na, na, $, 233752 
Finally, a JSON Schema file would look as follows: 
{ 
  “KM1”: { 
    "QuarterReference": "2022-Q1", 
    "T": { 
      "Capital": { 
        "Available Capital": { 
          "Current": { 
            "CET1": "240000", 
          } 
          "FullyLoaded": { 
            "CET1": "235000", 
          } 
        } 
      } 
    } 
    "T-1": { 
      "Capital": {

Machine-readable Pillar 3 disclosure 41 
 
 
        "Available Capital": { 
          "Current": { 
            "CET1": "239814", 
          } 
          "FullyLoaded": { 
            "CET1": "234962", 
          } 
        } 
      } 
    } 
    "T-2": { 
      "Capital": { 
        "Available Capital": { 
          "Current": { 
            "CET1": "239485", 
          } 
          "FullyLoaded": { 
            "CET1": "234577", 
          } 
        } 
      } 
    } 
    "T-3": { 
      "Capital": { 
        "Available Capital": { 
          "Current": { 
            "CET1": "239231", 
          } 
          "FullyLoaded": { 
            "CET1": "234130", 
          } 
        } 
      } 
    } 
    "T-4": { 
      "Capital": { 
        "Available Capital": { 
          "Current": { 
            "CET1": "238776", 
          } 
          "FullyLoaded": { 
            "CET1": "233752", 
          } 
        } 
      } 
    } 
  } 
}

42 Machine-readable Pillar 3 disclosure 
 
 
Annex 4: Taxonomy and mapping examples 
This section describes the relationship between existing disclosure templates, the proposed BCBS taxonomy , data structure definitions  (DSDs) and the 
mapping to member jurisdictions’ existing taxonomies. The BCBS uses two existing disclosure templates as illustrative examples. The KM1 and CR6 templates 
prescribe a fixed structure, while banks are allowed to alter the structure of rows or columns if stated as such in the template format description or following 
DIS10.23(1).29 The current standard provides the option to add rows in both template examples to cover, for example,  additional regulatory or financial 
metrics. 
DIS templates, data structure definition (DSD) and related IDs 
Each template will be translated into a technical DSD using the BCBS taxonomy. It will define the concepts used to describe the specific data sets. The final 
standard will provide unique identifiers (IDs) for all fields in the templates included in the DIS standard. In some cases, t his may also include addit ional IDs 
for fields that are not included at the BCBS level (shaded in light brown) but that have been added by national supervisors in the national implementation of 
the standard. The following examples illustrate these concepts in a simplified way. 
 
29  “ Where the format of a template is described as fixed, banks must complete the fields in accordance with the instructions given. If a row/column is not considered to be relevant to a bank’s 
activities or the required information would not be meaningful to users (eg immaterial from a quantitative perspective), the bank may delete the specific row/column from the template, but 
the numbering of the subsequent rows and columns must not be altered. Banks may add extra rows and extra columns to fixed format templates if they wish to provide additional detail to a 
disclosure requirement by adding sub-rows or columns, but the numbering of prescribed rows and columns in the template must not be altered.”

Machine-readable Pillar 3 disclosure 43 
 
 
Template KM1: Key metrics (at consolidated group level) 
The below example reflects the first part of the KM1 template in the current DIS standard. The example in Table 6 and Table 7 illustrates the concept of how 
a plain vanilla template could be handled in machine-readable reporting.

44 Machine-readable Pillar 3 disclosure 
 
 
KM1 Table 6 
Purpose: To provide an overview of a bank’s prudential regulatory metrics. 
Scope of application: The template is mandatory for all banks. 
Content: Key prudential metrics related to risk -based capital ratios, leverage ratio and liquidity standards. Banks are 
required to disclose each metric ’s value using the corresponding standard ’s specifications for the reporting period -end 
(designated by T in the template below) as well as the four previous quarter -end figures (T -1 to T -4). All metrics are 
intended to reflect actual bank values for (T), with the exception of “fully loaded expected credit losses (ECL)” metrics, the 
leverage ratio (excluding the impact of any applicable temporary exemption of central bank reserves) and metrics 
designated as “pre-floor” which may not reflect actual values. 
Frequency: Quarterly. 
Format: Fixed. If banks wish to add rows to provide additional regulatory or financial metrics, they must provide definitions 
for these metrics and a full explanation of how the metrics are calculated (including the scope of consolidation and the 
regulatory capital used if relevant). The additional metrics must not replace the metrics in this disclosure requirement. 
Accompanying narrative: Banks are expected to supplement the template with a narrative commentary to explain any 
significant change in each metric ’s value compared with previous quarters, including the key drivers of such changes 
(eg whether the changes are due to changes in the regulatory framework, group structure or business model). 
Banks that apply transitional arrangement for ECL are expected to supplement the template with the key elements of the 
transition they use. 
  a b c d e 
  T T-1 T-2 T-3 T-4 
 Available capital (amounts) 
1 Common Equity Tier 1 (CET1) f1 f35 f69 f103 f137 
1a Fully loaded ECL accounting model CET1 f2 f36 f70 f104 f138 
2 Tier 1 f3 f37 f71 f105 f139 
2a Fully loaded ECL accounting model Tier 1 f4 f38 f72 f106 f140 
3 Total capital  f5 f39 f73 f107 f141 
3a Fully loaded ECL accounting model total capital f6 f40 f74 f108 f142 
 Risk-weighted assets (amounts) 
4 Total risk-weighted assets (RWA) f7 f41 f75 f109 f143 
… … … … … … …

Machine-readable Pillar 3 disclosure 45 
 
 
A simplified DSD for KM1 could look as follows: 
KM1: simplified DSD Table 7 
Template 
Nr. 
ID Template Category Concept Framework Tier RelativePeriod … 
1 f1 KM1 Capital AvailableCapital Current CET1 T … 
1a f2 KM1 Capital AvailableCapital FullyLoaded CET1 T … 
2 f3 KM1 Capital AvailableCapital Current Tier1 T … 
2a f4 KM1 Capital AvailableCapital FullyLoaded Tier1 T … 
3 f5 KM1 Capital AvailableCapital Current Total T … 
3a f6 KM1 Capital AvailableCapital FullyLoaded Total T … 
4 f7 KM1 Assets RWA Current na T … 
… … … … … … … … … 
Dimension members can be concatenated to allow for a more human -readable observation name, for example Common Equity Tier 1 (CET1) with 
the BCBS ID f1 would read as “KM1.Capital.AvailableCapital.Current.CET1.T”.

46 Machine-readable Pillar 3 disclosure 
 
 
Template CR6: IRB – Credit risk exposures by portfolio and PD range 
This example is described as a fixed template structure in the DIS standard. At the same time, it uses the option in the standard to add rows for flexible 
portfolio breakdowns at jurisdiction level. While the standard says the PD scale cannot be altered, DIS10.23( 1) allows banks to add more granularity, by for 
example additional PD bands, as illustrated in Table 8. This example on flexibility also serve s other cases in which a specific metric in the DIS standard has a 
more granular representation in national disclosure standards. 
CR6 Table 8 
Purpose: Provide main parameters used for the calculation of capital requirements for IRB models. The purpose of disclosing these parameters is to enhance the transparency of 
banks’ RWA calculations and the reliability of regulatory measures. 
Scope of application: The template is mandatory for banks using either the F-IRB or the A-IRB approach for some or all of their exposures. 
Content: Columns (a) and (b) are based on accounting carrying values and columns (c) to (l) are regulatory values. All are based on the scope of regulatory consolidation. 
Frequency: Semiannual. 
Format: Fixed. The columns, their contents and the PD scale in the rows cannot be altered, but the portfolio breakdown in the rows will be set at the jurisdiction level to reflect 
exposure categories under local implementation of the IRB approaches. Where a bank makes use of both F-IRB and A-IRB approaches, it must disclose one template for each 
approach. 
Accompanying narrative: Banks are expected to supplement the template with a narrative to explain the effect of credit derivatives on RWAs. 
  a b c d e f g h i j k l 
 PD scale 
Original on-
balance sheet 
gross exposure 
Off-balance sheet 
exposures pre-CCF 
Average CCF 
EAD post-CRM and 
post-CCF 
Average PD 
Number of 
obligors 
Average LGD 
Average maturity 
RWA 
RWA density 
EL 
Provisions 
National 
portfolio X 
             
 0.00 to <0.15 f34545 … … … … … … … … … …  
 0.15 to <0.25 … … … … … … … … … … …  
 0.25 to <0.50 … … … … … … … … … … …  
 … … … … … … … … … … … …

Machine-readable Pillar 3 disclosure 47 
 
 
Sovereign              
 0.00 to <0.15 f34566 … … … … … … … … … …  
 0.00 to <0.05 f34567 … … … … … … … … … …  
 0.05 to <0.15 … … … … … … … … … … …  
 0.15 to <0.25 … … … … … … … … … … …  
 0.25 to <0.50 … … … … … … … … … … …  
 0.50 to <0.75 … … … … … … … … … … …  
 0.75 to <2.50 … … … … … … … … … … …  
 2.50 to <10.00 … … … … … … … … … … …  
 10.00 to <100.00 … … … … … … … … … … …  
 100.00 (Default) … … … … … … … … … … …  
 Sub-total  … … … … … … … … … … … … 
Total (all portfolios) … … … … … … … … … … … … 
 
BCBS taxonomy, field IDs and mapping to IDs in member jurisdictions 
Table 9 and Table 10 illustrate the idea of a mapping between the BCBS taxonomy and jurisdictions which already have a taxonomy in place  (for Brazil – 
country code “BR”). For countries using the standardised taxonomy of the BCBS (for an exemplary  country with code “XX”), the “national ID” column would 
remain empty and the existence of a row with a BCBS ID would indicate that a certain data item is also required in that country, which is important information 
for taxonomy entries that do not refer to a data item from the BCBS DIS standard. In both cases, the tables will act as a key to link data elements in the various 
taxonomies used across member jurisdictions with the standardised taxonomy of the  BCBS.

48 Machine-readable Pillar 3 disclosure 
 
 
BCBS taxonomy Table 9 
BCBS ID Included in BCBS 
DIS standard 
BCBS name Template Template version Valid from Valid to (na if until 
further notice) 
f1 Yes KM1.Capital.AvailableCapital.Current.CET1.T  KM1 1.0 2025-01-01 na 
… … …     
f34566 Yes CR6.Sovereign.0-00_0-15.OnBS.GrossExposure.Amount CR6 1.0 2025-01-01 na 
f34567 No CR6.Sovereign.0-00_0-05.OnBS.GrossExposure.Amount CR6 1.0 2025-01-01 na 
… … …     
 
Mapping national taxonomies Table 10 
ID BCBS ID Country National ID Valid from Valid to  
(na if until further notice) 
 f1 BR km1_t.km1_regulatory_capital.km1_1 2025-01-01 na 
 … … … … … 
 f34566 BR … 2025-01-01 na 
 f34567 BR … 2025-01-01 na 
 f1 XX na 2025-01-01 na 
 … … … … … 
 f23455 XX na 2025-01-01 na 
 … … … … … 
 f34566 XX na 2025-01-01 na 
 f34567 XX na 2025-01-01 na