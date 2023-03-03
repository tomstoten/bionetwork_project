import cobra
from cobra.io import load_model

model = load_model("textbook")
print(model.metabolites)