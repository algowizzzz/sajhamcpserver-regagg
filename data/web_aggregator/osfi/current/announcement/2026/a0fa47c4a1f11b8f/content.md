# Données de crédit selon l'approche NI du portefeuille de la clientèle de gros – Partie 1 (BB)

Information

Type de document

Spécifications techniques

Secteur

Institutions de dépôt

Relevé

Données de crédit selon l’approche NI du portefeuille de la clientèle de gros – Partie 1 (BB)

Dernière révision

Août 2017

Version

6.4

Table des matières

## Relevés

[BB - Définition des données (XLS, 658,5 Ko)](/sites/default/files/import-media/data_and_forms/data-definitions/2023-08/fr/ws_prt_cdd.xls) [BB - Règles de validation (XLSX, 145,34 Ko)](/sites/default/files/documents/bb-validation-fr.xlsx "bb-validation-fr.xlsx")

## Spécifications techniques

Pour les relevés produits à compter du T1 2018

### 1. Introduction

Un relevé en deux parties a été établi pour l'appel de données relatif aux portefeuilles de la clientèle de gors assujettis à l'approche NI. Ces deux parties doivent être présentées au BSIF par l'entremise du Système de déclaration réglementaire (SDR). Les définitions des données du premier fichier se trouvent dans le document [1]. Ce document précise les spécifications techniques concernant la présentation et le format du fichier, ainsi que les règles de validation des données et les messages d'erreur et avertissements connexes. Le document des spécifications techniques constituera le principal ouvrage de référence lorsque le relevé n'est pas complètement au diapason avec les définitions des données [1].

Les définitions des données contenues dans ce fichier sont expliquées dans le document [2], alors que les spécifications techniques se trouvent dans le document [3].

#### 1.1. Bibliographie

[1] BSIF, Données sur le risque de crédit – Définition des secteurs d'activité et des données selon l'approche fondée sur les notations internes (NI) avancée; Portefeuille de la clientèle de gros (Partie 1), chiffrier Microsoft Excel, mars 2007, publication non classifiée du BSIF.

[2] BSIF, Données sur le risque de crédit – Définition des secteurs d'activité et des données selon l'approche fondée sur les notations internes (NI) avancée; Portefeuille de la clientèle de gros (Partie 2), chiffrier Microsoft Excel, mars 2007, publication non classifiée du BSIF.

[3] BSIF, Données sur le crédit selon l'approche fondée sur les notations internes – Données du portefeuille de la clientèle de gros (Partie 2), Spécifications techniques – Présentation du fichier et règles de validation des données, document Microsoft Word, mars 2007, publication non classifiée du BSIF.

### 2. Concepts fondamentaux et terminologie

La présente section explique différents concepts et termes liés à l'organisation des données dans les fichiers des relevés, à commencer par les concepts de « catégories de données », de « dimensions » et d'« enregistrements ». Un lien est ensuite établi entre ces concepts et les « structures d'enregistrement », qui précisent l'ensemble des enregistrements de longueur fixe à fournir dans les fichiers de données des relevés.

#### 2.1. Catégories de données et dimensions

Le BSIF est chargé de recueillir et d'évaluer des données appartenant à plusieurs catégories générales, qui constituent des indicateurs de l'importance de l'exposition d'une institution financière au risque de crédit. Chaque catégorie de données est définie par un ensemble de dimensions.

Ainsi, dans la partie 1 du relevé du portefeuille de la clientèle de gros assujetti à l'approche NI, on recueille pour la catégorie de données définie par les quatre dimensions, SNR, NIRE, Industrie et Catégorie d'exposition des mesures comme « Facilités autorisées », « Encours », « ECD estimative selon l'approche NI », « Pertes prévues selon l'approche NI » et « Pertes économiques ». Les valeurs des données appartenant à différents ensembles de mesures, notamment « Total des provisions pour pertes sur créances », « Provisions individuelles pour pertes sur créances » et « Acceptations et prêts de crédit douteux », sont recueillies dans la catégorie de données représentée par la dimension unique Région géographique.

Les catégories de données et les dimensions de ce relevé sont présentées en détails à la section 4, Exigences relatives au fichier d'extraction des données.

#### 2.2. Enregistrements et valeurs de clé

Toutes les dimensions qui définissent une catégorie de données sont assorties d'un ensemble de « valeurs de clé ». Par exemple, dans le relevé du portefeuille de la clientèle de gros assujetti à l'approche NI, la dimension Industrie est assortie de valeurs de clé représentant les types d'industrie (p. ex., « agriculture », « construction », « défense », etc.), alors que la dimension Catégorie d'exposition est assortie de valeurs de clé représentant les catégories d'exposition au risque de crédit (p. ex., « entreprises », « banques », « emprunteurs souverains », etc.). Les dimensions du relevé visé par le présent document et les valeurs de clé qui y sont associées sont décrites à la section 4.4, Types de dimension.

En vertu de la loi, les institutions financières sont tenues de déclarer les données de mesure correspondant à **toutes les combinaisons valides de ces valeurs de clé**. Par conséquent, vous devez fournir un « enregistrement » (renfermant les valeurs des données déclarées pour chaque mesure) pour chaque combinaison de valeurs de clé d'une catégorie de données, ainsi que pour chaque catégorie de données. Il importe de souligner que les types de mesure déclarés pour une catégorie de données particulière peuvent différer de celles d'une autre catégorie de données.

En d'autres mots, lorsqu'on prépare un fichier de données pour un relevé, on déclare les données sous forme d'une série d'enregistrements de longueur fixe (380 caractères). Chaque enregistrement est séparé de celui qui le suit dans le fichier de données texte par un caractère de retour de chariot (RC) et par un caractère de saut de ligne (SL) (chaque enregistrement se trouve donc sur une ligne distincte dans le fichier). Les enregistrements du fichier de données comprennent un ensemble de mesures pour chaque catégorie de données, comme on l'explique dans la définition des structures d'enregistrement à la section 2.3 ci-dessous. Les enregistrements appartenant à une catégorie de données particulière comprennent une mesure pour chaque combinaison valide de valeurs de clé associée aux dimensions de cette catégorie de données. Tous les enregistrements d'une même catégorie de données contiennent des valeurs pour les mêmes types de mesure.

Prenons par exemple la première partie du relevé du portefeuille de la clientèle de gros assujetti à l'approche NI. Lorsqu'on déclare des valeurs pour la catégorie de données définie par les quatre dimensions, SNR, NIRE, Industrie et Catégories d'exposition (types d'enregistrements) 070, qui sont respectivement assorties de 1, 26, 50 et 11 valeurs de clé, il faut produire 14 300 enregistrements – un pour chaque combinaison valide des valeurs de clé (c.-à-d., 1 × 26 × 50 × 11 combinaisons). Chacun de ces enregistrements fournit une valeur pour les 11 mesures recueillies pour la catégorie de données concernée (p. ex., « Facilités autorisées », « Encours », « ECD estimative selon l'approche NI », « Pertes prévues selon l'approche NI », « Pertes économiques », etc.). Il faut aussi produire des enregistrements contenant les valeurs des huit mesures (c.-à-d., « Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés », « Garanties bancaires et garanties bancaires à première demande », « Lettres de crédit documentaires et commerciales », etc.) pour chacune des 286 combinaisons valides de valeurs de clé de la catégorie de données assortie des trois dimensions, SNR, NIRE et Catégories d'exposition (c.-à-d., 1 × 26 × 11 combinaisons de valeurs de clé) dans Types d'enregistrements 100. De la même manière, il faut produire des enregistrements pour chacune des autres catégories de données définies pour la partie 1 du portefeuille de la clientèle de gros assujetti à l'approche NI

L'ensemble des enregistrements à produire pour ce relevé particulierest entièrement déterminé par les structures d'enregistrement, concept dont il est question à la section 2.3 ci-dessous.

#### 2.3. Définition des enregistrements par des structures d'enregistrement

Comme un fichier de données de relevé renferme généralement des milliers d'enregistrements, il n'est pas possible d'énumérer chacun d'entre eux dans les présentes spécifications techniques. On définit plutôt une « structure d'enregistrement » descriptive pour chaque catégorie de données. Une structure d'enregistrement contient tous les renseignements nécessaires à propos des dimensions, des valeurs de clé et des mesures permettant de préciser l'ensemble complet des enregistrements d'une catégorie de données.

À la section 3, Description des structures d'enregistrement, on explique en détails comment lire et interpréter une structure d'enregistrement. Pour connaître la liste complète de toutes les structures d'enregistrement du relevé, reportez-vous à la section 4.5, Structures d'enregistrement.

### 3. Description des structures d'enregistrement

#### 3.1. Format d'un enregistrement

Chaque ligne du fichier de données, d'une longueur fixe de 380 caractères, représente un enregistrement physique du relevé. La première partie de cet enregistrement, qu'on appelle « descripteur d'enregistrement », précise les dimensions et les combinaisons de valeurs de clé de la catégorie de données visée par l'enregistrement. La deuxième partie de l'enregistrement, qu'on appelle « segment de mesures », renferme les valeurs de chaque mesure associée à la catégorie de données.

Par exemple, le descripteur et le segment de mesures d'un enregistrement appartenant à la partie 1 du relevé de portefeuille de la clientèle de gros assujetti à l'approche NI se présentent comme suit :

Exemple – Format d'un enregistrement

| Début | Fin | Longueur | Enregistrement |
| --- | --- | --- | --- |
| 1 | 23 | 23 | **Descripteur d'enregistrement** |
| 24 | 370 | 347 | **Segment de mesures** |
| 371 | 378 | 8 | **Compteur de lignes séquentiel** |
| 379 | 380 | 2 | **RC + SL** |

On remarque qu'un compteur de ligne séquentiel à huit caractères suit le segment de mesures. Ce compteur, qui n'utilise que des nombres entiers, augmente de 1 à chaque enregistrement, du premier au dernier enregistrement du fichier. Il peut servir à rétablir l'ordre des enregistrements dans le fichier durant le traitement en aval.

Enfin, chaque enregistrement se termine par un caractère de retour de chariot, et par un caractère de saut de ligne.

#### 3.2. Format d'un descripteur d'enregistrement

Pour faciliter le processus de validation des données, le descripteur d'enregistrement commence par un champ « Type d'enregistrement » à trois caractères, qui indique la catégorie de données visée par l'enregistrement. Pour connaître la liste des types d'enregistrement, reportez-vous à la section 4.3, Types d'enregistrement.

En outre, chaque descripteur d'enregistrement contient un champ « valeur de clé » à quatre caractères pour chaque dimension, y compris celles qui ne s'appliquent pas à la catégorie de données visée par l'enregistrement. Les valeurs de clé des dimensions sont représentées par des nombres entiers à quatre chiffres. La liste des dimensions possibles pour le relevé, ainsi que les valeurs de clé de chaque dimension, se trouvent à la section 4.4, Types de dimension.

Par exemple, les champs constituant un descripteur d'enregistrement de la partie 1 du relevé de portefeuille de clientèle de gros assujetti à l'approche NI (où les dimensions possibles sont NIRE, Industrie, Région géographique, Système de notation du risque et Catégories d'exposition) se présentent comme suit :

Exemple – Format d'un descripteur d'enregistrement

| Début | Fin | Longueur | Champ de données |
| --- | --- | --- | --- |
| 1 | 3 | 3 | **Type d'enregistrement** |
| 4 | 7 | 4 | **Clé NIRE** |
| 8 | 11 | 4 | **Clé Industrie** |
| 12 | 15 | 4 | **Clé Région géographique** |
| 16 | 19 | 4 | **Clé Système de notation du risque** |
| 20 | 23 | 4 | **Clé Catégories d'exposition** |

Les formats détaillés des descripteurs d'enregistrement utilisés dans le relevé visé par le présent document sont donnés à la section 4.5, Structures d'enregistrement.

#### 3.3. Définition des dimensions et des valeurs de clé valides

Chaque structure d'enregistrement définit les dimensions qui déterminent le nombre d'enregistrements nécessaires pour une catégorie particulière de données, ainsi que les dimensions qui ne s'appliquent pas à la catégorie.

Dans chaque structure d'enregistrement, des valeurs de clé spéciales sont inscrites pour les dimensions ne s'appliquant pas à la catégorie de données. Un ensemble de valeurs de clé valides est précisé pour toutes les autres dimensions. En intégrant des valeurs de clé pour toutes les dimensions dans chaque enregistrement, on s'assure que tous les descripteurs des enregistrements du fichier de données du relevé sont de la même longueur. Cette façon de faire facilite le traitement en aval des relevés.

Il faut donc fournir un enregistrement de 380 caractères pour chaque combinaison de valeurs de clé valides précisée dans la structure d'enregistrement.

#### 3.4. Format d'un segment de mesures

Le segment de mesures correspond à la deuxième partie de l'enregistrement et contient les champs de données pour chacune des mesures déclarées à l'égard des combinaisons de valeurs de clé définies par le descripteur d'enregistrement. Ce segment comprFin également un champ de « remplissage », qui introduit des caractères d'espacement pour combler les vides jusqu'au 370e caractère de l'enregistrement.

Par exemple, les champs de données à 15 caractères qui constituent le segment de mesures d'une catégorie de données appartenant à la partie 1 du relevé de portefeuille de clientèle de gros assujetti à l'approche NI assortie des mesures « Total des provisions pour pertes sur créances », « Provisions individuelles pour pertes sur créances », « Acceptations et prêts de crédit douteux » et « Ajouts aux acceptations et prêts de crédit douteux » se présentent comme suit :

Exemple – Format d'un segment de mesures

| Début | Fin | Longueur | Champ de données |
| --- | --- | --- | --- |
| 24 | 38 | 15 | **Total des provisions pour pertes sur créances** |
| 39 | 53 | 15 | **Provisions individuelles pour pertes sur créances** |
| 54 | 68 | 15 | **Acceptations et prêts de crédit douteux** |
| 69 | 83 | 15 | **Ajouts aux acceptations et prêts de crédit douteux** |
| 84 | 370 | 287 | **Caractères de remplissage** |

La structure d'enregistrement d'une catégorie de données particulière précise les mesures déclarées dans chaque enregistrement relevant de la catégorie, ainsi que la longueur des champs.

#### 3.5. Enregistrements de début et de fin

Les enregistrements de début et de fin servent à marquer le début et la fin du fichier des données du relevé, ainsi qu'à fournir des métadonnées sur le relevé lui-même. Ces enregistrements se présentent également sous la forme de lignes de 380 caractères, et respectent le format général d'un enregistrement ordinaire. Toutefois, les clés des dimensions des descripteurs des enregistrements de début et de fin sont établies à des valeurs spéciales, qui indiquent qu'aucune dimension n'est utilisée dans l'enregistrement. Les segments de mesures des enregistrements de début et de fin contiennent les métadonnées concernant le relevé.

Dans la suite du présent document, on utilise le terme « enregistrement » pour désigner globalement les enregistrements de mesures et les enregistrements de début et de fin.

La première ligne du fichier d'extraction des données doit être un enregistrement de début de type « 000 », alors que la dernière ligne doit correspondre à un enregistrement de fin de type « 999 ». Il doit s'agir des seuls enregistrements « 000 » et « 999 » du fichier.

À l'exception des enregistrements de début et de fin, tous les autres enregistrements peuvent être présentés dans n'importe quel ordre. L'intégrité référentielle est établie par la vérification de la présence d'enregistrements parents à l'aide de clés primaires (NIRE, importance de l'exposition, région géographique, ratio prêt/valeur, catégorie d'exposition, titrisation, taux, catégorie de retard).

Pour chaque clé primaire, il existe une valeur « Inconnu ». Comme aucun prêt ne devrait être assorti de ces chaînes, les valeurs « Inconnu » ne sont pas utilisées pour la concordance des valeurs dans les règles relatives aux opérations, puisque la banque ne devrait pas déclarer de données dans ces chaînes.

### 4. Exigences relatives au fichier d'extraction de données

Les sections qui suivent décrivent la présentation de la partie 1 du fichier d'extraction des données du portefeuille de la clientèle de gros assujetti à l'approche NI qui doit être soumis par l'entremise du SDR. Tout au long du texte sur la présentation du fichier d'extraction, les champs de clé primaire sont écrits en caractère gras, dans l'ordre dans lequel ils apparaissent dans la clé.

#### 4.1. Type de fichier et convention de désignation des fichiers

Les données destinées à être versées dans NCR doivent être enregistrées dans un fichier texte de largeur fixe, soit 380 octets par ligne, incluant un caractère de retour de chariot (RC) et un caractère de saut de ligne (SL) pour séparer les enregistrements. Les champs vides (c.-à-d. qui ne contiennent aucune valeur) sont remplacés par des caractères d'espacement s'il s'agit normalement de données alphanumériques, ou par des zéros s'il s'agit de données numériques. Les champs obligatoires doivent être remplis conformément aux directives énoncées dans le document [1].

Le fichier texte de largeur fixe doit être nommé, selon les conventions établies, au format IF\_BB\_MMAAAA.DAT, où IF correspond au numéro d'identification de l'institution financière (attribué par le BSIF), BB est une chaîne fixe, MM représente le mois de déclaration des données et AAAA, l'année.

#### 4.2. Structure du fichier

Comme il en a été question plus haut, la première ligne du fichier d'extraction doit correspondre à un enregistrement de début (« 000 ») et la dernière ligne, à un enregistrement de fin (« 999 »); il doit s'agir des seuls enregistrements « 000 » et « 999 » du fichier. À l'exception des enregistrements de début et de fin, tous les autres enregistrements peuvent être présentés dans n'importe quel ordre.

Dans les définitions de chaque structure d'enregistrement, la combinaison de toutes les valeurs de clé (type d'enregistrement, NIRE, industrie, région géographique, système de notation du risque et catégorie d'exposition) ne doit être précisée qu'une seule fois dans le fichier de données du relevé, à l'aide d'un enregistrement (si les données le permettent).

#### 4.3. Types d'enregistrement

Chaque ligne du fichier de données du relevé correspond à l'un des types d'enregistrement suivants : enregistrement de début, enregistrement de mesures (dont il existe plusieurs types) ou enregistrement de fin. Le logiciel de traitement des relevés en aval doit être en mesure de déterminer le type de chacun des enregistrements pour pouvoir les décomposer en leurs champs constituants. Pour faciliter cette opération, tous les enregistrements de mesures doivent commencer par un champ « Type d'enregistrement » à trois caractères qui détermine la structure de l'enregistrement (et, par conséquent, l'ensemble des champs qui le composent). Les types d'enregistrement définis pour le relevé visé par le présent document – un pour chaque catégorie de données – sont les suivants :

Types d'enregistrements pour le relevé des données du portefeuille de la clientèle de gros - Partie 1

| Type d'enregistrement | Description |
| --- | --- |
| 000 | Enregistrement de début (en-tête) |
| 005 | Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros |
| 010 | Déclaration des NIRE |
| 015 | TABLEAU DES TOTAUX, TOUTES LES CATÉGORIES ET SOUS-CATÉGORIES D'EXPOSITION |
| 020 | TABLEAU DES TOTAUX, TROIS CATÉGORIES D'EXPOSITION SEULEMENT |
| 030 | SYSTÈME DE NOTATION DU RISQUE |
| 050 | NIRE ET RÉGION GÉOGRAPHIQUE, CATÉGORIES ET SOUS-CATÉGORIES D'EXPOSITION |
| 070 | NIRE ET INDUSTRIE, CATÉGORIES ET SOUS-CATÉGORIES D'EXPOSITION |
| 080 | RÉGION GÉOGRAPHIQUE |
| 090 | INDUSTRIE |
| 100 | NIRE ET CATÉGORIES ET SOUS-CATÉGORIES D'EXPOSITION |
| 999 | Enregistrement de fin |

#### 4.4. Types de dimension

Afin de restreindre le nombre de dimensions, de réduire les risques d'erreur et de faciliter la validation des données, le relevé fait appel à des valeurs de clé, plutôt qu'aux noms des dimensions.

Voici la liste des dimensions utilisées dans le relevé, ainsi que les valeurs de clé correspondantes :

Dimensions utilisées dans le relevé des données du portefeuille de la clientèle de gros - Partie 1 et les valeurs de clé correspondantes

| Valeurs de clé | Nom de la dimension |
| --- | --- |
| 0100 – 0199 | NIRE |
| 0200 – 0299 | Système de notation du risque |
| 0300 – 0399 | Région géographique |
| 1200 – 1299 | ndustrie |
| 1800 – 1899 | Catégorie d'exposition |

On présente ci-dessous la liste des valeurs de clé des dimensions autorisées dans le relevé.

##### Clé primaire NIRE

Valeurs de clé primaire NIRE

| Valeur de clé | Description |
| --- | --- |
| 0100 | Total – NIRE |
| 0101 | 1ère NIRE |
| 0102 | 2e NIRE |
| 0103 | 3e NIRE |
| 0104 | 4e NIRE |
| 0105 | 5e NIRE |
| 0106 | 6e NIRE |
| 0107 | 7e NIRE |
| 0108 | 8e NIRE |
| 0109 | 9e NIRE |
| 0110 | 10e NIRE |
| 0111 | 11e NIRE |
| 0112 | 12e NIRE |
| 0113 | 13e NIRE |
| 0114 | 14e NIRE |
| 0115 | 15e NIRE |
| 0116 | 16e NIRE |
| 0117 | 17e NIRE |
| 0118 | 18e NIRE |
| 0119 | 19e NIRE |
| 0120 | 20e NIRE |
| 0121 | 21e NIRE |
| 0122 | 22e NIRE |
| 0123 | 23e NIRE |
| 0124 | 24e NIRE |
| 0125 | 25e NIRE |
| 0199 | Aucune NIRE |

##### Clé primaire Industrie

Valeurs de clé primaire Industrie

| Valeur de clé | Description |
| --- | --- |
| 1200 | Total – Industries |
| 1201 | Agriculture |
| 1202 | Construction |
| 1203 | Défense |
| 1204 | Équipement industriel et lourd |
| 1205 | Câblodistribution |
| 1206 | Médias |
| 1207 | Télécommunications |
| 1208 | Produits pétroliers et gaziers |
| 1209 | Services publics |
| 1210 | Banques et sociétés de fiducie |
| 1211 | Fonds |
| 1212 | Assurances |
| 1213 | Régimes de retraite |
| 1214 | Valeurs mobilières, services de courtage et autres |
| 1215 | Titrisation |
| 1216 | Banques multilatérales de développement |
| 1217 | Administrations provinciales, municipales et régionales |
| 1218 | Emprunteurs souverains et banques centrales |
| 1219 | Fournisseurs de soins de santé |
| 1220 | Équipement médical |
| 1221 | Médicaments et recherche pharmaceutique |
| 1222 | Fabrication de produits industriels |
| 1223 | Fabrication de produits de consommation |
| 1224 | Fabrication d'aliments, de boissons et de produits du tabac |
| 1225 | Fabrication de produits textiles et de vêtements |
| 1226 | Métaux précieux et diamants |
| 1227 | Acier et fer |
| 1228 | Autres produits miniers |
| 1229 | Immobilier commercial |
| 1230 | Immobilier résidentiel |
| 1231 | Produits chimiques |
| 1232 | Produits forestiers |
| 1233 | Caoutchouc et plastiques |
| 1234 | Vente au détail et en gros |
| 1235 | Éducation et formation |
| 1236 | Services alimentaires |
| 1237 | Jeux et divertissements |
| 1238 | Hébergement |
| 1239 | Services professionnels et autres |
| 1240 | Matériel informatique |
| 1241 | Électronique |
| 1242 | Logiciels |
| 1243 | Automobile |
| 1244 | Aviation et aérospatiale |
| 1245 | Transport ferroviaire |
| 1246 | Expédition – Transport par eau |
| 1247 | Transport par camion et services de messagerie |
| 1248 | Métaux de première fusion et aluminium |
| 1299 | Aucune industrie |

##### Clé primaire Région géographique

Valeurs de clé primaire Région géographique

| Valeur de clé | Description |
| --- | --- |
| 0300 | Total – Région géographique |
| 0301 | Total – Canada |
| 0302 | Alberta |
| 0303 | Colombie-Britannique |
| 0304 | Manitoba |
| 0305 | Nouveau-Brunswick |
| 0306 | Terre-Neuve-et-Labrador |
| 0307 | Territoires du Nord-Ouest |
| 0308 | Nouvelle-Écosse |
| 0309 | Nunavut |
| 0310 | Ontario |
| 0311 | Île-du-Prince-Edouard |
| 0312 | Québec |
| 0313 | Saskatchewan |
| 0314 | Yukon |
| 0315 | États-Unis |
| 0316 | Mexique |
| 0317 | Autre – Amérique latine et Caraïbes |
| 0318 | Europe |
| 0319 | Autre pays |
| 0399 | Aucune région géographique |

##### Clé primaire Système de notation du risque

Valeurs de clé primaire Système de notation du risque

| Valeur de clé | Description |
| --- | --- |
| 0200 | Total – Systèmes de notation du risque |
| 0201 | 1er système de notation du risque |
| 0202 | 2nd Système de notation du risque |
| 0203 | 3rd Système de notation du risque |
| 0204 | 4e système de notation du risque |
| 0205 | 5e système de notation du risque |
| 0206 | 6e système de notation du risque |
| 0207 | 7e système de notation du risque |
| 0208 | 8e système de notation du risque |
| 0209 | 9e système de notation du risque |
| 0210 | 10e système de notation du risque |
| 0211 | 11e système de notation du risque |
| 0212 | 12e système de notation du risque |
| 0213 | 13e système de notation du risque |
| 0214 | 14e système de notation du risque |
| 0215 | 15e système de notation du risque |
| 0216 | 16e système de notation du risque |
| 0217 | 17e système de notation du risque |
| 0218 | 18e système de notation du risque |
| 0219 | 19e système de notation du risque |
| 0220 | 20e système de notation du risque |
| 0299 | Aucun système de notation du risque |

##### Clé primaire Catégorie d'exposition

Valeurs de clé primaire Catégorie d'exposition

| Valeur de clé | Description |
| --- | --- |
| 1800 | Total – Clientèle de gros |
| 1801 | Total – Entreprises |
| 1804 | Financement de projets |
| 1805 | Financement d'objets |
| 1806 | Financement de produits de base |
| 1807 | Immobilier de rapport |
| 1825 | Immeubles résidentiels à logements multiples productifs de revenus |
| 1826 | Autres biens productifs de revenus |
| 1808 | Immobilier commercial à forte volatilité |
| 1823 | Total – Terrains pour subdivision |
| 1824 | Financement intermédiaire |
| 1809 | PME assimilées à des entreprises |
| 1810 | Autres entreprises |
| 1802 | Banques |
| 1803 | Emprunteurs souverains |
| 1899 | Aucune catégorie d'exposition |

#### 4.5. Structures d'enregistrement

La section qui suit donne une description des structures d'enregistrement autorisées dans le relevé visé par le présent document. Dans les tableaux ci-dessous, qui décrivent la structure des enregistrements, la première colonne correspond au numéro d'identification du champ, qui renvoie au document [1]. Les deuxième et troisième colonnes se rapportent aux positions de début et de fin du champ dans l'enregistrement. Les colonnes suivantes indiquent la longueur et le nom du champ, ainsi que son caractère obligatoire (« O »). La dernière colonne donne des renseignements complémentaires pour faciliter la planification de l'extraction des données et précise le format (masque) de champ à utiliser. Les noms de champ apparaissant en caractères gras correspondent aux clés du descripteur de l'enregistrement.

Les champs de l'enregistrement doivent apparaître dans l'ordre où ils sont présentés dans les structures d'enregistrement. En outre, les valeurs des champs doivent être au format précisé dans les tableaux définissant les structures d'enregistrement.

Les trois premiers caractères de chaque ligne du fichier de données du relevé correspondent au type d'enregistrement. Une valeur de clé Type d'enregistrement exclusive a été attribuée à chaque structure d'enregistrement; ces valeurs sont énumérées à la section 4.3.

La valeur de clé au format x99 sert à préciser que l'enregistrement ne renferme aucune valeur de clé pour la dimension concernée. La liste des valeurs de clé de toutes les dimensions se trouve à la section 4.4.

##### Enregistrement de début (000)

L'enregistrement de début constitue un mécanisme de contrôle de la qualité qui permet d'identifier sans ambiguïté chacun des fichiers transmis au BSIF (expéditeur, date de déclaration, nom du fichier, etc.). Les renseignements contenus dans cet en-tête sont comparés au nom du fichier et aux données contenues dans ce dernier afin de s'assurer que le fichier reçu par le BSIF n'a pas été altéré.

Le format de la structure de l'enregistrement de début est décrit en détails ci-dessous :

Format de la structure de l'enregistrement de début (000)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "000" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixe "1899" |
| 10 | 24 | 27 | 4 | Code d'identification de l'institution | ✓obligatoire | pic(X) – Remplissage à droite par des espaces |
| 28 | 28 | 35 | 8 | Date de déclaration des données | ✓obligatoire | pic(9) – Format : AAAAMMJJ |
| - | 36 | 42 | 7 | Nom du relevé | Check markCheck mark✔ | pic(X) – Chaîne fixe, BB, remplissage à droite par des espaces |
| - | 43 | 48 | 6 | Version du format du fichier de relevé | ✓obligatoire | pic(X) – Chaîne fixe « 06.0.0 » |
| - | 49 | 370 | 322 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros (005)

Les systèmes de notation du risque peuvent différer d'une institution financière à l'autre. Vous devez par conséquent déclarer tous les systèmes de notation du risque du portefeuille de la clientèle de grosmis en oeuvre durant la période de déclaration dans tous vos relevés NCR du portefeuille de la clientèle de gros, y compris ceux qui se rattachent aux opérations de la clientèle de gros : BF, BG. Les systèmes de notation du risque du portefeuille de la clientèle de grosdoivent être identiques dans tous les relevés NCR du portefeuille de la clientèle de grosdans lesquels on attribue une notation aux risques (BB et BC). Cela ne signifie pas qu'il faille déclarer des notations de risque (NIRE, NRF) ou des segments pour chaque système de notation du risque du portefeuille de la clientèle de gros.

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. En commençant par la clé de système de notation du risque du portefeuille de la clientèle de gros appelée « 1er système de notation du risque » et en continuant avec chacune des clés suivantes, créez un nouvel enregistrement pour chaque système de notation du risque du portefeuille de la clientèle de gros utilisé durant la période de déclaration, en précisant le nom de chacun :

Remarque :

1. À compter du troisième trimestre de 2012, les institutions financières doivent déclarer les systèmes de notation du risque du portefeuille de la clientèle de gros dans les relevés portant sur le portefeuille de la clientèle de gros (BB et BC), et les systèmes de notation du risque du portefeuille de la clientèle de détail dans le relevé du portefeuille de la clientèle de détail (BE).
2. Un nombre maximal de 20 systèmes de notation du risque du portefeuille de la clientèle de gros peuvent être déclarés dans les relevés du portefeuille de la clientèle de gros, au moyen des valeurs de clé allant de « 0201 » à « 0220 ».
3. Un nombre maximal de 40 systèmes de notation du risque du portefeuille de la clientèle de détail peuvent être déclarés dans le relevé du portefeuille de la clientèle de détail, au moyen des valeurs de clé allant de « 0201 » à « 0240 ».
4. Il n'est pas nécessaire d'utiliser les valeurs de clé des systèmes de notation du risque dans l'ordre numérique. Par exemple, il est possible de déclarer trois systèmes de notation du risque du portefeuille de la clientèle de gros au moyen des valeurs de clé « 0203 », « 0205 » et « 0210 ».

Format de la structure d'enregistrement correspondant à catégorie Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros (005)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "005" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0201 », « 0202 » à « 0220 », au besoin |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixe "1899" |
| 32 | 24 | 83 | 60 | Nom du système de notation du risque | ✓obligatoire | pic(X) – Remplissage à droite par des espaces |
| - | 84 | 370 | 287 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### Déclaration des NIRE (010)

Les NIRE peuvent différer d'une institution financière à l'autre. Vous devez par conséquent déclarer toutes les NIRE mises en oeuvre durant la période de déclaration dans tous vos relevés NCR, y compris celles qui se rattachent aux opérations de la clientèle de gros : BF, BG. Les NIRE doivent être identiques dans tous les relevés NCR du portefeuille de la clientèle de grosdans lesquels on déclare des NIRE (BB et BC). Cela ne signifie pas que tous les systèmes de notation du risque du portefeuille de la clientèle de grosdoivent être assortis d'une NIRE, bien que tous les systèmes de notation du risque assortie d'une NRF (relevé BC) doivent s'accompagner d'une NIRE.

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. En commençant par la clé de NIRE appelée « 1ère NIRE » et en continuant avec chacune des clés suivantes, créez un nouvel enregistrement pour chaque NIRE du système de notation du risque du portefeuille de la clientèle de gros utilisée durant la période de déclaration, en précisant le nom de chacune. Les noms des NIRE appartenant à un SNR doivent être énumérés selon les clés NIRE, en ordre croissant de risque (c.-à-d. que la NIRE correspondant au risque le plus faible doit apparaître en premier dans la liste en fonction de votre probabilité de défaut estimative – champ 2 du relevé BC). Un même nom de NIRE peut être utilisé dans plus d'un système de notation du risque du portefeuille de la clientèle de gros, mais ne peut servir qu'une seule fois au sein d'un même SNR.

Format de la structure d'enregistrement correspondant à catégorie Déclaration des NIRE (010)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "010" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaînes fixes « 0101 », « 0102 » à « 0125 », au besoin |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0201 », « 0202 » à « 0220 » au besoin |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixe "1899" |
| 33 | 24 | 83 | 60 | Nom de la NIRE | ✓obligatoire | pic(X) – Remplissage à droite par des espaces |
| - | 84 | 370 | 287 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### Tableau des totaux, toutes les catégories et sous-catégories d'exposition (015)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque catégorie et sous-catégorie d'exposition :

Format de la structure d'enregistrement correspondant à catégorie Tableau des totaux, toutes les catégories et sous-catégories d'exposition (015)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "015" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaînes fixes « 1800 » à « 1810 » et « 1823 » à « 1826 » |
| 1 | 24 | 38 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 39 | 53 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 11 | 54 | 68 | 15 | Exposition estimative en cas de défaut selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 12 | 69 | 83 | 15 | Pertes prévues selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 14 | 84 | 98 | 15 | Pertes économiques | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 15 | 99 | 113 | 15 | Radiations | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 19 | 114 | 128 | 15 | Recouvrements | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 13 | 129 | 143 | 15 | Fonds propres selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 3 | 144 | 158 | 15 | Liste de surveillance – Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 4 | 159 | 173 | 15 | Liste de surveillance – Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 5 | 174 | 182 | 9 | Nombre d'emprunteurs | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 183 | 370 | 188 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### Tableau des totaux, trois catégories d'exposition seulement (020)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque catégorie d'exposition :

Format de la structure d'enregistrement correspondant à catégorie Tableau des totaux, trois catégories d'exposition seulement (020)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "020" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaînes fixes « 1800 » à « 1803 » |
| 17 | 24 | 38 | 15 | Total des réserves pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 18 | 39 | 53 | 15 | Provisions individuelles pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 20 | 54 | 68 | 15 | Acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 23 | 69 | 83 | 15 | Ajouts aux acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 29 | 84 | 98 | 15 | Provisions individuelles pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 30 | 99 | 113 | 15 | Autres changements aux dotations aux pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 21 | 114 | 128 | 15 | Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 31 | 129 | 143 | 15 | Autres changements aux acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 144 | 370 | 227 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Hexadecimal: 0D + 0A |

##### Système de notation du risque (030)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque système de notation du risque du portefeuille de la clientèle de gros déclaré.

Les systèmes de notation du risque du portefeuille de la clientèle de gros mis en oeuvre durant la période de déclaration visée par le relevé doivent être précisés au moyen de la structure d'enregistrement « Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros » ci-dessus. Par conséquent, seules les valeurs de clé des systèmes de notation du risque utilisées doivent être déclarées :

Format de la structure d'enregistrement correspondant à catégorie Système de notation du risque (030)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "030" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199" |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0200 », « 0201 », « 0202 » à « 0220 », au besoin |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixe "1899" |
| 1 | 24 | 38 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 39 | 53 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 11 | 54 | 68 | 15 | Exposition estimative en cas de défaut selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 12 | 69 | 83 | 15 | Pertes prévues selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 14 | 84 | 98 | 15 | Pertes économiques | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 15 | 99 | 113 | 15 | Radiations | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 19 | 114 | 128 | 15 | Recouvrements | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 13 | 129 | 143 | 15 | Fonds propres selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 3 | 144 | 158 | 227 | Liste de surveillance – Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 4 | 159 | 173 | 8 | Liste de surveillance – Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 5 | 174 | 182 | 9 | Nombre d'emprunteurs | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 183 | 370 | 188 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Hexadecimal: 0D + 0A |

##### NIRE et Région géographique, Catégories et sous-catégories d'exposition (050)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque combinaison de la plage des valeurs précisée pour les clés NIRE, Région géographique, Systèmes de notation du risque et Catégories d'exposition.

Les NIRE utilisées durant la période de déclaration visée par le relevé doivent être précisées au moyen de la structure d'enregistrement « Déclaration des NIRE » ci-dessus. Par conséquent, seules les valeurs de la clé NIRE utilisées doivent être déclarées. (P.ex., il n'est pas nécessaire de créer des enregistrements pour les SNR déclarés à l'égard desquels aucune NIRE ne figure dans la structure d'enregistrement « Déclaration des NIRE ».)

Format de la structure d'enregistrement correspondant à cette catégorie NIRE et Région géographique, Catégories et sous-catégories d'exposition (050)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "050" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaînes fixes « 0100 », « 0101 », « 0102 » à « 0125 », au besoin[Tableau de la catégorie 050, note \*](#t050n*) |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaînes fixes « 0300 » à « 0319 » |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0201 », « 0202 » à « 0220 », au besoin[Tableau de la catégorie 050, note \*](#t050n*) |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaînes fixes « 1800 » à « 1810 » |
| 1 | 24 | 38 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 39 | 53 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 11 | 54 | 68 | 15 | Exposition estimative en cas de défaut selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 12 | 69 | 83 | 15 | Pertes prévues selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 14 | 84 | 98 | 15 | Pertes économiques | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 15 | 99 | 113 | 15 | Radiations | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 19 | 114 | 128 | 15 | Recouvrements | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 13 | 129 | 143 | 15 | Fonds propres selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 3 | 144 | 158 | 227 | Liste de surveillance – Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 4 | 159 | 173 | 8 | Liste de surveillance – Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 5 | 174 | 182 | 9 | Nombre d'emprunteurs | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 183 | 370 | 188 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Hexadecimal: 0D + 0A |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Notes de tableau de la catégorie 050 Note \* de tableau de la catégorie 050  Toute combinaison de NIRE et de SNR doit être déclarée dans le champ Déclaration des NIRE (010).  [Retour à la première référence de note \* de tableau de la catégorie 050](#t050n*-1-rf) | | | | | | |

##### NIRE et Industrie, Catégories et sous-catégories d'exposition (070)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque combinaison de la plage des valeurs précisée pour les clés NIRE, Industrie, Système de notation du risque et Catégories d'exposition.

Les NIRE utilisées durant la période de déclaration visée par le relevé doivent être précisées au moyen de la structure d'enregistrement « Déclaration des NIRE » ci-dessus. Par conséquent, seules les valeurs de la clé NIRE utilisées doivent être déclarées. (P.ex., il n'est pas nécessaire de créer des enregistrements pour les SNR déclarés à l'égard desquels aucune NIRE ne figure dans la structure d'enregistrement « Déclaration des NIRE ».)

Format de la structure d'enregistrement correspondant à catégorie IRE et Industrie, Catégories et sous-catégories d'exposition (070)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "070" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaînes fixes « 0100 », « 0101 », « 0102 » à « 0125 », au besoin[Tableau de la catégorie 070, note \*](#t070n*) |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaînes fixes « 1200 » à « 1248 » |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0201 », « 0202 » à « 0220 », au besoin[Tableau de la catégorie 070, note \*](#t070n*) |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaînes fixes « 1800 » à « 1810 » |
| 1 | 24 | 38 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 39 | 53 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 11 | 54 | 68 | 15 | Exposition estimative en cas de défaut selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 12 | 69 | 83 | 15 | Pertes prévues selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 14 | 84 | 98 | 15 | Pertes économiques | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 15 | 99 | 113 | 15 | Radiations | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 19 | 114 | 128 | 15 | Recouvrements | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 13 | 129 | 143 | 15 | Fonds propres selon l'approche NI | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 3 | 144 | 158 | 227 | Liste de surveillance – Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 4 | 159 | 173 | 8 | Liste de surveillance – Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 5 | 174 | 182 | 9 | Nombre d'emprunteurs | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 183 | 370 | 188 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Hexadecimal: 0D + 0A |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Notes de tableau de la catégorie 070 Note \* de tableau de la catégorie 070  Toute combinaison de NIRE et de SNR doit être déclarée dans le champ Déclaration des NIRE (010).  [Retour à la première référence de note \* de tableau de la catégorie 070](#t070n*-1-rf) | | | | | | |

##### Région géographique (080)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour la plage de valeurs précisée pour la clé Région géographique.

Format de la structure d'enregistrement correspondant à catégorie Région géographique (080)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "080" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaînes fixes « 0300 » à « 0319 » |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixes "1899" |
| 17 | 24 | 38 | 15 | Total des provisions pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 18 | 39 | 53 | 15 | Provisions individuelles pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 20 | 54 | 68 | 15 | Acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 23 | 69 | 83 | 15 | Ajouts aux acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 1 | 84 | 98 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 99 | 113 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 114 | 370 | 257 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### Industrie (090)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour la plage de valeurs précisée pour la clé Industrie.

Format de la structure d'enregistrement correspondant à catégorie Industrie (090)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | o | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "090" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaînes fixes « 1200 » à « 1248 » |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixes "1899" |
| 17 | 24 | 38 | 15 | Total des provisions pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 18 | 39 | 53 | 15 | Provisions individuelles pour pertes sur créances | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 20 | 54 | 68 | 15 | Acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 23 | 69 | 83 | 15 | Ajouts aux acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 1 | 84 | 98 | 15 | Facilités autorisées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 2 | 99 | 113 | 15 | Encours | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 114 | 370 | 257 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

##### NIRE et Catégories et sous-catégories d'exposition (100)

Le format de la structure d'enregistrement correspondant à cette catégorie de données est décrit en détails ci-dessous. Un nouvel enregistrement doit être créé pour chaque combinaison de la plage des valeurs précisée pour les clés NIRE, Système de notation du risque et Catégories d'exposition.

Les NIRE utilisées durant la période de déclaration visée par le relevé doivent être précisées au moyen de la structure d'enregistrement « Déclaration des NIRE » ci-dessus. Par conséquent, seules les valeurs de la clé NIRE utilisées doivent être déclarées. (P.ex., il n'est pas nécessaire de créer des enregistrements pour les SNR déclarés à l'égard desquels aucune NIRE ne figure dans la structure d'enregistrement « Déclaration des NIRE ».)

Format de la structure d'enregistrement correspondant à catégorie NIRE et Catégories et sous-catégories d'exposition (100)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "100" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaînes fixes « 0101 », « 0102 » à « 0125 », au besoin[Tableau de la catégorie 100, note \*](#t100n*) |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaînes fixes « 0201 », « 0202 » à « 0220 » au besoin[Tableau de la catégorie 100, note \*](#t100n*) |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaînes fixes « 1800 » à « 1810 » |
| 21 | 24 | 38 | 15 | Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 6 | 39 | 53 | 15 | Garanties bancaires et garanties bancaires à première demande | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 7 | 54 | 68 | 15 | Lettres de crédit documentaires et commerciales | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 8 | 69 | 83 | 15 | Engagements hors bilan dont l'échéance est inférieure à un an | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 9 | 84 | 98 | 15 | Engagements hors bilan dont l'échéance est inférieure à un an | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 23 | 99 | 113 | 15 | Ajouts aux acceptations et prêts de crédit douteux | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 26 | 114 | 128 | 15 | Protections de crédit vendues | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| 27 | 129 | 143 | 15 | Protections de crédit achetées | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 144 | 370 | 227 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |
|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Notes de tableau de la catégorie 100 Note \* de tableau de la catégorie 100  Toute combinaison de NIRE et de SNR doit être déclarée dans le champ Déclaration des NIRE (010).  [Retour à la première référence de note \* de tableau de la catégorie 100](#t100n*-1-rf) | | | | | | |

##### Enregistrement de fin (999)

Le format de la structure de l'enregistrement de fin est décrit en détails ci-dessous :

Format de la structure de l'enregistrement de fin (999)

| No d'identification du champ | Début | Fin | Longueur | Nom du champ | O | Remarques |
| --- | --- | --- | --- | --- | --- | --- |
| - | 1 | 3 | 3 | **Type d'enregistrement** | ✓obligatoire | pic(9) – Chaîne fixe "999" |
| - | 4 | 7 | 4 | **NIRE** | ✓obligatoire | pic(9) – Chaîne fixe "0199 " |
| - | 8 | 11 | 4 | **Industrie** | ✓obligatoire | pic(9) – Chaîne fixe "1299" |
| - | 12 | 15 | 4 | **Région géographique** | ✓obligatoire | pic(9) – Chaîne fixe "0399" |
| - | 16 | 19 | 4 | **Système de notation du risque** | ✓obligatoire | pic(9) – Chaîne fixe "0299" |
| - | 20 | 23 | 4 | **Catégorie d'exposition** | ✓obligatoire | pic(9) – Chaîne fixe "1899" |
| - | 24 | 32 | 9 | Nombre d'enregistrements dans le corps du fichier | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 33 | 44 | 12 | Taille du fichier (octets) | ✓obligatoire | pic(9) – Sans virgule ni point; remplissage à gauche par des zéros |
| - | 45 | 104 | 60 | Nom du fichier | ✓obligatoire | pic(X) - Fixed string, Name of this return data file, Right-padded with spaces |
| - | 105 | 112 | 8 | Date de création du fichier | ✓obligatoire | pic(9) – Format : AAAAMMJJ |
| - | 113 | 370 | 258 | Caractères de remplissage | ✓obligatoire | pic(X) – Espaces |
| - | 371 | 378 | 8 | Compteur de lignes séquentiel | ✓obligatoire | pic(9) – Remplissage à gauche par des zéros |
| - | 379 | 380 | 2 | RC + SL | ✓obligatoire | pix(X) – Valeur hexadécimale : 0D + 0A |

#### Remarques importantes

Le champ correspondant au compteur de lignes séquentiel qui apparaît au début de chaque enregistrement doit avoir la valeur « 00000001 » dans l'enregistrement de début, et être augmenté de 1 à chaque ligne. Le compteur de l'enregistrement de fin devrait donc indiquer le nombre total d'enregistrements du fichier.

### 5. Règles de validation des données

#### 5.1. Traitement des erreurs

Dans le cadre du traitement des erreurs, on vise à détecter le plus grand nombre possible d'erreurs et d'avertissements. Le fichier sera rejeté en entier si des erreurs sont décelées; aucune donnée ne sera enregistrée dans la base de données. Les avertissements concernent des erreurs non pertinentes qui n'empêchent pas l'enregistrement du contenu du fichier dans la base de données.

#### 5.2. Vérifications préalables au traitement

Un traitement préalable est effectué pour s'assurer que les fichiers d'extraction des données reçus sont formatés comme il se doit, et que les enregistrements de début et de fin correspondent bien au contenu du fichier. Un programme vérifie que les fichiers d'extraction des données contiennent un enregistrement de début et sont dénués d'erreurs de formatage. Ce programme vérifie notamment que :

1. tous les enregistrements sont assortis d'un type valide;
2. tous les enregistrements du fichier ont 378 caractères, plus deux caractères ASCII (retour de chariot et saut de ligne);
3. tous les enregistrements ont le nombre de champs correspondant au type d'enregistrement;
4. tous les enregistrements sont assortis d'un compteur séquentiel, celui de l'enregistrement de début étant 00000001 et la valeur des enregistrements suivants augmentée de 1 à chaque nouvel enregistrement;
5. le type de relevé correspond exactement aux données de l'enregistrement de début;
6. le nom du fichier de données correspond exactement aux données de l'enregistrement de fin;
7. le nom du fichier porte l'extension \*.DAT;
8. le code de l'institution fourni dans le nom du fichier et dans les enregistrements de début et de fin est un code valide de la Banque du Canada (ce code est fourni par le BSIF);
9. la clé composite donnée par chaque descripteur d'enregistrement est unique pour tous les enregistrements du fichier de données.
10. chaque valeur de champ doit être formaté conformément aux spécifications techniques (p. ex., il est inacceptable d'insérer des espaces à gauche lorsque les spécifications exigent un « remplissage à gauche par des zéros », même lorsque la partie « significative » du champ demeure la même.

#### Règles concernant les valeurs des champs

Les règles concernant les valeurs des champs garantissent que les données contenues dans chaque champ sont conformes aux types de données décrits dans le document [1]. Les règles générales suivantes s'appliquent à tous les fichiers de données de relevé. D'autres règles particulières concernant les valeurs des champs peuvent être énoncées dans le document [1], qui porte sur les définitions des données.

##### 5.3.1. Règles concernant les montants

Tous les montants sont déclarés et validés selon les règles suivantes :

1. Tous les montants sont déclarés en milliers de dollars.
2. Tous les montants sont arrondis au millier de dollars près.
3. Les champs renfermant des montants ne peuvent contenir que des chiffres, exception faite du symbole moins (-) lorsqu'il faut indiquer le négatif. Aucun espace ou séparateur décimal ne doit être utilisé.
4. Les montants négatifs doivent être précédés d'un trait d'union avant le premier chiffre significatif, avec remplissage à gauche par des zéros.
5. Tous les montants doivent être déclarés dans un champ à 15 caractères, avec remplissage à gauche par des zéros.

Par exemple, le montant 2 183 624,68 $ devient 000000000002184 et - 34 892,45 $ devient 000000000000-35.

##### 5.3.2. Règles concernant les probabilités et les pourcentages

Tous les pourcentages sont déclarés et validés selon les règles suivantes :

1. Toutes les probabilités entre 0 et 1 doivent être déclarées en pourcentage (entre 0 % et 100 %).
2. Tous les pourcentages doivent être déclarés comme étant assorties de deux chiffres significatifs après le séparateur décimal.
3. Tous les pourcentages doivent être arrondis au centième de pourcent le plus près.
4. Les pourcentages ne peuvent contenir que des valeurs numériques, un séparateur décimal et si la valeur est négative, un trait d'union. Ne pas employer la virgule.
5. Les pourcentages négatifs doivent être précédés d'un trait d'union avant le premier chiffre significatif, avec remplissage à gauche par des zéros.
6. Tous les pourcentages doivent être déclarés dans un champ à 6 caractères, avec remplissage à gauche par des zéros.

Par exemple, la valeur 98,738543 % devient 098.74 et – 6,1234 % devient 0-6.12.

##### 5.3.3. Règles concernant les autres valeurs numériques

Toutes les autres valeurs numériques sont déclarées et validées selon les règles suivantes :

1. Le nombre de chiffres dépend de la définition des données énoncée dans le document [1].
2. Les valeurs numériques ne peuvent contenir que des chiffres et, lorsqu'elles sont négatives, un trait d'union.
3. Les valeurs numériques (autres que les montants et les pourcentages, dont il est question ci-dessus) sont des entiers arrondis à l'unité près, sans chiffre significatif après la décimale.
4. Les valeurs négatives doivent être précédées d'un trait d'union avant le premier chiffre significatif, avec remplissage à gauche par des zéros.
5. Tous les champs contenant des valeurs numériques sont assortis d'un remplissage à gauche par des zéros.

Par exemple, 000073654 et 000000-79, deux des valeurs numériques valides constituées de 9 caractères, représentent respectivement 73 654 et -79,22. Les valeurs suivantes ne sont pas valides :

* 0073654 <= Nombre de caractères erroné (il devrait y avoir 9 chiffres au lieu de 7)
* 00073,654 <= Virgule non permise
* 0073654.5 <= Seuls les nombres entiers sont permis, et les caractères qui ne sont pas des chiffres sont interdits
* 73654 <= Le champ n'est pas rempli à gauche par des zéros
* -00000079 <= Le trait d'union n'est pas au bon endroit

##### 5.3.4. Règles concernant les dates

Toutes les dates sont déclarées et validées selon les règles suivantes :

1. Tous les champs renfermant une date comptent huit caractères;
2. Une date ne peut contenir que des chiffres (les mois ne peuvent pas être écrits en lettres et on ne peut utiliser les caractères spéciaux et les espaces);
3. Les dates doivent être au format AAAAMMJJ, où AAAA représente l'année, MM le mois et JJ le jour.

Par exemple, la chaîne 20100608 correspond au 8 juin 2010.

#### 5.4. Règles d'agrégation

Dans certains cas, les valeurs en dollars, en pourcentage ou en chiffres déclarées comme valeur de clé d'une dimension particulière peuvent être reliées d'une manière hiérarchique aux mesures d'autres valeurs de clé de la même dimension. Les règles ci-dessous décrivent comment ces mesures sont reliées et validées dans le relevé.

##### 5.4.1. Agrégation par sommation

À l'heure actuelle, les mesures représentant des montants, des pourcentages ou des valeurs numériques déclarées à l'égard de valeurs de clé de haut niveau appartenant à une hiérarchie dimensionnelle représentent en réalité la somme des mesures correspondantes déclarées pour les valeurs de clé de bas niveau. L'addition de mesures de valeurs de clé de bas niveau pour produire une mesure de valeur de clé de haut niveau constitue une « agrégation » des mesures (c.-à-d. un « cumul ») d'un niveau d'une dimension à l'autre.

Les mesures en dollars, en pourcentage ou en chiffres déclarées à l'égard des valeurs de clé « cumulatives » de haut niveau doivent correspondre à la somme des mesures déclarées pour les valeurs de clé de bas niveau – lorsque la mesure en question résulte d'une addition. Il arrive parfois que des mesures ou une de leurs dimensions ne résultent pas d'une addition. Ainsi, la mesure « nombre d'emprunteurs » ne résultera pas nécessairement d'une addition de toutes les valeurs figurant dans la catégorie des expositions puisque le même emprunteur pourrait avoir des expositions dans plus d'une catégorie d'exposition.

Les valeurs agrégées de chaque mesure à chaque niveau doivent être calculées de façon intelligente – c'est-à-dire en respectant la progression agrégative naturelle de la mesure en question de manière à ce que le résultat reflète réellement la mesure de la valeur à son niveau le plus élevé, quelque soit l'ordre dans lequel les valeurs servant au calcul sont déclarées. Ainsi, les valeurs agrégées correspondant aux pourcentages, aux ratios et aux probabilités doivent être calculées à partir des totaux préagrégés placés en position de numérateur et de dénominateur. Dans ce cas, le BSIF ne peut valider l'agrégation de ces deux niveaux.

Il convient de noter qu'une tolérance de 5 % ou de 20 (correspondant à 20 000 $) est acceptée (pour tenir compte d'éventuels problèmes d'arrondissement), toutefois, un écart supérieur à la fois à 5 % et à 20 entraîne un message d'erreur et les données sont rejetées. Voici comment fonctionne cette règle du 5 % : la somme des éléments doit systématiquement se trouver entre 95 % et 105 % de la valeur totale.

###### Exemple d'agrégation par sommation

Prenons par exemple la dimension Système de notation du risque du portefeuille de la clientèle de gros. Dans cette dimension, la mesure de la valeur de clé 0200 (Total – Systèmes de notation du risque du portefeuille de la clientèle de gros) correspond à la somme de toutes les mesures des valeurs de clé 0201 à 0220 (du 1er au 20e système de notation du risque).

Pour poursuivre cet exemple, prenons un cas où la structure d'enregistrement exige que la mesure ABC résultant d'une addition soit déclarée dans les combinaisons de toutesles valeurs de clé des dimensions Système de notation du risque, NIRE et Industrie. Si on examine tous les enregistrements ayant la même valeur pour les clés NIRE et Industrie (par exemple, 0101 et 1220, respectivement),alors la valeur de la mesure ABC dans l'enregistrement ayant la valeur 0200 pour la clé Système de notation du risque sera égale à la somme des mesures ABC de tous les enregistrements dont les valeurs de la clé Système de notation du risque sont de 0201 à 0220.

Il importe de souligner que ce principe général s'applique si on envisage l'agrégation des mesures de la dimension NIRE (pour des valeurs de clé Système de notation du risque et Industrie constantes), ou de la dimension Industrie (pour des valeurs de clé Système de notation du risque et NIRE constantes).

###### Variantes de l'agrégation par sommation

Dans certains cas, la structure d'enregistrement peut exiger seulement la déclaration des mesures d'un sous-ensemble de valeurs de clé d'une dimension. Seules les mesures de bas niveau déclarées sont alors prises en compte dans la somme. Par exemple, si vous devez déclarer uniquement un sous-ensemble des valeurs de clé pour la dimension Système de notation du risque (p. ex., les valeurs de clé 0201 à 0205), la somme de la clé Total – Systèmes de notation du risque (clé 200) ne tient compte que du sous-ensemble précisé.

Il peut arriver que pour certains fichiers de données de relevé, la structure d'enregistrement exige la déclaration des mesures totales seulement, et non des mesures de bas niveau. Dans un tel cas, le BSIF ne peut pas valider l'agrégation des différents niveaux.

Enfin, il peut arriver qu'une structure d'enregistrement exige seulement la déclaration des mesures des valeurs de clé de bas niveau, et non les valeurs de clé totales des niveaux supérieurs de la hiérarchie. Dans ce cas, le BSIF ne valide pas les valeurs totales.

##### 5.4.2. Règles d'agrégation par sommation pour les dimensions du portefeuille

Les règles d'agrégation par sommation suivantes sont utilisées pour les différentes dimensions figurant dans les fichiers de données des relevés des portefeuilles suivants : partie 1 du portefeuille de la clientèle de détail assujetti à l'approche NI;partie 2 du portefeuille de la clientèle de détail assujetti à l'approche NI;partie 1 du portefeuille de la clientèle de gros assujetti à l'approche NI; partie 2 du portefeuille de la clientèle de gros assujetti à l'approche NI.

Dans les descriptions suivantes des règles, le terme « mesure » se rapporte aux montants, aux pourcentages et aux autres valeurs numériques seulement qui résultent d'une addition des valeurs qui figurent dans la dimension en question.

Règles d'agrégation – NIRE
:   La mesure de la valeur de clé 0100 (Total – NIRE) correspond à la somme des mesures des valeurs de clé consécutives 0101 à 0125 (de la 1ère à la 25e NIRE).

Règles d'agrégation – Système de notation du risque
:   Pour le portefeuille de la clientèle de gros, la mesure de la valeur de clé 0200 (Total – Systèmes de notation du risque) correspond à la somme des mesures des valeurs de clé consécutives 0201 à 0220 (du 1er au 20e système de notation du risque).
:   Pour le portefeuille de la clientèle de détail, la mesure de la valeur 0200 (Total – Systèmes de notation du risque) correspond à la somme des mesures des valeurs de clé consécutives 0201 à 0240 (du 1er au 40e système de notation du risque).

Règles d'agrégation – Région géographique
:   La mesure de la valeur de clé 0301 (Total – Canada) correspond à la somme des mesures des valeurs de clé consécutives 0302 à 0314 (provinces et territoires).
:   La mesure de la valeur de clé 0300 (Total – Région géographique) correspond à la somme des mesures des valeurs de clé 0301 (Total – Canada) et 0315 à 0319 (régions géographiques autres que le Canada).

Règles d'agrégation – Ratio prêt/valeur
:   La mesure de la valeur de clé 0400 (Total – Ratio prêt/valeur) correspond à la somme des mesures des valeurs de clé consécutives 0401 à 0404 (catégories classifiées) et 0405 (catégorie non classifiée).

Règles d'agrégation – Titrisation
:   Aucune règle n'est définie, cette dimension ne comprenant aucune valeur cumulative pour le moment.

Règles d'agrégation – Taux
:   La mesure de la valeur de clé 0700 (Total – Taux) correspond à la somme des mesures des valeurs de clé consécutives 0701 (taux fixe) et 0702 (taux variable).

Règles d'agrégation – Catégories de retard
:   La mesure de la valeur de clé 0800 (Total – Catégories de retard) correspond à la somme des mesures des valeurs de clé consécutives 0801 à 0805 (catégories de retard connues).

Règles d'agrégation – Segment de PD
:   La mesure de la valeur de clé 0900 (Total – Segments de PD) correspond à la somme des mesures des valeurs de clé consécutives 0901 à 0925 (du 1er au 25e segment de PD).

Règles d'agrégation – Segment de PCD
:   La mesure de la valeur de clé 3200 (Total – Segments de PCD) correspond à la somme des mesures des valeurs de clé consécutives 3201 à 3225 (du 1er au 25e segment de PCD).

Règles d'agrégation – Segment de FECD
:   La mesure de la valeur de clé 3300 (Total – Segments de FECD) correspond à la somme des mesures des valeurs de clé consécutives 3301 à 3325 (du 1erau 25e segment de FECD).

Règles d'agrégation – Horizon
:   La mesure de la valeur de clé 1000 (Total – Horizons) correspond à la somme des mesures des valeurs de clé consécutives 1001 à 1002 (divers horizons annuels).

Règles d'agrégation – Industrie
:   La mesure de la valeur de clé 1200 (Total – Industrie) correspond à la somme des mesures des valeurs de clé consécutives 1201 à 1248 (48 catégories d'industrie).

Règles d'agrégation – Catégorie de PD
:   La mesure de la valeur de clé 1400 (Total – Catégories de PD) correspond à la somme des mesures des valeurs de clés consécutives 1401 à 1426 (de la 1ère à 26e catégorie de PD).

Règles d'agrégation – Importance de l'exposition
:   Aucune règle n'est définie, cette dimension ne comprenant aucune valeur cumulative pour le moment.

Règles d'agrégation – NRF
:   La mesure de la valeur de clé 1600 (Total – NRF) correspond à la somme des mesures des valeurs de clé consécutives 1601 à 1625 (de la 1ère à la 25e NRF).

Règles d'agrégation – Catégorie d'exposition (relevés portant sur le portefeuille de la clientèle de détail)
:   Ces règles sont utilisées pour la dimension Catégorie d'exposition définie dans les parties 1 et 2 des relevés portant sur le portefeuille de la clientèle de détail assujetti à l'approche NI.
:   La mesure de la valeur de clé 0502 (Prêts hypothécaires) correspond à la somme des mesures des valeurs de clé consécutives 0510 (Prêts hypothécaires résidentiels assurés par la SCHL), 0511 (Autres prêts hypothécaires résidentiels assurés) et 0512 Prêts hypothécaires résidentiels non assurés).
:   La mesure de la valeur de clé 0501 (Prêts hypothécaires et marges-crédit sur valeur domiciliaire) correspond à la somme des mesures des valeurs de clé consécutives 0502 (Prêts hypothécaires) et 0503 (Marges-crédit sur valeur domiciliaire).
:   La mesure de la valeur de clé 0504 (Total – Produits de détail renouvelables admissibles) correspond à la somme des mesures des valeurs de clé consécutives 0505 (Cartes de crédit) et 0506 (Marges-crédit).
:   La mesure de la valeur de clé 0500 (Total – Clientèle de détail) correspond à la somme des mesures des valeurs de clé 0501 (Prêts hypothécaires et marges-crédit sur valeur domiciliaire), 0504 (Total – Produits de détail renouvelables admissibles) et 0507 (Autres produits de détail).

Règles d'agrégation – Catégorie d'exposition (relevés portant sur le portefeuille de la clientèle de gros)
:   Ces règles sont utilisées pour la dimension Catégorie d'exposition définie dans les partie 1 et 2 des relevés portant sur le portefeuille de la clientèle de gros assujetti à l'approche NI.
:   La mesure de la valeur de clé 1807 (Immobilier de rapport) correspond à la somme des mesures des valeurs de clé 1825 (Immeubles résidentiels à logements multiples productifs de revenus) et 1826 (Autres biens productifs de revenus).
:   La mesure de la valeur de clé 1808 (Immobilier commercial à forte volatilité) correspond à la somme des mesures des valeurs de clés 1823 (Total – Terrains pour subdivision) et 1824 (Financement intermédiaire).
:   La mesure de la valeur de clé 1801 (Total – Entreprises) correspond à la somme des mesures des valeurs de clé consécutives 1804 à 1810 (diverses sous-catégories d'exposition liées aux entreprises).
:   La mesure de la valeur de clé 1800 (Total – Clientèle de gros) correspond à la somme des mesures des valeurs de clé 1801 (Total – Entreprises), 1802 (Banques) et 1803 (Emprunteurs souverains). À l'heure actuelle, il n'y pas de valeur « inconnue » (1898).

#### 5.5. Règles concernant la redondance des données

Plusieurs mesures du relevé sont déclarées dans plus d'un type d'enregistrement. On s'attend que les valeurs déclarées dans chaque type d'enregistrement soient conformes pour chaque mesure. Par exemple, l'encours du total général déclaré au type d'enregistrement 030 du relevé Portefeuille de la clientèle de gros – Partie 1 doit correspondre à l'encours du total général déclaré au type d'enregistrement 050 du relevé Portefeuille de la clientèle de gros – Partie 1 (Total de la catégorie d'exposition, NIRE, région géographique). La même attente s'applique aux mesures supplémentaires des mêmes types d'enregistrements et aux combinaisons éventuelles de SNR, NIRE et région géographique. Il convient de noter qu'une tolérance de 5 % ou de 20 (correspondant à 20 000 $) est acceptée (pour tenir compte d'éventuels problèmes d'arrondissement), toutefois, un écart supérieur à la fois à 5 % et à 20 entraîne un message d'erreur et les données sont rejetées.

La tolérance de 5 % est appliquée ainsi : dans le cas de deux nombres comparables (décrits dans les équations ci-après), le ratio des deux (quelque soit la direction) doit toujours se situer entre 0,95 et 1,05.

La présente section décrit les « règles de redondance » qui s'appliquent au relevé Portefeuille de la clientèle de gros – Partie 1.

##### 5.5.1. Redondance des données – Groupe 1

Le Groupe 1 comprend les « règles de redondance » qui s'appliquent aux types d'enregistrement suivants du relevé Portefeuille de la clientèle de gros – Partie 1 : 015, 030, 050 et 075. (Valeurs affichées de

![formule mathématique 1](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math1.gif)

où « Ex.C » désigne la clé de dimension de la catégorie d'exposition valide des types d'enregistrement applicables, et « r » désigne les clés de dimension de la taille d'exposition (« 0201 … 0220 »), tandis que 0100, 0300 et 1200 représentent le total des clés pour NIRE, Région géographique et Industrie, respectivement.

![formule mathématique 2](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math2.gif)

où « RRS » désigne la clé de dimension de la catégorie d'exposition valide des types d'enregistrement applicables, tandis que 0100, 0300 et 1200 représentent le total des clés pour NIRE, Région géographique et Industrie, respectivement.

![formule mathématique 3](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math3.gif)

où « BIRR, RRS et EX.C » désignent les clés de dimension de la catégorie d'exposition valide des types d'enregistrement applicables, tandis que 0300 et 1200 représentent le total des clés pour Région géographique et Industrie, respectivement.

Les règles applicables au groupe 1 s'appliquent à la mesure supplémentaire suivante :

* Autorisé (champ 1)
* Encours (champ 2)
* Valeur estimative de la probabilité de défaut selon l'approche NI (champ 11)
* Perte attendue selon l'approche NI (champ 12)
* Perte économique (champ 14)
* Radiations (champ 15)
* Recouvrements (champ 19)
* Fonds propres selon l'approche NI (champ 13)
* Liste de surveillance - Autorisé (champ 3)
* Liste de surveillance - Encours (champ 4)

##### 5.5.2. Redondance des données – Groupe 2

Le Groupe 2 comprend les « règles de redondance » qui s'appliquent aux types d'enregistrement suivants du relevé Portefeuille de la clientèle de gros – Partie 1 : 020, 080 et 090. (Valeurs affichées sous la forme

![formule mathématique 4](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math4.gif)

où 1800, 0300 et 1200 représentent le total des clés pour Catégories d'exposition, Région géographique et Industrie.

Les règles applicables au groupe 1 s'appliquent à la mesure supplémentaire suivante :

* Total des provisions pour pertes sur créances (champ 17)
* Provisions individuelles pour pertes sur créances (champ 18)
* Acceptations et prêts de crédit douteux (champ 20)
* Ajouts aux acceptations et prêts de crédit douteux (champ 23)

##### 5.5.3. Redondance des données – Groupe 3

Le Groupe 3 comprend les « règles de redondance » qui s'appliquent aux types d'enregistrement suivants du relevé Portefeuille de la clientèle de gros – Partie 1 : 015, 080 et 090. (Valeurs affichées sous la forme

![formule mathématique 5](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math5.gif)

où 1800, 0300 et 1200 représentent le total des clés « Catégories d'exposition », « Région géographique » et « Industrie », respectivement.

Les règles applicables au groupe 3 s'appliquent à la mesure supplémentaire suivante :

* Facilités autorisées (champ 1)
* Encours (champ 2)

##### 5.5.4. Redondance des données – Groupe 4

Le Groupe 4 comprend les « règles de redondance » qui s'appliquent aux types d'enregistrement suivants du relevé Portefeuille de la clientèle de gros – Partie 1 : 020 et 100. (Valeurs affichées sous la forme *RTxx*(*measure*, dim*ension\_key*1, dim*ension\_key*2, etc) pour le type d'enregistrement 0XX.)

![formule mathématique 6](/sites/default/files/import-media/data_and_forms/deposit-taking-institutions/2017-08/fr/ws_prt_cdts_math6.gif)

où « Ex.C » désigne la clé de dimension de la catégorie d'exposition valide des types d'enregistrement applicables, et « r » désigne les clés de dimension de la taille d'exposition (« 0201 … 0220 »), tandis que 0100 représente le total des clés pour NIRE.

Les règles applicables au groupe 4 s'appliquent à la mesure supplémentaire suivante :

* Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés (champ 21)

#### 5.6. Autres règles relatives aux opérations

##### 5.6.1. Montants (en dollars)

La section réservée à la règle de validation des montants en dollars décrit les règles de validation entre les mesures qui s'appliquent au relevé. Veuillez prendre note que chaque comparaison entre des mesures doit s'appliquer aux combinaisons de clés de dimension du même type d'enregistrement et du même niveau hiérarchique. (En d'autres termes, toutes les clés de dimension doivent être égales.) Les validations « entre niveaux » et « entre types d'enregistrement » sont abordées dans une section distincte du présent document. (Sections 5.4 – Règles d'agrégation et 5.5 – Règles concernant la redondance des données, respectivement)

* Encours (champ 2) ne doit pas dépasser la valeur autorisée (champ 1) de plus de 1 %, sinon les données sont rejetées.
* L'estimation du facteur d'exposition en cas de défaut selon l'approche NI (champ 11) ne doit pas dépasser la valeur autorisée (champ 1) de plus de 1 %, sinon les données sont rejetées.
* La perte attendue selon l'approche NI (champ 12) ne doit pas dépasser la valeur autorisée (champ 1) de plus de 1 %, sinon les données sont rejetées.
* La liste de surveillance - Encours (champ 4) ne doit pas dépasser la valeur de la liste de surveillance - autorisée (champ 3) de plus de 1 %, sinon les données sont rejetées

##### 5.6.2. Nombre d'emprunteurs

Le nombre d'emprunteurs (champ 5) ne doit pas dépasser 1000 fois la valeur de l'encours déclaré (champ 2). Autrement dit, on doit avoir en moyenne un encours d'au moins 1 $ par emprunteur, sinon les données sont rejetées.

De plus, le nombre total d'emprunteurs (champ 5) qui figure dans tous les types d'enregistrements doit être supérieur à zéro, sinon les données seront rejetées.

Les règles qui régissent le nombre d'emprunteurs ne comportent aucun niveau de tolérance.

##### 5.6.3. Valeurs négatives

L'inscription de valeurs négatives dans le relevé entraîne un refus, aux exceptions suivantes : Perte économique (champ 14), Radiations (champ 15), Recouvrements (champ 19) et Provisions individuelles pour pertes sur créances (champ 18), Provisions collectives pour pertes sur créances (champ 29), Autres changements aux acceptations et prêts de crédit douteux (champ 31), Autres changements aux dotations aux pertes sur créances (champ 30); dans ces cas, les valeurs négatives sont réputées acceptables dans certaines situations.

#### 5.7. Éléments de données facultatifs ou obligatoires

Les points de données réputés « facultatifs » s'appliquent aux situations où le point de donnée n'existe peut-être pas pour toutes les institutions financières. Toutefois, si une institution financière dispose des données pour un champ « facultatif », celles-ci doivent être déclarées dans le relevé.

Les champs obligatoires sont réservés aux points de données qui doivent être déclarés par toutes les institutions financières, sinon les données sont rejetées.

#### 5.8. Relevé des erreurs

Si l'une des règles de validation ci-dessus n'est pas respectée, un relevé des erreurs est produit et le fichier des données est rejeté. Le contenu du relevé des erreurs varie selon le type d'erreur décelé. Le relevé contient tous les renseignements nécessaires pour faciliter la compréhension et la correction des erreurs. Cependant, si le relevé des erreurs ne renferme que des avertissements, le fichier de données est accepté par le BSIF. Il convient de noter qu'il fautquand même corriger toutes les données erronées ou incohérentes (autrement dit, éliminer les messages « d'avertissement » qui s'y rattachent) pour la transmission de données suivante.

L'institution financière visée reçoit un courriel confirmant ou infirmant l'enregistrement du fichier dans la base de données. Si des problèmes ont été décelés, le relevé des erreurs (renfermant les « erreurs » et les « avertissements ») est joint à ce courriel.

### Relevé des modifications

#### Modifications à signaler dans la version 2.0

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 1.0 de ce document lorsqu'il consulte le présent relevé.

Les institutions qui n'utilisaient pas la version précédente du présent document n'ont pas besoin de tenir compte des modifications signalées ci-dessous.

1. Section 2.1 Sans objet
2. Section 3.1 Format d'un enregistrement TableauExemple – Format d'un enregistrement; la longueur du segment de mesures est modifiée de 361 à352
3. Section 4.1 Type de fichier et convention de désignation des fichiers La chaîne de désignation « IRBWHOA » est remplacée par « BB ».
4. Section 4.4 Ajout de « Métaux de première fusion et aluminium » dans la liste Clé primaire industrie (1248)
5. Section 4.5 Structures d'enregistrement – Enregistrement de début (000)
6. La mention du nom du relevé « IRBWHOA » est remplacée par « BB ».Section 4.5 Structures d'enregistrement – Déclaration des NIRE (010) Le type d'enregistrement est modifié de « 110 » à « 010 ».
7. Section 4.5 Structures d'enregistrement – Déclaration des NIRE (010)

   Les NIRE doivent être précisées dans le contexte d'un SNR. Et toutes les structures renvoyant à une NIRE ou un SNR sont modifiées. Voir :

   * NIRE et Région géographique, Systèmes de notation du risque (040)
   * NIRE et Région géographique, Catégories et sous-catégories d'exposition (050)
   * NIRE et Industrie, Systèmes de notation du risque (060)
   * NIRE et Industrie, Catégories et sous-catégories d'exposition (070)
   * NIRE et Catégories et sous-catégories d'exposition (100)
8. Section 5.4.1 Agrégation par sommation – Nouvel énoncé sur les valeurs agrégées correspondant aux pourcentages et aux ratios.
9. Section 5.4.2 Règles d'agrégation par sommation pour les dimensions du portefeuille – Suppression de la rubrique « Règles d'agrégation – Notation interne ».

#### Modifications à signaler dans la version 3.0

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 2.0 de ce document lorsqu'il consulte le présent relevé.

Les institutions qui n'utilisaient pas la version précédente du présent document n'ont pas besoin de tenir compte des modifications signalées ci-dessous.

1. Section 4.5 Structures d'enregistrementRemarques importantes – La remarque concernant les champs contenant des valeurs en pourcentage ou en dollars a été supprimée parce cette question est abordée plus en détail à la section suivante.
2. Section 4.5 Structures d'enregistrement – Enregistrement de début (000) Nouvelle remarque (Nom du relevé) : « remplissage à droite par des espaces ».
3. Section 4.5 Structures d'enregistrement – Enregistrement de début (000) Nouvelle remarque (Version du format du fichier de relevé) : « pic(X) – Chaîne fixe « 03.0.0 ».
4. Section 5.3.2 Règles concernant les probabilités et les pourcentages (point 4) Nouvelle remarque : Ne pas employer la virgule.

#### Modifications à signaler dans la version 3.0 (numéro 2)

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 3.0 de ce document lorsqu'il consulte le présent relevé. Précisons que les modifications de nature superficielle ne sont pas signalées ici.

Les institutions qui n'utilisaient pas la version précédente du présent document n'ont pas besoin de tenir compte des modifications signalées ci-dessous.

1. Section 1 Introduction Les relevés du portefeuille NCR sont renommés Partie 1 et Partie 2, reflétant le fait qu'ils doivent être présentés par l'entremise du SATD et du Système de base de données interinstitutions (SBDI).
2. Section 4.4 Les options 'catégorie inconnue' sont supprimées de la liste des clés de dimension là où elles n'étaient pas utilisées. (NIRE – 0198; SNR – 0298; Catégorie d'exposition – 1898)
3. Section 4.5 Structure d'enregistrement (005) et (010) Note ajoutée pour préciser que les systèmes de notation du risque et les NIRE doivent être les mêmes dans tous les relevés NCR, mais que les systèmes de notation du risque ne sont pas tous nécessairement assortis d'une NIRE.
4. Section 4.5 Structures d'enregistrement – Déclaration des segments (010) Note ajoutée pour préciser que l'ordre de déclaration des NIRE doit refléter la PD estimative de leur notation.
5. Section 4.5 Structures d'enregistrement (040, 050, 060, 070 et 100) Note ajoutée pour préciser les agencements de SNR et de NIRE à inclure dans les types d'enregistrement.
6. Section 4.5 Structures d'enregistrement (060, 070 and 090) Notes modifiées pour inclure les codes 1248 (métaux de première fusion et aluminium) et le champ 1298 (secteur inconnu) dans le champ « Industrie ».
7. Section 5.2 Vérifications préalables au traitement Ajout d'une dixième consigne.
8. Section 5.3.1 Règles concernant les montants Modification/ajout des remarques # 3 et # 4 pour incorporer la notion de valeur négative. Illustrée par un exemple.
9. Section 5.3.2 Modification/ajout des remarques # 2 et # 4 et #5 pour incorporer la notion de valeur négative. Illustrée par un exemple.
10. Section 5.3.3 Règles concernant les autres valeurs numériques Modification/ajout des remarques # 2 et # 4 pour incorporer la notion de valeur négative. Illustrée par un exemple.
11. Section 5.4.1 Agrégation par sommation Nouvelle note précisant les modalités d'agrégation des mesures ne résultant pas d'une addition, p. ex., Nombre d'emprunteurs.
12. Section 5.4.2 Règles d'agrégation par sommation pour les dimensions du portefeuille Correction de la règle sur l'agrégation des catégories données de l'industrie (incluant le code 1248)
13. Section 5.4.2 Règles d'agrégation par sommation pour les dimensions du portefeuille La règle d'agrégation des catégories de PD est corrigée (inclusion du code 1426)
14. Section 5.4.2 Règles d'agrégation par sommation pour les dimensions du portefeuille La dimension « catégorie inconnue » est supprimée de la liste des clés de dimension là où elle n'était pas utilisée.
15. Section 5.4.2 Règles d'agrégation par sommation pour les dimensions du portefeuille Les dimensions ne s'appliquant pas aux banques assujetties à l'approche NI ont été supprimées.

#### Modifications à signaler dans la version 4.0

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 3.0 de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici.

Les institutions qui n'utilisaient pas la version précédente du présent document n'ont pas besoin de tenir compte des modifications signalées ci-dessous.

1. Section 4.4 Clé primaire NIRE Le nombre de NIRE disponibles est passé de 40 à 25. Cela se reflète ailleurs dans le document – structures d'enregistrement, validation, etc.
2. Section 4.5 Structures d'enregistrement (000) Champ « Version du fichier » – la remarque se lit maintenant pic(X) – Chaîne fixe « 04.0.0. »
3. Section 4.5 Structures d'enregistrement – Enregistrement de début (000) Les types d'enregistrement 040 et 060 ont été supprimés. Tous les renvois qui s'y rapportaient ont aussi été supprimés.
4. Section 4.5 Structure d'enregistrement – Type d'enregistrement 050 La remarque correspondant à la clé dimension de la région géographique est modifiée, y compris les États-Unis (0315) et le Mexique (0316)
5. Section 5.5 Règles concernant la redondance des données Nouvelle section dans laquelle sont résumées les règles concernant la redondance des données entre les types d'enregistrements.
6. Section 5.6.1 Montants (en dollars) Nouvelle section dans laquelle sont résumées les règles de validation entre les mesures.
7. Section 5.6.2 Nombre d'emprunteurs Nouvelle section dans laquelle sont décrites les règles de validation concernant le nombre d'emprunteurs.
8. Section 5.6.3 Valeurs négatives Nouvelle section dans laquelle sont décrites les règles de validation concernant les valeurs négatives.
9. Section 5.6.7 Éléments de données facultatifs et obligatoires Nouvelle section sur l'interprétation des éléments de données dont la production est facultative ou obligatoire.
10. Section 5.8 Relevé des erreurs Des précisions sont apportées à la section « Relevé des erreurs ».

#### Modifications à signaler dans la version 4.0 – numéro 2

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 4.0 de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.

Les institutions qui n'utilisaient pas la version 4.0 du présent document n'ont pas besoin de tenir compte des modifications signalées ci-dessous.

1. Section 5.6.2 Nombre d'emprunteurs La première règle de validation, qui visait la mesure « Encours », vise désormais la mesure « Facilités autorisées ». La deuxième règle de validation a été précisée.
2. Section 5.8 Relevé des erreurs Le dernier paragraphe de cette section, qui portait sur la « période de tolérance », a été supprimé parce que cette mesure ne s'applique pas aux relevés produits après le 1er décembre 2007.

#### Modifications à signaler dans la version 5.0

Les modifications qui suivent ont été apportées depuis la dernière version du présent document. Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 4.0, numéro 2, de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.  
Les institutions qui n'utilisaient pas la version 4.0, numéro 2 du présent document n'ont pas besoin de tenir compte des modifications signalées ici.

1. Section 4.4 Suppression du commentaire au sujet de la dimension « inconnu ». La dimension « inconnu » (XX98) n'apparaît plus dans les tableaux de dimension des clés primaires.
2. Section 4.5 Structures d'enregistrement Suppression du commentaire au sujet de la dimension « inconnu ». La dimension « inconnu » (XX98) n'apparaît plus dans les tableaux des structures d'enregistrement.
3. Section 4.5 Structures d'enregistrement Enregistrement de début (000) La version du format du fichier du relevé est maintenant de 05.0.0.
4. Section 5.4 Règles d'agrégation La dimension « inconnu » (XX98) n'apparaît plus dans la description des règles d'agrégation.
5. Section 5.4 Règles d'agrégation Introduction de la valeur absolue « 20 » à la tolérance des règles d'agrégation – en plus du 5 % qui était déjà prévu.
6. Section 5.5 Règles concernant la redondance des données Introduction de la valeur absolue « 20 » à la tolérance des règles concernant la redondance des données – en plus du 5 % qui était déjà prévu.

#### Modifications à signaler dans la version 6.0 et 6.1

Les modifications qui suivent ont été apportées depuis la dernière version du présent document. Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 5.0, de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.

Les institutions qui n'utilisaient pas la version 5.0 du présent document n'ont pas besoin de tenir compte des modifications signalées ici.

##### Généralités

1. La mesure « Provisions pour pertes sur prêts » a été renommée « Total des provisions pour pertes sur créances » (sections 2.1, 2.2, 3.4, 4.4, 5.5.2).
2. La mesure « Provisions spécifiques » a été renommée « Provisions spécifiques pour pertes sur créances » (sections 2.1, 2.2, 3.4 ,4,4, 5.5.2).
3. Sans objet dans la version française.
4. Les références à la valeur de clé dimensionnelle « Inconnu » ont été supprimées.

##### Section 4.4

5. Mise en retrait de la description de la valeur de clé primaire pour illustrer les différents échelons de la hiérarchie relative à chaque dimension.
6. Modification de la description des valeurs de clé primaire Région géographique suivantes :
   * 0306 –« Terre-Neuve » remplacé par « Terre-Neuve-et-Labrador »
   * 0314 – « Territoire du Yukon » remplacé par « Yukon »
7. Ajout de dix dimensions SNR au tableau Clé primaire Système de notation du risque :
   * 0211 – 11e système de notation du risque
   * […]
   * 0220 – 20e système de notation du risque
8. Valeur de clé « Entreprises » (1801) renommée « Total – Entreprises ».
9. Ajout de quatre nouvelles sous-catégories d'exposition dans le tableau Clé primaire Catégorie d'exposition :
   * Sous 1807 – Immobilier commercial à forte volatilité
     + 1823 – Total – Terrains pour subdivision
     + 1824 – Financement intermédiaire
   * Sous 1808 – Immobilier de rapport
     + 1825 – Immeubles résidentiels à logements multiples productifs de revenus
     + 1826 – Autres biens productifs de revenus

##### Section 4.5

10. La remarque relative au champ de données « Système de notation du risque », auparavant « Chaînes fixes "0200" à "0210" a été remplacée par « Chaînes fixes "200", "0201", "0202" à "0220", au besoin », afin de préciser qu'au moins un SNR doit être déclaré et que les mesures de ce SNR, ainsi que le total des SNR doivent être déclarés.Cette modification a des répercussions sur les types d'enregistrement suivants :
    * 005 – Déclaration des systèmes de notation du risque
    * 010 – Déclaration des NIRE
    * 030 – Système de notation du risque
    * 050 – NIRE et Région géographique, Catégories et sous-catégories d'exposition
    * 070 – NIRE et Industrie, Catégories et sous-catégories d'exposition
    * 100 – NIRE et Catégories et sous-catégories d'exposition
11. La remarque relative au champ de données « NIRE », auparavant « Chaînes fixes "0100" à "0125", au besoin » a été remplacée par « Chaînes fixes "0100", "0101", "0102" à "0125", au besoin », afin de préciser qu'au moins une NIRE doit être déclaré et que les mesures de cette NIRE doivent être déclarées. Cette modification a des répercussions sur les types d'enregistrement suivants :
    * 010 – Déclaration des NIRE
    * 050 – NIRE et Région géographique, Catégories et sous-catégories d'exposition
    * 070 – NIRE et Industrie, Catégories et sous-catégories d'exposition
    * 100 – NIRE et Catégories et sous-catégories d'exposition
12. Type d'enregistrement 000 –Enregistrement de début
    * La version du format de fichier « 05.0.0 » a été remplacée par « 06.0.0 ».
13. Type d'enregistrement – Déclaration des systèmes de notation du risque (005) et type d'enregistrement 010 – Déclaration des NIRE
    * La remarque relative au champ de données « Système de notation du risque », auparavant « Chaînes fixes "0201" à "0210" a été remplacée par « Chaînes fixes '0201', '0202' à '0220', au besoin », afin de préciser qu'au moins un SNR doit être déclaré.
    * Attribution du champ 32 au nom du système de notation du risque.
14. Type d'enregistrement 010 – Déclaration des NIRE
    * La remarque relative au champ de données « NIRE », auparavant « Chaînes fixes "0101" à "0125", au besoin » a été remplacée par « Chaînes fixes "0101", "0102" à "0125", au besoin », afin de préciser qu'au moins une NIRE doit être déclarée.
    * Attribution du champ 33 au nom de la NIRE.
15. Type d'enregistrement 015 – Tableau des totaux, toutes les catégories et sous-catégories d'exposition
    * Ajout de quatre nouvelles catégories d'exposition (1823 – Total – Terrains pour subdivision, 1824 – Financement intermédiaire, 1825 – Immeubles résidentiels à logements multiples productifs de revenus et 1826 – Autres biens productifs de revenus).
16. Type d'enregistrement 020 – Tableau des totaux, trois catégories d'exposition seulement
    * Ajout des champs de données suivants :
      + Provisions générales pour pertes sur créances
      + Autres changements aux dotations aux pertes sur créances
      + Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés
      + Autres changements aux acceptations et prêts de crédit douteux
    * Modification de la position de départ et de la longueur du champ « Caractères de remplissage ».
17. Types d'enregistrement 080 – Région géographique et 090 – Industrie
    * Ajout des champs de données « Encours » et « Facilités autorisées ».
    * Modification de la position de départ et de la longueur du champ « Caractères de remplissage ».
18. Type d'enregistrement 100 – NIRE et Catégories et sous-catégories d'exposition
    * Champ « Total – Acceptations et prêts douteux dont les intérêts recommencent à être comptabilisés » renommé « Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés ».
19. Mesure de la valeur de clé 400 (« Total Canada ») renommée « Total – Ratio prêt/valeur ».
20. Rubrique « Règles d'agrégation – Segment » renommée « Règles d'agrégation – Segment de PD ».
21. Ajout de deux nouvelles règles d'agrégation des enregistrements :
    * Règles d'agrégation – Segment de PCD
    * Règles d'agrégation – Segment de FECD
22. Modification des Règles d'agrégation – Catégorie d'exposition (relevés portant sur le portefeuille de la clientèle de détail) pour inclure les trois nouvelles catégories d'exposition (0510, 0511 et 0512).
23. Modification des Règles d'agrégation – Catégorie d'exposition (relevés portant sur le portefeuille de la clientèle de gros) pour inclure les quatre nouvelles catégories d'exposition (1823, 1824 et 1825, 1826).

##### Section 5.5.1

24. Modification de la rubrique Redondance des données – Groupe 1 pour inclure les nouvelles clés de dimension de la taille d'exposition (c.-à-d., de 0210 à 0220) et ajout de la formule de calcul des règles de redondance pour Industrie.

##### Section 5.5.3

25. Ajout d'une nouvelle règle de redondance des données (Groupe 3) pour vérifier que les montants « Facilités autorisées » et « Encours » du type d'enregistrement 015 correspondent aux types d'enregistrement 080 et 090.

##### Section 5.5.3

25. Added new data redundancy rule (Group 3) to ensure Facilités autorisées and Encours Amounts in Type d'enregistrement 015 are equal to that in Type d'enregistrement 080 and 090

##### Section 5.5.4

26. Ajout d'une nouvelle règle de redondance des données (Groupe 4) pour vérifier que le montant « Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés » du type d'enregistrement 020 correspond au type d'enregistrement 100.

##### Section 5.6.3

27. Ajout de quatre exceptions aux règles de validation des valeurs négatives :
    * Provisions spécifiques pour pertes sur créances (champ 18)
    * Provisions générales pour pertes sur créances (champ 29)
    * Autres changements aux acceptations et prêts de crédit douteux (champ 31)
    * Autres changements aux dotations aux pertes sur créances (champ 30)

##### Version 6.1

28. Section 5.5.4 – Redondance des données – Groupe 4.
    * La règle est appliquéeà « Acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés » (champ 21), plutôt qu'à «Acceptations et prêts de crédit douteux » (champ 20).
29. Sommaire des modifications à signaler dans la version 6.0 ci-dessus – no 9
    * No 9 – Ajout de quatre nouvelles sous-catégories d'exposition
      + Sous 1808 – Immobilier commercial à forte volatilité
        - 1823 – Total – Terrains pour subdivision
        - 1824 – Financement intermédiaire
      + Sous 1807 – Immobilier commercial à forte volatilité
        - 1825 – Immeubles résidentiels à logements multiples productifs de revenus
        - 1826 – Autres biens productifs de revenus

#### Modifications à signaler dans la version 6.2

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 6.1 de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.

Les institutions qui n'utilisaient pas la version 6.1 du présent document n'ont pas besoin de tenir compte des modifications signalées ici.

##### Généralités

1. L'expression « système de notation du risque » se lit maintenant « système de notation du risque du portefeuille de la clientèle de gros ».

##### Section 2.2 – Enregistrements et valeurs de clé

2. Correction du nom de certaines mesures citées comme exemples.

##### Section 4.3 – Types d'enregistrement

3. Modification du nom du type d'enregistrement 005 pour « Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros ».

##### Section 4.5 – Structures d'enregistrement

4. Modification du nom pour « Déclaration des systèmes de notation du risque du portefeuille de la clientèle de gros(005) ».
5. Ajout d'une remarque décrivant la séparation des déclarations concernant les systèmes de notation du risque du portefeuille de la clientèle de gros et ceux du portefeuille de la clientèle de détail, ainsi que la fourchette des valeurs de clé des systèmes de notation du risque.

##### Section 5.4.2 – Règles d'agrégation par sommation pour les dimensions du portefeuille

6. Séparation des règles d'agrégation relatives au système de notation du risque du portefeuille de la clientèle de détail de celles qui touchent le système de notation du risque du portefeuille de la clientèle de gros.

#### Modifications à signaler dans la version 6.3

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 6.2 de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.

Les institutions qui n'utilisent pas la version 6.2 du présent document n'ont pas besoin de tenir compte des modifications signalées ici.

##### Généralités

1. L'expression « provisions spécifiques pour pertes sur créances » est remplacée par « provisions individuelles pour pertes sur créances ».
2. L'expression « provisions générales pour pertes sur créances » est remplacée par « provisions collectives pour pertes sur créances ».

#### Modifications à signaler dans la version 6.4

Le présent relevé s'adresse aux spécialistes. Nous l'avons préparé pour leur signaler les modifications apportées aux spécifications techniques depuis la version précédente. Le lecteur devrait avoir en main la version 6.3 de ce document à des fins de comparaison. Précisons que les modifications de nature superficielle ne sont pas signalées ici – elles ne devraient avoir aucune incidence sur le développement.

Les institutions qui n'utilisent pas la version 6.3 du présent document n'ont pas besoin de tenir compte des modifications signalées ici.

##### Généralités

1. L'expression « **acceptations et prêts douteux bruts** » est remplacée par « **acceptations et prêts de crédit douteux** ».
2. L'expression « **ajouts aux acceptations et prêts douteux bruts** » est remplacée par « **ajouts aux acceptations et prêts de crédit douteux** ».
3. L'expression « **acceptations et prêts douteux bruts dont les intérêts recommencent à être comptabilisés** » est remplacée par « **acceptations et prêts de crédit douteux dont les intérêts recommencent à être comptabilisés** ».
4. L'expression « **autres changements aux acceptations et prêts douteux bruts** » est remplacée par « **autres changements aux acceptations et prêts de crédit douteux** ».

Signaler un problème ou une erreur sur cette page

Date de modification :
:   2017-08-14