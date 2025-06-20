##############################################for all entries generate label for correctness#######################################################
import json
import re
from langchain_ollama import OllamaLLM

# choose LLM
llm = OllamaLLM(model="gemma")

# Load input hover/quantemp
with open("Datasets/hover_train_filtered_50_with_evidence.json", "r") as f:
    data = json.load(f)

results = []

# if you swap dataset change the label names in the prompt(again this is the last used, which is for hover)
PROMPT_TEMPLATE = """
You are given a factual claim and an evidence passage. Based solely on the evidence, determine whether the claim is SUPPORTED or NOT_SUPPORTED by the evidence.

Your output must include just one thing in the following syntax:
1. Justification: Explain your reasoning based only on the evidence.
2. Label: One of [SUPPORTED, NOT_SUPPORTED]

Claim: "{claim}"

Evidence:
\"\"\"{evidence}\"\"\"

Answer:
"""
# done later so i dont have to run all the parts from the scripts file
def extract_label(text):
    """Extracts the label from the response text after 'Label:'"""
    match = re.search(r"label\s*:\s*(SUPPORTED|NOT_SUPPORTED)", text, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return "UNKNOWN"

# Process all entries
for entry in data:
    claim = entry["claim"]
    evidence = entry.get("evidence", "")
    original_label = entry.get("label", "UNKNOWN")
    num_hops = entry.get("num_hops", None)

    prompt = PROMPT_TEMPLATE.format(claim=claim, evidence=evidence)

    try:
        response = llm.invoke(prompt).strip()
    except Exception as e:
        response = f"ERROR: {e}"

    generated_label = extract_label(response)

    results.append({
        "claim": claim,
        "original_label": original_label,
        "generated_label": generated_label,
        "num_hops": num_hops,
        "justification": response
    })


with open("hoverAnalysys/hover_gemma_justifications_final.json", "w") as f:
    json.dump(results, f, indent=2)

print("Justifications and labels saved to hover_gemma_justifications_final.json")


########################## For one entry to test the program ###########################
# import json
# from langchain_ollama import OllamaLLM
#
# # choose LLM
# llm = OllamaLLM(model="mistral")
#
# with open("filtered_evidence_test.json", "r") as f:
#     data = json.load(f)
#
# # Find the first entry where "found_ruling": true (this was from the filtering done by a teammate)
# target_entry = next((entry for entry in data if entry.get("found_ruling") is True), None)
#
# results = []
#
# if target_entry:
#     claim = target_entry["claim"]
#     doc = target_entry["doc"]
#     correct_label = target_entry.get("label", "Unknown")
#     taxonomy_label = target_entry.get("taxonomy_label", "unknown")
#
#     prompt = f"""
# Given the following claim, its correct label, and the supporting article text (evidence), generate a justification that explains why the label is appropriate.
#
# Claim: "{claim}"
#
# Label: {correct_label}
#
# Evidence:
# \"\"\"{doc}\"\"\"
#
# Your task is to write a justification for this label, based only on the evidence provided.
# """.strip()
#
#     try:
#         justification = llm.invoke(prompt).strip()
#     except Exception as e:
#         justification = f"ERROR: {e}"
#
#     results.append({
#         "claim": claim,
#         "taxonomy_label": taxonomy_label,
#         "original_label": correct_label,
#         "justification": justification
#     })
#
#     with open("mistral_justification_only1.json", "w") as f:
#         json.dump(results, f, indent=2)
#
#     print("Justification saved to mistral_justification_only1.json")
# else:
#     # Problem with the found_rulling field
#     print(" No entries found with 'found_ruling': true.")



##############################################try with 1 entry for hover#######################################################
# import json
# import re
# from langchain_ollama import OllamaLLM
#
# #choose LLM
# llm = OllamaLLM(model="mistral")
#
# # Load input from hover
# with open("hover_train_filtered_50_with_evidence.json", "r") as f:
#     data = json.load(f)
#
# # Only take the first entry
# first_entry = data[0]
# results = []
#
# PROMPT_TEMPLATE = """
# You are given a factual claim and an evidence passage. Based solely on the evidence, determine whether the claim is SUPPORTED or NOT_SUPPORTED by the evidence.
#
# Your output must include:
# 1. Justification: Explain your reasoning based only on the evidence.
# 2. Label: One of [SUPPORTED, NOT_SUPPORTED]
#
# Claim: "{claim}"
#
# Evidence:
# \"\"\"{evidence}\"\"\"
#
# Answer:
# """
#
# def extract_label(text):
#     """Extracts label following the pattern 'Label: <value>'."""
#     match = re.search(r"label\s*:\s*(SUPPORTED|NOT_SUPPORTED)", text, re.IGNORECASE)
#     if match:
#         return match.group(1).upper()
#     return "UNKNOWN"
#
# claim = first_entry["claim"]
# evidence = first_entry.get("evidence", "")
# original_label = first_entry.get("label", "UNKNOWN")
#
# prompt = PROMPT_TEMPLATE.format(claim=claim, evidence=evidence)
#
# try:
#     response = llm.invoke(prompt).strip()
# except Exception as e:
#     response = f"ERROR: {e}"
#
# generated_label = extract_label(response)
#
# results.append({
#     "claim": claim,
#     "original_label": original_label,
#     "generated_label": generated_label,
#     "justification": response
# })
#
# # Save result
# with open("hover_mistral_justifications_first_entry.json", "w") as f:
#     json.dump(results, f, indent=2)
#
# print("Justification for first entry saved to hover_mistral_justifications_first_entry.json")


##############################################for all entries run2 with the label given#######################################################

# import json
# from langchain_ollama import OllamaLLM
#
# # choose LLM
# llm = OllamaLLM(model="gemma")
#
# # Load your dataset (hover here as it was used lastly)
# with open("hover_train_filtered_50_with_evidence.json", "r") as f:
#     data = json.load(f)
#
# results = []
#
# # Prompt template: asks LLM to justify the correct label(can be used without modifications for both datasets)
# PROMPT_TEMPLATE = """
# You are given a factual claim, its correct label, and an evidence passage.
# Your task is to explain why the label is appropriate based only on the evidence.
#
# Claim: "{claim}"
#
# Label: {label}
#
# Evidence:
# \"\"\"{evidence}\"\"\"
#
# Justification:
# """
#
# # Process all entries
# for entry in data:
#     claim = entry["claim"]
#     evidence = entry.get("evidence", "")
#     original_label = entry.get("label", "UNKNOWN")
#     num_hops = entry.get("num_hops", None)
#
#     prompt = PROMPT_TEMPLATE.format(claim=claim, label=original_label, evidence=evidence)
#
#     try:
#         justification = llm.invoke(prompt).strip()
#     except Exception as e:
#         justification = f"ERROR: {e}"
#
#     results.append({
#         "claim": claim,
#         "original_label": original_label,
#         "num_hops": num_hops,
#         "justification": justification
#     })
#
# # Save the results
# with open("hover_gemma_justifications_label_final.json", "w") as f:
#     json.dump(results, f, indent=2)
#
# print("Justifications with labels and num_hops saved to hover_gemma_justifications_label_final.json")
