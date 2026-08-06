# Relevé des normes de fonds propres de Bâle (RNFPB) FAQ – Spécifications techniques

Information

Type de document

FAQ

Secteur

Institutions de dépôt

Relevé

Relevé des normes de fonds propres de Bâle (RNFPB)

Dernière révision

26 février 2024

Documents connexes

* [Relevé des normes de fonds propres de Bâle (RNFPB) 2026](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/releve-normes-fonds-propres-bale-rnfpb-2026)

## 1. Introduction

Le BSIF a désigné un relevé aux fins de l’appel de données du Relevé des normes de fonds propres de Bâle (RNFPB). Ce relevé doit être soumis au BSIF au moyen du système de base de données tripartite, le Système de déclaration réglementaire (SDR). Le présent document met en évidence la disposition et le format du fichier technique de ce relevé.

### Bibliographie

Veuillez noter que le « XX » dans l’année indique le début de la prochaine période de rapport financier.

Vous pouvez télécharger ces fichiers à l’adresse suivante :

[Relevé des normes de fonds propres de Bâle (RNFPB) (BA)](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/releve-normes-fonds-propres-bale-rnfpb-2026 "Relevé des normes de fonds propres de Bâle (RNFPB) 2026")

## 2. Concepts et termes de base

Dans cette section, nous expliquons un certain nombre de concepts et de termes liés à la façon dont les données sont organisées dans un fichier de données du relevé. Nous décrivons d’abord la façon de lire le nouveau gabarit du RNFPB, puis nous passons aux enregistrements des dimensions et des mesures. Ensuite, ces concepts sont liés aux types d’enregistrements, qui spécifient un regroupement d’enregistrements dimensionnels que vous fournirez dans votre fichier de données du relevé.

Le changement le plus important apporté au fichier de données du relevé est qu’il utilise le format XML plutôt que le format .dat existant. Le langage de balisage extensible (XML) vous permet de définir et de stocker des données de manière partageable. XML prend en charge l’échange d’information entre les systèmes informatiques comme les sites Web, les bases de données et les applications de tiers.

### 2.1. Comment lire les nouveaux gabarits du RNFPB

Le RNFPB peut être divisé en deux concepts : le format conventionnel de la collecte des données et le format dimensionnel de la collecte des données.

Les cellules conventionnelles sont celles où doit figurer une valeur dans un seul emplacement ou une seule cellule.

Il n’y a pas de dimensionnalité supplémentaire. Elles sont identifiées par des numéros d’adresse de point de données (APD) à quatre ou cinq chiffres.

À titre d’exemple, citons l’APD 1001, qui figure au tableau 10.010 et désigne le ratio de fonds propres de catégorie 1 (%). La représentation de ces APD de quatre ou cinq chiffres demeure la même dans la nouvelle définition du RNFPB.

Les cellules dimensionnelles ne sont pas rattachées à un numéro unique. Ce sont celles où figurent une combinaison de codes de dimensions et une mesure. Les cellules ne sont pas numérotées individuellement.

## 3. Dimensions, mesures et catégories d’information (types d’enregistrements)

### 3.1. Dimensions

Une dimension est une liste de catégories opérationnelles qui sont regroupées sous un seul concept opérationnel. Le RNFPB comporte huit dimensions, comme l’indique la liste ci-dessous. Il convient de noter que le cadre de double défaut (DD) constituait auparavant une dimension, mais qu’il n’est plus déclaré.

Identifiant de dimension

* Type d’approche (APPROACH\_TYPE)
* Catégorie d’exposition  (EXP\_CL)
* Type de risque (RISK\_TYPE)
* Type d’actions (EQUITY\_TYPE)
* Type d’exposition (EXP\_TYPE)
* Tranche de PD (PD)
* Coefficient de pondération du risque (RISK\_WEIGHT)
* Pays (COUNTRY)

### 3.2. Codes de dimension

Les codes de dimension correspondent aux valeurs spécifiques associées à chaque dimension. Chaque code de dimension est identifié par une étiquette et un identifiant de dimension.

Par exemple, les codes de dimension suivants font partie de la catégorie d’exposition, mais sans s’y limiter.

* Expositions sur les emprunteurs souverains (106)
* Expositions sur les entités du secteur public (ESP) (120)
* Expositions sur les banques multilatérales de développement (BMD) (121)
* Expositions sur les banques (à l’exclusion des obligations sécurisées) (107)

Le nombre de codes de dimension utilisés peut changer à chaque cycle de gestion interne.

On trouvera la liste complète de tous les codes de dimension et de leur utilisation ici :

BSIF, « Spécifications techniques – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.

### 3.3. Mesures

Les mesures sont des adresses ou des cellules précises qui représentent une valeur qui doit être déclarée.

Habituellement, une mesure est une cellule unique comportant une combinaison valide de codes de dimension.

On trouvera la liste complète de toutes les mesures et de leur utilisation ici :

BSIF, « Spécifications techniques – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.

### 3.4. Catégories de renseignements (types d’enregistrement)

Le BSIF est chargé de recueillir et d’évaluer plusieurs catégories générales de renseignements. Chaque catégorie de renseignements est définie par un ensemble de dimensions et de mesures.

Veuillez noter que l’enregistrement de type 025 n’est plus recueilli.

Types d’enregistrement

| Type d’enregistrement | Description |
| --- | --- |
| 005 | Méthode standard de calcul des actifs pondérés en fonction du risque de crédit |
| 010 | Expositions déclarées selon l’approche générale NI |
| 015 | Le financement spécialisé est une sous catégorie des expositions sur entreprises à l’égard de laquelle l’institution déclarante ne satisfait pas aux exigences d’estimation de la PD et à laquelle elle ne peut appliquer les formules de pondération en fonction du risque. L’institution doit alors utiliser une approche de classement prudentiel pour calculer les actifs pondérés en fonction du risque. |
| 030 | Dans les catégories des expositions sur les entreprises et sur la clientèle de détail, les débiteurs rachetés admissibles font l’objet d’un traitement particulier selon lequel les actifs pondérés en fonction des risques sont calculés séparément pour le risque de défaut et le risque de dilution. |
| 035 | Les mesures relatives aux créances achetées admissibles à un traitement spécial sont saisies dans ce type d’enregistrement ainsi que dans les créances achetées. |
| 040 | Les prêts hypothécaires inversés font l’objet d’un régime spécial au regard des normes de fonds propres énoncé dans le préavis Régime de fonds propres visant les prêts hypothécaires inversés. |
| 045 | Prêts hypothécaires inversés à déduire des fonds propres, comme l’indique le préavis Régime de fonds propres visant les prêts hypothécaires inversés |
| 050 | Exigence relative à la réserve contracyclique |
| 055 | Réserve contracyclique pour les PMB de catégorie III |

On trouvera la liste complète de toutes les mesures et de leur utilisation ici :

BSIF, « Spécifications techniques – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.

### 3.5. Combinaisons non valides (trous)

Une combinaison non valide connue sous le nom de trou est un cas où une valeur n’est pas requise. Cela ne s’applique qu’au RNFPB pour le moment, mais pourrait être éventuellement étendu à d’autres relevés. Un trou est identifié par une cellule grise.

**Trous de mesure**– Un trou de mesure est une cellule unique où une valeur n’est pas requise.

**Trous dimensionnels**– Un trou dimensionnel est une série de trous de mesure pouvant apparaître ou non dans le tableau. Souvent, le trou dimensionnel n’apparaît pas. Dans l’exemple du tableau 40.050, le type d’enregistrement 005 est défini comme regroupant plusieurs types d’expositions (EXP\_TYPE), mais seulement trois sont affichés pour la saisie des données :

* Types d’expositions (EXP\_TYPE) = Engagements utilisés (501)
* Types d’expositions (EXP\_TYPE) = Engagements inutilisés (502)
* Types d’expositions (EXP\_TYPE) = Autres éléments hors bilan (505)

Plusieurs types d’exposition ne sont pas requis pour ce tableau :

À noter que Type d’exposition (EXP\_TYPE)= Transaction assimilable à des pensions (503) est absent du tableau 40.150 – Type d’enregistrement 005, bien qu’il figure sur la liste des valeurs permises.

Étant donné qu’aucune valeur n’est requise pour toute la gamme de mesures pour ce type d’exposition, il ne figure tout simplement pas au tableau. S’il y figurait, toutes ses valeurs seraient en grisé. C’est un trou dimensionnel.

Ne soumettez pas de données pour les trous de mesure ou les trous dimensionnels, sinon vous recevrez un message d’erreur de validation.

## 4. Exigences de présentation

Les sections suivantes décrivent la disposition du fichier d’extraction du RNFPB requise par le SDR.

### 4.1. Type de fichier et convention de désignation des fichiers

Le RNFPB soumis est recueilli en format XML.

XML prend en charge l’échange d’information entre les systèmes informatiques comme les sites Web, les bases de données et les applications de tiers.

Il n’y a aucune exigence quant au nom du fichier à soumettre.

Un fichier XSD et un exemple de fichier XML sont disponibles sur le site Web du BSIF. Une définition de schéma XML (XSD) est un document-cadre qui définit les règles et les contraintes des documents XML.

On trouvera ici la liste exacte de l’ensemble des types d’enregistrement, dimensions, codes de dimension et mesures :

BSIF, « Spécifications techniques – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.

### 4.2. Structure des fichiers de présentation – Points de données conventionnels

Lorsque vous créez un fichier de présentation pour une APD classique à quatre ou cinq chiffres, veuillez noter ce qui suit :

1. Déterminez le point de données pour lequel vous souhaitez soumettre une valeur. Voir :

   BSIF, « RNFPB de 20XX – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.
2. Par exemple, le point de données 5615 se trouve dans le tableau 10.050 (Cellule D27).
3. Dans le document « RNFPB en XML – à compter du TX 20XX », à des fins d’exemple seulement, la valeur représente le numéro du point de données.
4. Les balises autour de la valeur identifient le numéro du point de données par la formule « \_x003 » + premier chiffre du point de données + soulignement + 3 ou 4 autres chiffres du point de données ».

```
35 <_x0035_615>
36   <value>5615</value>
37 </_x0035_615>
```

5. Dans le document XSD RNFPB (RNFPB en XSD – à compter du TX 20XX), cette valeur de balise peut être liée au XSD pour trouver des détails comme le type de données et la hiérarchie des autres éléments parents.

```
82633 <xs:element minOccurs="0" maxOccurs="1" name="BA-6">
82634   <xs:annotation>
82635    <xs:documentation>BA-6</xs:documentation>
82636  </xs:annotation>
82637  <xs:complexType>
82638     <xs:all>
82639      <xs:element minOccurs="0" maxOccurs="1" name="_x0035_615">
82640         <xs:annotation>
...
82642        </xs:annotation>
82643        <xs:complexType>
82644          <xs:complexContent mixed="false">
82645            <xs:extension base="Whole_x0020_Number">
```

### 4.3. Structure des fichiers de présentation – Points de données dimensionnels

La section de présentation dimensionnelle du XML peut être créée et définie en suivant la même logique que les présentations conventionnelles.

1. Déterminez la plage dimensionnelle pour laquelle vous souhaitez soumettre des données.

   BSIF, « RNFPB de 20XX – à compter du TX 20XX », feuille de calcul Microsoft Excel, publication non classifiée du BSIF.
2. Dans le tableau 40.010, nous savons que nous souhaitons soumettre des données pour les codes dimensionnels suivants :
   * Type d’enregistrement = 005 (Cellule de référence A4)
   * Catégorie d’exposition = Emprunteurs souverains (106) (Cellule de référence A3)
   * Type d’exposition = Engagements inutilisés (502) (Cellule de référence A20)
   * Coefficient de pondération du risque = 20 % coté (804) (Cellule de référence A22) Mesure = Montant de principal notionnel (M12) (Cellule de référence B7)
3. L’exemple de fichier XML du RNFPB en XML – à compter du TX 20XX peut être examiné pour voir comment les éléments sont présentés sur les lignes 18191, 18199, 18202.

Exemple de fichier XML du RNFPB, indiquant les balises XML que voici : à la ligne 18191, balise d’une valeur autour de 106, à la ligne 18199, balise d’une valeur autour de 502, à la ligne 18202, balise d’une valeur autour de 804, et à la ligne 18205, balise d’une valeur autour de 120.

```
18187 <BCAR>
18188   <_x0030_05>
18189     <_x0030_05_x0020_Repeat_x0020_Group>
18190       <EXP_CL>
18191         <value>106</value>
18192       </EXP_CL>
18193       <Standardized>
18194         <StandardizedTable>
...
18197        <StandardizedTable_x0020_Repeat_x0020_Group>
18198              <EXP_TYPE>
18199                <value>502</value>
18200      </EXP_TYPE>
18201               <RISK_WEIGHT>
18202                 <value>804</value>
18203       </RISK_WEIGHT>
18204       <M12>
18205                  <value>120</value>
18206       </M12>
18207       <M13>
18208         <value>130</value>
18209       </M13>
```

Dans le document XSD du RNFPB (RNFPB en XSD – à compter du TX 20XX), cette valeur de balise peut être liée au XSD pour trouver des détails comme le type de données et la hiérarchie des autres éléments parents. Par exemple, les lignes 154318 et 154324. La hiérarchie peut être différente pour chaque type d’enregistrement.

RNFPB en XSD – à compter du TX 20XX

Dans le document RNFPB XSD, indiquant les balises XML que voici  : à la ligne 154318, <xs:element minOccurs=“0” maxOccurs=“1” name=“EXP\_CL”>, et à la ligne 154324, <xs:extension base=“EXP\_CL”>.

```
154311  <xs:all>
154312    <xs:element minOccurs="0" maxOccurs="1" name="_x0030_05">
154313      <xs:complexType>
154314        <xs:sequence minOccurs="0" maxOccurs="unbounded">
154315          <xs:element minOccurs="1" maxOccurs="1" name="_x0030_05_x0020_Repeat_x0020_Group">
154316        <xs:complexType>
154317       <xs:all>
154318         <xs:element minOccurs="0" maxOccurs="1" name="EXP_CL">
154319        <xs:annotation>
154320          <xs:documentation>BCAR Exposure Classes / RNFPB - Catégories d'exposition</xs:documentation>
154321        </xs:annotation>
154322        <xs:complexType>
154323          <xs:complexContent mixed="false">
154324         <xs:extension base="EXP_CL">
154325           <xs:attribute default="item" name="type" />
154326         </xs:extension>
154327       </xs:complexContent>
154328        </xs:complexType>
154329      </xs:element>
154330        <xs:element minOccurs="0" maxOccurs="1" name="Standardized">
154331          <xs:annotation>
154332         <xs:documentation>Standardized</xs:documentation>
154333       </xs:annotation>
154334       <xs:complexType>
154335         <xs:all>
```

## 5. Foire aux questions

**Q: Que faire si je n’ai rien à soumettre pour un point de données ou une mesure en particulier?**
:   R : Si, par exemple, vous ne souhaitez pas soumettre de valeur pour le point de données 5615, il suffit d’omettre les balises d’élément et les balises de valeur. Ne soumettez pas de balises de valeur vides, car cela entraînera une erreur structurelle.

    Non valide – affichera une erreur

    ```
    35 <_x0035_615>
    36   <value>|</value>
    37 </_x0035_615>
    ```

    Omettez plutôt complètement les balises d’éléments et les balises de valeur.

**Q : Pour la présentation dimensionnelle, la structure de tous les types d’enregistrement est-elle la même?**
:   R : La hiérarchie dans la présentation des éléments est la même pour les types d’enregistrement 005, 010, 030 et 035. Veuillez consulter l’exemple de fichier XML et le fichier XSD pour plus de détails.

    BSIF, « RNFPB en XML – à compter du TX 20XX», Fichier XML, publication non classifiée du BSIF.

    Fichier XML qui peut être utilisé comme exemple de relevé à produire.

    BSIF, «RNFPB en XSD – à compter du TX 20XX», fichier XSD, publication non classifiée du BSIF.

    Fichier XSD qui définit l’exemple de fichier de relevé à produire.

**Q : Pourquoi certaines balises d’éléments XML semblent elles être mises en correspondance avec les calendriers de déclaration alors que d’autres semblent plus arbitraires?**
:   R : À l’instar d’autres systèmes internes, le SDR est utilisé par les trois organismes – le BSIF, la Banque du Canada et la SADC. Les différents éléments XML sont utilisés pour assurer la compatibilité entre les systèmes internes des trois organismes. Veuillez consulter l’exemple de fichier XML et le fichier XSD pour connaître les bons éléments à utiliser.

**Q : Que dois je faire si je reçois un message d’erreur de règle ou d’erreur structurelle que je ne comprends pas?**
:   R : Veuillez faire parvenir un courriel à l’adresse [RRSsupport-SDRsoutien@osfi-bsif.gc.ca](mailto:RRSsupport-SDRsoutien@osfi-bsif.gc.ca).

## 6. Suivi des versions

Suivi des versions

| Version | Date | Auteur | Description |
| --- | --- | --- | --- |
| 1.0 | 14 juillet 2023 | Deniz Berkin | Document créé |
| 1.1 | 19 février 2024 | Deniz Berkin | Modifié pour RNFPB 2024 |

Signaler un problème ou une erreur sur cette page

Date de modification :
:   2024-02-26