import cobra
from cobra.io import load_model
from reconstructor import reconstruct

input_file = 'data/protein.faa'
model = reconstruct(input_file, file_type=1, gram='negative', cpu=2)
print(model)