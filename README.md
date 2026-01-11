# structured-output
Structured output from large language models (LLMs) has enhanced efficiency in processing generated information and is increasingly adopted in industrial applications. Prior studies have investigated the impact of structured output on LLMs' generation quality, often presenting one-way findings. Some suggest that structured format enhances completeness and factual accuracy, while others argue that it restricts the reasoning capacity of LLMs and leads to reductions in standard evaluation metrics. Potential limitations of these assessments include restricted testing scenarios, weakly controlled comparative settings, and reliance on coarse metrics. In this work, we present a refined analysis using causal inference. Based on one assumed and two guaranteed constraints, we derive five potential causal structures characterizing the influence of structured output on LLMs' generation: (1) collider without m-bias, (2) collider with m-bias, (3) single cause from instruction, (4) single cause from output format, and (5) independence. Across seven public and one developed reasoning tasks, we find that coarse metrics report positive, negative, or neutral effects of structured output on GPT-4o's generation. However, causal inference reveals no causal impact in 43 out of 48 scenarios. In the remaining 5, 3 involve multifaceted causal structures influenced by concrete instructions. Further experiments show that OpenAI-o3 are more resilient to output formats than general-purpose GPT-4o and GPT-4.1, highlighting an unaware advantage of reasoning models.
### Please read our [article](https://arxiv.org/abs/2509.21791) for further information.
`gsm8k` folder records the causal discovery process of Grade School Math 8K.
- `gsm8k_json.ipynb`, `gsm8k_xml.ipynb`, and `gsm8k_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.
- `gsm8k_json_additional_intervention`, `gsm8k_xml_additional_intervention`, `gsm8k_yaml_additional_intervention`, corresponds to the causal discovery process of JSON, XML, and YAML under additional intervention of instructions, respectively.
- `llama_gsm8k_json.ipynb`, `llama_gsm8k_xml.ipynb`, `llama_gsm8k_yaml.ipynb`, corresponds to the causal discovery process of JSON, XML, and YAML, respectively.
- `gemma_gsm8k_json.ipynb`, `gemma_gsm8k_xml.ipynb`, `gemma_gsm8k_yaml.ipynb`, corresponds to the causal discovery process of JSON, XML, and YAML, respectively.
- `phi_gsm8k_json.ipynb`, `phi_gsm8k_xml.ipynb`, `phi_gsm8k_yaml.ipynb`, corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`llc` folder records the results of Last Letter Concatenation.
- `llc_json.ipynb`, `llc_xml.ipynb`, and `llc_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`ellc` folder records the causal discovery process of Enhanced Last Letter Concatenation.
- `ellc_json.ipynb`, `ellc_xml.ipynb`, and `ellc_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`sot` folder records the causal discovery process of Shuffled Objects Tracking.
- `sot_json.ipynb`, `sot_xml.ipynb`, and `sot_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`gcf` folder records the causal discovery process of German Credit Factuality.
- `gcf_json.ipynb`, `gcf_xml.ipynb`, and `gcf_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.
- `gcf_json_1.ipynb` and `gcf_json_2.ipynb` corresponds to the additional first and second API calls in the causal discovery process of JSON, respectively.
- `gcf_xml_1.ipynb` and `gcf_xml_2.ipynb` corresponds to the additional first and second API calls in the causal discovery process of XML, respectively.
- `gcf_yaml_1.ipynb` and `gcf_yaml_2.ipynb` corresponds to the additional first and second API calls in the causal discovery process of YAML, respectively.

`gcc` folder records the causal discovery process of German Credit Causality.
- `gcc_json.ipynb`, `gcc_xml.ipynb`, and `gcc_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`opseval` folder records the causal discovery process of Operations-oriented Evaluation.
- `opseval_json.ipynb`, `opseval_xml.ipynb`, and `opseval_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.
- `mobile_communication_network_reasoning.json` records the problems requiring reasoning in opseval dataset. 

`xcodeeval` folder records the causal discovery process of Execution-based Code Evaluation.
- `code_json.ipynb`, `code_xml.ipynb`, and `code_yaml.ipynb` corresponds to the causal discovery process of JSON, XML, and YAML, respectively.

`ellc_dataset` folder contains four datasets and benchmark results related to the ELLC task.

- `ellc_4_words.json` and `ellc_6_words.json` refer to last letter concatenation of 4 and 6 words, respectively.
- `emlc_4_words.json` and `emlc_6_words.json` stand for middle letter concatenation of 4 and 6 words, respectively.
- `ellc_benchmark.ipynb` records the code and results of benchmark study on ELLC.

Structured outputs above is generated by format-restricting instruction and function calling-based JSON generation is presented in the following files in each folder.
- `gsm8k_json_function_call.ipynb`, `llc_json_function_call.ipynb`, `ellc_json_function_call.ipynb`, `sot_json_function_call.ipynb`, `gcf_json_function_call.ipynb`, `gcc_json_function_call.ipynb`, `opseval_json_function_call.ipynb`, `code_json_function_call.ipynb`

## BibTeX Citation

If you use our findings in a scientific publication, we would appreciate using the following citations:

```
@inproceedings{yuan-etal-structured-output,
    title = "Quantifying the Impact of Structured Output Format on Large Language Models through Causal Inference",
    author = "Yuan, Han  and
      Zhao, Yue  and
      Zhang, Li  and
      Luo, Wuqiong  and
      Ma, Zheng",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2026",
    year = "2026",
    publisher = "Association for Computational Linguistics",
}

@misc{yuan2025quantifyingimpactstructuredoutput,
      title={Quantifying the Impact of Structured Output Format on Large Language Models through Causal Inference}, 
      author={Han Yuan and Yue Zhao and Li Zhang and Wuqiong Luo and Zheng Ma},
      year={2025},
      eprint={2509.21791},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.21791}, 
}
```
