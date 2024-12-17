**ANALYSIS OF LAND SUBSIDENCE BASED ON EXPERIMENTAL DATA OF A SIMULATED UNCONFINED AQUIFER**

> Analyzing the experimental results of land subsidence experiments in sands. The experiment consisted on simulating an unconfined sandy aquifer subjected to cycles of recharge and exploitation, and measuring the vertical displacement with three vertical linear transducers. 

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#Usage)
5. [Results](#Results)
6. [License](#license)

    ---

## Overview

The experimental setup is shown in Figure 1. It consists of a rectangular tank with
2.70 m (length) × 1.25 m (height) × 0.10 m (width) divided into three compartments
(3, 7, 10) a central compartment containing the porous media (2.50 m long) and two lateral
compartments (0.10 m long) for observing the water level. A fine screen mesh (4, 9) with
holes of 0.074 mm (also known as mesh No. 200) separates the lateral compartments from
the central compartment, preventing sand from flowing from the central into the side ones.
The sand was silica sand, specifically quarzitic sand with 94.7% silica content. Fine and
coarse sand with effective diameters of 0.39 mm and 0.67 mm, respectively, were used.
There are also two side chambers (2, 11) that control the water level. These chambers
are connected to the tank through pipes and transparent flexible tubes. The tank is made of
transparent Plexiglas with a thickness of 15 mm and is supported by a reinforced steel frame.
Steel tension pins were also added to strengthen the tank and prevent side deformation.
Three vertical displacement transducers were located at the top of the central compartment
separated 1.25 m from each other (8). The displacement transducers (LVDT) were the
Model Humbolt type HM-2310.04 range 0.4′′ (10 mm) with a precision of 0.001 mm. Two
side reservoirs (1, 14) with their respective pumps (5, 13) were included to store freshwater
and supply the lateral chambers, the left tank with a volume of 250 L and the right tank
with a volume of 500 L.

![image](https://github.com/user-attachments/assets/e5c27e03-a8e8-4845-b7bf-83096a34410a). fIGURE 1. Experimental setup for land subsidence experiments. 1. Left-side reservoir, 2. Left-side chamber for water level control, 3. Left-side compartment, 4. Lateral mesh, 5. Inlet pump, 6. Ball valve, 7. Central compartment with porous media, 8. Vertical displacement transducers, 9. Lateral mesh, 10. Right-side compartment, 11. Right-side chamber for water level, 12. Ball valve, 13. Inlet
pump, and 14. Right-side reservoir

The first step was to pack the sand simultaneously with the water on the lateral
compartments. To guarantee the uniformity of the grain size and avoid the formation of air
spaces and undesired strata, a packing technique was applied. It consisted of filling 10 cm
of water prior to adding 10 cm of sand, this process was repeated until the amount of soil
reached 1.10 cm. This process was applied for both coarse and fine sand.
The subsidence process was measured every 24-h using both analog and digital
longitudinal vertical displacement transducers (LVDT) type HM-2310.04 Modelo Humbolt
range 0.4′′ (10 mm) and a precision of 0.001 mm. The exploitation was simulated by
lowering the water level from 1.1 to 0.8 m in chambers (2) and (11), and the recharge was
simulated by increasing the water level from 0.8 to 1.1 m. To initiate the exploitation cycles
(lowering and increasing the water level), the hydraulic head was set to its initial height
of 1.1 m. The surface level of the sand was registered at the beginning of the experiment,
and it was considered the reference level to measure the vertical displacement of the sand.
Hereafter, the hydraulic head was lowered to 0.8 m and this level was maintained for 24 h.
The subsequent exploitation cycle began 24 h after the previous one, lowering the water
table by 30 cm. A total of four scenarios of exploitations, recharge, and stabilization cycles
were conducted, including two for fine sand and two scenarios for coarse sand. The selected
drawdown was considered based on the evidenced depletion of unconfined aquifers
subjected to overexploitation. Among the considered drawdowns are a 50% drawdown
of the Lower Bengal Delta (Yu et. al. 2019), a 43% drawdown of the Aguascalientes Valley, 42% at the
Wuxi city aquifer, and an average drawdown of 27.66% of the total depth of the Arroyo
Grande Aquifer, an unconfined sandy aquifer in Cartagena, Colombia. Therefore, for this
study, the considered drawdown was 30 cm, also equivalent to a 27% drawdown of the
experimental setup.

## Features

> After the experiments were developed, a numerical model was designed to explore
the capabilities of CFD platforms to recreate subsidence experimental results in sands. 

> Both the experimental data and simulated data were analyzed using error measurements and statistical analysis. 

After you collect the experimental data and have the results from the CFD simulations, you can use my project to analyze and compare the results of the three sensors and the numerical simulations. It will help you identify if there is a close agreement between experiments and numerical model.

This project offers:
- **User-Friendly Interface**:  
  Intuitive design allows users to interact with the application easily.

- **Fast and Accurate**:  
  Processes data quickly with minimal resource consumption, ensuring precise results.

- **Customizable Configurations**:  
  Users can modify parameters (e.g., input file formats, simulation settings) to suit their specific use case.

- **Supports Multiple Data Formats**:  
  Accepts input in CSV, and XML formats.

- **Visualizations**:  
  Automatically generates graphs and charts to help users interpret the results.
  
## Installation

Follow these steps to set up the project in your pc:

### 1. Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package installer)
- **Git**
- **Matplotlib**, **NumPy**, and **Pandas** (for graphing and data analysis)

### 2. Clone the repository 

git clone https://github.com/dayanachaladiaz/land_subsidence_graphs.git

cd land_subsidence_graphs

## Usage
### 1. Organize your data

- Experimental Data: experimental_data.csv
- Simulated Data: simulated_data.csv

### 2. Run the script
Scripts: Figure1.py (Visualization of the experimental and visualization data)

## Results
![image](https://github.com/user-attachments/assets/de25bb89-9db9-4d73-b15c-76bd5db313aa) Figure 2. Vertical displacement in the coarse sand for the first experimental scenario.

- The average absolute error of the numerical model to recreate the experimental results
of land subsidence was 0.14 mm for the first scenario of coarse sand, 0.34 mm for
the second scenario of coarse sand, 0.33 mm first the first scenario of fine sand, and
0.29 mm for the second scenario of fine sand. The maximum discrepancy of 0.34 mm
was obtained for the second scenario of coarse sand where the maximum experimental
subsidence was 3.86 mm.

- During the continued cycles of recharge and exploitation, both sands showed continued compaction that kept increasing over time. However, the deformation of coarse sand occurred at higher rates than for the fine sand. At times when the hydraulic head was maintained constant, the deformation for the coarse sand was significantly
reduced, and for fine sands, it evidenced a delayed response.

## License
Copyright (c) 2024 Dayana Chala

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE


