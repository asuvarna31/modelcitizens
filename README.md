# ModelCitizens: Representing Community Voices in Online Safety

![Hate Speech Detection](https://img.shields.io/badge/Task-Hate--Speech--Detection-red) 
![Models](https://img.shields.io/badge/Model-LLaMA/Gemma-green) 
![comm](https://img.shields.io/badge/Data-Ingroup--Annotations-blue) 

<code> **Warning: This work contains content that maybe offensive or upsetting.** </code>


[[Paper](https://arxiv.org/abs/2507.05455)] [[🤗 Huggingface](https://huggingface.co/modelcitizens)] [[Twitter]()]


## Evaluation 

## Train 
We use [LLAMAFACTORY](https://github.com/hiyouga/LLaMA-Factory) to finetune the CITIZEN models. 

```
bash
git clone https://github.com/hiyouga/LLaMA-Factory

Move the training configs from `train` folder to `LLaMA-Factory/examples/train_full`.

```
bash
mv modelcitizens/train/config_llama.yaml  LLaMA-Factory/examples/train_full

Download the training data from huggingface. 

```
Python 
from datasets import load_dataset
ds = load_dataset("modelcitizens/modelcitizens")

Add the train data entry in LLaMA-Factory/data/dataset_info.json with the correct local path to the train data. 






 Code for the Paper "[ModelCitizens: Representing Community Voices in Online Safety](https://arxiv.org/abs/2507.0545)".

:bell: If you have any questions or suggestions, please don't hesitate to let us know. You can comment on [Twitter](https://x.com/suvarna_ashima), or post an issue on this repository.

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
