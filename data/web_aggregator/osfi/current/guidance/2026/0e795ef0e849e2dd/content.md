255 Albert Street 
Ottawa, Canada  
K1A 0H2 
 
www.osfi-bsif.gc.ca 
 
 
 
 
 
Unclassified / Non classifié 
Guideline 
 
Subject: Interest Rate Risk Management  
 
Category: Sound Business and Financial Practices 
 
No:  B-12   Effective Date: November 2026/January 2027 
 
 
 
For institutions with a fiscal year ending October 31 or December 31, respectively.  
 
Interest rate risk is an important risk that can affect the safety and soundness of financial 
institutions. A control framework that manages this risk to prudent levels is a fundamental 
component of sound banking practice. This guideline outlines OSFI’s expectations regarding an 
institution’s identification, measurement, management, monitoring and control of interest rate 
risk in the banking book (IRRBB). The guideline applies to banks (including federal credit 
unions), bank holding companies, federally regulated trust companies and federally regulated 
loan companies, collectively referred to as “institutions”.   
 
This guideline is drawn from the Basel Committee on Banking Supervision (BCBS) Basel 
Framework published on the Bank for International Settlements (BIS) website.1 For reference, 
the Basel paragraph numbers that are associated with the text appearing in this guideline are 
indicated in square brackets at the end of each paragraph.2  
 
 
 
 
1    The Basel Framework  
2  Following the format: [Basel Framework XXX yy.zz].

Banks/BHC/T&L Interest Rate Risk Management 
  Page 2 of 28 
Unclassified / Non classifié 
 
Table of Contents 
 
 Page 
 
1. Introduction ....................................................................................................................3 
2. Overriding Principle of IRRBB .....................................................................................4 
3. Governance and Risk Appetite ......................................................................................5 
Risk management framework ..................................................................................6 
Delegation ................................................................................................................7 
Internal controls .......................................................................................................7 
Policy limits .............................................................................................................8 
4. Measurement, assumptions, systems integrity and model governance ..........................9 
Economic value and earnings-based measures ........................................................9 
Interest rate shock and stress scenarios ..................................................................10 
Developing internal interest rate shock and stress scenarios .................................11 
Common products with behavioural optionalities .................................................14 
Measurement systems and data integrity ...............................................................16 
Model governance process .....................................................................................17 
5. Public Disclosure .........................................................................................................19 
6. Capital adequacy and outlier test .................................................................................20 
Assessment .............................................................................................................21 
Outlier Test ............................................................................................................23 
Annex 1. The standardized interest rate shock scenarios ..................................................25

Banks/BHC/T&L Interest Rate Risk Management 
  Page 3 of 28 
Unclassified / Non classifié 
1. Introduction 
 
1. IRRBB refers to the current or prospective risk to an institution’s capital and earnings 
arising from adverse movements in interest rates that affect the institution’s banking book 
positions. When interest rates change, the present value and timing of future cash flows change. 
Such changes will affect the underlying value of an institution’s assets, liabilities and/or off-
balance sheet items and, hence, its economic value. Changes in interest rates also affect an 
institution’s earnings by altering interest rate-sensitive income and expenses, affecting its net 
interest income (NII). Excessive IRRBB can pose a significant threat to an institution’s current 
capital base and/or its future earnings if not managed appropriately. [Basel Framework, SRP 
31.1] 
 
1.1 Scope of Application 
 
2. This guideline applies to all institutions on a consolidated basis. OSFI’s application of 
this guideline will be commensurate with each institution’s nature, size, business and complexity 
as well as its structure, economic significance and risk profile. 
 
3. When reviewing an institution’s compliance with this guideline, OSFI will consider the 
following criteria:  
a. The level of inherent IRRBB at the institution;  
b. The complexity of an institution’s business lines, products and services; and 
c. The size of an institution, taking into consideration on and off-balance sheet exposures as 
well as income statement metrics (e.g. earnings) and potential organizational structural 
limitations due to an institution’s size.  
 
4. To the extent possible, OSFI will apply consistent expectations across institutions with 
similar characteristics based on the above criteria. OSFI will assess an institution’s adherence to 
this guideline based on the principles set out below. OSFI recognizes that there are a range of 
acceptable practices to effectively manage IRRBB.        
 
1.1.1 Definitions  
 
5. This guideline considers three main sub-types of IRRBB: 
a. Gap risk arises from the term structure of banking book3 instruments, and describes 
the risk arising from the timing of instruments’ rate changes. The extent of gap risk 
depends on whether changes to the term structure of interest rates occur consistently 
across the yield curve (parallel risk) or differentially by period (non-parallel risk). 
b. Basis risk describes the impact of relative changes in interest rates for financial 
instruments that have similar tenors but are priced using different interest rate indices. 
c. Option risk arises from option derivative positions or from optional elements 
embedded in an institution’s assets, liabilities and/or off-balance sheet items, where 
the institution or its customer can alter the level and timing of their cash flows. 
 
3   For the purposes of this guideline, “banking book” is defined as all products or instruments that do not fall within 
the trading book boundary.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 4 of 28 
Unclassified / Non classifié 
Option risk can be further characterized into automatic option risk and behavioural 
option risk. [Basel Framework, SRP 31.2] 
 
6. Each of these sub-types can change the price/value or earnings/costs of interest rate-
sensitive assets, liabilities and/or off-balance sheet items in a way, or at a time, that can 
adversely affect an institution’s financial condition. [Basel Framework, SRP 31.2] 
 
1.1.2 Credit spread risk in the banking book  
 
7. While the three sub-types listed above are directly linked to IRRBB, credit spread risk in 
the banking book (CSRBB) is a related risk that institutions need to monitor and assess as part of 
their interest rate risk management framework. CSRBB refers to any kind of asset/liability 
spread risk of credit-risky instruments that is not explained by IRRBB and by the expected 
credit/jump to default risk. [Basel Framework, SRP 31.3] 
 
1.1.3 Economic value and earnings-based measures 
 
8. While the economic value and earnings-based measures share certain characteristics, 
institutions primarily utilize the latter for IRRBB management, whereas economic value provides 
a suitable benchmark for comparability and capital adequacy. If an institution were to solely 
minimize its economic value risk by matching the repricing of its assets with liabilities beyond 
the short term, it could run the risk of earnings volatility. Likewise, management decisions to 
optimize short-term NII fluctuations could be structurally unviable when evaluated on a longer 
horizon. Consequently, it is important for institutions to manage IRRBB through both economic 
value and earnings-based measures, as stated under OSFI Principle #4 below. [Basel Framework, 
SRP 31.29] 
 
2. Overriding Principle of IRRBB 
 
OSFI Principle #1 (BCBS Principle #14): IRRBB is an important risk for all institutions 
that should be specifically identified, measured, monitored and controlled. In addition, 
institutions should monitor and assess CSRBB. [Basel Framework, SRP 31.4(1)] 
 
9. IRRBB is a significant risk that arises from banking activities of all institutions. IRRBB 
arises due to interest rate variability over time, while the business of banking typically involves 
intermediation activity that produces exposures to both maturity mismatch (e.g., long-maturity 
assets funded by short-maturity liabilities) and rate mismatch (e.g., fixed rate loans funded by 
variable rate deposits). In addition, there are optionalities embedded in many of the common 
banking products (e.g., non-maturity deposits, term deposits, fixed rate loans and mortgage 
commitments) that may or may not be triggered as a result of changes in interest rates. [Basel 
Framework, SRP 31.6] 
 
 
4  The numbering of the respective OSFI principles is sequential; however, the numbering featured in the Basel 
Framework is also provided (in brackets) for ease of reference.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 5 of 28 
Unclassified / Non classifié 
10. OSFI expects all institutions to be familiar with all potentially material elements of 
IRRBB, to actively identify their IRRBB exposures and to take appropriate steps to measure, 
monitor and control IRRBB. [Basel Framework, SRP 31.7] 
 
11. Institutions should identify the interest rate risks inherent in their banking book products 
and activities undertaken, and ensure that these are subject to adequate procedures and controls. 
Significant hedging or risk management initiatives should be approved by appropriate 
committees before being implemented. Products and activities that are new to an institution 
should undergo a careful pre-acquisition review to ensure that the IRRBB characteristics and 
model risks are well understood and subject to a predetermined test phase before being fully 
rolled out. Prior to introducing a new product, hedging or risk-taking strategy, institutions should 
have in place appropriate operational procedures and risk control systems. The management of 
an institution’s IRRBB should be integrated within its broader risk management framework and 
aligned with its business planning and budgeting activities. [Basel Framework, SRP 31.8] 
 
12. In identifying, measuring, monitoring and controlling IRRBB, institutions should also 
ensure that, where appropriate, and taking into account the scope of application of this guideline, 
CSRBB is properly monitored and assessed5.  [Basel Framework, SRP 31.9]  
13. The allocation of capital to risk is an integral component of sound IRRBB management. 
In the case of larger institutions6, OSFI expects that IRRBB management and IRRBB risk will be 
transferred to centre(s) of expertise, with risk capital and associated profit and loss being 
allocated and measured accordingly. As part of this centralization process, larger institutions 
should utilize an appropriate funds transfer pricing (FTP) mechanism to manage this transfer. 
Additionally, these institutions should have a Senior Management Committee to oversee this 
FTP process. The committee should include representatives from all major business lines as well 
as from the relevant control functions and treasury. Smaller institutions with low IRRBB profile 
may be able to incorporate simplified methods for FTP framework design and oversight. 
3. Governance and Risk Appetite 
 
OSFI Principle #2 (BCBS Principle #2): Institutions are responsible for oversight of the 
IRRBB management framework, and the institution’s risk appetite for IRRBB. Monitoring 
and management of IRRBB should be undertaken by Senior Management or its delegates. 
Institutions should have an adequate IRRBB management framework, involving regular 
independent reviews and evaluations of the effectiveness of the system. [Basel Framework, 
SRP 31.4(2)] 
 
Please refer to OSFI’s Corporate Governance Guideline for OSFI’s expectations of institution 
Boards of Directors in regards to the management of capital and liquidity.  
 
5    Refer to SRP98, Application Guidance on interest rate risk in the banking book of the Basel Committee on 
Banking Supervision for further details on CSRBB. 
6    The criteria considered for the application of this paragraph are described in the scope of application section of  
the guideline. In addition, other factors considered will include product diversity and funding models.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 6 of 28 
Unclassified / Non classifié 
 
3.1 Risk management framework 
 
14. Senior Management is responsible for understanding the nature and the level of the 
institution’s IRRBB exposure as well as overall policies with respect to IRRBB. It should ensure 
that there is clear guidance regarding the acceptable level of IRRBB, given the institution’s 
business strategies. [Basel Framework, SRP 31.10] 
 
15. Accordingly, Senior Management is responsible for ensuring that the institution 
identifies, measures, monitors and controls IRRBB consistent with the approved strategies and 
policies. More specifically, Senior Management is responsible for setting: 
a. appropriate limits on IRRBB, including the definition of specific procedures and 
approvals necessary for exceptions, and ensuring compliance with those limits; 
b. adequate systems for measuring IRRBB; 
c. standards for measuring IRRBB, valuing positions and assessing performance, including 
procedures for updating interest rate shock and stress scenarios and key underlying 
assumptions driving the institution’s IRRBB analysis; 
d. a comprehensive IRRBB reporting and review process; and 
e. effective internal controls and management information systems (MIS). 
[Basel Framework, SRP 31.11] 
 
16. Senior Management should oversee the approval, implementation and review of IRRBB 
management policies, procedures and limits. Senior Management should receive and review 
regular reports (at least monthly) on the level and trend of the institution’s IRRBB exposures. 
The reporting should be sufficiently detailed to allow Senior Management to understand and 
assess the performance of its delegates in monitoring and controlling IRRBB in compliance with 
approved policies. OSFI expects that such reviews will be carried out more frequently when the 
institution has significant IRRBB exposures or has positions in complex IRRBB instruments. 
[Basel Framework, SRP 31.12] 
 
17. Senior Management should understand the implications of the institution’s IRRBB 
strategies, including the potential linkages with and impact on market, liquidity, credit and 
operational risk. OSFI expects Senior Management members to have sufficient technical 
knowledge to question and challenge the reports, to be responsible for ensuring that delegated 
staff has the capability and skills to understand IRRBB, and to ensure that adequate resources are 
devoted to IRRBB management. Institutions should have an integrated view of IRRBB. As such, 
OSFI expects Senior Management to understand IRRBB management methodologies and to 
encourage discussion between the risk management control function(s) and position-taking 
operations. [Basel Framework, SRP 31.13]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 7 of 28 
Unclassified / Non classifié 
3.2 Delegation 
 
18. Senior Management may delegate the task for developing IRRBB policies and practices 
to expert individuals or to an asset and liability management committee (ALCO)7. In the case of 
an ALCO, it should meet at a minimum quarterly and include representatives from each major 
department connected to IRRBB. [Basel Framework, SRP 31.14] 
 
19. Senior Management should clearly identify its delegates for managing IRRBB and, to 
avoid potential conflicts of interest, should strive for adequate separation of responsibilities in 
key elements of the risk management process. Institutions should have IRRBB identification, 
measurement, monitoring and control functions with clearly defined responsibilities. Risk 
Management should provide sufficient independent oversight of the Treasury function and report 
IRRBB exposures directly to Senior Management or its delegates. The level of reporting should 
reflect the institution’s nature, size, business, complexity and risk profile. [Basel Framework, 
SRP 31.15] 
 
20. Delegates of Senior Management, who are responsible for managing IRRBB, should 
include individuals with clear lines of authority over the units responsible for establishing and 
managing positions. There should be a clear communication channel to convey the delegates’ 
directives to these line units. [Basel Framework, SRP 31.16] 
 
21. Senior Management should ensure that the institution’s organizational structure enables 
its delegates to carry out their responsibilities, and facilitates effective decision-making and good 
governance. The risk management and strategic planning areas of the institution should also 
communicate regularly to facilitate evaluations of risk arising from future business. [Basel 
Framework, SRP 31.17] 
 
22. OSFI also expects domestic systemically important banks (D-SIBs) to establish a 
committee to oversee asset liability management.  Such committees would be responsible for 
managing and vetting the strategic direction of IRRBB (such as positions and policies) within the 
institution. To the extent that risk management personnel form part of this committee, they are 
expected to be an impartial observer(s) under normal operating conditions and thus not 
participate in tactical decisions regarding IRRBB position taking. 
 
3.3 Internal controls 
 
23. Institutions should have adequate internal controls to ensure the integrity of their IRRBB 
management process and compliance with institution policies. The internal controls should 
promote effective and efficient operations, reliable financial and regulatory reporting, and 
compliance with relevant laws and regulations. [Basel Framework, SRP 31.18]  
 
 
7  While it may delegate tasks or functions, Senior Management should not delegate to functional areas its overall 
responsibility for IRRBB. Senior Management is expected to understand the nature and the level of an 
institution’s IRRBB exposure and the overall policies with respect to IRRBB. It should also approve strategic 
decisions for IRRBB. Furthermore, Senior Management is expected to know how IRRBB is managed and how 
this risk may affect the stability of the institution and the impacts on its performance and operations.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 8 of 28 
Unclassified / Non classifié 
24. With regard to IRRBB control policies and procedures, institutions should have 
appropriate approval processes, exposure limits, reviews and other mechanisms designed to 
provide a reasonable assurance that risk management objectives are being  achieved. [Basel 
Framework, SRP 31.19] 
 
25. In addition, institutions should have suitable routines for ongoing and independent 
evaluations and reviews of their internal control system and risk management processes. This 
includes certifying that personnel comply with established policies and procedures. Such 
reviews should address any recent significant changes that impact the effectiveness of controls 
(including changes in market conditions, personnel, technology and structures of compliance 
with exposure limits), and confirm that escalation procedures for any exceeded limits remain 
appropriate. All such evaluations and reviews should be conducted by individuals and/or units 
that are independent of the function they are assigned to review. When revisions or 
enhancements to internal controls are warranted, institutions should have internal review 
mechanisms in place to promote timely implementation. [Basel Framework, SRP 31.20] 
 
26. OSFI expects institutions to maintain an adequate degree of impartial oversight over 
treasury operations. OSFI recognizes that treasury operations in a number of institutions report to 
finance or another independent control function. In those cases, the institution’s management 
should consider establishing mitigating controls to maintain impartial oversight over treasury 
operations.    
 
27. Institutions’ IRRBB identification, measurement, monitoring and control processes 
should be reviewed by an independent auditing function (such as an internal or external auditor) 
on a regular basis. In such cases, reports written by internal/external auditors or other equivalent 
external parties (such as consultants) should be made available to OSFI upon request. [Basel 
Framework, SRP 31.21] 
 
OSFI Principle #3 (BCBS Principle #3): An institution’s risk appetite for IRRBB should be 
articulated in terms of the risk to both economic value and earnings. Institutions should 
implement policy limits that target maintaining IRRBB exposures consistent with their risk 
appetite. [Basel Framework, SRP 31.4(3)] 
 
28. Institutions should have clearly defined risk appetite statements8 implemented through 
comprehensive risk appetite frameworks, i.e., policies and procedures for limiting and 
controlling IRRBB. The risk appetite framework should delineate delegated powers, lines of 
responsibility and accountability over IRRBB management decisions and should clearly define 
authorized instruments, hedging strategies and risk-taking opportunities. All IRRBB policies 
should be reviewed periodically (at least annually) and revised as needed. [Basel Framework, 
SRP 31.22] 
 
3.4 Policy limits 
 
29. Policy limits should be appropriate to the nature, size, complexity and capital adequacy 
of the institution, as well as its ability to measure and manage its risks. Policy limits should be 
 
8  Refer to the OSFI’s Corporate Governance Guideline for additional guidance in this area.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 9 of 28 
Unclassified / Non classifié 
consistent with the institution’s overall approach for measuring IRRBB. Aggregate risk limits, 
clearly articulating the appropriate amount of IRRBB, should be applied on a consolidated basis 
and, as appropriate, at the level of individual affiliates. Limits may be associated with specific 
scenarios of changes in interest rates and/or term structures, such as an increase or decrease of a 
particular size or a change in shape, and for different currencies. The interest rate movements 
used in developing these limits should represent meaningful shock and stress situations, taking 
into account historical interest rate volatility and the time required by management to mitigate 
those risk exposures (i.e., reflective of the institution’s prospective expectations of interest rate 
volatility and calibrated to historic utilization levels). Material fluctuations in volatility could 
result in breaches of the limits. [Basel Framework, SRP 31.23]   
 
30. Depending on the nature of an institution's activities and business model, sub-limits may 
also be identified for individual business units, portfolios, instrument types or specific 
instruments. The granularity of risk limits should reflect the characteristics of the institution’s 
holdings, including the various sources of the institution’s IRRBB exposures. Institutions with 
significant exposures to gap risk or basis risk or having positions with explicit or embedded 
options should establish risk tolerances appropriate for these risks. [Basel Framework, SRP 
31.24] 
 
31. Senior Management should approve any major hedging or risk-taking initiatives in 
advance of implementation.9 Institutions should develop a dedicated set of risk limits and 
triggers to monitor the evolution of hedging strategies involving derivatives, and to control mark-
to-market risks in instruments that are accounted for at market value. Proposals to use new 
instrument types or new strategies (including hedging) should be assessed to verify activities are 
in line with the institution’s overall risk appetite. Procedures should be established to identify, 
measure, monitor and control applicable risks. [Basel Framework, SRP 31.25] 
 
32. Limits could be absolute in the sense that they should never be exceeded or they may be 
set so that, under specific circumstances, breaches of limits can be tolerated for a predetermined 
short period of time. There should be systems in place to promptly escalate any positions that 
exceed, or are likely to exceed, hard limits defined by Senior Management. There should be a 
clear policy on who will be informed, how the communication will take place and the actions to 
be taken in response to an exception. [Basel Framework, SRP 31.26] 
 
4. Measurement, assumptions, systems integrity and model governance  
 
OSFI Principle #4 (BCBS Principle #4): Measurement of IRRBB should be based on 
outcomes of both economic value and earnings-based measures, arising from a wide and 
appropriate range of interest rate shock and stress scenarios. [Basel Framework, SRP 
31.4(4)] 
 
4.1 Economic value and earnings-based measures 
 
 
9  Positions related to internal risk transfers between the banking book and the trading book should be properly 
documented.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 10 of 28 
Unclassified / Non classifié 
33. Institutions’ internal measurement systems (IMS) should capture all material sources of 
IRRBB and assess the effect of market changes on the scope of their activities. In addition to the 
impact of an interest rate shock on its economic value, an institution’s policy approach should 
consider its ability to generate stable earnings sufficient to maintain its normal business 
operations. [Basel Framework, SRP 31.27] 
 
34. For risk management purposes, institutions should pay attention to the complementary 
nature of economic value and earnings-based measures in their risk and internal capital 
assessments, in particular in terms of:  
a. outcomes: economic value measures compute a change in the net present value of the 
institution’s assets, liabilities and off -balance sheet items subject to specific interest rate 
shock and stress scenarios, while earnings -based measures focus on changes to future 
profitability within a given time horizon eventually affecting future levels of an 
institution’s own equity capital; 
b. assessment horizons : economic value measures reflect changes in value over the 
remaining life of the institution’s assets, liabilities and off -balance sheet items (i.e., until 
all positions have run off), while earnings-based measures cover only the short to medium 
term, and therefore do not fully capture those risks that will continue to impact profit and 
loss accounts beyond the period of estimation; and 
c. future business/production: economic value measures consider the net present value of 
repricing cash flows of instruments on the institution’s balance sheet or accounted for as 
an off-balance sheet item (i.e., a run-off view). Earning measures should be assessed under 
a constant balance sheet assumption. Depending on an institution’s nature, size, business, 
complexity and risk profile, earnings measures may, in addition to assuming a rollover of 
maturing items (i.e., a constant balance sheet),  assess the scenario-consistent impact on 
the institution’s future earnings inclusive of future business (i.e., a dynamic view).10 
[Basel Framework, SRP 31.28] 
 
4.2 Interest rate shock and stress scenarios 
 
35. Institutions’ IMS for IRRBB should be able to calculate the impact on economic value 
and earnings of multiple scenarios, based on: 
a. internally selected interest rate shock scenarios addressing the institution’s risk profile, 
according to its Internal Capital Adequacy Assessment Process (ICAAP)11; 
b. historical, hypothetical, and forward looking interest rate stress scenarios, which tend to 
be more severe than shock scenarios; 
c. the six prescribed interest rate shock scenarios set out in Annex 1; and  
 
10  A dynamic view can be useful for business planning and budgeting purposes. However, dynamic approaches are 
dependent on key variables and assumptions that are extremely difficult to project with accuracy over an 
extended period and can potentially hide certain key underlying risk exposures.  
11  Refer to OSFI’s Internal Capital Adequacy Assessment Process (ICAAP) for Deposit-Taking Institutions 
Guideline.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 11 of 28 
Unclassified / Non classifié 
d. other ad hoc stress scenarios, as required by OSFI, or scenarios in line with OSFI’s 
Macroprudential Stress Testing exercises.  
[Basel Framework, SRP 31.30] 
 
 
4.3 Developing internal interest rate shock and stress scenarios 
 
36. An institution’s stress testing framework for IRRBB should be commensurate with its 
nature, size and complexity as well as business activities and overall risk profile. The framework 
should include clearly defined objectives, scenarios tailored to the institution’s businesses and 
risks, well documented assumptions and sound methodologies. The framework will be used to 
assess the potential impact of the scenarios on the institution’s financial condition, enable 
ongoing and effective review processes for stress tests and recommend actions based on the 
stress test results. IRRBB stress tests should play an important role in the communication of 
risks, both within the institution and externally with supervisors regulators and the market 
through appropriate disclosures. [Basel Framework, SRP 31.33] 
 
4.3.1 Roles and objectives 
 
37. Institutions should measure their vulnerability to loss in value and/or reductions in short-
term earnings under stressful market conditions – including the breakdown of key assumptions – 
and consider those results when establishing and reviewing their policies and limits for IRRBB. 
[Basel Framework, SRP 31.31] 
 
38. The institution’s stress testing framework for IRRBB should be part of its broader risk 
management and governance processes. This should feed into the decision-making process at the 
appropriate management level, including strategic decisions (e.g., business and capital planning 
decisions). In particular, IRRBB stress testing and sensitivity analysis should be considered in 
the ICAAP, requiring institutions to undertake rigorous, forward-looking stress testing that 
identifies events of severe changes in market conditions that could adversely impact the 
institution’s capital or earnings, possibly also through changes in the behaviour of the customer 
base. [Basel Framework, SRP 31.32] 
 
4.3.2 Selection process for shock and stress scenarios 
 
39. The identification of relevant shock and stress scenarios for IRRBB, the application of 
sound modelling approaches and the appropriate use of the stress testing results require 
collaboration. A stress-testing program for IRRBB should consider the opinions of different 
experts within an institution (e.g., traders, the treasury department, the finance department, the 
ALCO, the risk management and risk control departments and/or the institution’s economists).  
[Basel Framework, SRP 31.34] 
 
40. Institutions should determine, by currency and across currencies, a range of potential 
interest rate movements against which they will measure their IRRBB exposures. Senior 
Management should ensure that risk is measured under a reasonable range of potential interest 
rate scenarios, including some containing severe stress elements. In developing the scenarios,

Banks/BHC/T&L Interest Rate Risk Management 
  Page 12 of 28 
Unclassified / Non classifié 
institutions should consider a variety of factors, such as the shape and level of the current term 
structure of interest rates and the historical and implied volatility of interest rates. In low interest 
rate environments, institutions should also consider negative interest rate scenarios and the 
possibility of asymmetrical effects of negative interest rates on their different asset and liability 
profiles. Institutions should evaluate various scenarios regarding how low or negative interest 
rates impact behaviour, products, and hedging. [Basel Framework, SRP 31.35] 
 
41. An institution should consider the nature and sources of its IRRBB exposures, the time 
required to reduce or unwind unfavorable IRRBB exposures, and its capability/willingness to 
withstand accounting losses in order to reposition its risk profile. An institution should select 
scenarios that provide meaningful estimates of risk and include a range of shocks that is 
sufficiently wide to allow Senior Management to understand the risk inherent in the institution’s 
products and activities. When developing interest rate shock and stress scenarios for IRRBB, 
institutions should consider the following: 
a. The scenarios should be sufficiently wide-ranging to identify parallel and non-parallel 
gap risk, basis risk and option risk. In many cases, static interest rate shocks may be 
insufficient to assess IRRBB exposure adequately. Institutions should ensure that the 
scenarios are both severe and plausible, in light of the existing level of interest rates and 
the current interest rate cycle.  
b. Special consideration should be given to instruments or markets where concentrations 
exist, because those positions may be more difficult to liquidate or offset in a stressful 
market environment.  
c. Institutions should assess the possible interaction of IRRBB with its related risks such as 
liquidity and credit risk. The degree and type of assessment should reflect an institution’s 
nature, size, business, complexity and risk profile. 
d. When assessing earnings risks, institutions should determine the effect of adverse 
changes in the spreads of new assets/liabilities replacing those assets/liabilities maturing 
within the time horizon of the forecast on their NII. 
e. Institutions with significant option risk, whether embedded or explicit, should include 
scenarios that capture the exercise of such options. For example, institutions that have 
products with sold caps or floors should include scenarios that assess how the risk 
positions would change should those caps or floors move into the money. Given that the 
market value of options also fluctuates with changes in the volatility of interest rates, 
institutions should develop interest rate assumptions to measure their IRRBB exposures 
to changes in interest rate volatilities. 
f. In building their interest rate shock and stress scenarios, institutions should specify the 
term structure of interest rates that will be incorporated and the basis relationship 
between yield curves, rate indices, etc. Institutions should also estimate how interest rates 
that are administered or managed by delegated expert individuals (e.g., prime rates or 
retail deposit rates, as opposed to those that are purely market-driven) might change. 
Institutions should document how these assumptions are derived.  
[Basel Framework, SRP 31.36]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 13 of 28 
Unclassified / Non classifié 
42. In addition, forward-looking scenarios should incorporate:  
a. changes in portfolio composition due to factors under the control of the institution 
(e.g., the institution’s acquisition and production plans) as well as external factors 
(e.g., changing competitive, legal or tax environments);  
b. new products where only limited historical data are available;  
c. new market information; and  
d. new emerging risks that are not necessarily covered by historical stress episodes.  
[Basel Framework, SRP 31.37] 
 
43. Further, institutions should perform qualitative and quantitative reverse stress tests12 in 
order to:  
a. identify interest rate scenarios that could severely threaten an institution’s capital and 
earnings; and  
b. reveal vulnerabilities arising from its hedging strategies and the potential behavioural 
reactions of its customers.  
 
Institutions should combine forward-looking scenarios with plausible rate shock periods (i.e., 
peer-to-peer lending erodes retail customer base as policy rates sharply change). [Basel 
Framework, SRP 31.38] 
 
OSFI Principle #5 (BCBS Principle #5): In measuring IRRBB, institutions should fully 
understand key behavioural and modelling assumptions. The assumptions should be 
conceptually sound and documented and should be rigorously tested and aligned with the 
institution’s business strategies. [Basel Framework, SRP 31.4(5)] 
 
44. Both economic value and earnings-based measures of IRRBB are significantly affected 
by a number of assumptions made for the purposes of risk quantification, namely: 
a. expectations for the exercise of interest rate options (explicit and embedded) by both the 
institution and its customers under specific interest rate shock and stress scenarios; 
b. treatment of balances and interest flows arising from non-maturity deposits (NMDs); 
c. treatment of own equity in economic value measures; and 
d. the implications of accounting practices for IRRBB.  
[Basel Framework, SRP 31.39] 
 
45. Hence, when assessing its IRRBB exposures, an institution should make judgments and 
assumptions about how an instrument’s actual maturity or repricing behaviour may vary from the 
instrument’s contractual terms because of behavioural optionalities as rates change (i.e., the 
embedded optionality effect). [Basel Framework, SRP 31.40] 
 
46. The degree of sophistication of IRRBB measurement techniques should be commensurate 
with the degree of risk inherent in the institution. Where institutions utilize models to measure 
 
12  See OSFI Guideline E-18: Stress Testing, Section E (Methodology and Scenario Selection) for more information.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 14 of 28 
Unclassified / Non classifié 
and mitigate their IRRBB exposure, these models should be thoroughly vetted by an independent 
function. 
 
4.4 Common products with behavioural optionalities 
 
47. Common products with behavioural optionalities include: 
a. Fixed rate loans subject to prepayment risk – Institutions should understand the nature 
of prepayment risk for their portfolios and make reasonable and prudent estimates of 
the expected prepayments. The assumptions underlying the estimates and where 
prepayment penalties or other contractual features materially affect the embedded 
optionality effect should be documented. There are several factors that are important 
determinants of the institution’s estimate of the effect of each interest rate shock and 
stress scenario on the average prepayment speed. Specifically, an institution should 
assess the expected average prepayment speed under each scenario. 
b. Fixed rate loan commitments – Institutions may sell options to retail customers (e.g., 
prospective mortgage buyers or renewers) whereby, for a limited period, the customers 
can choose to draw down a loan at a committed rate. Unlike loan commitments to 
corporates, where drawdowns strongly reflect characteristics of automatic interest rate 
options, mortgage commitments (i.e., pipelines) to retail customers are also impacted 
by other behavioural drivers.  
c. Term deposits subject to early redemption risk – Institutions may attract deposits with a 
contractual maturity term or with step-up clauses that enable the depositor at different 
time periods to modify the speed of redemption. A classification scheme should be 
documented, whether a term deposit is deemed to be subject to redemption penalties or 
to other contractual features that preserve, or extend, the cash flow profile of the 
instrument13.  
d. NMDs – Behavioural assumptions for deposits that have no specific repricing date are a 
material determinant of IRRBB exposures under the economic value and earnings-
based measures. Institutions should document, monitor and regularly update key 
assumptions for NMD balances and behaviour used in their IMS. To determine the 
appropriate assumptions for its NMDs, an institution should analyse its depositor base 
in order to identify the proportion of core deposits (i.e., NMDs that are unlikely to 
reprice even under significant changes in the interest rate environment). Assumptions 
should vary according to depositor characteristics (e.g., retail/wholesale) and account 
characteristics (e.g., transactional/non-transactional).  
[Basel Framework, SRP 31.41] 
 
 
13  If deemed not material, ‘hardship’ or ‘estate’ redemptions on non-cashable term deposits should not be 
considered as early redemption risk. As such, modeling of this risk would not be expected.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 15 of 28 
Unclassified / Non classifié 
48. Modelling assumptions14 should be conceptually sound and reasonable, and consistent 
with historical experience. They should also take into consideration the nature, size, business, 
complexity and risk profile of an institution. Institutions should carefully consider how the 
exercise of the behavioural optionality will vary not only under the interest rate shock and stress 
scenario but also across other dimensions. For instance, considerations may include: 
 
Product Dimensions influencing the exercise of the embedded behavioural options 
Fixed rate loans 
subject to 
prepayment risk 
Loan size, loan-to-value (LTV) ratio, borrower characteristics, contractual 
interest rates, seasoning, geographical location, original and remaining maturity, 
and other historical factors. 
Other macroeconomic variables such as stock indices, unemployment rates, GDP, 
inflation and housing price indices should be considered in modelling prepayment 
behaviour. 
Fixed rate loan 
commitments 
Borrower characteristics, geographical location (including competitive 
environment and local premium conventions), customer relationship with the 
institution, as evidenced by cross-products, remaining maturity of the 
commitment, seasoning and remaining term of the mortgage. 
Term deposits 
subject to early 
redemption risk 
Deposit size, depositor characteristics, funding channel (e.g., direct or brokered 
deposit), contractual interest rates, seasonal factors, geographical location and 
competitive environment, remaining maturity and other historical factors. 
Other macroeconomic variables such as stock indices, unemployment rates, GDP, 
inflation and housing price indices should be considered in modelling deposit 
redemption behaviour. 
NMDs Responsiveness of product rates to changes in market interest rates, current level 
of interest rates, spread between an institution’s offer rate and market rate, 
competition from other firms, the institution’s geographical location and 
demographic and other relevant characteristics of its customer base.  
[Basel Framework, SRP 31.42] 
 
49. In addition, institutions with positions denominated in different currencies can expose 
themselves to IRRBB in each of those currencies. Since yield curves vary from currency to 
currency, institutions should assess exposures in each currency and have sufficient controls to 
manage the risk in each of those currencies independently. Institutions with material 
multicurrency exposures may choose to include, in their IMS, methods to aggregate their IRRBB 
in different currencies using assumptions about the correlation between interest rates in different 
currencies. OSFI may exercise discretion in terms of allowing or restricting methods to aggregate 
institutions’ IRRBB in different currencies. For example, OSFI may request that institutions 
report exposures in different currencies either without or with different assumptions about the 
correlation between interest rates. [Basel Framework, SRP 31.43] 
 
50. Further, institutions should consider the materiality of the impact of behavioural 
optionalities within floating rate loans. For instance, the behaviour of prepayments arising from 
 
14  Institutions should subject all material behavioural assumptions to modeling. Institutions should also conduct due 
diligence and periodic reviews to determine and confirm materiality.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 16 of 28 
Unclassified / Non classifié 
embedded caps and floors could impact the institutions’ economic value of equity. [Basel 
Framework, SRP 31.44] 
 
51. Institutions should be able to test the appropriateness of key behavioural assumptions, 
and all changes to the assumptions of key parameters should be documented. Institutions should 
periodically perform sensitivity analyses for key assumptions to monitor their impact on 
measured IRRBB. Sensitivity analyses should be performed with reference to both economic 
value and earnings-based measures. [Basel Framework, SRP 31.45] 
 
52. The most significant assumptions underlying the system should be documented and 
clearly understood by Senior Management. Documentation should also include descriptions on 
how those assumptions could potentially affect the institution’s hedging strategies. [Basel 
Framework, SRP 31.46] 
 
53. As market conditions, competitive environments and strategies change over time, the 
institution should review significant measurement assumptions at least annually and more 
frequently during rapidly changing market conditions. For example, if the competitive market 
has changed such that consumers now have lower transaction costs available to them for 
refinancing their residential mortgages, prepayments may become more sensitive to smaller 
reductions in interest rates. Institutions are expected to undertake full reviews of their IRRBB 
measurement models consistent with OSFI’s guideline E-23 Enterprise-Wide Model Risk 
Management for Deposit-Taking Institutions. The frequency and the nature of these reviews 
depends on various factors, such as complexity of the institution and size of IRRBB exposures, 
market changes, and complexity of innovation with respect to measuring IRRBB. [Basel 
Framework, SRP 31.47] 
 
 
OSFI Principle #6 (BCBS Principle #6): Measurement systems and models used for IRRBB 
should be based on accurate data, and subject to appropriate documentation, testing and 
controls to give assurance on the accuracy of calculations. Models used to measure IRRBB 
should be comprehensive and covered by governance processes for model risk 
management, including a validation function that is independent of the development 
process. [Basel Framework, SRP 31.4(6)] 
 
4.5 Measurement systems and data integrity 
 
54. Accurate and timely measurement of IRRBB is necessary for effective risk management 
and control. An institution’s risk measurement system should be able to identify and quantify the 
major sources of IRRBB exposure. The mix of an institution’s business lines and the risk 
characteristics of its activities should guide management’s selection of the most appropriate form 
of measurement system. [Basel Framework, SRP 31.48] 
 
55. Institutions should not rely on a single measure of risk, given that risk management 
systems tend to vary in how they capture the components of IRRBB. Instead, institutions should 
use a variety of methodologies to quantify their IRRBB exposures under both the economic 
value and earnings-based measures, ranging from simple calculations based on static simulations

Banks/BHC/T&L Interest Rate Risk Management 
  Page 17 of 28 
Unclassified / Non classifié 
using current holdings to more sophisticated dynamic modelling techniques that reflect potential 
future business activities. [Basel Framework, SRP 31.49] 
 
56. An institution’s MIS should allow it to retrieve accurate IRRBB information in a timely 
manner. The MIS should capture interest rate risk data on all the institution’s material IRRBB 
exposures. There should be sufficient documentation of the major data sources used in the 
institution’s risk measurement process. [Basel Framework, SRP 31.50] 
 
57. Data inputs should be automated as much as possible to reduce operational errors. Data 
mapping should be periodically reviewed and tested against an approved model version. An 
institution should monitor the type of data extracts and set appropriate controls. [Basel 
Framework, SRP 31.51] 
 
58. Where cash flows are slotted into different time buckets (e.g., for gap analyses) or 
assigned to different vertex points to reflect the different tenors of the interest rate curve, the 
slotting criteria should be stable over time to allow for a meaningful comparison of risk figures 
over different periods. [Basel Framework, SRP 31.52] 
 
59. Institutions’ IMS should be able to compute economic value and earnings-based 
measures of IRRBB, as well as other measures of IRRBB prescribed by OSFI based on the 
interest rate shock and stress scenarios set defined. It should also be sufficiently flexible to 
incorporate supervisory-imposed constraints15 on institutions’ internal risk parameter estimates. 
[Basel Framework, SRP 31.53] 
 
4.6 Model governance process 
 
60. The validation of IRRBB measurement methods and assessment of corresponding model 
risk should be included in a formal policy process that should be reviewed and approved by 
Senior Management. The policy should specify the management roles and designate who is 
responsible for the development, implementation and use of models16. In addition, the model 
oversight responsibilities as well as policies including the development of initial and ongoing 
validation procedures, evaluation of results, approval, version control, exception, escalation, 
modification and decommission processes need to be specified and integrated within the 
governance processes for model risk management. [Basel Framework, SRP 31.54] 
 
61. An effective validation framework should include three core elements: 
a. evaluation of conceptual/methodological soundness, including developmental 
evidence; 
b. ongoing model monitoring, including process verification and benchmarking; and 
c. outcomes analysis, including backtesting of key internal parameters (e.g., stability of 
deposits, prepayments, early redemptions, pricing of instruments). 
 
15  Examples of supervisory constraints include changes in modeling assumptions or sensitivities of assumptions.  
16  For additional details about the model governance process, please refer to OSFI’s Guideline E-23 Enterprise-
Wide Model Risk Management for Deposit-Taking Institutions

Banks/BHC/T&L Interest Rate Risk Management 
  Page 18 of 28 
Unclassified / Non classifié 
[Basel Framework, SRP 31.55] 
 
62. In addressing the expected initial and ongoing validation activities, the policy should 
establish a hierarchical process for determining model risk soundness based on both quantitative 
and qualitative dimensions such as size, impact, past performance and familiarity with the 
modelling technique employed. [Basel Framework, SRP 31.56] 
 
63. Model risk management for IRRBB measures should follow a holistic approach that 
begins with motivation, development and implementation by model owners and users. Prior to 
receiving authorization for usage, the process for determining model inputs, assumptions, 
modelling methodologies and outputs should be reviewed and validated independently of the 
development of IRRBB models. The review and validation results and any recommendations on 
model usage should be presented to and approved by Senior Management. Upon approval, the 
model should be subject to ongoing review, process verification and validation at a frequency 
that is consistent with the level of model risk appetite determined and approved by the 
institution. [Basel Framework, SRP 31.57] 
 
64. The ongoing validation process should, where appropriate, establish a set of exception 
trigger events that obligate the model reviewers to notify Senior Management or its delegates in 
a timely fashion, in order to determine corrective actions and/or restrictions on model usage. 
Clear version control authorizations should be designated, where appropriate, to model owners. 
With the passage of time, an approved model may be modified or decommissioned. Institutions 
should articulate policies for model transition, including change and version control 
authorizations and documentation. [Basel Framework, SRP 31.58] 
 
65. IRRBB models might include those developed by third-party vendors. Model inputs or 
assumptions may also be sourced from related modelling processes or sub-models (both in-house 
and vendor-sourced) and should be included in the validation process. Institutions should 
document and explain model specification choices as part of the validation process. [Basel 
Framework, SRP 31.59] 
 
66. Institutions that purchase IRRBB models should ensure there is adequate documentation 
of their use of those models, including any specific customization. If vendors provide input for 
market data, behavioural assumptions or model settings, the institution should have a process in 
place to determine if those inputs are reasonable for its business and the risk characteristics of its 
activities. [Basel Framework, SRP 31.60] 
 
67. Internal audit should review the risk management system and the model risk management 
process as part of its annual risk assessment and audit plans. The audit activity should not 
duplicate model risk management processes, but should review its integrity and effectiveness. 
[Basel Framework, SRP 31.61] 
 
OSFI Principle #7 (BCBS Principle #7): Measurement outcomes of IRRBB and hedging 
strategies should be reported to Senior Management or its delegates on a regular basis, at 
relevant levels of aggregation (by consolidation level and currency). [Basel Framework, 
SRP 31.4(7)]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 19 of 28 
Unclassified / Non classifié 
 
68. The reporting of risk measures to the Senior Management or its delegates should occur on 
a frequent basis consistent with the timing of ALCO meetings. Such reporting should compare 
current IRRBB exposures with policy limits as well as past IRRBB forecasts or risk estimates 
with actual results (i.e. earnings) to inform potential modelling shortcomings. Reporting should 
also include the results of the periodic model reviews and audits on a similar frequency. 
Portfolios that may be subject to significant mark-to-market movements should be clearly 
identified within the institution’s MIS and subject to oversight in line with any other portfolios 
exposed to market risk. [Basel Framework, SRP 31.62] 
 
69. The types of reports prepared for the Senior Management will vary based on the 
institution’s portfolio composition but they should include at least the following: 
a. summaries of the institution’s aggregate IRRBB exposures, and explanatory text that 
highlights the assets, liabilities, cash flows, and strategies (including hedging program 
activities) that are driving the level and direction of IRRBB; 
b. reports demonstrating the institution’s compliance with policies and limits; 
c. key modelling assumptions such as NMD characteristics, prepayments on fixed rate loans 
and currency aggregation; 
d. results of stress tests, including assessment of sensitivity to key assumptions and 
parameters; and 
e. summaries of the reviews of IRRBB policies, procedures and adequacy of the 
measurement systems, including any findings of internal and external auditors and/or 
other equivalent external parties (such as consultants). 
[Basel Framework, SRP 31.63] 
 
70. Reports detailing the institution’s IRRBB exposures should be provided to the 
institution’s Senior Management on a timely basis and reviewed regularly. The IRRBB reports 
should provide aggregate information as well as sufficient supporting detail to enable Senior 
Management to assess the sensitivity of the institution to changes in market conditions, with 
particular reference to portfolios that may potentially be subject to significant mark-to-market 
movements. Senior Management should review the institution’s IRRBB management policies 
and procedures in light of the reports, to ensure that they remain appropriate and sound. Senior 
Management should also ensure that analysis and risk management activities related to IRRBB 
are conducted by competent staff with technical knowledge and experience, consistent with the 
nature and scope of the institution’s activities. [Basel Framework, SRP 31.64] 
 
 
5. Public Disclosure 
 
OSFI Principle #8 (BCBS Principle #8): Information on the level of IRRBB exposure and 
practices for measuring and controlling IRRBB should be disclosed to the public on a 
regular basis. [Basel Framework, SRP 31.4(8)]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 20 of 28 
Unclassified / Non classifié 
71. Refer to OSFI Pillar 3 Disclosure Expectations for additional guidance on public 
disclosures17. [Basel Framework, SRP 31.65] 
 
 
6. Capital adequacy and outlier test 
 
OSFI Principle #9 (BCBS Principle #9): Capital adequacy for IRRBB should be specifically 
considered as part of the Internal Capital Adequacy Assessment Process and approved by 
Senior Management, in line with the institution’s risk appetite on IRRBB. [Basel 
Framework, SRP 31.4(9)] 
 
72. Institutions are responsible for evaluating the level of capital that they should hold, and 
for ensuring that this is sufficient to cover IRRBB and its related risks. The contribution of 
IRRBB to the overall internal capital assessment should be based on the institution’s IMS 
outputs, taking account of key assumptions and risk limits. The overall level of capital should be 
commensurate with both the institution’s actual measured level of risk (including for IRRBB) 
and its risk appetite, and be duly documented in its ICAAP report. [Basel Framework, SRP 
31.66] 
 
73. Institutions should not only rely on supervisory assessments of capital adequacy for 
IRRBB, but should also develop their own methodologies for capital allocation, based on their 
risk appetite. In determining the appropriate level of capital, institutions should consider both the 
amount and the quality of capital needed. [Basel Framework, SRP 31.67] 
 
74. Capital adequacy for IRBBB should be considered in relation to the risks to economic 
value, given that such risks are embedded in the institution’s assets, liabilities and off-balance 
sheet items. Given the possibility that future earnings may be lower than expected, institutions 
should consider capital buffers to address any risks to future earnings.  
[Basel Framework, SRP 31.68] 
 
75. Capital adequacy assessments for IRRBB should factor in: 
a. the size and tenor of internal limits on IRRBB exposures, and whether these limits are 
reached at the point of capital calculation; 
b. the effectiveness and expected cost of hedging open positions that are intended to 
take advantage of internal expectations of the future level of interest rates; 
c. the sensitivity of the internal measures of IRRBB to key modelling assumptions; 
d. the impact of shock and stress scenarios on positions priced off different interest rate 
indices (basis risk); 
e. the impact on economic value and NII of mismatched positions in different 
currencies;  
f. the impact of embedded losses; 
 
17 Refer to the Pillar 3 Disclosure Guideline for Domestic Systemically Important Banks (D-SIBs) (2025) and the 
Pillar 3 Disclosure Guideline for Small and Medium-Sized Deposit-Taking Institutions (SMSBs) (2025).

Banks/BHC/T&L Interest Rate Risk Management 
  Page 21 of 28 
Unclassified / Non classifié 
g. the distribution of capital relative to risks across legal entities that form part of a 
capital consolidation group, in addition to the adequacy of overall capital on a 
consolidated basis; 
h. the drivers of the underlying risk; and 
i. the circumstances under which the risk might crystallise. 
[Basel Framework, SRP 31.69] 
 
 
76. The outcomes of the capital adequacy for IRRBB should be considered in an institution’s 
ICAAP and flow through to assessments of capital associated with business lines. [Basel 
Framework, SRP 31.70] 
 
OSFI Principle #10 (BCBS Principle #11): OSFI will regularly assess institutions’ IRRBB 
and the effectiveness of the approaches that institutions use to identify, measure, monitor 
and control IRRBB. [Basel Framework, SRP 31.4(11)] 
 
6.1 Assessment 
 
77. Taking into account an institution’s size and complexity at the time of assessment, OSFI 
will: 
a. collect sufficient information from institutions to assess their IRRBB exposure18. 
b. regularly evaluate the adequacy, integrity and effectiveness of an institution’s IRRBB 
management framework and assess whether its practices comply with the stated 
objectives and risk tolerances set by Senior Management, and with its expectations as set 
out in Principles 1 to 7.  
c. evaluate whether an institution’s IMS provides a sufficient basis for identifying and 
measuring IRRBB, taking note particularly of the key assumptions that affect the 
measurement of IRRBB. OSFI may request and evaluate information about significant 
model or policy changes that have occurred between its regular reviews and may 
concentrate its efforts on reviewing the most material models and policies. 
d. review regularly the outputs from the institution’s IMS, including the institution’s IRRBB 
exposures (both economic value and earnings-based measures) based on the internal 
calculations using at least the prescribed interest rate shock scenarios specified in 
Annex 1, as well as any additional interest rate shock and stress scenarios it determines 
should be assessed. OSFI may also form its evaluation of an institution’s IMS by 
applying supervisory estimates which has developed and will also review the information 
disclosed by institutions under Principle 8.  
[Basel Framework, SRP 31.74 to SRP 31.76] 
 
 
18  A limited and not necessarily exhaustive example of information that OSFI may collect is reflected under the 
BCBS Principle #10. For example, OSFI may collect information on the modelling of NMDs; the impact of 
assumptions used regarding product with optionalities; economic value and earnings-based measures for interest 
rate shock and stress scenarios in addition to those prescribed in Annex 1; etc.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 22 of 28 
Unclassified / Non classifié 
 
 
78. When reviewing the institution’s IRRBB exposures and forming conclusions about the 
quality of the institution’s IRRBB management, OSFI will consider: 
a. the complexity and level of risk posed by the institution’s assets, liabilities and off-
balance sheet activities; 
b. the adequacy and effectiveness of oversight by the institution’s Senior Management; 
c. an institution’s knowledge and ability to identify and manage the sources of IRRBB; 
d. the adequacy of internal validation of IRRBB measures, including sensitivity analysis and 
backtesting, in particular where changes in key modelling parameters have occurred; 
e. the adequacy of internal monitoring and of the institution’s MIS; 
f. the effectiveness of risk limits and controls that set tolerances on economic value and 
earnings; 
g. the effectiveness of the institution’s IRRBB stress testing programme; 
h. the adequacy and frequency of the internal review and audit of the IRRBB management 
process, including independent model validation and oversight of model risk; 
i. the adequacy and effectiveness of IRRBB management practices as evidenced by past 
and projected financial performance; 
j. the effectiveness of hedging strategies used by the institution to control IRRBB; and 
k. the appropriateness of the level of IRRBB (including embedded losses) in relation to the 
institution’s capital, earnings and risk management systems. 
[Basel Framework, SRP 31.77] 
 
79. OSFI will assess the adequacy of an institution’s capital relative to its IRRBB exposures 
(against expectations set out in Principle 9) to determine whether the institution requires more 
detailed examination and should potentially be subject to additional capital requirements and/or 
other mitigation actions. This assessment may exceed the capital prescription from the 
outlier/materiality test set out in Principle 11. [Basel Framework, SRP 31.78] 
 
80. OSFI’s evaluation could be undertaken both on a standalone basis and by making 
comparisons with peer institutions. In particular, OSFI may compare the key behavioural and 
strategic assumptions being made by institution to determine whether they can be justified with 
regard to the economic environment and business model. OSFI will ensure that both information 
and the review process is comparable and consistent across institutions. [Basel Framework, SRP 
31.79]  
 
OSFI Principle #11 (BCBS Principle #12): Institutions identified as outliers are considered 
as potentially having undue IRRBB. When a review of an institution’s IRRBB exposure 
reveals inadequate management or excessive risk relative to capital, earnings or general 
risk profile, OSFI will require mitigation actions and/or additional capital. [Basel 
Framework, SRP 31.4(12)]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 23 of 28 
Unclassified / Non classifié 
6.2 Outlier Test 
 
81. The outlier/materiality test compares an institution’s maximum ∆EVE (economic value 
of equity), under the six prescribed interest rate shock scenarios set out in Annex 1, with 15% of 
its Tier 1 capital. [Basel Framework, SRP 31.82]  
 
82. If deemed necessary, OSFI could also implement additional outlier/materiality tests that 
use a different capital measure instead of Tier 1 (e.g. CET1) or capture the institution’s IRRBB 
relative to earnings. For example, an institution could be considered to have potentially undue 
IRRBB relative to earnings if its shocked ΔNII was such that the institution would not have 
sufficient income to maintain its normal business operations. [Basel Framework, SRP 31.83, 
SRP 31.87]  
 
83. Institutions are expected to hold adequate capital for the risks they undertake. With 
regard to IRRBB, OSFI will evaluate whether the institutions have adequate capital and earnings 
that are commensurate with its level of short-term and long-term IRRBB exposures, as well as 
the risk those exposures may pose to its future financial performance. The following factors will 
be considered by OSFI: 
a. The ΔEVE under a variety of shocked and stressed interest rate scenarios. Where an 
institution’s EVE is significantly sensitive to interest rate shocks and stresses, OSFI will 
evaluate the impact on its capital levels arising from financial instruments held at market 
value, and potential impact should banking book positions held at historical cost become 
subject to market valuation. Throughout the assessment, OSFI will consider the impact of 
key assumptions on the ΔEVE calculated, including those related to the inclusion/ 
exclusion of commercial margins, the institution’s actual equity allocation profile, the 
stability of NMDs and prepayment optionality. 
b. The strength and stability of the earnings stream and the level of income needed to 
generate and maintain normal business operations. A high level of IRRBB exposure is 
one that could, under a plausible range of market scenarios, result in the institution 
reporting losses or curtailing normal dividend distribution and business operations. In 
such cases, senior management should ensure that the institution has sufficient capital to 
withstand the adverse impact of such events until it can implement mitigating actions 
such as reducing exposures or increasing capital. 
[Basel Framework, SRP 31.85] 
 
84. When OSFI concludes that an institution’s management of IRRBB is inadequate, OSFI 
will require the institution to take one or more of the following actions: 
• reduce its IRRBB exposures (e.g., by hedging); 
• raise additional capital; 
• set constraints on the internal risk parameters used by an institution; and/or 
• improve its risk management framework. 
[Basel Framework, SRP 31.88]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 24 of 28 
Unclassified / Non classifié 
85. The reduction in IRRBB and/or the expected higher level of capital should be achieved 
within a specified time frame, to be established taking into consideration prevailing financial and 
economic conditions, as well as the causes of the IRRBB exposure exceeding the supervisory 
threshold and its structural nature. [Basel Framework, SRP 31.89]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 25 of 28 
Unclassified / Non classifié 
Annex 1. The standardized interest rate shock scenarios 
 
1. Institutions should apply six prescribed interest rate shock scenarios to capture parallel 
and non-parallel gap risks for EVE and two prescribed interest rate shock scenarios for NII. 
These scenarios are applied to IRRBB exposures in each currency for which the institution has 
material positions. In order to accommodate heterogeneous economic environments across 
jurisdictions, the six shock scenarios reflect currency-specific absolute shocks as specified in the 
below Table 1. For the purposes of capturing the local rate environment, an historical time series 
ranging from January 2000 to December 2023 for various maturities was used to derive each 
scenario for a given currency.  
 
2. Under this approach, IRRBB is measured by means of the following six scenarios:  
a. parallel shock up;  
b. parallel shock down; 
c. steepener shock (short rates down and long rates up); 
d. flattener shock (short rates up and long rates down); 
e. short rates shock up; and 
f. short rates shock down. 
 
Table 1. Specified size of interest rate shocks 𝑺̅𝒔𝒉𝒐𝒄𝒌𝒕𝒚𝒑𝒆,𝒄 
 ARS AUD BRL CAD CHF CNY EUR GBP HKD IDR INR 
Parallel 400 350 400 200 175 225 225 275 225 400 325 
Short 500 425 500 275 250 300 350 425 375 500 475 
Long 300 300 300 175 200 150 200 250 200 300 225 
 
 JPY KRW MXN RUB SAR SEK SGD TRY USD ZAR 
Parallel 100 225 400 400 275 275 175 400 200 325 
Short 100 350 500 500 375 425 250 500 300 500 
Long 100 225 200 300 250 200 225 300 225 300 
[Basel Framework, SRP 31.90] 
 
3. Given Table 1, the instantaneous shocks to the risk-free rate for parallel, short and long, 
for each currency, the following parameterisations of the six interest rate shock scenarios should 
be applied: 
 
a. Parallel shock for currency c: a constant parallel shock up or down across all time 
buckets. 
∆𝑆𝑝𝑎𝑟𝑎𝑙𝑙𝑒𝑙,𝑐(𝑡𝑘) = ± 𝑆̅𝑝𝑎𝑟𝑎𝑙𝑙𝑒𝑙,𝑐

Banks/BHC/T&L Interest Rate Risk Management 
  Page 26 of 28 
Unclassified / Non classifié 
b. Short rate shock for currency c: shock up or down that is greatest at the shortest tenor 
midpoint. That shock, through the shaping scalar 𝛼𝑠ℎ𝑜𝑟𝑡(𝑡𝑘) = 𝑒
−𝑡𝑘
𝑥  , where x=4, 
diminishes towards zero at the tenor of the longest point in the term structure.19, 20   
 
∆𝑆𝑠ℎ𝑜𝑟𝑡,𝑐(𝑡𝑘) = ± 𝑆̅𝑠ℎ𝑜𝑟𝑡,𝑐  ∙  𝛼𝑠ℎ𝑜𝑟𝑡(𝑡𝑘) = ± 𝑆̅𝑠ℎ𝑜𝑟𝑡,𝑐 ∙ 𝑒
−𝑡k
𝑥  
 
c. Long rate shock for currency c (note: this is used only in the rotational shocks): Here 
the shock is greatest at the longest tenor midpoint and is related to the short scaling 
factor as:  
𝛼𝑙𝑜𝑛𝑔(𝑡𝑘) = 1 − 𝛼𝑠ℎ𝑜𝑟𝑡(𝑡𝑘). 
∆𝑆𝑙𝑜𝑛𝑔,𝑐(𝑡𝑘) = ± 𝑆̅𝑙𝑜𝑛𝑔,𝑐 ∙ 𝛼𝑙𝑜𝑛𝑔(𝑡𝑘) = ± 𝑆̅𝑙𝑜𝑛𝑔,𝑐 ∙ (1 − 𝑒
−𝑡k
𝑥 ) 
 
d. Rotation shocks for currency c: involving rotations to the term structure (i.e., steepeners 
and flatteners) of the interest rates whereby both the long and short rates are shocked 
and the shift in interest rates at each tenor midpoint is obtained by applying the 
following formulas to those shocks: 
 
∆𝑆𝑠𝑡𝑒𝑒𝑝𝑒𝑛𝑒𝑟,𝑐(𝑡𝑘) = − 0.65 ∙ ∣ ∆𝑆𝑠ℎ𝑜𝑟𝑡,𝑐(𝑡𝑘) ∣ +0.9 ∙ ∣ ∆𝑆𝑙𝑜𝑛𝑔,𝑐(𝑡𝑘) ∣. 
 
∆𝑆𝑓𝑙𝑎𝑡𝑡𝑒𝑛𝑒𝑟,𝑐(𝑡𝑘) = +0.8 ∙ ∣ ∆𝑆𝑠ℎ𝑜𝑟𝑡,𝑐(𝑡𝑘)  ∣ −0.6 ∙ ∣ ∆𝑆𝑙𝑜𝑛𝑔,𝑐(𝑡𝑘) ∣. 
 
[Basel Framework, SRP 31.91] 
 
4. The following examples illustrate the scenarios in the above sub-paragraphs (b) and (d):    
 
Short rate shock: Assume that the institution uses the standardised framework21 with K=19 time 
bands and with tK=25 years (the midpoint (in time) of the longest tenor bucket K), and where 𝑡𝑘 
is the midpoint (in time) for bucket k. In the standardised framework, if k=10 with tk=3.5 years, 
the scalar adjustment for the short shock would be 𝛼𝑠ℎ𝑜𝑟𝑡(𝑡𝑘) = (𝑒
−3.5
4 ) = 0.417. Institutions 
would multiply this by the value of the short rate shock to obtain the amount to be added to or 
subtracted from the yield curve at that tenor point. If the short rate shock was +100 bp, the 
increase in the yield curve at tk=3.5 years would be 41.7 bp. 
 
Steepener: Assume the same point on the yield curve as above, tk=3.5 years. If the absolute value 
of the short rate shock was 100 bp and the absolute value of the long rate shock was 100 bp (as 
for the Japanese yen), the change in the yield curve at tk=3.5 years would be the sum of the effect 
 
19  The value of x in the denominator of the function 𝑒
−𝑡k
𝑥  controls the rate of decay of the shock. This should be set 
to the value of 4 for most currencies and the related shocks unless otherwise determined by OSFI.     
20  tk is the midpoint (in time) of the kth bucket and tk is the midpoint (in time) of the last bucket K. There are 19 
buckets in the standardised framework, but the analysis may be generalised to any number of buckets. 
21  Refer to the BCBS’s standardized framework described in paragraphs 31.94 to 31.129 of SRP31 - Interest rate 
risk in the banking book.

Banks/BHC/T&L Interest Rate Risk Management 
  Page 27 of 28 
Unclassified / Non classifié 
of the short rate shock plus the effect of the long rate shock in basis points: − 0.65 ∙  100bp ∙
0.417 + 0.9 ∙  100bp ∙ (1 − 0.417) =  +25.4bp. 
 
Flattener: The corresponding change in the yield curve for the shocks in the example above at 
tk=3.5 years would be: + 0.8 ∙  100bp ∙ 0.417 − 0.6 ∙  100bp ∙ (1 − 0.417) =  −1.6bp. 
[Basel Framework, SRP 31.92] 
 
 
Derivation of the interest rate shocks in Table 1 
 
5. The above section describes the six prescribed interest rate shock scenarios that 
institutions should apply to parallel and non-parallel gap risks for EVE and two prescribed 
interest rate shock scenarios for NII. In order to derive the shocks described in Table 1, the 
following general steps are taken. [Basel Framework, SRP 98.56] 
 
6. Step 1: Generate a time series of daily interest rates 𝑅𝑘,𝑐 from the year 2000 (3 January 
2000) to 2023 (29 December 2023) in the time buckets k = 3m, 6m, 1Y, 2Y, 5Y, 7Y, 10Y, 15Y 
and 20Y for each currency c. [Basel Framework, SRP 98.57]    
 
7. Step 2: Using the time series of the interest rate levels at each tenor point k and for each 
currency c, calculate a new time series of rate changes 𝛥𝑅𝑘,𝑐 for a moving time window of h = 6 
months (125 days). 
 
𝛥𝑅𝑘,𝑐(𝑡) = 𝑅𝑘,𝑐(𝑡) − 𝑅𝑘,𝑐(𝑡 − ℎ) 
 
[Basel Framework, SRP 98.58]    
 
8. Step 3. For each scenario i and currency c, take the average of the rate changes across the 
corresponding time buckets in the below table, where 𝑁𝑖 represents the number of time buckets. 
 
𝛥𝑅𝑖,𝑐(𝑡) = 1
𝑁𝑖
∑ 𝛥𝑅𝑘,𝑐(𝑡)
𝑘
 
 
Average interest rate change by time bucket  
Scenario Averaged interest rate 
series 
Time buckets 
Parallel 
( ) ,parallel cRt  3m, 6m, 1Y, 2Y, 5Y, 7Y, 
10Y, 15Y, 20Y 
Short rate 
( ) ,short cRt  3m, 6m, 1Y 
Long rate 
( ) ,long cRt  10Y, 15Y, 20Y 
 
[Basel Framework, SRP 98.59]

Banks/BHC/T&L Interest Rate Risk Management 
  Page 28 of 28 
Unclassified / Non classifié 
 
9. Step 4. Use the 99.9th percentile value of the absolute value of 𝛥𝑅𝑖,𝑐 over the period from 
2000 to 2023, denoted |𝛥𝑅𝑖,𝑐(𝑡)|, for the interest rate shock of scenario 𝑖 for currency c. 
𝑆𝑖,𝑐 = 𝑃99.9(|𝛥𝑅𝑖,𝑐(𝑡)|) 
[Basel Framework, SRP 98.60]    
 
10. Step 5. In order to ensure a minimum level of prudence and a level playing field, set a floor 
of 100 bp and variable caps (denoted as 
iC ) for the scenarios concerned, those caps being 500 bp 
for the short-term, 400 bp for the parallel and 300 bp for the long-term interest rate shock scenario. 
The change in the interest rate shock for scenario i and currency c can be defined as: 
𝑆̄𝑖,𝑐 = 𝑚𝑎𝑥{100, 𝑚𝑖𝑛{𝑆𝑖,𝑐, 𝐶̄𝑖}} 
 
where 
iC = {400, 500, 300}, for i = parallel, short, and long, respectively. 
[Basel Framework, SRP 98.61]    
 
11. Finally, round the values from step 5 to the nearest multiple of 25 bp. This methodology 
results in the specified interest rate shocks set out in Table 1. 
[Basel Framework, SRP 98.62]    
 
 
Recalibrations over time 
 
12. OSFI may, applying national discretion, set a higher floor under the local interest rate 
shock scenarios for the home currency, or a higher cap, resulting in more conservative shocks.  
Specifically, OSFI has set a negative lower bound for the post-shock interest rates 
,jcR at 75 bp, 
where j represents the six interest rate shock scenarios set out in the above paragraph 3: 
𝑅̄𝑗, 𝑐(𝑡𝑘) = 𝑚𝑎𝑥(𝑅̄ 0, 𝑐(𝑡𝑘) + 𝛥𝑆̄𝑗, 𝑐(𝑡𝑘), −75 𝑏𝑝) 
 
13. OSFI will look to update Table 1 on a periodic basis, reflecting changes from other 
jurisdictions and/or CAD currency rates. Should the extent of the rate scenarios change 
materially, OSFI may review the outlier test threshold.  
  
14. For currencies not covered above, where an institution has a material position, the 
institution may estimate shocks using a methodology that is consistent with the one described in 
this annex.  
 
[Basel Framework, SRP 31.93 and SRP 98.63]