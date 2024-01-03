# ThermoreceptorModel

## Overview
ThermoreceptorModel is a comprehensive Python package designed to simulate the thermal response of skin receptors. 
This model accounts for various heat transfer processes, including conduction, convection, radiation, and the distribution of radiation within skin layers. 
It's tailored for researchers and engineers working in biophysical modeling, thermal physiology, and related fields.

The model is based on [de Dear's model](https://doi.org/10.1111/j.1600-0668.1993.t01-1-00004.x) 
and consider [spectral data of the skin](https://doi.org/10.1007/BF00502381) to allow user to simulate thermal perception affected by radiation of
different wavelengths.

Detail equations can be found here ([link](https://doi.org/10.1016/j.indenv.2023.100003)).

## Features
- Simulation of skin receptors' response to varying thermal environments.
- Incorporation of conduction, convection, and radiation heat transfer processes.
- Detailed modeling of radiation distribution within skin layers.
- Customizable simulation phases with different environmental conditions.

# Requirement
* [python3](https://www.python.org/downloads/)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)


## Installation
```bash
!git clone https://github.com/AkihisaNomoto/thermoreceptormodel.git
```

## Example
The following two codes are identical as the codes in the "examples" folder.

### Example 1
This code simulates thermoreceptor response resulting from a sudden ambient temperature change.

```python
from thermoreceptormodel import model

# --------------------------------------
# Example 1 (Environmental step-change)
# --------------------------------------
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
```

### Example 2
This code simulates thermoreceptor response when the skin is irradiated by visible rays.

```python
import pandas as pd
import configuration
from thermoreceptormodel import model

# --------------------------------------
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
# --------------------------------------
# Define spectral irradiance
example_spectrum_path = configuration.EXAMPLE_SPECTRUM
df_example_spectrum = pd.read_csv(example_spectrum_path)
df_example_spectrum.index = df_example_spectrum["wavelength_nm"]  # The index should be wavelength
spectrum_visible = df_example_spectrum["normalized_visible_radiation_W/m2nm"]

# Create instance
model_instance = model.ThermoreceptorModel()

# Set parameters (you can use some parameters using setter method (ex. XXX.Y))
model_instance.T_core = 34
model_instance.hr = 5
model_instance.T_r = 25
model_instance.q_spectrum = spectrum_visible

# Set environmental parameters using add_phase method
model_instance.add_phase(duration_in_sec=60 * 10, t_db=25, t_r=25, q_irradiance=0)
model_instance.add_phase(duration_in_sec=20, t_db=25, t_r=25, q_irradiance=800)  # 20 sec irradiation

# Define simulation results
df_simulation_results = model_instance.simulate(show_input=True)

# Output as a csv file
df_simulation_results.to_csv("example_simulation_2.csv")
```

## Inputs
### Setter methods
- `length`: thickness of skin layer in m.
- `n`: number of skin nodes.
- `dt`: time step for the simulation.
- `T_core`: core body temperaturoe in °C.
- `q_spectrum`: spectral irradiance in W/m²/µm
- `hc`: convection heat transfer coefficient in W/m²/K.
- `hr`: radiation heat transfer coefficient in W/m²/K.
### add_phase method
- `duration_in_sec`: Duration of each simulation phase in seconds.
- `t_db`: Dry bulb (ambient) temperature in °C.
- `t_r`: Radiant temperature in °C.
- `q_irradiance`: Total irradiance in W/m².

## Outputs
The `simulate` method returns a pandas DataFrame containing:
- Temperature for each skin layer.
- Impulse frequency from warm receptor.
- Environmental conditions for each phase if `show_input` is set to True.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Contact
Akihisa Nomoto (monyo323232@gmail.com; nomoto@berkeley.edu)

## License
This model is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
