
![Screenshot](images/logo-upc.jpg)

**Universidad Peruana de Ciencias Aplicadas**
=============================================

# CC42 – Complejidad Algorítmica – Trabajo Parcial 

# Profesor:
Luis Martin Canaval Sánchez 

# Integrantes

| Integrantes | Codigo | Usuario | Correo | 
|---|---|---|---|
| Jefferson Anthony Ortega Martel | u201920273 | JeffersonOrtega2018 | u201920273@upc.edu.pe |
| Marco Antonio Collantes Artola | u201410183 | Markollantes2307 | u201410183@upc.edu.pe |
| Luiggi Daniel Munaya Salcedo | u201617515 | lmsupc | U201617515@upc.edu.pe |


**2022 – 1**
============

# ÍNDICE
### 1. RESUMEN EJECUTIVO
### 2. OBJETIVOS 
### 3. IMAGEN ESTÁTICA DE LA CIUDAD O PORCIÓN DE CIUDAD ELEGIDA. 
### 4. DESCRIPCIÓN DE LOS DATOS CONSIGNADOS POR CALLE. 
### 5. DESCRIPCIÓN DE LA INFORMACIÓN CONSIGNADA POR INTERSECCIÓN. 
### 6. EXPLICACIÓN DE CÓMO SE ELABORÓ EL GRAFO, QUÉ REPRESENTAN LAS ARISTAS Y LOS VÉRTICES.
### 7. DESCRIPCIÓN DE LA CODIFICACIÓN DEL TRABAJO FINAL
### 8. CONCLUSIONES


# 1. RESUMEN EJECUTIVO 

##### El siguiente trabajo parcial consiste en elaborar un grafo para representar los distritos de San Borja, una porción de Surquillo y una porción de Santiago de Surco. Se debería seleccionar una sección equivalente a 500 intersecciones por estudiante, lo cual significa aproximadamente más o menos de 80 calles distribuidas. Obviamente ese sería el ideal de calle pero la ciudad de Lima no tiene proporciones cuadráticas exactas, así que se optó por escoger más calles.

# 2. OBJETIVOS

* Construir nuestro propio “waze”, es decir un sistema que nos permita encontrar la ruta más corta entre 2 puntos en una ciudad.
* Evidenciar el Outcome “Responsabilidad y ética profesional”.


# 3. IMAGEN ESTÁTICA DE LA CIUDAD O PORCIÓN DE CIUDAD ELEGIDA. 
##### En esta oportunidad se eligió de forma grupal abarcar el mapa del distrito de San Borja, empezando por su sector centro sur. Debido al tamaño de las cuadras y el número de intersecciones necesarias para el grafo, también se consideraron cuadras y calles pertenecientes a distritos aledaños como lo son Surco y Surquillo. 

![Screenshot](images/Imagen1.png)

![Screenshot](images/Imagen2.png)

![Screenshot](images/Imagen3.png)

![Screenshot](images/Imagen4.png)

# 4. DESCRIPCIÓN DE LOS DATOS CONSIGNADOS POR CALLE.
##### Con motivo de identificar las diferentes calles del distrito en el grafo, por no mencionar facilitar la creación del mismo, se procedió a numerarlas y considerarlas como calles de único sentido para así tener intersecciones más precisas y sin repetir. Las calles tomadas como muestra son:

* 01 San Borja Norte
* 02 De las artes norte
* 03 De las artes sur
* 04 Luini
* 05 Aviación
* 06 Matier
* 07 Miguel Angel
* 08 Lopez de Ayala
* 09 Johann Strauss
* 10 Pietro Marchand
* 11 Luigi Pirandelo
* 12 Crepi
* 13 Perugino
* 14 Gaddi
* 15 Duccio
* 16 Reynolds
* 17 Simoni
* 18 Monti
* 19 Donizetti
* 20 Jose Orozco
* 21 Fray Luis de León
* 22 San Borja Sur
* 23 Manuel de Falla
* 24 Ravel
* 25 Esquivel
* 26 Pisano
* 27 Renoir
* 28 Reni
* 29 Boccioni
* 30 Tintoretto
* 31 Leonardo Da Vinci
* 32 Degas
* 33 Benlliure
* 34 Berta Morisot
* 35 Derain
* 36 Vasari
* 37 Morelli
* 38 Ucello
* 39 Carpaccio
* 40 Holbein
* 41 Bernini
* 42 Regoyos
* 43 Carlo Crivelli
* 44 Sisley
* 45 Hals
* 46 Portinari
* 47 Moretti
* 48 Javier Prado Este
* 49 Guardia Civil
* 50 Jirón Tasso
* 51 Tiziano Vecellio
* 52 Giotto
* 53 Botticelli
* 54 Rafael
* 55 Donatello
* 56 Zurbaran
* 57 Tiepolo
* 58 Fray Angelico
* 59 Correggio
* 60 San Luis
* 61 Veronese
* 62 Rubens
* 63 Velasquez
* 64 Conti
* 65 Murillo
* 66 Bellini
* 67 Rivera
* 68 Goya
* 69 Picasso
* 70 Rembtandt
* 71 Andrea de Sarto
* 72 Jiron El Greco
* 73 Jean Jacques Rousseau
* 74 Breton
* 75 Dominguez
* 76 Toulouse Lautrec
* 77 José María Sert
* 78 Delacroix
* 79 Redon
* 80 Millet
* 81 Monet
* 82 Verrocchio
* 83 Cavallini
* 84 Van de Velde
* 85 Alonso del Arco
* 86 Joaquin Sorolla
* 87 Francisco de Ribalta
* 88 Bartolome Bermejo
* 89 Salvador Dalí
* 90 Hadraza
* 91 Anton van Dyck
* 92 Dore
* 93 Bronsino
* 94 Jr Los Sauces
* 95 Van Gogh
* 96 Pradilla
* 97 Jr Los Sauces
* 98 Rinaldo Lotta
* 99 Baron F de Gerard
* 100 Stephen Crane
* 101 Pisarro
* 102 Chardin
* 103 Gaugin
* 104 Poussin
* 105 Blvrd de Surco
* 106 Durero
* 107 Corot
* 108 Jean Louis Forain
* 109 Severini
* 110 Dupre
* 111 Benton
* 112 Carzou
* 113 Juan Gris
* 114 Mayer
* 115 Liszt
* 116 Preising
* 117 Bottger
* 118 Maurice Utrillo
* 119 Dante Gabriel Rosetti
* 120 Amadeo Mozart
* 121 Beethoven
* 122 Franz Schubert
* 123 Mauricio Casatti
* 124 Claude Monteverdi
* 125 Claude Debussy
* 126 Schipper
* 127 Johannes Brahms
* 128 Verdi
* 129 Wagner
* 130 Joaquin Valverde
* 131 Nicolo Paganini
* 132 Enrique Granados
* 133 Carla Schumann
* 134 Papini 
* 135 Rodin
* 136 Berruguette
* 137 Salzillo
* 138 Canova
* 139 Guardi
* 140 Españoleto
* 141 Eduardo Rosales
* 142 Fragonard
* 143 Parque Norte
* 144 Parque Sur
* 145 Pietro Torrigiano
* 146 Frederic Remington
* 147 Paul Dubois
* 148 Ossip Zadkin
* 149 José Galvez Barrenachea
* 150 Phillipp Von Leonard
* 151 Gozzoli Sur
* 152 Copernico
* 153 Gozzoli Norte
* 154 Leonhard Euler
* 155 Dalton
* 156 John Neper
* 157 Alexander Fleming
* 158 Ampere
* 159 Alberto Barajas
* 160 Gregorio Marañon
* 161 Evangelista Torricelli
* 162 Francesco Redi
* 163 Antonio Vivaldi
* 164 James Joule
* 165 Isaac Albeniz
* 166 Andreas Vesalio
* 167 Amadeo Avogadro
* 168 Sibelius
* 169 Pablo Casals
* 170 Maestro Arrieta
* 171 Saint Saenz
* 172 Leo Delibes
* 173 Argenta
* 174 Andres Segovia
* 175 Chueca
* 176 Joaquin Turina
* 177 Otto Muller
* 178 Moisés Mendelssohn
* 179 Pablo Usandizaga
* 180 Romero Hidalgo
* 181 Maestro Barbieri
* 182 Jacinto Guerrero
* 183 Joaquin de la Madrid
* 184 Geminis
* 185 Heinrich
* 186 Gluck
* 187 Chopin
* 188 Arredondo
* 189 Fedorovich Stravinski
* 190 Pockich
* 191 Pietro Mascagni
* 192 Ramon Cerdeira
* 193 Amadeo
* 194 Melissa
* 195 Paseo del Bosque
* 196 Venecia
* 197 Brescia
* 198 Turin
* 199 Pisa
* 200 Sicilia
* 201 Padua
* 202 Jr La Pradera
* 203 Del Piñar
* 204 Florencia
* 205 De la Floresta
* 206 Catania
* 207 Rigios
* 208 Treinta
* 209 Velasco Astete
* 210 Agustín de la Rosa Toro
* 211 Julio Baileti
* 212 Parraga
* 213 Enrique Pallardelli
* 214 Pezuela
* 215 Estremadoyro
* 216 Pinela
* 217 Jorge Aprile
* 218 Carlos Cobilich
* 219 Esteban Bentarelli
* 220 Jr Mercator
* 221 Eduardo Ordoñez
* 222 Ernesto Rutherford
* 223 Claudio Galeno
* 224 Joseph Thompson
* 225 Paul Linder
* 226 Arquitecto Fernando Echeandia
* 227 Luis Tapia Garcia
* 228 Oersted
* 229 Boralli
* 230 Bunsen 
* 231 A
* 232 Enrique Seoane
* 233 Manuel Piqueras
* 234 Benitez
* 235 Grana 
* 236 Prof Jorge Muelle
* 237 Marquina
* 238 Benjamín Doig
* 239 Alvarez Calderon
* 240 Vargas Prada
* 241 Malachowsky
* 242 Eduardo Orrego Villacorta
* 243 Urquiaga
* 244 Claude Sahut
* 245 Emilio Harth Terre
* 246 Angamos
* 247 Alfa
* 248 Omega
* 249 Geminis
* 250 Romero Hidalgo
* 251 Pietro Mascagni
* 252 Joachim Moser Hans
* 253 Toselli
* 254 Alejandro Scarlatti
* 255 Pablo Usandizaga
* 256 Tchaicovski
* 257 Gamma
* 258 Beta 
* 259 Delta
* 260 Epsilon
* 261 Sigma
* 262 Montero
* 263 Avenida Principal
* 264 Manuel Villaran 
* 265 Intihuatana
* 266 Garcia Robles
* 267 Manuel bonilla
* 268 Genaro Cobian
* 269 Gabriela Mistral
* 270 Octavio Paz
* 271 Alberto Einstein
* 272 Bernando Houssay
* 273 Roentgen
* 274 Juan Fuentes
* 275 Daniel Cruz
* 276 Alfa Centauro
* 277 Alfa Leon
* 278 La Pera 
* 279 El cerezo 
* 280 Berna 
* 281 Bruselas
* 282 Fermi
* 283 Jose Neyra 
* 284 Pascal
* 285 Descartes                                                                                 
* 286 Confucio
* 287 Harrington
* 288 Montesquieu
* 289 Manuel Alva
* 290 Crommer
* 291 Federico Engels
* 292 Alfa Orion
* 293 Fisher
* 294 Alfa Virgen
* 295 Alfa Lira
* 296 Alfa Boyero
* 297 Alfa Aguila
* 298 Alfa Cisne
* 299 Alfa Gemelos
* 300 Alfa Escorpion
* 301 Adam Smith
* 302 Ameghino
* 303 Alfa y Omega
* 304 Victor Hugo
* 305 Varsovia
* 306 Atenas
* 307 Dublin
* 308 Uva
* 309 Pacae 
* 310 Luxemburgo
* 311 Carlyle
* 312 Marco Polo
* 313 Paderewski
* 314 Emilio Zapata
* 315 Ortega y Gasset
* 316 Robinson
* 317 Hilman
* 318 Franklin
* 319 Murray
* 320 Calvino
* 321 Kandinsky
* 322 La Merced
* 323 Keller 
* 324 Clara Barton
* 325 Fray Angelico
* 326 Da Vinci
* 327 Vermer
* 328 Ghiberti
* 329 Sanzio
* 330 Hofman
* 331 Barbara DAchile
* 332 Modigliani
* 333 Rodin
* 334 Manet 
* 335 Sarto
* 336 Siqueiros
* 337 Girardout
* 338 Courbet
* 339 Holbein
* 340 Camilo Blas
* 341 Cassat
* 342 Car
* 343 Viena
* 344 Datilera
* 345 La Morera
* 346 Garrison
* 347 Green 
* 348 Russell
* 349 Spencer
* 350 Hegel
* 351 Diderot
* 352 William 
* 353 Teresa Carvallo
* 354 Marie Curie
* 355 Primavera
* 356 Panamericana Sur
* 357 Pedro Venturo 
* 358 Higuereta
* 359 Alfredo Benavides
* 360 Caminos del Inca
* 361  Punta Pejerrey
* 362  Tinajones
* 363  Antamina
* 364  Tampumachay
* 365  Marginal de la Selva
* 366  Jose Maria Quiroga
* 367  Zafra
* 368  Astorga
* 369  Aricota
* 370  Brea y Pariñas
* 371  Cañon del Pato 
* 372  La pampilla 
* 373  Marcona
* 374  Cadiz 
* 375  Barcelona
* 376  Aracena 
* 377  Condoroma 
* 378  El Rocio
* 379  Villa Carrillo
* 380  Malaga
* 381  Zamorra
* 382  Cosmos
* 383  Vilcabamba
* 384  Toquepala
* 385  La joya 
* 386  Pisac
* 387  Matarani
* 388  Canarias
* 389  Cuajone
* 390  Pontevedra
* 391  Majes
* 392  Taffur
* 393  Mendoza
* 394  Ocoña
* 395  Pinos del Valle 
* 396  Requena
* 397  Fortaleza de Paramonga
* 398  Granada
* 399  Aguada Blanca
* 400  Fe
* 401  Cordoba
* 402  Avila 
* 403  Segovia
* 404  Monte Bello
* 405  Monte Grande
* 406  del Pinar
* 407  Montepio
* 408  de la Floresta 
* 409  Alejandro Velasco Astete
* 410  Monte Claro
* 411  Del Sur
* 412  Monte de Oca
* 413  de los Precursores
* 414  Morro Solar 
* 415  Monterrey
* 416  Vea
* 417  Los Aviadores
* 418  Monte Lunar
* 419  Mariel
* 420  Monte Carmelo
* 421  Batallon Ayacucho
* 422  Batallon Libres de Trujillo
* 423  Batallon Callao
* 424  Batallon del Mar
* 425  Monserrate 
* 426  los Alguaciles
* 427  Sacramento
* 428  Montes de Oro
* 429  Coronel Reynaldo Vivanco
* 430  Monte Casino
* 431  Ramadal
* 432  Pamplona
* 433  Marcavilva
* 434  Monterrico Chico
* 435  Jose Manuel Quiroz 
* 436  Enrique Villanueva
* 437  La Chira
* 438  Batalla de San Juan
* 439  Tintoreros
* 440  Monte Rosa
* 441  Monte Azul
* 442  Monte Mayor
* 443  Monte Carlo
* 444  Monte Umbroso
* 445  La Niña
* 446  La Pinta  
* 447  Los Cabildos 
* 448  Monte Real 
* 449  Monte Blanco
* 450  Marqueses
* 451  Los Virreyes
* 452  Monte Flor
* 453  Montego Bay
* 454  Monte Frio
* 455  Batallon Tarma 
* 456  Monte Cristi
* 457  Manuel Ganoza
* 458  Conde De la Vega del Ren
* 459  Monte Sierpe
* 460  Montemar
* 461  Silvana
* 462  Monte Alegre
* 463  Trinitatarias
* 464  La Presa
* 465  Botoneros
* 466  Mercedarias
* 467  Franco Peruano
* 468  De Alcaldes
* 469  Nestor Batanero
* 470  Batallón Concepción
* 471  San Lucas 
* 472  Los Cabildos
* 473  Monte Melia
* 474  Av Canta Callao
* 475  Av Naranjal
* 476  Av Los Alisos
* 477  Av Carlos Izaquirre
* 478  Francisco Bolognesi
* 479  Mariano Usteriz y Rivero
* 480  Monte Negro
* 481  Monte Verde
* 482  Monte Azul
* 483  Monte Blanco
* 484  Av Las Malvas
* 485  Violetas
* 486  Av Próceres
* 487  Huaylas
* 488  Conray Grande
* 489  Huacllan
* 490  C. Hasta
* 491  Av Universitaria
* 492  Mallash
* 493  Ocros
* 494  Lipia
* 495  Ajia
* 496  Av Las Palmeras
* 497  Río Tarica
* 498  Marcara
* 499  José A. Quiñones
* 500  Av Oscar R.Benavides
* 501  Av C
* 502  C 11
* 503  C. Las Dalias
* 504  Gardenias
* 505  Las Lilas
* 506  Aquía
* 507  El Olivar
* 508  Virgin de Fatina
* 509  C Naranjal
* 510  13 de Mayo
* 511  Lenguaje
* 512  Federico Villareal
* 513  Av. Alfredo Mendiola
* 514  Av Perú
* 515  Av Santa Rosa
* 516  Av Jose Santos Chocano
* 517  Jose Carlos Mariategui
* 518  Av los diamantes
* 519  Jirón Sta Fe
* 520  La Comunión
* 521  Jr Las Margaritas
* 522  Jiron Rafael Alberti
* 523  Jirón Pablo Velarde
* 524  Jiron Ramon Herrera
* 525  Jirón Joaquín Tagle
* 526  Av Los Olivos
* 527  C. El Olivar  
* 528  C. Las Lomas
* 529  Los Lirios
* 530  Zircones
* 531  C Los Milagros
* 532  Los Claveles
* 533  Jirón Mariano Zarate
* 534  Chabuca Granda
* 535  Jade
* 536  Los Mármoles
* 537  Sta. Rosa
* 538  Av Rosario del Nte.
* 539  Agatas
* 540  C Las Esmeraldas
* 541  Las Galenas
* 542  C Los opalos
* 543  Las Palmeras
* 544  Los Zafiros
* 545  José M.Pereyra
* 546  Granate
* 547  Esmeraldas
* 548  Union
* 549  Jr Las Azucenas
* 550  Limocillos
* 551  El Amargon
* 552  Los Melones
* 553  C Granadillas
* 554  Los Pinos
* 555  Amarantos
* 556  Fresas 
* 557  Calistemo
* 558 Jiron Tritoma
* 559 Jr La Hidra
* 560 Azafran
* 561 Ca. Los Castaños
* 562 Diamantes
* 563 Ambar
* 564 Zafiro
* 565 Los Cafetales
* 566 Los Helenios
* 567 Jr Samanez Ocampo
* 568 Av Jose Santos Chocano
* 569 Barranca
* 570 Larco Herrera
* 571 Ignacio Merino 
* 572 Jr C. A. Salaverru
* 573 Jiron las Acurinas
* 574 Los Mirabeles
* 575 Los chirimoyas
* 576 Los tabacales 
* 577 Las Grandas
* 578 Los Musgos
* 579 Los Capulíes 
* 580 Jose Pereyra
* 581 Mesones
* 582 GodoFredo García
* 583 C los Claveles
* 584 Amarantos
* 585 San Barranca
* 586 Larco Herrera
* 587 Jr el Cuarzo
* 588 Jr Las Azucenas
* 589 El Manantial
* 590 Ca. Ramon Herrera
* 591 Calle 9
* 595 C. Los Frutales
* 596 Los Nogales de Oro
* 597 Av Sta Rosa
* 598 Jirón Pablo Verlaine
* 599 C.Pinos Oregon
* 600 C. Robles Blancos
* 601 av. Próceres
* 602 Piscobamba
* 603 Colcas
* 604 Av Marañon
* 605 Ganimedes 
* 606 Atenas
* 607 Avenida A
* 608 Av. Sta. Rosa
* 609 Av Central
* 610 Boreal
* 611 Jr Polonia
* 612 Jr Olimpo
* 613 Odeon
* 614 Av Holanda 
* 615 Av 2 de Octubre
* 616 Rio Ucayali
* 617 Rio Chicana
* 618 Marcara
* 619 Rio Chotano
* 620 Jr La Begonias
* 621 Los Gladiolos
* 622 Cipreses
* 623 Jiron Las Gardenias
* 624 Jiron Los Eucaliptos
* 625 C. Los Abedules

##### Como evidencia de que las calles existen, se adjunta una foto sacada de google maps donde se puede apreciar algunas de las calles que se extrajeron de una porción de distrito de Surquillo, en ellas se puede apreciar fácilmente a  la Av Aviacion (nro. 05), Juan Fuentes (nro. 274), Daniel Cruz (nro. 275), Alfa Cisne (nro. 298), Alfa Centauro (nro. 276), Alfa Orion (nro. 292), entre otros

![Screenshot](images/Imagen5.png)

# 5. DESCRIPCIÓN DE LA INFORMACIÓN CONSIGNADA POR INTERSECCIÓN. 
##### Para las intersecciones, se consideró que los cruces de nuestra área de estudio serían únicos tanto en sus componentes como en sus direcciones. De esa forma, independientemente si la calle se trata de una vía de doble sentido, un jirón o un pasaje, solo tendría una dirección a tener en cuenta a la hora de registrar las intersecciones en el grafo, pero a la vez puede tomarse una dirección diferente en un cruce diferente a uno presentado con anterioridad. Esto permitirá hacer un grafo más dinámico y con más direcciones de entrada y salida de elementos. 
##### En la siguiente imagen se puede observar la intersección entre Jr Eduardo Ordoñez y Claudio Galeno, que está representado como el nodo número 507.

![Screenshot](images/Imagen6.png)

# 6. EXPLICACIÓN DE CÓMO SE ELABORÓ EL GRAFO, QUÉ REPRESENTAN LAS ARISTAS Y LOS VÉRTICES.
##### Primero tuvimos que enumerar todas las calles que íbamos a usar en la elaboración del grafo. Luego tuvimos que contar las intersecciones que teníamos por calle hasta que cada estudiante llegara a un mínimo de 500 intersecciones, para así poder enumerarlas una por una como si fueran nodos. Finalmente, tuvimos que trabajarlo manualmente para poder convertir los datos de los nodos en una lista de adyacencia que permita un mejor tratamiento de los datos.
##### A continuación, se adjunta una visualización gráfica de nuestra lista de las primeras 500 intersecciones (los espacios en blanco representan 0 y los espacios en rojo representan 1):

![Screenshot](images/Imagen7.png)

##### Las aristas representan las calles tomadas de los distritos y las aristas son las intersecciones de las calles.

![Screenshot](images/Imagen8.png)

# 7. DESCRIPCIÓN DE LA CODIFICACIÓN DEL TRABAJO FINAL

##### Para el trabajo conjunto del equipo, se utilizó el uso de un repositorio público en GitHub.
##### Link del repositorio: https://github.com/JeffersonOrtega2018/TF-201410183-201617515-201920273 
![Screenshot](images/Imagen10.png)

##### Dentro de este repositorio, se añadieron todos los datos de las coordenadas de nuestras intersecciones.
![Screenshot](images/Imagen11.png)

##### Asimismo, se añadió la codificación correspondiente para la implementación de todo el trabajo final.

![Screenshot](images/Imagen12.png)
-
![Screenshot](images/Imagen13.png)
-
![Screenshot](images/Imagen14.png)
-
![Screenshot](images/Imagen15.png)

##### Adicionalmente, se usaron algoritmos para transformar los datos que teníamos en grafos y lista de adyacencia.
![Screenshot](images/Imagen16.png)

##### Como dato adicional, se muestra el código de implementación de interfaz que fue entregado por el docente.
![Screenshot](images/Imagen17.png)

# 8. CONCLUSIONES

##### 1. Gran parte de los conocimientos adquiridos dentro del curso fueron de vital importancia para el desarrollo del trabajo final, ya que todos estos se aplicaron satisfactoriamente.
##### 2. El razonamiento cuantitativo del curso se llevó a cabo exitosamente.
##### 3. Creemos que todas las competencias del curso de Complejidad Algorítmica fueron completadas a gran medida debido a que se puedo llevar a cabo todas las instancias del trabajo final.
##### 4. El trabajo final sirve como entrenamiento y preparación para el mundo laboral, ya que en un futuro podríamos implementar un software similar al trabajo final.
##### 5. Gracias a la realización del trabajo final, se aprendieron nuevas cosas que posiblemente no estaban dentro del curso como por ejemplo el manejo colaborativo de la herramienta GitHub.

##### Gracias :3


