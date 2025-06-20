######################################File used to import the Evidence for the HoVer Dataset######################################
import json
from datasets import load_dataset

# My file with the filtered data
with open("ignored(bad_old_data)/hover_train_filtered_200.json", "r") as f:
    filtered_claims = json.load(f)

# Take the coresponding entries from the web
print("Downloading first 1000 entries from Dzeniks/hover dataset...")
hover_subset = load_dataset("Dzeniks/hover", split="train").select(range(1000))
print(f"Subset loaded with {len(hover_subset)} entries.")

# Map based on claim
claim_to_evidence = {
    example["claim"]: example.get("evidence", "") for example in hover_subset
}

# Merge the evidence
missing_count = 0
for entry in filtered_claims:
    claim_text = entry["claim"]
    matched_evidence = claim_to_evidence.get(claim_text, "")
    entry["evidence"] = matched_evidence
    if not matched_evidence:
        missing_count += 1

# Save results
output_file = "Datasets/hover_train_filtered_50_with_evidence.json"
with open(output_file, "w") as f:
    json.dump(filtered_claims, f, indent=2)

# warning
if missing_count > 0:
    print(f"Warning: {missing_count} claims had no matching evidence in the subset.")
