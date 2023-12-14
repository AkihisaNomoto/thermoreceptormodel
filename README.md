# Thermoreceptor model

This model simulates thermoreceotor responces in the skin.
The model is based on de Dear's model (https://doi.org/10.1111/j.1600-0668.1993.t01-1-00004.x) 
and consider the spectral data of the skin to allow user to simulate thermal perception affected by radiation of
different wavelengths.

# Requirement
* python3
* numpy

# Documentation
Detail equations can be found here (link)

# Installation

```bash
!git clone https://github.com/AkihisaNomoto/thermoreceptormodel.git
```

# Example
```python
import pandas as pd
import configuration
from src.thermoreceptormodel import model

#--------------------------------------
# Example 1 (Environmental step-change)
#--------------------------------------
# Create instance
model_instance = model.ThermoreceptorModel()

# Set parameters (you can use some parameters using setter method (ex. XXX.Y))
model_instance.T_core = 34
model_instance.hr = 5

# Set environmental parameters using add_phase method
model_instance.add_phase(duration_in_sec=60, t_db=25, t_r=25, q_irradiance=0)
model_instance.add_phase(duration_in_sec=60, t_db=30, t_r=30, q_irradiance=0)

# Define simulation results
df_simulation_results = model_instance.simulate(show_input=False)

# Output as a csv file
df_simulation_results.to_csv("example_simulation_1.csv")

#--------------------------------------
# Example 2 (Spectral irradiation)
#
# Note: Data for radiation spectrum should be pandas dataframe including wavelength as columns
# Example data
# wavelength_nm
# 300     0.000000
# 310     0.000342
# 320     0.002414
# 330     0.008306
# 340     0.012904
#           ...
# 2460    0.000000
# 2470    0.000000
# 2480    0.000000
# 2490    0.000000
# 2500    0.000000
# Name: normalized_visible_radiation_W/m2nm, Length: 221, dtype: float64
#--------------------------------------
# Define spectral irradiance
example_spectrum_path = configuration.EXAMPLE_SPECTRUM
df_example_spectrum = pd.read_csv(example_spectrum_path)
df_example_spectrum.index = df_example_spectrum["wavelength_nm"] # The index should be wavelength
spectrum_visible = df_example_spectrum["normalized_visible_radiation_W/m2nm"]

# Create instance
model_instance = model.ThermoreceptorModel()

# Set parameters (you can use some parameters using setter method (ex. XXX.Y))
model_instance.T_core = 34
model_instance.hr = 5
model_instance.T_r = 25
model_instance.q_spectrum = spectrum_visible

# Set environmental parameters using add_phase method
model_instance.add_phase(duration_in_sec=60*10, t_db=25, t_r=25, q_irradiance=0)
model_instance.add_phase(duration_in_sec=20, t_db=25, t_r=25, q_irradiance=800) # 20 sec irradiation

# Define simulation results
df_simulation_results = model_instance.simulate(show_input=True)

# Output as a csv file
df_simulation_results.to_csv("example_simulation_2.csv")
```

# Contact
Akihisa Nomoto (monyo323232@gmailcom; nomoto@berkeley.edu)

# License
This model is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
