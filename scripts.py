######################################This file was used to format the LLM outputs when it was not the desired form and merging them######################################

#########################################Fix when label: is in answer##################################
import json
import re

with open("mistral_results_fixed.json", "r") as f:
    results = json.load(f)

mismatches = []

# Check each entry
for idx, entry in enumerate(results, start=1):
    justification = entry.get("justification", "")
    expected = entry.get("generated_label", "").strip().lower()

    # Check for syntax then fix
    match = re.search(r"Label:\s*(True|False|Conflicting)", justification, re.IGNORECASE)
    if not match:
        continue

    extracted = match.group(1).strip().lower()

    if extracted != expected:
        mismatches.append({
            "index": idx,
            "claim": entry["claim"],
            "generated_label": entry["generated_label"],
            "extracted_label": match.group(1),
            "justification": justification
        })
######################################### Count Mismatches between what i extracted and what the LLM actually outputed #########################################




# import json
# import re
#
#
# with open("llama2_results_fixed_final.json", "r") as f:
#     data = json.load(f)
#
# mismatches = []
#
# for idx, entry in enumerate(data):
#     justification = entry.get("justification", "")
#     current_label = entry.get("generated_label", "")
#
#     # skip if fixed by program above
#     if re.search(r"Label:\s*(True|False|Conflicting)", justification, re.IGNORECASE):
#         continue
#
#     # Check for a capitalized label(all LLMs outputed this)
#     match = re.search(r"\b(True|False|Conflicting)\b", justification)
#     if match:
#         extracted_label = match.group(1)
#         if extracted_label != current_label:
#             mismatches.append({
#                 "index": idx,
#                 "claim": entry.get("claim", ""),
#                 "generated_label": current_label,
#                 "extracted_label": extracted_label
#             })
#
# print(f" Found {len(mismatches)} mismatches (excluding 'Label:' cases).")


######################################### Fix the mismatches from above ########################################


# import json
# import re
#
#
# with open("phi_results_fixed.json", "r") as f:
#     data = json.load(f)
#
# fixed_count = 0
#
# for entry in data:
#     justification = entry.get("justification", "")
#     current_label = entry.get("generated_label", "")
#
#     if re.search(r"Label:\s*(True|False|Conflicting)", justification, re.IGNORECASE):
#         continue
#     # fix the mismatches from above
#     match = re.search(r"\b(True|False|Conflicting)\b", justification)
#     if match:
#         extracted_label = match.group(1)
#         if extracted_label != current_label:
#             entry["generated_label"] = extracted_label
#             fixed_count += 1
#
# # Save results
# with open("phi_results_fixed_clean.json", "w") as f:
#     json.dump(data, f, indent=2)
#
# print("Saved updated file as phi_results_fixed_clean.json")


#########################################Merging the 4 justifications for evaluation#########################################


# import json
#
# with open("Labelling(run1)/llama2_results_fixed_final.json", "r") as f:
#     llama2_data = json.load(f)
#
# with open("Labelling(run1)/gemma_results_fixed.json", "r") as f:
#     gemma_data = json.load(f)
#
# with open("Labelling(run1)/mistral_results_fixed.json", "r") as f:
#     mistral_data = json.load(f)
#
# with open("Labelling(run1)/phi_results_fixed_final.json", "r") as f:
#     phi_data = json.load(f)
#
# # Build index by claim for each model
# def build_index(data):
#     return {entry["claim"]: entry for entry in data}
#
# # get the data
# llama2_index = build_index(llama2_data)
# gemma_index = build_index(gemma_data)
# mistral_index = build_index(mistral_data)
# phi_index = build_index(phi_data)
#
# merged_results = []
#
# #take any model as primary I chose llama
# for claim, entry in llama2_index.items():
#     if claim in gemma_index and claim in mistral_index and claim in phi_index:
#         merged_results.append({
#             "claim": claim,
#             "taxonomy_label": entry.get("taxonomy_label", "unknown"),
#             "llama2_justification": entry.get("justification", ""),
#             "gemma_justification": gemma_index[claim].get("justification", ""),
#             "mistral_justification": mistral_index[claim].get("justification", ""),
#             "phi_justification": phi_index[claim].get("justification", "")
#         })
#
# # Save results
# with open("merged_justifications_(no_label_given).json", "w") as f:
#     json.dump(merged_results, f, indent=2)
#
# print(" Saved to merged_justifications.json")