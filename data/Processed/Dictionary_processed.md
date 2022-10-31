<h1>Diccionario de datos</h1>

<p>Insurance Company Benchmark (COIL 2000) Practice<br />
<strong>Aprendizaje Autom&aacute;tico</strong><br />
<strong>Master Universitario en Ciencia de Datos</strong></p>

<p>&nbsp;</p>

<p style="text-align:right">V&iacute;ctor Viloria V&aacute;zquez (<em>victor.viloria@cunef.edu</em>)</p>

---

Este documento pretende aportar información descriptiva del contenido y forma del dataset utilizado en la primera práctica de la asignatura de Machine Learning, la cual consiste en la elaboración del EDA del dataset **Insurance Company Benchmark**.

Este dataset incorpora informacion relativa a diferentes clientes de una aseguradora, exactamente un número de **86 variables**, **agrupadas** en dos grupos:
- **Datos sociodemográficos derivados del código postal**.
- **Datos acerca de la titulariad de pólizas sobre diferentes bienes**.

En este diccionario nos disponemos a describir cada una de las variables que posee el dataset, su
significado, posibles valores que puede tomar y otros aspectos técnicos relevantes para el
manejo y que permitan la elaboración de modelos.


## Sociodemographic Data (Derived from zipcodes)


| **Field Name** 	| **Description** 	| **Variable Type** 	| **Data Type** 	| **Value** 	|
|:---:	|:---:	|:---:	|:---:	|:---	|
| MOSTYPE 	| Customer Subtype 	| Categorical 	| _int64_ 	| 1: High Income, expensive child<br>2: Very Important Provincials                                           <br>3: High status seniors<br>4: Affluent senior apartments<br>5: Mixed seniors<br>6: Career and childcare<br>7: Dinki's (double income no kids)<br>8: Middle class families<br>9: Modern, complete families<br>11: Family starters<br>12: Affluent young families<br>13: Young all american family<br>14: Junior cosmopolitan<br>15: Senior cosmopolitans<br>16: Students in apartments<br>17: Fresh masters in the city<br>18: Single youth<br>19: Suburban youth<br>20: Etnically diverse<br>21: Young urban have-nots<br>22: Mixed apartment dwellers<br>23: Young and rising<br>24: Young, low educated <br>25: Young seniors in the city<br>26: Own home elderly<br>27: Seniors in apartments<br>28: Residential elderly<br>29: Porchless seniors: no front yard<br>30: Religious elderly singles<br>31: Low income catholics<br>32: Mixed seniors<br>33: Lower class large families<br>34: Large family, employed child<br>35: Village families<br>36: Couples with teens 'Married with children'<br>37: Mixed small town dwellers<br>38: Traditional families<br>39: Large religous families<br>40: Large family farms<br>41: Mixed rurals 	|
| MAANTHUI 	| Number of houses 	| Discrete 	| _int64_ 	| Values between [1 – 10] 	|
| MGEMOMV 	| Avg size household 	| Discrete 	| _int64_ 	| Values between [1 – 6] 	|
| MGEMLEEF 	| Avg age 	| Categorical 	| _int64_ 	| 1: 20-30 years<br>2: 30-40 years<br>3: 40-50 years<br>4: 50-60 years<br>5: 60-70 years<br>6: 70-80 years 	|
| MOSHOOFD 	| Customer main type 	| Categorical 	| _int64_ 	| 1: Successful hedonists<br>2: Driven Growers<br>3: Average Family<br>4: Career Loners<br>5: Living well<br>6: Cruising Seniors<br>7: Retired and Religeous<br>8: Family with grown ups<br>9: Conservative families<br>10: Farmers 	|
| MGODRK 	| Roman catholic 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MGODPR 	| Protestant 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MGODOV 	| Other religion 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MGODGE 	| No religion 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MRELGE 	| Married 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MRELSA 	| Living together 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MRELOV 	| Other relation 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MFALLEEN 	| Singles 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MFGEKIND 	| Household without children 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MFWEKIND 	| Household with children 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MOPLHOOG 	| High level education 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MOPLMIDD 	| Medium level education 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MOPLLAAG 	| Lower level education 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERHOOG 	| High status 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERZELF 	| Entrepreneur 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERBOER 	| Farmer 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERMIDD 	| Middle management 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERARBG 	| Skilled labourers 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MBERARBO 	| Unskilled labourers 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MSKA 	| Social class A 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MSKB1 	| Social class B1 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MSKB2 	| Social class B2 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MSKC 	| Social class C 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MSKD 	| Social class D 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MHHUUR 	| Rented house 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MHKOOP 	| Home owners 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MAUT1 	| 1 car 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MAUT2 	| 2 cars 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MAUT0 	| No car 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MZFONDS 	| National Health Service 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MZPART 	| Private health insurance 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINKM30 	| Income < 30.000 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINK3045 	| Income 30-45.000 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINK4575 	| Income 45-75.000 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINK7512 	| Income 75-122.000 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINK123M 	| Income >123.000 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MINKGEM 	| Average income 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| MKOOPKLA 	| Purchasing power class 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|

## Product Ownership

| **Field Name** 	| **Description** 	| **Variable Type** 	| **Data Type** 	| **Range** 	|
|:---:	|:---:		|:---:	|:---:		|:---	|
| PWAPART 	| Contribution private third party insurance 	| Categorical 	| _int64_ 	| 0: 0%<br>1: 1 - 10%<br>2: 11 - 23%<br>3: 24 - 36%<br>4: 37 - 49%<br>5: 50 - 62%<br>6: 63 - 75%<br>7: 76 - 88%<br>8: 89 - 99%<br>9: 100% 	|
| PWABEDR 	| Contribution third party insurance (firms) 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PWALAND 	| Contribution third party insurane (agriculture) 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PPERSAUT 	| Contribution car policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PBESAUT 	| Contribution delivery van policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PMOTSCO 	| Contribution motorcycle/scooter policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PVRAAUT 	| Contribution lorry policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PAANHANG 	| Contribution trailer policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PTRACTOR 	| Contribution tractor policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PWERKT 	| Contribution agricultural machines policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PBROM 	| Contribution moped policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PLEVEN 	| Contribution life insurances 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PPERSONG 	| Contribution private accident insurance policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PGEZONG 	| Contribution family accidents insurance policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PWAOREG 	| Contribution disability insurance policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PBRAND 	| Contribution fire policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PZEILPL 	| Contribution surfboard policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PPLEZIER 	| Contribution boat policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PFIETS 	| Contribution bicycle policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PINBOED 	| Contribution property insurance policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| PBYSTAND 	| Contribution social security insurance policies 	| Categorical 	| _int64_ 	| 0: f 0<br>1: f 1 – 49<br>2: f 50 – 99<br>3: f 100 – 199<br>4: f 200 – 499<br>5: f 500 – 999<br>6: f 1000 – 4999<br>7: f 5000 – 9999<br>8: f 10.000 - 19.999<br>9: f 20.000 - ? 	|
| AWAPART 	| Number of private third party insurance 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AWABEDR 	| Number of third party insurance (firms) 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AWALAND 	| Number of third party insurane (agriculture) 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| APERSAUT 	| Number of car policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ABESAUT 	| Number of delivery van policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AMOTSCO 	| Number of motorcycle/scooter policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AVRAAUT 	| Number of lorry policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AAANHANG 	| Number of trailer policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ATRACTOR 	| Number of tractor policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AWERKT 	| Number of agricultural machines policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ABROM 	| Number of moped policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ALEVEN 	| Number of life insurances 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| APERSONG 	| Number of private accident insurance policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AGEZONG 	| Number of family accidents insurance policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AWAOREG 	| Number of disability insurance policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ABRAND 	| Number of fire policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AZEILPL 	| Number of surfboard policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| APLEZIER 	| Number of boat policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AFIETS 	| Number of bicycle policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| AINBOED 	| Number of property insurance policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| ABYSTAND 	| Number of social security insurance policies 	| Discrete 	| _int64_ 	| Values between [1-12] 	|
| **CARAVAN** 	| **TARGET : Number of mobile home policies** 	| **Categorical** 	|**int64** 	| **0: Won't accquire the home policy<br> 1: Will accquire the home policy** 	|
