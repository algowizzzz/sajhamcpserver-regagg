---
title: "f921603e b85a 48fb b76b 049fbcd516de en"
regulator: "eiopa"
doc_type: "announcement"
status: "final"
source_kind: "policy_pdf"
source_url: "https://www.eiopa.europa.eu/document/download/f921603e-b85a-48fb-b76b-049fbcd516de_en?filename=Technical%20documentation%20of%20the%20methodology%20to%20derive%20EIOPA%E2%80%99s%20RFR%20term%20structures.pdf"
version: "1"
---

EIOPA – Westhafen Tower, Westhafenplatz 1 - 60327 Frankfurt – Germany - Tel. + 49 69-951119-20; 
Fax. + 49 69-951119-19; email: info@eiopa.europa.eu site: www.eiopa.europa.eu 
 
 
 
   
 
EIOPA-BoS-15/035 
31 January 2018 
 
 
 
 
  
Technical documentation  
of the methodology to derive EIOPA’s 
risk-free interest rate term structures 
 
 
 
EIOPA has changed the methodology to calculate the risk-free interest rate term 
structures as follows: 
The ticker for Swiss franc OIS rates was replaced. The change is implemented on 
page 33. 
 
Furthermore the description of the derivation of the UFR was updated in 
accordance with earlier announcements 1 and clarifications were included with 
regard to t he treatment of Icelandic government bonds (page 24) and the 
calculation of the long-term average spread (page 68).   
                                       
1https://eiopa.europa.eu/Publications/Reports/Specification%20of%20the%20methodology%20to%20derive%
20the%20UFR.pdf

2/131 
 
Table of contents 
Letter of the Executive Director .......................................................... 6 
Legal Notice ..................................................................................... 9 
Legal basis ..................................................................................... 11 
1. Basis for decision .................................................................... 12 
1.A. General issues ...................................................................... 12 
1.B. Basic risk-free interest rates term structure ............................. 14 
1.C. Volatility adjustment (VA) and Matching adjustment (MA) ......... 15 
2. Governance and controls of the process of calculation and publication
  ............................................................................................. 19 
3. Data sources for the inputs from financial markets ...................... 21 
3.A. Financial market data providers .............................................. 21 
3.B. Selection of the relevant currencies ........................................ 21 
3.C. Selection of market rates ....................................................... 22 
Basic risk-free interest rate term structure ........................................... 25 
4. Identification of relevant financial instruments and assessment of 
depth, liquidity and transparency ...................................................... 25 
4.A. Introduction ......................................................................... 25 
4.B. Conceptual framework for EEA currencies ................................ 25 
4.C. Conceptual framework for non-EEA currencies ......................... 28 
4.D. Update of the DLT assessment ............................................... 30 
4.E. Currencies without DLT financial instruments ........................... 30 
5. Credit risk adjustment ............................................................. 31 
5.A. Legal framework ................................................................... 31 
5.B. Application of the adjustment ................................................. 31 
5.C. Calculation of the credit risk adjustment .................................. 31 
5.D. Data sources for the credit risk adjustment .............................. 33 
6. Currency risk adjustment for currencies pegged to the euro ......... 34 
6.A. Legal framework ................................................................... 34 
6.B. Application of the adjustment ................................................. 34 
6.C. Calculation of the adjustment ................................................. 34 
6.D. Update of the adjustment ...................................................... 36 
7. Extrapolation and interpolation ................................................. 37 
7.A. Extrapolation and interpolation method ................................... 37

3/131 
 
7.B. Last liquid point .................................................................... 37 
7.C. Ultimate forward rate ............................................................ 39 
7.D. Convergence point and tolerance ............................................ 39 
7.E. Description of the Smith-Wilson method with intensities ............ 39 
7.F. Fitting the term structure to bond and swap rates .................... 46 
Volatility and matching adjustment ...................................................... 49 
8. Introduction: Conceptual Framework. ........................................ 49 
8.A. Conceptual framework of the volatility adjustment .................... 50 
8.A.1. Currency volatility adjustment ............................................. 50 
8.A.2. Country specific increase of the volatility adjustment ............. 52 
8.A.3. Publication of the volatility adjustment ................................. 53 
8.B. Conceptual framework of the matching adjustment ................... 53 
9. Deriving the representative portfolios of bonds and the reference 
portfolios of ‘yield market indices’ for the Volatility Adjustment ............. 55 
9.A. Introduction ......................................................................... 55 
9.B. Introductory remarks on the representative portfolios applied in 
the calculation of the currency volatility adjustment and in the calculation 
of the country specific increase of the volatility adjustment. ................. 56 
9.C. Representative portfolios of assets referred to in Article 50 of the 
Delegated Regulation ...................................................................... 57 
9.D. The portfolio weights referred to in Article 50 of the Delegated 
Regulation ..................................................................................... 58 
9.E. Reference portfolios of ‘yield market indices’ ............................ 60 
9.F. Volatility Adjustment for non-EEA currencies ............................ 64 
10. Methodology for the determination of the risk corrections and the 
fundamental spreads ....................................................................... 66 
10.A. Introduction ......................................................................... 66 
10.B. Determination of the risk-corrections and the fundamental spreads 
for government bonds ..................................................................... 66 
10.B.1. Long-term average of the spread on government bonds ......... 67 
10.C. Determination of the risk-corrections and fundamental spreads for 
assets other than government bonds ................................................. 69 
10.C.1. General elements ............................................................... 69 
10.C.2. Method for deriving the probability of default (PD) and the cost 
of downgrade (CoD) ........................................................................ 70 
10.C.3. Long-term average of the spread on other assets .................. 72

4/131 
 
10.C.4. Currencies without yield market indices for corporates, loans and 
securitizations. ............................................................................... 73 
10.C.5. Inputs used to determine Sgov and Scorp ................................. 74 
11. Process of calculation of the risk-corrected spread at portfolio level 77 
12. Financial market data applied for VA and MA calculation ............... 80 
12.A. Market data for government bonds ......................................... 80 
12.B. Financial market data for assets other than government bonds .. 80 
12.B.1. Market yields for corporate bonds ........................................ 80 
12.B.2. Market data for the calculation of the PD and CoD .................. 81 
13. Calculation of the relevant risk-free interest rates term structures at 
a glance. ........................................................................................ 85 
14. Annexes ................................................................................. 87 
14.A. Annex to section 3: Relevant currencies .................................. 87 
14.B. Annex to section 4: Identification of reference instruments and DLT 
assessment .................................................................................... 88 
14.C. Annex to subsection 4.B: DLT assessment of EEA currencies ...... 91 
14.D. Annex to subsection 4.C: DLT assessment of non-EEA currencies
 92 
14.D.1. Volatility analysis ............................................................... 92 
14.D.2. The analysis of bid-ask spreads: Direct observation ............... 97 
14.D.3. The analysis of bid-ask spreads: Roll measure ..................... 100 
14.D.4. Quantitative analysis ........................................................ 100 
14.E. Annex to Section 4: History of relevant financial instruments ... 102 
14.F. Annex to Subsection 7.A: Numerical illustration of the 
extrapolation of term structures ...................................................... 103 
14.G. Annex to subsection 7.C: Rationale for the UFR calibration .... 108 
14.H. Annex to subsection 9.D: Methodology to update the 
representative portfolios ................................................................ 112 
14.I. Annex to subsection 10.B.1: History of government bond rates for 
the calculation of the LTAS ............................................................. 119 
14.J. Annex to subsections 10.B.1 und 10.C.3: Adjustment factors for 
the pound sterling LTAS ................................................................. 119 
14.K. Annex to subsection 10.C.2: Calculation of the cost of downgrade 
(CoD) and probability of default (PD)............................................... 120 
14.L. Annex to subsection 10.C.4: Background on the treatment of 
Danish covered bonds ................................................................... 129

5/131 
 
14.M. Annex to subsection 10.C.2: Specification of the input data for 
the transition matrices ................................................................... 130 
14.N. Diagram of calculations .................................................... 131

6/131 
 
Letter of the Executive Director 
Solvency II aims at implementing an economic and risk -based supervisory 
framework in the field of insurance and reinsurance. The framework is built upon 
three pillars, all equally relevant, that provide for quantitative requirements 
(Pillar 1), qualitative requirements ( Pillar 2) and enhanced transparency and 
disclosure (Pillar 3). 
The starting point in Solvency II is the economic valuation of the whole balance 
sheet, where all assets and liabilities are valued according to market consistent 
principles. 
The risk-free interest rate term structure (hereafter in this  letter, risk-free 
interest rate) underpins the calculation of liabilities by insurance and reinsurance 
undertakings. EIOPA is required to publish the risk-free interest rate.  
This technical document sets out the basis on which it will do so. It is the result 
of collaboration between EIOPA’s members and its staff.  
As a default approach, the risk-free interest rate is primarily derived from the 
rates at which two parties are prepared to swap fixed and floating interest rate 
obligations. In the absence of financial swap markets, or where information of 
such transactions is not sufficiently reliable, the risk-free interest rate is based 
on the government bond rates of the country.  The risk-free interest rates are: 
 Calculated for different time periods, reflecting that the liabilities  of 
insurance and reinsurance undertakings stretch years and decades into 
the future.  
 Calculated in respect of the most important currencies for the EU 
insurance market. 
 Adjusted to reflect that a portion of the interest rate in a swap transaction 
(or a government bond) will reflect the risk of default of the counterparty 
and hence without adjustment would not be risk-free. 
 Based on data available from financial markets. For those periods in the 
more distant future for which data are not available, the rat e is 
extrapolated from the point at which data are available to a 
macroeconomic long-term equilibrium rate.  
An adjustment (the volatility adjustment) is made to the liquid part of the risk-
free interest rate in order to reduce the impact of short term market volatility on 
the balance sheet of undertakings. EIOPA is required to provide, both on a 
currency and country basis, the size of this adjustment for volatility. 
A different adjustment (the matching adjustment) is made in respect of 
predictable portfoli os of liabilities.  An undertaking can assign to eligible 
portfolios assets with fixed cash flows that it intends to hold to maturity. EIOPA 
is required to provide an estimate of what portion of the spread of such assets 
above the risk-free interest rate reflects risks not faced by those who hold assets 
to maturity.

7/131 
 
Many of the parameters of the risk-free rates are already determined in 
legislation. Some choices remain however, and in many cases more than one 
option is possible. The rationale for the key ch oices made by EIOPA is set out in 
section 1 (Basis for decision) of this technical documentation. The choices made 
by EIOPA, always within the limits set by EU legislation, are designed to secure 
the following objectives. 
Replicability 
EIOPA intends the risk-free rate interest rate to be capable of replication by 
undertakings and other interested parties, through this technical documentation. 
This will benefit undertakings for their own risk management and other 
purposes. One consequence of replicability is  that the use of so -called “expert 
judgement” i.e. the exercise of discretion in the regular construction of the risk-
free interest rate, has been kept to a minimum.  
Market consistency 
Whenever possible, data from deep, liquid and transparent financial ma rkets are 
used to construct the risk-free interest rate.  Adopting such a market consistent 
approach helps foster transparency in insurance markets with a positive impact 
on understanding and trust, as well as helping create a level playing field  by 
enabling the comparison between undertakings. 
Solvency II reporting  
The intended frequency of publication of the risk-free interest rate is monthly. 
Such a frequency will enable undertakings to have a common basis for 
calculating the value of the financial info rmation they are required to report to 
their supervisor on a quarterly and annual basis.  
Stability for insurance undertakings 
EIOPA does not want to exacerbate volatility in the value of liabilities through 
unwarranted changes to the risk-free interest ra te. Changes would naturally 
have to be justifiable on an EU -wide basis. The experience of those EIOPA 
members who have already produced risk-free interest rates is however that 
from time to time the case for change is made. Regardless of any earlier 
changes, there will also be a more formal stocktake, for example at the point at 
which the calibration of capital requirements under Solvency II is reviewed. 
The risk-free rate interest rate is intended to be published from February 2015, 
to give undertakings time to prepare. EIOPA does not seek a timescale between 
publication of the risk-free interest rate and the requirement on undertakings to 
report that could trigger rapid sale or purchase of assets. 
Policyholders 
These objectives will benefit policyholders. Replicability, market consistency, 
Solvency II reporting, and stability for undertakings will make easier the 
valuation of undertakings and the work of supervisors.

8/131 
 
The key components of the risk-free rate are summarised in the table below. 
They are exp lained in much greater detail, alongside other components, in the 
technical documentation. 
 
Component Approach adopted by EIOPA 
Assessment of deep, liquid, 
transparent financial market 
information 
 Assessments by each EIOPA member 
or (for non-EEA currencies) analysis of 
market interest rates 
Last liquid point (LLP) 
 Euro: residual volume criterion 
 Other EEA currencies: assessment by 
each EEA member state 
 Non-EEA currencies: EIOPA assessment 
Extrapolation  Smith-Wilson method as applied in the 
Long-term Guarantees Assessment 
Convergence maturity 
 Euro: 60 years 
 Non-euro currencies: in general 
max(LLP+40Y; 60Y) 
Volatility adjustment: calculation 
of risk correction 
 Calculated in the same manner as the 
fundamental spread 
 For government bonds, based on the 
long-term average spreads over the 
basic risk-free interest rates term 
structure 
 For assets other than government 
bonds, based on the maximum of: 
the long-term average spreads 
a probability of default and cost of 
downgrade based on the projection 
of an average 1-year transition 
matrix  
 
Matching adjustment: calculation 
of fundamental spread 
 Separate calculation of a probability of 
default and cost of downgrade based 
on the projection of an average 1-year 
transition matrix

9/131 
 
Legal Notice 
1. This document aims to assist users in complying with their obligations 
under Directive 2009/138/EC  (hereinafter “Solvency II Directive”). 
Information in this document does not constitute legal advice. Usage of the 
information remains under the sole responsibility of the user. EIOPA does 
not accept any liability with regard to the use that may be made of the 
information. 
2. The references to financial data, financial and statistical methodologies, and 
trademarks mentioned in this document are protected by their respective 
property rights (be they proprietary to EIOPA or third parties). The 
references to such information neither means any change of such rights, 
nor constitutes any type of explicit or implicit authorization of EIOPA for 
any use, nor provides any type of opinion of EIO PA in respect of them for 
purposes other than those proposed in this technical documentation. 
3. Whenever reference is made to a (third party) market data provider, the 
use of the relevant data shall be subject to the terms and conditions of 
such market data provider, including the relevant disclaimers (as can be 
consulted on the relevant market data provider’s website). 
 
© European Insurance and Occupational Pensions Authority-EIOPA, 2015. 
 
Disclaimers 
S&P disclaimer 
“This may contain information obtained fro m third parties (including ratings 
from credit ratings agencies such as Standard & Poor’s, modeling tools, 
software or other applications or output therefrom) or any part therefrom 
(Third Party Content).  Reproduction and distribution of Third Party Conten t 
in any form is prohibited except with the prior written permission of the 
related third party.  Third Party Content providers do not guarantee the 
accuracy, completeness, timeliness or availability of any of the Third Party 
Content and are not responsibl e for any errors or omissions (negligent or 
otherwise), regardless of the cause, or for the results obtained from the use 
of such Third Party Content.  THIRD PARTY CONTENT PROVIDERS GIVE NO 
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
ANY WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
PURPOSE OR USE.  THIRD PARTY CONTENT PROVIDERS SHALL NOT BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, EXEMPLARY, 
COMPENSATORY, PUNITIVE, SPECIAL OR CONSEQUENTIAL DAMAGES, 
COSTS, EXPENSES, LEGAL F EES, OR LOSSES (INCLUDING LOST INCOME 
OR PROFITS AND OPPORTUNITY COSTS OR LOSSES CAUSED BY 
NEGLIGENCE) IN CONNECTION WITH ANY USE OF THE THIRD PARTY 
CONTENT.  Credit ratings are statements of opinions and are not statements

10/131 
 
of fact or recommendations to purchase, hold or sell securities.  They do not 
address the suitability of securities or the suitability of securities for 
investment purposes, and should not be relied on as investment advice.”  
  
 
Markit disclaimer 
Neither Markit, its Affiliates or any thi rd party data provider makes any 
warranty, express or implied, as to the accuracy, completeness or 
timeliness of the data contained herewith nor as to the results to be 
obtained by recipients of the data.  Neither Markit, its Affiliates nor any data 
provider shall in any way be liable to any recipient of the data for any 
inaccuracies, errors or omissions in the Markit data, regardless of cause, or 
for any damages (whether direct or indirect) resulting therefrom. 
Markit has no obligation to update, modify or  amend the data or to 
otherwise notify a recipient thereof in the event that any matter stated 
herein changes or subsequently becomes inaccurate. 
 
Without limiting the foregoing, Markit, its Affiliates, or any third party data 
provider shall have no liabil ity whatsoever to you, whether in contract 
(including under an indemnity), in tort (including negligence), under a 
warranty, under statute or otherwise, in respect of any loss or damage 
suffered by you as a result of or in connection with any opinions, 
recommendations, forecasts, judgments, or any other conclusions, or any 
course of action determined, by you or any third party, whether or not 
based on the content, information or materials contained herein.

11/131 
 
Legal basis 
4. The Union legislator entrusted EIOPA  to lay down and publish technical 
information on risk -free interest rates with the purpose to allow for the 
consistent calculation of technical provisions by insurance and reinsurance 
undertakings under Article 77e(1) of the Solvency II Directive. 
5. To furt her reinforce the importance of that technical information towards 
achieving consistency in the calculation of technical provisions, the Union 
legislator provided for binding effects of this technical information on 
insurance and reinsurance undertakings,  subject to the inclusion of this 
information into an implementing act of the European Commission (Article 
77e(2) of the Solvency II Directive). 
6. In accordance with recital 23 of the Commission Delegated Regulation (EU) 
2015/352 (hereinafter “Delegated Regulation”), the present EIOPA technical 
documentation is published by EIOPA a s part of the technical information 
published pursuant to  Article 77e(1) of the Solvency II Directive . The 
technical documentation explains in a transparent manner how the relevant 
risk-free interest rate term structures are derived. It is published to achieve 
a consistent calculation of technical provisions.  
 
  
                                       
2 Commission Delegated Regulation (EU) No 2015/35 of 10 October 2014 supplementing Directive 
2009/138/EC of the European Parliament and of the Council on the taking-up and pursuit of the 
business of Insurance and Reinsurance (Solvency II) (OJ L 12, 17.01.2015, p. 1)

12/131 
 
1. Basis for decision 
7. The development of the methodology to calculate the relevant risk -free 
interest rates term structures  has required a number of decisions on the 
methods, assumptions and inputs to use in that calculation.  
8. EIOPA has based those decisions on the following principles: 
a) respect to the essential elements underpinning the political 
agreement of Directive 2014/51/EU (Omnibus II Directive), 
b) transparency of all the elements of the process of calculation, 
c) replicability of the calculations, which has as a direct 
consequence the restriction of expert judgement to the 
minimum extent possible, if any, 
d) market consistency, pr udent assessment of the technical 
provisions and optimal use of market information. 
9. The following items describe the main decisions adopted, following the 
order of the topics contained in this technical documentation. 
1.A. General issues 
Financial market data used as inputs 
10. This technical documentation identifies the financial market data used as 
inputs of the calculations.  
11. EIOPA keeps unambiguous neutrality regarding the market data providers 
competing in the market. The reason for selecting market data provid ers 
relies only on the high priority given to: 
a) the legal imperative of publishing the concrete figures of the 
technical information set out in Article 77e of the Solvency II 
Directive, 
b) the full traceability of the calculations, as part of EIOPA ’s 
commitment to the principle of transparency, 
c) the ‘replicability’ of the process of calculation by those 
stakeholders wishing to reproduce the technical information, 
d) the ability  to put into place an appropriate process of 
validation.  
12. In order to ensure the appropri ateness of the data,  two market data 
sources are used, one for inputs (‘direct input provider’), and the other for 
validation.   
13. EIOPA has decided to use the same direct input provider for swaps and 
government bonds curves. EIOPA has selected different providers for yields

13/131 
 
of corporate bonds and for default statistics to reduce the operational risk 
and the dependence on the data providers.    
14. The selection of these providers should not be understood as EIOPA ’s 
preference for them. The selection does not con stitute advice to  
undertakings when deciding which provider better fits to their needs. 
Use of market data with maturities of less than one year 
15. EIOPA has decided to publi sh the relevant risk -free interest rates term 
structure from 1 year maturity onwards. Instruments with a maturity below 
1 year are not always swaps and the adjustment of their credit risk, among 
other features, may add unnecessary complexity  to the calculations . 
Furthermore, below 1 -year rates have  a negligible impact on the rates 
extrapolated with the Smith-Wilson method, and hence a negligible impact 
on the amount of long-term technical provisions. 
Methods for the assessment of deep, liquid and transparent financial 
markets (DLT assessment) 
16. Based on academic literature and the methods app lied by practitioners 
EIOPA has analysed the metrics and criteria commonly used for 
assessments of market liquidity and  assessed their applicability for the 
purposes of setting a conceptual framework for the DLT assessment.  
17. Having in mind that the National Competent Authorities have better 
knowledge of the financial markets of each currency, the DLT assessment 
of EEA currencies has been made by each National Competent Authority. All 
National Authorities applied the same methodology and reported their 
findings in a common template. Three main findings may be extracted from 
the set of lessons learnt: 
a) The application of the common conceptual framework should not 
rely on hard thresholds and should not disregard qualitative 
information. In particular , a number o f criteria are inter -linked 
and the markets for the same financial instruments for different 
currencies may present different features. 
b) The DLT assessment is a demanding exercise and therefore the 
frequency of updating the assessment should be carefully 
considered.  
c) Furthermore, with the exception of crisis situations, frequent 
violent changes in the outputs of the DLT assessment  do not 
seem plausible . Rather, a plausible future trend will be the 
development of financial markets and the extension of the 
market interest rates meeting DLT requirements (i.e. the use of 
market consistent information).

14/131 
 
1.B. Basic risk-free interest rates term structure 
Credit risk adjustment (CRA) 
18. The Delegated Regulation only covers the calculation of the CRA for those 
currencies with DLT swap markets and overnight swaps markets.  
19. For currencies where either swaps or overnight swaps markets do not meet 
DLT requirements or currencies whose risk -free interest rates term 
structure is based on government bonds rates,  EIOPA has appli ed the 
objective criteria described below in section 5 , avoiding any margin for 
expert judgement.  
20. Furthermore EIOPA is aware of the initiatives in the Union for the 
development of more transparent financial markets for risk -free financial 
instruments.  
Extrapolation method 
21. The interpolation, where necessary, and extrapolation of interest rates have 
been developed applying the Smith-Wilson method. 
22. This method is of course not the only one possible method for the 
extrapolation of interest rates. All methods have their pros and cons. 
23. The Smith-Wilson method has been applied during the last years of the 
development of the Solvency II framework, and in particular in the fifth 
Quantitative Impact Study (QIS5)  and in the Long-term Guarantees 
Assessment (LTGA)  that has underpinned the political agreement of the 
Omnibus II Directive.  
24. EIOPA will however carefully monitor market developments, and their 
influence on the implementation of the Smith-Wilson method. 
Last Liquid Point (LLP) 
25. The Delegated Regulation includes a specific recital for the determination of 
the LLP and the application of DLT requirements for the euro. Its sets out a 
criterion regarding the residual volume of bonds meeting DLT requirements 
(residual volume criteri on). The criterion is precise except for the very 
specific market data to be used as input. 
26. For currencies other than the euro, according to recital 30 of the Omnibus 
II Directive, the choice of the LLP should allow undertakings to match with 
bonds the cash flows which are discounted with non -extrapolated interest 
rates in the calculation of the best estimate. The application of this principle 
is currently challenging due to the limitation of the information available on 
cash flows from insurance and reinsurance obligations . Therefore, for 
currencies other than the euro, EIOPA is basing the LLP on the results of 
the DLT assessment, rather than developing th at matching criterion at this 
stage.

15/131 
 
Convergence point 
27. The Omnibus II Directive explicitly reflects for the euro a convergence 
period of 40 yea rs and a LLP of 20 years, which is equivalent to assuming 
that the forward rate will be close  to its ultimate level from 20+40=60 
years maturity onwards.  
28. For currencies other than the euro,  the convergence point is the maximum 
of (LLP+40 years) and 60 yea rs. This method is considered as the most 
stable, least influenced by expert judgement and also the one with lowest 
impact on the level playing field between market participants.  
29. In accordance with recital 30 of the Omnibus II Directive, the  selected 
option keeps the allowance of different outcome  for specific cases  
conditional on their adequate justification.  
1.C. Volatility adjustment (VA) and Matching adjustment (MA) 
Financial market inputs for VA and MA 
30. The Delegated Regulation  states that the manner in wh ich the risk 
correction for the VA and the fundamental spread for the MA are calculated 
should be the same. EIOPA understands that the intention of the phrase ‘in 
the same manner’  in Article 51 is to cover all the elements of the 
calculation, including the  data underlying it. This means that the same 
approach should be applied for both the risk correction  and the 
fundamental spread . In particular EIOPA has not used different market 
default and transition inputs for these calculations. 
31. EIOPA has gathered inp uts on bonds, using the following granularity: 
currency, credit quality, duration and economic sector of the issuer. This 
segmentation is based on Article 77c of the Solvency II Directive. 
Financial market inputs for bond yields 
32. EIOPA has elaborated a conc eptual framework in order to apply to the 
maximum extent the use of market ind ices in the calculation of the VA  as 
required in Article 49(3)(b) of the Delegated Regulation. 
33. For this purpose EIOPA maps the representative portfolios of assets to 
yields that are derived from yield curves and yield indices. 
34. In the case of the euro currency VA, EIOPA has opted for a simplification in 
the use of indices  for central government bonds : the replacement of the 
calculation based on all the government curves of th e members of the euro 
area, by a single curve: the ECB yield curve, annual spot rates, with 
reference to all members of the euro area.

16/131 
 
35. For non-euro currencies and for the purpose of the country-specific increase 
of the VA, the use of yield curves for each issuer  of government bonds is 
necessary given the materially different degrees of home-bias. 
36. Finally, in the case of other bonds (e .g. corporate bonds and collateri sed 
bonds, etc.), a major challenge has been the availability of the information 
with the necessary granularity (maturities, ratings, economic sectors) for all 
relevant currencies. 
Inputs for the calculation of the long-term average spread 
37. Article 54(3) of the Delegated Regulation sets out: 
The long-term average referred to in Article 77c(2)(b) and (c) of Directive 
2009/138/EC shall be based on data relating to the last 30 years. Where a 
part of that data is not available, it shall be replaced by constructed data. 
The constructed data shall be based on the available and reliable data 
relating to the last 30 years. Data that is not reliable shall be replaced by 
constructed data using that methodology. The constructed data shall be 
based on prudent assumptions.     
38. There is currently a lack of full 30 years of historical data for swaps and  
government bonds, for almost all currencies.  Furthermore, overnight swap 
markets (whose short term rates are necessary for the calculation of the 
credit risk adjustment), were active only since the end of the last century. 
39. EIOPA has decided to construct the missing spread  data for each currency 
and maturity using the average of the spread data that is available from 1 
January 1985 or, failing that, whenever reliable spread data is first 
available. In practice, the lack of overnight swap rates has led to consider 
market data only from January 1999. 
40. The same considerations apply to  the floor for bonds other than central 
government and central banks bonds, with two further features that 
increase the practical difficulties: 
a)  For most EEA currencies there are no reliable yield term 
structures for corporate bonds. 
b)  For the euro, the curves currently provided by financial market 
data providers have a limited history. 
41. For the selection of market providers, EIOPA has considered a decision 
process for central governments and cen tral banks bonds and for other 
bonds (e.g. corporates), taking into account in particular the following: 
a) the availability of historical data, 
b) the market information and methodology behind the construction 
of the market indices (e.g. government and corporate bonds),

17/131 
 
c) the granularity (e .g. buckets regarding the maturities, ratings, 
economic sectors, for bonds other than central governments and 
central banks). 
Central governments and central banks bonds  - Calculation of the 
long-term average spread 
42. Depending on the period of observation, EIOPA has considered whether 
market data should be weighted for the calculation of the average referred 
to in Article 77c(2) of the Solvency II Directive. 
43. Both in the LTGA and the EIOPA Stress Test 2014  a simple average  was 
applied. 
44. The allowance of adjustments to the simple average means to disregard 
market observations and embeds the use of material expert judgement. 
This option lacks legal basement and has been rejected due to the 
subjective assumptions required. 
45. Furthermore, EIOPA believes that assuming a flat curve as reconstructed 
history (e.g. for the euro before 1 January 1999) is the most neutral choice 
as well as being in line with the Solvency II Directive and in particular the 
political agreement on the Omnibus II Directive. The level should be equal 
to the simple and unadjusted average of the available market spreads. 
Methodology of calculation of the spread before risk correction, for 
currencies where yield term structures are not available 
46. For most of the EEA currencies either there are no available interest rate 
term structures for the assets relevant to determine Scorp
3 or the number of 
potential underlying assets to build such curves is rather low. Market data 
providers only produce corporate yield curves for a few EAA currencies (just 
the most developed financial markets).  
47. In absence of empirical data, EIOPA has decided to apply the following 
formulas which are based on the approach already applied in the LTGA: 
 
 €€
€€
)1( rfr
X
rfrcorp
X
corp
rfr
X
rfrcorp
X
corp
YYYY
YYSS




 
where € denotes the euro, X refers to a currency without yield term 
structures for the assets relevant for the spread Scorp, Ycorp denotes the 
                                       
3 According to Article 50 of the Delegated Regulation, Scorp denotes the average currency spread on 
bonds other than governments bonds, loans and securitizations included in the reference portfolio 
of assets for that currency or country.

18/131 
 
yield of the respective corporate bonds of the same credit qualit y, Yrfr 
denotes the basic risk -free interest rate and  is equal to 0.5. The inputs 
of this formula are maturity dependent according to the information 
available. 
48. This approach is based on the following rationale:  spreads might be better 
reflected by spreads derived from the basic risk -free rates than using no 
data. In addition, this method is simple and, where necessary, immediately 
applicable to all published currencies in a consistent manner. 
49. Further than its simplicity and traceability, this formula guarantees that for 
each currency their ‘notional‘ yield curves for corp orates will behave -
compared to the basic risk -free interest rates term structure  - similarly to 
the main currency where corporate yield term structures for the euro are 
available for a number of years. 
50. Setting  = 0.5 seems the best proxy for a formula to  be applied to all 
relevant currencies. This proxy provides a central estimate and ensures 
that differences with the more accurate and complex calculation are 
reduced to the maximum extent possible using a simple and implementable 
approach. 
Granularity of yield information for bonds other than central 
government and central bank bonds 
51. An appropriate  granularity according to maturities, ratings  and economic 
sectors has been adopted in order to adequately capture the different 
behaviour of spreads (e.g. of financial and non-financial bonds).

19/131 
 
2. Governance and control s of the process of calculation and 
publication 
52. EIOPA has established internal governance arrangements in order to define 
the essential elements of the operational framework such as: 
i)  The perio d of time after which the technical information shall be 
published 
ii)  Definition of the functions involved 
iii)  The resources necessary for running the process  and the registers 
and logs for recording 
iv)  Internal controls to safeguard the process used built on ‘four eyes’ 
principle 
vi) The frequency of activities, in particular audits, reviews and internal 
controls 
viii)  Definition in a limitative manner of the areas where expert 
judgement in the process is allowed (e.g. some areas of the DLT 
assessment). In that case, the documentation of the expert 
judgement includes its content, link to the authorized scope, 
validation, internal control and log of escalation, in order to ascertain 
that, in accordance with the  EIOPA regulation, such expert 
judgement is independently exercised, it acts in the interest of the 
Union, enhances the protection of policyholders and foster s a level 
playing field of the EU insurance market. 
ix)  Definition of the specific process to follow new information might 
advise the revi ew of the technical information already published . 
EIOPA rules on public consultation will apply to the review of th is 
technical documentation, 
x) Contingency plans for continuing the publication of the technical 
information in case of unexpected events 
xi)  Rules in order to record, store and report exceptional events in the 
development of any of the steps of the process  (process events, IT 
events, financial market data events, etc.) 
xii) Establishment of an oversight function and of a control function 
ensuring that the technical information is provided and published or 
made available in accordance with the methodology, assumptions 
and inputs approved by EIOPA. 
53. EIOPA’s framework regarding code of conduct and conflict of interests 
applies to all the persons involved in the process in any function. All these 
persons have to declare and sign the relevant documentation at least every 
year, and as soon as any factual or potential, current or foreseeable, 
conflict of interest appears or may appear.

20/131 
 
54. EIOPA has not approved and does not envisage approving, the outsourcing 
of any function or activity of the process for the calculation and publication 
of the technical information, other than the collection of data of financial 
markets from generally used financial provi ders, and the outsourcing 
applied to some parts of the IT systems of EIOPA.

21/131 
 
3. Data sources for the inputs from financial markets 
3.A. Financial market data providers 
55. In order to mitigate the  operational risks of a market provider failure , the 
calculation of th e technical information should not over -rely on a single 
market source. 
56. A first way to ensure this would be to derive each input using data obtained 
from a range of providers. A  second alternative would be to calculate a 
given input based on data from a si ngle market provider, but to use 
different providers for different inputs or functions, under the condition that 
all sources are sufficiently consistent. 
57. As a general rule EIOPA has opted for the second of these options, on the 
basis that an application of  the first option  to all inputs would introduce 
additional complexity and increase the operational risks , without providing 
material benefits compared to the second alternative. 
58. EIOPA has no evidence o f the superiority of a concrete market data 
provider. The choice of market data providers included in th is technical 
documentation are disclosed only for the purposes of transparency (recital 
23 of the Delegated Regulation).  
59. In accordance with recital 23 of the Delegated Regulation, EIOPA’s technical 
documentation will accompany the technical information set out in Article 
77e(2) of the Solvency II Directive in order to ensure transparency. 
60. The following providers are used (see subsections below for detail): 
a. Swaps and overnight indexed swaps: Bloomberg 
b. Government bonds: Bloomberg 
c. Bonds other than government bonds: Markit – iBoxx indices and, 
for Danish covered bonds, Bloomberg 
d. Default statistics: Standard & Poors 
61. The market data inputs will be analysed under the relevant review process 
according to section 2. 
3.B. Selection of the relevant currencies 
62. EIOPA applies the following criteria to select the currencies (and countries 
for the country specific increase of the volatility adjustment) for which  
technical information is published: 
 all currencies and countries of the EEA, 
 all non-EEA currencies, where EIOPA has evidence on their materiality 
for the EU insurance sector , and where reliable and adequate financial

22/131 
 
market data are publicly available  to perform the necessary 
calculations. 
63. The list of relevant currencies and, where applicable, countries can be 
found in Annex 14.A. 
64. EIOPA will review the list of relevant currencies on an annual basis. Any 
changes will be announced three month before their implementation. In 
exceptional circumstances EIOPA may deviate from thi s process to change 
the list of relevant currencies. 
3.C. Selection of market rates 
65. The construction of the basic risk-free interest rate term structures is based 
on swaps and/or government bonds as set out in Article 44 of the 
Delegated Regulation . EIOPA is aw are of the initiatives in the Union to 
develop in the future risk-free instruments traded on deep, liquid and 
transparent markets. 
66. EIOPA applies the financial references in the table below from the market 
data provider selected.  
67. The last  column of the tab le specifies whether the financial instruments 
applied are either swaps or government bonds. For a clear identification of 
swaps, the floating is also included. 
68. In the process of calculation of the basic risk -free interest rates term 
structures, the ticker s for government bonds are used only for the 
currencies with ‘GVT’ in the last column. The inputs to the process of 
calculation of the volatility and matching adjustment s regarding 
government bonds are also based on the information referred to in the 
table below. 
 
Table 1. Swaps and government bonds used for the derivation of the 
technical information 
Country ISO 
3166 
ISO 
4217 Swap Ticker Swap
freq 
Swap Float  
Ticker 
Government Bond 
Ticker Id 
Govts/
Swaps 
Euro - EUR EUSA CMPL Curncy 1 EUR006M Index ECB curve all 
governments-spot SWP 
Austria AT EUR EUSA CMPL Curncy 1 EUR006M Index G0063Z BLC2 Curncy SWP 
Belgium BE EUR EUSA CMPL Curncy 1 EUR006M Index G0006Z BLC2 Curncy SWP 
Bulgaria (*) BG BGN EUSA CMPL Curncy 1 EUR006M Index BI0662Z BVLI Curncy SWP 
Croatia HR HRK       G0369Z BLC2 Curncy GVT 
Cyprus CY EUR EUSA CMPL Curncy 1 EUR006M Index  SWP 
Czech Rep. CZ CZK CKSW CMPL Curncy 1 PRIB06M Index G0112Z BLC2 Curncy SWP 
Denmark (*) DK DKK EUSA CMPL Curncy 1 EUR006M Index G0011Z BLC2 Curncy SWP 
Estonia EE EUR EUSA CMPL Curncy 1 EUR006M Index   SWP

23/131 
 
Finland FI EUR EUSA CMPL Curncy 1 EUR006M Index G0081Z BLC2 Curncy SWP 
France FR EUR EUSA CMPL Curncy 1 EUR006M Index G0014Z BLC2 Curncy SWP 
Germany DE EUR EUSA CMPL Curncy 1 EUR006M Index G0016Z BLC2 Curncy SWP 
Greece GR EUR EUSA CMPL Curncy 1 EUR006M Index G0156Z BLC2 Curncy SWP 
Hungary HU HUF HFSW CMPL Curncy  1  BUBOR06M Index  G0165Z BLC2 Curncy GVT 
Iceland IS ISK       I328 CMPL Index GVT 
Ireland IE EUR EUSA CMPL Curncy 1 EUR006M Index G0062Z BLC2 Curncy SWP 
Italy IT EUR EUSA CMPL Curncy 1 EUR006M Index G0040Z BLC2 Curncy SWP 
Latvia LV EUR EUSA CMPL Curncy 1 EUR006M Index  SWP 
Liechtenstein LI CHF SFSW CMPL Curncy 1 SF0006M Index   SWP 
Lithuania LT EUR EUSA CMPL Curncy 1 EUR006M Index  SWP 
Luxembourg LU EUR EUSA CMPL Curncy 1 EUR006M Index   SWP 
Malta MT EUR EUSA CMPL Curncy 1 EUR006M Index   SWP 
Netherlands NL EUR EUSA CMPL Curncy 1 EUR006M Index G0020Z BLC2 Curncy SWP 
Norway (*) NO NOK NKSW CMPL Curncy 1 NIBOR6M Index G0078Z BLC2 Curncy SWP 
Poland PL PLN       G0177Z BLC2 Curncy GVT 
Portugal PT EUR EUSA CMPL Curncy 1 EUR006M Index G0084Z BLC2 Curncy SWP 
Romania RO RON RNSW CMPL Curncy 1 BUBR3M Index BI0631Z BVLI Curncy GVT 
Russia RU RUB RRSWM CMPL 
Curncy 1 MOSKP3 Index G0326Z BLC2 Curncy SWP 
Slovakia SK EUR EUSA CMPL Curncy 1 EUR006M Index G0256Z BLC2 Curncy SWP 
Slovenia SI EUR EUSA CMPL Curncy 1 EUR006M Index G0259Z BLC2 Curncy SWP 
Spain ES EUR EUSA CMPL Curncy 1 EUR006M Index G0061Z BLC2 Curncy SWP 
Sweden SE SEK SKSW CMPL Curncy 1 STIB3M Index G0021Z BLC2 Curncy SWP 
Switzerland CH CHF SFSW CMPL Curncy 1 SF0006M Index G0082Z BLC2 Curncy SWP 
United 
Kingdom GB GBP BPSW CMPL Curncy 2 BP0006M Index G0022Z BLC2 Curncy SWP 
Australia AU AUD ADSW CMPT Curncy 2 BBSW6M Index G0001Z BLC2 Curncy SWP 
Brazil BR BRL       G0393Z BLC2 Curncy GVT 
Canada CA CAD CDSW CMPN Curncy 2 CDOR03 Index G0007Z BLC2 Curncy SWP 
Chile CL CLP CHSWP CMPN 
Curncy 2 CLICP Index G0351Z BLC2 Curncy SWP 
China CN CNY CCSWO CMPT 
Curncy 4 CNRR007 Index G0299Z BLC2 Curncy SWP 
Colombia CO COP CLSWD CMPN 
Curncy 4 DTF RATE Index G0217Z BLC2 Curncy GVT 
Hong Kong HK HKD HDSW CMPT Curncy 4 HIHD03M Index G0095Z BLC2 Curncy SWP 
India IN INR       BI0571Z BVLI Curncy GVT 
Japan JP JPY JYSW CMPT Curncy 2 JY0006M Index G0018Z BLC2 Curncy SWP 
Malaysia MY MYR MRSWQO CMPT 
Curncy 4 KLIB3M Index G0196Z BLC2 Curncy SWP 
Mexico (*) MX MXN MPSW CMPN Curncy  13  MXIBTIIE 
Index  G0251Z BLC2 Curncy SWP 
New Zealand NZ NZD NDSW CMPT Curncy 2 NFIX3FRA Index G0049Z BLC2 Curncy SWP 
Singapore SG SGD SDSW CMPT Curncy 2 SORF6M Index G0107Z BLC2 Curncy SWP 
South Africa ZA ZAR SASW CMPL Curncy 4 JIBA3M Index G0090Z BLC2 Curncy SWP 
South Korea KR KRW KWSWO CMPT 
Curncy 4 KWCDC Index G0173Z BLC2 Curncy SWP

24/131 
 
Taiwan TW TWD       BI0594Z BVLI Curncy GVT 
Thailand TH THB TBSWO CMPT 
Curncy 2 THFX6M Index BI0570Z BVLI Curncy SWP 
Turkey TR TRY TYSW CMPL Curncy 1 TRLIB3M Index  SWP 
United 
States US USD USSW CMPN Curncy 2 US0003M Index G0111Z BLC2 Curncy SWP 
Notes:  
 Bloombergs identifiers. Prices PX_LAST. 
 For reference dates after 31 May 2015, the swap rates for European and 
African currencies are based on London fixing (CMPL), for American 
currencies are based on New York fixing (CMPN) and for the currencies of 
Asia and Australia are based on Tokyo fixing (CMPT). F or earlier reference 
dates, all swap rates are based on New York fixing, irrespective of their 
currency. 
 For reference dates after 30 November 2017 the Bloomberg government 
bond tickers with the exception of Iceland  are converted from continuous 
to annual compounded rates before application, where relevant, of the 
credit risk adjustment.    
69. Specific cases are: 
(a) The Norwegian currency, whose 1 year interest rate is based on 
swaps with floating NIBOR 03 mont hs, while the rest of interest 
rates are based on NIBOR 06 months. 
(b) For those non-euro countries with contracts where  the benefits 
guaranteed to the policy holders are valued in euro while the 
payments (including the evolutions of the exchange rate) are in 
the local currency, the term structure is derived on the basis on 
the interest rates denominated in the local currency. 
(c) The rates for Icelandic government bonds are the rates of  
Bloomberg’s Iceland Sovereign Curve with pricing source EXCH . 
These rates are usually not zero coupon rates  but are treated as 
such.  
(d) For the Bulgarian lev and the Danish krone the basic-risk-free 
interest rate term structures are based on the financial 
instruments used for the euro because these two currencies meet 
the legal conditions to be considered as pegged to the euro. 
(e) For the Mexican peso the relevant tickers are MPSW1A, MPSW2B, 
MPSW3C, MPSW4D, MPSW5E, MPSW7G, MPSW10K, MPSW16C 
and MPSW21H (all CMPN Curncy).  The tickers  MPSW16C and 
MPSW21H are used for the maturities 15 and 20 years 
respectively.

25/131 
 
Basic risk-free interest rate term structure 
4. Identification of relevant financial instruments and assessment 
of depth, liquidity and transparency 
4.A. Introduction 
70. According to Article 77a of the Solvency II Directive the relevant risk -free 
interest rate term structure should be based on  relevant financial 
instruments traded in deep, liquid and transparent (DLT) markets. This 
provision is further specified in recital 21, Article 1(32), (33) and (34), and 
Articles 43, 44 and 46 of the Delegated Regulation. The identification of the 
relevant financial instruments is based on a DLT assessment.  
71. The inputs for the DLT assessment are market data on interest rate swap 
rates, government bond rates and corporate bon d rates. These are 
obtained from market data providers whose services are also avai lable to 
insurance and reinsurance undertakings. 
72. The output of the DLT assessment is a list, for each  currency, of the 
maturities for which the market of the relevant financial instrument  is 
considered DLT including the identification of the last maturity for which 
rates can be observed in DLT markets ( section 7.B refers to the 
determination of the last liquid point (LLP)). 
4.B. Conceptual framework for EEA currencies 
73. In a first step, an initial DLT assessment for EEA currencies is carried out by 
the relevant National Competent Authorities.  
74. In a second step , EIOPA has a process in place aimed at ensuring  
homogeneity across national assessment s and preserv ing a level playing 
field. 
75. The relevant financial instruments for EEA currencies that are currently 
used to d erive the term structures were identified on the basis of a DLT 
assessment carried out in 2015. 
76. The table below sets out the results of the DLT assessment . The entries 
identify the instrument used: S=Interest rate swap, B=government bond, 
«empty»=no DLT ma rkets for this maturity available. The last non -empty 
entry defines the LLP. No market data beyond the LLP is used. Hence, no 
further entries are shown in the table, even if single maturities beyond the 
LLP might be considered as meeting DLT criteria. 
77. For the Bulgarian lev and the Danish krone no DLT assessments are made. 
Since these currencies are pegged to the euro, their basic risk -free interest 
rates are based on the DLT assessment for the euro.

26/131 
 
78. The relevant risk -free interest rates are based on  market data for integer 
maturities from one year onwards. 
 
Table 2. EEA currencies: Financial instruments used for the derivation of 
the basic risk-free interest rate term structures 
 EUR CHF NOK PLN ISK HRK RON SEK CZK HUF GBP 
1Y S S S B  B B S S B S 
2Y S S S B B  B S S B S 
3Y S S S B B B B S S B S 
4Y S S S B  B B S S B S 
5Y S S S B   B S S B S 
6Y S S S B B   S S B S 
7Y S S S B   B S S B S 
8Y S S S B B B B S S B S 
9Y S S S B  B B S S B S 
10Y S S S B   B S S B S 
11Y  S         S 
12Y S S       S  S 
13Y  S         S 
14Y  S         S 
15Y S S       S B S 
16Y to 19Y           S 
20Y S S         S 
25Y  S         S 
30Y           S 
35, 40, 45, 
50Y           S 
The table sets out the financial instruments currently used to derive the risk -free interest 
rates. Past changes to the selection of financial instruments are set out in the Annex to 
section 4.

27/131 
 
Table 3. DLT assessment for swaps of EEA currencies whose term structures are based on swap rates  
(1 = DLT , 0 = non-DLT)  
 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 25 30 35 40 45 50 
EUR 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 
CHF 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 1 0 0 0 0 0 
CZK 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 
GBP 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
NOK 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
SEK 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
 
 
Table 4. DLT assessment for government bonds in EEA currencies whose term structure s are based on 
government bonds (1 = DLT , 0 = non-DLT) 
 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 25 30 35 40 45 50 
HRK 1 0 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
HUF 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 
ISK 0 1 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
PLN 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
RON 1 1 1 1 1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
 
For the euro the last liquid point is 20 years, determined in accordance with recital 21 of the Delegated Regulation.

28/131 
 
4.C. Conceptual framework for non-EEA currencies 
79. The DLT assessment for non -EEA currencies is carried out using a specific 
approach based on the empirical evidence provided by market information 
on the behaviour of the relevant rates. The empirical evidence is assessed 
using a twofo ld approach (see the Annex to this subsection  for a more 
detailed explanation): 
a. volatility analysis; 
b. analysis of the bid-ask spread.  
The analysis of bid-ask spread is carried out for all currencies using both 
the observed bid -ask spread and also the appro ximation of the Roll 
measure, as applied in EBA’s report on high quality liquid assets (HQLA)4. 
80. The two aforementioned approaches are supported by three toolkits: 
a. Chart analysis,  consisting of  analysis of volatility and analysis of 
bid-ask spread with the Roll measure; 
b. Quantitative analysis; 
c. Qualitative analysis. 
81. Where these approaches do not provide conclusive results, the market is 
not deemed to be  DLT. Consequently, t he interest rate for the affected  
maturity and currency is disregarded as input. 
82. The swap markets for four non-EEA currencies do not  meet the DLT 
requirements. For the time being , according to the Delegated Regulations, 
the risk-free interest rate term structures of those currencies are based on 
government bond rates.  
Table 5. DLT assessment for non-EEA currencies whose risk-free interest 
rate term structures are based on government bonds 
(1 = DLT , 0 = non-DLT)  
Country Currency 1 2 3 4 5 6 7 8 9 10 
Brazil BRL 1 1 1 1 1 1 1 1 1 1 
Colombia COP 1 1 1 1 1 1 1 1 1 1 
India INR 1 1 1 1 1 1 1 1 1 1 
Taiwan TWD 1 1 1 1 1 1 1 1 1 1 
    
                                       
4 Report on appropriate uniform definitions of extremely high quality liquid assets (extremely HQLA) and high quality liquid 
assets (HQLA) and on operational requirements for liquid assets under Article 509(3) and (5) CRR, 
http://www.eba.europa.eu/documents/10180/16145/EBA+BS+2013+413+Report+on+definition+of+HQLA.pdf

29/131 
 
Table 6. DLT assessment for swaps for non-EEA currencies whose term structures are based on swaps (1 = DLT , 0 = 
non-DLT) 
 
Country Currency 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 25 30 35 40 45 50 
Russia RUB 1 1 1 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
Australia AUD 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 
Canada CAD 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 0 1 0 0 0 0 
Chile CLP 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
China CNY 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
Hong Kong HKD 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 
Japan JPY 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 
Malaysia MYR 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 
Mexico MXN 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 
New Zealand NZD 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 
Singapore SGD 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 
South Africa ZAR 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 
South Korea KRW 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 
Thailand THB 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 
Turkey TYR 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
United States USD 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0 0 0 1 1 1 0 1 0 1 
 
From 20 years onwards, only the rates for the maturities shown in the table are applied. 
The table sets out the financial instruments currently used to derive the risk-free interest rates. Past changes to the selection of financial instruments are set 
out in the Annex to section 4.

30/131 
 
4.D. Update of the DLT assessment 
83. EIOPA will update the DLT assessment for the relevant currencies on an 
annual basis. In case of indications that the depth, liquidity or transparency 
of financial market s has significantly changed, EIOPA may update the DLT 
assessment for the affected currencies outside the annual update. 
84. The changes resulting from the DLT assessment will be implemented after a 
warning period of up to three months. The duration of the warn ing period 
will depend on the urgency of the changes and the materiality of their 
impact. Where appropriate, EIOPA will avoid the implementation of changes 
at the end of a quarter. 
85. The update will be based on the methodology for the DLT assessment set 
out in this technical documentation. 
4.E. Currencies without DLT financial instruments 
86. For those currencies where EIOPA does not publish the technical information 
set out in Article 77e of the Solvency II Directive, the methodology 
described in this document should be applied. 
87. In case of lack of reliable financial market data to apply the methodology, it 
is expected that insurance and reinsurance undertakings, the relevant EEA 
supervisor and the supervisor of the corresponding country will have a 
dialogue in order to derive appropriate technical information. 
88. For that purpose the use of the basic risk-free interest rate term structures  
of economies sufficiently similar or inter-linked, may be an option, provided 
that any adjustment to the term structure used as refere nce is made under 
a prudent and objective process, and it is compatible with the methodology 
described in this document.

31/131 
 
5. Credit risk adjustment  
5.A. Legal framework 
89. The calculation of the credit risk adjustment has been developed in 
accordance with recital 20 and Article 45 of the Delegated Regulation.  
5.B. Application of the adjustment 
90. The credit risk adjustment (CRA) is a pplied as a parallel downward shift of 
the market rates observed for maturities up to the last liquid point.  
91. With regard to swaps, t he CRA is applied to the observed par swap rates 
before deriving zero coupon rates. In the case of risk-free interest rate term 
structures based on government bond rates, the input rates are already 
zero coupon rates . The credit risk adjustment is applied to th ose 
government bonds rates. 
92. The credit risk adjustment may lead to negative interest rates (i.e. there is 
no floor for the adjusted rates). 
5.C. Calculation of the credit risk adjustment 
93. The calculation of the CRA considers three possible situations , which are 
successively described below. 
First situation 
94. In the first situation,  the risk-free interest rate term structure is based on 
swap rates and the relevant overnight indexed swap (OIS) rate meets the 
DLT requirements. 
95. In this case  the approach prescribed in Artic le 45 of the Delegated 
Regulation for the credit risk adjustment applies, with the following 
methodological conventions: 
a. The maturity of the OIS rate used to derive the CRA  is consistent 
with the tenor of the floating legs of the swap instrument s used to 
derive the term structure.  
For example, the risk-free interest rate term structure for the 
Swiss franc is based on swaps with floating legs that refer to the 
six month IBOR. Consistently with this, the OIS rate used in the 
CRA calculation is the 6 month Swiss franc OIS rate. 
In the case of the Swedish currency, the risk-free interest rate 
term structure is based on swaps with floating legs that refer to 
the three month IBOR, and consequently the OIS rate used in the 
CRA calculation is the 3 month Swedish krona OIS rate.

32/131 
 
b. For the euro, the OIS rate to be used is the 3 -month rate, as 
specified in recital 20 of the Delegated Regulation. 
c. The calculation of the one-year average referred to in Article 45 of 
the Delegated Regulation is based on daily data for the la st twelve 
months. The average is a simple average calculated giving equal 
weight to all of the observations. 
96. In cases where market data is missing for either the interbank offered rate 
or for the relevant OIS rate, the missing data are completed by  linear 
interpolation and flat extrapolation . If for more than 20% of the business 
days during the preceding year the swap rate or the OIS rate or both are 
missing, it is considered that DLT requirements are not met . In that case  
the third method described in this subsection applies. 
Second situation 
97. The second situation considered for the calculation of the CRA concerns EEA 
currencies that are not in the first situation . For these currencies, the same 
CRA as for the euro applies. 
98. A specific case is the Norwegian k rone. For that currency the CRA for the 
Swedish krona applies. 
Third situation 
99. In the third situation, f or the remainder of currencies the following method 
applies: 
a. A ratio is calculated of the sum of the current interest rates for the 
currency for maturities from 1 to 10 years (numerator) and the sum 
of the current interest rates for the US dollar  and the same 
maturities (denominator). Only maturities meeting DLT 
requirements for both currencies are considered. 
b. The ratio is applied to the CRA for the US do llar before the 
application of the corridor (i.e. after applying the 50% factor).  
c. The credit risk adjustment for the currency is derived by applying a 
corridor of 10 to 35 bps to the output of step (b). 
d. Where the sum of the current interest rates for the US dollar  
referred to in point (a) is zero or negative the CRA is 35 bps. 
e. The rates referred to in point (a) are chosen in line with paragraph 
115. 
100. For all currencies, irrespective of their situation,, the corridor for the CRA to 
swap rates of 10 to 35 bps set out in Article 45 of the Delegated Regulation 
applies. The CRA is rounded to the nearest integer basis points.  The 
rounding is applied in the final step of the calculation.

33/131 
 
5.D. Data sources for the credit risk adjustment 
101. The following table lists the curr encies for which on a monthly basis the 
criterion set out in paragraph 96 is checked . In case there are sufficient  
swap data and overnight indexed swap data, the first situation described 
above applies and the CRA is calculated with interbank offered rates  and 
OIS rates specified in the table.  
Table 7. Currencies with DLT overnight indexed swap markets 
Currency ISO 4217 Bloomberg ticker (PX_LAST) 
Euro  EUR   EUR003M Index   EUSWEC CMPL Curncy  
 Krona   SEK   STIB3M Index   SKSWTNC CMPL Curncy  
 Swiss franc   CHF   SF0006M Index   SFSNTF CMPL Curncy  
 Pound sterling  GBP   BP0006M Index   BPSWSF CMPL Curncy  
 Canadian dollar   CAD   CDOR03 Index   CDSOC CMPN Curncy  
 Yen   JPY   JY0006M Index   JYSOF CMPT Curncy  
 US dollar   USD   US0003M Index   USSOC CMPN Curncy  
Australian dollar AUD BBSW6M Index ADSOF CMPT Curncy 
Hong Kong dollar HKD HIHD03M Index HDSOC CMPT Curncy 
Ringgit MYR KLIB3M Index MRSOC CMPT Curncy 
New Zealand 
dollar NZD NFIX3FRA Index NDSOF CMPT Curncy 
 
Notes:  
 For reference dates a fter 31 May 2015, the overnight swap rates for 
European currencies are based on London fixing (CMPL), for American 
currencies are based on New York fixing (CMPN) and for the currencies 
of Asia and Australia are based on Tokyo fixing (CMPT). For earlier 
reference dates, all overnight swap rates are based on New York fixing, 
irrespective of their currency. 
 
 For the Swiss franc, the Bloomberg ticker SFSWTF is used for reference 
dates until 31 December 2017.

34/131 
 
6. Currency risk adjustment for currencies pegged to the euro 
6.A. Legal framework 
102. According to Article 48 of the Delegated Regulation, the basic risk -free 
interest rate term structure for a currency pegged to the euro should be the 
term structure for the euro, adjusted for currency risk. The Danish krone 
and the Bulgarian lev have been identified as relevant currencies that meet 
the requirements set out in that Article. 
6.B. Application of the adjustment 
103. The currency risk adjustment is applied in addition to, and in the same way 
as the credit risk adjustment (see section 5). 
104. The currency risk adjustment may lead to negative interest rates (i.e. there 
is no floor for the adjusted rates). 
105. The currency risk adjustments for t he Danish krone and the Bulgarian lev  
are currently as follows: 
 1 bp for the Danish krone; 
 5 bps for the Bulgarian lev. 
6.C. Calculation of the adjustment 
106. According to Article 48(2) of the Delegated Regulation, the currency risk 
adjustment should correspond to the cost of hedging against the risk that 
the value in the pegged currency of an investment denomina ted in euro 
decreases as a result of changes in the level of the exchange rate between 
the euro and the pegged currency. 
107. In line with that provision, the currency risk adjustment for the relevant 
currency is based on the following formula: 
TP
RM
Duration
LAC
SCR
BEfCurrencyRA  )0(
 
where:  
 CurrencyRA denotes the currency risk adjustment; 
 f denotes the adjusted currency risk factor for the exchange rate of 
the relevant currency to the euro as set out in the implementing 
technical standard with regard to the adjusted factors to calculate the 
capital requirement for currency risk for currencies pegged to the 
euro; 
 BE denotes the best estimate;

35/131 
 
 SCR(0) denotes the current Solvency Capital Requirement applied to 
calculate the risk margin; 
 LAC denotes the ratio of the adjustment for t he loss -absorbing 
capacity of technical provisions and SCR(0); 
 Duration denotes the modified duration of the technical provisions; 
 RM denotes the risk margin; 
 TP denotes the technical provisions. 
The currency risk adjustment is calculated with regard to in surance and 
reinsurance obligations denominated in the relevant currency. As the 
adjustment should be the same for all insurance and reinsurance 
undertakings, an average adjustment for all undertakings is estimated. 
108. The rationale of the formula is as follows: 
 The cost of hedging against currency risk referred to in Article 48(2) 
of the Delegated Regulation corresponds to the cost of providing 
eligible own funds to cover the SCR for currency risk.   
 The SCR for currency risk is calculated as f·BE·LAC, based on the 
assumption that all the liabilities gives rise to currency risk (i.e. it is 
not hedged) and that the loss -absorbing capacity of technical 
provisions mitigates the risk.  
 The cost of capital for covering the SCR for currency risk is derived by 
multiplying the ratio of the SCR for currency risk and the total SCR by 
the risk margin, resulting in 
RMSCR
LACBEfactor 
)0( . 
 The cost of capital is translated into a change of the discount rate by 
dividing it by the amount and the duration of technical provisions.  
109. The current calibration of the currency risk adjustments for the Danish 
krone and the Bulgarian lev are based on data from EIOPA’s 2014 insurance 
stress test. The following approximation was used for this purpose: 

























NLL
NLL
NLNLLL
NLNLLL
NLL
NLL
TPTP
RMRM
DurationBEDurationBE
LACBELACBE
SCRSCR
BEBEfactor
CurrencRA
)0()0(
 
where the subscripts L and NL identify amounts that relate to life and non -
life insurance obligations respectively.

36/131 
 
6.D. Update of the adjustment 
110. EIOPA will monitor the currency risk adjustment on an annual basis by 
means of the formula set out in paragraph 107. The curren cy risk 
adjustment will only be amended where the difference to the formula result 
is material. When updates are necessary they will be implemented end -
January.

37/131 
 
7. Extrapolation and interpolation 
7.A. Extrapolation and interpolation method 
111. For each currency the  basic risk -free interest rate term structure is 
constructed from risk-free interest rates for a finite number of maturities. 
Both the interpolation between these maturities, where necessary, and the 
extrapolation beyond the last liquid point are based on  the Smith-Wilson 
methodology. This methodology is described in subsection 7.E. 
112. The control input parameters for the interpolation and extrapolation are the  
last liquid point, ultimate forward rate (UFR), the convergence point and the 
convergence tolerance. These parameters are specified in subsection s 7.B 
to D. The control parameters will not be updated on a monthly basis. 
113. In order to apply the Smith -Wilson method, a  cash-flow matrix is derived 
from the observed market interest rate data.  This is further ex plained in 
subsection 7.F. The Smith-Wilson method takes care that the present value 
function of the derived term structure exactly agrees with the empirical data 
for the observable maturities. 
114. If the reference instruments are swap rates, the market intere st rates to be 
used as input s are the swap par rates after deduction of the credit and 
currency risk adjustments described in section s 5 and 6. If the reference 
instruments are zero coupon government bonds, the market interest rates 
to be used as inputs are the zero coupon rates after deduction of the credit 
and currency risk adjustments. 
115. The derivation of the term structures is based on the rates for the DLT 
maturities set out in section 4. Where for a certain day one or several of 
those rates are not avai lable, the term structure is derived on the basis of 
the remaining rates, provided that not more than 20% of rates are missing 
and the rate at the last liquid point is available.  Otherwise, the market 
information of the preceding trading day is used  to der ive the term 
structure.  
116. EIOPA publishes the risk-free interest rates for  integer maturities from one 
year to 150 years.  
7.B. Last liquid point  
117. Recital 21 of the Delegated Regulation defines a criterion (referred to as the 
residual volume criterion) to calculate the LLP. The residual volume criterion 
is used to derive the LLP for the euro only. For that currency, it gives an LLP 
of 20 years. 
For all other currencies, the LLP has been chosen according to the results of 
the DLT assessment . It is the longest matu rity for wh ich risk-free interest 
rates can be derived from DLT markets.

38/131 
 
 
Table 8. Last liquid points of EEA currencies 
 Currency LLP 
EUR euro 20 
BGN lev 20 
CHF Swiss franc 25 
CZK Czech koruna 15 
DKK Danish krone 20 
GBP pound sterling 50 
HRK kuna 9 
HUF forint 15 
ISK króna 8 
NOK Norwegian krone 10 
PLN zloty 10 
RON leu 10 
SEK krona 10 
 
Table 9. Last liquid points of non-EEA currencies 
AUD Australian dollar 30 
BRL real 10 
CAD Canadian dollar 30 
CLP Chilean peso 10 
CNY renminbi-yuan 10 
COP Colombian peso 10 
HKD Hong Kong dollar 15 
INR Indian rupee 10 
JPY yen 30 
KRW South Korean won 20 
MYR ringgit 20 
MXN Mexican peso 20 
NZD New Zealand dollar 20 
RUB Russian rouble 10 
SGD Singapore dollar 20 
THB baht 15 
TRY Turkish lira 10 
TWD new Taiwan dollar 10 
USD US dollar 50 
ZAR rand 15 
 
118. The LLP will be updated together with the DLT assessment.

39/131 
 
7.C. Ultimate forward rate 
119. The methodology to derive the UFRs is set out in the Annex to this 
subsection. The UFRs will be calculated in accordance with  that 
methodology on an annual basis and  updated when they are sufficiently 
different from the then applicable UFRs. 
 
7.D. Convergence point and tolerance 
120. The convergence point is the maximum of (LLP+40) and 60 years . 
Consequently, the convergence period is the maximum of (60-LLP) and 40  
years. 
121. The parameter alpha that controls the convergence speed is set at the 
lowest value that produces a term structure  reaching the convergence 
tolerance of the UFR by the convergence point . The convergence tolerance 
is set at 1 bp . A lower bound for alpha is set at 0.05. The convergence 
criterion is assessed by EIOPA with a scanning procedure with six decimals 
precision for alpha. The method for deriving alpha is illustrated in the Excel 
tool “Smith-Wilson Risk-free Interest Rate Extrapolation” that can be found 
on EIOPA’s website. 
122. In accordance to recital 30 of the Omnibus II Directive, is is possible to 
account for  specific cases  in the derivation of the convergence period , 
provided they are adequately justified. In view of the characteristics of the 
Swedish bond market, EIOPA has decided to use  a convergence period of 
ten years for the Swedish krona. 
 
 
 
7.E. Description of the Smith-Wilson method with intensities 
An interest trinity 
123. By way of introduction,  an annual interest rate r is considered that defines 
an annual interest factor R=(1+r). From this a continuous -time interest 
intensity =log(R) can be defined.5 Negative interest rates are allowed, but 
the conditions r>1 or R>0 should be met . Only the interest intensity  is 
                                       
5 The “log” function is to be understood as the natural logarithm. This is the case throughout the 
document.

40/131 
 
unrestricted and this makes it convenient for modelling purposes. In this 
documentation the concise term intensity instead of instantaneous rate or 
infinitesimal rate is used to avoid ambiguity with annualised interest rates. 
 
Another trinity 
124. With a constant  the present value of an amount of 1 maturing after v 
years would be just p(v)=exp(v). Since interest intensities usually depend 
on the term to maturity , it is of interest to analyse present value with 
changing interest intensity. The yield intensity function is what would be the 
average flat interest intensity: 
 
125. The forward intensity function measures the change in the present value 
function: 
 
126. The yield function can also be written as an averaged integral of the forward 
function: 
 
127. For the forward and yield curve there holds that y(0)=f(0), the zero spot 
intensity. Also in the limit y()=f() is obtained , what is the ultimate 
forward intensity. Furthermore any turning point of the yield curve will be 
crossed by the forward curve. This similarity with average and marginal cost 
curves is mentioned by McCulloch (1971), page 24.6 
128. A parallel shock in the forward intensity curve will translate as the same 
parallel shock in the yield intensity curve. This property does not transpose 
to annualised interest rates, however. 
 
A Simple Econometric Model 
129. Nelson & Siegel (1987)7 proposed as a model for the forward intensity: 
                                       
6 McCulloch, J Huston, 1971. ”Measuring the term structure of interest rates”. 
The Journal of Business, University of Chicago Press vol. 44(1) 19-31, January.  
7 Nelson, Charles R & Siegel, Andrew F, 1987. ”Parsimonious Modelling of yield curves”.  
The Journal of Business, University of Chicago Press vol. 60(4) 473-489, October.  
  v
vpvyvyvvp )(log)(              )(exp)( 
)(
)(
d
)(logd)( vp
vp
v
vpvf 

v
zzfvvy
0
d)(1)(

41/131 
 
 
130. The implied yield curve follows as an averaged integral using the formula of 
paragraph 126: 





 




  

v
vv
ev
e
v
evy 

 11)( 321
 
and the implied present value function follows using the formula of 
paragraph 124: 





 




  

v
v
veevvp 

 3321
1)(exp)(
 
131. Diebold & Li (2006) 8 extend this Nelson -Siegel model by incorpo rating a 
change process through calendar time t. This enables them to forecast 
future yield curves.  Compared with Ne lson-Siegel, Smith & Wilson (2001) 9 
start the other way around. They propose  a model for the present value 
function, from which the yield and forward intensity function follow. The 
specification of this present value function needs a special type of functi on, 
known as Wilson function, that we will focus on next. 
 
Wilson function 
132. The Wilson function W(u,v) can be specified as: 
 
where H(u,v) is the heart of the Wilson function: 
   
2
||)(            
2),min(            
),min(sinh),max(exp),min(),(
||)(
||)(
vuvu
vuvu
evuevu
eevu
vuvuvuvuH










 
133. Here  and  are parameters that have a dimension reciprocal to that of the 
time duration to maturity u and v that we take the year, and measured as 
number of days divided by 365.25. 
                                       
8 Diebold, Francis X & Li, Canlin (2006). ”Forecasting the term structure of government bond 
yields”. Journal of Econometrics vol. 130 337-364. 
9 Smith, A & Wilson, T (2001). ”Fitting yield curves with long term constraints”. 
London: Bacon & Woodrow. 
vv veevf     321)(
vuvu evuHevuHevuW    ),(),(),( )(

42/131 
 
134. The parameter  denotes the ultimate forward intensity and takes the value 
log(1.042) in case the ultimate forward rate equals 4.2% . The parameter  
controls the speed of convergence to this asymptotic level.   
135. This H-function and its first two derivatives happen to be continuous at 
v=u: 
   ),min(sinh),max(exp),min(),( vuvuvuvuH  
 
Differentiation with respect to v gives: 




 

vuue
uvvevuGv
vuH
v
u
                           )sinh(
                    )cosh(),(d
),(d




 
For the second order derivative the following is obtained: 
),min(),(d
),(d 32
2
2
vuvuHv
vuH  
 
However, the third derivative shows a discontinuity at u=v. 
 
Matrices and vectors 
136. Matrices and vectors will be boldface. Transposition is indicated by a prime 
and 
 denotes element-wise multiplication of conformable matrices. 1 and 0 
will denote column vectors with all components equal to 1 and 0 
respectively, and of appropriate order. 
137. A vector u for the m observed durations to maturity is introduced, as well 
as an mn matrix C that for the cash-flows of the n financial instruments: 
 
The derivation of these items is explained in the following sub-section 7.F. 
138. Nonlinear functions of vectors will indicate by square brackets the 
component-wise operation as in: 
 
 
139. An auxiliary matrix 
CdQ  will be needed where the subscript  denotes 
transforming a column vector into a diagonal matrix such that 
d1d  . 
0                      
21
22221
11211
2
1


























 ij
mnmm
n
n
m
c
ccc
ccc
ccc
u
u
u




 Cu




















































mmm uu
uu
uu
m
u
u
u
ee
ee
ee
up
up
up
p
e
e
e








22
11
2
1
2
12
1
]sinh[          
)(
)(
)(
][          ]exp[ uuud

43/131 
 
Furthermore there are the following  three column vectors with n 
components: 
dC1Qqpb 







































nnn q
q
q
p
p
p
b
b
b

2
1
2
1
2
1
                    
 
Here b is an auxiliary matrix and  p contains the n observed market prices 
for the n financial instruments that will be compared with the m 
components of the present values in p[u]. 
140. The data can be stored in an ( m+1)(n+1) tableau containing C bordered 
by u and the transpose of p: 
 
Without loss of generality the rows of this tableau may be ordered according 
to the components of u such that there holds 
.21 muuu   Likewise the 
columns of this tableau can be ordered such that C will be as u pper-
triangular as possible. Such a canonical format will be useful for validation 
purposes but is not of any importance for the mathematical formulations. 
141. Zero-rows in C can be deleted from the tableau without loss of generality. 
In case of non-deletion this will imply zero components in the output vector 
Qb at the appropriate places. 
142. The tableau, whether canonical or not, can be normalized by dividing the 
columns by the appropriate component of p, that is post -multiplying with 
the inverse of  
 
143. In case o f zero -coupon bonds, the canonical format makes C a diagonal 
matrix that can be normalized to the identity matrix I resulting in a 
canonical normalized tableau: 



 
uI
p
 
144. Of course, this case does not need a data tableau, but just u and p. In what 
follows data are  not assume d to have  a canonical or normalized format, 
such that the exposition holds in full generality. 
 
Wilson matrix and H-matrix  



 
uC
p
:p



 

 uCp
1
1

44/131 
 
145. On that basis of the definitions made above, the following can be displayed:  
 
 
ddHHddWuuW   ),(
 
146. The symmetric matrices W and H will be positive definite as soon as u 
contains distinct positive components. Implementation of the method with 
H is simpler as it only depends on  and not on . 
 
Smith-Wilson present value function 
147. This function, also known as discount pricing function, can be displayed as: 
 
where the values for u correspond to the observed durations to maturity of 
the financial instruments and v is the duration to maturity of the present 
value function.  
148. A set of equations can be formed by having v the values of u: 
HQbddCbHdddW CbdW Cbuu    ]exp[][ p
 
Pre-multiplication with the transpose of C gives n linear equations in b: 
 
149. p is the market observable counterpart of  
HQbQqp 
 
From this follows the solution for b: 
)()( 1 qpHQQb  
 
This solution depends on  through Q and q as well as on  through H. The 
value for  will be determined through convergence requirements. 
 
Smith-Wilson for zero-coupon bonds 
150. When m=n, the cash-flow matrix C may be taken as the identity matrix and 
we are in the zero -coupon bond case. The present value function simplifies 
as: 
 
),(
),(),(),(
),(),(),(
),(),(),(
),(          
21
22212
12111
2
1
vuWuvWv 


























mkkk
m
m
k uvWuvWuvW
uvWuvWuvW
uvWuvWuvW
v
v
v





  ),(),(),(),(),( 21 vuvWuvWuvWv m uWuW  
QbuHCbuW ),(),()( veevevp vvv   
HQbQqW CbCdCuC  ][p
][uC p
  bdbbuH   ~          where          ~),(1)( vevp v

45/131 
 
and the calculation for  the coefficient vector  
 1upHb   ]exp[~ 1 
 
 
Smith-Wilson yield and forward intensity function 
151. From paragraph 147 the yield intensity function follows as: 
  
The forward intensity function follows as: 
QbuH
QbuGQbuH
),(1
),(
d
)),(1log(d
d
)(logd)( v
v
v
v
v
vpvf  
 
where the components of the row vector G(v,u) follow from paragraph 135. 
152. As H(u,v) has a continuous second order derivative, it can be  concluded 
that the Smith-Wilson present value and yield curve are sufficiently smooth 
at the nodes given by the observed liquid maturities. However, the forward 
intensity curve is less smooth as it does not have a continuous second order 
derivative at these nodes. 
 
Zero spot intensity 
153. When , paragraph 135 implies: 
 
For 
0v the following is obtained: 
]exp[)0,(          )0,(),0( u1uG0uHuH  
 
From this the zero spot intensity follows from paragraph 151 as: 
QbuQb1 ]exp[)0()0(  fy
 
 
Analysis of convergence to ultimate forward intensity  
154. When 
)max(u Uv  paragraph 135 implies: 
]sinh[),(          ]sinh[),( uuGuuuH   vv evev  
 
155. Now, the upper end of the forward intensity function reduces to: 
Uvevf v            1)( 

 
where  is a quasi-constant that depends on  (and ) but not on v: 
v
v
v
vpvy )),(1log()(log)( QbuH 
)min(uv
]exp[)cosh(),(),( u1uGuG   vvv

46/131 
 
Qbu
Qbu
]sinh[
1

 

 
If  is such that =0, then 
)(vf , irrespective of the value of v and 
the ultimate forward intensity
)(f  will not approach .   
156. The value of  is determined by requirements on the convergence speed 
and will automatically be chosen in such a way that ≠0.  
157. Adopting a convergence period 𝑆=max⁡(40,60−𝑈) implies a point of 
convergence T as follows: 
𝑇=𝑈+𝑆=max⁡(𝑈+40,60)  
158. The convergence gap at the point of convergence T can be analysed as a 
function of : 
|1||)(|)( TeTfg 
 
 
and the problem of determining  can be formulated as a nonlinear 
minimization problem: 
Minimize  
with respect to  
 subject to the two inequality conditions: 
(1) 
a  with the lower bound 
a =0.05 
(2) 
 )(g  
159. A heuristic solution strategy is the following: 
 
optimal is    then      )(     implies       if aga    
 
  )(ga   that such  for  search else  
 
160. Without the lower boundary to alpha,  the second inequality 
 )(g  should 
not be rewritten as 
|1| Te   because it might favour a false root for  
approaching the value 0. 
7.F. Fitting the term structure to bond and swap rates 
161. With the Smith-Wilson method the term structure can be fitted to the rates 
of all the relevant financial instruments. 
162. For e ach set of instruments the input for the Smith -Wilson metho d is 
defined by: 
 the vector of the market prices of the n instruments at valuation date,

47/131 
 
 the vector of the m different cash payment dates up to the last maturity, 
and  
 the mn matrix of the cash-flows of the instruments at these dates.  
163. We will now look a t this input when the term structure  is fitted to zero  
coupon bond rates, coupon bond rates and par swap rates. 
 
Instruments Market prices p Cash payment dates u Cash-flow matrix C 
Zero 
coupon 
bonds 
 Market prices 
of the n input 
instruments, 
given as the 
percent 
amount of the 
notional 
amount 
 The market 
prices of the 
zero coupon 
input bonds 
translate at 
once into spot 
rates for input 
maturities  
 The cash payment 
dates are the 
maturity dates of 
the n zero coupon 
input bonds (i.e. 
m=n) 
 An nn matrix 
with entries:  
- cij =1 for i=j, 
- cij =0 else. 
 C is the identity 
matrix. 
Coupon 
bonds 
 Market prices 
of the n 
coupon input 
bonds, given 
as the percent 
amount of the 
notional 
amount of the 
bond. 
 The cash payment 
dates are, in 
addition to the 
maturity dates of 
the input bonds all 
coupon dates.  
 
 
 An mn matrix 
with entries:  
- cij =rc(i)/s, i<t(j) 
- ct(j),j =1+rc(i)/s, 
- cij=0, i>t(j), 
where rc(i) is the 
coupon rate of 
bond i, s is the 
settlement 
frequency and t(j) 
the maturity of 
bond j. 
Par swap 
rates 
 The market 
prices of the n 
par swap input 
instruments 
are taken as 
unit (i.e. 1). 
 To receive the 
swap rate, a 
floating rate 
 The cash payment 
dates are, in 
addition to the 
maturity dates of 
the swap 
agreements all 
swap rate payment 
dates. 
 An mn matrix 
with entries:  
- cij =rc(i)/s, i<t(j) 
- ct(j),j =1+rc(i)/s, 
- cij =0, i>t(j), 
where rc(i) is the 
swap rate of

48/131 
 
 
A numerical illustration is provided in Annex 14.E. 
  
has to be 
earned, that 
can be 
swapped 
against the 
fixed rate. To 
earn the 
variable rate a 
notional 
amount has to 
be invested. At 
maturity, the 
notional 
amount is de-
invested.  
 
 
agreement i, and 
s is the settlement 
frequency  and 
t(j) the maturity 
of arrangement j.

49/131 
 
Volatility and matching adjustment 
8. Introduction: Conceptual Framework. 
164. According to Article 77e of the Solvency II Directive: 
EIOPA shall lay down and publish for each relevant currency the 
following technical information at least on a quarterly basis:  
[…] 
(b) for each relevant duration, credit quality and asset class a 
fundamental spread for the cal culation of the matching 
adjustment referred to in Article 77c(1)(b);  
(c) for each relevant national insurance market a volatility 
adjustment to the relevant risk -free interest rate term structure 
referred to in Article 77d(1) 
165. This part of the technical documentation describes how EIOPA derives the 
technical information mentioned above, in accordance with Articles 77b, 77c 
and 77d of the Solvency II Directive and Articles 49 to 54 of the Delegated 
Regulation.    
166. The deriv ation of  the volatility adjustments  and fundamental spreads 
requires decisions on the following: 
a. The range and granularity of asset classes, credit quality steps and 
durations for which the risk corrections of the volatility adjustment 
and the fundamental spreads are calculated 
b. The source data for the probability of default (PD) calculation 
c. The method of deriving PD from source data 
d. The source data for the cost of downgrade (CoD) calculation 
e. The method of deriving CoD from source data 
f. The s ource data for the long-term average of spreads ( LTAS) 
calculation 
g. The m ethod of constructing missing data of the  30 year spread 
history 
h. The treatment of currencies for which source data are not available 
 
167. The methodology to derive the volatility adjustment and the fundamental 
spread, including the aforementioned decisions, is explained in the following 
sections.

50/131 
 
8.A. Conceptual framework of the volatility adjustment 
168. The volatility adjustment (VA) is an adjustment to the relevant risk -free 
interest rate term structure . The VA is based on 65% of the risk -corrected 
spread between the interest rate that could be earned from bonds, loans 
and securitisations included in a reference portfolio for , and the basic risk -
free interest rates. 
169. The VA is derived per relevant currency. It is the same for all insurance and 
reinsurance obligations of a currency  unless a country specific increase 
applies. The following sub section explains the calculation of the VA before 
application of any country-specific increase (currency volatility adjustment). 
The subsequent sub section sets ou t the calculation of the country-specific 
increase. 
8.A.1. Currency volatility adjustment 
170. In order to determine a currency volatility adjustment, the following inputs  
are used: 
a. A currency representative portfolio 10 of bonds , securitisations, 
loans, equity and prop erty covering the best estimate of insurance 
and reinsurance obligations denominated in that currency, based on 
insurance market data collected by the means of the regulatory 
reporting; 
b. A currency reference portfolio of yield market indices based on 
the af orementioned representative portfolio. The expression yield 
market indices covers in this section both yield curves and indices 
on yields. 
171. Those inputs are used to calculate the following outputs: 
a. the currency spread S between the interest rate derived fro m the 
reference portfolio of indices and the rates of the relevant basic 
risk-free interest rate term structure; 
b. the portion of the currency spread S, denoted RC for risk 
correction, which corresponds to “the portion of the spread that is 
attributable to a  realistic assessment of expected losses, 
unexpected credit risk or any other risk, of the assets” in the 
reference portfolio (Article 77d of the Solvency II Directive); 
                                       
10 Article 49 of the Delegated Regulation provides that “the [reference] portfolio is based on relevant indices”. In 
order to compose the reference portfolio of indices, EIOPA needs to build first a representative portfolio of 
assets.

51/131 
 
c. the risk-corrected currency spread , which corresponds to the 
difference between the spread S and the risk correction RC. 
172. In accordance with Article 50 of the Delegated Regulation , the  spread S 
before risk correction is equal to the following: 
𝑆=⁡𝑤𝑔𝑜𝑣⁡.max(𝑆𝑔𝑜𝑣;0)+⁡𝑤𝑐𝑜𝑟𝑝.max(𝑆𝑐𝑜𝑟𝑝;0) 
where: 
a. 𝑤𝑔𝑜𝑣 denotes the ratio of the value of government bonds included in 
the reference portfolio of assets for that currency and the value of 
all the assets included in that  reference portfolio (see also section 
9.D); 
b. 𝑆𝑔𝑜𝑣 denotes the average currency spread on government bonds 
included in the reference portfolio of assets for that currency; 
c. 𝑤𝑐𝑜𝑟𝑝 denotes the ratio of the value of bonds other than government 
bonds, loans and securitisations  included in the reference portfolio 
of assets for that currency or country and the value of all the assets 
included in that reference portfolio (see also section 9.D); 
d. 𝑆𝑐𝑜𝑟𝑝 denotes the average currency spread on  bonds other than 
government bonds , loans an d securitisations included in the 
reference portfolio of assets for that currency. 
173. Here and in the following sections ‘government bonds’ means exposures to 
central governments, central banks and exposures to regional governments 
and local authorities that are treated as central governments. 
174. The risk correction RC is equal to the following: 
𝑅𝐶=𝑤𝑔𝑜𝑣⁡.max⁡(𝑅𝐶𝑔𝑜𝑣,0)⁡+⁡𝑤𝑐𝑜𝑟𝑝⁡.max⁡(𝑅𝐶𝑐𝑜𝑟𝑝,0) 
where: 
a. 𝑤𝑔𝑜𝑣 and 𝑤𝑐𝑜𝑟𝑝  are defined as above;  
b. 𝑅𝐶𝑔𝑜𝑣 denotes the risk correction corresponding to the portion of the 
spread 𝑆𝑔𝑜𝑣 that is attribut able to a realistic assessment of the 
expected losses, unexpected credit risk or any other risk; 
c. 𝑅𝐶𝑐𝑜𝑟𝑝 denotes the risk correction corresponding to the portion of the 
spread 𝑆𝑐𝑜𝑟𝑝 that is attributable to a realistic assessment of the 
expected losses, unexpected credit risk or any other risk. 
175. The risk-corrected currency spread 
RC
crncyS  is equal to the following: 
     
RCSS RC
crncy 

52/131 
 
The risk-corrected currency spread may be negative when  𝑅𝐶>𝑆. The zero floor 
mentioned in Article 50 of the Delegated Regulation only applies at portfolio level 
to the spread before the risk correction. 
176. For each relevant currency, the currency VA is equal to the following: 
    
RC
crncycrncy SVA  65.0  
Therefore also the currency VA may be n egative. The following table 
summarizes the application of floors in the process of calculation of the 
currency VA: 
 
 Market spread Risk correction Risk-corrected spread 
For each 
individual 
bond 
No floor  - spread 
may be either 
positive or 
negative 
For each individual 
bond and hence at 
portfolio level as 
well, the risk 
correction cannot be 
negative  
 
No floor – risk-
corrected spread may 
be negative 
At portfolio 
level 
Floor at zero -  
spread cannot be 
negative 
No floor – risk-
corrected spread may 
be negative 
 
8.A.2. Country specific increase of the volatility adjustment 
177. For each relevant country, the currency volatility adjustment is increased by 
the difference between the risk -corrected country spread  
RC
countryS  and twice 
the risk-corrected currency spread, whenever that difference is positive and 
the risk-corrected country spread is higher than 100 basis points.  
178. In order to determine the country specific increase of the volatility 
adjustment, the following inputs are used: 
a. A country representative portfolio of bonds, securitisations, 
loans, equity and property covering the best estimate of obligations 
sold in that country,  based on insurance market data collected by 
the means of the regulatory reporting; 
b. A country reference portfolio  of indices bas ed on the 
aforementioned representative portfolio. 
179. Those inputs are used to calculate the following outputs: 
a. the country spread S between the interest rate derived from the 
reference portfolio of indices and the rates of the relevant basic 
risk-free interest rate term structure; 
b. the portion of the country spread S, denoted RC for risk 
correction, which corresponds to “the portion of the spread that is 
attributable to a realistic assessment of expected losses,

53/131 
 
unexpected credit risk or any other risk, of the  assets” in the 
reference portfolio (Article 77d of the Solvency II Directive); 
c. the risk-corrected country spread ,  which corresponds to the 
difference between the spread S and the risk correction RC. 
180. The country spread, risk correction and risk -corrected country spread 
RC
countryS  
are calculated in the same way as the currency spread, risk correction and 
risk-corrected spread 
RC
crncyS  for the currency of that country, but based on 
the inputs stemming from the country representative  portfolio and the 
country reference portfolio.  
181. For each relevant country, a country specific increase of the volatility may 
also apply, in such a manner that the total volatility adjustment is equal to:  
𝑉𝐴𝑡𝑜𝑡𝑎𝑙=⁡0.65∙(𝑆𝑐𝑟𝑛𝑐𝑦𝑅𝐶 +⁡max(𝑆𝑐𝑜𝑢𝑛𝑡𝑟𝑦
𝑅𝐶 −2.𝑆𝑐𝑟𝑛𝑐𝑦𝑅𝐶 ;0)) 
where 𝑆𝑐𝑜𝑢𝑛𝑡𝑟𝑦
𝑅𝐶  > 100 basis points. 
 
182. Where 𝑆𝑐𝑜𝑢𝑛𝑡𝑟𝑦
𝑅𝐶  is lower than or equal to 100 basis points, there is no country 
specific increase of the volatility adjustment. That mea ns we have:  
 
𝑉𝐴𝑡𝑜𝑡𝑎𝑙=⁡0.65∙𝑆𝑐𝑟𝑛𝑐𝑦𝑅𝐶  
 
8.A.3. Publication of the volatility adjustment 
183. According to Article 77d of the Solvency II Directive, the volatility 
adjustment is not an entity -specific adjustment. Its value should be the 
same for all the insurance or reinsurance obligations expressed in the same 
currency or, where  the country specific increase applies , relating to the 
same country.  
184. There is not a volatility adjustment at group level. The influence of the 
volatility adjustment at grou p level will be derived from the volatility 
adjustment applied by each component of the group, according to the 
method of calculation of the group solvency. 
 
8.B. Conceptual framework of the matching adjustment 
185. The matching adjustment (MA) is an adjustment to t he basic risk -free 
interest rate, based on the spread on a n undertaking’s own portfolio of 
matching assets , less a fundamental spread that allows for default and 
downgrade risk.

54/131 
 
186. Undertakings must calculate the MA themselves, based on their own 
assigned portfolios of eligible assets. Rather than publishing the MA, EIOPA 
publishes only the fundamental spreads that undertakings should use, 
together with the following information: 
a. for assets other than government bonds, the probability of default 
(PD) to use in  the de -risking of the cash flows of th e assigned 
assets, 
b. the probability of default expressed as a part of the spread used to 
calculate the fundamental spread,  
c. the cost of downgrade (CoD), 
d. the long-term average spread (LTAS). 
187. For corporate bonds  the fund amental spread is calculated a s FS = 
max(PD+CoD, 35%·LTAS ). Consequently, t he fundamental spread is not 
always the sum of PD and CoD. Where the floor relating to the LTAS applies 
the fundamental spread is larger than that sum. In general, the MA should 
be calculated on the basis of the amount FS – PD = max(CoD, 35%·LTAS – 
PD).  
188. EIOPA publishes both the probability of default and cost of downgrade for 
each relevant asset class, duration and credit quality step.  
189. The steps involved in calculating the Matching  Adjustment are set out in 
Article 77c of the Solvency II Directive and Articles 52 to 54  of the 
Delegated Regulation.  
190. For each relevant currency, the Matching Adjustment for an undertaking will 
be a single number expressed in basis points. This single nu mber should be 
added to the basic risk-free interest rate term structure for that currency at 
all maturities (i.e. it should be applied as a parallel shift of the whole of the 
basic risk-free interest rate term structure).

55/131 
 
9. Deriving the representative portfolios of bonds and the 
reference portfolios of ‘ yield market indices ’ for the Volatility 
Adjustment 
9.A. Introduction 
191. The organization of this section follows the conceptual framework described 
in the previous section. In subsection B  the relationship among th e 
representative portfolios applied for the currency VA and the country  
specific increase of the  VA is explained. In subsection C  the calculation of 
the representative portfolio of government bonds and  the representative 
portfolio of other assets is introduced. In subsection D the weights referred 
to in Article 50 of the Delegated Regulation are set out. In subsection E the 
calculation of the reference portfolios of ‘yield market indices’ is specified for 
the representative portfolio of government bonds and  the representative 
portfolio of other assets. 
192. For the purpose of the preparatory phase in 2015  and the beginning of 
Solvency II in 2016, the data collected to build the representative portfolios 
were taken from the EIOPA Stress Test 2014  exercise. In 2016  the 
representative portfolios were updated on the basis of data reported by 
insurance and reinsurance undertakings to their supervisory authority 
during the preparatory phase for Solvency II. In the annex to section 9.D 
the methodology for the update is described.  
193. EIOPA intends to  update the representative portfolios at the end of the  
year, on the basis of  the annual supervisory reporting of insurance and 
reinsurance undertakings and of insurance groups in accordance with t he 
methodology set out in this t echnical documentation. The insurance market 
data referred to year end N -1, (which undertakings will report in year N ) 
will be used for the calculation of the technical information t hat 
undertakings should apply  with reference to their situation at the end  of 
year N.  Updated insurance market data will be published at least three 
months before the year end N. 
 
31-12-(N-1) 
Submission of 
reporting as of 
31-12-(N-1)  
first half year 
 
Publication of updated 
insurance market data 
(no later than 30-09-N) 
Use of the new 
insurance market data 
in the calculation of VA 
as of 31-12-N

56/131 
 
194. EIOPA will review this timeline for the annual update by the end of 2016.  
For a limited period of time, the date of pub lication of the updated 
representative portfolio may be deferred from 30 September to a later date, 
while maintaining a three -month alert period until the updated 
representative portfolios are used in the calculation of the VA.  
9.B. Introductory remarks on the  representative portfolios  
applied in the calculation of the currency volatility 
adjustment and in the calculation of the country specific 
increase of the volatility adjustment. 
195. According to Article 77d of the Solvency II Directive, the currency volatility 
adjustment shall be based on a reference portfolio “ representative for the 
assets which are denominated in that currency and which insurance and 
reinsurance undertakings are invested in to cover the best estimate for 
insurance and reinsurance obligations denominated in that currency”.  
196. According to the same Article, the country specific increase of the volatility 
adjustment shall be based on a reference portfolio “ representative for the 
assets which insurance and reinsurance undertakings are invested in to  
cover the best estimate for insurance and reinsurance obligations sold in the 
insurance market of that country and denominated in the currency of that 
country”.  
197. Therefore, the  scope of assets to include in the currency and country 
representative portfoli os is different . However, in the Solvency II 
framework, insurance and reinsurance undertakings are not required to 
identify the assets covering their best estimate (except in the case of those 
covering insurance and reinsurance obligations applying the mat ching 
adjustment or under a ring fenced fund regime). It is also not required to 
classify the assets covering the best estimate of the insurance or 
reinsurance obligations according to the country where the  obligations are 
sold.  
198. In order to implement Arti cle 77d of the Solvency II Directive in the 
simplest possible manner EIOPA applies the following proxies: 
a. For the currency representative portfolio: A calculation considering 
that all assets in a currency X cover liabilities in currency X . Hence, 
the currency representative portfolio of currency X is based on all

57/131 
 
assets denominated in that currency X and in which undertakings 
are invested in.11  
b. For the country representative portfolio: A calculation conside ring 
that all liabilities are sold in the country o f the undertaking and 
denominated in the currency of that country . Hence, the country 
representative portfolio of country A is based on all assets in which 
undertakings established in that particular country are invested in.  
199. These assumptions will be moni tored in the future and also they  may be 
removed when there is evidence to the contrary (e.g. for a certain market). 
The evidence used to remove either or both  of these assumption s will be 
centrally validated by EIOPA. 
200. The calculation of the two different sets of reference portfolios (currency VA 
and country specific increase of the VA, respectively) is feasible for the EEA 
currencies, since the information contained in the individual reporting at 
solo level provides the data necessary for the purpose. 
201. In t he case of non -EEA currencies, the information contained in the 
reporting at group level allows a proxy only for the calculation of the 
currency volatility adjustment. Therefore for non -EEA currencies, the only 
currently feasible approach is to apply the portfolios used for the calculation 
of the currency adjustment also for the country specific increase of the 
volatility adjustment. 
 
 
9.C. Representative portfolios of assets referred to in Article 
50 of the Delegated Regulation 
202. The derivation of the representative portfolios is based in particular on the 
following information: 
a. The market value  of the assets included in the representative 
portfolio. Those market values are required to calculate the weights 
𝑤𝑔𝑜𝑣 and 𝑤𝑐𝑜𝑟𝑝 and the risk-corrected spread 𝑆𝑅𝐶. 
b. The duration of the bonds, loans and securitizations included in the 
representative portfolio. Those durations are required to make the 
spread S maturity-dependent and to select the rele vant yield 
market indices. 
                                       
11  Therefore, the representative portfolio for a currency X may include as issuer country Y with a 
different currency, when country Y issued bonds expressed in currency X and hold by undertakings 
in country X.

58/131 
 
c. The asset class, understood as economic sector (financial sector or 
non-final sector) of the bonds other than government bonds, loans 
and securitizations included in the representative portfolio.   
Government bonds are distinguish ed according to issuer to form 
asset classes. The asset classes are required to select the relevant 
yield market indices. 
d. The credit quality step (on a scale from 0 to 6) of the bonds other 
than government bonds, loans and securitizations included in the 
representative portfolio. Those credit quality steps are required to 
calculate the spread S and the risk correction RC and to select the 
relevant yield market indices.   
203. On the basis of th at information, the aggregated market value and the 
average duration per asset class and credit quality step can be calculated 
for each currency and country . The weights for the determination of the 
average duration are the market values of the assets. 
 
9.D. The portfolio weights referred to  in Article 50 of the 
Delegated Regulation 
 
204. The weights wgov and wcorp applied for the calculation of the volatility 
adjustments for EEA currencies and countries since 30 September 2016 are 
set out in the following table . The derivation of the weights is described in 
the annex to this section. 
Table 10. EEA currencies and countries. Weights referred to in 
Article 50 of the Delegated Regulation 
Weights for the currency 
representative portfolios 
 Government 
bonds 
Other 
assets 
EUR 27.4% 43.8% 
BGN 23.5% 2.3% 
CHF 23.8% 51.4% 
CZK 50.8% 15.6% 
DKK 19.3% 61.9% 
GBP 19.4% 33.1% 
HRK 29.6% 6.7% 
HUF 55.4% 15.1%

59/131 
 
ISK 77.2% 9.3% 
NOK 12.0% 59.5% 
PLN 38.4% 20.7% 
RON 64.8% 6.7% 
SEK 12.1% 31.1% 
 
Weights for the country 
representative portfolios 
 Government 
bonds 
Other 
assets 
AT 18.3% 46.5% 
BE 48.7% 34.2% 
BG 53.3% 18.5% 
CY 5.5% 42.5% 
CZ 52.3% 27.4% 
DK 19.3% 61.9% 
EE 24.2% 42.4% 
FI 8.2% 38.3% 
FR 27.0% 46.9% 
DE 15.6% 55.2% 
GR 32.9% 33.1% 
HR 58.9% 11.4% 
HU 52.7% 19.5% 
IE 17.9% 27.9% 
IS 77.2% 9.3% 
IT 45.5% 22.9% 
LV 49.3% 18.9% 
LI 2.5% 32.6% 
LT 59.3% 23.7% 
LU 40.2% 49.8% 
MT 16.6% 25.7% 
NL 30.3% 38.9% 
NO 11.8% 54.3% 
PL 37.2% 22.0% 
PT 37.8% 37.6%

60/131 
 
RO 46.9% 29.6% 
SK 41.6% 38.1% 
SI 31.9% 27.0% 
ES 43.3% 33.2% 
SE 10.9% 29.0% 
UK 17.2% 31.3% 
 
205. The weights and durations of the representative portfolios are set out in the 
Excel files of the monthly publication of the risk -free interest rate term 
structures on EIOPA’s website. 
206. For Iceland, there is not enough reliable information to calculate long-term 
average spreads. Therefore, Croatia ha s been assigned as a peer country 
for the VA calculation. Croatian spreads and risk corrections on the one 
hand and Icelandic króna weights on the other hand are used to derive a 
VA. 
207. The last subsection of  section 9 describes the approach for non -EEA 
currencies during the preparatory phase and the beginning of Solvency II in 
2016. 
9.E. Reference portfolios of ‘yield market indices’ 
208. For the calculation of the VA the representative portfolio of bonds needs to 
be mapped to a given granularity of ‘ yield market indic es’.The expression 
‘yield market indices’ covers in this section both yield curves and indices on 
yields. 
209. In order to be compliant with Articles 77b, 77c  and 77 d of the Solvency II 
Directive, the definition of the reference portfolios of ‘ yield market ind ices’ 
needs to be granular enough to reflect the duration, credit quality and asset 
class of the ‘yield market indices’. This is critical to ascertain an appropriate 
calibration of the volatility adjustment and the matching adjustment 
because the spread, the risk correction and the fundamental spread depend 
to a great extent on those features. Furthermore, such dependence is not 
linear and therefore the use of simple averages or baskets materially 
deviates from the relevant calculation 
210. EIOPA uses a referenc e portfolio for each relevant currency and country to 
calculate the volatility and matching adjustment according to the following 
information: 
a. Data from the relevant government bonds  yield market 
indices. Those data are required to determine the interest r ates of 
government bonds including in the representative portfolio, by 
duration and country of issuance. Those interest rates are then used

61/131 
 
to compute the spread S and the risk correction RC for those 
government bonds. For representative portfolios that co uld not be 
updated in 2016 government bond yields are also used to determine 
the interest rates of separately modelled non -central government 
bonds.  
b. Data from the relevant corporate bonds yield market indices. 
Those data are required to determine the interest rates of corporate 
bonds including in the representative portfolio, by duration, asset 
class and credit quality step. Those interest rates are then used to 
compute the spread S and the risk correction RC for corporate 
bonds.   
c. Currently EIOPA does not  use market data to derive the spread S 
and the risk correction RC for loans and securitisations included 
in the representative portfolios . The assumption underlying this 
choice is that the spread S and the risk correction RC for loans and 
for securiti zations are sufficiently similar to those for corporate 
bonds with the same credit quality and duration. EIOPA will test this 
assumption and may remove it in the future to the extent that there 
are appropriate indices for loans and for securitisations, which a re 
readily available to the public and for which there are published 
criteria for when and how the constituents of those indices will be 
changed, in accordance with Article 49 of the Delegated Regulation.   
211. The currency and country reference portfolios are  built on the basis of the 
representative portfolios of the same currency or country. For this purpose, 
a mapping is made to associate the characteristics of the assets including in 
the representative portfolios with indices. 
 
 
For government bonds. Currency portfolio 
212. The reference portfolio of ‘yield market indices’ used to calculate the VA for 
a given currency has as many model bonds as government bonds in that 
currency (and which insurance and reinsurance undertakings are invested 
in). 
213. The calculations for each issuer are based on its specific yield curve (‘ yield 
market index ’) according to the average duration , at the currency area  
level, of those  issuances where undertakings are invested in . Linear 
interpolation is used to derive the interannual rates c orresponding to the 
average duration.

62/131 
 
214. For the sake of simplicity, exposures are expressed in percentages and 
rounded to the nearest percentage.12 
215. In the case of the euro area, all the issuers of the euro area are mapped 
with a single ‘yield market index’: the relevant maturity of the ECB curve for 
all government bonds of the euro area (daily observations of annual spot 
rates). EIOPA provides the necessary information to allow the 
reconstruction of the LTAS of this curve. 
For governments banks bonds. Portfoli o for the country specific increase of 
the volatility adjustment 
216. For each ‘country reference portfolio’, EIOPA selects as many ‘ yield market 
indices” as issuers of government bonds in which undertakings of that 
country are invested in. The market yield for each issuer is derived from the 
government bond yield curves listed in subsection 3.C, according to the 
relevant duration.  Linear interpolation is used to derive the interannual 
rates corresponding to that duration. 
217. In case of issuances in a currency different than the currency of the issuer, 
the use of the  yield curve in the currency of the issuer is considered to be 
an acceptable proxy. 
218. Using yield curve s allows EIOPA to collect interest rates of government 
bonds for several maturities.  Furthermore, the yield curves should be 
consistent with those used for the calculation of the basic risk -free interest 
rates term structures in the case of currencies without DLT swaps. 
219. For the sake of simplicity, exposures are expressed in percentages and 
rounded to the nearest percentage as for the currency portfolio. 
220. In case there is no government yield curve for a country of the euro area, 
EIOPA applies the following criteria: 
 the national increase of the VA will be zero, 
 the long term average spread of the government b onds will be 
approximated with the long term average spread of a peer country , 
considering those countries with  similar credit quality and  level of 
interest rates for the  financial instruments used for the respective 
basic risk-free curves. 
 
 
                                       
12 In case the total exposure after rounding is not 100%, the rounding differences (positive or 
negative) are allocated to the largest exposure.

63/131 
 
Table 11. Peer countries as issuers for the calculation of the 
long term average spreads of government bonds 
Country without 
govts. yield curve 
Peer country 
Cyprus Portugal 
Estonia Belgium 
Latvia Ireland* 
Liechtenstein Switzerland 
Lithuania Spain 
Luxemburg Netherlands** 
Malta Ireland 
* For reference dates until 30 January 2017 the peer country for Latvia was Spain. 
** For reference dates until 31 May 2017 the peer country for Luxembourg was France. 
 
221. EIOPA will continuously monitor the allocation to peer countries. In case the 
credit quality or level of interest rate of an allocated country or of a peer 
country significantly changes, the allocation may be changed. Changes may 
be implemented at short notice in order to ensure the functionality of the 
volatility adjustment, in particular where the perceived credit quality of an 
allocated country deteriorates. 
For corporate bonds. 
222. Regarding corporate bonds , further than the duration,  the following 
dimensions are considered: 
 Assets classes, with a differentiation am ong ‘financial’ and ‘non -
financial exposures’,  
 Credit quality steps  as set out in the Delegated Regulation (from 0 to 
6), 
 Currencies, with a differentiation where possible for the euro, GBP and 
USD. 
223. Section 12 lists the market yield indices used for the i mplementation of this 
granularity.

64/131 
 
224. Exposures are expressed in percentages and rounded to the nearest 
percentage13. Therefore the theoretical 42 model corporate bonds resulting 
from the granularity mentioned above, i n practice and for most of markets, 
is limited to just a few market yield indices. 
225. The following table reflects the allocation of the ratings used by the market 
providers to credit quality steps for the only purposes of this technical 
documentation. EIOPA states explicitly that this allocation doe s not pre -
empt the work in progress regarding the ratings of ECAIs  in relation with 
the Delegated Regulation 
Table 12. Allocation of ratings to credit quality steps  
(only for the purpose of the technical information set out in 
Article 77e of the Solvency II Directive) 
iBoxx or S&P 
rating 
CQS iBoxx  or S&P 
rating 
CQS 
AAA 0 BB 4 
AA 1 B 5 
A 2 CCC 6 
BBB 3 CC, C,… 6 
 
226. For representative portfolios that were not updated in 2016 t he portfolio of 
‘assets other than government bonds ’ includes separately modelle d non-
central government bonds. These bonds  are not split by economic sectors 
and credit quality steps. Instead, t hey are treated in the same way as 
central government bonds.  
227. For the time being and due to the lack of data, no specific model bonds 
have bee n developed specifically for securitizations and loans. Once the 
relevant information is available, it will be necessary to assess the impact 
on the number of model points of a specific consideration of securitizations 
and loans (including mortgage loans). 
9.F. Volatility Adjustment for non-EEA currencies 
228. Due to the incompleteness of the available information, EIOPA has carried 
out an ad hoc survey based on market data at group level regarding 
                                       
13 In case the total exposure after rounding is not 100%, the rounding differences (positive or 
negative) are allocated to the largest exposure.

65/131 
 
exposures denominated in five non -EEA currencies: Australian dollar, 
Canadian dollar, Swiss franc, Japanese yen and US dollar. The selection of 
these currencies was based on the information available. 
229. EIOPA highlights the possibility of variations in the outputs, once a better 
set of information become s available. The weigh ts that EIOPA will apply 
during the preparatory phase and the beginning of Solvency II in 2016 are 
the following ones: 
Table 13. Non-EEA currencies and countries. Weights referred 
to in Article 50 of the Delegated Regulation 
 Govts. Others 
Australian 
dollar, 
Australia 
76.5% 18.2% 
Canadian 
dollar, Canada 51.9% 41.1% 
Switzerland 23.8% 51.4% 
Yen, Japan 85.2% 11.4% 
US dollar, USA 18.2% 76.1% 
 
230. EIOPA will assess the relevance of publishing the volatility adjustment  for 
other non-EEA currencies on a case by case and considering, among other 
factors, the materiality of the currency both at  the individual and market 
level. So far, no other need has been identified.

66/131 
 
10. Methodology for the determination of the risk corrections and 
the fundamental spreads 
10.A. Introduction 
231. In this section the expression ‘ risk correction ’ refers to the volatility 
adjustment. The expression ‘ fundamental spread ’ refers to the matching 
adjustment.  
232. Article 51 of Delegated Regulation specifies that the risk correction “shall be 
calculated in the same manner  as the fundamental spread”  and using the 
same inputs. Therefore, the methods and source data described in this 
section are relevant for both the risk correction used for the volatility 
adjustment and the fundamental spread  applied for the  matching 
adjustment.  
233. In the absence of specific reference  to the contrary , the content of this 
section refers to both the risk correction spread and the fundamental 
spread. 
10.B. Determination of the risk -corrections and the 
fundamental spreads for government bonds 
234. According to Article 77c of the Solvency II Directive, the fundamental 
spread on government bonds is equal to the maximum between: 
a. The sum of the credit spread corresponding to the probability of 
default of the assets considered and the credit spread corresponding 
to the expected loss resulting from down grading of the assets 
concerned. 
b. A percentage of the long-term average of the spread, over the basic 
risk-free interest rate, of assets of the same duration, credit quality 
and asset class, as observed in financial markets. This percentage is 
30% for exposures to governments of EEA member states, and 35% 
for exposures to other governments (Article 77c(2)(b) and (c) of the 
Solvency II Directive). 
235. Recital 22 of the Delegated Regulation  specifies that ‘ where no reliable 
credit spread can be derived from the default statistics, as in the case of 
exposures to sovereign debt, the fundamental spread for the calculation of 
the matching adjustment and the volatility adjustment should be equal to 
the long-term average of the spread over the risk-free interest rate set out 
in Article 77c(2)(b) and (c) of Directive 2009/138/EC’.  
236. Therefore, the risk correction of the spread Sgov and the fundamental spread 
on government bonds corresponds only to:

67/131 
 
RC = FS = 30% LTAS fo r exposures to governments of EEA 
member states 
RC = FS = 35% LTAS for exposures to other governments  
where LTAS is the long-term average of the spread over the risk -free 
interest rate of assets of the same duration, credit quality and asset class. 
10.B.1. Long-term average of the spread on government bonds 
237. Article 54(3) of the Delegated Regulation provides the following: 
a. The long-term average shall be based on data referring to the last 
30 years;  
b. Where a part of that data is not available, it shall be replaced b y 
constructed data; 
c. The constructed data shall be based on the available and reliable 
data referring to the last 30 years. Data that are not reliable shall be 
replaced by constructed data using that methodology; 
d. The constructed data shall be based on prudent assumptions.  
238. In order to determine the long-term average for each relevant currency and 
country, EIOPA needs the following inputs: 
a. The zero -coupon yield curve of the government bonds in the 
government bonds representative portfolio, over the last 30 years; 
b. The basic risk -free interest rate term structure denominated in the 
currency of the bonds in the government bonds representative 
portfolio, over the last 30 years. 
239. However, in most cases there is no historical data over a 30 years period on 
interest rate swaps and government bonds.  
240. To overcome this issue, EIOPA re -constructs missing data, in accordance 
with Article 54(3) of the Delegated Regulation, applying the following rule:  
the missing spread data for each currency and maturity are re -constructed 
using the average spread calculated with the data available from 1  January 
1985 or, failing that, whenever reliable spread data are available.  
241. Nevertheless, since the overnight market have developed only since the end 
of the last century, the availability  of overnight swap rates (necessary to 
calculate the credit risk adjustment) has been limited, resulting de facto in a 
calculation of the LTAS since 1 January 1999 for all currencies.  
242. Therefore, EIOPA assumes the average spread over the period for which 
data are missing is not materially different from the average spread that 
can be calculated with available data. 
243. To illustrate the implementation of this rule, let’s take the following 
example. Suppose that the volatility adjustment is calculated at year en d

68/131 
 
2015. Suppose further that, for a given currency and maturity, data are 
only available from 01 January 1999 till 31 December 2015 (i.e. 17 years). 
The assumption is that the constructed data have the same average as the 
average obtained from the available market data: 
a. From 1986 to 1998: the constructed spread for each year 
corresponds to the flat average spread calculated on the period 
1999-2015.  
b. From 1999 to 2015: the available spread data are used.  
244. EIOPA will determine the constructed spread for each currency and maturity 
where data are missing on the basis of the data available at 31 December 
2015. All the calculations are developed using daily data. 
245. The LTAS for UK government bonds is a  special case because reliable data, 
to assess the spread of these bonds, in particular pound sterling swap data, 
are available for the period before 1999. These additional data are taken 
account by applying the adjustment factors set out in Annex 14.H to the 
LTAS that are calculated as described in the two paragraphs above. 
246. From 1 January 2016 until having the complete 30 -years historical series 
from January 1999, at each publication the LTAS will be calculated as: 
𝐿𝑇𝐴𝑆31_12_2015 ∗(7800−𝑛𝑡𝑑)+∑ 𝑆𝑝𝑟𝑒𝑎𝑑𝑠_𝑓𝑟𝑜𝑚_1_1_2016𝑛𝑡𝑑
7800  
where ntd denotes the number of new trading days from 1  January 
2016 onwards where data are available ; ∑ 𝑆𝑝𝑟𝑒𝑎𝑑𝑠_𝑓𝑟𝑜𝑚_1_1_2016𝑛𝑡𝑑   
means the sum of the spreads during those new dates; LTAS31_12_2015 
identifies the LTAS as of 31  December 2015; and it is assu med that a 
30 years period is composed of 7800 trading days. 
247. For the sake of transparency EIOPA will publish the long-term average 
spreads. 
248. The calculations according to the methodology above show that for most of 
currencies, the market s of government bond s with more  than 10 years 
duration have developed only from the first half of the last decade. As a 
consequence, the calculation of the LTAS for maturities higher than 10 
years lacks of representativeness due to the reduced number of 
observations and to th e fact that a major part of the observations refer to 
the current financial crisis. 
249. In order to avoid this bias, the calculation of LTAS for government bonds is 
carried out from 1 to 10 year maturities. The LTAS resulting for maturity 10 
years is applied f or longer maturities. Even below 10 years, for a few 
currencies some maturities deliver non plausible results. The following table 
reflects the currencies with some maturity delivering non plausible LTAS. To 
derive the spreads for those maturities, linear interpolation of spreads using 
neighbor maturities is applied  (see also sub section 10.C.3 where the same 
linear interpolation is used).

69/131 
 
 
Table 14. Disregarded maturities for the LTAS on government bonds 
calculation 
(0 = disregarded and then interpolated; 1 = LTAS historical data)  
 
Country ISO 4217 1 2 3 4 5 6 7 8 9 10 
Austria AT 1 1 1 0 1 1 1 1 1 1 
Croatia HRK 1 0 1 1 0 0 0 1 1 0 
Cyprus CY 1 1 1 1 1 0 1 1 1 1 
Czech Republic CZK 1 1 1 1 1 1 1 1 0 1 
Denmark DKK 1 1 1 1 1 1 1 1 0 1 
Greece GR 1 1 0 1 1 0 1 1 1 1 
Hungary HUF 1 1 1 1 1 1 1 1 1 1 
Norway NOK 1 1 1 1 1 1 1 1 1 0 
Romania RON 1 1 1 1 1 0 1 1 1 1 
Russia RUB 1 1 1 1 1 1 1 1 1 0 
Slovakia SK 1 1 1 0 1 1 1 1 1 1 
Slovenia SI 1 1 0 1 1 1 1 1 1 1 
Sweden SEK 1 1 1 1 1 1 1 1 0 1 
Switzerland CHF 0 1 1 1 1 1 1 1 0 1 
Chile CLP 1 1 1 1 1 1 1 0 1 1 
Malaysia MYR 1 1 1 1 1 1 1 1 1 0 
Korea, South KRW 1 1 1 1 1 0 1 0 0 0 
Thailand THB 1 1 1 1 1 0 1 1 1 1 
The table sets out the maturities used to derive the government bond spreads for current 
reference dates that enter the calculation of the LTAS. Past changes to the maturities are 
set out in the Annex to subsection 10.B.1.  
 
10.C. Determination of the risk -corrections and fundamental 
spreads for assets other than government bonds 
10.C.1. General elements 
250. The Solvency II Directive and Articles 49 to 54 of the Delegated Regulation 
set down several aspects of the methodology for calculating the Risk 
Correction and the Fundamental Spread of assets other than government 
bonds. The methodology to be used is different depend ing on whether 
reliable credit spreads can be determined from long-term default statistics.  
251. Where reliable credit spreads can be derived from such statistics, the risk 
correction spread and the fundamental spread can be expressed as: 
RC = FS = MAX ( PD + CoD, 35% LTAS ) where 
PD = the credit spread corresponding to the probability of default 
on the assets;

70/131 
 
CoD = the credit spread corresponding to the expected loss 
resulting from downgrading of the assets; 
LTAS = the long-term average of the spread over the  risk-free 
interest rate of assets of the same duration, credit quality and 
asset class. 
252. Where no reliable credit spreads can be derived from long -term default 
statistics, the risk correction and f undamental spread can be expressed as 
RC = FS = 35% LTAS, w here LTAS is the long-term average of the spread 
over the risk-free interest rate of assets of the same duration, credit quality 
and asset class. 
253. The Delegated Regulation sets the recovery rate assumption in the event of 
a default at 30% for all asset classes. 
254. The Delegated Regulation also specifies that the LTAS should be based on 
data of the last 30 years.  
255. Where there is not 30 years of complete and reliable information relating to 
spreads, the Delegated Regulation specifies that the ‘missing’ data shoul d 
be constructed using the data that is available, in a prudent manner. The 
process of reconstruction is consistent with the process described above for 
government bonds. 
256. Where the fundamental spread is defined by the 35% LTAS, the difference 
among the fundamental spread and the PD will be attributed to the CoD. 
 
10.C.2. Method for deriving the probability of default (PD) and 
the cost of downgrade (CoD) 
257. The calculation of the PD derives an amount that is interpreted as an 
investor’s required compensation for assumi ng the risk of the expected 
probability of default of a bond. The expectation of a default (based on 
historical default probabilities derived from the transition matrices) is thus 
combined with an assumption on the recovery value in case of default, 
which is assumed to be 30% of the market value as set out in Article 54(2) 
of the Delegated Regulation. 
258. For the sake of consistency, EIOPA applies the same method to calculate 
both the PD and CoD, with the following difference: 
- For the PD, EIOPA assumes a “buy a nd hold” strategy: assets are not 
sold after downgrade. 
- For the CoD, EIOPA assumes a “buy and replace” strategy: assets 
downgraded are replaced by an asset of the same credit quality step as 
before downgrade, or higher. This difference in calculation of PD  and 
CoD may give rise to the double -counting of risks. To avoid that,  the

71/131 
 
CoD calculation is reduced by the following difference: the PD calculated 
with the “buy and hold” strategy minus the PD calculated with the “buy 
and replace” strategy. EIOPA ensures the final outcome stays greater or 
equal to zero. 
259. Both computations use the transition matrix adjusted for cost accounting  
and are based on the same inputs: empirical one-year transition matrices, 
the relevant basic risk-free interest rates term structure and for each credit 
quality step a vector of relevant portions of the market value of a risk-free 
benchmark instrument. These portions have been designed to be analogous 
to the recovery rate for the PD. 
Table 15. Vector of scaling factors used in 
the calculation of the Cost of Downgrade  
CQS Rc CQS Rc 
AAA 98% BB 70% 
AA 97% B 50% 
A 95% CCC 40% 
BBB 85%   
 
260. In case of a rating migration  to a credit quality step  of lower quality 
(downgrades), the cost is defined as difference between the two market 
values. This cost reflects the cost of replacing the downgraded asset with an 
asset of the same credit quality it was downgraded from and preserving the 
original cash flow pattern. Knowing that the asset did not default, the cost is 
reduced so that it takes account of that information. 
261. For the next year of projection the asset is supposed to start from the credit 
quality step of the replaced bond . This cost accounting and rebalancing 
procedure is applied  until maturity of the original bond . This procedure 
implements the rebalancing requirement as set out in Article 54(4) of the 
Delegated Regulation. 
262. The total loss is defined as the loss in market value by subtracting the 
present value of future downgrading cost cash flows. Finally, the loss in 
market value is trans formed into an implied (higher) yield  and the result is 
expressed as spread over the basic risk free interest rate in basis points. 
263. The annex to this subsection contains a detailed description of this method.  
Subsection 12.B.2. details the transit ion matrices used for the calculations 
described in this subsection. 
264. For the calculation of the volatility adjustment, the value of the PD and CoD 
expressed in basis points are rounded to the nearest basis point. This 
rounded value is used as input in the relevant step of the calculation of the 
volatility adjustment.

72/131 
 
265. For the matching adjustment, the PD that EIOPA publishes is the probability 
to apply for the de-risking of cash flows as follows: 
de-risked⁡cash⁡flow=cashflow∗(1−𝑃𝐷𝐸𝐼𝑂𝑃𝐴)+recovery_rate∗cashflow∗𝑃𝐷𝐸𝐼𝑂𝑃𝐴 
266. The PD probability for de-risking cash flows expected at time ‘t’ is derived 
from a Markov matrix as the last column obtained when powering ‘t’ times 
the one year average transition matrices (see the annex for further details). 
267. The probability of default, cost of downgrade and fundamental spread are 
published until 30 years maturity. From that maturity onwards the value of 
those magnitudes for the 30 years maturity will apply. 
268. The calculation o f PD and CoD is set out in the E xcel tool “CoD & PD 
Calculation” that can be found on EIOPA’s website. 
 
10.C.3. Long-term average of the spread on other assets 
269. The long-term average of the spread on other assets is calculated in the 
same manner as the long-term average spread on government bonds 
described in the subsection 10.B.1 above, with the following specificities.  
270. A linear interpolation is performed to obtain complete corporate yield curves 
where there is missing data 14. Where there are no market data or only 
market data for a single maturity, then the yields are set to zero.  All yields 
below the first maturity available are equal to the first yield available. 
271. As explained in sub -section 12.B.1, the CQS 0 corporate yields are equal 
to 85% of the CQS 1 corporat e yields where those yields are positive or zero  
and otherwise equal to 115%  of those yields. This operation is performed for 
financial and non-financial bonds and for all currencies. 
272. The long-term average spread is calculated for those dates where neither  
the basic risk-free rate term structures nor the corporate yields of the same 
currency15 are nil. The calculation is performed in the same manner than 
the long-term average spread on government bonds, i.e. assuming tha t the 
average spread over the period f or which data is missing is not materially 
different from the average spread that can be calculated with available 
data. 
273. Having in mind the content of the market input data as described in section 
12, the value of the 2 year LTAS is used also as value of the 1 year LTAS. 
                                       
14 This linear interpolation is performed for each 10th of a year. See also subsection 12.B.1. 
15 Currencies for which a LTAS on other assets is calculated are EUR, GBP and USD.

73/131 
 
274. LTAS on other assets is kept constant from the last maturity available of the 
market source onwards. 
275. For GBP non-financial bonds, credit quality step 1, the LTAS for maturities 4 
to 9 years calculated before 1 st January 2016  is obtained by linear 
interpolation of LTAS using 3 and 10 years maturities, because the history 
of the indices available in the range of 4 to 9 years does not allow a reliable 
calculation of th ose LTAS. From 1 st January onwards, the new data to be 
used in the LTAS calcu lation is of better quality and one does not need to 
interpolate anymore. 
276. As for UK government bonds, there are adjustment factors for the LTAS of 
corporate bonds denoted in pound sterling in order to take account of 
reliable data for the period before 199 9. The adjustment factors are set out 
in Annex 14.H. 
277. The LTAS of GBP and US D CQS 4 and 5 corporate bonds are calculated 
using the approach described in sub -section 10.C.4. For LTAS, that means 
that, first the spread of the GBP/USD basic risk -free term stru ctures over 
the EUR basic risk -free term structure is calculated; second the average of 
the above calculation is performed for all relevant dates; third =0.5 is 
multiplied to this long -term average; fourth the result is added to the 
corresponding LTAS of the EUR. 
278. The LTAS of CQS 6 corporate bonds is equal to the LTAS of CQS 5 corporate 
bonds. 
 
10.C.4. Currencies without yield market indices for corporates, 
loans and securitizations. 
279. For currencies for which there are no yield market ind ices satisfying the 
calculation needs, the spread on corporate bonds denominated in euro is 
used with an adjustment proportionate to the difference between the basic 
risk-free interest rate term structure of the concerned currency and the 
euro. In such case, the following formulas applies:  
 
 €€
€€
)1( rfr
X
rfrcorp
X
corp
rfr
X
rfrcorp
X
corp
YYYY
YYSS




 
where € denotes the euro, X refers to a currency without interest rates term 
structures for the assets relevant for the spread Scorp, Ycorp denotes the yield 
of the respective corporate bonds of the same credit quality, Yrfr denotes the 
basic risk  free interest rate and =0.5. The inputs of this formula are 
maturity dependent according to the information available.

74/131 
 
280. EIOPA may also consider the specific case of covered bonds, once the 
current limitations in the information available are solved.  
281. For the time being an operational solution has been identified for the Danish 
market of covered bonds based on the following formula:  
DKK
rfr
DKK
covered
DKK
covered YRS 
 
where DKK denotes Danish krone and: 
DKK
coveredR
 shall be based on the yield from Nykredits Realkreditindeks. 
(Bloomberg ticker NYKDYTM) 
The maturity used for 
DKK
rfrY shall correspond to the duration of the 
Nykredits Realkreditindeks (7 years). 
282. The resulting 
DKK
coveredS  is relevant for AAA Financials in the calculation for DKK. 
283. Nykredits Realkreditindeks includes a representative extract of the Danish 
covered bond market. The index includes both covered bonds with short 
and long maturities. See also the accompanying annex to this section. 
 
10.C.5. Inputs used to determine Sgov and Scorp 
284. For determining the spread Sgov on government bonds, the starting point is 
the information of insurance market data relevant for the currency (or 
country) whose VA is calculated. This information is composed of two 
elements: 
a. The composition of the reference portfolio of yield market indices of 
government bonds for the currency (or country). This composition is 
applied considering for each component of the portfolio (i.e. each 
issuer) its relative market value (the percentage of the total market 
value of the portfolio).  
b. It is also necessary to know the duration of each component of the 
reference portfolio. 
Each relative market value  and its corresponding duration build a model 
bond (i.e. a model bond is a government bond with the duration for such 
bond in the currency or country where the VA is calculated). 
Since in the case of government bonds the selected yield market indices 
are yield curves, this means that each model bond is the value of the yield 
curve for each issuer at the relevant maturity. 
285. The following financial market inputs are also necessary:

75/131 
 
a. The market yield s corresponding to  the currency and duration of 
each model point representing the government bonds as referred 
above and in section 9, 
b. The basic risk -free interest rates corresponding tothe currency and 
durations of each model point representing the government bonds 
as referred above and in section 9, 
c. The risk corrections corresponding to the currency and durations of 
each model point representing the government bon ds as referred 
above and in section 9. 
286. Where the average duration of the relevant government bond in which the 
insurance and reinsurance undertakings of a given market are invested in 
does not coincide with one of the maturities of the yield curve, EIOPA uses a 
linear interpolation to find the interest rate of the government bond and/or 
the basic risk -free rate and/or the risk correction that corresponds to the 
average duration. 
287. For determining the spread Scorp on assets other than government bonds, 
the same approach applies mutatis mutandis.

76/131 
 
Table 16. Specification of the input for the calculation of the VA 
Corporate part of the VA 
 Yield Risk-free interest rate Risk correction 
Currency VA Corporate bonds Corporate bonds in the currency for 
which a VA is calculated (if needed 
with K factor approach) 
Currency for which a VA is 
calculated 
Corporate bond FS in the currency 
for which a VA is calculated (if 
needed with K factor approach) 
RGLA bonds Euro VA: ECB curve for all euro area 
issuers, government bond of the 
issuer for all non-euro area issuers 
VAs for other currencies: Government 
bond of the issuer 
Currency of the issuer Euro VA: ECB curve FS for all euro 
are issuers, government bond FS 
of the issuer for all non-euro area 
issuers  
VAs for other currencies: 
Government bond FS of the issuer 
Country VA Corporate bonds Corporate bonds in the currency of 
the country for which a VA is 
calculated (if needed with K factor 
approach) 
Currency of the country for 
which a VA is calculated 
Corporate bond FS in the currency 
of the country for which a VA is 
calculated (if needed with K factor 
approach) 
RGLA bonds  
(only relevant for 
portfolios not updated 
in 2016) 
Government bond of the country of 
the issuer 
Currency of the issuer Government bond FS of the issuer 
Government part of the VA 
 Yield Risk-free interest rate Risk correction 
Currency VA Govt bonds Euro VA: ECB curve for all euro area 
issuers, government bond of the 
issuer for all non-euro area issuers 
VAs for other currencies: Government 
bond of the issuer 
Currency of the issuer Euro VA: ECB curve FS for all euro 
are issuers, government bond FS 
of the issuer for all non-euro area 
issuers  
VAs for other currencies: 
Government bond FS of the issuer 
Country VA Govt bonds Government bond of the issuer Currency of the issuer Government bond FS of the issuer

77/131 
 
11. Process of calculation of the risk -corrected spread at 
portfolio level 
288. Process of calculation of the currency volatility adjustment  (the process 
applies mutatis mutandis to the calculation of the country  specific increase 
of the volatility adjustment). 
Step 1.- For each currency, i dentify the model bonds (and their duration) 
included in the representative portfolio. 
Step 2. - For each model bond, input the market yield at the date of 
calculation, according to the table in section 1 2 and the duration of the 
model bond16. This yield is referred to in the process as ‘ yield before risk 
correction‘. 
Step 3.-   For each model bond, input the basic  risk-free interest rate s 
curve at the date of calculation, accordin g to the duration of the model 
bond.17 
Step 4. - For each model bond, calculat e the risk correction as the 
maximum of the relevant percentage of the long-term average spread (30 
or 35% as described in subsection 10.B), and the PD+CoD (probability of 
default and cost of downgrade, as referred to in subsection 10.C and its 
annex). In the case of government bonds , the risk correction is the 
relevant percentage of the long-term average spread (i.e. the PD+CoD 
component does not apply).  Where the LTAS is negative,  a zero floor is 
applied as mentioned in section 8.  
Step 5. - Once completed the previous steps, a single cash flow is 
projected for each model bond according to the duration of the model 
bond, and using as capitalization rate the market ‘yield before risk  
correction‘ referred to in step 2. This means a cash flows projection with 
the features of each model bond. 
Step 6.- The projection of single cash flows for each model bond made in 
step 5 is repeated but using as capitalization rate the basic risk -free rate 
referred to in step 3. 
Step 7. - A third projection is necessary but using this time , as 
capitalization rate, the ‘yield before risk correction ‘ reduced with the risk 
correction derived in step 4. 
                                       
16 Where the market yield is given for a maturity that does not fit exactly the weighted average 
duration of the model bond, a linear interpolation of yields of the same index or the same curve is 
performed.   
17 The same linear interpolation as in step 2 applies if necessary.

78/131 
 
Steps 8, 9 and 10. - Calculation of the three following in ternal effective 
rates (IER18) for the overall reference portfolio: 
a. Step 8.- “IER_yield_before” is e qual to the internal effective rate, 
calculated as a single discount rate that, where applied to the cash-
flows calculated in step 5, results in a value that  is equal to the 
aggregated value of the whole portfolio (since relative percentages 
are used, this aggregated value is 1); 
b. Step 9. - “IER_basic_RFR” is equal to the internal effective rate, 
calculated as a single discount rate that, where applied to the cash-
flows calculated in step 6, results in a value that is equal to the 
aggregated value of the whole portfolio (since relative percentages 
are used, this aggregated value is 1); 
c. Step 10. - “IER_yield_corrected” is equal to the internal effective 
rate, calculated as a single discount rate that, where applied to the 
cash-flows calculated in step 7, results in a value that is equal to the 
aggregated value of the whole portfolio (since relative percentages 
are used, this aggregated value is 1). 
289. Finally, for each  relevant currency, the spreads 𝑆𝑔𝑜𝑣 (the same applies for  
𝑆𝑐𝑜𝑟𝑝) before the risk correction  is equal to the following , in accordance to 
Article 50 of the Delegated Regulation: 
𝑆𝑔𝑜𝑣=𝑚𝑎𝑥(⁡0⁡;⁡𝐼𝐸𝑅𝑦𝑖𝑒𝑙𝑑⁡𝑏𝑒𝑓𝑜𝑟𝑒⁡𝑅𝐶−𝐼𝐸𝑅𝐵𝑅𝐹𝑅) 
while the risk c orrection 𝑅𝐶𝑔𝑜𝑣⁡(the same applies to ⁡𝑅𝐶𝑐𝑜𝑟𝑝) is equal to the 
following19: 
𝑅𝐶𝑔𝑜𝑣=⁡𝑚𝑎𝑥⁡(⁡0⁡;⁡𝐼𝐸𝑅𝑦𝑖𝑒𝑙𝑑⁡𝑏𝑒𝑓𝑜𝑟𝑒⁡𝑅𝐶−𝐼𝐸𝑅𝑦𝑖𝑒𝑙𝑑⁡𝑅𝐶⁡) 
Finally, for each relevant currency and country the VA is calculated usin g 
these four values (𝑆𝑔𝑜𝑣, 𝑆𝑐𝑜𝑟𝑝, 𝑅𝐶𝑔𝑜𝑣, 𝑅𝐶𝑐𝑜𝑟𝑝) as inputs to the formula referred 
to in subsection 8.A 
290. The volatility adjustment is rounded at the nearest integer basis point. This 
rounding is applied only at the end of the calculation process. 
 
 
 
                                       
18 The IER is calculated by EIOPA using a pre-defined Matlab function: “xirr” with the following 
parameters: “GUESS” = 0.05 and “MAXITER” = 200. 
19  The risk correction at portfolio level cannot be negative because, as mentioned in section 7, the 
risk correction for each individual model bond cannot be negative.

79/131 
 
Illustrative example (dummy data) 
Wgov 62,00% 
  Wcorp 25,10% 
  Sgov 0,85% = IER 1(step 8) - IER 2 (step 9) 
Scorp 1,20% = IER 1(step 8) - IER 2 (step 9) 
RC gov 0,20% = IER 1(step 8) - IER 3 (step 10) 
RC corp 0,35% = IER 1(step 8) - IER 3 (step 10) 
S 0,83% 
  RC 0,21% 
  S RC crncy 0,62% 
  Currency VA 0,40% 
   
Detailed examples of the VA calculation can be found in the two Excel files “VA 
calculation example IT” and “VA calculation example UK”.

80/131 
 
12. Financial market data applied for VA and MA calculation 
12.A. Market data for government bonds 
291. The calculation of the LTAS is based on the basic risk -free interest rates 
term structures and the government yield curves described in section 3. 
12.B. Financial market data for assets other than gove rnment 
bonds 
12.B.1. Market yields for corporate bonds 
292. The market yields for corporate bonds are those provided by the Markit – 
iBoxx indices listed in the tables below in this subsection.  The yield is the 
‘Annual Yield’ and the duration is the ‘ Portfolio Duration’ (rounded to the 
first decimal). For high-yield indices the ‘Annual Yield to Maturity’  and the 
‘Portfolio Duration to Maturity’ (rounded to the first decimal) are used.20 
293. The relevant yield curve is calculated by linear interpolation for those 
maturities p rovided by the source. For shorter and longer maturities the 
interest rate published for the nearest duration is applied.  An example for 
the interpolation is as follows: in order to  calculate the yield for a bond of 
duration 8.8, a linear interpolation is performed using the closest data 
available. For instance  this could be , on the one hand the market yield of 
the bucket 7 -10 and its duration (e.g. 8.3 years) and, on the other hand, 
the market yield of the bucket 10-15 and its duration (e.g. 12.1 years). 
294. Having in mind the availability of both the current value of market yield 
indices for exposures to corporate bonds, and of their historical series 
(necessary to calculate the long-term average spreads), the following 
decisions have been adopted for pragmatic reasons: 
a. CQS0 (AAA) corporate yield indices for the euro and GBP have not 
been available during the last two years for a major part of the 
maturity buckets, and even for those maturity buckets where yields 
are available, the number of constituents of the  index is very low. 
Furthermore, availability of buckets ha s continuously changed 
during the last years (i.e. not always the same buckets of duration 
have been available).  
In order to solve the current lack of data and avoid the exposure of 
the calculation to likely business contingencies, the market yields of 
                                       
20 The names of the yield and duration concepts relate to the fieldnames of the data files  from the Markit FTP 
server.

81/131 
 
CQS0 exposures will be 85% of CQS1 yields for the euro and for the 
GBP. The 0.85 reduction factor is based on the historical experience 
of those periods where both CQS0 and CQS1 yields have been 
simultaneously available.  In case CQS1 yields are negative the 
market yields of CQS0 exposures will be 115% of CQS1 yields. 
b. Regarding CQS1 non -financial bonds expressed in GBP,  the 
available historical series of market yield indices for maturities from 
4 to 9 years are incomplete and a reliable calculation of the long -
term average spread (LTAS) is not possible before 1st January 2016. 
Therefore for GBP n on-financial bonds, credit quality step 1 , the 
LTAS for maturities 4 to 9  years is obtained by linear interpo lation 
of 3 and 10 years maturities LTAS. This interpolation is performed 
for all data before the 31 December 2015. It won’t be performed for 
the data afterwards as reliable data is available. This rule does not 
apply to the current market yields, because for the time being it is 
possible to use the indices GBP CQS1 Non-financial. 
c. The currently available indices  for CQS4 and CQS5 do not 
discriminate by duration. Therefore, the market yield of sub -
investment grade assets CQS4 and CQS5 is used for all maturit ies 
(i.e. a flat curve is used). 
d. The market yield indices available for CQS6 are based on a limited 
number of constituents and the historical information available is 
not complete enough. For these exposures the market yield indices 
of CQS5 are applied. 
295. EIOPA will monitor the effect of these criteria and the improvements of the 
available financial market data 
12.B.2. Market data for the calculation of the PD and CoD 
296. The inputs necessary for the calculation of the probability of default and 
cost of downgrade are the benchmark curve used to calculate the spreads, 
the corporate bonds spreads  to the benchmark curve , and the relevant 
transition matrices: 
a. The benchmark curve is the basic risk-free curve, 
b. The spread s are  calculated as the difference between the market 
yields for corporate bonds described above, and the basic risk-free 
interest rate term structure.  
c. Two transition matrices are used as inputs: financial and non-
financial exposures. Both transition matrices have been obtained 
according to the following criteria: 
i.) the transition probabilities refer to the 1 year average 
calculated along the last 30 years, until 1 January 2016;

82/131 
 
ii.) having in mind the limited number of exposures per 
geographical area, credit quality step and economic 
sector, the geographical area consi dered refers to all 
countries; 
iii.) the withdrawn  exposures are excluded (i.e. not 
considered in the initial population of names); 
iv.) the statistics refer to issuers (i.e. names); 
v.) having in mind the definition of the market source for 
ratings below CCC, those cate gories are included as 
defaults. Therefore matrices used as input have seven 
credit quality steps (i.e. eight rows and columns, 
including the situation of being defaulted, which is 
considered to be an absorbing state – no return to rated 
categories). 
The i nput data for the transition matrices are specified in 
annex 14.K. 
 
297. EIOPA will update the transition matrices on an annual basis at mid -
January. The updated matrices will be applied for the first time in the 
calculation of end-January technical information.

83/131 
 
 
Markit – iBoxx indices 1-3yr 3-5yr 5-7yr 7-10yr 10+yr 
EUR_Financial AAA 85% of the EUR financial AA yields if those yields are positive or zero, otherwise 115% of those yields 
EUR_Financial AA DE000A0JZBB2  DE000A0JZBD8  DE000A0JZBF3  DE000A0JZBH9  DE000A0JZA95  
EUR_Financial A DE000A0JZA12 DE000A0JZA38  DE000A0JZA53 DE000A0JZA79  DE000A0JZAZ3  
EUR_Financial BBB DE000A0JZBX6  DE000A0JZBZ1  DE000A0JZB11  DE000A0JZB37  DE000A0JZBV0  
EUR_Financial BB Iboxx EUR High Yield curve Financial ex crossover LC BB (GB00B1CQYN32) 
EUR_Financial B Iboxx EUR High Yield curve Financial ex crossover LC B (GB00B1CQYW23) 
EUR_Financial CCC Iboxx EUR High Yield curve Financial ex crossover LC B (GB00B1CQYW23 
EUR_Non Financial AAA 85% of the EUR Non financial AA yields yields if those yields are positive or zero, otherwise 115% of those yields 
EUR_Non Financial AA DE000A0JZCH7  DE000A0JZCK1  DE000A0JZCM7  DE000A0JZCP0  DE000A0JZCF1  
EUR_Non Financial A DE000A0JZB78  DE000A0JZB94  DE000A0JZCB0  DE000A0JZCD6  DE000A0JZB52  
EUR_Non Financial BBB DE000A0JZC36 DE000A0JZC51  DE000A0JZC77  DE000A0JZC93  DE000A0JZC10  
EUR_Non Financial BB Iboxx EUR High Yield curve Non-financial ex crossover LC BB (GB00B1CR1Z75) 
EUR_Non Financial B Iboxx EUR High Yield curve Non-financial ex crossover LC B (GB00B1CR2653) 
EUR_Non Financial CCC Iboxx EUR High Yield curve Non-financial ex crossover LC B (GB00B1CR2653)

84/131 
 
Markit – iBoxx indices 1-3yr 3-5yr 5-7yr 7-10yr 10-15yr 15+yr 
GBP_Financial AAA 85% of the GBP financial AA yields yields if those yields are positive or zero, otherwise 115% of those yields 
GBP_Financial AA DE000A0JY7T1  DE000A0JY7X3  DE000A0JY7Z8  DE000A0JY712  DE000A0JY7R5  DE000A0JY7V7  
GBP_Financial A DE000A0JY7B9  DE000A0JY7F0  DE000A0JY7H6  DE000A0JY7K0  DE000A0JY696  DE000A0JY7D5  
GBP_Financial BBB DE000A0JY8R3  DE000A0JY8V5  DE000A0JY8X1  DE000A0JY8Z6  DE000A0JY8P7  DE000A0JY8T9  
GBP_Non Financial AAA 85% of the GBP Non financial AA yields yields if those yields are positive or zero, otherwise 115% of those yields 
GBP_Non Financial AA DE000A0JY9P5  DE000A0JY9T7  DE000A0JY9V3  DE000A0JY9X9  DE000A0JY9M2  DE000A0JY9R1  
GBP_Non Financial A DE000A0JY878  DE000A0JY9B5  DE000A0JY9D1   DE000A0JY9F6   DE000A0JY852  DE000A0JY894  
GBP_Non Financial BBB DE000A0JZAM1 DE000A0JZAR0 DE000A0JZAT6 DE000A0JZAV2 DE000A0JZAK5 DE000A0JZAP4 
 
 
Markit – iBoxx indices 1-3yr 3-5yr 5-7yr 7-10yr 10-15yr 15+yr 
USD_Financial AAA 85% of the USD financial AA yields 
USD_Financial AA GB00B05DN483 GB00B05DN590 GB00B05DN608 GB00B05DN715 GB00B05DN822 GB00B05DNB55 
USD_Financial A GB00B05DMS57 GB00B05DMT64 GB00B05DMV86 GB00B05DMW93 GB00B05DMX01 GB00B05DN046 
USD_Financial BBB GB00B05DNS23 GB00B05DNT30  GB00B05DNV51  GB00B05DNW68  GB00B05DNX75 GB00B05DNZ99  
USD_Non Financial AAA 85% of the USD Non financial AA yields yields if those yields are positive or zero, otherwise 115% of those yields 
USD_Non Financial AA GB00B05DQD84  GB00B05DQF09  GB00B05DQG16  GB00B05DQH23  GB00B05DQJ47  GB00B05DQL68  
USD_Non Financial A GB00B05DQ270  GB00B05DQ387  GB00B05DQ494  GB00B05DQ502  GB00B05DQ619  GB00B05DQ833  
USD_Non Financial BBB GB00B05DR245  GB00B05DR351  GB00B05DR468  GB00B05DR575  GB00B05DR682  GB00B05DR807  
 
 
 
Yields for sub-investment grade bonds denominated in pound sterling and US dollar are derived from yields of corresponding 
bonds denominated in euro by applying the factor described in section 10.C.4.

85/131 
 
13. Calculation of the relevant risk -free interest rates term 
structures at a glance. 
298. The complete process of calculation may be summarized as follows: 
Basic risk-free interest rates term structure 
Step A.- Use the data specified in table 1 of section 3.C as input for the 
market interest rates of the relevant financial instrument. 
Step B.- According to the tables in section 4, remov al of  the rates  
either not meeting the DLT requirements (tables 3 to 5) or longer than 
the LLP (table 2). 
Step C.- Calculation of the credit risk adjustment as described in 
section 5. 
Step D.- Reduction of all the market rates remaining af ter step B by 
the amount of the credit risk adjustment (and the currency adjustment 
in the case of the Bulgarian and Danish currencies). 
Step E.- Construction of the matrix of cash flows corresponding to the 
credit risk adjusted rates after step C.  
One of the dimensions of this matrix reflects the maturities 
corresponding to DLT rates (e.g. 1 to 10, 12, 15 and 20 years in 
the case of the euro), while the other dimensions reflects the 
future terms with payments of the underlying financial 
instrument, according to the frequency of the financial instrument 
(e.g. annualized rates in the case of the euro curve). For 
simplicity, market conventions are not used, since its effect is 
negligible. 
Step F.- Selection of the rest of inputs of the method of extrapolation 
in accordance with sections 4 a nd 7: LLP (table 2 and subsection 7.B), 
ultimate forward rate (subsection 7.C), convergence period, tolerance 
(1 basis point) and lower bound of alpha parameter (0.05) (subsection 
7.D). 
Step G.- Application of the method of extrapolation (subsection 7.E). 
Risk-free interest rates term structure with the volatility adjustment 
Step H.- Calculation of the volatility adjustment. This subprocess has 
been described in section 1 1 above. For each relevant currency and 
each relevant country, the volatility adjustmen t is a fixed number, 
expressed in basis points  and rounded to the nearest integer basis 
point, and applied to all maturities till the last liquid point. 
Step I.- Construction of the matrix of cash flows corresponding to the 
zero-coupon annualized rates res ulting from step G. All integer 
maturities until the last liquid point, included, will be used to build th is

86/131 
 
matrix. Furthermore, for each maturity a single payment will be 
considered. Therefore the matrix of this step will usually have different 
dimensions than the one built in step E. 
Step J.- Addition of the annualized volatility adjustment to the matrix 
of cash flows obtained in step I. 
Step K.- Application of the me thod of extrapolation with the same 
inputs used in step F and according to the method me ntioned in step 
G. 
299. The volatility adjustment is not added directly to the par swap rates 
adjusted for credit risk but is added to the zero-coupon spot rates of the 
basic risk-free interest rate term structure obtained after using the Smith -
Wilson method (a s described in an earlier part  of this technical 
documentation).  
300. In accordance with Article 46 of the Delegated Regulation , the volatility 
adjustment is added to the aforementioned zero -coupon spot rates only in 
the liquid part of the curve.  
301. The resultin g rates are the relevant risk -free interest rates including the 
volatility adjustment to which the extrapolation is applied, using again the  
Smith-Wilson method. 
302. Because the volatility adjustment is applied to the liquid zero coupon rates  
of the basic risk -free interest rate term structure , the relevant risk -free 
interest rate term structure including the VA is a parallel shift of the basic 
risk-free interest rate term structure  until the LLP. There is no parallel shift 
after the LLP since both the basic an d relevant risk -free curves ultimately 
converge to the same UFR.

87/131 
 
14. Annexes  
 
14.A. Annex to section 3: Relevant currencies 
   
EEA currencies 
ISO 
4217 
Currency Countries where the 
currency is used 
EUR euro Euro area members 
BGN lev Bulgaria 
CHF Swiss franc Liechtenstein, Switzerland 
CZK Czech koruna Czech Republic 
DKK Danish krone Denmark 
GBP pound sterling United Kingdom 
HRK kuna Croatia 
HUF forint Hungary 
ISK króna Iceland 
NOK Norwegian krone Norway 
PLN zloty Poland 
RON leu Romania 
SEK krona Sweden 
 
Other currencies 
AUD Australian dollar Australia 
BRL real Brazil 
CAD Canadian dollar Canada 
CLP Chilean peso Chile 
CNY renminbi-yuan China 
COP Colombian peso Colombia 
HKD Hong Kong dollar Hong Kong 
INR Indian rupee India 
JPY yen Japan 
KRW South Korean won South Korea 
MYR ringgit Malaysia 
MXN Mexican peso Mexico 
NZD New Zealand dollar New Zealand 
RUB Russian rouble Russia 
SGD Singapore dollar Singapore 
THB baht Thailand 
TRY Turkish lira Turkey 
TWD new Taiwan dollar Taiwan 
USD US dollar United States 
ZAR rand South Africa

88/131 
 
14.B. Annex to section 4: Identification of reference 
instruments and DLT assessment 
303. Solvency II sets out market consistency as a core principle for the 
assessment of the financial and solvency position of insurance and 
reinsurance undertakings . The principle of market consistency applies to 
both assets and liabilities .21 In particular , for the calculation of technical 
provisions the relevant risk-free interest rate term structure should be used. 
That term structure  should be based on upon up -to-date and credible 
information.22 
304. These principles underpin the assessment of the depth, liquidity and 
transparency of markets where the  interest rates are observed. As well as 
providing assurance that the relevant DLT requirements are me t, the DLT 
assessment should foster the optimal use of the information provided by 
financial markets.23 
305. In developing the methodology applied for the DLT assessment, EIOPA has 
analysed the generally applied practices and the academic literature on the 
issue. This analysis has dealt in particular with the process of the liquidity 
assessment, but has also considered the available  measures of depth and 
transparency. 
306. As part of the preparation and follow -up of the Long-term Guarantees 
Assessment, EIOPA developed a conceptual framework for DLT assessment 
based on the aforementioned analysis  in 2013. This conceptual framework 
was put into practice on a tentative basis for the EIOPA Stress Test 2014.  
307. EIOPA’s work and lessons learnt during 2013 are in line with EBA’s report 
on high quality liquid assets (HQLA).24  
308. While acknowledging the differences between the banking and insurance 
sectors, EIOPA recognises the existence of commonalities between the DLT 
assessment for risk-free interest rate term structures and the work carried 
out by EBA on HQLA. 
                                       
21 Recital 53, Articles 75 and 76 of the Solvency II Directive 
22 Recital 58 and Article 77 of the Solvency II Directive 
23 Recital 45 of the Solvency II Directive 
24 Report on appropriate uniform definitions of extremely high quality liquid assets (extremely 
HQLA) and high quality liquid assets (HQLA) and on operational requirements for liquid assets 
under Article 509(3) and (5) CRR, 
http://www.eba.europa.eu/documents/10180/16145/EBA+BS+2013+413+Report+on+definition+
of+HQLA.pdf

89/131 
 
309. Although t here is a set of generally applied metrics for the purpose  of 
making a DLT assessment , carrying out the assessment in practice is  
currently constrained by the following limitations: 
310. While there is a general approac h to assessing liquidity and depth, the 
precise definitions of these terms depend on the context. For example, the 
definition of ‘liquidity’ for the purpose of the Liquidity Coverage Ratio (LCR) 
in the banking sector is quite similar to its definition in the case of the DLT 
assessment in the insurance sector. Having said that, the purpose of the 
DLT assessment is focused on ensuring the reliability of market interest 
rates rather than the need to convert assets into cash. 
311. There are several factors influencing the liquidity (and depth) of financial 
markets. Further, the influence of these factors varies across markets (e.g. 
according to their practices, conventions and operational rules ) and also 
varies over time within the same market (e.g. according to chan ges in the 
environment). Finding a generalized way to measure the level of th ese 
factors is the subject of continuing research. 
312. It is generally accepted that no single metric can be conclusive in assessing 
the DLT nature of a financial instrument. For example, high trading volumes 
and turnovers indicate that assets are liquid, while the converse does not 
necessarily hold true (some assets may be in high demand without being 
traded often, and hence could be easily liquidated if necessary).25 
313. There are severe limitations for the calculation of some metrics, in terms of 
the availability and reliability of the inputs necessary for the calculation and 
the completeness or homogeneity of the data series. In particular for the 
swap market, the lack of information on real trading volumes means that it 
is not possible to use some of the main indicators generally used when 
making DLT assessments of other types of instrument . This limitation has 
particular importance because Solvency II  prescribes swaps as the first 
choice of instrument for deriving the relevant risk -free interest rate term 
structure. 
314. Finally, practitioners, academics and supervisors acknowledge the relevance 
of supplementing quantitative metrics with qualitative or expert judgement. 
EIOPA supports the appropriate consideration of qualitative information, and 
this view is also reflected in the EBA report on HQLA.26 In particular, EIOPA 
is of the view that the assessment of the depth of a financial market should 
take into account the existence of appropriate supervision; such supervision 
can be an effective mechanism to ensure that large transactions will only 
affect prices according to the natural trends of the market, and not because 
                                       
25 EBA report on HQLA (p. 16) 
26  EBA report on HQLA (p. 26)

90/131 
 
of any spurious influence. Another relevant qualitative consideration for the 
assessment of market  depth is the way in which market prices  are 
collected; market data providers have developed effective methods and 
controls that can help to give reassurance that the influence of large 
transactions or unusual trades on prices is likely to be immaterial. 
315. The following annexes describe EIOPA’s approach to the DLT assessment, 
separately for the following two cases: 
a. EEA currencies, for which it is feasible to obtain ad-hoc information 
on pricing and trading (except for traded volumes for  swaps, as 
mentioned above). 
b. Non-EEA currencies, for which EIOPA has adapted its methodology 
to account for  data limitations. In particular this approach includes 
those metrics used by EBA that do not rely on either traded volumes 
or on any other information that is not generally available. 
316. In both cases, EIOPA ’s methodology aims to provide a  stable DLT 
assessment; this is considered a necessary condition to allow insurance and 
reinsurance undertakings to implement the relevant calculation processes. 
Therefore, as a general rule , hard thresholds and the automatic use of 
benchmarks have not been considered appropriate. For example, comparing 
the bid-ask spreads of one currency against another does not necessarily 
provide conclusive evidence for a DLT assessment, not only because of the 
specifics of each financial market (level of interest rates, trends,  etc.), but 
also because experience shows that the relative positions of two currencies 
may change over time.

91/131 
 
14.C. Annex to subsection 4.B: DLT assessment of EEA 
currencies 
317. The DLT assessment for EEA currencies is based on the conceptual 
framework that EIOPA developed for the purposes of the L ong-term 
Guarantees Assessment in 2013. 
318. As mentioned in the general annex to Section 4 above, each of the depth, 
liquidity and transparency criteria lacks a globally accepted clear definition 
that is of practical use. Even in academic literature a wide range of 
measures for depth and liquidity exist; however, none of those measures is 
considered authoritative and applicable in all markets. 
319. Therefore, the list of criteria mentioned below should be considered as non-
exhaustive. EIOPA has focused on criteria that may be helpful in assessing 
the credibility of market data for interest rate swaps  and government 
bonds. Additional criteria consider the general bond market. The criteria are 
as follows: 
a. Bid-ask spread: the price difference between the highest price a 
buyer would pay and the lowest price for which a seller would sell 
b. Trade frequency: number of trades that take place within a defined 
period of time 
c. Trade volume 
d. Trader quotes/dealer surveys (incl. dispersion of answers); 
e. Quote counts (1): number of dealer quotes within a window of a few 
days; 
f. Quote counts (2): number of dealers quoting 
g. Number of pricing sources 
h. Assessment of large trades and movement of prices (depth) 
i. Only applicable to the euro: residual volume approach for bonds.

92/131 
 
14.D. Annex to subsection 4.C: DLT assessment of non -EEA 
currencies 
 
320. The DLT assessment of non -EEA currencies is based, in addition to  
qualitative analysis, on the joint consideration of three main methodologies: 
a. volatility analysis; 
b. analysis of bid-ask spreads (both direct observations and also using 
the Roll measure, as described below); 
c. quantitative analysis. 
321. The DLT assessment methodology presented in  this annex is going to be 
applied to  non-EEA currencies . Results of that methodology  for EEA 
currencies are presented only for illustration purposes. The DLT assessment 
for EEA currencies will be conducted according to methodology described in 
subsection 4.B. 
14.D.1. Volatility analysis 
322. For the volatility analysis, t he behaviour of the available interest rates for 
each maturity and non -EEA currency over the past 105 business days is 
analysed (this is approximately a chronological period of five months). 
323. The analysis is conducted for rates directly observed in markets ( e.g. par 
swap rates where swaps are the financial instrument used as reference), for 
zero-coupon spot rates, and finally for the 1 -year forward rate term 
structure. 
324. For each of the three set s of rates  above, and for each currency and 
maturity, the analysis considers both the values of the rate and the 
behaviour of the volatility calculated considering the last 21 
days27(approximately one chronological month). Therefore, 84 values of the 
                                       
27 The following formula is used: 
Volatility = standard deviation of natural logarithms of variations = 
=   
 

1
))(( 2
n
nccn i   where 
1
lnln


k
k
k
rate
ratec and 
nc  denotes the si mple 
average of the last 21 daily logarithmic changes. 
Note that no 
t adjustment is applied in order to derive annual volatilities. This has no 
impact on the conclusions to the extent the DLT analysis aims at comparing volatilities, not  
at assessing its values on an annual basis.

93/131 
 
volatility for e ach rate are calculated , with rolling windows referring to the 
last 105 trading days (i.e. for the oldest 21 dates in the series, no volatility 
is calculated, as  these dates do not have the  21-day period of reference 
necessary for the calculation). 
325. The ana lysis described in the paragraphs above is used to conduct three 
tests and to produce the set of statistics described below. 
326. The first test focuses on how the rate for a given maturity behaves during 
the 105 day window (both the level of the rate itself and its 21 -day 
volatility). 
327. As an example, the charts below show the behaviour of the 10 -year (first 
two charts) and 25-year rates and volatilities (second two charts) for the 
Canadian dollar, as of 31 December 2014, using the par swap market rates. 
 
 
328. There are several ways of inferring an empirical view on the behaviour of 
the interest rates. For example, by considering the values of the rates (y -
axis in the left chart) and the level of the volatility (y-axis on the right hand 
side), by considering the lack of/presence of repeated sudden changes in 
the level of the volatility, or by examining the range of variation in both 
charts. From these perspectives the rates for both maturities show a similar 
pattern, and do not convey abnormal features.

94/131 
 
 
329. The second test aims to  detect whether the rate for a given maturity 
produces humps or hollows in the term structure curve (i.e. by comparing 
with the behaviour of neighbouring maturities). 
330. Again using the example of the Canadian curve as at 31 December 2014, it 
can be seen that the curve does not present abnormal features and the 21 -
days volatility of all observable maturities is in a reasonable range (note the 
LLP for the Canadian currency is 25 years, therefore the part of the curve 
for maturities longer than 25 years does not represent market data, but the 
Smith-Wilson extrapolation). 
 
 
331. For the third analysis, a comparison across currencies has been developed. 
The comparison is used in  situations where there is an adequate 
relationship between the non-EEA currency now being analysed and an  EEA 
currency whose DLT nature has been tested as described in section  4.B. 
This third test aims to verify whether the behaviour of the non -EEA rate is 
sufficiently similar to its ‘peer’ EEA rate.

95/131 
 
332. For example, the charts below compare the behaviour of 50-year maturities 
for GBP and USD as at 31 December 2014 using par swap rates ( note that 
the similarity of behaviours between these currencies is also observed when 
using zero-coupon rates and forward rates). 
 
 
 
333. The charts below compare the behaviour of 25 -year maturities for GBP and 
CHF as at 31 December 2014 using 1 -year forward rates ( note that the 
similarity of behaviours is also observed when using  par swap rates and 
zero-coupon rates).

96/131

97/131 
 
14.D.2. The analysis of bid-ask spreads: Direct observation 
334. For all currencies where a  ‘likely’ longest DLT maturit y has been 
established, a direct investigation of the specific bid-ask spreads at these 
maturities is  also carried out. The following metrics are obtained for the 
month prior to the reference date and also for the last quarter: 
a. Median of bid-ask spreads during the last month 
b. 80thPercentile of bid-ask spreads during the last month 
c. Maximum of bid-ask spreads during the last month 
d. Simple Average of bid-ask spreads during the last month 
e. Last  spread (at the date of reference of the curve) 
f. Number of days with zero spreads. 
335. The table s below summar izes some findings for long-term maturities of 
swaps as of 31 December 2014 (currencies identified according to ISO 4217 
in all tables): 
Analysis of bid-ask spread for 15-year interest rates swaps IBOR 
 
Analysis of bid-ask spread for 20-year interest rates swaps IBOR 
Zero 
observat
ions
Median 
non-zero 
spreads
Percentile 80 
non-zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero spread
Zero 
observatio
ns
Median 
non-zero 
spreads
Percentile 
80 non-
zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero 
spread
EUR 0 2.25            4.00                  4.00                 2.34            2.40                0 3.00            4.00            4.00            2.58            2.40            
BGN 48 260.00        260.00             260.00            260.00        260.00            5 260.00        260.00        260.00        260.00        260.00        
CZK 0 4.00            4.00                  7.00                 4.22            4.00                0 4.00            4.00            4.00            3.86            4.00            
DKK 0 3.00            3.00                  7.00                 3.06            7.00                0 3.00            4.73            7.00            3.70            7.00            
HUF 3 6.00            7.45                  10.00              5.93            10.00              0 6.00            6.00            10.00          5.21            10.00          
LIC 0 4.00            4.00                  10.00              3.61            4.00                0 4.00            4.00            10.00          3.62            4.00            
NOK 0 10.00          10.00               10.00              7.54            4.00                0 5.00            10.00          10.00          6.44            4.00            
PLN 0 3.00            4.00                  6.00                 3.37            3.00                0 3.00            3.00            3.00            3.00            3.00            
RON 0 140.00        140.00             140.00            140.00        140.00            0 140.00        140.00        140.00        140.00        140.00        
RUB 0 14.00          14.00               14.00              14.00          14.00              0 14.00          14.00          14.00          14.00          14.00          
SEK 0 3.00            3.10                  6.00                 3.17            3.00                0 3.00            3.00            3.10            2.88            3.00            
CHF 0 4.00            4.00                  10.00              3.61            4.00                0 4.00            4.00            10.00          3.62            4.00            
GBP 0 1.00            1.00                  1.90                 1.00            1.80                0 1.00            1.56            1.90            1.13            1.80            
AUD 0 3.00            4.00                  8.50                 3.45            4.00                0 3.00            4.00            8.50            3.60            4.00            
CAD 0 3.17            4.00                  6.10                 3.09            4.00                0 3.42            4.00            5.90            3.06            4.00            
CLP 2 4.00            5.00                  5.00                 4.21            4.00                2 4.00            4.70            5.00            4.21            4.00            
CNY 3 40.00          40.00               59.00              40.51          40.00              0 39.00          40.00          59.00          40.33          40.00          
HKD 2 7.00            7.10                  10.00              7.25            10.00              2 7.00            7.10            10.00          7.48            10.00          
JPY 0 2.00            2.00                  8.00                 2.20            2.00                0 2.00            2.00            8.00            2.24            2.00            
MYR 0 10.00          10.00               10.00              9.94            10.00              0 10.00          10.00          10.00          10.00          10.00          
MXN 0 4.00            4.00                  6.00                 4.00            4.00                0 4.00            4.60            6.00            4.27            4.00            
NZD 3 1.00            1.74                  8.00                 2.00            0.75                1 0.75            1.00            8.00            1.39            0.75            
SGD 0 7.00            7.00                  7.10                 5.88            7.00                0 7.00            7.00            7.00            6.12            7.00            
ZAR 0 8.00            10.00               10.00              8.06            8.00                0 8.00            10.00          10.00          8.25            8.00            
KRW 0 3.00            3.50                  3.50                 3.20            3.00                0 3.00            3.50            3.50            3.17            3.00            
THB 0 9.00            10.00               12.00              8.84            9.00                0 9.00            10.00          10.00          8.71            9.00            
TRY 0 40.00          40.00               42.00              40.08          40.00              0 40.00          40.00          41.00          40.05          40.00          
USD 2 0.40            0.51                  0.80                 0.39            0.50                -               0.45            0.56            0.80            0.43            0.50            
Last 64 days with trading Last 21 days with trading

98/131 
 
 
 
Analysis of bid-ask spread for 25-year interest rates swaps IBOR 
  
Zero 
observa
tions
Median 
non-zero 
spreads
Percentile 80 
non-zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero spread
Zero 
observati
ons
Median 
non-zero 
spreads
Percentile 
80 non-
zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero 
spread
EUR 0 2.18            4.00                  4.00                 2.28            2.40                0 2.66            4.00            4.00            2.52            2.40            
BGN 48 260.00        260.00             260.00            260.00        260.00            5 260.00        260.00        260.00        260.00        260.00        
CZK 0 4.00            4.00                  7.00                 4.20            4.00                0 4.00            4.00            4.00            3.86            4.00            
DKK 0 3.00            3.00                  7.00                 3.12            7.00                0 3.00            4.80            7.00            3.63            7.00            
HUF 4 6.00            10.00               10.00              6.67            6.00                1 6.00            6.00            6.00            5.73            6.00            
LIC 0 4.00            4.00                  10.00              3.66            5.00                0 3.00            4.30            10.00          3.33            5.00            
NOK 0 15.50          15.50               15.50              14.66          3.70                0 15.50          15.50          15.50          12.94          3.70            
PLN 1 3.00            3.97                  6.00                 3.25            3.00                0 3.00            3.00            3.00            2.89            3.00            
RON 0 140.00        140.00             140.00            140.00        140.00            0 140.00        140.00        140.00        140.00        140.00        
RUB 2 10.00          60.00               61.00              24.53          60.00              2 60.00          60.70          61.00          55.42          60.00          
SEK 0 3.00            3.10                  8.00                 3.57            3.00                0 3.00            3.10            6.00            3.15            3.00            
CHF 0 4.00            4.00                  10.00              3.66            5.00                0 3.00            4.30            10.00          3.33            5.00            
GBP 0 1.18            1.33                  13.10              1.69            1.16                0 1.18            1.45            13.10          2.68            1.16            
AUD 0 3.68            4.00                  4.00                 3.67            4.00                0 3.62            4.00            4.00            3.65            4.00            
CAD 0 3.38            4.00                  6.10                 3.10            4.00                0 3.93            4.05            6.10            3.28            4.00            
CLP 2 4.00            5.00                  5.00                 4.21            4.00                2 4.00            5.00            5.00            4.26            4.00            
JPY 0 2.00            2.00                  8.00                 2.20            2.00                0 2.00            2.00            8.00            2.24            2.00            
MYR 0 10.00          10.00               10.00              9.97            10.00              0 10.00          10.00          10.00          10.00          10.00          
MXN 20 3.00            3.00                  3.00                 3.00            3.00                14 3.00            3.00            3.00            3.00            3.00            
NZD 0 1.00            5.73                  8.00                 2.36            8.00                0 1.00            3.10            8.00            2.25            8.00            
SGD 0 7.00            7.00                  7.70                 6.10            7.00                0 7.00            7.00            7.70            6.39            7.00            
ZAR 0 8.00            8.00                  11.00              7.24            8.00                0 8.00            8.00            11.00          8.00            8.00            
KRW 0 3.25            3.50                  3.50                 3.24            3.50                0 3.50            3.50            3.50            3.31            3.50            
THB 0 15.00          15.00               31.50              13.01          6.00                0 15.00          15.00          15.00          12.00          6.00            
TRY 0 20.00          20.00               21.00              20.02          20.00              0 20.00          20.00          21.00          20.05          20.00          
USD 0 0.40            0.55                  0.80                 0.41            0.50                -           0.48            0.57            0.80            0.44            0.50            
Last 64 days with trading Last 21 days with trading
Zero 
observa
tions
Median 
non-zero 
spreads
Percentile 80 
non-zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero spread
Zero 
observati
ons
Median 
non-zero 
spreads
Percentile 
80 non-
zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero 
spread
EUR 0 2.46            4.00                  4.00                 2.43            2.40                0 3.00            4.00            4.00            2.56            2.40            
CZK 0 4.00            4.00                  7.00                 4.45            4.00                0 4.00            4.00            4.00            4.00            4.00            
DKK 0 3.00            3.00                  7.00                 3.25            7.00                0 3.00            4.20            7.00            3.76            7.00            
LIC 0 6.00            6.00                  10.00              4.48            5.00                0 3.00            5.30            10.00          3.41            5.00            
NOK 0 17.50          17.50               21.30              16.94          3.70                0 17.50          17.50          17.50          15.60          3.70            
SEK 1 3.00            5.00                  8.00                 3.77            3.00                1 3.00            5.00            8.00            3.56            3.00            
CHF 0 6.00            6.00                  10.00              4.48            5.00                0 3.00            5.30            10.00          3.41            5.00            
GBP 0 1.00            1.00                  1.70                 1.00            1.00                0 1.00            1.00            1.70            1.02            1.00            
AUD 0 3.56            4.00                  4.00                 3.66            4.00                0 3.62            4.00            4.00            3.65            4.00            
CAD 0 3.00            4.00                  6.10                 3.04            4.00                0 3.45            4.00            6.00            3.25            4.00            
JPY 0 2.00            2.00                  8.00                 2.39            8.00                0 2.00            2.00            8.00            2.47            8.00            
MYR 0 10.00          10.00               10.00              9.97            10.00              0 10.00          10.00          10.00          10.00          10.00          
NZD 7 1.00            1.00                  1.00                 1.00            1.00                0 1.00            1.00            1.00            1.00            1.00            
ZAR 0 8.00            10.00               10.00              7.95            8.00                0 8.00            10.00          10.00          8.40            8.00            
KRW 0 3.50            3.50                  3.50                 3.26            3.50                0 3.50            3.50            3.50            3.33            3.50            
USD 0 0.40            0.60                  0.85                 0.45            0.60                0 0.50            0.60            0.69            0.48            0.60            
Last 64 days with trading Last 21 days with trading

99/131 
 
Analysis of bid-ask spread for 30-year interest rates swaps IBOR 
 
 
Analysis of bid-ask spread for 50-year interest rates swaps IBOR 
 
Zero 
observa
tions
Median 
non-zero 
spreads
Percentile 80 
non-zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero spread
Zero 
observati
ons
Median 
non-zero 
spreads
Percentile 
80 non-
zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero 
spread
EUR 0 3.00            3.00                  3.00                 2.28            1.00                0 3.00            3.00            3.00            2.39            1.00            
CZK 0 4.00            4.00                  7.00                 3.95            4.00                0 4.00            4.00            4.00            3.81            4.00            
DKK 0 3.00            3.00                  7.00                 2.94            7.00                0 3.00            4.80            7.00            3.43            7.00            
LIC 0 6.00            6.00                  10.00              4.91            6.00                0 6.00            6.00            10.00          4.66            6.00            
NOK 0 17.50          17.50               17.50              16.55          3.70                0 17.50          17.50          17.50          15.77          3.70            
PLN 0 4.00            4.00                  6.00                 4.08            4.00                0 4.00            4.00            4.00            4.00            4.00            
SEK 0 5.37            6.00                  10.00              5.05            3.00                0 3.00            6.00            10.00          4.57            3.00            
CHF 0 6.00            6.00                  10.00              4.91            6.00                0 6.00            6.00            10.00          4.66            6.00            
GBP 0 0.95            1.00                  2.00                 0.98            1.80                0 1.00            1.83            2.00            1.17            1.80            
AUD 0 3.75            4.00                  5.00                 3.64            4.00                0 3.75            4.00            4.00            3.68            4.00            
CAD 0 4.00            4.00                  6.10                 3.92            4.00                0 4.00            4.00            6.10            4.00            4.00            
JPY 0 2.00            2.00                  8.00                 2.40            8.00                0 2.00            2.00            8.00            2.52            8.00            
SGD 0 5.00            6.00                  8.00                 5.24            6.00                0 5.00            6.00            8.00            5.33            6.00            
ZAR 0 8.00            8.00                  10.00              7.53            8.00                0 8.00            8.00            10.00          7.86            8.00            
KRW 0 3.50            3.50                  3.50                 3.26            3.50                0 3.50            3.50            3.50            3.33            3.50            
USD 1 0.44            0.70                  1.45                 0.47            0.72                0 0.48            0.71            0.92            0.49            0.72            
Last 64 days with trading Last 21 days with trading
Zero 
observa
tions
Median 
non-zero 
spreads
Percentile 80 
non-zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero spread
Zero 
observati
ons
Median 
non-zero 
spreads
Percentile 
80 non-
zero 
spreads
Maximum 
spread 
Average 
non-zero 
spreads
Last non-
zero 
spread
EUR 0 3.00            3.00                  3.00                 2.39            2.00                0 3.00            3.00            3.00            2.49            2.00            
LIC 0 10.00          10.00               10.00              10.00          10.00              0 10.00          10.00          10.00          10.00          10.00          
CHF 0 10.00          10.00               10.00              10.00          10.00              0 10.00          10.00          10.00          10.00          10.00          
GBP 0 1.00            1.00                  2.00                 1.07            1.80                0 1.00            1.52            2.00            1.21            1.80            
USD 0 1.20            2.00                  2.10                 1.36            2.00                0 1.20            2.00            2.00            1.45            2.00            
Last 64 days with trading Last 21 days with trading

100/131 
 
14.D.3. The analysis of bid-ask spreads: Roll measure 
336. For this analysis,  EIOPA has followed the approach used in the EBA report 
on HQLA. Roll (1984)28 shows that under certain conditions, the percentage 
bid/ask spread equals two times the square root of minus the covariance 
between consecutive returns: 
),cov(2 1 kkt rrRoll
,   
where t is the time period over which the measure is calculated and rk = 
pricek – pricek-1.  
The higher value of Roll measure, the lower liquidity of the analysed interest 
rate.  
337. EIOPA’s analysis considers a daily Roll measure, using a 21 trading day 
rolling window in the computation of the covariance. In cases where a 
positive covariance is found, the Roll measure is set to zero. 
338. The set of analy tical tests  described for the volatility analysis  are also  
applied for the Roll measure, although in this case only the zero coupon 
rates are examined. This approach (examining only the zero coupon rates) 
does not have a material influence on the outcome of the assessment, 
because all the information is already captured in the chart analysis for both 
the volatility and the Roll measurement. 
14.D.4. Quantitative analysis 
339. As mentioned in Annex 3, EIOPA does not consider it appropriate to app ly 
hard thresholds purely based on quantitative metrics, because it is 
necessary to make an appropriate allowance for the characteristics of each 
individual market and for prevailing financial conditions. 
340. For the same reasons , metrics that can be calculated as at  a specific date 
should be supplemented by examining the behaviour of these metrics 
during the rolling windows of the period of observation mentioned above 
(105 days). 
341. Thus, additional relevant metrics are as follows: 
a. Number of days without any available data; 
b. Median of spot zero coupon rates during the 105  day period of 
observation. This provides a metric to measure the ‘size effect ’, 
                                       
28 Richard Roll (1984), A Simple Implicit Measure of the Effective Bid -Ask Spread in an Efficient 
Market. The Journal of Finance, 39: 1127–1139.

101/131 
 
which is currently material both across currencies and across 
maturities within the same currency. 
c. Trend of interest  rates during the period (obtained as the first 
degree coefficient of a linear fitting with LSM). This metric is 
necessary for a n appropriate assessment of other metrics, to the 
extent that the existence of a clear and strong trend in interest 
rates, influences other metrics (e.g. the Roll measure). 
d. For the series of zero coupon rates, the i nterquartile range (Q 75 – 
Q25) relative to the median. 
e. For the series of zero coupon rates, the number of outliers, 
calculated a s the number of interest rates falling ou tside of  the 
interval (mean - 1.5 standard deviation s; mean + 1.5 standard 
deviations). Note that  these statistics are calculated using only the 
interest rates between the 12.5 th and 87.5 thpercentiles (thus 
avoiding any influence on the mean or standard deviation of ‘large’ 
outliers). 
f. Last 21-day volatility observed in the 105 day period. 
g. For the series of first order difference s of zero coupon rates, the 
interquartile range (Q75 – Q25) relative to the median. 
h. For the series of first order difference s of ze ro coupon rates, the 
number of outliers as described above. 
i. Last observed Roll measure. 
j. 90thPercentile for the series of Roll measurements. 
k. 90thPercentile of logarithmic returns. 
342. The table below provides an illustrative example of the outputs of these 
metrics, for those non-EEA currencies where it has been possible to obtain 
interest rates for 40-year maturities.   
343. As mentioned above, this qu antitative analysis is supplemented with the 
other analysis mentioned in this annex.

102/131 
 
14.E. Annex to Section 4: History of relevant financial 
instruments 
344. The following tables  specify the relevant financial instruments that were 
used to derive the risk-free interest rates in the past since 1 January 2016 . 
For currencies that do not appear in those tables the  relevant financi al 
instruments are unchanged since 1 January 2016. The currently used 
financial instruments are set out in tables 2, 5 and 6 of the main text.  
EEA currencies 
 Financial instruments used 
SWP=swaps, GVT=government bonds. All 
maturities in years 
Period 
HRK GVT 1-4, 10 1 January – 30 December 
2016  
ISK GVT 2, 4, 5, 8, 10  1 January – 30 December 
2016 
 
Non-EEA currencies 
 Financial instruments used 
SWP=swaps, GVT=government bonds. All 
maturities in years 
Period 
CAD SWP 1-10, 12, 15, 20, 25 1 January – 30 December 
2016  
CLP SWP 1-10 1 January – 30 December 
2016 
CNY SWP 1-10 1 January – 30 December 
2016  
COP SWP 1-5, 7, 8, 10 1 January – 30 December 
2016 
JPY SWP 1-20, 25, 30 1 January – 30 December 
2016  
MYR SWP 1-10, 12, 15, 20 1 January – 30 December 
2016 
MXN GVT 1-10, 15, 20 1 January – 30 December 
2016  
SWP 1-5, 7, 10, 16, 21 31 December 2016 
RUB SWP 1-10 1 January – 30 December 
2016 
SGD SWP 1-10, 12, 15, 20 1 January – 30 December 
2016

103/131 
 
THB SWP 1 to 10, 12, 15 1 January – 30 May 2016 
USD SWP 1-15, 20, 25, 35, 30, 40, 45, 
50 
1 January – 30 December 
2016 
 
14.F. Annex to Subsection 7.A: Numerical illustration of the 
extrapolation of term structures 
345. With the data in the canonical normalized format as given on the next page 
and where the ultimate forward intensity =log(1.042) and convergence 
period S=40, the following results are obtained for the key parameters of 
the Smith-Wilson method: 
 
 
 
346. With , , u and Qb the Smith -Wilson present value function can be 
evaluated for any maturity v: 
 Qbu),(1)( vHevp v  
 
 
347. The yield intensity follows as: 
v
vpvy )(log)( 
 
and the annualized yield rate can be calculated as a fractional power of the 
present value function or as the exponential of the yield intensity:

104/131 
 
 
  
 
348. Besides the data tableau in canonical norma lized format on the next page s, 
also a graph of the yield and forward intensity curve is displayed  and a 
tabulation of yield intensity together with annualized yield rate for 
maturities from 0 up to 120 years. 
    1)(exp1)(
1


vyvp v

105/131

106/131

107/131 
 
 
Table of spot yield intensities (continuous curve) 
and annualized spot yield rates.

108/131 
 
14.G. Annex to subsection 7.C: Methodology for the 
derivation of the UFR 
1. Introduction 
349. This annex sets out the methodology to derive the (UFR) and its 
implementation as decided by EIOPA at the end of March 2 017. The 
methodology is in accordance with Article 47 of the Delegated Regulation 
on Solvency II 29 which requires in particular that such a methodology shall 
be clearly specified in order to ensure the performance of scenario 
calculations by insurance and reinsurance undertakings.  
 
 
2. Methodology to derive the UFR 
Update of the UFRs 
350. EIOPA will annually calculate the UFRs and, where they are sufficiently 
different according to the methodology from the then applicable UFRs, 
update them at the beginning of th e next year. The updated UFRs will be 
announced every year by the end of March  on EIOPA’s website . Nine 
months after the announcement of the updated UFRs, EIOPA will use them 
to calculate the risk -free interest rate term structures for the term 
structures of 1 January of the following year.  
 
Calculation of the UFRs 
351. For each currency the change of the UFR is limited in such a way that it 
increases or decreases by 15 bps or remains unchanged in accordance with 
the following rule:  
𝑈𝐹𝑅𝑡
𝐿={
𝑈𝐹𝑅𝑡−1
𝐿 +15⁡𝑏𝑝𝑠 𝑖𝑓⁡⁡𝑈𝐹𝑅𝑡≥𝑈𝐹𝑅𝑡−1
𝐿 +15⁡𝑏𝑝𝑠 ⁡
𝑈𝐹𝑅𝑡−1
𝐿 −15⁡𝑏𝑝𝑠 𝑖𝑓⁡⁡𝑈𝐹𝑅𝑡≤𝑈𝐹𝑅𝑡−1
𝐿 −15⁡𝑏𝑝𝑠 ⁡
𝑈𝐹𝑅𝑡−1
𝐿 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 ⁡
 
where:  
 𝑈𝐹𝑅𝑡
𝐿 denotes the UFR of year t, after limitation of the annua l 
change,  
                                       
29 Commission Delegated Regulation (EU) No 2015/35 of 10 October 2014 supplementing Directive 2009/138/EC of the 
European Parliament and of the Council on the taking-up and pursuit of the business of Insurance and Reinsurance 
(Solvency II) (OJ L 12, 17.01.2015, p. 1)

109/131 
 
 𝑈𝐹𝑅𝑡−1
𝐿  denotes the UFR of year t+1 , after limitation of the annual 
change, 
 𝑈𝐹𝑅𝑡  denotes the UFR of year t, before limitation of the annual 
change. 
352. For each currency the UFR before limitation of the annual change is the sum 
of an expected real rate and an expected inflation rate. The expected real 
rate is the same for each currency. The expected inflation rate is currency -
specific. 
 
Calculation of the expected real rate 
353. The expected real rate is the simple arithmetic mean of ann ual real rates 
from 1961 to the year before the recalculation of the UFRs according to the 
following formula:  
𝑅=1
𝑛∑𝑟1960+𝑖
𝑛
𝑖=1
 
where:  
 R is the expected real rate, 
 n is the number of years since end of 1960, 
 ri is the annual real rate for the year 1960+i, 
354. For each of the years since 1961 the annual real rate is derived as the 
simple arithmetic mean of the annual real rates of Belgium, Germany, 
France, Italy, the Netherlands, the United Kingdom and the United States.      
355. For each of those years and each country the annual real rate is calculated 
as follows: 
real rate = (short-term nominal rate – inflation rate)/(1 + inflation rate).  
356. The short-term nominal rates are taken from the annual macro -economic 
database of the European Commission (AMECO database). 30 The inflation 
rates are taken from the Main Economic Indicators database of the OECD.31  
                                       
30 Short-term nominal rates used for deriving the expected real rate can be found in the annual macro-economic database 
of the European Commission's Directorate General for Economic and Financial Affairs, “AMECO”. On AMECO online, select 
13-Monetary variables, select Interest Rates and then tick the box Short-term nominal (ISN). 
(http://ec.europa.eu/economy_finance/ameco/user/serie/ResultSerie.cfm) 
31 Inflation rates used for deriving the expected real rate can be found on the website of the Organisation for Economic Co-
operation and Development (OECD): go to the OECD Main Economic Indicators (MEI) and select consumer price indices. 
When accessing the database, choose consumer prices – all items for the subject, percentage change on the same period 
of the previous year for the measure and percentage for the unit.

110/131 
 
357. The expected real rate is rounded to full five basis points as follows: 
 When the unrounded rate is lower than the rounded rate of the 
previous year, the rate is rounded upwards. 
 When the unrounded rate is higher than the rounded rate of the 
previous year, the rate is rounded downwards. 
 
Calculation of the expected inflation rate   
358. For currencies where the central bank has announced an inflation target, 
the expected inflation is based on that inflation target according to the 
following rules: 
 The expected inflation rate is: 
o 1%, where the inflation target is lower than or equal to 1%, 
o 2%, where the inflation target is higher than 1% and lower than 
3%,  
o 3%, where the inflation target is higher or equal to 3% and 
lower than 4%, 
o 4%, where the inflation target is 4% or higher. 
 
 Where a central bank is not targeting a specific inflation figure but tries 
to keep the inflation in a specified corridor, the midpoint of that 
corridor is relevant for the allocation to the four inflation rate buckets.  
 
359. For currencies where the ce ntral bank has not announced an inflation 
target, the expected inflation rate is 2% by default. However, where past 
inflation experience and projection of inflations both clearly indicate that 
the inflation of a currency is expected in the long -term to be at least 1 
percentage point higher or lower than 2%, the expected inflation rate will 
be chosen in accordance with those indications. The expected inflation rate 
will be rounded downwards to full percentage points.  
360. The past inflation experience will be as sessed against the average of 10 
years annual inflation rates. The projection of inflation rates will be derived 
on the basis of an autoregressive–moving-average model.  
 
                                                                                                                       
(http://stats.oecd.org/Index.aspx?DataSetCode=MEI_PRICES). OECD data used in this document were accessed in March 
2016.

111/131 
 
3. Implementation of the methodology 
361. The methodology to derive the UFR should be impl emented in 2018. The 
first UFRs calculated according to the methodology should be announced at 
the beginning of April 2017. Those UFRs should be applied for the first time 
to calculate the risk-free interest rate term structures for 1 January 2018. 
362. The initial application of the methodology in 2018 should be based on the 
following additional specification: 
 The UFR of 2017, denoted 𝑈𝐹𝑅𝑡−1
𝐿  in paragraph 351, is: 
o 3.2% for the Swiss franc and the Japanese yen,  
o 5.2% for the Brazilian real, the Indian r upee, the Mexican peso, 
the Turkish lira and the South African rand, 
o 4.2% for all other relevant currencies. 
 The rounded expected real rate of the previous year referred to in 
paragraph 353 is equal to 2.2%.

112/131 
 
14.H. Annex to subsection  9.D: Methodology to upda te the 
representative portfolios 
 
1. Introduction 
363. The calculation of the volatility adjustment is based on representative 
portfolios of assets for each currency and country. The initially used 
representative portfolios were based on asset data for the referen ce date 
end of 2013 collected for the 2014 insurance stress test of EIOPA.  
364. It is important for the accuracy and well -functioning of the volatility 
adjustment that the representative portfolios are based on up-to-date data. 
EIOPA has therefore updated the representative portfolio in 2016. The 
update representative portfolios have been applied since 30 September 
2016.  
365. This annex describes the methodology to derive the updated representative 
portfolios. 
 
2. Database 
366. The updated representative portfolios were de rived from the supervisory 
reporting data collected during the preparatory phase of Solvency II. The 
date of reference of those data is 31 December 2014.  
367. Article 77d of the Solvency II Directive distinguishes two different types of 
representative portfolios: 
- The currency representative portfolio: a portfolio “representative for 
the assets which are denominated in that currency and which insurance 
and reinsurance undertakings are invested in to cover the best estimate 
for insurance and reinsurance obligatio ns denominated in that 
currency”. 
 
- The country representative portfolio : a portfolio “representative for 
the assets which insurance and reinsurance undertakings are invested in 
to cover the best estimate for insurance and reinsurance obligations sold 
in th e insurance market of that country and denominated in the 
currency of that country”. 
 
368. The reporting data of solo undertakings collected during the preparatory 
phase of Solvency II allowed for the update of all EEA country and EEA 
currency portfolios except for the following:

113/131 
 
 The LU country representative portfolio because LU did not participate in 
the reporting during the preparatory phase. 
 The DK country and DKK currency portfolios because DK  did not 
participate in the reporting during the preparatory phase. 
 The CHF currency portfolios because data of Swiss solo undertakings 
were not available.    
For these currencies and countries and for the non -EEA currencies and 
countries the initial representative portfolios are still in use. 
 
369. To allow for the calcula tion of the representative portfolios, assets from all 
relevant solo undertakings are aggregated line by line to create a database 
for each country and each currency representative portfolio. This database 
is enriched by several calculations and indicators  to allocate the assets in 
the relevant portfolio and perform the calculations. 
 
3. Composition of the representative portfolios 
370. Each representative portfolio provides the following information: 
- Weights (in percentages) of the  
o central government and central banks bonds – called 
“government portfolio”; and 
o bonds other than above, loans and securitisations – called 
“corporate portfolio”. 
- For the government portfolio, weight of and duration of the following 
relevant issuers: 
o AT, BE, BG, HR, CY, CZ, DK, EE, FI, F R, DE, GR, HU, IE, IT, LV, 
LT, LU, MT, NL, NO, PL, PT, SK, SI, ES, SE, UK, US, IS, LI, AU, 
CA, CH, JP.  
- For the corporate portfolio, weight of and duration for each of the 
following issuers: 
o Financial entities, categorised in seven credit quality steps. 
o Non-financial entities, categorised in seven credit quality steps. 
 
Regional government and local authorities (RGLA): 
371. In the initial representative portfolio, exposures to RGLA were allocated to 
the corporate portfolio in their quality of “non -central government bonds” 
and their spreads were modelled on the basis of the corresponding 
government bond indices.  
372. Because of the adoption of the Commission Implementing Regulation (EU) 
2015/2011 on the list of regional governments and local authorities

114/131 
 
exposures to whom are to be treated as exposures to central government32, 
this allocation was changed as follows: 
- the RGLA listed in the Regulation are allocated to the government 
portfolio; 
- the remaining RGLA are allocated to the corporate portfolio and 
classified as non-financial assets taking into account their credit quality 
step. 
 
4. Assumptions 
373. Given the information available in the preparatory phase reporting, 
assumptions were needed to calculate the representative portfolios. Those 
assumptions, as explained below, a re unchanged compared to the initial 
representative portfolios. 
Currency representative portfolios 
374. As in Solvency II reporting undertakings are not required to identify the 
assets covering their best estimate, an assumption is needed to calculate 
the curre ncy representative  portfolios: all assets in currency X cover 
liabilities in the same currency X. Therefore, the database used for the 
calculation of a given currency representative portfolio was composed of all 
the assets denominated in that same currency held by all solo undertakings 
which participated in the preparatory phase reporting. 
Country representative portfolios 
375. A calculation taking into account in which countries insurance obligations 
were sold would have been most precise. However, in absence o f reliable 
information about the country of sale, the assumption was made that all 
liabilities are sold in the country of the undertaking and denominated in the 
currency of that country. Therefore, the database used for the calculation of 
a given country representative portfolio was composed of all the assets held 
by all solo undertakings of that same country which participated in the 
preparatory phase reporting. 
 
5. Calculation of the weights for the government and corporate 
portfolios 
Assets value used in the calculation 
376. The weights were calculated with the value of assets as reported in the 
reporting field “Total SII amount”, expressed in the currency of the 
                                       
32 See http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32015R2011&from=EN.

115/131 
 
reporting (specific to each undertaking).  The asset value was converted to 
euro so that all assets can be compared. ECB exchange rates were used for 
that purpose. 
377. The converted assets value could not be used directly as the representative 
portfolios needs to be representative of the assets covering the best 
estimate of the insurance and reinsurance oblig ations where the matching 
adjustment does not apply. 
Reduction of the assets value in proportion to the best estimate 
378. The value of the assets was reduced by ratios calculated with the 
information reported in the “balance-sheet” reporting template. 
379. Two reduction factors per undertaking were calculated: one reduction factor 
for assets held in unit-linked/index-linked funds and another one for assets 
not held in unit-linked/index-linked funds. 33  
380. The first ratio was applied to assets held in unit -linked/index-linked funds 
only. All relevant assets have been identified line by line, and their 
Solvency II value has been multiplied by the ratio: (best estimate for unit -
linked/index-linked products)/(overall  technical provisions for unit -
linked/index-linked products). 
381. The second ratio was applied to all other assets. All relevant assets have 
been identified line by line, and their Solvency II value has been multiplied 
by the ratio: (best estimate for all products excluding unit -linked/index-
linked products)/(overall  technical provisions for all products excluding 
unit-linked/index-linked products). 
Reduction of the assets value to take the matching adjustment into account 
382. As the legislation does not allow cumulating the matching adjustment (MA) 
with the volatility ad justment, assets held in a matching adjustment 
portfolio should be excluded from the calculation.  
383. However, the preparatory phase templates do not provide an indication of 
whether an asset is held or not in a MA portfolio. Therefore, an 
approximation was used. Only the countries where significant MA business 
has been authorised by the national supervisory authorities are affected by 
this approximation: Spain and the United Kingdom. For those two 
countries, the authorities provided figures on the share of as sets in MA 
portfolios and their allocation to government and corporate bonds. 
                                       
33 Some unit-linked/index-linked insurance obligations are not or only partly valued as a whole, as 
referred to in the second subparagraph of Article 77(4) of the Solvency II Directive, but a risk 
margin and a best estimate is calculated for them.

116/131 
 
384. The value of each asset not held in unit -linked/index-linked fund is reduced 
with a different ratio, depending on its allocation to the government or 
corporate portfolio. 
 
Allocation of the assets to the government and corporate portfolios 
385. CIC codes (as reported in the field “CIC”) were used to allocate the assets 
to the government or corporate portfolio as set out in the following table: 
 
 
CIC codes 
Government 
portfolio 
11, 13*, 14*, 15, 16, 
17, 19 
Corporate 
portfolio 
12, 13*, 14*, 21, 22, 
23, 24, 25, 26, 27, 28, 
29, 42, 43, 52, 54, 62, 
64, 81, 85, 86, 89 
Other All other CIC codes 
 
(*) The CIC codes 13 and 14 were used to identify bonds issued by RGLA. 
For those assets, the al location to the government or corporate portfolio 
depends on the issuer (identified with the field “Issuer Country”). Where 
no issuer was reported, those assets were allocated to the corporate 
portfolio.  
 
Calculation of the weights for the government and corporate portfolios 
386. The calculation of the weights wgov and wcorp for government and corporate 
bonds was done in accordance with the following formulas: 
𝑤𝑔𝑜𝑣=
𝑀𝑉𝑔𝑜𝑣
𝑀𝑉𝑔𝑜𝑣+𝑀𝑉𝑐𝑜𝑟𝑝+𝑀𝑉𝑜𝑡ℎ𝑒𝑟
 
𝑤𝑐𝑜𝑟𝑝=
𝑀𝑉𝑐𝑜𝑟𝑝
𝑀𝑉𝑔𝑜𝑣+𝑀𝑉𝑐𝑜𝑟𝑝+𝑀𝑉𝑜𝑡ℎ𝑒𝑟
 
where  
MVgov  denotes the market value of assets with CIC codes that are 
allocated to  the government bond portfolio, 
MVcorp  denotes the market value of assets with CIC codes that are 
allocated to  the corporate bond portfolio,

117/131 
 
MVother denotes the market value of all assets with CIC codes that are not 
 allocated to  the government or corporate bond portfolio. 
387. The market values were reduced in proportion to the best estimate and to 
take into account the ma tching adjustment, as described earlier in this 
section. 
 
 
6. Calculation of the government portfolio  
Identification of issuers 
388. The country of the issuer is reported in the list of assets template with the 
field “Issuer Country”. Only assets of the following  issuers were taken into 
account: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, 
LT, LU, MT, NL, NO, PL, PT, SK, SI, ES, SE, UK, US, IS, LI, AU, CA, CH, JP. 
Duration 
389. The assets where no duration, zero duration or a duration greater than 50  
years had been reported were excluded for the determination of the 
average durations. The average durations were calculated by means of a 
weighted average, using the reduced asset values as weights. 
 
7. Calculation of the corporate portfolio 
Identification of issuers 
390. Two allocations needed to be made to calculate the corporate portfolio: the 
allocation according to the sector of issuer (financial or non -financial) and 
according to credit quality steps. 
Determination of the sector 
391. The sector was determined on the basis of the field “Issuer Sector”. This 
field corresponds to the NACE code: 
http://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=L
ST_NOM_DTL&StrNom=NACE_REV2&StrLanguageCode=EN&IntPcKey=&Str
LayoutCode=HIERARCHIC&CFID=12721637&CFTOKEN=9fa1f017d5f2811e-
C999B956-E7EA-A517-
3AB8BA746C9C60F5&jsessionid=f90060eefcba131dc3c6 
392. Section K is used to identify “Financial and Insurance activities”. The code 
can be  
- 64: financial service activities, except insurance and pension funding 
- 65: insurance, reinsurance and pension funding, except compulsory 
social security

118/131 
 
- 66: activities auxiliary to financial services and insurance activities 
393. All those assets where the issuer sector field starts with a “K” were 
allocated to the financial pa rt of the corporate portfolio.  All other assets 
were allocated to the non -financial part of the corporate portfolio, except 
for those were no information on the sector was reported: those were 
excluded from the calculations. 
 
 
Determination of the credit quality step 
394. The preparatory phase template gives information on the rating agency and 
on the external rating (fields “Rating agency” and “External rating”). Using 
the field “External rating” and the draft implementing technical standards 
on ECAI mappings f or Solvency II 34, assets were allocated a credit quality 
step. 
395. Assets where no external rating had been reported were excluded from the 
allocation to credit quality steps. 
Duration 
396. The assets where no duration, zero duration or a duration greater than 50 
years had been reported were excluded for the determination of the 
average durations. The average durations were calculated by means of a 
weighted average, using the reduced asset values as weights. 
  
                                       
34 See https://eiopa.europa.eu/Publications/Technical%20Standards/JC%202015%20068%20-
%20Final%20Draft%20ITS%20on%20ECAIs%20mapping%20under%20Solvency%20II.PDF.

119/131 
 
14.I. Annex to subsection 10.B.1: History of government 
bond rates for the calculation of the LTAS 
397. The following table specifies  the government bond maturities  that were 
used to derive spreads for the government bond LTAS  in the past since 1 
January 2016. For currencies that do not appear in those tables the 
maturities are unchanged since 1 January 2016. The currently used 
maturities are set out in table 14 of the main text. 
 Government bond maturities 
used 
All maturities in years 
Period 
HRK 1-4, 10 1 January – 30 December 
2016  
 
14.J. Annex to subsections 10.B.1 und 10.C. 3: Adjustment 
factors for the pound sterling LTAS 
398. The ad justment factors applied to LTAS31_12_2015 of UK government bonds  
are as follows: 
Maturity Adjustment factor 
1 103% 
2 95% 
3 94% 
4 94% 
5 95% 
6 103% 
7 99% 
8 104% 
9 105% 
10 to 30 105% 
 
399. The adjustment factors applied to LTAS31_12_2015 of pound sterling corporate 
bonds are as follows: 
 
Maturity  CQS 0, 
CQS 1 CQS 2 CQS 3 
1 to 4 years 82% 88% 97%

120/131 
 
5 to 8 years 80% 84% 93% 
9 to 30 years 95% 93% 93% 
The adjustment factors apply to financial and no n-financial bonds. There 
are no adjustments to corporate bonds of CQS 4 to 6. 
 
14.K. Annex to subsection 10.C.2: Calculation of the cost of 
downgrade (CoD) and probability of default (PD) 
 
 
Legal Context 
400. The two components Cost of Downgrade (CoD) and Probability  of Default 
(PD) are required by Art icle 77c(2)(a) (Calculation of the matching 
adjustment) of the Solvency II Directive, supplemented by Article 51 (Risk-
corrected spread, for volatility adjustment) and 54(4) (Calculation of the 
fundamental spread) of the  Delegated Regulation. Furthermore, recital 31 
of the Omnibus II Directive and the recitals 22 and 23 of the Delegated 
Regulation apply. 
401. The Cost of Downgrade (CoD) is defined as the present value of costs 
resulting from future downgrade, expressed as spreads in base points over 
the risk -free interest rates . According to Art icle 54(4)(a) the cash flow 
pattern does not change, according to point (b) the replacing asset belongs 
to the same asset class as the replaced asset, and according to point (c) 
the replacing asset has the same credit quality step or a better one as the 
replaced asset. 
402. As described below, the same approach applies to the Probability of Default 
(PD) with the appropriate modifications. 
 
 
The three components of a present value 
 
𝑃𝑉=∑CashFlow𝑡⋅Probability(Cashflow)
(1+InterestRate𝑡)𝑡
𝑇
𝑡=1
 
 
Probability 
403. Looking from 𝑡=0 (“today”), the probability for a downgrade event from 𝑋 
to 𝑌 to occur between time 𝑡=𝑡0 and 𝑡=𝑡1 is given as the probability for

121/131 
 
the bond to be in CQS 𝑋 at time 𝑡=𝑡0 and then to end in CQS 𝑌 at time 𝑡=
𝑡1.

122/131 
 
Example: Downgrade from 𝑩 to 𝑪 between 𝒕=𝟏 and 𝒕=𝟐 for a 𝑩 Bond at 
inception 𝒕=𝟎 
 
 
404. The probability for being in CQS 𝐵 at time 𝑡=1 is determined by all the 
paths leading to 𝐵 in 𝑡=1. For the above example, where we only consider 
the initial CQS  𝐵, the path  without replacement  would be 𝐵→𝐵→𝐶. 
However, due to the requirement of Art icle 54(4) of the Delegated 
Regulation to replace bonds that have been downgra ded by a bond of the 
CQS it was in before the downgrade event, we could have also come to 𝐵 at 
time 𝑡=1 via the path 𝐵→𝐶(
𝐴𝑟𝑡.54 (4)
→      𝐵)→𝐵. So, the total probability to 
have a downgrade event between 𝑡=1 and 𝑡=2 is given by (𝑃𝐵𝐵+𝑃𝐵𝐶)⋅𝑃𝐵𝐶. 
 
405. Hence, the replacement requirement of Art icle 54(4) of the Delegated 
Regulation leads to the following ‘change’ in that transition matrix which 
determines the starting credit quality step for the year in which the cost of 
the downgrading event is accounted: 
 
A 
B
B 
C 
d 
𝑝𝐵𝐴 
𝑝𝐵𝐵 
𝑝𝐵𝐶 
𝑝𝐵d 
B
B 
A  
w
it
h 
C 
B 
d 
A 
C 
B 
d 
A 
C 
B 
d 
A 
C 
B 
d 
𝑝𝐴𝐴 
𝑝𝐴𝐵 
𝑝𝐴𝐶 
𝑝𝐴𝑑  
𝑝𝐵𝐴 
𝑝𝐵𝐵 
𝑝𝐵𝐶 
𝑝𝐵𝑑  
𝑝𝐶𝐴 
𝑝𝐶𝐵 
𝑝𝐶𝐶 
𝑝𝐶𝑑  
𝑝𝑑𝐴 
𝑝𝑑𝐵 
𝑝𝑑𝐶  
𝑝𝑑𝑑  
t=0 t=1 t=2 
Art. 54 (4) DA

123/131 
 
𝑇=(
𝑃𝐴𝐴 𝑃𝐴𝐵 𝑃𝐴𝐶 𝑃𝐴𝑑
𝑃𝐵𝐴 𝑃𝐵𝐵 𝑃𝐵𝐶 𝑃𝐵𝑑
𝑃𝐶𝐴 𝑃𝐶𝐵 𝑃𝐶𝐶 𝑃𝐶𝑑
𝑃𝑑𝐴 𝑃𝑑𝐵 𝑃𝑑𝐶 𝑃𝑑𝑑
)
Art.⁡54⁡(4)⁡Delegated⁡Regulation
→                      
(
 
 
𝑃𝐴𝐴+𝑃𝐴𝐵+𝑃𝐴𝐶
Art.⁡54⁡(4)⁡DR
←         
Art.⁡54⁡(4)⁡DR
←         𝑃𝐴𝑑
𝑃𝐵𝐴 𝑃𝐵𝐵+𝑃𝐵𝐶
Art.⁡54⁡(4)⁡DR
←         𝑃𝐵𝑑
𝑃𝐶𝐴 𝑃𝐶𝐵 𝑃𝐶𝐶 𝑃𝐶𝑑
𝑃𝑑𝐴 𝑃𝑑𝐵 𝑃𝑑𝐶 𝑃𝑑𝑑)
 
 =𝑄 
 
406. The original transition matrix  𝑇 is retained for those probabilities regar ding 
the transitions in the year the cost accounting is done. 
407. This means, the probability for a downgrade from 𝐵 at 𝑡=1 to 𝐶 at 𝑡=2 is 
given by the probability of being in credit quality step 𝐵 at 𝑡=1 (regarding 
possible upgrading events due to Art.  54 (4) of the Delegated Regulation 
between 𝑡=0 and 𝑡=1), multiplied by the probability 𝑃𝐵𝐶 of transitioning 
from credit quality step 𝐵 at 𝑡=1 to 𝐶 at 𝑡=2⁡. In matrix notation, this can 
be expressed by the matrix multiplication of 𝑄 for the pos sible paths from 
𝑡=0 to 𝑡=1 with 𝑇 for the possible paths from 𝑡=1 to 𝑡=2. 
408. More general, for a downgrade event to be accounted for in year 𝑚 (i.e. 
between 𝑡=𝑚 and 𝑡=𝑚+1, we consider the matrix Q the first 𝑚 times and 
then once the matrix 𝑇. Thus, the probabilities to be used for a downgrade 
event in year 𝑚 (i.e. between 𝑡=𝑚 and 𝑡=𝑚+1) are all contained in the 
matrix 𝑄𝑚𝑇. 
 
Zero bond cash flow (−𝟏),𝟎,…,𝟎,(𝟏+𝒓𝒕)𝒕 
409. By Art icle 54(4) of the Delegated Regulation , the cash flow in case of 
downgrade is defined as the difference in market values of the original 
(higher) credit quality and the new (lower) credit quality. There is no 
specific requirement for the case of upgrade, the case of staying in the 
same credit quality or for t he case of defaulting. The defaulting case is 
considered in the separate component for PD (probability of default).  
410. The corresponding market values change over time. The cash flows are 
derived from zero bonds with investment (−1) at inception 𝑡=0 and final 
payment (1+𝑟𝑡)𝑡 at maturity. The compound interest rate 𝑟𝑡 is based on the 
financial instrument considered to be risk -free once adjusted . For 
Solvency II purposes, this is considered to be the basic risk -free interest 
rate structure. 
Discount factor 
411. The discount factor 1/(1+InterestRate𝑡)𝑡 considers the risk-free spot rate. 
412. The above considerations give rise to the following nutshell description.

124/131 
 
 
Cost of Downgrade and Probability of Default in a nutshell 
 
Input Data 
Transition Matrix 𝑇=(𝑝𝑋,𝑌)𝑋,𝑌∈𝐶𝑄𝑆 for the 𝑛-element set 𝐶𝑄𝑆 of credit quality steps 
including default state denoted by “𝑑” (note that 𝑝𝑑𝑋=0 and 𝑝𝑑𝑑=1 because 𝑑 is 
considered an absorbing state)  and relevant portions 𝑅𝑐 for credit quality 
steps 𝑐∈𝐶𝑄𝑆. Any explicit reference to economic sectors or other granularity 
buckets is dropped, because Art icle 54(4) of the Delegated Regulation does not 
require costs of transitions between economic sectors or other granularity 
buckets to be considered. However, the following calculation needs to be done 
within each of those buckets not explicitly mentioned here. 
 
Cost of Downgrade, step 1 
Based on the basic risk-free interest rate term structure(𝑟𝑀)𝑀=1…30, the market value of a zero bond 
of maturity 𝑀 at time 𝑚 is given by 
𝑀𝑉𝑀(𝑚)= (1+𝑟𝑀)𝑀
(1+𝑓𝑚,𝑀)
𝑀−𝑚, 
where the forward rates 𝑓𝑚,𝑀 are derived on an arbitrage-free basis: 
(1+𝑟𝑚)𝑚(1+𝑓𝑚,𝑀)𝑀−𝑚=(1+𝑟𝑀)𝑀.This provides the following closed formula for the market 
value of the risk-free reference instrument: 
𝑀𝑉𝑀(𝑚)=(1+𝑟𝑚)𝑚⁡. 
The market value of the risky instruments in CQS c is defined based on a fixed portion 𝑅𝑐⁡as a 
portion of the risk-free instrument and given by 
𝑀𝑉𝑐,𝑀(𝑚)=𝑅𝑐
𝑀−𝑚
15 ⋅(1+𝑟𝑚)𝑚. 
The portion is a certain percentage 𝑅𝑐𝑀 of the market value of the risk-free reference instrument at 
inception and increases to 100% at maturity.  The factors ar e applied having in mind 15 years 
maturity as an approximation of the highest duration observed. 
A downgrade at time 𝑚 from credit quality step 𝑋 to 𝑌>𝑋 results in the following cost: 
𝐶𝑜𝐷(𝑋,𝑌),𝑀(𝑚)≔𝑀𝑉𝑋,𝑀(𝑚)−𝑀𝑉𝑌,𝑀(𝑚)>0. 
Define the following strictly upper triangular matrix (an upgrade or stay is not accounted for): 
𝐶𝑀
(𝑚)≔({ 𝐶𝑜𝐷(𝑋,𝑌),𝑀(𝑚)⋅𝑝𝑋,𝑌⁡⁡for⁡𝑌≠default
(1−RecoveryRate)⋅𝑀𝑉𝑋,𝑀(𝑚)⋅𝑝𝑋,𝑌⁡⁡for⁡𝑌=default})
(𝑋<𝑌)∈𝐶𝑄𝑆
.

125/131 
 
Define the matrix 𝑄 according to the replacement requirement of Article 54(4) of the Delegated 
Regulation 
(𝑞𝑋𝑌)𝑋,𝑌∈𝐶𝑄𝑆≔
{  
  𝑝𝑋𝑌 for⁡𝑋>𝑌⁡and⁡𝑌=n⁡(lower⁡triangle⁡and⁡rightmost⁡column)
∑𝑝𝑖,𝑘
n−1
𝑘=𝑖
for⁡𝑋=𝑌≤𝑛⁡(Art.⁡54⁡(4)⁡DR)⁡(main⁡diagonal)
0 for⁡𝑋<𝑌<𝑛⁡(upper⁡triangle⁡except⁡rightmost⁡column) }  
  
. 
The following matrix contains the expected cash flows representing the expected cost of downgrade 
for bonds in the credit quality step in 𝐶𝑄𝑆 of original maturity 𝑀 at times 𝑚=1,…,𝑀. 
(
 
 
𝐶𝑜𝐷best⁡quality,𝑀(1) ⋯ 𝐶𝑜𝐷best⁡quality,𝑀(𝑀)
⋮ ⋱ ⋮
𝐶𝑜𝐷lowest⁡quality,𝑀(1) ⋯ 𝐶𝑜𝐷lowest⁡quality,𝑀(𝑀)
𝐶𝑜𝐷default,𝑀(1)=0 ⋯ 𝐶𝑜𝐷default,𝑀(1)=0 )
 
 ≔ ⋃
(
 𝑄𝑚−1𝐶𝑀
(𝑚)(
1
⋮
1
0
)
)
 
⏟            
colum⁡vector
𝑀
𝑚=1
, 
where ⋃ (⋮)𝑀
𝑚=1  shall denote the concatenation (to the right) of column vectors into a matrix. In base 
points, 𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝) is solved from the following equation. Note 𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝)=0 if 𝐶𝑜𝐷𝑐,𝑀(𝑚)=0 for 
all 𝑐,𝑚. 
1
(1+𝑟𝑀+𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝))
𝑀= 1
(1+𝑟𝑀)𝑀(1−∑ 𝐶𝑜𝐷𝑐,𝑀(𝑚)
(1+𝑟𝑚)𝑚−0.5
𝑀
𝑚=1
). 
 
Probability of Default in a nutshell 
The computation of the probability of default in base points as spread over the basic risk-free rate is 
done completely consistently with the above approach. There is no Article 54(4) requirement to 
replace downgraded bonds along the way. Hence, the only difference is to use the original transition 
matrix 𝑇 instead of the “twisted Article 54(4) matrix” 𝑄 and to use the column vector (
0
⋮
0
1
) instead 
of (
1
⋮
1
0
). Rename 𝐶𝑜𝐷 to 𝑃𝐷 in this case. The other special case corresponds to the RecoveryRate 
term, which is given by Article 54(2) of the Delegated Regulation as 30% of the market value of the 
bond. 
For the risk-correction of cash flows to be considered in the matching adjustment, the probability of 
default is the total probability for a zero bond’s final payment at maturity not to occur . This 
probability is independent of market values and just given by the r ightmost column of the matrix 
powers 𝑇𝑚.

126/131 
 
Cost of Downgrade, step 2 
Using the same notation as before, we have now calculated:  
 𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝) 
 𝑃𝐷𝑐,𝑀
(𝑏𝑝)(𝑇) using the original transition matrix ⁡𝑇. 
We need to calculate 𝑃𝐷𝑐,𝑀
(𝑏𝑝)(𝑄): for that purpose, we proceed as before, while using the  “twisted 
Article 54(4) matrix” 𝑄 instead of the original transition matrix 𝑇. 
The final cost of downgrade becomes: 
𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝)=⁡𝑚𝑎𝑥[0⁡,𝐶𝑜𝐷𝑐,𝑀
(𝑏𝑝)−(𝑃𝐷𝑐,𝑀
(𝑏𝑝)(𝑇)−𝑃𝐷𝑐,𝑀
(𝑏𝑝)(𝑄))] 
 
Reducing computational and numerical complexity 
413. Please note that 𝐶𝑀
(𝑚) is strictly upper triangular. This might help to further 
reduce complexity if needed. One can setup an internal table of all the 
values (1+𝑟𝑚)⁡𝑚 and 𝑅𝑐𝑚 for 𝑚=1,…,𝑀. The market values are then just 
given by the product of two entries of this fixed-value table. 
414. Furthermore, the matrix powers 𝑄𝑚 and 𝑇𝑚 can be saved in an internal 
(three-dimensional) array. 
415. The matrix 𝑄 excluding the last row and column  is lower triangular with 
non-zero values on the main diagonal (unless “stay or upgrade” would both 
be impossible for any CQS). That is, the diagonal consists of the 
Eigenvalues 𝜆𝑐 of the matrix  𝑄 which is immediate from the characteristic 
polynomial decomposing into linear terms of the form  (𝜆−𝜆𝑐). Write 
𝑄=𝑆−1∗diag(𝜆𝑐)𝑐∈𝐶𝑄𝑆∗𝑆, then  𝑄𝑚=𝑆−1diag(𝜆𝑐𝑚,)𝑐∈𝐶𝑄𝑆𝑆, where the columns 
of 𝑆 are the corresponding left-Eigenvectors. 
 
A remark about probability in con tinuous time and why it has not been 
used here 
416. In this notation, one could – in theory – also define matrix powers for non-
integral times 𝑡 by 
𝑄𝑡≔𝑆−1diag(𝜆𝑐𝑡)𝑆. 
417. However, the use of the continuous version of  powers of 𝑄 should carefully 
consider whether continuous downgrade events with immediate upgrade 
make sense in the specific application context. Even if one would consider 
integrals instead of sums, downgrades would still be discrete jumps 
between a finite number of rating classes or c redit quality steps. This could 
be different if spreads were considered to continuously change without 
regard to a rather limited number of rating categories or credit quality

127/131 
 
steps. The choice taken in this approach stays away from this complexity in 
order to create consistency with the mechanics behind the creation of 
transition matrices. 
 
A remark about intra-year chains of rating changes 
418. In real life, if a financial instrument receives a downgrade with negative 
forecast, it is not unlikely that the same  instrument receives a second 
downgrade within the same year. The approach taken here would not “see” 
this chain of rating changes, because it only looks at discrete points 𝑡=0, 
𝑡=1, …,𝑡=𝑀. 
419. However, this would only be influential on the result if there is an upgrade 
event followed by a downgrade event in that chain of rating changes, 
because this downgrade event would have to be accounted for. But it is not 
accounted for, because it would not be recognized if one only opens the 
“black box” at the next point in time. Since these events are quite unlikely 
to occur, we disregard the difference stemming from this simplified view. 
420. If the chain consists of only downgrading event s, there is almost no 
difference at all, because the CoD cashflows are defined as differences 
between market values: 
𝐶𝑜𝐷𝑋→𝑌+𝐶𝑜𝐷𝑌→𝑍=(𝑀𝑉𝑋−𝑀𝑉𝑌)+(𝑀𝑉𝑌−𝑀𝑉𝑍)=𝑀𝑉𝑋−𝑀𝑉𝑍=𝐶𝑜𝐷𝑋→𝑍. 
421. The only difference would stem from the different points in time and 
therefore the different interest/forward rates concerned. But again, this 
simplification has been considered to be of negligible materiality. However, 
in theory, this can be recognized within this model.

128/131 
 
Transition matrix implementing the rebalancing requirement after a 
downgrade event 
 
Define the lower triangular matrix 𝑄 according to the replacement requirement of Art. 54 (4) of 
Delegated Regulation 
(𝑞𝑋𝑌)𝑋,𝑌∈𝐶𝑄𝑆&≔
{  
  𝑝𝑋𝑌 for⁡𝑋>𝑌⁡and⁡𝑌=n⁡(lower⁡triangle⁡and⁡rightmost⁡column)
∑𝑝𝑖,𝑘
n−1
𝑘=𝑖
for⁡𝑋=𝑌≤𝑛⁡(Art. 54 (4) DA) (main diagonal)
0 for 𝑋<𝑌<𝑛⁡(upper triangle except rightmost column) }  
  
=
(
 
 
 
 
 
 
 
 
 
 ∑𝑝1,𝑘
n−1
𝑘=1
←0 ⋯ ←0 𝑝1𝑑
𝑝21 ∑𝑝2,𝑘
n−1
𝑘=2
←0 ⋮ 𝑝2𝑑
𝑝31 𝑝32 ∑𝑝3,𝑘
n−1
𝑘=3
←0 𝑝3𝑑
⋮ ⋮ ⋱ ⋱ ⋮
𝑝𝑛−1,1 ⋯ 𝑝𝑛−2,𝑛−1 𝑝𝑛−1,𝑛−1 𝑝𝑛−1,𝑑
𝑝𝑑1=0 𝑝𝑑2=0 ⋯ 𝑝𝑑,𝑛−1=0 𝑝𝑑𝑑=1)
 
 
 
 
 
 
 
 
 
 
.

129/131 
 
14.L. Annex to subsection 10.C.4: Background on the 
treatment of Danish covered bonds 
 
422. Nykredits Realkreditindeks includes a representative extract of the Danish 
covered bond market. The index includes both cov ered bonds with short 
and long maturities.  
423. A single index which covers all maturities is preferred over a more granular 
approach e.g. mapping exposures to two indices with maturity 3 years and 
30 years. Such a mapping will include major expert judgement o n the split 
of insurance undertakings holdings of short and long duration covered 
bonds.  
424. The use of a single index reflects better the exposures of the Danish 
insurance sector as a whole than an attempt to map exposures in to two 
buckets. It should also b e noted that the Nykredit s Realkreditindeks is the 
index used as input for the covered bond component in the current Danish 
interest rate curve. 
425. Historical data for the yield of Nykredits Realkreditindeks is given in the 
figure below. This data corresponds to the input 
DKK
coveredR  
426. The average yield to maturity of this covered bond index for the time period 
1 September 2003 to 31 December 2014 is 3.86 % 
 
  
0.000
1.000
2.000
3.000
4.000
5.000
6.000
7.000%-YTM for DKK covered bonds

130/131 
 
14.M. Annex to subsection 10.C.2: Specification of the input 
data for the transition matrices 
This annex sets out the input data of Standard & Poor’s for the transition 
matrices used to calculate the probabilities of default and the cost of 
downgrading. The specific time period of the data used and the timing of the 
data download are specified in the monthly publication of the probabilities of 
default and the cost of downgrading.  
 
Financial bonds 
Report Type Transition Matrices  (Percent, NR Excluded) 
Calculation Base Number of Issuers (All) 
Horizon 1Year 
Industry Selection GICS -40 -- Financials 
Country Selection All 
Vintage Years Selection All 
Number of Pools 30 
 
Non-financial bonds 
Report Type Transition Matrices  (Percent, NR Excluded) 
Calculation Base Number of Issuers (All) 
Horizon 1Year 
Industry Selection 
GICS -10 -- Energy, 15 -- Materials, 20 -- 
Industrials, 25 -- Consumer Discretionary, 30 -- 
Consumer Staples, 35 -- Health Care, 45 -- 
Information Technology, 50 -- Telecommunication 
Services, 55 – Utilities,  60 -- Real Estate  
Country Selection All 
Vintage Years Selection All 
Number of Pools 30

131/131 
 
14.N. Diagram of calculations 
 
 
 
 
 
 
 
 
 
 
Govt / Swap / OIS 
rates 
Credit Risk Adjustment  
(with swap and OIS rates) 
Basic risk-free interest rate term 
structure 
Basic risk-free interest rate for the 
liquid maturities 
DLT assessment 
Extrapolation 
History of govt rates 
 History of corps rates 
 History of basic  
risk-free interest rates 
Long Term Average Spread 
Transition matrix 
PD and CoD 
 Fundamental spread 
Reference portfolio 
 Volatility 
Adjustment