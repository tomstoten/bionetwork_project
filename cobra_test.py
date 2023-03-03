import cobra
from cobra.io import load_model
from reconstructor import reconstruct

input_file = 'data/GCF_001645765.1_ASM164576v1_genomic.fna'
model = reconstruct(input_file, file_type=1)
print(model)