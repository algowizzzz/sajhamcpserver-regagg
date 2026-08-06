# Instructions et spécifications pour la transmission en format XML de déclarations par lots

**MODULE 2**

**Le 29 novembre 2010**

**Présente les spécifications ayant trait aux déclarations relatives aux déboursements de casinos (DDC)**

## Sur cette page

1. [**Spécifications des fichiers DDC**](#s1)
   * 1.1 [Configuration des déclarations transmises par lots XML - format de la version 1.0](#s1-1)
   * 1.2 [Configuration détaillée](#s1-2)
     + 1.2.1 [Parties de la déclaration](#s1-2-1)
2. [**Diagramme du schéma**](#s2)
   * 2.1 [Éléments compris dans l'en-tête](#s2-1)
   * 2.2 [Renseignements sur le casino devant déclarer le déboursement](#s2-2)
   * 2.3 [Renseignements sur l'opération](#s2-3)
   * 2.4 [Renseignements sur la personne qui a demandé le déboursement](#s2-4)
   * 2.5 [Renseignements sur le tiers pour le compte de qui le déboursement a été reçu (le cas échéant)](#s2-5)
   * 2.6 [Motif du déboursement](#s2-6)
   * 2.7 [Méthode du déboursement](#s2-7)
   * 2.8 [Éléments compris dans la fin de lot](#s2-8)
3. [Diagramme de production d'une déclaration relative à un déboursement de casino (DDC ou « CDR »)](#s3)

  
  

## 1. Spécifications des fichiers DDC

### 1.1 Configuration des déclarations transmises par lots XML - format de la version 1.0

Les spécifications pour les déclarations relatives à un déboursement de casino (DDC) sont fondées sur le format XML version « 1.0 ». Vous devez donc transmettre des données d'essai en mode opérationnel d'essai (test) pour fins de procédures d'acceptation si vous voulez soumettre des DDC par lots à partir du 28 septembre 2009. Pour de plus amples renseignements sur la transmission des données d'essai en mode opérationnel, veuillez consulter les le Module 1 de ce document de spécifications.

Le détail des spécifications techniques est expliqué dans le reste de ce module.

### 1.2 Configuration détaillée

Les spécifications suivantes définissent le format à utiliser pour produire, au moyen du transfert de fichiers par lots, des DDC (« CDR ») selon le format de lot XML de la version « 1.0 ».

La structure logique d'un fichier de lot contenant des déclarations de type DDC sera comme suit :

Spécifications des fichiers DDC

| CasinoDisbursementReportXmlFile |  |
| ReportSubmissionFileHeader | Section d'en-tête |
| CasinoDisbursementReport | Première déclaration |
| CasinoDisbursementReport | Deuxième déclaration |
| ... (pour chaque déclaration DDC dans le fichier) ... | etc. |
| ReportSubmissionFileTrailer | Section de fermeture |

#### 1.2.1 Parties de la déclaration

Veuillez ne pas inclure les parties d'une déclaration lorsqu'elles ne s'appliquent pas. Cependant, tous les champs compris dans les parties que vous soumettez doivent être inclus, à moins que vous supprimiez une déclaration (comme l'explique le paragraphe 3.3 du Module 1). Pour de plus amples renseignements sur les champs d'une déclaration DDC, reportez-vous à la *Ligne directrice 10A : Déclaration des déboursements de casino à CANAFE par voie électronique.*

Une déclaration DDC ne devrait inclure qu'un seul déboursement, à moins qu'il s'agisse de deux ou plusieurs déboursements de moins de 10 000 $ chacun effectués au cours d'une période de vingt-quatre heures consécutives et totalisant 10 000 $ ou plus.

Le lot au complet sera rejeté si les spécifications ne sont pas suivies.

## 2. Diagramme du schéma

Les éléments du schéma XML pour la DDC sont identifiés dans le diagramme qui suit :

![CDR XML schema](images/Mod2/image001.gif)

### 2.1 Éléments compris dans l'en-tête

L'en-tête de lot doit contenir les renseignements nécessaires pour identifier la personne ou l'institution à l'origine de la transmission. Chaque fichier transmis doit comprendre un seul en-tête de lot. Les éléments suivants de l'en-tête de lot doivent être inclus à la transmission d'un lot.

#### ?xml (Déclaration XML)

Déclaration XML

| Définition : | Cette déclaration principale spécifie la version de XML utilisée. |
| Attributs : | **version**:  fixe : "1.0"  **encodage**:  fixe : "UTF-8" |
| Contraintes : | Obligatoire aux fins de traitement  Un par fichier soumis |
| Exemple : | `<?xml version="1.0" encoding="UTF-8" ?>` |
| Commentaires : | Cet élément doit être **seul** sur la première ligne du fichier. Les numéros de la version et de l'encodage sont fixes pour cette version du schéma. |

#### CasinoDisbursementReportXmlFile (Balise racine)

![CasinoDisbursementReportXmlFile](images/Mod2/image002.jpg)

Balise racine

| Définition : | Cette balise racine renferme les balises parents suivantes :  **ReportSubmissionFileHeader**  **CasinoDisbursementReport**  **ReportSubmissionFileTrailer** |
| Attributs : | **ModelVersionNumber**  fixe : "1.0" |
| Contraintes : | Obligatoire aux fins de traitement  Un par fichier soumis |
| Exemple : | `<CasinoDisbursementReportXmlFile ModelVersionNumber="1.0"> …  </CasinoDisbursementReportXmlFile>` |
| Commentaires : |  |

#### ReportSubmissionFileHeader (En-tête de transmission de déclarations)

![ReportSubmissionFileHeader](images/Mod2/image003.gif)

En-tête de transmission de déclarations

| Définition : | Cet élément parent renferme les renseignements au sujet de la personne ou l'institution à l'origine de la transmission. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **ReportXmlFile** |
| Exemple : | ``` <ReportSubmissionFileHeader>   <SubmitOrganizationNumber>9999999</SubmitOrganizationNumber>   <ExternalFileName>20091010_1101112_CDR.xml</ExternalFileName>   <ReportTypeCode>13</ReportTypeCode>   <OperationModeCode>2</OperationModeCode>   <PkiCertificateNumber>1211379999</PkiCertificateNumber> </ReportSubmissionFileHeader> ``` |
| Commentaires : | Cet élément fournit des renseignements uniques servant à identifier le fichier XML transmis à CANAFE. Ces renseignements serviront de référence dans le message d'accusé de réception qui sera envoyé à la personne ou l'institution à l'origine de la transmission de ce fichier. |

#### SubmitOrganizationNumber (Numéro d'identification de l'organisation)

![SubmitOrganizationNumber](images/Mod2/image004.gif)

Numéro d'identification de l'organisation

| Définition : | Ce numéro d'identification de sept chiffres a été donné par CANAFE au moment de l'inscription de la personne ou l'institution à l'origine de la transmission. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 7 chiffres  Un par **ReportSubmissionFileHeader** |
| Exemple : | `<SubmitOrganizationNumber>9999999</SubmitOrganizationNumber>` |
| Commentaires : |  |

#### ExternalFileName (Désignation de fichier)

![ExternalFileName](images/Mod2/image005.gif)

Désignation de fichier

| Définition : | Ce nom unique doit être fourni par la personne ou l'institution à l'origine de la transmission afin d'identifier chaque fichier transmis par lot. Ce nom servira de référence dans le message d'accusé de réception qui sera envoyé à la personne ou l'institution à l'origine de la transmission de ce fichier. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 80 caractères  Un par **ReportSubmissionFileHeader** |
| Exemple : | `<ExternalFileName>20091010_1101112_CDR.xml </ExternalFileName>` |
| Commentaires : | Le nom du fichier ne doit pas contenir d'espaces ou de traits d'union. |

#### ReportTypeCode (Genre de déclaration)

![ReportTypeCode](images/Mod2/image006.gif)

Genre de déclaration

| Définition : | Ce code sert à identifier le genre de déclaration. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  2 chiffres  Un par **ReportSubmissionFileHeader** |
| Exemple : | `<ReportTypeCode>13</ReportTypeCode>` |
| Commentaires : | Code :  13 - Déclaration relative à un déboursement de casino |

#### OperationModeCode (Mode opérationnel)

![OperationModeCode](images/Mod2/image007.gif)

Mode opérationnel

| Définition : | Ce code est utilisé pour identifier le canal de la transmission du fichier de lot. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **ReportSubmissionFileHeader** |
| Exemple : | `<OperationModeCode>2</OperationModeCode>` |
| Commentaires : | Codes :  2 - Production  1 - Test (essai par l'entremise du canal de formation du logiciel pour la transsmission par lots) |

#### PKICertificateNumber (Numéro de certificat d'ICP)

![PKICertificateNumber](images/Mod2/image008.gif)

Numéro de certificat d'ICP

| Définition : | Ce numéro d'identification set celui du certificat d'ICP que CANAFE a fourni à la personne ou l'institution à l'origine de la transmission. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  10 chiffres  Un par **ReportSubmissionFileHeader** |
| Exemple : | `<PkiCertificateNumber>1211379999</PkiCertificateNumber>` |
| Commentaires : |  |

### 2.2 Renseignements sur le casino devant déclarer le déboursement

#### CasinoDisbursementReport (Déclaration relative à un déboursement de casino)

![CasinoDisbursementReport](images/Mod2/image009.gif)

Déclaration relative à un déboursement de casino

| Définition : | Cette balise parent renferme le contenu de la déclaration. |
| Attributs : | **CasinoDisbursementReportSequenceNumber**  Obligatoire aux fins de traitement  1 à 99999 chiffres  Un par **CasinoDisbursementReport**  **ActionCode**: 1 ¦ 2 ¦ 5  Codes :  1 Ajouter  2 Modifier  5 Supprimer  Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoDisbursementReport** |
| Contraintes : | Obligatoire aux fins de traitement  Un ou plusieurs par **CasinoDisbursementReportXmlFile** |
| Exemple : | `<CasinoDisbursementReport CasinoDisbursementReportSequenceNumber="1" ActionCode="1"> … </CasinoDisbursementReport>` |
| Commentaires : |  |

#### ReportHeader (Partie A)

![ReportHeader](images/Mod2/image010.gif)

ReportHeader (Partie A)

| Définition : | Cet élément parent renferme les renseignements sur le casino devant déclarer le déboursement à CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **CasinoDisbursementReport** |
| Exemple : | ``` <ReportHeader>   <OrganizationNumber>9999999</OrganizationNumber>   <OrganizationReportReferenceIdentifier>Report01  </OrganizationReportReferenceIdentifier>   <TwentyFourHourRuleCode>0</TwentyFourHourRuleCode>   <ReportContactInformation>    <IndividualName>     <Surname>Doe</Surname>     <GivenName>John</GivenName>     <MiddleName>E</MiddleName>    </IndividualName>    <BusinessTelephone>      <TelephoneNumber>905-999-9999</TelephoneNumber>      <TelephoneExtensionNumber>912</TelephoneExtensionNumber>     </BusinessTelephone>    </ReportContactInformation>    <ExternalLocationIdentifier>999999999   </ExternalLocationIdentifier>  </ReportHeader> ``` |
| Commentaires : |  |

#### A2 OrganizationNumber\* (Numéro d'identification de l'entité déclarante\*)

![OrganizationNumber*](images/Mod2/image011.gif)

Numéro d'identification de l'entité déclarante

| Définition : | Ce numéro a été donné au casino par CANAFE lors de l'inscription. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 7 chiffres  Un par **ReportHeader** |
| Exemple : | `<OrganizationNumber>9999999</OrganizationNumber>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A3 OrganizationReportReferenceIdentifier (Numéro de référence de la déclaration de l'entité déclarante)

![OrganizationReportReferenceIdentifier](images/Mod2/image012.gif)

Numéro de référence de la déclaration de l'entité déclarante

| Définition : | Ce numéro de référence distinct est assigné par le casino ou par la personne ou l'institution à l'origine de la transmission de ce fichier pour chaque déclaration transmise à CANAFE de la part du même casino. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 20 caractères  Un par **ReportHeader** |
| Exemple : | `<OrganizationReportReferenceIdentifier>Report01  </OrganizationReportReferenceIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A1 TwentyFourHourRuleCode (Indicateur de règle de 24 heures)

![TwentyFourHourRuleCode](images/Mod2/image013.gif)

Indicateur de règle de 24 heures

| Définition : | Ce code est utilisé pour indiquer que la déclaration vise un déboursement de moins de 10 000 $ faisant partie d'un groupe de deux déboursements ou plus de moins de 10 000 $ chacun effectués au cours d'une période de 24 heures consécutives et totalisant 10 000 $ ou plus. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **ReportHeader** |
| Exemple : | `<TwentyFourHourRuleCode>0</TwentyFourHourRuleCode>` |
| Commentaires : | Codes :  0 La règle de 24 heures ne s'applique pas  1 La règle de 24 heures s'applique  Veuillez inclure un élément **CasinoTransaction** distinct, et toutes les parties qui s'appliquent, pour chaque déboursement dans la période de 24 heures en question.  Cet élément ne doit pas être vide. |

#### ReportContactInformation (Avec qui CANAFE peut-il communiquer au sujet de cette déclaration?)

![ReportContactInformation](images/Mod2/image014.gif)

Avec qui CANAFE peut-il communiquer au sujet de cette déclaration?

| Définition : | Cet élément parent renferme les renseignements sur la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **ReportHeader** |
| Exemple : | ``` <ReportContactInformation>   <IndividualName>    <Surname>Doe</Surname>    <GivenName>John</GivenName>    <MiddleName>E</MiddleName>   </IndividualName>   <BusinessTelephone>    <TelephoneNumber>905-999-9999</TelephoneNumber>    <TelephoneExtensionNumber>912</TelephoneExtensionNumber>   </BusinessTelephone>  </ReportContactInformation> ``` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### IndividualName (Nom au complet de la personne)

![IndividualName](images/Mod2/image015.gif)

Nom au complet de la personne

| Définition : | Cet élément parent renferme le nom de la personne avec qui CANAFE peut communiquer afin d'obtenir des clarifications quant à la déclaration. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **ReportContactInformation** |
| Exemple : | ``` <IndividualName>   <Surname>Doe</Surname>   <GivenName>John</GivenName>   <MiddleName>E</MiddleName>  </IndividualName> ``` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A4 Surname\* (Nom de famille de la personne-ressource\*)

![Surname*](images/Mod2/image016.gif)

Nom de famille de la personne-ressource

| Définition : | Le nom de famille de la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<Surname>Doe</Surname>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A5 GivenName\* (Prénom de la personne-ressource\*)

![GivenName*](images/Mod2/image017.gif)

Prénom de la personne-ressource

| Définition : | Le prénom de la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<GivenName>John</GivenName>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A6 MiddleName (Autres noms/initiales de la personne-ressource)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales de la personne-ressource

| Définition : | Les autres noms ou initiales de la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<MiddleName>E</MiddleName>` |
| Commentaires : |  |

#### BusinessTelephone (Numéro de téléphone d'affaires)

![BusinessTelephone](images/Mod2/image019.gif)

Numéro de téléphone d'affaires

| Définition : | Cet élément parent renferme le numéro de téléphone d'affaires de la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **ReportContactInformation** |
| Exemple : | ``` <BusinessTelephone>  <TelephoneNumber>905-999-9999</TelephoneNumber>  <TelephoneExtensionNumber>912</TelephoneExtensionNumber>  </BusinessTelephone> ``` |
| Commentaires : |  |

#### A7 TelephoneNumber\* (Numéro de téléphone de la personne-ressource\*)

![TelephoneNumber*](images/Mod2/image020.gif)

Numéro de téléphone de la personne-ressource

| Définition : | Le numéro de téléphone d'affaires de la personne-ressource avec qui CANAFE peut communiquer afin d'obtenir des précisions quant à la déclaration |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneNumber>905-999-9999</TelephoneNumber>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### A8 TelephoneExtensionNumber (Numéro du poste téléphonique de la personne-ressource)

![TelephoneExtensionNumber](images/Mod2/image021.gif)

Numéro du poste téléphonique de la personne-ressource

| Définition : | Le numéro du poste téléphonique de la personne-ressource |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 10 chiffres  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneExtensionNumber>912</TelephoneExtensionNumber>` |
| Commentaires : |  |

#### ExternalLocationIdentifier (Numéro de l'emplacement de l'entité déclarante)

![ExternalLocationIdentifier](images/Mod2/image022.gif)

Numéro de l'emplacement de l'entité déclarante

| Définition : | Le numéro d'emplacement qui représente l'endroit où l'opération a été effectuée |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 15 caractères (Ne pas utiliser de caractères spéciaux.)  Un par **ReportHeader** |
| Exemple : | `<ExternalLocationIdentifier>999999999</ExternalLocationIdentifier>` |
| Commentaires : |  |

### 2.3 Renseignements sur l'opération

#### CasinoTransaction (L'opération)

![CasinoTransaction](images/Mod2/image023.gif)

L'opération

| Définition : | Cet élément parent renferme les renseignements au sujet des opérations de la déclaration. |
| Attributs : | **CasinoTransactionSequenceNumber**  Obligatoire aux fins de traitement  1 à 999999999 chiffres  Un par **CasinoTransaction** |
| Contraintes : | Obligatoire aux fins de traitement  Un ou plusieurs par **CasinoDisbursementReport** |
| Exemple : | `<CasinoTransaction CasinoTransactionSequenceNumber="250">... </CasinoTransaction>` |
| Commentaires : |  |

#### CasinoTransactionDetail (Partie B)

![CasinoTransactionDetail](images/Mod2/image024.gif)

CasinoTransactionDetail (Partie B)

| Définition : | Cet élément parent renferme les renseignements qui décrivent où l'opération a été effectuée et comment l'opération a été effectuée. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **CasinoTransaction** |
| Exemple : | ``` <CasinoTransactionDetail>          <ExternalLocationIdentifier>999999999 </ExternalLocationIdentifier>  <TransactionConductMethodCode>7</TransactionConductMethodCode>  <TransactionConductOtherMethodDescriptionText> Autres renseignements  </TransactionConductOtherMethodDescriptionText>  <TransactionDate>20091010</TransactionDate>  <TransactionTime>111200</TransactionTime>  </CasinoTransactionDetail> ``` |
| Commentaires : |  |

#### B1 ExternalLocationIdentifier\* (Numéro de l'emplacement de l'entité déclarante\*)

![ExternalLocationIdentifier*](images/Mod2/image025.gif)

Numéro de l'emplacement de l'entité déclarante

| Définition : | Le numéro d'emplacement représente l'endroit où l'opération a été effectuée. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 15 caractères (Ne pas utiliser de caractères spéciaux.)  Un par**CasinoTransactionDetail** |
| Exemple : | `<ExternalLocationIdentifier>999999999</ExternalLocationIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### B2 TransactionConductMethodCode\* (Comment l'opération a-t-elle été effectuée?\*)

![TransactionConductMethodCode*](images/Mod2/image026.gif)

Comment l'opération a-t-elle été effectuée?

| Définition : | Ce code indique comment l'opération a été effectuée. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoTransactionDetail** |
| Exemple : | `<TransactionConductMethodCode>7</TransactionConductMethodCode>` |
| Commentaires : | Codes :  1 En personne  2 Guichet de rachat automatique  3 Téléphone  4 Poste  5 Messager  6 Véhicule blindé  7 Autre  Cet élément ne doit pas être vide. |

#### B3 TransactionConductMethodOtherDescriptionText (Description de « Autre »)

![TransactionConductMethodOtherDescriptionText](images/Mod2/image027.gif)

Description de Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **CasinoTransactionDetail** |
| Exemple : | `<TransactionConductOtherMethodDescriptionText>Autres renseignements</TransactionConductOtherMethodDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **TransactionConductMethodCode** =  7 Autre |

#### B4 TransactionDate\* (Date de l'opération\*)

![TransactionDate*](images/Mod2/image028.gif)

Date de l'opération

| Définition : | La date de l'opération |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 8 chiffres  Format = AAAAMMJJ  Un par **CasinoTransactionDetail** |
| Exemple : | `<TransactionDate>20091010</TransactionDate>` |
| Commentaires : | Cet élément ne doit pas être vide. |

#### B5 TransactionTime (Heure de l'opération)

![TransactionTime](images/Mod2/image029.gif)

Heure de l'opération

| Définition : | L'heure de l'opération |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 6 chiffres  Format = HHMMSS  Un par **CasinoTransactionDetail** |
| Exemple : | `<TransactionTime>111200</TransactionTime>` |
| Commentaires : |  |

### 2.4 Renseignements sur la personne qui a demandé le déboursement

#### DisbursementRequestor (Partie C)

![DisbursementRequestor](images/Mod2/image030.gif)

DisbursementRequestor (Partie C)

| Définition : | Cet élément parent renferme les renseignements sur la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **CasinoTransaction** |
| Exemple : | `<DisbursementRequestor> … </DisbursementRequestor>` |
| Commentaires : |  |

#### C1 ClientIdentifierAssignCode (Le casino déclarant a-t-il attribué un numéro de client à cette personne?)

![ClientIdentifierAssignCode](images/Mod2/image031.gif)

Le casino déclarant a-t-il attribué un numéro de client à cette personne?

| Définition : | Ce code indique si le casino a attribué ou non un numéro de client à la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **DisbursementRequestor** |
| Exemple : | `<ClientIdentifierAssignCode>1</ClientIdentifierAssignCode>` |
| Commentaires : | Codes :  1 Numéro de client attribué  2 Aucun numéro de client attribué |

#### C2 ClientIdentifier (Numéro de client attribué par le casino déclarant)

![ClientIdentifier](images/Mod2/image032.gif)

Numéro de client attribué par le casino déclarant

| Définition : | Le numéro de client attribué au client par le casino déclarant |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 20 caractères  Un par **DisbursementRequestor** |
| Exemple : | `<ClientIdentifier>12345</ClientIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **ClientIdentifierAssignCode** =  1 Numéro de client attribué |

#### IndividualInformation (Renseignement sur la personne qui a demandé le déboursement)

![IndividualInformation](images/Mod2/image033.gif)

Renseignement sur la personne qui a demandé le déboursement

| Définition : | Cet élément parent renferme les renseignements sur la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementRequestor** |
| Exemple : | `<IndividualInformation> … </IndividualInformation>` |
| Commentaires : |  |

#### IndividualName (Nom au complet de la personne)

![IndividualName](images/Mod2/image015.gif)

Nom au complet de la personne

| Définition : | Cet élément parent renferme les renseignements sur le nom de la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **IndividualInformation** |
| Exemple : | ``` <IndividualName>  <Surname>Smith</Surname>  <GivenName>Jane</GivenName>  <MiddleName></MiddleName>  </IndividualName> ``` |
| Commentaires : |  |

#### C3 Surname\* (Nom de famille de la personne \*)

![Surname*](images/Mod2/image016.gif)

Nom de famille de la personne

| Définition : | Le nom de famille de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<Surname>Smith</Surname>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =   0 Règle de 24 heures ne s'applique pas |

#### C4 GivenName\* (Prénom de la personne \*)

![GivenName*](images/Mod2/image017.gif)

Prénom de la personne

| Définition : | Le prénom de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<GivenName>Jane</GivenName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =   0 Règle de 24 heures ne s'applique pas |

#### C5 MiddleName (Autres noms/initiales de la personne)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales de la personne

| Définition : | Les autres noms ou initiales de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<MiddleName></MiddleName>` |
| Commentaires : |  |

#### Address (Adresse complète de la personne)

![Address](images/Mod2/image034.gif)

Adresse complète de la personne

| Définition : | L'élément parent pour l'adresse complète de la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **IndividualInformation** |
| Exemple : | ``` <Address>  <StreetAddressText>123 rue Principale</StreetAddressText>  <CityName>Montréal</CityName>  <AlphaProvinceStateCode>QC</AlphaProvinceStateCode>  <PostalZipCode>M3M3M3</PostalZipCode>  <AlphaCountryCode>CA</AlphaCountryCode>  </Address> ``` |
| Commentaires : |  |

#### C6 StreetAddressText\* (Adresse (rue et numéro) \*)

![StreetAddressText*](images/Mod2/image035.gif)

Adresse (rue et numéro)

| Définition : | L'adresse municipale |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 70 caractères  Un par **Address** |
| Exemple : | `<StreetAddressText>123 rue Principale</StreetAddressText>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =   0 Règle de 24 heures ne s'applique pas |

#### C7 CityName\* (Ville \*)

![CityName*](images/Mod2/image036.gif)

Ville

| Définition : | Le nom officiel de la municipalité |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Address** |
| Exemple : | `<CityName>Montréal</CityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =   0 Règle de 24 heures ne s'applique pas |

#### C9 AlphaProvinceStateCode\* (Province ou État \*)

![AlphaProvinceStateCode*](images/Mod2/image037.gif)

Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces et territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaProvinceStateCode>QC</AlphaProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA - Canada  US - États-Unis  MX - Mexique  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode**=   0 Règle de 24 heures ne s'applique pas |

#### C9 ProvinceStateName\* (Province ou État \*)

![ProvinceStateName*](images/Mod2/image038.gif)

Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Address** |
| Exemple : | `<ProvinceStateName>Sussex</IProvinceStateName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C10 PostalZipCode\* (Code postal ou zip \*)

![PostalZipCode*](images/Mod2/image039.gif)

Code postal ou zip

| Définition : | Le code postal ou zip |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Address** |
| Exemple : | `<PostalZipCode>M3M3M3</PostalZipCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA - Canada  US - États-Unis  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C8 AlphaCountryCode\* (Pays \*)

![AlphaCountryCode*](images/Mod2/image040.gif)

Pays

| Définition : | Ce code est utilisé pour indiquer le pays. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaCountryCode>CA</AlphaCountryCode>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C11 HomeTelephoneNumber (Numéro de téléphone à domicile)

![HomeTelephoneNumber](images/Mod2/image041.gif)

Numéro de téléphone à domicile

| Définition : | Le numéro de téléphone à domicile de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **IndividualInformation** |
| Exemple : | `<HomeTelephoneNumber>905-999-9999</HomeTelephoneNumber>` |
| Commentaires : |  |

#### BusinessTelephone (Numéro de téléphone d'affaires)

![BusinessTelephone](images/Mod2/image019.gif)

Numéro de téléphone d'affaires

| Définition : | Cet élément parent renferme le numéro de téléphone d'affaires de la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **IndividualInformation** |
| Exemple : | ``` <BusinessTelephone>  <TelephoneNumber>905-999-9999</TelephoneNumber>               <TelephoneExtensionNumber>912</TelephoneExtensionNumber>  </BusinessTelephone> ``` |
| Commentaires : |  |

#### C12 TelephoneNumber (Numéro de téléphone d'affaires de la personne)

![TelephoneNumber](images/Mod2/image020.gif)

Numéro de téléphone d'affaires de la personne

| Définition : | Le numéro de téléphone d'affaires de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneNumber>905-999-9999</TelephoneNumber>` |
| Commentaires : |  |

#### C13 TelephoneExtensionNumber (Numéro du poste téléphonique)

![TelephoneExtensionNumber](images/Mod2/image021.gif)

Numéro du poste téléphonique

| Définition : | Le numéro du poste téléphonique |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 10 chiffres  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneExtensionNumber>912</TelephoneExtensionNumber>` |
| Commentaires : |  |

#### C14 BirthDate\* (Date de naissance de la personne \*)

![BirthDate*](images/Mod2/image042.gif)

Date de naissance de la personne

| Définition : | La date de naissance de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 8 chiffres  Format = AAAAMMJJ  Un par **IndividualInformation** |
| Exemple : | `<BirthDate>19701212</BirthDate>` |
| Commentaires : | La date doit être postérieure à 1900, mais ne pas être une date future.  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C15 AlphaResidenceCountryCode (Pays de résidence)

![AlphaResidenceCountryCode](images/Mod2/image043.gif)

Pays de résidence

| Définition : | Ce code est utilisé pour indiquer le pays de résidence de la personne qui a demandé le déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **IndividualInformation** |
| Exemple : | `<AlphaResidenceCountryCode>CA</AlphaResidenceCountryCode>` |
| Commentaires : |  |

#### IndividualIdentification (Identification de la personne)

![IndividualIdentification](images/Mod2/image044.gif)

Identification de la personne

| Définition : | Cet élément parent renferme les renseignements relatifs au document d'identification présenté par la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **IndividualInformation** |
| Exemple : | ``` <IndividualIdentification>  <IdentificationTypeCode>3</IdentificationTypeCode>   <IdentificationOtherTypeDescriptionText>Carte Services Nouveau-  Brunswick</IdentificationOtherTypeDescriptionText>  <IdentificationIdentifier>UT12345</IdentificationIdentifier>  <AlphaIssueCountryCode>CA</AlphaIssueCountryCode>        <AlphaIssueProvinceStateCode>ON</AlphaIssueProvinceStateCode>  </IndividualIdentification> ``` |
| Commentaires : | Cet élément est obligatoire pour l'élément **DisbursementRequestor** |

#### C16 IdentificationTypeCode\* (Document d'identification présenté par la personne \*)

![IdentificationTypeCode*](images/Mod2/image045.gif)

Document d'identification présenté par la personne

| Définition : | Ce code est utilisé pour identifier le document d'identification présenté par la personne qui a demandé le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 2 chiffres  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationTypeCode>3</IdentificationTypeCode>` |
| Commentaires : | Codes :  1 Certificat de naissance  2 Passeport  3 Autre  4 Permis de conduire  5 Carte d'assurance-maladie provinciale  6 Fiche d'établissement ou carte de résident permanent  27 Carte d'assurance sociale  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C17 IdentificationOtherTypeDescription (Description de « Autre »)

![IdentificationOtherTypeDescription](images/Mod2/image046.gif)

Description d' Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationOtherTypeDescriptionText>Carte Services Nouveau-Brunswick</IdentificationOtherTypeDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **IdentificationTypeCode** =  3 Autre  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C18 IdentificationIdentifier\* (Numéro d'identification \*)

![IdentificationIdentifier*](images/Mod2/image047.gif)

Numéro d'identification

| Définition : | Le numéro d'identification pour le document d'identification décrit par l'élément **IdentificationTypeCode** ou **IdentificationOtherTypeDescription**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationIdentifier>UT12345</IdentificationIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas  sauf si **IdentificationTypeCode****=**  27 Carte d'assurance sociale**←**ne pas inclure le numéro |

#### C19 AlphaIssueCountryCode\* (Lieu de délivrance du document d'identification : Pays\*)

![AlphaIssueCountryCode*](images/Mod2/image048.gif)

Lieu de délivrance du document d'identification : Pays

| Définition : | Ce code est utilisé pour indiquer le pays de délivrance du document d'identification présenté par la personne qui a demandé le déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **IndividualIdentification** |
| Exemple : | `<AlphaIssueCountryCode>CA</AlphaIssueCountryCode>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C20 AlphaIssueProvinceStateCode\* (Lieu de délivrance du document d'identification : Province ou État \*)

![AlphaIssueProvinceStateCode*](images/Mod2/image049.gif)

Lieu de délivrance du document d'identification : Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État de délivrance du document d'identification. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces ou territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 2 caractères alpha  Un par **IndividualIdentification** |
| Exemple : | `<AlphaIssueProvinceStateCode>ON</AlphaIssueProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaIssueCountryCode =**  CA Canada  US États-Unis  MX Mexique  Cet élément est obligatoire si **IdentificationTypeCode****=**  1 Certificat de naissance  4 Permis de conduire  5 Carte d'assurance-maladie provinciale  La déclaration sera rejetée si **IdentificationTypeCode****=**  5 Carte d'assurance-maladie provinciale  **et AlphaIssueProvinceStateCode =**  MB Manitoba ou  PE Île-D=du-Prince-Édouard  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C20 IssueProvinceStateName\* (Lieu de délivrance du document d'identification : Province ou État \*)

![IssueProvinceStateName*](images/Mod2/image050.gif)

Lieu de délivrance du document d'identification : Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 60 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IssueProvinceStateName>Sussex</IssueProvinceStateName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### C21 IndividualOccupationDescriptionText\* (Le métier ou la profession de la personne \*)

![IndividualOccupationDescriptionText*](images/Mod2/image051.gif)

Le métier ou la profession de la personne

| Définition : | Le métier ou la profession de la personne qui a demandé le déboursement |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **IndividualInformation** |
| Exemple : | `<IndividualOccupationDescriptionText>Étudiante  </IndividualOccupationDescriptionText>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

### 2.5 Renseignements sur le tiers pour le compte de qui le déboursement a été reçu (le cas échéant)

#### OnBehalfOfInformation (Renseignements sur le tiers)

![OnBehalfOfInformation](images/Mod2/image052.gif)

Renseignements sur le tiers

| Définition : | Cet élément parent renferme les renseignements sur le tiers pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **CasinoTransaction** |
| Exemple : | `<OnBehalfOfInformation> … </OnBehalfOfInformation>` |
| Commentaires : |  |

#### C22 OnBehalfOfCode (Indicateur « Pour le compte de »)

![OnBehalfOfCode](images/Mod2/image053.gif)

Indicateur pour le compte de

| Définition : | Ce code sert à indiquer si le déboursement a été reçu pour le compte d'un tiers. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OnBehalfOfInformation** |
| Exemple : | `<OnBehalfOfCode>1</OnBehalfOfCode>` |
| Commentaires : | Codes :  1 Sans objet  2 Pour le compte d'une entité (Inclure **OnBehalfOfBusinessEntity**)  3 Pour le compte d'une autre personne (Inclure **OnBehalfOfIndividual**) |

#### OnBehalfOfIndividual (Partie E)

![OnBehalfOfIndividual](images/Mod2/image054.gif)

OnBehalfOfIndividual (Partie E)

| Définition : | Cet élément parent renferme les renseignements sur la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfInformation** |
| Exemple : | `<OnBehalfOfIndividual> … </OnBehalfOfIndividual>` |
| Commentaires : | Cet élément est obligatoire si **OnBehalfOfCode** =  3 Pour le compte d'une autre personne |

#### IndividualInformation (Renseignements sur la personne pour le compte de qui le déboursement a été reçu)

![IndividualInformation](images/Mod2/image033.gif)

Renseignements sur la personne pour le compte de qui le déboursement a été reçu

| Définition : | Cet élément parent renferme les renseignements sur la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfIndividual** |
| Exemple : | `<IndividualInformation> … </IndividualInformation>` |
| Commentaires : |  |

#### IndividualName (Nom au complet de la personne)

![IndividualName](images/Mod2/image055.gif)

Nom au complet de la personne

| Définition : | Cet élément parent renferme les renseignements sur le nom de la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **IndividualInformation** |
| Exemple : | ``` <IndividualName>  <Surname>Jones</Surname>  <GivenName>Robert</GivenName>  <MiddleName>B</MiddleName>  </IndividualName> ``` |
| Commentaires : |  |

#### E1 Surname\* (Nom de famille de la personne\*)

![Surname*](images/Mod2/image016.gif)

Nom de famille de la personne

| Définition : | Le nom de famille de la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<Surname>Jones</Surname>` |
| Commentaires : |  |

#### E2 GivenName\* (Prénom de la personne \*)

![GivenName*](images/Mod2/image017.gif)

Prénom de la personne

| Définition : | Le prénom de la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<GivenName>Robert</GivenName>` |
| Commentaires : |  |

#### E3 MiddleName (Autres noms/initiales de la personne)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales de la personne

| Définition : | Les autres noms ou initiales la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<MiddleName>B</MiddleName>` |
| Commentaires : |  |

#### Address (Adresse complète de la personne)

![Address](images/Mod2/image034.gif)

Adresse complète de la personne

| Définition : | Cet élément parent renferme l'adresse complète de la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **IndividualInformation** |
| Exemple : | ``` <Address>  <StreetAddressText>234 rue Principale</StreetAddressText>  <CityName>Montréal</CityName>  <AlphaProvinceStateCode>QC</AlphaProvinceStateCode>  <PostalZipCode>H3H3H3</PostalZipCode>  <AlphaCountryCode>CA</AlphaCountryCode> </Address> ``` |
| Commentaires : |  |

#### E4 StreetAddressText\* (Adresse (rue et numéro)\*)

![StreetAddressText*](images/Mod2/image035.gif)

Adresse (rue et numéro

| Définition : | L'adresse municipale |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 70 caractères  Un par **Address** |
| Exemple : | `<StreetAddressText>234 rue Principale</StreetAddressText>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E5 CityName\* (Ville \*)

![CityName*](images/Mod2/image036.gif)

Ville

| Définition : | Le nom officiel de la municipalité |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Address** |
| Exemple : | `<CityName>Montréal</CityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E7 AlphaProvinceStateCode\* (Province ou État \*)

![AlphaProvinceStateCode*](images/Mod2/image037.gif)

Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces et territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaProvinceStateCode>QC</AlphaProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA Canada  US États-Unis  MX Mexique  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E7 ProvinceStateName\* (Province ou État \*)

![ProvinceStateName*](images/Mod2/image038.gif)

Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 to 60 caractères  Un par **Address** |
| Exemple : | `<ProvinceStateName>Sussex</ProvinceStateName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E8 PostalZipCode\* (Code postal ou zip \*)

![PostalZipCode*](images/Mod2/image039.gif)

Code postal ou zip

| Définition : | Le code postal ou zip |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Address** |
| Exemple : | `<PostalZipCode>H3H3H3</PostalZipCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA Canada  US États-Unis  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E6 AlphaCountryCode\* (Pays \*)

![AlphaCountryCode*](images/Mod2/image040.gif)

Pays

| Définition : | Ce code est utilisé pour indiquer le pays. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaCountryCode>CA</AlphaCountryCode>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E9 HomeTelephoneNumber (Numéro de téléphone à domicile)

![HomeTelephoneNumber](images/Mod2/image056.gif)

Numéro de téléphone à domicile

| Définition : | Le numéro de téléphone à domicile de la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **IndividualInformation** |
| Exemple : | `<HomeTelephoneNumber>514-999-9999</HomeTelephoneNumber>` |
| Commentaires : |  |

#### BusinessTelephone (Numéro de téléphone d'affaires)

![BusinessTelephone](images/Mod2/image019.gif)

Numéro de téléphone d'affaires

| Définition : | Cet élément parent renferme les renseignements sur le numéro de téléphone d'affaires de la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : | ``` <BusinessTelephone>  <TelephoneNumber>514-999-9999</TelephoneNumber>                <TelephoneExtensionNumber>912</TelephoneExtensionNumber>  </BusinessTelephone> ``` |
| Contraintes : | Facultatif  Un par **IndividualInformation** |
| Exemple : |  |
| Commentaires : |  |

#### E10 TelephoneNumber (Numéro de téléphone d'affaires de la personne)

![TelephoneNumber](images/Mod2/image020.gif)

Numéro de téléphone d'affaires de la personne

| Définition : | Le numéro de téléphone d'affaires de la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneNumber>514-999-9999</TelephoneNumber>` |
| Commentaires : |  |

#### E11 TelephoneExtensionNumber (Numéro du poste téléphonique)

![TelephoneExtensionNumber](images/Mod2/image021.gif)

Numéro du poste téléphonique

| Définition : | Le numéro du poste téléphonique |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 10 chiffres  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneExtensionNumber>912</TelephoneExtensionNumber>` |
| Commentaires : |  |

#### E12 BirthDate (Date de naissance de la personne)

![BirthDate](images/Mod2/image042.gif)

Date de naissance de la personne

| Définition : | La date de naissance de la personne pour le compte de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 8 chiffres  Format = AAAAMMJJ  Un par **IndividualInformation** |
| Exemple : | `<BirthDate>19720505</BirthDate>` |
| Commentaires : | La date doit être postérieure à 1900, mais ne pas être une date future. |

#### E13 AlphaResidenceCountryCode (Pays de résidence)

![AlphaResidenceCountryCode](images/Mod2/image043.gif)

Pays de résidence

| Définition : | Ce code est utilisé pour indiquer le pays de résidence de la personne pour le compte de qui le déboursement a été effectué. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **IndividualInformation** |
| Exemple : | `<AlphaResidenceCountryCode>CA</AlphaResidenceCountryCode>` |
| Commentaires : |  |

#### IndividualIdentification (Identification de la personne)

![IndividualIdentification](images/Mod2/image044.gif)

Identification de la personne

| Définition : | Cet élément parent renferme les renseignements relatifs au document d'identification présenté par la personne pour le compte de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **IndividualInformation** |
| Exemple : | ``` <IndividualIdentification>  <IdentificationTypeCode>27</IdentificationTypeCode>  <IdentificationOtherTypeDescriptionText>   </IdentificationOtherTypeDescriptionText>  <IdentificationIdentifier> </IdentificationIdentifier>  <AlphaIssueCountryCode>CA</AlphaIssueCountryCode>       <AlphaIssueProvinceStateCode></AlphaIssueProvinceStateCode>  </IndividualIdentification> ``` |
| Commentaires : |  |

#### E14 IdentificationTypeCode (Document d'identification présentée par la personne)

![IdentificationTypeCode](images/Mod2/image045.gif)

Document d'identification présentée par la personne

| Définition : | Ce code est utilisé pour identifier le type de document d'identification utilisé pour établir l'identité de la personne au nom de laquelle le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 2 chiffres  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationTypeCode>27</IdentificationTypeCode>` |
| Commentaires : | Codes :  1 Certificat de naissance  2 Passeport  3 Autre  4 Permis de conduire  5 Carte d'assurance-maladie provinciale  6 Fiche d'établissement ou carte de résident permanent  27 Carte d'assurance sociale  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### E15 IdentificationOtherTypeDescription (Description de « Autre »)

![dentificationOtherTypeDescription](images/Mod2/image046.gif)

Description d' Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationOtherTypeDescriptionText>Carte Services Nouveau-Brunswick</IdentificationOtherTypeDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **IdentificationTypeCode** =  3 Autre |

#### E16 IdentificationIdentifier (Numéro d'identification)

![IdentificationIdentifier](images/Mod2/image047.gif)

Numéro d'identification

| Définition : | Le numéro d'identification pour le document d'identification décrit par l'élément **IdentificationTypeCode** ou **IdentificationOtherTypeDescription**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IdentificationIdentifier></IdentificationIdentifier>` |
| Commentaires : | Cet élément doit être vide si **IdentificationTypeCode****=**  27 Carte d'assurance sociale |

#### E17 AlphaIssueCountryCode (Lieu de délivrance du document d'identification : Pays)

![AlphaIssueCountryCode](images/Mod2/image048.gif)

Lieu de délivrance du document d'identification : Pays

| Définition : | Ce code est utilisé pour indiquer le pays de délivrance du document d'identification présenté par la personne pour qui le déboursement a été reçu. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **IndividualIdentification** |
| Exemple : | `<AlphaIssueCountryCode>CA</AlphaIssueCountryCode>` |
| Commentaires : |  |

#### E18 AlphaIssueProvinceStateCode (Lieu de délivrance du document d'identification : Province ou État)

![AlphaIssueProvinceStateCode](images/Mod2/image049.gif)

Lieu de délivrance du document d'identification : Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État de délivrance du document d'identification. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces et territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 2 caractères alpha  Un par **IndividualIdentification** |
| Exemple : | `<AlphaIssueProvinceStateCode></AlphaIssueProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si  **AlphaIssueCountryCode =**  CA Canada  US États-Unis  MX Mexique  Cet élément est obligatoire si **IdentificationTypeCode****=**  1 Certificat de naissance  4 Permis de conduire  5 Carte d'assurance maladie provinciale  La déclaration sera rejetée si **IdentificationTypeCode****=**  5 Carte d'assurance maladie **et**  **AlphaIssueProvinceStateCode =**  MB Manitoba **ou**  PE Île-du-Prince-Édouard |

#### E18 IssueProvinceStateName (Lieu de délivrance du document d'identification : Province ou État)

![IssueProvinceStateName](images/Mod2/image050.gif)

Lieu de délivrance du document d'identification : Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 60 caractères  Un par **IndividualIdentification** |
| Exemple : | `<IssueProvinceStateName>Sussex</IssueProvinceStateName>` |
| Commentaires : |  |

#### E19 IndividualOccupationDescriptionText (Le métier ou la profession de la personne)

![IndividualOccupationDescriptionText](images/Mod2/image051.gif)

Le métier ou la profession de la personne

| Définition : | Le métier ou la profession de la personne au nom de laquelle le déboursement a été effectué. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **IndividualInformation** |
| Exemple : | `<IndividualOccupationDescriptionText>Serveur  </IndividualOccupationDescriptionText>` |
| Commentaires : |  |

#### E20 RelationshipTypeCode (Lien entre la personne nommée à la partie C et celle nommée ci-dessus)

![RelationshipTypeCode](images/Mod2/image057.gif)

Lien entre la personne nommée à la partie C et celle nommée ci-dessus

| Définition : | Le lien entre la personne nommée dans l'élément **DisbursementRequestor** et la personne nommée dans l'élément **OnBehalfOfIndividual** |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 2 chiffres  Un par **OnBehalfOfIndividual** |
| Exemple : | `<RelationshipTypeCode>7</RelationshipTypeCode>` |
| Commentaires : | Codes :  1 Comptable  2 Mandataire  3 Emprunteur  4 Courtier  5 Client  6 Employé  7 Ami  8 Membre de la famille  9 Autre  10 Conseiller juridique |

#### E21 RealtionshipOtherTypeDescriptionText (Description de « Autre »)

![RealtionshipOtherTypeDescriptionText](images/Mod2/image058.gif)

Description d' Autre

| Définition : | La description de « Autre ». |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **OnBehalfOfIndividual** |
| Exemple : | `<RelationshipOtherTypeDescriptionText>Voisin  </RelationshipOtherTypeDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **RelationshipTypeCode** =  9 Autre |

#### OnBehalfOfBusinessEntity (Partie D)

![OnBehalfOfBusinessEntity](images/Mod2/image059.gif)

OnBehalfOfBusinessEntity (Partie D)

| Définition : | Cet élément parent renferme les renseignements sur l'entité au nom de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfInformation** |
| Exemple : | `<OnBehalfOfBusinessEntity> … </OnBehalfOfBusinessEntity>` |
| Commentaires : | Cet élément est obligatoire si **OnBehalfOfCode** =  2 Pour le compte d'une entité |

#### D1 BusinessEntityName\* (Dénomination sociale de l'entité \*)

![BusinessEntityName*](images/Mod2/image060.gif)

Dénomination sociale de l'entité

| Définition : | La dénomination sociale au complet de l'entreprise, de la société, de la fiducie ou de toute autre entité. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **OnBehalfOfBusinessEntity** |
| Exemple : | `<BusinessEntityName>CleanSweep Inc</BusinessEntityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D2 BusinessTypeDescriptionText\* (Nature de ses activités \*)

![BusinessTypeDescriptionText*](images/Mod2/image061.gif)

Nature de ses activités

| Définition : | La nature des activités de l'entité |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 40 caractères  Un par**OnBehalfOfBusinessEntity** |
| Exemple : | `<BusinessTypeDescriptionText>Nettoyeur résidentiel</BusinessTypeDescriptionText>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### Address (Adresse complète de l'entité)

![Address](images/Mod2/image062.gif)

Adresse complète de l'entité

| Définition : | Cet élément parent renferme l'adresse complète de l'entité au nom de laquelle le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfBusinessEntity** |
| Exemple : | ``` <Address>  <StreetAddressText>345 Huron Ave</StreetAddressText>  <CityName>Winnipeg</CityName>  <AlphaProvinceStateCode>MB</AlphaProvinceStateCode>  <PostalZipCode>R3R3R3</PostalZipCode>  <AlphaCountryCode>CA</AlphaCountryCode> </Address> ``` |
| Commentaires : |  |

#### D3 StreetAddressText\* (Adresse (rue et numéro) \*)

![StreetAddressText*](images/Mod2/image035.gif)

Adresse (rue et numéro

| Définition : | L'adresse municipale |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 70 caractères  Un par **Address** |
| Exemple : | `<StreetAddressText>345 Huron Ave</StreetAddressText>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D4 CityName\* (Ville \*)

![CityName*](images/Mod2/image036.gif)

Ville

| Définition : | Le nom officiel de la municipalité |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Address** |
| Exemple : | `<CityName>Winnipeg</CityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D6 AlphaProvinceStateCode\* (Province ou État \*)

![AlphaProvinceStateCode*](images/Mod2/image037.gif)

Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces ou territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaProvinceStateCode>MB</AlphaProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA Canada  US États-Unis  MX Mexique  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D6 ProvinceStateName\* (Province ou État \*)

![ProvinceStateName*](images/Mod2/image038.gif)

Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Address** |
| Exemple : | `<ProvinceStateName>Sussex</ProvinceStateName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D7 PostalCode\* (Code postal ou zip \*)

![PostalCode*](images/Mod2/image039.gif)

Code postal ou zip

| Définition : | Le code postal ou zip |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Address** |
| Exemple : | `<PostalZipCode>R3R3R3</PostalZipCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaCountryCode =**  CA Canada  US États-Unis  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D5 AlphaCountryCode\* (Pays \*)

![AlphaCountryCode*](images/Mod2/image040.gif)

Pays

| Définition : | Ce code est utilisé pour indiquer le pays. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **Address** |
| Exemple : | `<AlphaCountryCode>CA</AlphaCountryCode>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### BusinessTelephone (Numéro de téléphone d'affaires)

![BusinessTelephone](images/Mod2/image063.gif)

Numéro de téléphone d'affaires

| Définition : | Cet élément parent renferme les renseignements sur le numéro de téléphone d'affaires de l'entité au nom de qui le déboursement a été reçu. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfBusinessEntity** |
| Exemple : | ``` <BusinessTelephone>  <TelephoneNumber>204-999-9999</TelephoneNumber>                <TelephoneExtensionNumber>912</TelephoneExtensionNumber>  </BusinessTelephone> ``` |
| Commentaires : |  |

#### D8 TelephoneNumber (Numéro de téléphone d'affaires)

![TelephoneNumber](images/Mod2/image020.gif)

Numéro de téléphone d'affaires

| Définition : | Le numéro de téléphone d'affaires de l'entité au nom de qui le déboursement a été reçu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneNumber>204-999-9999</TelephoneNumber>` |
| Commentaires : |  |

#### D9 TelephoneExtensionNumber (Numéro du poste téléphonique)

![TelephoneExtensionNumber](images/Mod2/image021.gif)

Numéro du poste téléphonique

| Définition : | Numéro de poste téléphonique |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 10 chiffres  Un par **BusinessTelephone** |
| Exemple : | `<TelephoneExtensionNumber>912</TelephoneExtensionNumber>` |
| Commentaires : |  |

#### BusinessEntityIncorporationInformation (Renseignements sur l'incorporation de l'entité)

![BusinessEntityIncorporationInformation](images/Mod2/image064.gif)

Renseignements sur l'incorporation de l'entité

| Définition : | Cet élément parent renferme les renseignements sur l'incorporation. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **OnBehalfOfBusinessEntity** |
| Exemple : | ``` <BusinessEntityIncorporationInformation>               <BusinessEntityIncorporationCode>1  </BusinessEntityIncorporationCode>  <IncorporationInformation>                    <IncorporationIdentifier>MB12345</IncorporationIdentifier>   <AlphaIssueCountryCode>CA</AlphaIssueCountryCode>   <AlphaIssueProvinceStateCode>MB</AlphaIssueProvinceStateCode>  </IncorporationInformation>  </BusinessEntityIncorporationInformation> ``` |
| Commentaires : |  |

#### D10 BusinessEntityIncorporationCode (L'entité au nom de laquelle le déboursement a été reçu est-elle une personne morale?)

![BusinessEntityIncorporationCode](images/Mod2/image065.gif)

L'entité au nom de laquelle le déboursement a été reçu est-elle une personne morale?

| Définition : | Ce code est utilisé pour indiquer si l'entité est une personne morale. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **BusinessEntityIncorporationInformation** |
| Exemple : | `<BusinessEntityIncorporationCode>1  </BusinessEntityIncorporationCode>` |
| Commentaires : | Codes :  1 L'entité est une personne morale  2 L'entité n'est pas une personne morale |

#### IncorporationInformation (Renseignements sur l'incorporation)

![IncorporationInformation](images/Mod2/image066.gif)

Renseignements sur l'incorporation

| Définition : | Cet élément parent renferme les renseignements sur l'entité constituée en personne morale. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **BusinessEntityIncorporationInformation** |
| Exemple : | ``` <IncorporationInformation>  <IncorporationIdentifier>MB12345</IncorporationIdentifier>  <AlphaIssueCountryCode></AlphaIssueCountryCode>            <AlphaIssueProvinceStateCode>MB</AlphaIssueProvinceStateCode>  </IncorporationInformation> ``` |
| Commentaires : | Cet élément est obligatoire si **BusinessEntityIncorporationCode** =  1 L'entité est une personne morale |

#### D11 IncorporationIdentifier\* (Numéro du certificat de constitution en personne morale \*)

![IncorporationIdentifier*](images/Mod2/image067.gif)

Numéro du certificat de constitution en personne morale

| Définition : | Le numéro du certificat de constitution en personne morale |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **IncorporationInformation** |
| Exemple : | `<IncorporationIdentifier>MB12345</IncorporationIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D12 AlphaIssueCountryCode\* (Lieu de délivrance du certificat de constitution en personne morale : Pays \*)

![AlphaIssueCountryCode*](images/Mod2/image048.gif)

Lieu de délivrance du certificat de constitution en personne morale : Pays

| Définition : | Ce code est utilisé pour indiquer le pays. Veuillez consulter la table de codes pertinents dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 2 caractères alpha  Un par **IncorporationInformation** |
| Exemple : | `<AlphaIssueCountryCode></AlphaIssueCountryCode>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D13 AlphaIssueProvinceStateCode\* (Lieu de délivrance du certificat de constitution en personne morale : Province ou État \*)

![AlphaIssueProvinceStateCode*](images/Mod2/image049.gif)

Lieu de délivrance du certificat de constitution en personne morale : Province ou État

| Définition : | Ce code est utilisé pour indiquer la province, le territoire ou l'État. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE pour obtenir une liste des provinces et territoires du Canada ou des États du Mexique ou des États-Unis. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 2 caractères alpha  Un par **IncorporationInformation** |
| Exemple : | `<AlphaIssueProvinceStateCode>MB</AlphaIssueProvinceStateCode>` |
| Commentaires : | Cet élément est obligatoire si **AlphaIssueCountryCode =**  CA Canada  US États-Unis  MX Mexique  Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### D13 AlphaIssueProvinceStateName\* (Lieu de délivrance du certificat de constitution en personne morale : Province ou État \*)

![AlphaIssueProvinceStateName*](images/Mod2/image050.gif)

Lieu de délivrance du certificat de constitution en personne morale : Province ou État

| Définition : | Le nom de la province ou de l'État |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 60 caractères  Un par **IncorporationInformation** |
| Exemple : | `<IssueProvinceStateName>Sussex</IssueProvinceStateName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### AuthorizeIndividual (Nom(s) de signataire(s) ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino)

![AuthorizeIndividual](images/Mod2/image068.gif)

Nom(s) de signataire(s) ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino

| Définition : | Cet élément parent renferme les renseignements sur le nom du signataire ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino. |
| Attributs : | **AuthorizeIndividualSequenceNumber**  Obligatoire aux fins de traitement  1 à 99999 chiffres  Un par **AuthorizeIndividual** |
| Contraintes : | Facultatif  Zéro à trois par **OnBehalfOfBusinessEntity** |
| Exemple : | ``` <AuthorizeIndividual>  <Surname>Belliveau</Surname>  <GivenName>Jean</GivenName>  <MiddleName>Paul</MiddleName>  </AuthorizeIndividual> ``` |
| Commentaires : |  |

#### D14 Surname (Nom de famille de la personne)

![Surname](images/Mod2/image016.gif)

Nom de famille de la personne

| Définition : | Le nom de famille du signataire ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **AuthorizeIndividual** |
| Exemple : | `<Surname>Belliveau</Surname>` |
| Commentaires : |  |

#### D15 GivenName (Prénom de la personne)

![GivenName](images/Mod2/image017.gif)

Prénom de la personne

| Définition : | Le prénom du signataire ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **AuthorizeIndividual** |
| Exemple : | `<GivenName>Jean</GivenName>` |
| Commentaires : |  |

#### D16 MiddleName (Autres noms/initiales de la personne)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales de la personne

| Définition : | Les autres noms ou initiales du signataire ayant le pouvoir de lier l'entité ou d'agir à l'égard du compte du casino. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **AuthorizeIndividual** |
| Exemple : | `<MiddleName>Paul</MiddleName>` |
| Commentaires : |  |

### 2.6 Motif du déboursement

Si votre déclaration vise plus d'une opération en vertu de la règle de 24 heures, vous devez remplir la partie F1 pour chaque opération visée par la déclaration.

#### DisbursementReasonInformation (Partie F1)

![DisbursementReasonInformation](images/Mod2/image069.gif)

DisbursementReasonInformation (Partie F1)

| Définition : | Cet élément parent renferme les renseignements liés au motif du déboursement. |
| Attributs : | **DisbursementReasonInformationSequenceNumber**  Obligatoire aux fins de traitement  1 à 999999999 chiffres  Un par **DisbursementReasonInformation** |
| Contraintes : | Obligatoire aux fins de traitement  Un ou plusieurs par **CasinoTransaction** |
| Exemple : | `<DisbursementReasonInformation DisbursementReasonInformationSequenceNumber="1"> … </DisbursementReasonInformation>` |
| Commentaires : |  |

#### DisbursementReasonDetail (Renseignements sur le motif de déboursement)

![DisbursementReasonDetail](images/Mod2/image070.gif)

Renseignements sur le motif de déboursement

| Définition : | Cet élément parent renferme le motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementReasonInformation** |
| Exemple : | ``` <DisbursementReasonDetail>  <DisbursementReasonCode>2</DisbursementReasonCode>  <Amount>25000.00</Amount>  <AlphaCurrencyCode>CAD</AlphaCurrencyCode>  </DisbursementReasonDetail> ``` |
| Commentaires : |  |

#### F1.1 DisbursementReasonCode\* (Motif du déboursement \*)

![DisbursementReasonCode*](images/Mod2/image071.gif)

Motif du déboursement

| Définition : | Ce code est utilisé pour indiquer le motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 2 chiffres  Un par **DisbursementReasonDetail** |
| Exemple : | `<DisbursementReasonCode>2</DisbursementReasonCode>` |
| Commentaires : | Codes :  1 Rachat : Billets de machine à sous  2 Rachat : Jetons  3 Rachat : Plaques   4 Retrait d'une somme initiale     **→ CasinoAccount** est obligatoire  5 Retrait d'une somme confiée à la garde du casino  6 Avance sur crédit : Chèque au porteur      **→ OtherIndividual** ou **OtherBusinessEntity** est obligatoire  7 Avance sur crédit : Compte de crédit du casino      **→ CasinoAccount** est obligatoire  8 Avance sur crédit : Reconnaissance de dette   9 Avance sur crédit : Autre  10 Paiement : Pari  11 Paiement : Carte à valeur stockée du casino   12 Paiement : Cagnotte mach. à sous (autre que billets)  13 Paiement : Cagnotte de la table de jeu  14 Paiement : Tournoi  15 Paiement : Tirage ou prix  16 Paiement : Crédit au bénéficiaire   17 Paiement : Crédit à un tiers autre que le bénéficiaire     **→ OtherIndividual** ou **OtherBusinessEntity** est obligatoire  18 Encaissement de titres négociables : Traite bancaire      **→ OtherBusinessEntity** est obligatoire  19 Encaissement de titres négociables : Chèque de casino   20 Encaissement de titres négociables : Chèque (ne provenant pas d'un casino)      **→ OtherIndividual** ou **OtherBusinessEntity** est obligatoire  21 Encaissement de titres négociables : Mandat     **→ OtherBusinessEntity** est obligatoire  22 Encaissement de titres négociables : Chèque de voyage     **→ OtherBusinessEntity** est obligatoire  23 Remboursement : Frais de réception   24 Remboursement : Frais de déplacement |

#### F1.2 DisbursementAdvanceOnCreditOtherReasonDescriptionText (Description de « Autre »)

![DisbursementAdvanceOnCreditOtherReasonDescriptionText](images/Mod2/image072.gif)

Description d' Autre

| Définition : | La description de « Autre » pour le motif d'une avance sur crédit. |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **DisbursementReasonDetail** |
| Exemple : | `<DisbursementAdvanceOnCreditOtherReasonDescriptionText>Détails  </DisbursementAdvanceOnCreditOtherReasonDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **DisbursementReasonCode** =  9 Avance sur crédit : Autre |

#### F1.3 Amount\* (Montant \*)

![Amount*](images/Mod2/image073.gif)

Montant

| Définition : | Le montant total des fonds visés par l'opération, y compris deux positions décimales |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 15 positions décimales  Un par **DisbursementReasonDetail** |
| Exemple : | `<Amount>25000.00</Amount>` |
| Commentaires : |  |

#### F1.4 AlphaCurrencyCode\* (Code de la devise \*)

![AlphaCurrencyCode*](images/Mod2/image074.gif)

Code de la devise

| Définition : | Ce code est utilisé pour indiquer la devise associée au motif du déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  3 caractères alpha  Un par **DisbursementReasonDetail** |
| Exemple : | `<AlphaCurrencyCode>CAD</AlphaCurrencyCode>` |
| Commentaires : |  |

#### CasinoAccountInformation (Renseignements au sujet d'un compte du casino)

![CasinoAccountInformation](images/Mod2/image075.gif)

Renseignements au sujet d'un compte du casino

| Définition : | Cet élément parent renferme les renseignements sur un compte du casino touché par le motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementReasonInformation** |
| Exemple : | `<CasinoAccountInformation> … </CasinoAccountInformation>` |
| Commentaires : |  |

#### F1.5 CasinoAccountInvolveCode (Le motif associé au déboursement a-t-il concerné un compte du casino?)

![CasinoAccountInvolveCode](images/Mod2/image076.gif)

Le motif associé au déboursement a-t-il concerné un compte du casino?

| Définition : | Ce code est utilisé pour indiquer si le motif du déboursement a touché un compte du casino. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccountInformation** |
| Exemple : | `<CasinoAccountInvolveCode>1</CasinoAccountInvolveCode>` |
| Commentaires : | Codes :  1 Compte du casino touché  2 Aucun compte du casino touché |

#### CasinoAccount (Partie G)

![CasinoAccount](images/Mod2/image077.gif)

CasinoAccount (Partie G)

| Définition : | Cet élément parent renferme les renseignements sur le compte du casino où le déboursement a eu lieu. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **CasinoAccountInformation** |
| Exemple : | ``` <CasinoAccount>  <CasinoIdentifierAssignCode>1</CasinoIdentifierAssignCode>  <CasinoIdentifier>BB12345</CasinoIdentifier>  <AccountIdentifier>34567</AccountIdentifier>  <CasinoAccountTypeCode>2</CasinoAccountTypeCode>  <AlphaCurrencyCode>CAD</AlphaCurrencyCode>   <AccountHolderTypeCode>1</AccountHolderTypeCode>   <IndividualAccountHolderName    IndividualAccountHolderNameSequenceNumber="1">    <Surname>Ngo</Surname>    <GivenName>Robert</GivenName>    <MiddleName>S</MiddleName>   </IndividualAccountHolderName>  </CasinoAccount> ``` |
| Commentaires : | Cet élément est obligatoire si **CasinoAccountInvolveCode** =  1 Compte du casino touché |

#### G1 CasinoIdentifierAssignCode (Le casino où le compte est ouvert a-t-il un numéro d'identification?)

![CasinoIdentifierAssignCode](images/Mod2/image078.gif)

Le casino où le compte est ouvert a-t-il un numéro d'identification?

| Définition : | Ce code est utilisé pour indiquer s'il existe un numéro d'identification pour le casino où le compte est ouvert. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<CasinoIdentifierAssignCode>1</CasinoIdentifierAssignCode>` |
| Commentaires : | Codes :  1 Un numéro d'identification existe.  2 Un numéro d'identification n'existe pas. |

#### G2 CasinoIdentifier\* (Numéro d'identification du casino où le compte est ouvert\*)

![CasinoIdentifier*](images/Mod2/image079.gif)

Numéro d'identification du casino où le compte est ouvert

| Définition : | Le numéro d'identification du casino où le compte est ouvert |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **CasinoAccount** |
| Exemple : | `<CasinoIdentifier> BB12345</CasinoIdentifier>` |
| Commentaires : | Cet élément est obligatoire si **CasinoIdentifierAssignCode** =  1 Un numéro d'identification existe. |

#### G3 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro du compte touché par le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **CasinoAccount** |
| Exemple : | `<AccountIdentifier>34567</AccountIdentifier>` |
| Commentaires : |  |

#### G4 CasinoAccountTypeCode\* (Genre de compte \*)

![CasinoAccountTypeCode*](images/Mod2/image081.gif)

Genre de compte

| Définition : | Ce code est utilisé pour indiquer le genre de compte. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<CasinoAccountTypeCode>2</CasinoAccountTypeCode>` |
| Commentaires : | Codes :  1 Crédit  2 Montant initial  3 Autre |

#### G5 CasinoAccountOtherTypeDescriptionText (Description de « Autre »)

![CasinoAccountOtherTypeDescriptionText](images/Mod2/image082.gif)

Description d' Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **CasinoAccount** |
| Exemple : | `<CasinoAccountOtherTypeDescriptionText>Détails  </CasinoAccountOtherTypeDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **CasinoAccountTypeCode** =  3 Autre |

#### G6 AlphaCurrencyCode\* (Code de la devise du compte \*)

![AlphaCurrencyCode*](images/Mod2/image074.gif)

Code de la devise du compte

| Définition : | Ce code est utilisé pour indiquer la devise du compte touché par le motif du déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 3 caractères alpha   Un par **CasinoAccount** |
| Exemple : | `<AlphaCurrencyCode>CAD</AlphaCurrencyCode>` |
| Commentaires : |  |

#### G7 AccountHolderTypeCode\* (Le détenteur du compte \*)

![AccountHolderTypeCode*](images/Mod2/image083.gif)

Le détenteur du compte

| Définition : | Ce code est utilisé pour indiquer le si le détenteur du compte est une personne ou une entité. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<AccountHolderTypeCode>1</AccountHolderTypeCode>` |
| Commentaires : | Codes :  1 Personne  2 Société ou autre entité |

#### IndividualAccountHolderName (Nom au complet de la personne qui détient le compte)

![IndividualAccountHolderName](images/Mod2/image084.gif)

Nom au complet de la personne qui détient le compte

| Définition : | Cet élément parent renferme les renseignements sur le détenteur du compte. |
| Attributs : | **IndividualAccountHolderNameSequenceNumber**  Obligatoire aux fins de traitement  1 à 999999999 chiffres  Un par **IndividualAccountHolderName** |
| Contraintes : | Obligatoire aux fins de traitement  Un à trois par **CasinoAccount** |
| Exemple : | ``` <IndividualAccountHolderName  IndividualAccountHolderNameSequenceNumber="1">  <Surname>Ngo</Surname>  <GivenName>Robert</GivenName>  <MiddleName>S</MiddleName>  </IndividualAccountHolderName> ``` |
| Commentaires : | Cet élément est obligatoire si **AccountHolderTypeCode** =  1 Personne |

#### G8 Surname\* (Nom de famille du détenteur de compte\*)

![Surname*](images/Mod2/image016.gif)

Nom de famille du détenteur de compte

| Définition : | Le nom de famille du détenteur du compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<Surname>Ngo</Surname>` |
| Commentaires : |  |

#### G9 GivenName\* (Prénom du détenteur de compte\*)

![GivenName*](images/Mod2/image017.gif)

Prénom du détenteur de compte

| Définition : | Le prénom du détenteur du compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<GivenName>Robert</GivenName>` |
| Commentaires : |  |

#### G10 MiddleName (Autres noms/initiales du détenteur de compte)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales du détenteur de compte

| Définition : | Les autres noms ou initiales du détenteur du compte |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<MiddleName>S</MiddleName>` |
| Commentaires : |  |

#### G11 BusinessEntityAccountHolderName\* (Dénomination sociale complète de l'entité \*)

![BusinessEntityAccountHolderName*](images/Mod2/image085.gif)

Dénomination sociale complète de l'entité

| Définition : | La dénomination sociale complète de l'entité qui détient le compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **CasinoAccount** |
| Exemple : | `<BusinessEntityAccountHolderName>CleanSweep Inc </BusinessEntityAccountHolderName>` |
| Commentaires : | Cet élément est obligatoire si **AccountHolderTypeCode** =  2 Société ou autre entité |

#### OtherIndividualInformation (Renseignements sur l'autre personne)

![OtherIndividualInformation](images/Mod2/image086.gif)

Renseignements sur l'autre personne

| Définition : | Cet élément parent renferme les renseignements sur la personne associée au motif du déboursement autre que les personnes nommées dans les éléments **DisbursementRequestor** ou **OnBehalfOfIndividual**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementReasonInformation** |
| Exemple : | ``` <OtherIndividualInformation>  <AssociateOtherIndividualCode>1</AssociateOtherIndividualCode>  <OtherIndividual OtherIndividualSequenceNumber="1">   <IndividualName>    <Surname>Joli</Surname>    <GivenName>Trey</GivenName>    <MiddleName>S</MiddleName>   </IndividualName>   <AssociateAccountCode>1</AssociateAccountCode>   <Account>    <FinancialInstitutionName>Bank     of BC</FinancialInstitutionName>                             <TransitIdentifier>12321</TransitIdentifier>    <AccountIdentifier>234565</AccountIdentifier>   </Account>  </OtherIndividual>  </OtherIndividualInformation> ``` |
| Commentaires : |  |

#### F1.6 AssociateOtherIndividualCode (Y avait-il une personne (autre que celles qui sont nommées aux parties C ou E de la présente opération) associée au motif du déboursement?)

![AssociateOtherIndividualCode](images/Mod2/image087.gif)

Y avait-il une personne (autre que celles qui sont nommées aux parties C ou E de la présente opération) associée au motif du déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait une autre personne associée au motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  One per **OtherIndividualInformation** |
| Exemple : | `<AssociateOtherIndividualCode>1</AssociateOtherIndividualCode>` |
| Commentaires : | Codes :  1 Une autre personne associée  2 Aucune autre personne associée |

#### OtherIndividual (Partie H)

![OtherIndividual](images/Mod2/image088.gif)

OtherIndividual (Partie H)

| Définition : | Cet élément parent renferme les renseignements sur la personne associée au motif du déboursement autre que les personnes nommées dans les éléments **DisbursementRequestor** ou **OnBehalfOfIndividual**. |
| Attributs : | **OtherIndividualSequenceNumber**  1 à 999999999 chiffres  Un par **OtherIndividual** |
| Contraintes : | Facultatif  Zéro ou plusieurs par **OtherIndividualInformation** |
| Exemple : | `<OtherIndividual OtherIndividualSequenceNumber="1"> … </OtherIndividual>` |
| Commentaires : | Cet élément est obligatoire si **AssociateOtherIndividualCode** =  1 Une autre personne associée |

#### IndividualName (Nom au complet de la personne)

![IndividualName (Nom au complet de la personne)](images/Mod2/image015.gif)

Nom au complet de la personne

| Définition : | Cet élément parent renferme les renseignements sur l'autre personne associée au motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **Other****Individual** |
| Exemple : | ``` <IndividualName>  <Surname>Joli</Surname>  <GivenName>Trey</GivenName>  <MiddleName>S</MiddleName> </IndividualName> ``` |
| Commentaires : |  |

#### H1 Surname\* (Nom de famille de la personne \*)

![Surname*](images/Mod2/image016.gif)

Nom de famille de la personne

| Définition : | Le nom de famille de l'autre personne associée au motif du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<Surname>Joli</Surname>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H2 GivenName\* (Prénom de la personne \*)

![GivenName*](images/Mod2/image017.gif)

Prénom de la personne

| Définition : | Le prénom de l'autre personne associée au motif du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<GivenName>Trey</GivenName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H3 MiddleName (Autres noms/initiales de la personne)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales de la personne

| Définition : | Les autres noms ou initiales de l'autre personne associée au motif du déboursement |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<MiddleName>S</MiddleName>` |
| Commentaires : |  |

#### H4 AssociateAccountCode (Y avait-il un compte pour cette personne (autre qu'un compte indiqué à la partie G) associé au déboursement?)

![AssociateAccountCode](images/Mod2/image089.gif)

Y avait-il un compte pour cette personne (autre qu'un compte indiqué à la partie G) associé au déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait un compte pour cette personne qui était associé au motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherIndividual** |
| Exemple : | `<AssociateAccountCode>1</AssociateAccountCode>` |
| Commentaires : | Codes :  1 Compte associé  2 Aucun compte associé |

#### Account (Renseignements sur le compte)

![Account](images/Mod2/image090.gif)

Renseignements sur le compte

| Définition : | Cet élément parent renferme les renseignements sur le compte associé au motif de déboursement (autre que celui de l'élément **CasinoAccount**). |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **OtherIndividual** |
| Exemple : | ``` <Account>  <FinancialInstitutionName>Bank of BC</FinancialInstitutionName>  <TransitIdentifier>12321</TransitIdentifier>  <AccountIdentifier>234565</AccountIdentifier>  </Account> ``` |
| Commentaires : | Cet élément est obligatoire si **AssociatedAccountCode** =  1 Compte associé |

#### H5 FinancialInstitutionName\* (Nom de l'institution financière \*)

![FinancialInstitutionName*](images/Mod2/image091.gif)

Nom de l'institution financière

| Définition : | Le nom de l'institution financière où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Account** |
| Exemple : | `<FinancialInstitutionName>Bank of BC</FinancialInstitutionName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H6 TransitIdentifier\* (Numéro de transit \*)

![TransitIdentifier*](images/Mod2/image092.gif)

Numéro de transit

| Définition : | Le numéro de transit où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 12 caractères  Un par **Account** |
| Exemple : | `<TransitIdentifier>12321</TransitIdentifier>` |
| Commentaires : |  |

#### H7 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro de compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Account** |
| Exemple : | `<AccountIdentifier>234565</AccountIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### OtherBusinessEntityInformation (Renseignements sur l'autre entité)

![OtherBusinessEntityInformation](images/Mod2/image093.gif)

Renseignements sur l'autre entité

| Définition : | Cet élément parent renferme les renseignements sur l'entité associée au motif du déboursement, autre que l'entité nommée à l'élément **OnBehalfOfBusinessEntity**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementReasonInformation** |
| Exemple : | ```  <OtherBusinessEntityInformation>           <AssociateOtherBusinessEntityCode>1  </AssociateOtherBusinessEntityCode>  <OtherBusinessEntity OtherBusinessEntitySequenceNumber="1">  <BusinessEntityName>Cleansweep Inc</BusinessEntityName>  <AssociateAccountCode>1</AssociateAccountCode>   <Account>    <FinancialInstitutionName>Bank of BC</FinancialInstitutionName>    <TransitIdentifier>12321</TransitIdentifier>    <AccountIdentifier>234565</AccountIdentifier>   </Account>  </OtherBusinessEntity>  </OtherBusinessEntityInformation> ``` |
| Commentaires : |  |

#### F1.7 AssociateOtherBusinessEntityCode (Y avait-il une entité (autre que le casino qui présente la déclaration ou l'entité nommée à la partie D de la présente opération) associée au motif du déboursement?)

![AssociateOtherBusinessEntityCode](images/Mod2/image094.gif)

Y avait-il une entité (autre que le casino qui présente la déclaration ou l'entité nommée à la partie D de la présente opération) associée au motif du déboursement?

| Définition : | Ce code est utilisé pour indiquer si une autre entité est associée au motif du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherBusinessEntityInformation** |
| Exemple : | `<AssociateOtherBusinessEntityCode>1  </AssociateOtherBusinessEntityCode>` |
| Commentaires : | Codes :  1 Une autre entité associée  2 Aucune autre entité associée |

#### OtherBusinessEntity (Partie I)

![OtherBusinessEntity](images/Mod2/image095.gif)

OtherBusinessEntity (Partie I)

| Définition : | Cet élément parent renferme les renseignements sur l'autre entité associée au motif du déboursement. |
| Attributs : | **OtherBusinessEntitySequenceNumber**  1 à 999999999 chiffres  Un par **OtherBusinessEntityInformation** |
| Contraintes : | Facultatif  Zéro ou plusieurs par **OtherBusinessEntityInformation** |
| Exemple : | `<OtherBusinessEntity OtherBusinessEntitySequenceNumber="1">…</OtherBusinessEntity>` |
| Commentaires : | Cet élément est obligatoire si   **AssociateOtherBusinessEntityCode** =  1 Une autre entité associée |

#### I1 BusinessEntityName\* (Dénomination sociale complète de l'entité \*)

![BusinessEntityName*](images/Mod2/image060.gif)

Dénomination sociale complète de l'entité

| Définition : | La dénomination sociale complète de l'entité associée au motif du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **OtherBusinessEntity** |
| Exemple : | `<BusinessEntityName>CleanSweep Inc</BusinessEntityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### I2 AssociateAccountCode Y avait-il un compte pour cette entité (autre qu'un compte indiqué à la partie G) associé au déboursement?

![AssociateAccountCode ](images/Mod2/image089.gif)

Y avait-il un compte pour cette entité (autre qu'un compte indiqué à la partie G) associé au déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait un compte pour cette entité. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherBusinessEntity** |
| Exemple : | `<AssociateAccountCode>1</AssociateAccountCode>` |
| Commentaires : | Codes :  1 Compte associé  2 Aucun compte associé |

#### Account (Renseignements sur le compte)

![Account](images/Mod2/image090.gif)

Renseignements sur le compte

| Définition : | Cet élément parent renferme les renseignements sur le compte associé au déboursement (autre que ceux de l'élément **CasinoAccount**). |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **OtherBusinessEntity** |
| Exemple : | ``` <Account>  <FinancialInstitutionName>Bank   of BC</FinancialInstitutionName>  <TransitIdentifier>12321</TransitIdentifier>  <AccountIdentifier>234565</AccountIdentifier>  </Account> ``` |
| Commentaires : | Cet élément est obligatoire si **AssociatedAccountCode** =  1 Compte associé |

#### I3 FinancialInstitutionName\* (Nom de l'institution financière \*)

![FinancialInstitutionName*](images/Mod2/image091.gif)

Nom de l'institution financière

| Définition : | Le nom de l'institution financière où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Account** |
| Exemple : | `<FinancialInstitutionName>Bank of BC</FinancialInstitutionName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### I4 TransitIdentifier\* (Numéro de transit \*)

![TransitIdentifier*](images/Mod2/image092.gif)

Numéro de transit

| Définition : | Le numéro de transit où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 12 caractères  Un par **Account** |
| Exemple : | `<TransitIdentifier>12321</TransitIdentifier>` |
| Commentaires : |  |

#### I5 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro de compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Account** |
| Exemple : | `<AccountIdentifier>234565</AccountIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

### 2.7 Méthode du déboursement

Si votre déclaration vise plus d'une opération en vertu de la règle de 24 heures, vous devez remplir la partie F2pour chaque opération visée par la déclaration.

#### DisbursementMethodInformation (Partie F2)

![DisbursementMethodInformation](images/Mod2/image096.gif)

DisbursementMethodInformation (Partie F2)

| Définition : | Cet élément parent renferme les renseignements sur comment le déboursement a réellement été versé. |
| Attributs : | **DisbursementMethodInformationSequenceNumber**  1 à 999999999 chiffres  Un par **DisbursementMethodInformation** |
| Contraintes : | Obligatoire aux fins de traitement  Un ou plusieurs par **CasinoTransaction** |
| Exemple : | `<DisbursementMethodInformation DisbursementMethodInformationSequenceNumber="1"> … </DisbursementMethodInformation>` |
| Commentaires : |  |

#### DisbursementMethodDetail (Renseignements sur la méthode du déboursement)

![DisbursementMethodDetail](images/Mod2/image097.gif)

Renseignements sur la méthode du déboursement

| Définition : | Cet élément parent renferme la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementMethodInformation** |
| Exemple : | ``` <DisbursementMethodDetail>  <DisbursementMethodCode>1</DisbursementMethodCode>  <Amount>25000.00</Amount>  <AlphaCurrencyCode>CAD</AlphaCurrencyCode>  </DisbursementMethodDetail> ``` |
| Commentaires : |  |

#### F2.1 DisbursementMethodCode\* (Méthode du déboursement\*)

![DisbursementMethodCode*](images/Mod2/image098.gif)

Méthode du déboursement

| Définition : | Ce code est utilisé pour indiquer la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 2 chiffres  Un par**DisbursementMethodDetail** |
| Exemple : | `<DisbursementMethodCode>1</DisbursementMethodCode>` |
| Commentaires : | Codes :  1 Porté à une carte de crédit  2 Porté à une carte à valeur stockée du casino  3 Dépôt dans le compte d'une institution financière     **→ OtherIndividual** ou  **OtherBusinessEntity** est obligatoire  4 Émission d'un chèque  5 Transfert de fonds international     **→ OtherIndividual** ou  **OtherBusinessEntity** est obligatoire  6 Transfert de fonds domestique     **→ OtherIndividual** ou  **OtherBusinessEntity** est obligatoire  7 Paiement en espèces  8 Transfert vers un autre casino     **→ OtherBusinessEntity** est obligatoire  9 Autre |

#### F2.2 DisbursementOtherMethodDescriptionText (Description de « Autre »)

![DisbursementOtherMethodDescriptionText](images/Mod2/image099.gif)

Description d'Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **DisbursementMethodDetail** |
| Exemple : | `<DisbursementOtherMethodDescriptionText>Détails  </DisbursementOtherMethodDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **DisbursementMethodCode** =  9 Autre |

#### F2.3 Amount\* (Montant \*)

![Amount*](images/Mod2/image073.gif)

Montant

| Définition : | Le montant total versé pour la méthode du déboursement, y compris deux décimales. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 15 positions décimales  Un par **DisbursementMethodDetail** |
| Exemple : | `<Amount>25000.00</Amount>` |
| Commentaires : |  |

#### F2.4 AlphaCurrencyCode\* (Code de la devise\*)

![AlphaCurrencyCode*](images/Mod2/image074.gif)

Code de la devise

| Définition : | Ce code est utilisé pour indiquer la devise associée à la méthode du déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  3 caractères alpha   Un par **DisbursementMethodDetail** |
| Exemple : | `<AlphaCurrencyCode>CAD</AlphaCurrencyCode>` |
| Commentaires : |  |

#### CasinoAccountInformation (Renseignements au sujet d'un compte du casino)

![CasinoAccountInformation](images/Mod2/image075.gif)

Renseignements au sujet d'un compte du casino

| Définition : | Cet élément parent renferme les renseignements sur un compte du casino touché par la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementMethodInformation** |
| Exemple : | `<CasinoAccountInformation> … </CasinoAccountInformation>` |
| Commentaires : |  |

#### F2.5 CasinoAccountInvolveCode (La méthode associée au déboursement a-t-elle touchée un compte du casino?)

![CasinoAccountInvolveCode](images/Mod2/image076.gif)

La méthode associée au déboursement a-t-elle touchée un compte du casino?

| Définition : | Ce code est utilisé pour indiquer si la méthode du déboursement a touché un compte du casino. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccountInformation** |
| Exemple : | `<CasinoAccountInvolveCode>1</CasinoAccountInvolveCode>` |
| Commentaires : | Codes :  1 Compte du casino touché  2 Aucun compte du casino touché |

#### CasinoAccount (Partie G)

![CasinoAccount](images/Mod2/image077.gif)

CasinoAccount (Partie G)

| Définition : | Cet élément parent renferme les renseignements sur le compte du casino où le déboursement a eu lieu. |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **DisbursementMethodInformation** |
| Exemple : | ``` <CasinoAccount>  <CasinoIdentifierAssignCode>1</CasinoIdentifierAssignCode>  <CasinoIdentifier>BB12345</CasinoIdentifier>  <AccountIdentifier>23456</AccountIdentifier>  <CasinoAccountTypeCode>1</CasinoAccountTypeCode>  <AlphaCurrencyCode>CAD</AlphaCurrencyCode>   <AccountHolderTypeCode>1</AccountHolderTypeCode>   <IndividualAccountHolderName    IndividualAccountHolderNameSequenceNumber="1">    <Surname>Holliday</Surname>    <GivenName>William</GivenName>    <MiddleName>S</MiddleName>   </IndividualAccountHolderName>  </CasinoAccount> ``` |
| Commentaires : | Cet élément est obligatoire si **CasinoAccountInvolveCode** =  1 Compte du casino touché |

#### G1 CasinoIdentifierAssignCode (Le casino où le compte est ouvert a-t-il un numéro d'identification?)

![CasinoIdentifierAssignCode](images/Mod2/image078.gif)

Le casino où le compte est ouvert a-t-il un numéro d'identification?

| Définition : | Ce code est utilisé pour indiquer s'il existe un numéro d'identification pour le casino où le compte est ouvert. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<CasinoIdentifierAssignCode>1</CasinoIdentifierAssignCode>` |
| Commentaires : | Codes :  1 Un numéro d'identification existe.  2 Un numéro d'identification n'existe pas. |

#### G2 CasinoIdentifier\* (Numéro d'identification du casino où le compte est ouvert \*)

![CasinoIdentifier*](images/Mod2/image079.gif)

Numéro d'identification du casino où le compte est ouvert

| Définition : | Le numéro d'identification du casino où le compte est ouvert |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 20 caractères  Un par **CasinoAccount** |
| Exemple : | `<CasinoIdentifier>BB12345</CasinoIdentifier>` |
| Commentaires : | Cet élément est obligatoire si **CasinoIdentifierAssignCode** =  1 Un numéro d'identification existe. |

#### G3 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro du compte touché par le déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **CasinoAccount** |
| Exemple : | `<AccountIdentifier>23456</AccountIdentifier>` |
| Commentaires : |  |

#### G4 CasinoAccountTypeCode\* (Genre de compte \*)

![CasinoAccountTypeCode*](images/Mod2/image081.gif)

Genre de compte

| Définition : | Ce code est utilisé pour indiquer le genre de compte. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<CasinoAccountTypeCode>1</CasinoAccountTypeCode>` |
| Commentaires : | Codes :  1 Crédit  2 Montant initial  3 Autre |

#### G5 CasinoAccountOtherTypeDescriptionText (Description de « Autre »)

![CasinoAccountOtherTypeDescriptionText](images/Mod2/image082.gif)

Description d' Autre

| Définition : | La description de « Autre » |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 40 caractères  Un par **CasinoAccount** |
| Exemple : | `<CasinoAccountOtherTypeDescriptionText>Détails  </CasinoAccountOtherTypeDescriptionText>` |
| Commentaires : | Cet élément est obligatoire si **CasinoAccountTypeCode** =  3 Autre |

#### G6 AlphaCurrencyCode\* (Code de la devise du compte \*)

![AlphaCurrencyCode*](images/Mod2/image074.gif)

Code de la devise du compte

| Définition : | Ce code est utilisé pour indiquer la devise du compte touché par la méthode du déboursement. Veuillez consulter la table de codes pertinente dans la documentation technique de la page des publications sur le site Web de CANAFE. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 3 caractères alpha   Un par **CasinoAccount** |
| Exemple : | `<AlphaCurrencyCode>CAD</AlphaCurrencyCode>` |
| Commentaires : |  |

#### G7 AccountHolderTypeCode\* (Le détenteur du compte \*)

![AccountHolderTypeCode*](images/Mod2/image083.gif)

Le détenteur du compte

| Définition : | Ce code est utilisé pour indiquer si le détenteur du compte est une personne ou une entité. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **CasinoAccount** |
| Exemple : | `<AccountHolderTypeCode>1</AccountHolderTypeCode>` |
| Commentaires : | Codes :  1 Personne  2 Société ou autre entité |

#### IndividualAccountHolderName (Nom au complet de la personne qui détient le compte)

![IndividualAccountHolderName](images/Mod2/image084.gif)

Nom au complet de la personne qui détient le compte

| Définition : | Cet élément parent renferme les renseignements sur le détenteur du compte. |
| Attributs : | **IndividualAccountHolderNameSequenceNumber**  Obligatoire aux fins de traitement  1 à 999999999 chiffres  Un par **IndividualAccountHolderName** |
| Contraintes : | Obligatoire aux fins de traitement  Un à trois par **CasinoAccount** |
| Exemple : | ``` <IndividualAccountHolderName  IndividualAccountHolderNameSequenceNumber="1">  <Surname>Holliday</Surname>  <GivenName>William</GivenName>  <MiddleName>S</MiddleName>  </IndividualAccountHolderName> ``` |
| Commentaires : | Cet élément est obligatoire si **AccountHolderTypeCode** =  1 Personne |

#### G8 Surname\* (Nom de famille du détenteur de compte \*)

![Surname*](images/Mod2/image016.gif)

Nom de famille du détenteur de compte

| **G8** | **Surname\*** | **Nom de famille du détenteur de compte \*** |
|  | Surname |
| Définition : | Le nom de famille du détenteur du compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<Surname>Holliday</Surname>` |
| Commentaires : |  |

#### G9 GivenName\* (Prénom du détenteur de compte \*)

![GivenName*](images/Mod2/image017.gif)

Prénom du détenteur de compte

| Définition : | Le prénom du détenteur du compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<GivenName>William</GivenName>` |
| Commentaires : |  |

#### G10 MiddleName (Autres noms/initiales du détenteur de compte)

![MiddleName](images/Mod2/image018.gif)

Autres noms/initiales du détenteur de compte

| Définition : | Les autres noms ou initiales du détenteur du compte |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualAccountHolderName** |
| Exemple : | `<MiddleName>S</MiddleName>` |
| Commentaires : |  |

#### G11 BusinessEntityAccountHolderName\* (Dénomination sociale complète de l'entité \*)

![BusinessEntityAccountHolderName*](images/Mod2/image085.gif)

Dénomination sociale complète de l'entité

| Définition : | La dénomination sociale complète de l'entité qui détient le compte. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **CasinoAccount** |
| Exemple : | `<BusinessEntityAccountHolderName>CleanSweep Inc</BusinessEntityAccountHolderName>` |
| Commentaires : | Cet élément est obligatoire si **AccountHolderTypeCode** =  2 Société ou autre entité |

#### OtherIndividualInformation (Renseignements sur l'autre personne)

![OtherIndividualInformation](images/Mod2/image086.gif)

Renseignements sur l'autre personne

| Définition : | Cet élément parent renferme les renseignements sur la personne associée à la méthode du déboursement autre que les personnes nommées dans les éléments **DisbursementRequestor** ou **OnBehalfOfIndividual**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementMethodInformation** |
| Exemple : | ``` <OtherIndividualInformation>  <AssociateOtherIndividualCode>1  </AssociateOtherIndividualCode>  <OtherIndividual   OtherIndividualSequenceNumber="1">   <IndividualName>    <Surname>Peters</Surname>    <GivenName>Peter</GivenName>    <MiddleName>P</MiddleName>   </IndividualName>   <AssociateAccountCode>1</AssociateAccountCode>   <Account>    <FinancialInstitutionName>Bank     of BC </FinancialInstitutionName>                               <TransitIdentifier>12321    </TransitIdentifier>                             <AccountIdentifier>234565    </AccountIdentifier>   </Account>  </OtherIndividual>  </OtherIndividualInformation> ``` |
| Commentaires : |  |

#### F2.6 AssociateOtherIndividualCode (Y avait-il une personne (autre que celles qui sont nommées aux parties C ou E de la présente opération) associée à la méthode du déboursement?)

![AssociateOtherIndividualCode](images/Mod2/image087.gif)

Y avait-il une personne (autre que celles qui sont nommées aux parties C ou E de la présente opération) associée à la méthode du déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait une autre personne associée à la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  One per **OtherIndividualInformation** |
| Exemple : | `<AssociateOtherIndividualCode>1</AssociateOtherIndividualCode>` |
| Commentaires : | Codes :  1 Une autre personne associée  2 Aucune autre personne associée |

#### OtherIndividual (Partie H)

![OtherIndividual](images/Mod2/image088.gif)

OtherIndividual (Partie H)

| Définition : | Cet élément parent renferme les renseignements sur la personne associée à la méthode du déboursement autre que la personne nommée dans les éléments **DisbursementRequestor** ou **OnBehalfOfIndividual**. |
| Attributs : | **OtherIndividualSequenceNumber**  1 à 999999999 chiffres  Un par **OtherIndividual** |
| Contraintes : | Facultatif  Zéro ou plusieurs par **OtherIndividualInformation** |
| Exemple : | `<OtherIndividual OtherIndividualSequenceNumber="1">…</OtherIndividual>` |
| Commentaires : | Cet élément est obligatoire si **AssociateOtherIndividualCode** =  1 Une autre personne associée |

#### IndividualName (Nom au complet de la personne)

![IndividualName](images/Mod2/image015.gif)

Nom au complet de la personne

| Définition : | Cet élément parent renferme les renseignements sur l'autre personne associée à la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **Other****Individual** |
| Exemple : | ``` <IndividualName>  <Surname>Peters</Surname>  <GivenName>Peter</GivenName>  <MiddleName>P</MiddleName>  </IndividualName> ``` |
| Commentaires : |  |

#### H1 Surname\* (Nom de famille de la personne \*)

![Surname*](images/Mod2/image016.gif)

Nom de famille de la personne

| Définition : | Le nom de famille de l'autre personne associée à la méthode du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<Surname>Peters</Surname>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H2 GivenName\* (Prénom de la personne \*)

![GivenName*](images/Mod2/image017.gif)

Prénom de la personne

| Définition : | Le prénom de l'autre personne associée à la méthode du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<GivenName>Peter</GivenName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H3 MiddleName (Autres noms/initiales de la personne)

![MiddleName](images/Mod2/image018.gif)

| Définition : | Les autres noms ou initiales de l'autre personne associée à la méthode du déboursement |
| Attributs : |  |
| Contraintes : | Facultatif  0 à 30 caractères  Un par **IndividualName** |
| Exemple : | `<MiddleName>P</MiddleName>` |
| Commentaires : |  |

#### H4 AssociateAccountCode (Y avait-il un compte pour cette personne (autre qu'un compte indiqué à la partie G) associé au déboursement?)

![AssociateAccountCode](images/Mod2/image089.gif)

Y avait-il un compte pour cette personne (autre qu'un compte indiqué à la partie G) associé au déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait un compte pour cette personne qui était associé à la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherIndividual** |
| Exemple : | `<AssociateAccountCode>1</AssociateAccountCode>` |
| Commentaires : | Codes :  1 Compte associé  2 Pas de compte associé |

#### Account (Renseignements sur le compte)

![Account](images/Mod2/image090.gif)

Renseignements sur le compte

| Définition : | Cet élément parent renferme les renseignements sur le compte associé à la méthode du déboursement (autre que celui de l'élément **CasinoAccount**). |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **OtherIndividual** |
| Exemple : | ``` <Account>  <FinancialInstitutionName>Bank of BC</FinancialInstitutionName>  <TransitIdentifier>12321</TransitIdentifier>  <AccountIdentifier>234565</AccountIdentifier>  </Account> ``` |
| Commentaires : | Cet élément est obligatoire si **AssociatedAccountCode** =  1 Compte associé |

#### H5 FinancialInstitutionName\* (Nom de l'institution financière \*)

![FinancialInstitutionName*](images/Mod2/image091.gif)

Nom de l'institution financière

| Définition : | Le nom de l'institution financière où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Account** |
| Exemple : | `<FinancialInstitutionName>Bank of BC</FinancialInstitutionName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### H6 TransitIdentifier\* (Numéro de transit \*)

![TransitIdentifier*](images/Mod2/image092.gif)

Numéro de transit

| Définition : | Le numéro de transit ou le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 12 caractères  Un par **Account** |
| Exemple : | `<TransitIdentifier>12321</TransitIdentifier>` |
| Commentaires : |  |

#### H7 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro de compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Account** |
| Exemple : | `<AccountIdentifier>234565</AccountIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### OtherBusinessEntityInformation (Renseignements sur l'autre entité)

![OtherBusinessEntityInformation](images/Mod2/image093.gif)

Renseignements sur l'autre entité

| Définition : | Cet élément parent renferme les renseignements sur l'entité associée à la méthode du déboursement, autre que l'entité nommée à l'élément **OnBehalfOfBusinessEntity**. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par **DisbursementMethodInformation** |
| Exemple : | ``` <OtherBusinessEntityInformation>  <AssociateOtherBusinessEntityCode>1   </AssociateOtherBusinessEntityCode>  <OtherBusinessEntity OtherBusinessEntitySequenceNumber="1">  <BusinessEntityName>Cleansweep Inc</BusinessEntityName>  <AssociateAccountCode>1</AssociateAccountCode>   <Account>    <FinancialInstitutionName>Bank of BC</FinancialInstitutionName>    <TransitIdentifier>12321</TransitIdentifier>    <AccountIdentifier>234565</AccountIdentifier>   </Account>  </OtherBusinessEntity>  </OtherBusinessEntityInformation> ``` |
| Commentaires : |  |

#### F2.7 AssociateOtherBusinessEntityCode (Y avait-il une entité (autre que le casino qui présente la déclaration ou l'entité nommée à la partie D de la présente opération) associée à la méthode du déboursement?)

![AssociateOtherBusinessEntityCode](images/Mod2/image094.gif)

Y avait-il une entité (autre que le casino qui présente la déclaration ou l'entité nommée à la partie D de la présente opération) associée à la méthode du déboursement?

| Définition : | Ce code est utilisé pour indiquer si une autre entité est associée à la méthode du déboursement. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherBusinessEntityInformation** |
| Exemple : | `<AssociateOtherBusinessEntityCode>1  </AssociateOtherBusinessEntityCode>` |
| Commentaires : | Codes :  1 Une autre entité associée  2 Aucune autre entité associée |

#### OtherBusinessEntity (Partie I)

![OtherBusinessEntity](images/Mod2/image095.gif)

OtherBusinessEntity (Partie I)

| Définition : | Cet élément parent renferme les renseignements sur l'autre entité associée à la méthode du déboursement. |
| Attributs : | **OtherBusinessEntitySequenceNumber**  1 à 999999999 chiffres  Un par **OtherBusinessEntityInformation** |
| Contraintes : | Facultatif  Zéro ou plusieurs par **OtherBusinessEntityInformation** |
| Exemple : | `<OtherBusinessEntity OtherBusinessEntitySequenceNumber="1"> … </OtherBusinessEntity>` |
| Commentaires : | Cet élément est obligatoire si   **AssociateOtherBusinessEntityCode** =  1 Une autre entité associée |

#### I1 BusinessEntityName\* (Dénomination sociale complète de l'entité \*)

![BusinessEntityName*](images/Mod2/image060.gif)

Dénomination sociale complète de l'entité

| Définition : | La dénomination sociale complète de l'entité associée à la méthode du déboursement |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **OtherBusinessEntity** |
| Exemple : | `<BusinessEntityName>CleanSweep Inc</BusinessEntityName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### I2 AssociatedAccountCode (Y avait-il un compte pour cette entité (autre qu'un compte indiqué à la partie G) associé au déboursement?)

![AssociatedAccountCode](images/Mod2/image089.gif)

Y avait-il un compte pour cette entité (autre qu'un compte indiqué à la partie G) associé au déboursement?

| Définition : | Ce code est utilisé pour indiquer s'il y avait un compte pour cette personne. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 chiffre  Un par **OtherBusinessEntity** |
| Exemple : | `<AssociateAccountCode>1</AssociateAccountCode>` |
| Commentaires : | Codes :  1 Compte associé  2 Pas de compte associé |

#### Account

![Account](images/Mod2/image090.gif)

Account

| Définition : | Cet élément parent renferme les renseignements sur le compte associé au déboursement (autre que ceux de l'élément **CasinoAccount**). |
| Attributs : |  |
| Contraintes : | Facultatif  Un par **OtherBusinessEntity** |
| Exemple : | ``` <Account>  <FinancialInstitutionName>Bank of BC</FinancialInstitutionName>  <TransitIdentifier>12321</TransitIdentifier>  <AccountIdentifier>234565</AccountIdentifier>  </Account> ``` |
| Commentaires : | Cet élément est obligatoire si **AssociatedAccountCode** =  1 Compte associé |

#### I3 FinancialInstitutionName\* (Nom de l'institution financière \*)

![FinancialInstitutionName*](images/Mod2/image091.gif)

Nom de l'institution financière

| Définition : | Le nom de l'institution financière. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 60 caractères  Un par **Account** |
| Exemple : | `<FinancialInstitutionName>Bank of BC</FinancialInstitutionName>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

#### I4 TransitIdentifier\* (Numéro de transit \*)

![TransitIdentifier*](images/Mod2/image092.gif)

Numéro de transit

| Définition : | Le numéro de transit où le compte est détenu |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 12 caractères  Un par **Account** |
| Exemple : | `<TransitIdentifier>12321</TransitIdentifier>` |
| Commentaires : |  |

#### I5 AccountIdentifier\* (Numéro de compte \*)

![AccountIdentifier*](images/Mod2/image080.gif)

Numéro de compte

| Définition : | Le numéro de compte |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  0 à 30 caractères  Un par **Account** |
| Exemple : | `<AccountIdentifier>234565</AccountIdentifier>` |
| Commentaires : | Cet élément ne doit pas être vide si **TwentyFourHourRuleCode** =  0 Règle de 24 heures ne s'applique pas |

### 2.8 Éléments compris dans la fin de lot

La fin de lot indique la fin des déclarations comprises dans le fichier.

#### ReportSubmissionFileTrailer (Fin de lot)

![ReportSubmissionFileTrailer](images/Mod2/image100.gif)

Fin de lot

| Définition : | Cette balise parent renferme l'élément de la fin de lot. |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  Un par fichier transmis |
| Exemple : | ``` <ReportSubmissionFileTrailer>  <ReportCount>750</ReportCount>  </ReportSubmissionFileTrailer> ``` |
| Commentaires : |  |

#### ReportCount (Nombre de déclarations)

![ReportCount](images/Mod2/image101.gif)

Nombre de déclarations

| Définition : | Nombre de déclarations dans le fichier transmis par lot |
| Attributs : |  |
| Contraintes : | Obligatoire aux fins de traitement  1 à 999999999 chiffres  Un par **ReportSubmissionFileTrailer** |
| Exemple : | `<ReportCount>750</ReportCount>` |
| Commentaires : |  |

  

## 3. Diagramme de production d'une déclaration relative à un déboursement de casino (DDC ou « CDR »)

![Diagramme de production d'une déclaration relative à un déboursement de casino (DDC ou « CDR ») image 1](images/Mod2/image102fra.gif)

![Diagramme de production d'une déclaration relative à un déboursement de casino (DDC ou « CDR ») image 2](images/Mod2/image103fra.gif)

![Diagramme de production d'une déclaration relative à un déboursement de casino (DDC ou « CDR ») image 3](images/Mod2/image104fra.gif)

Date de modification :
:   2017-06-29