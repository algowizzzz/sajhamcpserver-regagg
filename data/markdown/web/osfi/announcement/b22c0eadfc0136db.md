---
title: "H4 – Foire aux questions | Bureau du surintendant des institutions financières"
regulator: "osfi"
doc_type: "announcement"
status: "final"
source_kind: "web"
source_url: "http://www.osfi-bsif.gc.ca/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/h4-foire-questions"
version: "1"
---

# H4 – Foire aux questions

Information

Type de document

FAQ

Secteur

Institutions de dépôt

Relevé

Relevé des sûretés et des opérations de nantissement (H4)

Dernière révision

Mai 2023

Numéro de relevé

H4

Documentation

* [Relevé des sûretés et des opérations de nantissement (H4)](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/releve-suretes-operations-nantissement-h4)

## Déclaration et méthodes

1. À quelle catégorie appartiennent les opérations sur dérivés de gré à gré avec les gouvernements et banques centrales à l’étranger (Partie B, Section 2)?

**Réponse** : Par souci de cohérence avec les règles de validation et les normes de déclaration applicables aux relevés H4, veuillez classer ces opérations dans la catégorie Autres contreparties – Partie B, Section 6; Contreparties étrangères (b155).

2. À quelle catégorie appartiennent les opérations sur dérivés de gré à gré avec les organismes gouvernementaux canadiens – Partie B, Section 1?

**Réponse** : Par souci de cohérence avec les règles de validation et les normes de déclaration applicables aux relevés H4, veuillez classer ces opérations dans la catégorie Autres contreparties – Partie B, Section 6; Autres contreparties canadiennes (b147).

3. Quelle est la méthode de déclaration indiquée pour les titres hypothécaires garantis en vertu de la *Loi nationale sur l’habitation* (titres hypothécaires LNH) et pour les Obligations hypothécaires du Canada (OHC)?

**Réponse :**

* Sous-partie Au bilan
  + Les titres hypothécaires LNH émis par l’organisme même doivent être déclarés sous Prêts (a11-a14).
  + Les titres hypothécaires LNH achetés sur le marché secondaire doivent être déclarés sous Valeurs mobilières – position longue (valeur nette) (a5).
* À la sous-partie Au bilan, les titres hypothécaires LNH remis en nantissement dans le cadre du programme des OHC sont déclarés sous Prêts financés par titrisation (a13).
* À la sous-partie Mouvements des sûretés, les sûretés engagées dans le cadre du programme des OHC sont déclarées sous Sûretés applicables à d’autres financements par prêt garanti (a70) ou SORTIE d’autres sûretés (a71).

4. Quelle est la ventilation indiquée pour les opérations liées à la CLS?

**Réponse** : Les opérations liées à la CLS sont traitées par le Système de transfert de paiements de grande valeur (STPGV), qui fonctionne sous la supervision de la Banque du Canada. Comme les opérations de nantissement que les banques canadiennes sous réglementation fédérale effectuent avec la CLS passent par la Banque du Canada, elles doivent être déclarées sous Organismes gouvernementaux canadiens – Partie B, Section 1; Banque du Canada, STPGV (b1). Les filiales étrangères de banques canadiennes effectuant des opérations de nantissement dans le cadre d’activités liées à la CLS doivent affecter leur montant respectif à la contrepartie concernée dans leur pays d’exercice.

5. Pourquoi le Système de déclaration réglementaire (SDR) donne-t-il une échéance de déclaration différente de celle indiquée dans les directives?

**Réponse** : En raison des limites du SDR, la date réelle de transmission ne correspond pas aux dates de fin générées automatiquement par le système. Tous les relevés dûment remplis les jours ouvrables d’un mois de référence doivent être transmis dans les 35 jours civils suivant le dernier jour ouvrable de ce mois.

Exemple : Les relevés H4 remplis du 1er au 31 juillet 2017 devaient être transmis le 5 septembre 2017 au plus tard (soit 35 jours civils après le dernier jour ouvrable du mois). Comme le 4 septembre 2017 était un jour férié en Ontario, la date d’échéance tombait le 5 septembre 2017. En effet, si la date d’échéance tombe un jour férié en Ontario, elle est reportée au jour ouvrable suivant.

## Transmissions dans le SDR

1. Fichier XML : Est-il possible de supprimer les adresses de points de données dans le fichier XML si leur valeur est nulle ou si la zone correspondante reste vide?

**Réponse :** Oui, les adresses de points de données peuvent être supprimées dans ces cas-là. Veillez à retirer toutes les identifications liées au fichier XML dans les adresses de référence des points de données. Pour vous faciliter la tâche, reportez-vous à la capture d’écran ci-dessous. En cas de suppression des adresses de points de données, retirez le code surligné en noir.

![Capture d'écran montrant le code xml qui peut être retiré en cas de suppression des adresses de points de données](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2023-05/fr/H4_FAQ_img1.png)

2. Fichier XML : Est-il possible de supprimer la Section B si elle n’a pas lieu d’être?

**Réponse** : Oui, il est possible de la supprimer si elle n’est pas pertinente pour l’institution déclarante. Veillez à retirer toutes les identifications liées au fichier XML dans la Section B. Reportez-vous aux captures d’écran ci-dessous. Si la section B n’a pas lieu d’être, retirez tous les codes situés entre <B type =“group”> et </B>.

![Capture d'écran montrant le code xml qui peut être retiré si la section B ne s’applique pas](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2023-05/fr/H4_FAQ_img2.png)

3. Fichier XML : Est-il possible de modifier l’agencement des groupes d’adresses de points de données dans le gabarit de fichier XML?

**Réponse** : Le gabarit de fichier XML ne suit pas de logique particulière. Toutefois, comme les adresses de points de données ont été intégrées à un groupe en fonction de ce gabarit, il est impératif d’utiliser le même mode d’agencement.

4. À quelle fréquence faut-il faire une déclaration?

**Réponse** : Pour la phase de test (relevé non structuré), il faut soumettre un fichier XML ou une feuille de calcul Excel par classeur à chaque date de fin de relevé du SDR. Si le relevé est structuré, il ne faut soumettre qu’un fichier XML par date correspondante de fin de relevé du SDR.

5. Dans le cas du relevé H4, qu’entend-on par date de fin de relevé du SDR?

**Réponse** : La date inscrite sur le relevé transmis doit correspondre à la date de fin de relevé du SDR. Par exemple, si le relevé est transmis le 1er août 2017, la date de fin de relevé du SDR est aussi le 1er août. Seule exception : s’il s’agit de la phase de test (relevé non structuré), les institutions financières ont le droit de transmettre leur relevé dans les trois jours suivant la dernière date du mois.

6. Est-il possible de faire tester un fichier XML?

**Réponse** : Si une institution financière veut faire tester le format XML et les règles de validation en cas de transmission d’un fichier XML, elle peut en faire la demande par courriel. Elle devra donner d’autres renseignements concernant la période de déclaration (la date de la transmission).

7. Comment régler les problèmes touchant les règles de validation d’un relevé structuré H4?

**Réponse** : La méthode la plus efficace consiste à comparer l’ID de la règle sur le portail SDR avec la feuille de calcul des règles de validation qui est fournie par la Banque du Canada.

Signaler un problème ou une erreur sur cette page

Date de modification :
:   2023-11-17