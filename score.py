######################################File to create the scoring dataset(adding the evidence)######################################
import json
with open("Datasets/hover_train_filtered_50_with_evidence.json", "r") as f1:
    filtered_evidence = json.load(f1)

with open("hoverAnalysys/hover_llama2_mistral_justifications_(no_label_given).json", "r") as f2:
    gemma_results = json.load(f2)

# match on claim
claim_to_doc = {entry["claim"]: entry["evidence"] for entry in filtered_evidence}

# Merge
for entry in gemma_results:
    claim = entry["claim"]
    if claim in claim_to_doc:
        entry["evidence"] = claim_to_doc[claim]
    else:
        entry["evidence"] = None

# output
with open("scores/1_hover_llama2_mistral_doc.json", "w") as outfile:
    json.dump(gemma_results, outfile, indent=2)
