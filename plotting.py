######################################Plot Quantemp corectness scores######################################
# import json
# import matplotlib.pyplot as plt
# from collections import defaultdict
#
# # Get data(change path if you need to)
# model_files = {
#     "llama2": "Labelling(run1)/llama2_results_with_labels_final.json",
#     "gemma": "Labelling(run1)/gemma_results_with_labels2.json",
#     "phi": "Labelling(run1)/phi_results_with_labels_final.json",
#     "mistral": "Labelling(run1)/mistral_results_with_labels_final.json"
# }
#
# # Define labels and colors
# label_types = ["True", "False", "Conflicting"]
# colors = {"True": "green", "False": "red", "Conflicting": "yellow"}
#
# # Store data per model
# per_label_accuracy = defaultdict(dict)
#
# for model, path in model_files.items():
#     try:
#         with open(path, "r") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         print(f"File not found for model: {model}")
#         continue
#
#     # Group entries by original_label
#     grouped = defaultdict(list)
#     for entry in data:
#         orig = entry.get("original_label")
#         pred = entry.get("generated_label")
#         if orig and pred and orig in label_types:
#             grouped[orig].append((orig.strip().lower(), pred.strip().lower()))
#
#     for label in label_types:
#         entries = grouped[label]
#         if not entries:
#             acc = 0.0
#         else:
#             correct = sum(1 for orig, pred in entries if orig == pred)
#             acc = correct / len(entries) * 100
#         per_label_accuracy[model][label] = acc
#
#
# models = list(per_label_accuracy.keys())
# x = range(len(models))
# bar_width = 0.2
#
# fig, ax = plt.subplots(figsize=(5.5, 3.5))
#
# # Draw 3 bars per model
# for i, label in enumerate(label_types):
#     acc_values = [per_label_accuracy[model][label] for model in models]
#     ax.bar(
#         [pos + i * bar_width for pos in x],
#         acc_values,
#         width=bar_width,
#         label=label,
#         color=colors[label]
#     )
#
# ax.set_xlabel("Model")
# ax.set_ylabel("Accuracy (%)")
# ax.set_title("Model correctness")
# ax.set_xticks([pos + bar_width for pos in x])
# ax.set_xticklabels(models)
# ax.set_ylim(0, 100)
# ax.legend(title="Label Type", loc="upper right", fontsize=7, title_fontsize=7)
# ax.grid(axis="y", linestyle="--", alpha=0.5)
#
# plt.tight_layout()
# plt.savefig("quantemp_correct_final.png")
# plt.show()


######################################Plot hover corectness scores######################################

# import json
# import matplotlib.pyplot as plt
# from collections import defaultdict
#
# # Get data(change path if you need to)
# model_files = {
#     "llama2": "hover(run)/hover_llama2_justifications_final.json",
#     "mistral": "hover(run)/hover_mistral_justifications_final.json",
#     "gemma": "hover_gemma_justifications_final.json",
#     "phi": "hover_phi_justifications_final.json"
# }
#
# # Define labels and colors
# label_types = ["SUPPORTED", "NOT_SUPPORTED"]
# colors = {"SUPPORTED": "green", "NOT_SUPPORTED": "red"}
#
# # Store data per model
# per_label_accuracy = defaultdict(dict)
#
# for model, path in model_files.items():
#     try:
#         with open(path, "r") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         print(f"File not found for model: {model}")
#         continue
#
#     # Group entries by original_label
#     grouped = defaultdict(list)
#     for entry in data:
#         orig = entry.get("original_label", "").strip().upper()
#         pred = entry.get("generated_label", "").strip().upper()
#         if orig and pred and orig in label_types:
#             grouped[orig].append((orig, pred))
#
#     for label in label_types:
#         entries = grouped[label]
#         if not entries:
#             acc = 0.0
#         else:
#             correct = sum(1 for orig, pred in entries if orig == pred)
#             acc = correct / len(entries) * 100
#         per_label_accuracy[model][label] = acc
#
# models = list(per_label_accuracy.keys())
# x = range(len(models))
# bar_width = 0.2  # Tighter bar spacing
#
# fig, ax = plt.subplots(figsize=(5.5, 3.5))  # Slightly wider for 4 models
#
# # Draw 2 bars per model
# for i, label in enumerate(label_types):
#     acc_values = [per_label_accuracy[model][label] for model in models]
#     positions = [pos + (i - 0.5) * bar_width for pos in x]  # Center bars
#     ax.bar(
#         positions,
#         acc_values,
#         width=bar_width,
#         label=label,
#         color=colors[label]
#     )
#
# ax.set_xlabel("Model", fontsize=12)
# ax.set_ylabel("Accuracy (%)", fontsize=12)
# ax.set_title("Model Accuracy by Label (HOVER)", fontsize=14)
# ax.set_xticks(list(x))
# ax.set_xticklabels(models, fontsize=11)
# ax.set_ylim(0, 100)
# ax.legend(title="Label", loc="upper right", fontsize=8, title_fontsize=8)
# ax.tick_params(axis='y', labelsize=8)
# ax.grid(axis="y", linestyle="--", alpha=0.5)
#
# plt.tight_layout()
# plt.savefig("hover_correct_all.png", dpi=300)
# plt.show()

######################################Plot Quantemp faithfulness scores######################################
import matplotlib.pyplot as plt
import numpy as np

models = ["LLaMA2", "Mistral", "Phi", "Gemma"]
run1_scores = [3.420, 3.258, 3.041, 2.717]
run2_scores = [4.34, 4.26, 4.19, 4.41]

x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, run1_scores, width, label='Run 1', color='red')
plt.bar(x + width/2, run2_scores, width, label='Run 2', color='green')

plt.xlabel('Model')
plt.ylabel('Score')
plt.title('QuanTemp Faithfulness Scores')
plt.xticks(x, models)
plt.legend(loc='upper left')
plt.grid(axis='y')

plt.tight_layout()
plt.savefig("faithfulness_quantemp.png", dpi=300)
plt.show()


######################################Plot hover faithfulness scores######################################
# import matplotlib.pyplot as plt
#
#
# models = ["Mistral", "LLaMA2", "Gemma", "Phi"]
# scores = [2.492, 2.454, 2.258, 2.256]
#
#
# plt.figure(figsize=(6, 4))
# bars = plt.bar(models, scores, color='red')
#
# plt.xlabel("Model")
# plt.ylabel("Score")
# plt.title("Hover Faithfulness Scores")
# plt.ylim(0, 4)
#
# #highlight the values on top of the bars
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{height:.3f}",
#              ha='center', va='bottom', fontsize=9)
#
# plt.tight_layout()
# plt.savefig("faithfulness_hover.png", dpi=300)
# plt.show()
