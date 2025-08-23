


<p align="center">
    <img src="https://huggingface.co/datasets/modelcitizens/modelcitizens/resolve/main/paper.png" width="90%">
</p>

<p align="center">
      <img src = "https://img.shields.io/badge/Task-Toxicity--Detection-red">
      <img src = "https://img.shields.io/badge/Model-LLaMA/Gemma-green">
      <img src = "https://img.shields.io/badge/Data-Ingroup--Annotations-blue">
</p>

<div align="center">

[📜 Paper](https://arxiv.org/abs/2507.05455) • [🤗 Huggingface](https://huggingface.co/modelcitizens) • [🐦 Twitter]()

🎉🎉 ModelCitizens was accepted at EMNLP Main 2025!

</div>



## Evaluation 
Download the evaluation data from huggingface. 

```
python 
from datasets import load_dataset
ds = load_dataset("modelcitizens/modelcitizens", "eval")
```
Run `evaluation/eval_models.py` to get model responses and `evaluation/get_accuracy.py` to get the model accuracy score. 

## Train 
We use [LLAMAFACTORY](https://github.com/hiyouga/LLaMA-Factory) to finetune the CITIZEN models. 

```
bash
git clone https://github.com/hiyouga/LLaMA-Factory
```
Move the training configs from `train` folder to `LLaMA-Factory/examples/train_full`.

```
bash
mv modelcitizens/train/config_llama.yaml  LLaMA-Factory/examples/train_full
```
Download the training data from huggingface. 

```
python 
from datasets import load_dataset
ds = load_dataset("modelcitizens/modelcitizens", "train")
```
Add the train data entry in LLaMA-Factory/data/dataset_info.json with the correct local path to the train data. 


:bell: If you have any questions or suggestions, please don't hesitate to let us know. You can comment on [Twitter](https://x.com/suvarna_ashima), or post an issue on this repository.

## Related Work 
- [ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection](https://github.com/microsoft/ToxiGen)
- [Exploring Cross-Cultural Differences in English Hate Speech Annotations: From Dataset Construction to Analysis](https://github.com/nlee0212/CREHate)
- [When Do Annotator Demographics Matter? Measuring the Influence of Annotator Demographics with the POPQUORN Dataset](https://arxiv.org/abs/2306.06826)

## Acknowledgements
This work was supported by the UCLA Initiative to Study Hate and UCLA Racial and Social Justice Seed Grants program.

## Citation
If you find ModelCitizens useful, please consider citing us!

```
@misc{suvarna2025modelcitizensrepresentingcommunityvoicesonline,
      title={ModelCitizens:Representing Community Voices in Online Safety}, 
      author={Ashima Suvarna and Christina Chance and Karolina Naranjo and Hamid Palangi and Sophie Hao and Thomas Hartvigsen and Saadia Gabriel},
      year={2025},
      eprint={2507.05455},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.05455}, 
}
```
