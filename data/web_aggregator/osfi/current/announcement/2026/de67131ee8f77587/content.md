# Précisions au sujet de l’appel de données sur les prêts aux entreprises

Information

Type de document

Instructions

Secteur

Institutions de dépôt

Table des matières

Documents connexes

* [Appel de données transactionnelles sur les prêts aux entreprises – Phase 3 (BSIF 965)](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/appel-donnees-transactionnelles-sur-prets-entreprises-phase-3-bsif-965)
* [Appel de données transactionnelles sur les prêts aux entreprises – Phase 3 (BSIF 988)](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/appel-donnees-transactionnelles-sur-prets-entreprises-phase-3-bsif-988)

Avant de soumettre vos réponses à notre appel de données sur les prêts aux entreprises, veuillez prendre connaissance des précisions ci-dessous.

## Resoumettre les fichiers

Si vous devez resoumettre une déclaration pour corriger 1 ou plusieurs tableaux, veuillez resoumettre les 4 tableaux au complet (c’est-à-dire, les tableaux intitulés Emprunteur, Facilité, Sûreté et Projet d’aménagement).

## Exclusions de cet appel de données

### Appel de données sur les prêts garantis par un bien immobilier (RESL)

Si vous avez déclaré un bien dans l’appel de données sur les prêts garantis par un bien immobilier (RESL), **ne** l’incluez **pas** dans la déclaration de l’appel de données sur les prêts aux entreprises.

### Prêts hors bilan

L’appel de données sur les prêts aux entreprises exclut les prêts hors bilan, comme les prêts garantis par la Société canadienne d’hypothèques et de logement qui font partie d’un véhicule de titrisation, ou les prêts autorisés mais non financés.

### Découverts

Si le découvert n’est pas lié à une facilité distincte, veuillez **ne pas** l’inclure dans votre déclaration à l’appel de données sur les prêts aux entreprises.

## Considérations à l’égard des déclarations

### Valeurs nulles

Pour indiquer les valeurs nulles (c’est-à-dire, s’il n’y a pas de donnée à inscrire dans un champ précis), veuillez laisser le champ vide, sans caractère et sans espace. Par exemple, n’écrivez pas « S.O. », « nul », « », « - ». Les barres verticales (pipes) d’un point de données d’une valeur nulle doivent être côte à côte (« || ») sans caractère ou espace entre les deux.

### Niveau de détail

Veuillez déclarer chacune des facilités de la façon la plus détaillée possible, c’est-à-dire au niveau où sont définis le taux d’intérêt, le terme de la facilité, l’échéance, etc.

## Précisions sur certains champs de données

120 Ratio prêt-valeur (RPV) de l’emprunteur (emprunteur\_rpv\_actuel)
:   Pour la **valeur marchande courante totale**, utilisez l’évaluation la plus récente (peut être une évaluation interne). Conformément à la [version révisée de l’avis relatif à la réglementation sur l’octroi de prêts immobiliers commerciaux](/fr/consignes/repertoire-consignes/gestion-du-risque-lie-limmobilier-commercial "Version révisée de l’avis relatif à la réglementation sur l’octroi de prêts immobiliers commerciaux").

    Indiquez **le RPV au niveau de l’emprunteur** seulement si votre institution le calcule. Veuillez laisser ce champ vide si la donnée n’est pas disponible.

220 Amortissement contractuel (actuel) (facilite\_amortissement\_contractuel)
:   Si la facilité n’a pas d’amortissement (par exemple, s’il s’agit d’un prêt avec paiement différé du principal qui a un terme mais pas d’amortissement), vous devez inscrire **nul** dans le champ de l’**amortissement contractuel** plutôt que 0.

221 Mensualité (facilite\_mensualite)
:   Les versements facultatifs ou imprévus, comme les remboursements anticipés, ne sont pas inclus dans le champ des **mensualités**. Indiquez les mensualités contractuelles seulement.

224 Intérêts capitalisés (facilite\_interets\_capitalises)
:   Les **intérêts capitalisés** doivent correspondre seulement aux intérêts qui ont été capitalisés pendant la période de déclaration et demeurent capitalisés à la date limite de déclaration.

227 Rôle dans le syndicat financier ou la participation (facilite\_syndicate\_participant\_role)
:   Définitions de participation ou syndication :

    * **Participation** : Le prêteur participant n’est pas le créancier direct de l’emprunteur.
      + Il s’agit habituellement d’une entente juridique entre l’émetteur et le prêteur participant.
    * **Syndication** : Chacun des prêteurs est un créancier direct de l’emprunteur.

304 Valeur d’expertise de la sûreté (surete\_valeur\_dexpertise)
:   Calculez au prorata pour les prêts par syndication et les prêts par participation.

306 Valeur estimée de la sûreté (surete\_valeur\_estimee)
:   Calculez au prorata pour les prêts par syndication et les prêts par participation.

316 Indicateur de sûreté principale (surete\_ind\_principale) (pour la version COMPLÈTE du gabarit BSIF988)
:   S’il n’y a qu’**une** (1) seule sûreté (et non plusieurs) pour cette facilité, nous considérons qu’il s’agit de la sûreté principale. Écrivez « 1 ».

    S’il existe plusieurs sûretés sur le prêt, veuillez préciser la sûreté qui est considérée comme principale dans vos systèmes internes et en fonction d’autres déclarations réglementaires.

    Veuillez noter que le BSIF procédera au rapprochement des données de cet appel avec les données d’autres déclarations où sont ventilés les types de bien, comme dans BSIF980 et E-2.

414 Montant de l’engagement (projet\_montant\_de\_lengagement)
:   Veuillez saisir le montant maximal que le prêteur s’engage contractuellement à financer/à avancer au moment où les conditions de l’entente sont confirmées et respectées. Le financement n’est pas un prêt à vue.

    S’il y a 2 facilités (ou plus), assorties de différents pourcentages de syndication et associées à un seul projet, le **montant de l’engagement** du projet doit correspondre à l’engagement contractuel, calculé au prorata selon le pourcentage de syndication de chacune des facilités.

    Si aucun montant n’a été engagé, veuillez inscrire zéro (« 0 »).

    Calculez le montant de ce champ au prorata pour les prêts par syndication et les prêts par participation.

Signaler un problème ou une erreur sur cette page

Date de modification :
:   2024-12-04