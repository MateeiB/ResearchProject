######################################Only 1 element evaluation(used to test)######################################
# import json
# from langchain_ollama import OllamaLLM
#
#
# llm = OllamaLLM(model="gemma")  # Change model if needed
#
# # load justifications here
# with open("merged_justifications_label.json", "r") as f:
#     merged_data = json.load(f)
#
# # Take only the first entry
# entry = merged_data[0]
#
# claim = entry["claim"]
# taxonomy = entry["taxonomy_label"]
#
# PROMPT_TEMPLATE = """
# You are a fact-checking assistant tasked with comparing explanations from multiple language models for the same claim and evidence. You are required to think in steps.
#
# Claim: "{claim}"
# Claim Type: {taxonomy_label}
#
# Justification from LLaMA2:
# {llama2}
#
# Justification from Gemma:
# {gemma}
#
# Justification from Mistral:
# {mistral}
#
# Justification from Phi:
# {phi}
#
# Write a short comparative analysis of the justifications above, explaining which model(s) provided the most convincing and faithful explanation, and why.
# """.strip()
#
# prompt = PROMPT_TEMPLATE.format(
#     claim=claim,
#     taxonomy_label=taxonomy,
#     llama2=entry["llama2_justification"],
#     gemma=entry["gemma_justification"],
#     mistral=entry["mistral_justification"],
#     phi=entry["phi_justification"]
# )
#
# try:
#     analysis = llm.invoke(prompt).strip()
# except Exception as e:
#     analysis = f"ERROR: {e}"
#
#
# with open("comparative_gemma_test2.json", "w") as f:
#     json.dump([{
#         "claim": claim,
#         "taxonomy_label": taxonomy,
#         "analysis": analysis
#     }], f, indent=2)
# #warning
# print("Test analysis saved to comparative_gemma_test2.json")
######################################Quantemp evaluation######################################
# import json
# from langchain_ollama import OllamaLLM
#
# # choose LLM
# llm = OllamaLLM(model="gemma")
#
# # load justifications here
# with open("Comp_analysis/merged_justifications_(no_label_given).json", "r") as f:
#     merged_data = json.load(f)
#
# results = []
#
# # Prompt template(names can be changed)
# PROMPT_TEMPLATE = """
# You are a fact-checking assistant tasked with comparing explanations from multiple language models for the same claim and evidence. You are required to think in steps.
#
# Claim: "{claim}"
# Claim Type: {taxonomy_label}
#
# Justification from LLaMA2:
# {llama2}
#
# Justification from Gemma:
# {gemma}
#
# Justification from Mistral:
# {mistral}
#
# Justification from Phi:
# {phi}
#
# Write a short comparative analysis of the justifications above, explaining which model(s) provided the most convincing and faithful explanation, and why.
# """.strip()
#
# # Process each entry
# for entry in merged_data:
#     claim = entry["claim"]
#     taxonomy = entry["taxonomy_label"]
#
#     prompt = PROMPT_TEMPLATE.format(
#         claim=claim,
#         taxonomy_label=taxonomy,
#         llama2=entry["llama2_justification"],
#         gemma=entry["gemma_justification"],
#         mistral=entry["mistral_justification"],
#         phi=entry["phi_justification"]
#     )
#
#     try:
#         analysis = llm.invoke(prompt).strip()
#     except Exception as e:
#         analysis = f"ERROR: {e}"
#
#     results.append({
#         "claim": claim,
#         "taxonomy_label": taxonomy,
#         "analysis": analysis
#     })
#
# with open("Comp_analysis/comparative_gemma_(no_label_given).json", "w") as f:
#     json.dump(results, f, indent=2)
# #warning
# print(f"Analyses saved to comparative_gemma_(no_label_given).json")
######################################Hover evaluation######################################
# import json
# from langchain_ollama import OllamaLLM
#
#
# llm = OllamaLLM(model="llama2")
#
# #load justifications here
# with open("hover_phi_gemma_justifications_(label_given).json", "r") as f:
#     merged_data = json.load(f)
#
# results = []
#
# # Prompt template(names can be changed)
# PROMPT_TEMPLATE = """
# You are a fact-checking assistant tasked with comparing explanations from two language models for the same claim and evidence. You are required to think in steps.
#
# Claim: "{claim}"
# Number of Hops: {num_hops}
#
# Justification from Phi:
# {phi}
#
# Justification from Gemma:
# {gemma}
#
# Write a short comparative analysis of the justifications above, explaining which model provided the most convincing and faithful explanation, and why.
# """.strip()
#
# # Process each entry
# for entry in merged_data:
#     claim = entry["claim"]
#     num_hops = entry.get("num_hops")
#
#     prompt = PROMPT_TEMPLATE.format(
#         claim=claim,
#         num_hops=num_hops,
#         gemma=entry["gemma_justification"],
#         phi=entry["phi_justification"]
#     )
#
#     try:
#         analysis = llm.invoke(prompt).strip()
#     except Exception as e:
#         analysis = f"ERROR: {e}"
#
#     results.append({
#         "claim": claim,
#         "num_hops": num_hops,
#         "analysis": analysis
#     })
#
# with open("hover_llama2_analysis_(label_given).json", "w") as f:
#     json.dump(results, f, indent=2)
# #warning
# print("Analyses saved to hover_llama2_analysis_(label_given).json")
