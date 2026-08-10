---
title: "the devil in the detail assessing state contingent tail effects"
regulator: "boe_pra"
doc_type: "announcement"
status: "final"
source_kind: "policy_pdf"
source_url: "https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2026/the-devil-in-the-detail-assessing-state-contingent-tail-effects.pdf"
published: "2026-07-24"
version: "1"
---

Staff Working Paper No. 1,198
July 2026
The devil in the DeTail: assessing  
state-contingent tail effects of a releasable 
macroprudential capital buffer using a 
parsimonious agent-based framework
Staff Working Papers describe research in progress by the author(s) and are published to elicit comments 
and to further debate. Any views expressed are solely those of the author(s) and so cannot be taken to 
represent those of the Bank of England or any of its committees, or to state Bank of England policy. 
Enrico Minnella, Ana Pereira and Eugen Tereanu

Staff Working Paper No. 1,198
The devil in the DeTail: assessing state-contingent tail effects 
of a releasable macroprudential capital buffer using a 
parsimonious agent-based framework
Enrico Minnella,(1) Ana Pereira(2) and Eugen Tereanu(3)
Abstract
This paper develops an agent-based framework (DeTail) to assess the state-contingent tail 
effects of releasable macroprudential capital buffers. The model features heterogeneous 
firms, households, and banks, and a single central bank, all interacting in a fully integrated, 
stock-flow consistent framework which generates endogenous credit cycles. Using this 
approach, we evaluate how time-varying capital requirements affect the time-varying 
distributions of credit growth, firm and household default rates, and bank losses along 
the credit cycle. Policy experiments show that releasing capital buffers during economic 
downturns preserves credit supply by improving risky (lower-tail) credit outcomes, reduces 
both households and firms defaults, and supports macro-financial resilience by limiting tail 
bank losses. At the same time, capital buffer accumulation during upturns imposes minimal 
costs and does not significantly constrain lending. These findings support the active use of 
releasable buffers to mitigate systemic risk and smooth credit cycles without weakening the 
banking system.
Key words: Agent-based modelling, macroprudential policy, macro-financial linkages,  
credit cycles, bank resilience, tail risk, state-dependent effects.
JEL classification: C63, E44, E58, G28.
(1) Bank of England. Email: enrico.minnella@bankofengland.co.uk
(2) Bank of England. Email: ana.pereira@bankofengland.co.uk
(3) European Central Bank and Joint Vienna Institute. Email: etereanu@jvi.org
The authors gratefully acknowledge comments from participants at the European Central Bank (ECB), 
Bank of England and Magyar Nemzeti Bank financial stability seminars, the 28th Annual Workshop on 
Economics with Heterogeneous Interacting Agents (WEHIA), the ECB workshop of agent-based models for 
policy 2025, the 30th International Conference on Macroeconomic Analysis and International Finance (ICMAIF) 
2026, and the 24th Conference of the European Economics and Finance Society (EEFS). The views expressed 
are those of the authors and do not necessarily represent the views of the ECB, the Bank of England or the 
Joint Vienna Institute.

The Bank’s working paper series can be found at www.bankofengland.co.uk/working-paper/staff-working-papers 
Bank of England, Threadneedle Street, London, EC2R 8AH  
Email: enquiries@bankofengland.co.uk
©2026 Bank of England  
ISSN 1749-9135 (on-line)

1 Introduction
The importance of releasable macroprudential capital buffers in enhancing bank resilience and sup-
porting credit provision during periods of stress was re-emphasised by the COVID-19 pandemic. While
post-Global Financial Crisis reforms strengthened banking system resilience, the pandemic highlighted
challenges of operating macroprudential capital buffers in a countercyclical manner. Although macro-
prudential buffers are designed to be drawn down in adverse conditions to avoid bank deleveraging and
stabilise credit supply, empirical evidence showed that they were often underutilised by banks during
downturns (see Couaillier et al., 2025; Mathur et al., 2023, among others). Banks’ reluctance to draw
down capital buffers during downturns is partly driven by concerns about stigma and the risk of ad-
verse market reactions when capital ratios approach regulatory minima. 1 Additionally, the pandemic
experience also showed the desirability of sufficient macroprudential space to moderate adverse shocks
which can also occur irrespective of the phases of the financial cycle (Detken et al., 2025).
Consequently, much of the recent policy debate in Europe and the UK has focused on promoting
the use of capital buffers. One direction is the active and systemic use of releasable buffers, including
their use in response to a broader range of shocks. 2 Releasable macroprudential buffers, such as the
Countercyclical Capital Buffer (CCyB), are designed to vary over the credit cycle. Their pro-active build-
up and release can help to mitigate banks’ concerns about drawing down capital to maintain lending
during downturns. Consistent with this view, several countries, including EU member states as well
as the UK, released the CCyB during the COVID-19 pandemic and other stress episodes to encourage
buffer use and sustain lending. Although the conceptual rationale for such time-varying buffers is
well established, evidence on their state-contingent effects, in particular regarding tail risks, remains
limited. This paper contributes to this debate by analysing how releasable buffers impact the tails of
distributions of key macro-financial and banking system outcomes along the cycle. We examine both
tail benefits of releasing the buffers during downturns, as well as the potential costs of their build-up
during upturns.
1Banks may be reluctant to draw down capital buffers during periods of stress due to concerns about market stigma.
Using buffers may be interpreted by the market as a signal that a bank is under financial pressure or is weaker than its
peers. This perception can lead to higher funding costs, reduced market access, or even credit rating downgrades (see Basel
Committee on Banking Supervision, 2022; European Central Bank, 2022). As a result, banks may prefer to maintain buffers
during periods of stress, even when the regulatory framework allows their use to absorb losses and support lending during
downturns (for a separate discussion of challenges related to using bank capital to meet parallel regulatory requirements, see
European Central Bank - European Systemic Risk Board, 2026).
2The capital buffer framework includes multiple buffers, which can be grouped into two categories: releasable and non-
releasable. Releasable buffers are those that macroprudential authorities can reduce or release when risks materialise to pre-
vent credit supply constraints during downturns. These buffers vary over the financial cycle and include the Countercyclical
Capital Buffer (CCyB) and, in some cases, certain forms of the Sectoral Systemic Risk Buffer (sSyRB).
1

For our analysis, we develop DeTail, a parsimonious, credit-driven agent-based model (ABM) which
can generate complete distributions of our policy variables of interest (and in particular their tails). 3
The model builds on the framework in Gross (2022), where endogenous cycles arise from a combi-
nation of interest-bearing debt and downward nominal wage rigidity. To allow for the evaluation of
macroprudential policies, we extend this framework by introducing a housing market with mortgage-
financed homeownership, multiple heterogeneous banks subject to risk-based capital requirements,
and a central bank that settles interbank reserve transfers and sets macroprudential policy. Together,
these extensions allow the model to capture richer credit dynamics and the channels through which
capital-based macroprudential policy affects firms, households, and banks simultaneously.
All agents’ balance sheets are fully integrated and consistent as the cross-agent flows of funds result
in corresponding changes in assets and liabilities across sectors (firms, households, banks, and central
bank). The four types of agents engage in production/consumption, employment, borrowing/lending
and dividend payment relations. Firms and households can default on their debt, leading to firm clo-
sures, job losses and collateral repossession, which in turn have macroeconomic implications. Since our
economy is credit-driven, we assume that banks falling below their capital requirements are resolved
in an orderly manner, i.e. without macroeconomic feedback effects. 4
The DeTail framework contributes to the growing family of macro-financial agent-based mod-
els used to study financial stability and regulatory policies. Building on Gross (2022), it adds fea-
tures aligned with recent macro-ABM applications analysing capital and borrower-based policies, such
as Bardoscia et al. (2025), while maintaining a parsimonious structure suited for tail-focused, state-
contingent policy analysis. The model also complements general-equilibrium approaches, such as the
DSGE framework with three layers of default (3D) of Clerc et al. (2015), by assessing capital-based tools
beyond average effects and without relying on linearisation. Finally, it connects to the recent litera-
ture emphasising non-linear and state-dependent effects of capital requirements (e.g. Lang and Menno,
2025), providing a macro-financial environment that captures heterogeneity, non-linear interactions,
and the full distribution of outcomes.
Using DeTail, we compare the macroprudential policy effects from a model with time-varying cap-
ital requirements (TVP) with simulations from a model with only time-invariant capital requirements
(TIP). We focus on relative changes in the time-varying distributions of credit growth, default rates
3See Borsos et al. (2025) for a recent review of the application of ABM models in central bank policy analysis.
4This assumption is consistent with modern bank resolution frameworks, which aim to manage bank failures without
destabilising the economy or burdening taxpayers. In line with these objectives, other ABM applications make a similar
simplification (e.g. Bardoscia et al., 2025, assumes bank resolution is orderly and imposes no costs on the public).
2

by borrower segments, and bank losses, evaluated separately over economic upturns and downturns.
Specifically, we analyse policy-induced changes in the relevant (high risk) tail of these distributions, as
well as changes in their volatility (the interquartile range) and shifts in the probability of extreme tail
events.5 As part of the policy benefit analysis, we additionally track the frequency and size of central
bank interventions required to resolve ex-post undercapitalised banks. Finally, taking advantage of the
endogenous cycles in our model, we also evaluate the impact of a releasable buffer on the amplitude
and duration of the cyclical credit expansions and contractions using the approach in Drehmann et al.
(2012).
Our key results confirm the importance of having sufficient releasable buffers in place. Firstly, we
find that a releasable buffer can provide meaningful resilience benefits during downturns, by helping to
reduce the occurrence of negative credit growth events and preserve credit supply when the economy
is under stress. The release of the buffer in a downturn improves the lower (riskier) tail of real credit
growth, reduces its volatility, and attenuates severe default events, especially for households, relative to
a time-invariant capital regime. These improvements translate into reducing upper-tail (higher) bank
losses as well as fewer systemic-level recapitalisation needs. Secondly, the macro-financial costs of
building buffers during upturns are limited. Increasing the buffer does not materially tighten credit
supply or raises default rates, reflecting the gradual implementation of higher requirements, which
helps smooth adjustment costs. At the same time, the resulting slightly tighter credit supply conditions
help to restrain credit to more highly leveraged firms, thereby improving credit quality and reducing
default risks. Thirdly, the releasable buffer helps to shorten contractions and, to a lesser extent, limit
the credit boom, resulting in a lower median cycle duration. The cycle amplitude also decreases, albeit
modestly, in the presence of a releasable buffer. The remainder of the paper is organised as follows.
Section 2 reviews the related literature. Section 3 introduces the DeTail model used in the policy experi-
ments. Section 4 presents the model’s economic and empirical validation exercise supporting its use for
policy evaluation. Section 5 discusses the policy evaluation strategy and results. Section 6 concludes.
5Policy-relevant tails are defined as the bottom and top quartiles of the distribution (the 25th or 75th percentile), de-
pending on whether lower or higher values correspond to worse outcomes (costs) or better outcomes (benefits). Extreme tail
events refer to percentiles lying beyond the policy-relevant tails, that is below the 25th percentile or above the 75th percentile.
3

2 Related literature
ABMs have gained traction in macroeconomic and macro-financial policy analysis because of their
flexibility to address policy design and evaluation questions where “heterogeneity, complexity, non-
linearity, emergence, heuristics and detailed rules” matter (Haldane and Turrell, 2018). A comprehen-
sive survey of 60 years of ABM usage in economics and finance notes their significant complementarity
to conventional economic modelling, particularly due to increased need to model heterogeneous agents
with possibly differentiated (boundedly rational) behaviour whose non-linear interactions generate the
aggregate (not necessarily equilibrium) outcomes (Axtell and Farmer, 2025). Within the general class of
ABMs, macro-ABMs have been developed to study the economy as a complex, emerging system where
both the aggregate but also granular effect of macroeconomic and macro-financial stabilisation policies
can be evaluated (Axtell and Farmer, 2025; Dosi and Roventini, 2025). Recent developments also in-
clude macro-ABMs which generate micro-founded macro behaviour while also delivering a short-term
forecast performance comparable to V ARs and DSGE models (Poledna et al., 2023).
Reflecting this progress, ABMs have been increasingly used to analyse policies relevant to central
bank mandates. A targeted survey of ABM modelling at central banks (Borsos et al., 2025) documents
a wide range of applications ranging from systemic risk assessment and financial stability policies to
monetary policy, payment systems and Central Bank Digital Currencies (CBDCs) and the analysis of
climate risks. Following the global financial crisis, ABMs have been used to look into various regula-
tory policies (Krug and Wohltmann, 2016; Popoyan et al., 2020; Catullo et al., 2021), in particular the
relevance of capital requirements to support the resilience of the banking system (Raberto et al., 2017;
Van der Hoog and Dawid, 2019; Alexandre and Lima, 2020; Riccetti et al., 2022). Housing markets and
related financial stability policies such as borrower-based measures have been included in a growing
number of applications. Early contributions include the seminal works of Geanakoplos et al. (2012)
and Axtell et al. (2014), while more recent policy-oriented analysis are provided by Cokayne (2019),
Laliotis et al. (2020), Tarne et al. (2022), Mérő et al. (2023), Carro (2023), and Catapano (2023). More re-
cently, Bardoscia et al. (2025) combine the granular housing market of Carro et al. (2022) with a complex
macro-ABM of Popoyan et al. (2017), which features, inter alia, a labour market, multiple banks, a cen-
tral bank, and a government, to explore the interaction of capital and borrower-based macroprudential
policies in the UK.
Against this background, our DeTail agent-based framework lies within the family of macro-financial
ABMs and is closely related to the growing strand of applications analysing financial stability and reg-
4

ulatory policies. From a macroeconomic perspective, it builds on the stock-flow consistent macro-ABM
approach of Gross (2022), who proposes a parsimonious model in which endogenous economic cycles
emerge from interest-bearing debt and downward nominal wage rigidity. Two of the stylised facts gen-
erated in the model are particularly relevant for macroprudential policy analysis: a) procyclical leverage
and b) default cascades arising at the peak of the cycle.
We expand this modelling framework along three important dimensions. First, we introduce a
housing market and mortgage borrowers, thereby incorporating the two core borrowing sectors of
the economy. Second, we allow for multiple banks that supply credit to both firms and households
and that are subject to risk-based capital requirements set by a central bank. Third, we add a central
bank to manage interbank reserve transfers and set macroprudential policies, which are not present
in the original framework. Importantly, firms and households can default on their loan obligations,
with defaults affecting banks’ capital ratios. When banks become undercapitalised, they are resolved
without economic consequences.
Combining endogenous cycles with heterogeneous borrowers and multiple banks provides a unique
framework for analysing capital-based policies. Specifically, we can assess the state-contingent impact
of releasable capital buffers on specific tails of the distribution of variables of interest such as credit
growth and agent defaults. The cyclical nature of the DeTail framework further allows an evaluation
of the effects of the policy on the amplitude and duration of economic expansions and contractions.
Finally, even though bank defaults do not generate direct macroeconomic losses in the model, we can
still explore some indirect effects through the simulated cost of bailouts and the proportion of bank
assets under default.
In this sense, our model closely relates to Bardoscia et al. (2025), as both frameworks analyse the in-
teraction between housing markets, banks, and macroprudential capital-based policies within a macro-
ABM setting. However, our approach is considerably more parsimonious and, through its endogenously
generated cycles is specifically well-suited for a state-contingent and tail-focused assessment of macro-
prudential capital policy rules which is, to the best of our knowledge, novel in the literature. The smaller
parameter space may prove valuable in future attempts to calibrate our framework for a comparable
assessment across countries.
The DeTail model also relates to and complements existing general-equilibrium and banking sector
models used in macroprudential policy analysis. General equilibrium models based on the DSGE model
with three layers of default by Clerc et al. (2015) have been widely used to evaluate the risk-based se-
lection of various macroprudential instruments (Azzone and Pirovano, 2024) as well as compute the
5

risk-based calibration of a positive neutral countercyclical capital buffer (Herrera et al., 2025). This
micro-founded DSGE model with financial frictions includes representative borrowing firms and house-
holds and two types of representative banks, specialising respectively in firm and household lending.
The model is solved through standard linearisation around a steady state (equilibrium). Firms, house-
holds and banks maximise utility, profits and the NPV of equity. Importantly, borrowers can default
on their loans which may lead to bank default when the loan return, subject to an idiosyncratic shock,
falls below the cost of deposits. The higher the bank risks and leverage (the lower the capitalisation),
the higher the probability that banks default. The DeTail framework complements this model by al-
lowing an assessment of macroprudential capital policies not only in expectation, but also in terms of
their state-contingent and tail-focused effects, which are features difficult to capture in representative-
agent or linearised DSGE settings. Moreover, by modelling each sector as a time-varying distribution
of (interacting) firms, households and banks, each with pre-specified behavioural rules, it offers an
alternative to the fully optimising representative agent paradigm.
Recently, Lang and Menno (2025) use a non-linear structural banking sector model to show that
the effects of changes in capital requirements on bank lending are strongly state dependent. Their
work discusses both the “pricing” channel (lending rate) and the “quantity” channel (loan supply) and
relates the strength of these channels to banks’ capital positions and profitability. Importantly, they
highlight the need for a non-linear modelling approach to determine a state-differentiated effect of
macroprudential policies. The DeTail model complements this analysis by providing a macro-financial
agent-based perspective that embeds similar concerns about non-linearity and state-contingent effects
while allowing for a granular and tail-focused assessment of policy impacts.
Finally, our model contributes to a growing strand of work that assesses the distributional effects of
macroprudential policies by explicitly modelling agent heterogeneity. This has become an increasing
focus for several central banks. For example, Bush et al. (2025) highlight the importance of incorpo-
rating heterogeneity into analytical frameworks as a key step towards improving the evaluation of
macroprudential policies.
3 DeTail model
This section introduces the DeTail model - an agent-based macro-financial framework used to assess
the tail effects of releasable capital buffers over the credit cycle. It is organised as follows: subsection
3.1 provides a high-level description of the model and sets out the sequence of interactions between
6

agents; subsections 3.2, 3.3 and 3.4 discuss the behaviour of firms, households and banks, respectively;
and subsection 3.5 discusses the role of the central bank within the model and the capital requirements
framework.
3.1 Model overview
The DeTail model is a parsimonious stock-flow consistent agent-based model. It relies on four types
of agents - heterogeneous firms, households, banks and a single central bank – that interact in three
economic sectors, as illustrated in Figure 1. 6 Agents engage in production/consumption, employment,
borrowing/lending and dividend payment relations. The macroeconomy emerging from the agents’
interaction is primarily credit-driven. The balance sheets are fully integrated and consistent across
agents, as the cross-sector flows of funds result in corresponding changes in agent balance sheets. As
discussed in section 2, we extend the Gross (2022) model in three key dimensions, highlighted in red
in Figure 1. Firms and households can default, but in our current specification, any bank that breaches
its capital requirements is recapitalised by the central bank, so that bank failures do not result in credit
supply contractions on the wider economy. 7 This simplification reflects an assumption of an orderly
resolution and allows us to focus on the state-contingent costs and benefits of a releasable capital buffer
rather than modelling systemic contagion from bank failures.
At the start of each period, firms compute their labour costs (wage bill) based on firm-specific wages
set for that period. They then assess their financing needs, and when necessary, apply for loans to meet
wage payments. Simultaneously, a subset of households participates in the housing market auction to
gain home ownership while the remaining households are assumed to reside in social housing. Suc-
cessful household bidders apply for mortgage loans to finance their purchases. The simulated economy
emerges from six iterative steps each period, driven by agents’ interactions. Figure 2 summarises the
sequence of these events. Banks extend credit only if their capital ratio exceeds capital requirements,
not exceeding capital requirements might result in credit rationing. Firms that are denied credit become
inactive and cease production for some time, rendering their assigned workers unemployed.
6Heterogeneity across agents is multidimensional in our model. For example, firms are heterogeneous in terms of balance
sheet size but also behaviour (e.g. active vs inactive (defaulted) firms).
7In its current specification, DeTail can be considered as a 2D+ type of model rather than a 3D model as in Clerc et al.
(2015). Firms and household loan default result in losses to banks that can affect their capital ratios. Given that our economy
is fundamentally credit driven, capital ratios below capital requirements are compensated by central bank capital injection to
support credit supply, akin to orderly bank resolution. Various forms of orderly bank resolutions are common in the macro-
ABM literature (e.g. Popoyan et al., 2017; Bardoscia et al., 2025) and modelling the macroeconomic feedback from bank default
is left for future research.
7

Figure 1: DeTail model
3. Consume
2. Pay wages
Households sector
Borrow
, provide 
labour
, 
consume, 
buy/sell houses
, own 
banks
Firms sector
Borrow, produce a 
consumption good
Multiple banks
Receive deposits
Provide credit 
subject to 
capital requirements
Sets lending rates
Housing market
Central Bank
Reserves holding/borrowing
Sets prudential policies
Bails out banks
Note: The figure illustrates the structure of the DeTail model, which is built on the framework developed in Gross (2022).
Elements highlighted in red indicate the extensions introduced in the DeTail model.
Households unable to secure mortgage loans remain in social housing and may re-enter the auction
in later periods. Because the model is credit-driven, each bank is required to satisfy a minimum share
of the loan demand it receives, defined as a fixed percentage of the wage bill of its client firms. When
a bank’s capital ratio is insufficient to satisfy this minimum while remaining compliant with capital
requirements, the central bank injects capital into the bank to restore its lending capacity.
Figure 2: Sequence of events in each period
Wage 
setting
Loan granting, 
housing auction, 
and capital 
injections
Wage 
payment
Production, 
sales, 
consumption
Dividend   
payment
Debt 
servicing or
default
STEP 1 STEP 2 STEP 3 STEP 4 STEP 5 STEP 6
One simulation period
Note: The sequence of events largely follows the structure of the original model with differences in step 2, which incorporates
the housing market and capital injections, and in step 6, which includes mortgage debt servicing and household default.
Next, active firms pay wages to their employees and produce the consumption good. Households
then allocate a fraction of their available resources to consumption, selecting a supplying firm at ran-
dom. This assumption introduces idiosyncratic demand shocks at the firm level, which are the sole
source of endogenous cycle fluctuations in the model. Prices are firm-specific and determined by de-
mand, under the assumption that all output is sold within the period, with no inventory carried over.
Subsequently, each bank that did not receive a capital injection distributes dividends, provided its cap-
ital ratio exceeds the target threshold for dividend payments. These dividends are allocated equally
across households, thereby increasing their disposable income for consumption in the subsequent pe-
8

riod. After production and consumption, firms and households service their debt obligations. Indebted
firms, including inactive ones, use their available resources to repay outstanding loans. Firms either: (i)
repay the debt in full when resources exceed the debt amount; (ii) roll over the outstanding debt to the
next period when resources are sufficient to cover only interest payments; or (iii) default when they
cannot cover at least interest payments. In the case of default, the firm is shut down for two periods,
and the bank seizes its deposits to mitigate losses. Indebted households face similar decisions when
making mortgage payments. They either make the full annuity payment, pay only interest and roll
over the outstanding principal, or default, in which case the bank repossesses the house pledged as
collateral. Unlike defaulting firms which cannot access the credit market for two periods, defaulting
households may re-enter the mortgage market already from the next period. Tables 1 and 2 display the
balance sheets for the four agent types and the corresponding flow of funds between agents in each
period, respectively. This integrated view highlights how every outflow from one sector corresponds
to an inflow to another, ensuring consistency in balance sheet updates across agents.
Table 1: Agents’ integrated balance sheets
Assets/Agents Firm (f) Household ( h) Bank ( b) Central Bank ( cb) Σ
Loans −𝐿𝑓 ,𝑏 −𝐿ℎ,𝑏 𝐿𝑏 = Í
𝑓 𝐿𝑓 ,𝑏 + Í
ℎ 𝐿ℎ,𝑏 0
Deposits 𝑀𝑓 ,𝑏 𝑀ℎ,𝑏 −𝑀𝑏 = −(Í
𝑓 𝑀𝑓 ,𝑏 + Í
ℎ 𝑀ℎ,𝑏) 0
Reserve holdings 𝑅𝑏 −𝑅𝑐𝑏 = − Í
𝑏 𝑅𝑏 0
Reserve issuance −𝐵𝑏 𝐵𝑐𝑏 = Í
𝑏 𝐵𝑏 0
Net worth 𝑁𝑊 𝑓 𝑁𝑊 ℎ 𝑁𝑊 𝑏 𝑁𝑊 𝑐𝑏 0
Table 2: Agents’ flow of funds
Flows/Agents Firm (f) Household ( h) Bank ( b) Central Bank ( cb) Σ
Wages − Í(𝑤 𝑓 ,𝑡 × 𝑛) + Í(𝑤 𝑓 ,𝑡 × 𝑛) 0
Consumption + Í(𝑝 𝑓 ,𝑡 × 𝑌𝑓 ,𝑡 ) − Í(𝑝 𝑓 ,𝑡 × 𝑌𝑓 ,𝑡 ) 0
Dividends + Í 𝑑𝑖𝑣 𝑏,𝑡 − Í 𝑑𝑖𝑣 𝑏,𝑡 0
Interest on loans − Í(𝑖𝐹
𝑡 × 𝐿𝑓 ,𝑡 ) − Í(𝑖𝐻
𝑡 × 𝐿ℎ,𝑡 ) + Í(𝑖𝐹
𝑡 × 𝐿𝑓 ,𝑡 ) + Í(𝑖𝐻
𝑡 × 𝐿ℎ,𝑡 ) 0
Capital injections + Í 𝐶𝐼𝑏,𝑡 − Í 𝐶𝐼𝑏,𝑡 0
Notes: The table only shows interactions between agents that result in changes in net worth.
9

3.2 Firm behaviour
Firm behaviour in the model is determined by wage and price setting rules, production and borrowing
decisions, and debt obligations. Our simulated economy is populated by a total of 𝐹 heterogeneous
firms, indexed by 𝑓 , that produce a homogeneous consumption good using household labour as their
only input. Each firm holds deposits and possibly an outstanding loan on its balance sheet. Let 𝑀𝑓 ,𝑡
denote firm 𝑓 ’s deposits at time 𝑡, and 𝐿𝑓 ,𝑡 its outstanding loans at time 𝑡.
Wages in the simulated economy are firm-specific and incorporate nominal rigidity. Each firm
employs a fixed number of households as workers, given by 𝑛 = 𝐻
𝐹 , where 𝐻 is the total number of
households in the model, with 𝐻 > 𝐹 . This workforce per firm remains constant over the simulation.
Each active firm pays a firm-specific nominal wage, denoted by 𝑤 𝑓 ,𝑡. Firms that become inactive (due
to default or credit denial) cease operations and therefore do not set wages while inactive. Wages are
downwardly rigid, as documented in the empirical literature summarised in Gross (2022), such that
firms only increase wages when past inflation exceeds past wage growth; otherwise, wages remain
unchanged. For an existing firm
𝑤 𝑓 ,𝑡 = 𝑤 𝑓 ,𝑡 −1 × 𝑒 Δ𝑤𝑓 ,𝑡
where 𝑒 Δ𝑤𝑓 ,𝑡 is a wage growth factor. New entrant firms, which have no wage history, set
𝑤 𝑓 ,𝑡 = ¯𝑤𝑡 −1 × 𝑒 Δ𝑤𝑓 ,𝑡
where ¯𝑤𝑡 −1 is the economy-wide average wage in period 𝑡 − 1. A new firm, lacking its own wage
history, benchmarks its initial wage on last period’s average wage in the economy.
Wage growth, Δ𝑤 𝑓 ,𝑡, is determined by comparing the firm’s price inflation in period 𝑡 − 1 with
its wage growth in the same period and applying an inflation pass-through parameter, 𝜅 ∈ ( 0, 1].8
Formally,
Δ𝑤 𝑓 ,𝑡 =
 

𝜅 × Δ𝑝 𝑓 ,𝑡 −1, if Δ𝑝 𝑓 ,𝑡 −1 > Δ𝑤 𝑓 ,𝑡 −1
0, if Δ𝑝 𝑓 ,𝑡 −1 ≤ Δ𝑤 𝑓 ,𝑡 −1
For existing firms, Δ𝑝 𝑓 ,𝑡 −1 denotes a firm’s own price inflation in period 𝑡 − 1, and Δ𝑤 𝑓 ,𝑡 −1 is its wage
growth in period 𝑡 − 1. For a new entrant, inflation and wage growth are taken from the aggregate
economy, Δ𝑝 𝑓 ,𝑡 −1 = ¯Δ𝑝𝑡 −1 and Δ𝑤 𝑓 ,𝑡 −1 = ¯Δ𝑤𝑡 −1. This rule ensures nominal wage rigidity: wages do
not fall, and increases occur only when price inflation outpaces past wage growth, and even then, only
8We allow 𝜅 < 1 to capture incomplete wage indexation. Partial pass-through dampens “second-round” wage–price
feedback, where strong indexation can amplify inflationary shocks through mutually reinforcing wage and price adjustments,
limiting inflation persistence.
10

partially, depending on 𝜅.
All firms start with the same initial nominal wage, which is arbitrary and has no effect on results,
as only relative wage changes matter in the model. The total wage bill for firm 𝑓 at time 𝑡 is given by:
𝑊 𝐵𝑓 ,𝑡 = 𝑤 𝑓 ,𝑡 × 𝑛.
Firms borrow only when their resources are insufficient to meet the wage payments. In each period
𝑡, if a firm’s deposits do not cover its wage bill, it demands a working-capital loan of size 𝑙𝑓 ,𝑡. This
loan amount equals the difference between the wage bill and the firm’s deposit balance. 9 Firms do
not necessarily borrow every period; however, in the first simulation period all firms start with zero
deposits (𝑀𝑓 ,0 = 0) and therefore must borrow to pay wages. The interest rate on these loans, 𝑖𝐹
𝑡 , varies
over time and is set by the bank based on the economy-wide average credit risk of firm loans (see
subsection 3.4 for details). This is consistent with the model’s assumption of no bank competition, and
does not constrain the model, as firms operate in a common sector and can reasonably be assumed to
sustain stable banking relationships over time. Each new loan has a maturity of one simulation period
(𝑑𝑓 ,𝑡 = 1).10
Bank credit supply is not perfectly elastic, as banks must satisfy regulatory capital requirements,
leading to credit rationing. Consequently, not all firms obtain the credit needed to meet their wage-bill
obligations. Firms that fail to secure credit become inactive for two consecutive periods, generating
unemployment. Some of these firms may still hold outstanding debt; however, temporary inactivity
due to credit denial does not automatically trigger default. As long as a firm has sufficient deposits
to cover its interest payments, it remains solvent, despite ceasing operations (see default conditions
below).
Firm output is linear in labour, with each worker producing one unit of the consumption good per
period. In each period 𝑡, each active firm 𝑓 produces 𝑌𝑓 ,𝑡 = 𝑛, implying that labour productivity is
fixed and normalised to one unit of output per worker. Because firm-level output is proportional to its
number of employees, the aggregate output in period 𝑡 equals the sum of output across all firms. The
assumption of constant returns to labour ensures that scaling the number of firms or workers expands
aggregate output proportionally.
Firms set prices to fully clear their output each period, ensuring that nominal demand equals rev-
enue and that no inventory is carried forward. In this single-good economy, firms produce a homo-
geneous consumption good but set their own prices based on the demand they face from households,
9When the bank extends this loan, it simultaneously credits the firm’s deposit account with the same amount, thereby
creating new money in the economy.
10This is interpreted as one month in the model by calibrating the annual interest rate consistent with 12 model periods.
11

who choose a supplier each period (see subsection 3.3). Given these demand conditions, firms select a
price that guarantees the sale of their entire output. Formally, the pricing rule is:
𝑝 𝑓 ,𝑡 =
Í
ℎ→𝑓 𝑐ℎ,𝑡
𝑌𝑓 ,𝑡
where Í
ℎ→𝑓 𝑐ℎ,𝑡 is the nominal consumption allocated by households to firm 𝑓 in period 𝑡. This rule
ensures market clearing for firm 𝑓 ’s goods market by equating revenue to nominal demand. It is also
consistent with profit maximisation: setting a lower price would reduce profits by selling output too
cheaply, while a higher price would leave some output unsold. As a result, the firm optimally clears its
market each period. The aggregate price index is calculated by applying a price growth factor to the
previous period index value. The growth factor is calculated as the ratio of the cross-sectional mean of
firm-level prices in period 𝑡 to that in period 𝑡 − 1. This approach ensures that the price index reflects
the average proportional change in prices across firms over time.
Firms operate under limited liability, under which firms default when their deposits are insufficient
to meet interest obligations. Default generates losses for the bank, which are partially mitigated through
the seizure of the firm’s deposits as recovery value. A defaulting firm becomes inactive for two periods,
during which its workers become unemployed, and subsequently re-enters the market as a new firm
with zero net worth and the same workforce. Conditional on avoiding default, the firm either repays
the full principal and interest or, if only the interest can be paid, rolls over the outstanding principal
to the next period. When rollover occurs, the new credit granted to the firm is added to its existing
liabilities. Overall, in each period, some firms remain active and contribute to aggregate output, while
others are inactive and contribute to unemployment. Importantly, inactivity can arise both from default
and from credit denial.
3.3 Household behaviour
Household behaviour in the model is governed by decisions on consumption, housing market par-
ticipation, and the servicing of mortgage debt. The simulated economy contains 𝐻 heterogeneous
households indexed by ℎ. These households consume goods produced by firms, earn labour income,
regularly participate in the housing market (financing purchases through borrowing), and hold equity
stakes in banks, from which they receive dividends. Each household holds a deposit account at a bank
and, if indebted, services a mortgage issued by the same bank. A household’s net worth is defined as
the difference between its deposits in period 𝑡, 𝑀ℎ,𝑡 , and its outstanding mortgage, 𝐿ℎ,𝑡 .
Housing demand and mortgage borrowing are modelled through a constrained homeownership
12

process in which households participate in a double-auction market for houses, as illustrated in Figure
3. Only a fixed fraction of households, 𝐻𝑓 𝑟𝑎𝑐 , can own a house in the model because housing supply
is limited. At the start of the simulation, available houses are randomly allocated to households, des-
ignating them as initial homeowners. The remaining households live in social housing, where no rent
is charged. However, households have an intrinsic demand for housing services that can be satisfied
only via mortgage-financed homeownership. Consequently, those without a house enter the housing
market and participate in a double-auction mechanism to acquire a dwelling, provided they can afford
it.11 This, together with the introduction of mortgage lending, is one of the key extensions we introduce
to the original framework.
Household bids in the housing market are constrained by affordability considerations. Each prospec-
tive buyer submits a bid price, 𝑝𝑏𝑖𝑑
ℎ,𝑡 , for the house, which is capped by what the household can afford un-
der a debt service-to-income (DSTI) constraint. Households are assumed to finance the entire purchase
with a mortgage (100% loan-to-value ratio assumption) of duration 𝑑ℎ,𝑡 at interest rate 𝑖𝐻
𝑡 . Accordingly,
the bid reflects the maximum house price consistent with keeping mortgage payments within a feasible
share of wage income. The maximum amount of income the household allocates to mortgage payments
in each period is 𝐷𝑆𝑇 𝐼ℎ × (1 − 𝑀𝑃𝐶 ) × 𝑤ℎ,𝑡 , where 𝑤ℎ,𝑡 is wage income, 𝑀𝑃𝐶 represents the economy-
wide marginal propensity to consume (i.e., the share of income available for mortgage payments), and
𝐷𝑆𝑇 𝐼ℎ captures household-specific borrowing limit preferences. 12 Different households have different
DSTI tolerances, introducing heterogeneity in how much of their income they are willing to commit to
debt service.13 Given this maximum affordable payment, the implied maximum mortgage, and therefore
the bid price is:
𝑃𝑏𝑖𝑑
ℎ,𝑡 = [𝐷𝑆𝑇 𝐼ℎ × ( 1 − 𝑀𝑃𝐶 ) × 𝑤ℎ,𝑡 ] × 1 − ( 1 + 𝑖𝐻
𝑡 ) −𝑑ℎ,𝑡
𝑖𝐻
𝑡
where the very last term is the standard annuity present-value factor. This affordability constraint
prevents households from taking on mortgage obligations that exceed a prudent share of their income.
Sellers set ask prices by indexing them to recent market conditions, adjusting prices in line with
movements in the median transaction price. Sellers include households that have repaid their mort-
gages and are offering their homes for sale, as well as banks liquidating foreclosed properties (see more
11Only households that are employed and do not already own a property can take part in the house auction.
12In our model, households allocate their wage income according to a fixed marginal propensity to consume (MPC). We
use a common MPC for all households (an economy-wide value), for simplicity.
13The borrowing limit for each household is determined by sampling from a truncated Beta distribution, with scale and
shape parameters 𝛼 and 𝛽, and truncation bounds L and U. Specifically, the distribution is truncated between a minimum
DSTI ratio of 5% and a maximum of 55%. This approach reflects heterogeneity in household borrowing capacity and ensures
values remain within realistic policy bounds.
13

on household default below). At the start of the simulation, each house is assigned an initial price drawn
from a cross-sectional distribution, denoted by 𝑃 𝑗
𝑡 with 𝑗 = 1, . . . , (𝐻𝑓 𝑟𝑎𝑐 × 𝐻 ), where (𝐻𝑓 𝑟𝑎𝑐 × 𝐻 ) is
total housing supply. Thereafter, each seller updates the asking price of house 𝑗 based on overall mar-
ket conditions. Specifically, the ask price is indexed to the recent median transaction price, including
transactions involving foreclosed properties. The ask price for house 𝑗 at time 𝑡 is given by:
𝑃 𝑗
𝑡 = 𝑃 𝑗
𝑡 −1 ×

1 +
˜𝑃𝑡 −1 − ˜𝑃𝑡 −2
˜𝑃𝑡 −2

where ˜𝑃𝑡 −1 denotes the median price of all houses transacted in period 𝑡 − 1. Thus, sellers adjust ask
prices in line with recent market-wide price movements: increases in the median transaction price lead
to higher ask prices, while stable or declining medians prompt sellers to maintain or reduce prices. 14
A housing transaction occurs when a matched buyer–seller pair agrees on a price and the buyer
successfully obtains mortgage financing, which may not always be possible due to credit supply con-
straints. A prospective buyer is considered successful when their bid price meets or exceeds the seller’s
ask price. In the model, the transaction price is set equal to the buyer’s bid; thus, buyers may pay
above the seller’s minimum acceptable price. Given the assumption of 100% loan-to-value financing,
the transaction price also determines the new mortgage principal 𝑙ℎ,𝑡 , if the household is able to secure
the loan.
The prices of houses sold are updated to reflect their transaction values, while unsold house prices
are adjusted using the growth rate of the median transaction price. The overall house price growth in
the simulated economy is then calculated based on the average price of both sold and unsold properties.
Mortgage credit in the model is constrained by bank capital regulation, which affects whether successful
bidders in the housing market can complete their transactions. A successful house bidder may not be
able to obtain the mortgage it needs, in that case the transaction does not occur, and the household
remains in social housing. If the household secures a mortgage, the purchase is completed, and the
new homeowner begins servicing the debt each period. The interest rate on new mortgage loans is set
by the banks based on the economy-wide average credit risk of household mortgages (see subsection 3.4
for details). Mortgage loans are long-term, with an average maturity of 30 years, considerably longer
than the one-period maturity of firm loans. 15
14At the start of the simulation, when no house transactions have yet occurred, house prices are updated using a growth
rate based on the median price of all houses in the market, rather than only those that have been sold.
15Maturities are randomly drawn from a lognormal distribution with mean 𝜇𝐻 , and standard deviation 𝜎𝐻 .
14

Figure 3: Housing market: double auction mechanism
BUYERS  ·  bid price
𝑩𝟏 Bid = 120
𝑩𝟐 Bid = 100
𝑩𝟑 Bid = 85
𝑩𝟒 Bid = 60
SELLERS  ·  ask price
𝑺𝟏 Ask = 90
𝑺𝟐 Ask = 80
𝑺𝟑 Ask = 70
𝑺𝟒 Ask = 130
Selection rule: highest price among eligible sellers
✓ Price = 120
✓ Price = 100
✓ Price = 85
✕ No transaction
Bid too low
(no seller has ask ≤ 60)
Ask too high
(130 > all buyer bids)
①
Sort buyers
by bid price
(descending)
→ ②
Find eligible sellers
ask price ≤
bid price
→ ③
Select best seller
highest ask price
→ ④
Settle transaction
Transaction price = bid price;
remove matched seller
Notes: Transaction price equals the bid price. The eligible seller with the highest ask price (closest to bid) is selected. Unmatched
buyers remain in social housing; unmatched sellers re-list in later periods.
Household income in the model is generated through wage earnings and dividend payments, evolv-
ing with employment status and bank profitability. Households receive wage income, 𝑤ℎ,𝑡 , from sup-
plying labour to firms, and dividend income, 𝑑𝑖𝑣 ℎ,𝑡 , from holding bank equity. Wages are paid each
period unless a household becomes unemployed due to the temporary inactivity of its employing firm.
In that case, wage income is suspended for two periods, after which the household resumes employment
at the same firm and wage payments restart. When banks accumulate capital in excess of regulatory
requirements, they distribute dividends to households (see subsection 3.4). Importantly, unemployed
households do not earn wages during the inactivity spell but may continue to receive dividend income.
Household consumption is determined by a simple rule linking available resources to spending.
Household income flows, i.e. wages and dividends, are added to savings from the previous period
to determine the resources available for consumption and debt payments. Each period, a household
allocates its consumption 𝑐ℎ,𝑡 to a randomly selected firm, generating firm-specific demand. This as-
sumption introduces the only stochastic element in the model, and it is important for generating the
endogenous macro-financial cycles in the absence of external shocks. Households follow a simple con-
sumption rule: they spend a fixed fraction of their available resources each period. 16 The consumption
rule is:
𝑐ℎ,𝑡 = 𝑀𝑃𝐶 × ( 𝑀ℎ,𝑡 −1 + 𝑤ℎ,𝑡 )
16For this calculation, available resources include beginning-of-period deposits and wage income received during the
period. Dividend payments, which are distributed at the end of the period, are saved entirely until the next period.
15

When a household sells its house, the resulting increase in its deposit balance represents a temporary
positive wealth shock. Instead of applying the standard consumption rule to this unusually large inflow,
the model imposes a consumption-smoothing rule (a “Ferrari fix”) to avoid an unrealistically sharp rise
in consumption (see Appendix A for details).
Mortgage defaults arise when households cannot meet minimum debt-service requirements, re-
sulting in foreclosure of the property. After allocating resources to consumption, a household uses
its remaining deposits together with any dividend payout to service its mortgage. As with firms, the
household either repays a part of the principal and interest or, if it can only cover interest, rolls over the
outstanding principal to the next period. However, if available resources are insufficient even to meet
the interest payment, the household defaults. In this case, the bank forecloses on the property, whose
value may have changed relative to the original purchase price, and the repossessed house is placed in
the next period’s housing auction. For simplicity, the model does not impose an additional discount on
foreclosed properties beyond what is already captured by housing market dynamics; as a result, bank
credit losses may be understated relative to a setting with distressed-asset price effects.
3.4 Bank behaviour
The banking system in the model performs the following core functions: supplying and allocating
credit across borrowers, setting interest rates, and distributing dividends. We introduce a number of 𝐵
heterogeneous banks, indexed by 𝑏, subject to capital requirements and two forms of capital injections,
one to sustain minimum credit supply and one to prevent bank insolvency. A bank’s asset side consists
of loans to firms ( 𝐿𝐹
𝑏,𝑡 ) and households ( 𝐿𝐻
𝑏,𝑡 ), 𝐿𝑏,𝑡 = 𝐿𝐹
𝑏,𝑡 + 𝐿𝐻
𝑏,𝑡 , and reserves held at the central bank,
𝑅𝑏,𝑡 . Total assets are therefore given by 𝐴𝑏,𝑡 = 𝐿𝑏,𝑡 + 𝑅𝑏,𝑡 . On the liability side, bank 𝑏 holds deposits
from firms ( 𝑀 𝐹
𝑏,𝑡 ) and households ( 𝑀𝐻
𝑏,𝑡 ), 𝑀𝑏,𝑡 = 𝑀 𝐹
𝑏,𝑡 + 𝑀𝐻
𝑏,𝑡 , and may borrow from the central bank
𝐵𝑏,𝑡 . Net worth (equity) is defined as 𝑁𝑊𝑏,𝑡 = 𝐴𝑏,𝑡 − ( 𝑀𝑏,𝑡 + 𝐵𝑏,𝑡 ). All banks start the simulation with
zero net worth. Over time, heterogeneity across banks emerges endogenously, reflecting differences in
loan portfolio composition (e.g., loan size, maturity structure, and default events). Compared to a single
bank, introducing relatively simple but multiple banks allows a more granular assessment of the impact
of releasable buffers, as the ex-post heterogeneous bank balance sheets can inform the distribution of
interventions and costs of safeguarding the banking system under a TVP regime. 17
Banks begin the simulation with an evenly distributed customer base, which remains fixed over
17The balance sheet heterogeneity is a first step towards a richer modelling of the banking sector, e.g. through bank
competition or differentiated business models, which, together with the macroeconomic feedback of complete bank default,
we leave for future research.
16

time and shapes the flow of deposits and liquidity in the system. At the outset, households and firms
are allocated evenly across banks, such that each bank serves 𝑛𝐻 = 𝐻
𝐵 households and 𝑛𝐹 = 𝐹
𝐵 firms.
Customers do not switch banks during the simulation, giving each bank a stable depositor base that can
eventually become borrowers too. However, this fixed allocation does not imply a closed system per
bank. When a customer of one bank transacts with a customer of another bank, funds move between
banks through the settlement of central bank reserves (see Appendix A for details). These reserve flows
redistribute liquidity across the banking system without directly affecting any bank’s net worth.
Banks’ credit supply is bounded by regulatory capital requirements, which limit their ability to meet
all loan demand from firms and households. The primary role of banks in the model is to provide loans,
differentiated by purpose and maturity. Firm loans are unsecured short-term credit used to finance
working capital needs. Household loans (mortgages) are long-term and secured by housing collateral.
Importantly, banks cannot expand lending without bound; their credit supply is constrained by capital
regulation.
The credit supply of bank 𝑏 in period 𝑡, denoted 𝐶𝑆𝑏,𝑡 , is limited by its capital headroom, defined
as the difference between its capital ratio and the regulatory capital requirement, both expressed in
terms of a bank’s risk-weighted assets (RW A). Subsection 3.5 and Appendix A provide additional details
about the risk-based capital requirements framework. Specifically, let 𝐶𝐴𝑅𝑏,𝑡 = 𝑁𝑊𝑏,𝑡
𝑅𝑊 𝐴𝑏,𝑡
be the bank’s
capital ratio and 𝐶𝐴𝑅𝑟𝑒𝑞
𝑡 the regulatory capital requirement. The bank’s credit supply corresponds to
the maximum increase in RW A it can take on without breaching the capital requirement:
𝐶𝑆𝑏,𝑡 = max

0, 𝑁𝑊𝑏,𝑡
𝐶𝐴𝑅𝑟𝑒𝑞
𝑡
− 𝑅𝑊 𝐴𝑏,𝑡

This rule limits the aggregate supply of credit to firms and households. When available credit is insuf-
ficient to meet demand, some loan applications are rejected. As discussed in subsections 3.2 and 3.3,
firms that cannot obtain working-capital financing become inactive, while households unable to secure
a mortgage forgo the housing transaction.
Capital injections in the model serve two purposes: ensuring minimum credit supply to firms and
preventing banks from breaching regulatory capital requirements following losses. Although banks
may deny credit to comply with capital requirements, each bank in the model must satisfy a minimum
share of the working-capital loan demand it receives, defined as a fixed percentage, 𝜎, of the wage
bill of its client firms. When a bank’s available credit supply is insufficient to meet this minimum, it
receives an equity injection from the central bank. Effectively, the central bank recapitalises the bank
17

pre-emptively to avoid a contraction in credit (see Appendix A for details). Banks capable of supplying
at least 𝜎 percent of their firms’ wage bill receive no injection. This mechanism is not present in
the original model because banks are not subject to regulatory capital requirements and can therefore
continue operating with negative equity without restricting credit supply. In our model, by contrast,
capital requirements constrain banks’ lending capacity. If this constraint causes credit supply to be
substantially lower than firms’ demand for working-capital loans, many firms may be unable to finance
production, resulting in a collapse of the economy. The minimum credit provision rule is therefore
introduced to preclude such outcomes, which may arise as a consequence of imposing regulatory capital
requirements.
The central bank also injects capital into banks, when losses from firm and household defaults
reduce a bank’s capital ratio below the regulatory capital requirements. This is because the model does
not allow banks to fail or exit due to insolvency. This assumption of a public backstop reflects historical
crisis interventions, where authorities recapitalised banks to prevent a systemic credit crunch, and is
consistent with an effective resolution framework, an assumption also used in Bardoscia et al. (2025). 18
Both types of capital injections carry no economic costs in the model because taxes and shareholder
dilution are abstracted from. This simplifying assumption allows the analysis to focus on how alter-
native capital regimes affect credit dynamics and bank resilience without introducing second-round
macroeconomic effects. One output of our simulation is the frequency and magnitude of capital injec-
tions to avert bank insolvency under different regulatory settings (see section 5), which we interpret as
an inverse indicator of banking-system robustness.
Banks allocate credit using a risk-based rule that prioritises safer borrowers. In each period, banks
manage risk conservatively by ranking loan applicants according to their assessed creditworthiness
and approving loans in order of increasing risk. For firms, applicants are ranked by their leverage ra-
tio at loan origination, with lower-leverage firms considered safer due to a larger equity buffer and
a lower likelihood of default. For households, banks use the debt-service-to-income (DSTI) ratio at
loan origination as the main risk indicator. Households with lower DSTI ratios are viewed as safer
because they have greater income capacity to meet mortgage payments in case of a shock. This risk-
based allocation framework ensures that scarce credit is directed toward borrowers with the highest
expected repayment probability and aligns with empirical evidence that banks tighten lending stan-
dards in downturns. Finally, each bank allocates a fixed share, 𝜆, of its credit supply to firm lending,
18While this mechanism prevents bank runs and maintains credit flow, it could introduce moral hazard (implicit subsidies).
In our model, we take this mechanism as an exogenous safety net rather than a choice, to strictly compare scenarios with
different capital requirement regimes in a controlled way.
18

with the remainder allocated to household loans.
Firms can have multiple loans at the same time. When this occurs, the model consolidates the
old and new loans into a single obligation for repayment purposes (see Appendix A for details). This
simplification preserves computational tractability without altering the economic mechanisms driving
firm behaviour. By contrast, household mortgages are not consolidated because each household holds
at most one mortgage at a time.
Loan maturities differ across borrower segment and loan pricing reflects a markup over funding
costs and aggregate segment-level credit risk. As outlined in subsections 3.2 and 3.3, firm debt is essen-
tially short term while mortgage loans span multiple periods. Interest rates on new loans to both firms
and households are set at origination and remain unchanged over the entire duration of the loan. In
the absence of price competition, all borrowers within a segment face the same interest rate in a given
period, irrespective of which bank they use or its specific (idiosyncratic) risk. Loan pricing follows a
markup rule over funding costs and expected credit losses:
𝑖 𝑗
𝑡 = 𝜇 + 𝑖𝑀
𝑡 + 𝑃𝐷 𝑗
𝑡 × 𝐿𝐺𝐷 𝑗
𝑡
1 − 𝑃𝐷 𝑗
𝑡
, 𝑗 ∈ {𝐻, 𝐹 } .
where, 𝜇 bank profit margin, 𝑖𝑀
𝑡 is the deposit rate, and 𝑃𝐷 𝑗
𝑡 and 𝐿𝐺𝐷 𝑗
𝑡 denote the bank’s expected
probability of default and loss given default in borrower segment 𝑗.19 Under this pricing rule, loan
rates increase with credit risk: a bank charges a higher loan rate if it expects a larger share of loans in
its portfolio to default or if the expected losses in the event of default are larger. We assume that banks
form their expectations of PDs and LGDs in an adaptive backward-looking manner. That is, rather than
forecasting, banks use realized default rates and losses as proxies for current risk levels (see Appendix
A for details).
Dividend distribution is governed by a simple rule linking payouts to banks’ capital positions, en-
suring that dividends are paid only when banks remain above their internal target capital ratios. Banks
distribute dividends to households, their equity holders, only when certain conditions are met. Each
bank has a target capital ratio for distributions, denoted𝐶𝐴𝑅𝑡𝑎𝑟𝑔𝑒𝑡
𝑡 , which establishes the minimum level
of capital the bank aims to maintain relative to its risk-weighted assets. This target is identical across
banks but varies with the regulatory regime and is typically set at or above the regulatory requirement
to ensure that payouts occur only when banks are sufficiently capitalised.
A bank distributes dividends at period 𝑡 only if it did not receive a capital injection in that period;
19Deposit rates are set to zero throughout the simulation as in Gross (2022) baseline simulation. Also, in our simulations,
all banks use the same pricing rule, with the markups and credit risk parameters identical across banks.
19

and its capital ratio before considering interest income, loan losses and dividend payments is above its
target capital ratio. The first condition ensures that banks that were just bailed out do not immedi-
ately pay that money out to shareholders, consistent with dividend restrictions following government
support. If both conditions hold, the bank distributes all capital in excess of its target. The dividend
amount is:
𝑑𝑖𝑣 𝑏,𝑡 = max
h
0,

𝐶𝐴𝑅𝑏,𝑡 − 𝐶𝐴𝑅𝑡𝑎𝑟𝑔𝑒𝑡
𝑡

𝑅𝑊 𝐴𝑏,𝑡
i
which reduces the bank’s post-dividend capital ratio to exactly its target level. This rule effectively
keeps capital ratio at the targeted minimum while returning surplus capital to shareholders (see Ap-
pendix A for details). Dividend payments are allocated equally across the bank’s household depositors,
increasing their deposit balances but not their current-period resources for consumption (see subsec-
tion 3.3).
Debt servicing follows an annuity structure, under which borrowers either repay principal and in-
terest, roll over principal, or default depending on their available resources. At the end of each period,
all firms and households with outstanding loans are required to make debt payments, which amount to
an annuity payment that covers interest and principal and is based on the loan’s terms (see Appendix
A for details). If the borrower has sufficient deposits to pay the full annuity amount, the loan amortises
normally (i.e. the principal amount outstanding decreases). If deposits cover only the interest com-
ponent, the borrower pays interest and rolls over the principal to the next period (i.e. the principal
amount outstanding stays constant into the next period). If the borrower cannot even pay the interest
due, the loan goes into default.
Default events trigger different recovery mechanisms for firms and households, reflecting the dis-
tinct nature of their loans and timing of loss recognition. When a firm defaults, the bank first seizes
the firm’s deposits to offset losses. If a defaulting firm e𝑓 has outstanding loan 𝐿 e𝑓 ,𝑡 and deposits 𝑀 e𝑓 ,𝑡,
the bank recovers:
𝑠𝑒𝑖𝑧𝑒 𝑏, e𝑓 ,𝑡 = min

𝑀 e𝑓 ,𝑡, 𝐿e𝑓 ,𝑡

,
with any remaining loan value written off immediately. The model does not include non-performing
loans or provisioning; losses are realized immediately and written off against capital. Household default
follows a different process. When a household eℎ defaults, the bank writes off the entire outstanding
mortgage in period 𝑡, as the collateral value cannot be recovered immediately. Household deposits
20

are not seized (i.e., mortgages are non-recourse in the model). 20. The bank repossesses the house and
attempts to sell it in period 𝑡 + 1. When successful, the sales proceeds partially offset the capital loss
depending on house price dynamics. 21
3.5 Central bank and capital requirements framework
The central bank performs two roles in the model; it acts as the system’s settlement authority, and as
the prudential regulator. It is modelled as a single agent and in its settlement function provides reserve
balances that banks use to clear deposit transfers arising from transactions between their customers.
These are needed when a household decides to consume from a firm associated with a different bank
or when the household purchases a house from either a seller associated with a different bank or from
a bank that is not the household’s bank (e.g. when a bank sells a foreclosed house). In both cases,
banks settle payments by adjusting their reserve accounts at the central bank. Reserves are also used
to inject capital into banks when needed. Operationally, the central bank credits the reserve account
of the recipient bank by the amount of the injection. On the bank’s balance sheet, reserves and equity
increase by the same amount. On the central bank’s balance sheet, reserve liabilities increase and net
worth declines correspondingly.
The central bank regulatory function shapes bank’s credit supply through risk-based capital re-
quirements. Although these requirements constrain banks’ balance-sheet capacity, they do not gen-
erate any balance sheet transactions between the central bank and banks. Capital requirements are
set as a share of banks’ RW A, reflecting the prudential principle that different assets carry different
levels of risk. The central bank, acting as the prudential authority, assigns risk weights to each asset
class. It distinguishes three asset categories: reserves held at the central bank, mortgage loans to house-
holds, and loans to firms. Reserves are treated as risk-free, while loans to firms are treated as much
riskier than household mortgages, reflecting the existence of collateral (see Appendix A for details).
Given RW As, the central bank requires banks to maintain their regulatory capital ratio at or above a
20This assumption reflects the fact that, while most European jurisdictions employ recourse systems, mortgage lenders
still rely primarily on the collateral securing the loan to offset losses, while any offset against household deposits may not be
automatic.
21This implies that the LGD for mortgage loans is set equal to one and any recovery from the subsequent sale of the repos-
sessed property is recorded separately when the sale occurs. As a result, mortgage lending rates are somewhat higher than
they would be if pricing were based on the net loss after collateral recovery. This simplification is unlikely to materially affect
the results, as mortgage exposures are small relative to firms’ working capital loans. However, it prevents us from capturing
the procyclicality of mortgage LGDs through fluctuations in house prices. Incorporating realized collateral recoveries into
LGD estimates is left for future research.
21

minimum threshold:
𝐶𝐴𝑅𝑏,𝑡 ≥ 𝐶𝐴𝑅𝑟𝑒𝑞
𝑡 ,
where 𝐶𝐴𝑅𝑟𝑒𝑞
𝑡 denotes the regulatory capital requirement. This prudential constraint directly condi-
tions banks’ credit supply and determines whether additional lending is feasible.
Regulatory capital requirements in the model can follow either a time-invariant framework or a
time-varying framework that adjusts over the credit cycle. Given our objective of identifying the tail
effects of a releasable buffer, we consider that the central bank can set regulatory capital requirements
under two distinct regimes. In the first regime, banks operate under a time-invariant capital require-
ment (hereafter, TIP model), which remains constant throughout the credit cycle and serves as our
benchmark for assessing the benefits and costs of introducing a releasable buffer. In the second regime,
banks are subject to a time-varying capital requirement that fluctuates over the credit cycle (hereafter,
TVP model).
3.5.1 Time-varying capital requirements regime.
Under this regime, banks are subject to a constant minimum requirement of 8% and to a time-varying
releasable buffer, conceptually similar to the Countercyclical Capital Buffer (CCyB), denoted 𝐶𝐶𝑦𝐵𝑡 ,
that fluctuates over the credit cycle. 22 The required capital ratio therefore becomes:
𝐶𝐴𝑅𝑟𝑒𝑞
𝑡 = 8% + 𝐶𝐶𝑦𝐵𝑡 .
The buffer accumulation is based on a smoothed measure of real credit growth, defined as a 48-month
exponential backward moving average (𝐶𝑟𝑒𝑑𝑖𝑡𝐸𝐵𝑀𝐴 𝑡 ). This smoothing approach filters out short-term
volatility and highlights cyclical patterns that the central bank uses to inform the setting of the buffer.
Specifically, the releasable buffer is set according to:
𝐶𝐶𝑦𝐵𝑡 =
 

0%, 𝐶𝑟𝑒𝑑𝑖𝑡𝐸𝐵𝑀𝐴 𝑡 < 6.5%,
0.185 × (𝐶𝑟𝑒𝑑𝑖𝑡𝐸𝐵𝑀𝐴 𝑡 − 6.5%), 6.5% ≤ 𝐶𝑟𝑒𝑑𝑖𝑡𝐸𝐵𝑀𝐴 𝑡 ≤ 20%,
2.5%, 𝐶𝑟𝑒𝑑𝑖𝑡𝐸𝐵𝑀𝐴 𝑡 > 20%.
22Macroprudential authorities in the EU have at their disposal multiple buffers. Even though the CCyB is the only buffer
with releasable features in its design, macroprudential authorities recognise that other buffer like the sectoral systemic risk
buffer could be used in a countercyclical way. So, the analysis presented here could be easily extended to consider the impact
of certain time-varying sectoral capital policies.
22

rounded down to the nearest 0.25 percentage point and capped at 2.5% of RW As, consistent with Basel
III guidance.23 According to this rule, when credit growth is modest (i.e. below 6.5%, which is the 50th
percentile of the simulated distribution) the releasable buffer is set to zero. Credit growth below the
median is interpreted as a normal (neutral) risk environment in our model. Once credit growth is equal
or greater than 6.5%, the releasable buffer is set to a positive rate, increasing linearly as credit growth
accelerates up to 20% (95th percentile of the distribution). The central bank reviews the buffer quarterly
and any announced increase at time 𝑡 is implemented after 12 months. This lag is consistent with Basel
III guidance and is intended to give banks time to adjust to the higher requirements without imposing
costs on the economy (e.g. restricting credit supply).
Buffer release is triggered when labour market conditions deteriorate, proxied by an increase in the
three-month moving average of the unemployment rate. 24 Specifically, the buffer is set to zero when
this indicator exceeds 5% (80th percentile of the unemployment distribution), a threshold indicating a
recession. The immediate and full release of the buffer maximises its benefits as banks immediately
increase their capital headroom, helping them continue lending or at least avoid sharply cutting credit
supply. The objective of the time-varying capital requirement is to build resilience during upturns
and to support lending conditions in downturns through buffer releasability. Subsections 5.2 and 5.3
examine the implications of this regime in downturns and upturns, respectively.
4 Empirical and economic validation
In this section, we conduct a set of exercises to assess the empirical validity of our parametrised bench-
mark model, i.e. the TIP model. Appendix C presents the values for all model parameters used in the
simulations.
4.1 Empirical validation through moment matching
The model’s simulated moments fall within plausible cross-country empirical ranges. We assess the
empirical validity of the model by comparing simulated and empirical moments for three key macroeco-
23The coefficient 1.6 ensures a linear mapping from the credit growth range to a maximum buffer of 2.5% in the continuous
version of the rule. The implementation in discrete 25 basis point steps is imposed separately by rounding down the resulting
buffer to the nearest increment.
24Default rates could also be used as the indicator guiding the buffer release. However, in our model, default rates are
highly correlated with the unemployment rate (see panel 4B in Figure 4), so using them would yield similar results.
23

nomic variables: annual growth rate of real GDP and real credit, and the unemployment rate.25 The sim-
ulated moments are computed from 100 independent runs of the model, each spanning 1,500 monthly
periods.26 For each statistic, we average across the 100 runs to obtain a representative simulated mo-
ment. The corresponding empirical moments are obtained from quarterly data for all EU countries and
the United States over the period 1999–2024 (see Appendix D for data details). 27 For each variable,
we consider summary statistics that capture key features of their distributions: the mean, standard
deviation, median, and the 25th and 75th percentiles.
Table 3 reports these moments and indicates whether the simulated statistic lies within the empir-
ical range defined by the minimum and maximum values across countries. Cells highlighted in green
denote that the model-generated moment falls within this empirical range, while amber shading indi-
cates deviations. Despite its intentionally parsimonious structure, the model seems to reproduce the
empirical moments of GDP and credit growth well (though less so for unemployment), suggesting a
reasonable starting point for potentially calibrating the model to country-specific data. Appendix E
presents the simulated moments values for a broader set of variables.
Table 3: Key macroeconomic variables: simulated vs empirical moments
Mean Std. Dev. p25 Median p75
Real GDP growth (%, p.a.) Yes Yes Yes Yes Yes
Unemployment (%) No Yes No No No
Real credit growth (%, p.a.) Yes Yes Yes No Yes
Notes: Std. Dev. stands for standard deviation, p25 and p75 stand for the 25th and 75th percentiles, respectively, p.a. stands
for per year. Real GDP and real credit are measured as annual growth rates. For each statistic, the yes(no) indicator reflects
whether the average simulated moment (across 100 independent simulation runs of 1,850 monthly periods, with a 350-period
burn-in), falls within (outside) the min-max range of its empirical cross-country equivalent. Empirical moments are computed
using quarterly data for EU countries and the US between 1999 and 2024.
4.2 Cyclical properties of the model
The simulated economy captures expected cyclical co-movements, particularly the pro-cyclicality of
credit and the countercyclicality of unemployment and default rates. To assess how well the model
matches established stylised facts on cyclical behaviour, we analyse whether selected simulated vari-
25Inflation measures are excluded from the validation exercises because the model uses a stylised demand-driven pricing
rule without calibrated sticky price dynamics. Consequently, nominal values cannot be matched consistently to observed data.
More generally, the validation is intended as a generic empirical moment check and not a detailed, country level calibration.
26Each Monte Carlo simulation spans 1,850 monthly periods, with the first 350 periods discarded ( 20% of time-steps) to
allow agents’ balance sheets to stabilise and remove the effect of initial conditions. This simulation length provides a sufficient
number of economic cycles for a robust analysis and ensures the model’s statistical properties have stabilised, while keeping
computations tractable.
27Data for the UK are included up to the point of the UK’s withdrawal from the EU.
24

ables move in the same direction as the business cycle (pro-cyclical) or in the opposite direction (coun-
tercyclical), following the approach of Stock and Watson (1999). The cyclical component of real GDP,
extracted using the Hodrick-Prescott filter, is used as the reference business cycle indicator. For each
variable 𝑥𝑖
𝑡 with 𝑖 ∈ { 1, . . . , 𝑙}, we compute its cross-correlation with future and past values of the
reference indicator, corr (𝑥𝑖
𝑡, 𝑦𝑡 +𝑘 ) for 𝑘 ∈ {− 12, 0, 12}, corresponding to a one-year lag, contempora-
neous value, and one-year lead. Table 4 reports the results, with shading reflecting the strength of
cross-correlation.
Table 4: Cross-correlations with real GDP of selected simulated variables
t-12 t t+12
Unemployment - - -
Real credit + + +
Default rate – Firms - - -
Default rate – Households - - -
Inflation + + +
Notes: The table reports the sign of the average cross-correlations from 100 indepen-
dent runs of the model of 1,850 monthly periods, discarding the first 350 periods as
burn-in. Real GDP and real credit are expressed in logarithmic form and detrended us-
ing an HP filter with smoothing parameter of 129,600. Inflation is measured as annual
growth rates. Lags (-) and leads (+) correspond to one year (12 simulations periods).
A plus (minus) sign indicates a procyclical (countercyclical) relationship with the ref-
erence business cycle indicator. Cell shading indicates cross-correlation strength in
absolute terms: light orange (0.5-0.7), medium orange (0.7-0.9), and dark orange (>
0.9).
A positive contemporaneous correlation (𝑘 = 0) indicates pro-cyclicality, whereas a negative one
indicates countercyclicality. Inflation and real credit are procyclical, while the unemployment rate, and
default rates are countercyclical. The strong contemporaneous correlation between real GDP and real
credit reflects the credit-driven structure of the model. This is also consistent with empirical evidence
that credit expands in booms and contracts in recessions. Stronger lagged correlations for some vari-
ables also reflect plausible macroeconomic patterns, such as gradual labour market adjustment and
default risk responding to earlier GDP conditions and prolonged economic stress.
The simulated series exhibit clear cyclical patterns consistent with the cross-correlation results.
Figure 4 illustrates the joint behaviour of real credit growth (panel A), default rates by borrower segment
(panel B), against that of the unemployment rate, which serves as the proxy for the business cycle. 28
28Using real GDP growth as the business cycle indicator, as in Table 4, leaves the results qualitatively unchanged.
25

Figure 4: Cyclical behaviour of key simulated variables
(A) Real credit growth
(B) Firm and household default rates
Notes: Simulated variables are obtained from a single run of the model over 1, 850 monthly
periods. All series are smoothed using a moving average approach.
Consistent with the cross-correlation patterns, real credit growth displays a strong negative re-
lationship with unemployment: periods of rising credit growth tend to precede decreases in unem-
ployment. In contrast, both firm and household default rates move closely with the unemployment
rate, exhibiting a strong positive and largely contemporaneous relationship. All variables exhibit pro-
nounced cyclical fluctuations and firm default rate is noticeably higher than household default rate
during downturns. These patterns are in line with well-documented empirical regularities (Ivashina
et al., 2024; European Central Bank, 2025; European Banking Authority, 2025). Overall, the model’s
replication of a set of key empirical regularities, including matching selected statistical moments and
26

expected cyclical relationships between economic variables, supports its reliability as a framework for
studying the state-contingent effects of a releasable buffer.
5 Policy experiments
This section sets out the policy evaluation strategy used to assess the state-contingent tail costs and
benefits of a time-varying releasable buffer and discusses the main results.
5.1 Policy experiment design
Policy experiments evaluate the tail costs and benefits of introducing a time-varying, releasable capital
buffer by comparing distributions of key macro-financial variables between alternative capital require-
ment regimes. We use the DeTail model to conduct two policy experiments that evaluate the tail costs
and, respectively, benefits of a releasable buffer, which fluctuates over the credit cycle. In both experi-
ments, we compare the distribution of selected variables under a benchmark model with time-invariant
capital requirements (TIP model) to those generated by a model with a time-varying, releasable buffer
(TVP model). The variables of interest include real credit growth, default rates by borrower segment,
and bank losses.
The analysis evaluates policy costs and benefits separately during upturns and downturns of the
credit cycle. Downturns are defined as periods when the unemployment rate exceeds its 80th percentile,
capturing times of heightened stress in the real economy. Upturns are the complementary periods out-
side of these high-unemployment episodes. Because costs and benefits arise at different phases of the
credit cycle, we assess the policy effects separately for upturns and downturns. Specifically, policy
effectiveness is evaluated through: (i) improvements in the policy-relevant tail of each variable’s dis-
tribution, capturing whether severe outcomes become less severe; (ii) changes in dispersion, measured
by the interquartile range of the distribution; and (iii) shifts in probability mass near the tails, reflecting
changes in the likelihood of extreme events.
The tail benefits of releasable buffers arise during economic downturns as an improvement in the
policy-relevant tail of the distribution of the outcome variable under the TVP model relative to the TIP
model. The definition of improvement is contingent on whether an increase or decrease in the outcome
variable is the desired policy impact, from a systemic risk reduction perspective. Policy driven benefits
can be represented by increases in the lower-tail (also negative) percentiles of a variable (e.g. credit
27

growth) under a releasable buffer relative to a time-invariant capital requirement regime. 29 They may
also take the form of decreases in the higher-tail percentiles of a variable (e.g. sectoral default rates).
Conversely, the tail costs of releasable buffers are identified during upturns. Any costs are reflected
in a deterioration of the policy-relevant tail percentiles, a widening of the interquartile range, or an
increase in the probability mass around the extreme tails.
We further examine the policy’s effects on banking-system resilience and on the amplitude and
duration of the endogenous credit cycles. Although our model abstracts from the macroeconomic feed-
back effect of bank default, we can nevertheless gauge changes in the implicit cost of bank default by
tracking the need for central bank interventions. A lower frequency or size of such interventions in
the TVP model relative to the TIP model would indicate improvements in banking system resilience
even in the absence of formal defaults. Such results are consistent with a policy induced systemic risk
reduction; therefore, we include them as part of the assessment of the tail benefits of a releasable buffer.
Finally, because the DeTail model generates endogenous credit cycles, we are also able to assess the
effects of a releasable buffer on credit cycle dynamics. Following Drehmann et al. (2012), we evaluate
whether introducing a releasable buffer in the mix of capital requirements affects the amplitude and
duration of credit expansions and contractions (for example, whether contractions become shorter or
less severe under the TVP regime compared to the TIP regime).
5.2 Assessing the benefits of a releasable buffer in downturns
Tail benefits of releasable buffers emerge during economic downturns, when easing capital constraints
can mitigate severe outcomes. The first policy experiment focuses on the tail benefits of releasing a
capital buffer by comparing the distributions of key variables under the TIP model and the TVP model
during economic downturns. In the TIP model, banks are subject to a minimum capital requirement
of 8% plus a fixed buffer of 2.5%, which applies throughout the credit cycle (TIP-buffer model). In the
TVP model, banks are subject to the same minimum requirement but face a buffer that varies over
the credit cycle. Dividend payout decisions are governed by a target capital ratio linked to capital
requirements (see Appendix A for details). Under the TIP model, this target is fixed at the regulatory
requirement of 10.5%, whereas in the TVP model it starts at 10.5% when the releasable buffer is zero,
and then increases proportionally as the buffer accumulates. In general, because banks anticipate future
increases in time-varying capital buffers but cannot foresee their timing, they typically maintain capital
29An improvement in the lower tail of credit growth means that the bottom percentiles of the distribution are higher
(either positive or less negative) as a result of releasing the buffer, reflecting milder credit contractions during a downturn.
28

ratios above regulatory requirements by adjusting, for instance, dividend payouts. Our specification of
a target capital ratio that moves with the releasable buffer, while starting at the TIP level, replicates this
behaviour. Figure 5 illustrates the capital stack and associated dividend-payment thresholds in both
settings. This setup ensures that banks in both model simulations face the same capital requirements
at the peak of the credit cycle, so any differences in downturn outcomes can be attributed to the effects
of buffer releasability.
Figure 5: Components of capital ratios in the TIP-buffer and TVP models
Notes: The solid outline box denotes the minimum capital requirement of 8%. In the TIP-
buffer model (left capital stack), the dash-dotted outline marks the fixed 2.5% buffer. In the
TVP model (right capital stack), the dashed outline indicates the time-varying releasable
buffer, which can reach up to 2.5%. The dotted outline box represents capital held in excess
of the total requirement (minimum requirement plus the applicable buffer).
The release of capital buffers during downturns yields notable improvements in the tail of credit dy-
namics. Panel A of Figure 6 presents the simulated distributions of real credit growth during downturn
periods under the TIP-buffer and TVP models, based on 100 Monte-Carlo simulations of 1, 850 monthly
periods each, with the first 350 periods discarded as burn-in. All downturn observations across simu-
lations are pooled to construct the distributions. Panel B reports bootstrap-based confidence intervals
for the difference in selected distributional statistics between the two regimes, namely, the interquartile
range (IQR) and the 25th, 50th, and 75th percentiles, computed from 10, 000 resamples of the model-
by-model differences. 30 This statistical assessment complements the economic interpretation by indi-
cating whether observed differences are distinguishable from zero. This approach represents, to our
knowledge, the first application of such inference to policy experiments involving capital buffers in an
30These intervals are centred on the median difference between models because the bootstrap distributions of some statis-
tics are skewed, making the median a more representative measure of the typical difference than the mean.
29

agent-based model.
Figure 6: Real credit growth in downturns: TIP-buffer vs TVP models
TIP-buffer modelTVP model-60
-40
-20
0
20
40
60Per cent
(A) Distributions
IQR P25 Median P75-5
-4
-3
-2
-1
0
1
2
3Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Notes: Panel A shows the distribution of simulated real credit growth during downturn episodes, based on 100 Monte-Carlo simulations
of each model. Each simulation spans 1, 850 monthly periods, with the first 350 periods discarded as burn-in. Real credit growth is mea-
sured as an annual rate. Boxplots display the 25th percentile, median, and 75th percentile, with whiskers indicating values within 1.5 times
the interquartile range, excluding outliers; shaded areas show the kernel density estimate of the distribution of pooled real credit growth
in downturns (Gaussian kernel, bandwidth selected using Silverman’s rule). Panel B reports bootstrap-based confidence intervals for se-
lected statistics. For each statistic, the difference between models is computed for every run and resampled 10, 000 times with replacement.
Confidence intervals, centred around the median of the bootstrap distribution, are shown at the 80%, 90%, and 95% levels. IQR stands for
interquartile range, P25 and P75 stand for the 25th and 75th percentiles, respectively.
Results show that releasing the buffer in downturns improves the lower (riskier) tail of real credit
growth, by shifting it upward relative to the TIP-buffer model. The 25th percentile of real credit growth
is approximately 2 percentage points (p.p.) higher (equivalent to a 15.7% improvement in the lower tail).
The IQR is about 2.7 p.p. narrower (equivalent to a 12.1% reduction), indicating lower volatility in real
credit growth in downturns. Finally, the probability mass in the riskier lower tail is reduced. These
notable economic effects are statistically significant at conventional confidence levels. Taken together,
our results suggest that the TVP regime delivers more stable credit conditions when the economy is
under stress, consistent with the intended objectives of the policy.
Household and firm default rates also improve under a releasable buffer. Figure 7 presents the same
set of results for default rates by borrower segment, with panels A and C displaying the distributions
and panels B and D reporting confidence intervals for the differences between the TIP-buffer and TVP
models. The release of the buffer reduces default rates in the upper riskier tail of the distribution
by 0.7 p.p. for firms and 1.2 p.p. for households. However, this reduction is statistically significant
only at the 80% confidence level for firms, whereas it is statistically significant across all confidence
levels for households. In our model, the effectiveness of a releasable buffer in mitigating credit risk is
30

more robust in the household sector. The more muted response among firms reflects two offsetting
forces. While the buffer release supports loan demand and helps reduce firm closures in the model, it
also allows firms to obtain additional financing, raising leverage and increasing their vulnerability in
subsequent periods. As a result, the net improvement in firm-sector default risk is more limited, though
importantly, it does not worsen. As for volatility, the interquartile range of firm default rates remains
broadly unchanged under the TVP model relative to the TIP-buffer model, whereas households exhibit
a statistically significant reduction. Finally, the likelihood of extremely high default rates declines in
both sectors in the presence of a releasable buffer, with the effect again stronger for households.
Figure 7: Firms and household default rates in downturns: TIP-buffer vs TVP models
TIP-buffer modelTVP model0
5
10
15
20
25Per cent
(A) Distributions - Firms
IQR P25 Median P75-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
0.2Percentage points
Confidence level:95%90%80% (B) Confidence intervals - Firms
TIP-buffer modelTVP model0
5
10
15
20
25Per cent
(C) Distributions - Households
IQR P25 Median P75-1.4
-1.2
-1
-0.8
-0.6
-0.4
-0.2
0
Percentage points
Confidence level:95%90%80% (D) Confidence intervals - Households
Note: See the notes to Figure 6 for details on the distributions and confidence intervals.
Buffer release during downturns supports the economy without compromising banking system re-
silience. Reflecting the improvement in the loan portfolio’s risk profile, the upper tail of the bank loss
31

distribution declines by 0.9 percentage points relative to the TIP-buffer model (see Figure 8), corre-
sponding to a reduction of 4.8%. This indicates a reduced likelihood of very large bank losses during
downturns, mitigating the potential for negative spillovers from the banking system to the real econ-
omy that could exacerbate downturns. This decline is statistically significant across all conventional
confidence levels. Although the interquartile range is only modestly narrower and not statistically sig-
nificant, it still points to slightly more stable loss dynamics when the buffer is released. Overall, these
findings suggest that expanding credit availability via the release of the buffer in downturns to support
the economy does not exacerbate banks’ default risk.
Capital injections become smaller and less frequent under a releasable buffer, indicating greater
banking-system resilience during downturns. To complement the analysis on bank losses, Figure 9
shows the frequency of capital injections during economic downturns, disaggregated by the number
of banks receiving support. An x-axis value of zero indicates that no bank required a capital injection,
which means that all banks remained solvent. The release of capital buffers is associated with a lower
incidence of interventions relative to a regime with time-invariant requirements. When capital injec-
tions do occur, they typically involve a smaller share of the banking sector under the TVP model. In
the latter model, most downturn periods require support for only one or two banks, whereas under the
TIP-buffer regime, interventions commonly span from one up to three banks.
Figure 8: Bank losses in downturns: TIP-buffer and TVP models
TIP-buffer modelTVP model0
10
20
30Per cent
(A) Distributions
IQR P25 Median P75-1.4
-1.2
-1
-0.8
-0.6
-0.4
-0.2
0
0.2Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: Bank losses are measured as the product of default rates and loss-given-default for firms and households. See the notes to Figure 6 for details
on the distributions and confidence intervals.
Figure 10 further shows that the size of interventions is also lower when a releasable buffer is in
place. The upper percentile of the distribution of capital injections under the TVP model is 1.2 p.p.
32

(16.3%) below that of the TIP-buffer model, implying that sizeable interventions by the central bank
are rarer when buffers can be released. This suggests that the banking system is more capable of with-
standing economic stress under the TVP regime, as the buffer release provides additional credit to firms,
reducing closures, and supporting income by preventing a rise in unemployment. The improvement in
the size of capital injections is statistically significant.
Figure 9: Frequency of capital injections in downturns: TIP-buffer vs TVP models
0 1 2 3 4 5Number of banks
0
5
10
15
20
25
30
35Per cent
TIP bufferTVP
Note: Capital injections refer exclusively to interventions aimed at preventing bank
defaults by restoring banks’ capital ratios above the regulatory minimum. An x-axis
value of zero indicates that no bank required a capital injection to remain solvent.
Figure 10: Capital injections in downturns: TIP-buffer vs TVP models
TIP-buffer modelTVP model0
5
10
15
20
25
30
35
40
45
50
55Per cent
(A) Distributions
IQR P25 Median P75-1.6
-1.4
-1.2
-1
-0.8
-0.6
-0.4
-0.2
0
Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: Capital injections refer exclusively to interventions aimed at preventing bank defaults by restoring banks’ capital ratios above regulatory
minimum. Capital injections are expressed as a percentage of output. See the notes to Figure 6 for details on the distributions and confidence
intervals
In addition to the main variables analysed, we also find modest improvements in other macroeco-
nomic outcomes when the buffer is released in a downturn, including a slight downward shift in the
33

median and lower quartile of unemployment and a reduction of downside risks (riskier tail) to house
price growth. Additional evidence on these variables is reported in Appendix B. These effects are either
economically small or, in the case of house prices, should be interpreted cautiously given the challenges
in matching the empirical inflation level.
5.3 Assessing the costs of a releasable buffer in upturns
Tail costs associated with buffer accumulation, if present, would materialise during economic upturns.
The second policy experiment evaluates the potential tail costs associated with building a releasable
capital buffer, which may emerge during economic upturns when such buffers are typically accumu-
lated. To investigate these costs, we compare the distribution of simulated variables under a TIP model
with only the minimum capital requirement to that under the TVP model used in the first policy exper-
iment. Figure 11 illustrates the two capital regimes used. Although capital requirements differ between
the two models at the peak of the credit cycle, both begin each upturn with identical requirements.
This ensures that any divergence in outcomes during the accumulation phase can be attributed to the
build-up of a releasable buffer. The dividend payout rule remains the same as in the downturn analysis,
ensuring comparability across policy regimes.
Figure 11: Components of capital ratios in the TIP and TVP models
Note: The solid outline box denotes the minimum capital requirement of 8%. In the TVP
model (right capital stack), the dashed outline indicates the time-varying releasable buffer,
which can reach up to 2.5%. The dotted outline box represents capital held in excess of the
total requirement (minimum requirement plus the buffer, if applicable).
Buffer accumulation during economic upturns does not materially alter credit dynamics. Panel A
of Figure 12 displays the distributions of real credit growth during upturns for both the TIP and TVP
34

models, while Panel B reports the confidence intervals for the differences in key distributional statistics.
Apart from the applicable capital requirements in the TIP model, these results draw on the same model
simulations used in the first policy experiment. Relative to the TIP regime, the distribution of real credit
growth under the TVP model remains broadly unchanged. Nonetheless, there is a mild improvement
in the lower risky tail of the distribution, and some reduction in the incidence of extreme outcomes.
These findings suggest that the presence of a releasable buffer does not constrain credit growth during
economic upturns. The underlying mechanism is that the reduction in credit supply, triggered only
during periods of unusually strong credit growth within upturns, is not large enough to impede the
banking system from meeting aggregate credit demand.
Figure 12: Real credit growth in upturns: TIP vs TVP models
TIP modelTVP model-60
-40
-20
0
20
40
60Per cent
(A) Distributions
IQR P25 Median P75-1
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: See the notes to Figure 6 for details on the distributions and confidence intervals.
Default-risk dynamics in expansions show no evidence of tail costs from buffer accumulation, with
tail improvements for firms and no meaningful effects for households. Panel A of Figure 13 shows an
improvement in the upper tail of firm default rate, indicating that worst-case default rates are lower
under the TVP model than under the TIP model. This reduction is statistically significant (see panel B).
Two mechanisms drive this result. First, as banks accumulate the releasable buffer, they moderate credit
supply relative to the TIP model. Second, this reduction occurs under a risk-based allocation rule that
prioritises lending to less-leveraged firms, thereby limiting credit to more vulnerable, highly leveraged
firms, more likely to default in future. By curbing credit to these riskier borrowers, the overall risk
profile of the credit portfolio improves, resulting in a lower upper tail firm default rates and reduced
volatility. In contrast, the distributions of household default rate remain largely unchanged (see panels
C and D in Figure 13).
35

Figure 13: Firm and household default rate in upturns: TIP vs TVP models
TIP modelTVP model0
5
10
15
20
25Per cent
(A) Distributions - Firms
IQR P25 Median P75
-1.2
-1
-0.8
-0.6
-0.4
-0.2
0
Percentage points
Confidence level:95%90%80% (B) Confidence intervals - Firms
TIP modelTVP model0
5
10
15
20
25Per cent
(C) Distributions - Households
IQR P25 Median P75-0.2
-0.15
-0.1
-0.05
0
0.05
0.1
0.15
0.2Percentage points
Confidence level:95%90%80% (D) Confidence intervals - Households
Note: See the notes to Figure 6 for details on the distributions and confidence intervals.
Finally, the accumulation of a releasable capital buffer during expansions does not materially change
the distribution of bank losses (see Figure 14). Nevertheless, there is a statistically significant reduction
in the upper tail and volatility, consistent with the improvement in firm-sector default risk. Overall,
these results indicate that the resilience of the banking system is not negatively affected by the building
up of the buffer. This pattern also carries over to broader macroeconomic outcomes. The unemployment
rate is broadly unchanged to slightly improved under the TVP regime, while house price growth shows
limited differences across most of the distribution, with some evidence of stronger growth in favourable
states. Further results are reported in Appendix B.
36

Figure 14: Bank losses in upturns: TIP vs TVP models
TIP modelTVP model0
10
20
30Per cent
(A) Distributions
IQR P25 Median P75
-1.2
-1
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: Bank losses are expressed as the default rate times loss given default of firms and households. See the notes to Figure 6 for details on the
distributions and confidence intervals.
5.4 Assessing the effects of a releasable buffer on credit cycle dynamics
Releasing the buffer reduces the median duration and modestly dampens the amplitude of the credit
cycle. The effects are particularly pronounced during contractions, which become notably shorter in
duration and exhibit a decline in amplitude. Having assessed the state-contingent tail costs and benefits,
we now evaluate the impact of a releasable buffer policy on the duration and amplitude of the credit
cycle. To do so, we apply the turning point methodology as in Drehmann et al. (2012) to identify
medium-term peaks and troughs in our simulated credit series. Table 5 shows the median duration
and amplitude of the credit cycle during both phases of the credit cycle (expansions and contractions)
across the TIP and TVP regimes. 31 Consistent with the empirical evidence, the contraction phase in
the credit cycle is significantly shorter than the expansion phase in both models. More importantly, the
credit cycle under the TVP model shows a notably shorter median contraction by two quarters relative
to the TIP model, while the expansion phase shortens only marginally (by less than one quarter). As a
result, the overall median cycle duration is slightly lower under the TVP regime. The amplitude of both
expansions and contractions also declines, although these effects appear modest and similar between
cyclical phases.
31Duration and amplitude in expansions is measured from trough to peak and in contractions from peak to trough.
37

Table 5: Turning point analysis of simulated credit series
Median duration Median amplitude
Expansion Contraction Expansion Contraction
Real credit – TIP model 13.8 4.0 1.5 -0.8
Real credit – TVP model 13.6 3.5 1.4 -0.7
Difference (TVP-TIP) -0.2 -0.5 -0.1 0.1
Note: The turning point methodology of Drehmann et al. (2012) is applied to the simulated log level of real credit
to identify medium-term credit cycles. Both the TIP and TVP models are simulated for 8, 000 monthly periods.
Peaks and troughs are identified based on the following rules: a) window length 9 quarters (27 months) with a
peak (trough) identified if the change in the variable is positive (negative) at predetermined lags and leads, b)
the minimum length of the cycle is set to 5 years (60 months) and that of each phase (expansion/contraction)
to 2 quarters (6 months). Manual adjustment was occasionally needed, with the additional application of the
Christiano-Fitzgerald bandpass filter serving as complementary analysis (see Figure 15). Cycle duration is mea-
sured in years and amplitude in percent changes.
Figure 15 complements the results in Table 5 by providing a visual representation of the effects of a
releasable buffer on credit cycle dynamics. The left panel aligns representative peaks, identified using
the turning point analysis, from one TIP cycle and one TVP cycle. This comparison helps to identify
that the contraction phase is notably shorter under the releasable buffer approach. The right panel
plots the Christiano–Fitzgerald filtered credit cycles for one selected cycle episode in each regime. 32
The comparison shows that the amplitude of the credit cycle is modestly lower under the TVP model
relative to the TIP model, supporting the earlier finding.
Figure 15: Cycle windows
(A) Turning point approach
 (B) Frequency-based approach
Note: Panel A aligns representative peaks, identified using the turning point methodology, for one TIP cycle and one TVP cycle. Panel
B presents the Christiano–Fitzgerald filtered credit cycles for a selected episode under each regime. The filter is applied to the annual
growth rate of real credit, retaining cycles with a duration between 32 and 120 quarters (or, equivalently, between 96 and 360 months).
32The turning-point approach and the Christiano–Fitzgerald (CF) filter are employed as complementary methods for ex-
tracting the medium-term credit cycle, following the practice in Drehmann et al. (2012).
38

6 Conclusion
This paper introduces the DeTail agent-based (ABM) framework to assess macroprudential policies.
The economy features heterogeneous firms, households, banks, and a single central bank interact-
ing across production, labour, consumption, housing, and credit markets. These interactions generate
a credit-driven macroeconomy that endogenously generates standard cyclical dynamics and is suit-
able for analysing macroprudential policies. The model extends the stock-flow consistent agent-based
framework of Gross (2022) in three significant directions by introducing a housing market and mort-
gage lending, multiple banks subject to risk-based capital requirements, including both minimum cap-
ital requirements and buffers, and a central bank. An essential strength of our ABM framework is the
simulation of full distributions of key variables of interest based on heterogeneous agent interaction.
We use the DeTail framework to analyse the state-contingent tail effects of a releasable macropru-
dential capital buffer. A first policy experiment isolates the tail benefits of buffer release when economic
conditions deteriorate, while the second assesses the potential tail costs associated with buffer accumu-
lation during upturns. In both experiments, we compare the simulated distributions of key variables,
such as credit growth, borrower-segment default rates, and bank losses, under a fixed capital require-
ment regime and under a regime with time-varying capital requirements.
We find that releasing the macroprudential capital buffer provides clear tail benefits during down-
turns. When economic conditions deteriorate, easing macroprudential capital requirements helps pre-
serve credit supply and reduces the volatility of credit growth. This results in significantly better
outcomes: severe credit contractions are less pronounced, and the upper (riskier) tails of firm and
household default rate distributions decrease. Importantly, these gains are achieved without weaken-
ing banking sector resilience. We also find that building-up macroprudential buffers during upturns
does not generate significant costs. The distribution of credit growth remains effectively unchanged
when banks are required to build up capital during upturns, indicating that tighter requirements do not
significantly constrain lending in good times. Moreover, by curbing credit to the riskiest borrowers,
higher requirements yield slight improvements in the upper tail of firm default rate. We also find no
adverse impact on bank loss distribution. Overall, our policy experiments confirm that introducing
a releasable buffer in the capital mix supports the continued provision of credit during downturns at
little cost during upturns and without compromising banking system resilience. Consistent with this,
we also find that a releasable buffer improves the dynamics of the credit cycle by reducing its median
duration and modestly dampening its amplitude.
39

Our ABM approach is directly relevant for systemic risk analysis and macroprudential policies,
which are particularly concerned with tail risks. The development and application of DeTail com-
plement the existing literature on the costs and benefits of releasable buffers by generating cross-
section, time-varying distributions of key variables, supporting a more granular, state-contingent, and
tail-focused assessment of macroprudential policy effectiveness. Taken together, these results provide
strong support for the timely build-up and active use of a releasable capital buffer throughout the cy-
cle. Our results show that macroprudential capital buffers help to contain the most adverse outcomes
of credit cycles without creating drag during upturns or weakening banking system resilience, fully
aligning with the policy’s intended objectives.
Additional model extensions, such as the inclusion of a positive neutral rate rule for the CCyB
and other (sectoral) macroprudential buffers, including more detailed calibrations to reflect potential
specificities at the country level are left for future research.
40

References
Alexandre, M. and Lima, G. T. (2020). Combining monetary policy and prudential regulation: an agent-
based modeling approach. Journal of Economic Interaction and Coordination , 15(2):385–411.
Axtell, R., Farmer, D., Geanakoplos, J., Howitt, P., Carrella, E., Conlee, B., Goldstein, J., Hendrey, M.,
Kalikman, P., Masad, D., Palmer, N., and Yang, C.-Y. (2014). An agent-based model of the housing
market bubble in metropolitan Washington, DC. In Deutsche Bundesbank’s Spring Conference on
Housing markets and the macroeconomy: Challenges for monetary policy and financial stability , pages
5–6, Frankfurt am Main, Germany.
Axtell, R. L. and Farmer, J. D. (2025). Agent-based modeling in economics and finance: Past, present,
and future. Journal of Economic Literature , 63(1):197–287.
Azzone, M. and Pirovano, M. (2024). Aim, focus, shoot. The choice of appropriate and effective macro-
prudential instruments. Working Paper Series 2979, European Central Bank.
Bardoscia, M., Carro, A., Hinterschweiger, M., Napoletano, M., Popoyan, L., Roventini, A., and Uluc, A.
(2025). The impact of prudential regulation on the uk housing market and economy: Insights from
an agent-based model. Journal of Economic Behavior & Organization , 229:106839.
Basel Committee on Banking Supervision (2022). Buffer usability and cyclicality in the Basel framework.
Implementation report, Bank for International Settlements.
Borsos, A., Carro, A., Glielmo, A., Hinterschweiger, M., Kaszowska-Mojsa, J., and Uluc, A. (2025). Agent-
based modeling at central banks: recent developments and new challenges. Bank of England Staff
Working Paper 1122, Bank of England.
Bush, O., Hüser, A.-C., Lowe, P., Sowerbutts, R., and Waldron, M. (2025). Review of the analytical
framework supporting financial policy at the Bank of England. Financial Stability Paper 52, Bank of
England.
Carro, A. (2023). Taming the housing roller coaster: The impact of macroprudential policy on the house
price cycle. Journal of Economic Dynamics and Control , 156:104753.
Carro, A., Hinterschweiger, M., Uluc, A., and Farmer, J. D. (2022). Heterogeneous effects and spillovers
of macroprudential policy in an agent-based model of the UK housing market. Bank of England
working papers 976, Bank of England.
41

Catapano, G. (2023). Borrower-based measures analysis via a new agent-based model of the Italian real
estate sector. Occasional Papers 822, Banca d’Italia, Rome.
Catullo, E., Giri, F., and Gallegati, M. (2021). Macro- and microprudential policies: Sweet and lowdown
in a credit network agent-based model. Macroeconomic Dynamics, 25(5):1227–1246.
Clerc, L., Derviz, A., Mendicino, C., Moyen, S., Nikolov, K., Stracca, L., Suarez, J., and Vardoulakis, A. P.
(2015). Capital Regulation in a Macroeconomic Model with Three Layers of Default. International
Journal of Central Banking , 11(3):9–63.
Cokayne, G. (2019). The effects of macroprudential policies on house price cycles in an agent-based
model of the Danish housing market. Working Paper 138, Danmarks Nationalbank.
Couaillier, C., Lo Duca, M., Reghezza, A., and Rodriguez D’Acri, C. (2025). Caution: Do not cross!
distance to regulatory capital buffers and corporate lending in a downturn. Journal of Money, Credit
and Banking, 57(4):833–862.
Detken, C., Hempell, H. S., and Pirovano, M. (2025). Macroprudential and monetary policy interaction:
the role of early activation of the countercyclical capital buffer. European Central Bank Macropru-
dential Bulletin 31, European Central Bank.
Dosi, G. and Roventini, A. (2025). Agent-based macroeconomics: The Schumpeter meeting Keynes models .
Cambridge: Cambridge University Press.
Drehmann, M., Borio, C., and Tsatsaronis, K. (2012). Characterising the financial cycle: don’t lose sight
of the medium term! BIS Working Papers 380, Bank for International Settlements.
Durante, E., Rusnak, M., and Tereanu, E. (2025). A decade of borrower-based measures in the banking
union. Macroprudential Bulletin 29, European Central Bank.
European Banking Authority (2025). EBA Report: Results from the 2024 Credit Risk Benchmarking
Exercise. Accessed: 5 January 2026.
European Central Bank (2022). Enhancing macroprudential space in the banking union . Report from
the drafting team of the steering committee of the macroprudential forum, European Central Bank.
European Central Bank (2025). ECB Banking Supervision Press Release on banking statistics on signif-
icant institutions for the third quarter of 2025. Accessed: 5 January 2026.
42

European Central Bank - European Systemic Risk Board (2026). Report of the ECB-ESRB workstream
on buffer usability. Technical report, European Central Bank - European Systemic Risk Board.
Geanakoplos, J., Axtell, R., Farmer, J. D., Howitt, P., Conlee, B., Goldstein, J., Hendrey, M., Palmer,
N. M., and Yang, C.-Y. (2012). Getting at systemic risk via an agent-based model of the housing
market. American Economic Review, 102(3):53–58.
Gross, M. (2022). Beautiful cycles: A theory and a model implying a curious role for interest. Economic
Modelling, 106:105678.
Haldane, A. G. and Turrell, A. E. (2018). An interdisciplinary model for macroeconomics. Oxford Review
of Economic Policy , 34(1-2):219–251.
Herrera, L., Pirovano, M., and Scalone, V. (2025). From risk to buffer: Calibrating the positive neutral
CCyB rate in the euro area. ECB Working Paper 3075, European Central Bank.
Ivashina, V., Kalemli-Özcan, S., Laeven, L., and Müller, K. (2024). Corporate debt, boom-bust cycles, and
financial crises. NBER Working Papers 32225, National Bureau of Economic Research, Inc.
Krug, S. and Wohltmann, H.-W. (2016). Shadow banking, financial regulation and animal spirits: An ace
approach. Economics Working Papers 2016-08, Christian-Albrechts-University of Kiel, Department
of Economics.
Laliotis, D., Buesa, A., Leber, M., and Población, J. (2020). An agent-based model for the assessment of
LTV caps. Quantitative Finance, 20(10):1721–1748.
Lang, J. H. and Menno, D. (2025). The state-dependent impact of changes in bank capital requirements.
Journal of Banking & Finance , 176(C).
Mathur, A., Naylor, M., and Rajan, A. (2023). Useful, usable, and used? Buffer usability during the
Covid-19 crisis. Bank of England Working Papers 1011, Bank of England.
Mérő, B., Borsos, A., Hosszú, Z., Oláh, Z., and Vágó, N. (2023). A high-resolution, data-driven agent-
based model of the housing market. Journal of Economic Dynamics and Control , 155(C).
Poledna, S., Miess, M. G., Hommes, C., and Rabitsch, K. (2023). Economic forecasting with an agent-
based model. European Economic Review, 151(C):None.
43

Popoyan, L., Napoletano, M., and Roventini, A. (2017). Taming macroeconomic instability: Monetary
and macro-prudential policy interactions in an agent-based model. Journal of Economic Behavior &
Organization, 134(C):117–140.
Popoyan, L., Napoletano, M., and Roventini, A. (2020). Winter is possibly not coming: Mitigating
financial instability in an agent-based model with interbank market. Journal of Economic Dynamics
and Control, 117.
Raberto, M., Nathanael, R. C., and Ozel, B. (2017). Credit-driven business cycles in an agent-based macro
model. In Theory and Method of Evolutionary Political Economy , pages 11–30. Routledge, London, 1st
edition.
Riccetti, L., Russo, A., and Gallegati, M. (2022). Firm-bank credit network, business cycle and macro-
prudential policy. Journal of Economic Interaction and Coordination , 17(2):475–499.
Stock, J. H. and Watson, M. W. (1999). Forecasting inflation. Journal of Monetary Economics , 44(2):293–
335.
Tarne, R., Bezemer, D., and Theobald, T. (2022). The effect of borrower-specific loan-to-value policies
on household debt, wealth inequality and consumption volatility: An agent-based analysis. Journal
of Economic Dynamics and Control , 144:104526.
Van der Hoog, S. and Dawid, H. (2019). Bubbles, crashes, and the financial cycle: The impact of banking
regulation on deep recessions. Macroeconomic Dynamics, 23(3):1205–1246.
44

A Additional model details
Household behaviour
Consumption smoothing. When a household sells its house, the resulting increase in its deposit
balance represents a temporary positive wealth shock. To avoid an unrealistically sharp rise in con-
sumption, the model imposes a consumption-smoothing rule instead of the standard MPC rule to this
unusually large inflow. Specifically, household consumption after a house sale is given by:
𝑐ℎ,𝑡 = (1 + 𝑣) × ˜𝐶𝑡 −1
where ˜𝐶𝑡 −1 represents the economy-wide average consumption level in period𝑡 −1 and 𝑣 is the smooth-
ing parameter. Under this rule, the additional deposits from the sale are gradually drawn down, with
the duration of the drawdown determined by the choice of 𝑣. In the baseline parametrisation (see Ap-
pendix C), this implies full depletion after 60 periods, at which point the standard consumption rule
is resumed. This behaviour is consistent with the permanent income hypothesis: households treat the
sale proceeds as transitory wealth and smooth consumption accordingly rather than consuming the
full amount immediately.
Bank behaviour
Interbank payments. When a household whose deposit account is held at bank 𝑏1 purchases goods
from a firm banking with bank𝑏2, the payment associated with this consumption flow is settled through
an interbank reserve transfer. The settlement occurs through the central bank: an equivalent amount
of reserves is debited from bank 𝑏1’s reserve account and credited to bank 𝑏2 reserve account. Although
firms and households do not change banks, payments across banks cause interbank reserve transfers
managed by the central bank’s clearing mechanism (see subsection 3.5 for details on the central bank’s
role in the model).
Capital injections to satisfy minimum credit supply. The required capital injection for bank 𝑏
in period 𝑡, denoted 𝐶𝐼𝑏,𝑡 , is the amount needed to restore compliance with capital requirements after
extending the additional firm loans implied by the minimum credit supply rule. Formally,
𝐶𝐼𝑏,𝑡 =

𝜎 × 𝑟𝑤 𝐹 × 𝑊 𝐵𝑏,𝑡 + 𝑅𝑊 𝐴𝑏,𝑡

𝐶𝐴𝑅 req
𝑡 − 𝑁𝑊𝑏,𝑡 .
where, 𝑟𝑤 𝐹 is the risk weight assigned to firm loans in the capital requirements framework. The first
term in parentheses represents the risk-weighted assets (RW A) associated with the additional required
45

loans, while the second term captures the bank’s existing RW A. Multiplying their sum by the regulatory
capital ratio yields the total capital required to support the combined portfolio, and subtracting current
net worth gives the resulting capital shortfall. A capital injection immediately increases bank equity
and expands lending capacity. Following an injection, the bank’s available credit supply is recalculated
using the higher capital position.
Consolidation of multiple firm loans. When a firm with an existing loan takes a new working-
capital loan, the model combines the two into a single composite loan for the purposes of interest and
maturity calculations. The composite interest rate, 𝐼𝑓 ,𝑡, and remaining maturity, 𝐷 𝑓 ,𝑡, are calculated as
loan-size-weighted averages of the previous and new loan terms:
𝐼𝑓 ,𝑡 = 𝐿𝑓 ,𝑡 −1 · 𝐼𝑓 ,𝑡 −1 + 𝑙𝑓 ,𝑡 · 𝑖𝐹
𝑡
𝐿𝑓 ,𝑡 −1 + 𝑙𝑓 ,𝑡
𝐷 𝑓 ,𝑡 = 𝐿𝑓 ,𝑡 −1 · 𝐷 𝑓 ,𝑡 −1 + 𝑙𝑓 ,𝑡 · 𝑑𝑓 ,𝑡
𝐿𝑓 ,𝑡 −1 + 𝑙𝑓 ,𝑡
If the firm has no prior loan, 𝐿𝑓 ,𝑡 −1 = 0, the composite loan simply inherits the terms of the new loan.
Loan pricing rule. Banks price loans based on expected segment-level credit risk and funding costs.
At origination, bank 𝑏 sets the interest rate for borrower segment 𝑗 ∈ { 𝐻, 𝐹 } so that the expected return
on the loan equals the expected cost of funds: 33
𝑃𝐷 𝑗
𝑡 × 𝐿𝐺𝐷 𝑗
𝑡 +

1 − 𝑃𝐷 𝑗
𝑡
 
𝜇 − 𝑖𝑀
𝑡

=

1 − 𝑃𝐷 𝑗
𝑡

𝑖 𝑗
𝑡 .
which yields
𝑖 𝑗
𝑡 = 𝜇 + 𝑖𝑀
𝑡 + 𝑃𝐷 𝑗
𝑡 × 𝐿𝐺𝐷 𝑗
𝑡
1 − 𝑃𝐷 𝑗
𝑡
, 𝑗 ∈ { 𝐻, 𝐹 }.
Credit risk expectations. The time-varying credit risk premium in the loan pricing rule is a function
of the bank’s expectations about aggregate probability of default ( 𝑃𝐷 𝑗
𝑡 ) and loss given default ( 𝐿𝐺𝐷 𝑗
𝑡 )
within each borrower segment. Banks update 𝑃𝐷 𝑗
𝑡 based on observed default flows:
𝑃𝐷 𝑗
𝑡 =
Í
𝑗 DefaultFlow𝑗,𝑡 −1
1 − 𝐿 𝑗
𝑡
This assumes that the best estimate for the likelihood a loan will default is the proportion that
33Both the probability of default (PD) and loss given default (LGD) used in the loan pricing rule are smoothed using a
15-period moving average, following Gross (2022). This approach mitigates short-term volatility and ensures more stable
estimates for loan pricing.
46

defaulted last period adjusted for the loan portfolio. Expected loss given default differs by loan segment.
For firm loans:
𝐿𝐺𝐷 𝐹
𝑡 =
Í
𝑘 ∈𝐹
 DefaultFlow𝑘,𝑡 −1 − seize𝑘,𝑡

Í
𝑘 ∈𝐹 DefaultFlow𝑘,𝑡 −1
reflecting deposit seizure upon firm default. For household mortgages, 𝐿𝐺𝐷 𝐻
𝑡 = 1, as deposits are not
seized to cover losses.
Setting the interest rate based on the aggregate credit risk at borrower segment level, rather than
using the borrower’s specific credit risk, introduces a friction in the model that reflects either the cost
of monitoring for banks or informational asymmetries faced by banks.
Dividend distribution mechanism. The target capital ratio depends on the capital requirements
regime introduced in subsection 3.5. Under time-invariant capital requirements, the target does not
vary over the credit cycle and is set equal or above the requirement. Under time-varying requirements,
the target rises and falls with the buffer, ensuring banks avoid breaching requirements throughout the
cycle.
Dividends are distributed equally among all households that are depositors of that bank. Each receives
𝑑𝑖𝑣 𝑏,𝑡
𝑛𝐻
as dividend income. Dividend income increases households’ deposit balances and is used for debt
servicing or future consumption but does not affect current consumption (see subsection 3.3).
Debt servicing. At the end of each period, every borrower calculates a fixed annuity payment
𝑎 𝑗,𝑡 = 𝑎𝐼
𝑗,𝑡 + 𝑎𝐷
𝑗,𝑡 , 𝑗 ∈ { 𝑓 , ℎ},
where 𝑎𝐼
𝑗,𝑡 and 𝑎𝐷
𝑗,𝑡 stand for the interest component of the payment and for the principal amortisation
component, respectively. The annuity payment is given by the standard instalment-loan formula:
𝑎 𝑗,𝑡 = 𝐷 𝑗,𝑡 × 𝐼 𝑗,𝑡
 1 + 𝐼 𝑗,𝑡
𝐷 𝑗,𝑡
 1 + 𝐼 𝑗,𝑡
𝐷 𝑗,𝑡 − 1
, 𝑗 ∈ { 𝑓 , ℎ}.
Depending on the borrower’s available resources, 𝑀𝑗,𝑡 , one of three cases applies:
• Regular amortisation: If the borrower has sufficient deposits to cover the full annuity, 𝑀𝑗,𝑡 ≥ 𝑎 𝑗,𝑡 ,
it pays the full amount.
• Interest-only payment: If the borrower’s deposits are sufficient to cover the interest but not the
full annuity, i.e. 𝑎 𝑗,𝑡 ≥ 𝑀𝑗,𝑡 ≥ 𝑎𝐼
𝑗,𝑡 , the borrower pays interest only and the unpaid principal is
rolled over and added to next period’s obligations.
47

• Default: If the borrower cannot cover the interest due, i.e. 𝑎 𝑗,𝑡 ≥ 𝑎𝐼
𝑗,𝑡 > 𝑀𝑗,𝑡 , then it defaults on
the loan. Because partial interest payments are not allowed, inability to cover interest triggers
immediate default on the entire outstanding loan.
Central bank and capital requirements framework
Asset classes and risk weights. Reserves are treated as risk-free and therefore carry a risk weight of
zero (𝑟𝑤 𝑅 = 0). Mortgages are assigned a risk weight of 35% (𝑟𝑤 𝐻 = 35%), reflecting the presence of
collateral. Loans to firms are considered riskier and receive a risk weight of 100% (𝑟𝑤 𝐹 = 100%). These
choices follow the standardised approach to credit risk under Basel II. As a result, the total RW As of
bank 𝑏 in period 𝑡 are given by:
𝑅𝑊 𝐴𝑏,𝑡 = 𝑟𝑤 𝑅𝑅𝑏,𝑡 + 𝑟𝑤 𝐻 𝐿𝐻
𝑏,𝑡 + 𝑟𝑤 𝐹 𝐿𝐹
𝑏,𝑡 .
B Additional results
Figure 16 illustrates the impact of buffer releases during downturns on the distribution of the unem-
ployment rate. Relative to the TIP-buffer model, the TVP model yields a mild but statistically significant
downward shift in the median and lower quartile of unemployment. Despite being economically mod-
est, these improvements reflect the transmission mechanism embedded in the model. Releasing the
buffer supports lending to firms during periods of stress, thereby reducing firm default rate, as docu-
mented in the main text. As for other macroeconomic variables, the TVP regime also delivers significant
improvements in the lower tail of the distribution of house price growth, indicating that house prices
fall by less during downturns when the buffer is released. However, because house prices in the current
parametrisation of the model do not closely match the empirical data, given its indirect link to inflation,
we treat these results as illustrative and do not report them.
Figure 17 shows the results for the unemployment rate during upturns. Relative to the TIP model,
the TVP model yields mild reductions in the median, 75th percentile, and IQR, indicating both lower
and less volatile unemployment outcomes.
While statistically significant, these effects are quantitatively modest, suggesting that the gradual
accumulation of the buffer in the upturn does not materially impair lending to firms. In line with
the broader assessment of upturn dynamics, house price growth shows limited evidence of tail costs
from buffer accumulation. Differences between the TIP and TVP regimes are not statistically signifi-
48

Figure 16: Unemployment rate in downturns: TIP-buffer and TVP models
TIP-buffer modelTVP model0
4
8
12
16Per cent
(A) Distributions
IQR P25 Median P75-0.4
-0.3
-0.2
-0.1
0
0.1
0.2Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: See the notes to Figure 6 for details on the distributions and confidence intervals.
Figure 17: Unemployment rate in upturns: TIP and TVP models
TIP modelTVP model0
4
8
12
16Per cent
(A) Distributions
IQR P25 Median P75
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
Percentage points
Confidence level:95%90%80% (B) Confidence intervals
Note: See the notes to Figure 6 for details on the distributions and confidence intervals.
cant across most of the distribution, although the upper tail is somewhat higher under TVP, reflecting
stronger growth in favourable states rather than increased downside risk.
49

C Table of parameters
Table C.1: Parameter values
Description Parameter Value Source
Number of firms 𝐹 200 Gross (2022)
Number of households 𝐻 20000 Gross (2022)
Number of banks 𝐵 5 Bardoscia et al. (2025)
Inflation pass-through to wages 𝜅 0.9 Calibration
Mortgage loan duration distr. (mean) 𝜇𝐻 5.9 Informed by Durante et al. (2025)
Mortgage loan duration distr. (var) 𝜎𝐻 0.1 Informed by Durante et al. (2025)
Marginal propensity to consume (%) 𝑀𝑃𝐶 80 Calibration
Bank profit margin on loans (%) 𝜇 5 Gross (2022)
Fraction of homeowner households (%) ℎ𝑓 𝑟𝑎𝑐 75 Informed by EU data
Scale parameter of DSTI preference distr. 𝛼 5.4 Informed by EU data
Shape parameter of DSTI preference distr. 𝛽 8.9 Informed by EU data
Lower bound of DSTI preference distr. 𝐿 0.05 Modeller’s choice
Upper bound of DSTI preference distr. 𝑈 0.55 Informed by Durante et al. (2025)
Consumption smoothing (%) 𝑣 5 Calibration
Risk-weight on firm loans (%) 𝑟𝑤 𝐹 100 Basel standards
Risk-weight on mortgage loans (%) 𝑟𝑤 𝐻 35 Basel standards
Risk-weight on reserves (%) 𝑟𝑤 𝑅 0 Basel standards
Firm loans share in credit supply (%) 𝜆 95 Modeller’s choice
Minimum share of credit supply (%) 𝜎 40 Calibration
50

D Data used for economic validation
Table D.2: Variable definitions and data sources
Variable Description Source
Real GDP Quarterly real GDP, seasonally adjusted. EUROSTAT, FRED
Unemployment Monthly unemployment rate. EUROSTAT, FRED
Bank credit Quarterly bank credit to the non-financial private sector. BIS (Credit Statistics)
E Additional information on simulated moments
Table E.3: Simulated moments
Mean Std. Dev. p25 Median p75
Real GDP growth (%, p.a.) 4.2 4.7 1.5 4.3 6.7
Unemployment (%) 2.5 2.6 0.5 1.5 4.0
Real credit growth (%, p.a.) 5.1 14.1 -1.8 6.8 13.9
Default rate – Firms (%) 5.2 4.5 1.2 3.7 8.4
Default rate – Households (%) 3.2 3.0 0.7 2.4 4.7
Note: Std. Dev. stands for standard deviation, p25 and p75 stand for the 25th and 75th percentiles, respectively, p.a.
stands for per year. Real GDP and real credit are measured as annual growth rates. The table shows the average of the
different statistics across 100 independent simulations of the model, each simulating 1, 850 monthly periods with a 350
periods burn-in.
51