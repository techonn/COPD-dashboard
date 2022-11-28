<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Cyan Dashboard</h3>

  <p align="center">
    An awesome Dashboard
    <br />
    <a href="https://github.com/eedrobup/cyan"><strong>Explore the codes »</strong></a>
    <br />
    <br />
    <a href="https://github.com/eedrobup/cyan">View Demo</a>
    ·
    <a href="https://github.com/eedrobup/cyan/issues">Report Bug</a>
    ·
    <a href="https://github.com/eedrobup/cyan/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#cyan-dashboard">Cyan Dashboard</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#Logic"></a></li>
        <li><a href="#data-used">Data Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#running-the-dashboard">Running the Dashboard</a></li>
        <li><a href="#testing-the-dashboard">Testing the Dashboard</a></li>
      </ul>
    </li>
    <li><a href="#scrum-team-details">Scrum Team Details</a></li>
    </li><a href="#License">License </a></a></li>
  </ol>
</details>

<!-- CYAN DASHBOARD -->

Cyan is a dashboard that shows insights regarding drug prescription. It serves to help members of the clinical commissioning group:

* Assess local needs
* Rank priorities and develop strategies to meet the public's medical needs
* Distribute the NHS budget given to their CCG a) Buying services on behalf of the population from providers including hospitals, clinics, community health bodies, etc
* Ensuring the services and pathways in which medicines are utilized are set to standards that provide cost-effective use of resources, reduced risks associated with medicines use, and improved patient outcomes

### Features

All the features displayed on the dashboard:

* Average actual cost
* Description of the max quantity item
* Percentage of the top prescribed drug among all the prescriptions
* Number of unique items in the data
* A bar chart depicting the total prescribed items per primary care trust(PCT)
* A table with a dropdown filtering the BNF data per PCT.
* A creatinine clearance calculator acting as a clinical support tool for physicians
* Details about the purpose of the dashboard
* Percentage of infection treatment drug out of all infection treatments 
* A search box that filters the drug by name or BNF code and displays it in the form of a table.
* A bar chart visualizing the total number of prescribed antibiotics for each GP practice in a selected PCT.

### Logic

* Creatinine clearance calculator considerations:- <br/>
  1) Cockcroft-Gault Formula- <br/>
     CrCl,mL/min = (140 - age)*(weight,kg)*(0.85 if female)/(72 * Cr, mg/dL) <br/>
  2) Age- 12 to 70 years. <br/>
  3) Body weight formula's-
  * Adjusted body weight (ABW), kg = IBW, kg + 0.4 × (actual body weight, kg – IBW, kg)
  * Ideal body weight (IBW), kg (male) = 50 + [ 2.3 × (height, inches – 60)]
  * IBW, kg (female) = 45.5 + [ 2.3 × (height, inches – 60)] <br/>
  4) Body weight ranges-
  * Body Mass Index (BMI) <18.5 - Underweight
  * BMI 18.5-24.9 - Normal weight
  * BMI >= 25 - Overweight/Obese

### Data Used
(click on the blue text to know more)

The data that drives the data dashboard is the practice level prescribing data provided by NHS Digital- [NHS Digital Practice level prescribing data: more information.](https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-data-more-information)

The BNF codes for the required classes of drugs:-<br/>
1) Antibacterial drugs - [Openprescribing.net.BNF 5.1: Antibacterial Drugs | OpenPrescribing.](https://openprescribing.net/bnf/0501/)<br/>
2) Antifungal drugs    - [Openprescribing.net.BNF 5.2: Antifungal drugs | OpenPrescribing.](https://openprescribing.net/bnf/0502/)<br/>
3) Antiviral drugs     - [Openprescribing.net.BNF 5.3: Antiviral drugs | OpenPrescribing.](https://openprescribing.net/bnf/0503/)<br/>
4) Antiprotozoal drugs - [Openprescribing.net.BNF 5.4: Antiprotozoal drugs | OpenPrescribing.](https://openprescribing.net/bnf/0504/)<br/>
5) Antihelmentic drugs - [Openprescribing.net.BNF 5.5: Anthelmintics | OpenPrescribing.](https://openprescribing.net/bnf/0505/)<br/>

The Glossary of terms  - [NHS Digital Practice level prescribing - glossary of terms.](https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-glossary-of-terms#bnf-code-structure)

Reference resource -
Creatinine calculator - <br/>
1) The formula - [Cockcroft, D.W. and Gault, H. (1976). Prediction of Creatinine Clearance from Serum Creatinine. Nephron, 16(1), pp.31–41.](https://doi.org/10.1159/000180580)<br/>
2) Age range - <br/> a. [Pierrat, A., Gravier, E., Saunders, C., Caira, M.-V., Aït-Djafer, Z., Legras, B. and Mallié, J.-P. (2003). Predicting GFR in children and adults: A comparison of the Cockcroft-Gault, Schwartz, and Modification of Diet in Renal Disease formulas. Kidney International, 64(4), pp.1425–1436.](https://doi.org/10.1046/j.1523-1755.2003.00208.x)<br/> 
                     b. [Willems, J.M., Vlasveld, T., den Elzen, W.P., Westendorp, R.G., Rabelink, T.J., de Craen, A.J. and Blauw, G.J. (2013). Performance of Cockcroft-Gault, MDRD, and CKD-EPI in estimating prevalence of renal function and predicting survival in the oldest old. BMC Geriatrics, 13(1).](https://doi.org/10.1186/1471-2318-13-113)<br/> 
                     
3) Body weight formula- [McCarron, M.M. and Devine, B.J. (1974). Clinical Pharmacy: Case Studies. Drug Intelligence & Clinical Pharmacy, 8(11), pp.650–655.](https://doi.org/10.1177/106002807400801104)<br/>
4) Body weight ranges - <br/>
  a. [Brown, D.L.,Masselink, A.J. and Lalla, C.D. (2013). Functional Range of Creatinine Clearance for Renal Drug Dosing: A Practical Solution to the Controversy of Which Weight to Use in the Cockcroft-Gault Equation. Annals of Pharmacotherapy, 47(7-8), pp.1039–1044. doi:10.1345/aph.1s176.](https://doi.org/10.1345/aph.1S176)<br/>
  b. [Winter, M.A.,Guhr, K.N. and Berg, G.M. (2012). Impact of Various Body Weights and Serum Creatinine Concentrations on the Bias and Accuracy of the Cockcroft-Gault Equation. Pharmacotherapy: The Journal of Human Pharmacology and Drug Therapy, 32(7), pp.604–612.]( https://doi.org/10.1002/j.1875-9114.2012.01098.x)<br/>
  
Additional resources - </br>
1) BNF Online-[MedicinesComplete Digital Medicines Information Suite.](https://www.medicinescomplete.com/#/)<br/>
2) Practice level prescribing dataset used in the dashboard -[NHS Digital Practice Level Prescribing December 2019.](https://digital.nhs.uk/data-and-information/publications/statistical/practice-level-prescribing-data/december-2019)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Instructions for setting up the dashbaord: <br/>
conda install flask <br />
conda install flask-sqlalchemy <br />
conda install nose2 <br />
conda install markdown <br />
conda install selenium <br />
download the [chrome-webdriver](https://chromedriver.chromium.org/downloads) <br />
git clone https://github.com/eedrobup/cyan.git <br />
cd cyan

### Running the Dashboard

Open terminal and run the following commands: <br />
cd cyan <br />
python run.py

### Testing the Dashboard

cd cyan <br />
nose2

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Scrum Team Details -->
## Scrum Team Details

- Alix Har [Linkedin](https://www.linkedin.com/in/alixhar)
- Franklin Rajadurai [Linkedin](https://www.linkedin.com/in/franklin-rajadurai-v-6249981bb)
- Halimah Fetuga [Linkedin](https://www.linkedin.com/in/halimah-fetuga-0b1123111)
- Tech Onn Ding [Linkedin](https://www.linkedin.com/in/techonnding/)
- Nishat Girkar [Linkedin](www.linkedin.com/in/dr-nishat-g-6b473580)
- Pubordee Aussavavirojekul [Linkedin](https://www.linkedin.com/in/pubordee-aussavavirojekul-5bb0b611a)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- License -->
## License 
The cyan dashboard is free and open source software licensed under MIT.<br/>
It is subject to only the condition that the copyright notice and the permission notice be included in all the copies and
other portions of the software.

[MIT](https://github.com/eedrobup/cyan/blob/master/LICENSE) <br/>
<strong> Copyright(c) cyan <strong>