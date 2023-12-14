import os

PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

MODEL_DIRECTRY = os.path.join(PROJECT_DIRECTORY, "src/thermoreceptormodel")
SKIN_OPTICAL_PROPERTIES = os.path.join(MODEL_DIRECTRY , "skin-spectral-properties.csv")

EXAMPLE_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "examples")
EXAMPLE_SPECTRUM = os.path.join(EXAMPLE_DIRECTORY, "example_normalized_spectral_irradiance.csv")
