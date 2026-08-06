# Tout règles de validation applicables au relevé H4

Information

Type de document

Règles de validation

Secteur

Institutions de dépôt

Relevé

Relevé des sûretés et des opérations de nantissement (H4)

Dernière révision

2017

Numéro de relevé

H4

Documentation

* [Relevé des sûretés et des opérations de nantissement (H4)](/fr/donnees-formulaires/rapports-releves/produire-releve-financier/guides-production-releves-financiers/releve-suretes-operations-nantissement-h4)

Pour de plus amples renseignements, veuillez écrire à James Younker ([jyounker@banqueducanada.ca](mailto:jyounker@banqueducanada.ca)).

## Principales règles de validation au sein d'un même relevé

### Actifs grevés et non grevés

Actifs grevés = Trésorerie (liquidités grevées)
:   + Marge de liquidité fournie  
    + Entrée de sûretés (non réhypothécables)  
    + Sortie de sûretés  
    + Ajustements

* a106 = (-1)\*a4 + (-1)\*a15 + (-1)\*(a41+a44+a52+a56+a65) + a38 + a102

### Règles relatives aux mouvements des sûretés à des fins de rapprochement avec la partie B

Partie A : Sortie de sûretés applicables aux dérivés de gré à gré = Partie B : Programme des OHC – *Sellers Swap* -> Sûretés engagées + Total des dérivés de gré à gré -> Sûretés engagées (IF seulement)

* a57 + (-1)\*a16 = b22+b99+b107+b115+b123+b131+b139+b147+b155

Partie A : Sûretés engagées auprès d'une IMF/CC = Partie B : STPGV -> Sûretés engagées + Total des IMF -> Toutes les transactions-> Sûretés engagées (IMF seulement)

* a62 + (-1)\*a17= b1+b64+b69+b74+b77+b82+b85+b88+b89+b92
* a125 + (-1)\*a121=b158+b160+b165+b167+b172+b177+b179+b184+b186
* a126=b161+b168+b173+b180+b187
* a127+a128 + (-1)\*a122 + (-1)\*a123=b162+b163+b169+b170+b174+b175+b181+b182+b188+b189
* a129 + (-1)\*a124= b1+b159+b164+b166+b171+b176+b178+b183+b185+b190

Partie A : Sortie de sûretés applicables aux swaps =Partie B : Total des swaps de sûretés -> Sûretés engagées (y compris banques centrales et IF)

* a53 = b12+b25+b33+b42+b54+b97+b105+b113+b121+b129+b137+b145+b153

Partie A : Sûretés applicables aux cessions en pension (montant brut) = Partie B : Total des cessions en pension -> Sûretés engagées (y compris banques centrales et IF) + SCHL/FCH & Opérations de pension au bilan [Remarque& : Les sûretés applicables aux cessions en pension engagées auprès d'une CC sont prises en compte dans les sûretés engagées auprès d'une IMF/CC.]

* a47 = b6+b8+b23+b29+b31+b38+b50+b93+b101+b109+b117+b125+b133+b141+b149

Partie A : Sûretés applicables au prêt de titres (montant brut) = Partie B : Total des opérations de prêt de titres -> Sûretés engagées (y compris banques centrales et IF)

* a49 = b40+b52+b95+b103+b111+b119+b127+b135+b143+b151

Partie A : Sortie d'autres sûretés = Partie B : Total& Autres -> Sûretés engagées (y compris banques centrales et IF)

* a71+a69+a70 + (-1)\*a4 + (-1)\*a18 =b4+b14+b19+b20+b21+b27 +b35+b36+b44+b45+ b56+b57+b100+b108+b116+ b124+b132+b140 +b148+b156

Partie A : Entrée de sûretés applicables aux swaps = Partie B : Total des sûretés applicables aux swaps -> Sûretés reçues (y compris banques centrales et IF)

* a51+a52 = b13+b26+b34+b43+b55+b98+b106+b114+b122+b130+b138+b146+b154

### Règles relatives à la section sur le bilan à des fins de rapprochement avec la partie B

Partie A : Total des cessions en pension au bilan (montant brut) = Partie B : Total des cessions en pension -> Liquidités reçues (y compris IMF, banques centrales et IF)

* a21 = b7+b9+b24+b30+b32+b39+b51+b62+b67+b72+b75+b80+b83+b86+b90+b94+b102+b110+b118 +b126+b134+b142+b150
* a22= b62+b67+b72+b75+b80+b83+b86+b90
* a23= b7+b9+ b24+b30+b32+b39+b51+ b94+b102+b110+b118 +b126+b134+b142+b150

Partie A : Prêt de titres au bilan (montant brut) (total) = Partie B : Total des prêts de titres -> Liquidités reçues (y compris IMF, banques centrales et IF)

* a25 = b41+b53+b63+b68+b73+b76+b81+b84+b87+b91+b96+b104+b112+b120+b128+b136+ b144+b152
* a26= b63+b68+b73+b76+b81+b84+b87+b91
* a27=b41+b53+ b96+b104+b112+b120+b128+b136+b144+b152

## Principales règles de validation entre relevés

### Règles de validation à des fins de rapprochement avec le relevé M4 (Bilan) (précision à ± seuil de 2 %)

Partie A : Valeurs mobilières en position longue (ajustements& : y compris filiales non déclarées) = Valeurs& mobilières (relevé M4)

* Cell (a5, c52) = M4 0865 + M4 0866 + M4 0518 + M4 0520 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a5, c52) = Cell (a5, c53) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Prêts garantis (ajustements& : position nette, y compris filiales non déclarées) = Prises en pension (relevé M4)

* Cell (a6, c52) = M4 0666 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a6, c52) = Cell (a6, c53) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Prêts (ajustements& : y compris filiales non déclarées) = Prêts, déduction faite des prises en pension (relevé M4)

* Cell (a10, c52) = M4 2310 + M4 2057 + M4 0524 + M4 0526 + M4 2067 + M4 0534 +M4 0572 + M4 0540 + M4 0542 + M4 0608 + M4 2117 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a10, c52) = Cell (a10, c53) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Financement garanti (ajustements& : position nette, y compris filiales non déclarées) = Accords de rachat (relevé& M4)

* Cell (a20, c52) = M4 0634 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a20, c52) = Cell (a20, c53) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Valeurs mobilières en position courte (ajustements& : filiales et autres non déclarés) = Engagements afférents aux valeurs mobilières empruntées

* Cell (a28, c52) = M4 0632 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a28, c52) = Cell (a28, c53) [précision à ± seuil de 2 % en dernier jour du mois]

### Règles de validation à des fins de rapprochement avec le relevé du ratio de liquidité à court terme (LCR) (précision à ± seuil de 2 %)

Partie A : Actifs non grevés disponibles de niveau 1 = Valeur marchande des actifs de niveau 1 (relevé LCR)

* Cell (a73, c17) = LCR 11001 + LCR 11002 + LCR 11003 + LCR 11004 + LCR 11005 + LCR 11006 + LCR 11007 + LCR 11008 + LCR 11009 + LCR 11010 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a73, c17) = Cell (a72, c17) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Actifs non grevés disponibles de niveau 2A = Valeur marchande des actifs de niveau 2A (relevé LCR)

* Cell (a73, c25) = LCR 99004 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a73, c25) = Cell (a72, c25) [précision à ± seuil de 2 % en dernier jour du mois]

Partie A : Actifs non grevés disponibles de niveau 2B = Valeur marchande des actifs de niveau 2B (relevé LCR)

* Cell (a73, c30) = LCR 99009 + LCR 99012 [déclaration obligatoire à la fin du mois, mais les valeurs saisies sont reportées au jour ouvrable suivant]
* Cell (a73, c30) = Cell (a72, c30) [précision à ± seuil de 2 % en dernier jour du mois]

## Autre règles

a2=a3+a4  
a6=a7+a8  
a10=a11+a12+a13+a14  
a15=a16+a17+a18  
a16=a119+a120  
a17=a121+a122+a123+a124  
a20=a21+a25  
a21=a22+a23  
a25=a26+a27  
a29=a30+a31+a32  
a33=a34+a35+a36  
a37=a39+a51+a52+a55+a56+a61+a63  
a38=a46+a53+a57+a62+a66  
a39=a40+a41+a42+a44  
a46=a47+a49  
a50=a51+a52+a53  
a54=a55+a56+a57  
a57=a58+a59  
a60=a61+a62  
a62=a125+a126+a127+a128+a129  
a63=a64+a65  
a66=a67+a68+a69+a70+a71  
a72=a74+a93  
a74=a75+a76+a77+a78+a79+a80+a81+a82+a83+a84+a85+a86+a87+a88+a89+a90+a91+a92 [exception: ne s'appliquent pas à cells (a74, c17), (a74, c31)]  
a75=a3  
a76=a5  
a77=a10  
a78=a40+a42  
a79=a46  
a80=(-1)\*a28  
a81=a51  
a82=a53  
a83=a55  
a84=a57  
a85=a61  
a86=a62 [exception: ne s'appliquent pas à cell (a86, c46)]  
a87=a64 [exception: ne s'appliquent pas à cell (a87, c46)]  
a88=a67 [exception: ne s'appliquent pas à cell (a88, c46)]  
a89=a68  
a90=a70  
a91=a71 [exception: ne s'appliquent pas à cell (a91, c46)]  
a92=a102 [exception: ne s'appliquent pas à cell (a92, c46)]  
a93=a94+a95+a96+a97+a98+a99+a100+a101  
a94=a10  
a95=a67 [exception: ne s'appliquent pas à cell (a95, c46)]  
a96=a68  
a97=a69  
a98=a62 [exception: ne s'appliquent pas à cell (a98, c46)]  
a99=a64 [exception: ne s'appliquent pas à cell (a99, c46)]  
a100=a71 [exception: ne s'appliquent pas à cell (a100, c46)]  
a101=a102 [exception: ne s'appliquent pas à cell (a101, c46)]  
a102=a103+a104+a105

b16=b1+b4+b6+b8+b10+b12+b14  
b28=+b20+b21+b22+b23+b25+b27  
b47=b36+b38+b40+b42+b44+b45  
b59=b50+b52+b54+b56+b57  
b64=b158+b159  
b69=b160+b161+b162+b163+b164  
b74=b165+b166  
b77=b167+b168+b169+b170+b171  
b82=b172+b173+b174+b175+b176  
b85=b177+b178  
b88=b179+b180+b181+b182+b183  
b89=b184+b185  
b92=b186+b187+b188+b189+b190  
b157=b16+b19+b28+b29+b31+b33+b35+b47+b59+b64+b69+b74+b77+b82+b85+b88+b89+b92+b93+b95+ b97+b99+b100+b101+b103+b105+b107+b108+b109+b111+b113+b115+b116+b117+b119+b121+b123+b124 +b125+b127+b129+b131+b132+b133+b135+b137+b139+b140+b141+b143+b145+b147+b148+b149+b151+ b153+b155+b156

c5=c6+c9+c11  
c17=c2+c3+c4+c5+c16  
c18=c19+c20  
c25=c18+c22+c23+c24  
c30=c26+c27+c28+c29  
c31=c17+c25+c30  
c32=c33+c34+c35+c36+c39+c40  
c46=c32+c41+c42+c43+c44+c45  
c47=c1+c31+c46 [Exception: cette règle doit être remplacée par c47=c1+c2+c3+c4 pour (a75, c47), (b5, c47), (b7, c47), (b9, c47), (b15, c47), (b24, c47), (b30, c47), (b32, c47), (b37, c47), (b39, c47), (b41, c47), (b44, c47), (b46, c47), (b51, c47), (b53, c47), (b56, c47), (b58, c47), (b62, c47), (b63, c47), (b67, c47), (b68, c47), (b72, c47), (b73, c47), (b75, c47), (b76, c47), (b80, c47), (b81, c47), (b83, c47), (b84, c47), (b86, c47), (b87, c47), (b90, c47), (b91, c47), (b94, c47), (b96, c47), (b102, c47), (b104, c47), (b110, c47), (b112, c47), (b118, c47), (b120, c47), (b126, c47), (b128, c47), (b134, c47), (b136, c47), (b142, c47), (b144, c47), (b150, c47), (b152, c47)]  
c53=c47+c48+c49+c50+c51

a1 >=0  
a2 >=0  
a3 >=0  
a4 >=0  
a5 >=0  
a6 >=0  
a7 >=0  
a8 >=0  
a9 >=0  
a10 >=0  
a11 >=0  
a12 >=0  
a13 >=0  
a14 >=0  
a15 >=0  
a16 >=0  
a119 >=0  
a120 >=0  
a17 >=0  
a121 >=0  
a122 >=0  
a123 >=0  
a124 >=0  
a18 >=0  
a19 >=0  
a20 >=0  
a21 >=0  
a22 >=0  
a23 >=0  
a24 >=0  
a25 >=0  
a26 >=0  
a27 >=0  
a28 >=0  
a29 >=0  
a30 >=0  
a31 >=0  
a32 >=0  
a33 >=0  
a34 >=0  
a35 >=0  
a36 >=0  
a37 >=0  
a39 >=0  
a40 >=0  
a41 >=0  
a42 >=0  
a43 >=0  
a44 >=0  
a45 >=0  
a51 >=0  
a52 >=0  
a55 >=0  
a56 >=0  
a61 >=0  
a63 >=0  
a64 >=0  
a65 >=0

a38 <=0  
a46 <=0  
a47 <=0  
a48 <=0  
a49 <=0  
a53 <=0  
a57 <=0  
a58 <=0  
a59 <=0  
a62 <=0  
a125 <=0  
a126 <=0  
a127 <=0  
a128 <=0  
a129 <=0  
a66 <=0  
a67 <=0  
a68 <=0  
a69 <=0  
a70 <=0  
a71 <=0

Cell (b20, c10) = Cell (b20, c54)  
Cell (a10, c10) = Cell (a10, c54)  
Cell (a11, c10) = Cell (a11, c54)  
Cell (a12, c10) = Cell (a12, c54)  
Cell (a13, c10) = Cell (a13, c54)  
Cell (a14, c10) = Cell (a14, c54)  
Cell (b20, c9) = Cell (b20, c10)  
Cell (b49, c47) = (Cell (b48, c47) / Cell (b47, c47))\*100  
Cell (b61, c47) = (Cell (b60, c47) / Cell (b59, c47))\*100  
Cell (b66, c47) = (Cell (b65, c47) / Cell (b64, c47))\*100  
Cell (b71, c47) = (Cell (b70, c47) / Cell (b69, c47))\*100  
Cell (b79, c47) = (Cell (b78, c47) / Cell (b77, c47))\*100

Signaler un problème ou une erreur sur cette page

Date de modification :
:   2023-11-17