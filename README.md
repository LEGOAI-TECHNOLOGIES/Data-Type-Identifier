<p align="center">
      <img src="documentation/logo_white.jpg" alt="LegoAI Logo" width="350">
 <h3 align="center"><i>Empowering Data Teams with utilities to build Data Products</i></h3>
</p>

[![Release](https://img.shields.io/github/release/LEGOAI-TECHNOLOGIES/legoai_community_accelerator)](https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator/releases/tag/v0.1.0)     
[![Made with Python](https://img.shields.io/badge/Made_with-Python-blue?logo=python&logoColor=white)](https://www.python.org/)
![contributions - welcome](https://img.shields.io/badge/contributions-welcome-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Issues](https://img.shields.io/github/issues-raw/LEGOAI-TECHNOLOGIES/legoai_community_accelerator)](https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator/issues)
[![GitHub star chart](https://img.shields.io/github/stars/LEGOAI-TECHNOLOGIES/legoai_community_accelerator?style=social)](https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator/stargazers)



## What is it ?
This is a cutting-edge project leveraging advanced Machine Learning technologies to accurately discern and classify data types from various values. Designed to enhance data preprocessing and analysis pipelines, this tool automates the often tedious and error-prone task of manually identifying data types.

## Table of contents
- [Getting Started](#getting-started)
- [Main Features](#main-features)
- [Where to get it](#where-to-get-it)
- [Performance](#performance)
- [License](#license)
- [Contributing](#contributing)

##  Getting Started
To quickly start using the library just [install](#where-to-get-it) and follow jupyter notebook below ( or directly hop on the collab notebook ).
### Inference - DataType Identification
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/137XKjKA-awa5XYlb1bAnOoFCl3XALh1K?usp=sharing) 
- [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](DataTypeIdentification-Inference.ipynb)
> [!IMPORTANT]  
> **openai api key** is required for running L2 model inference.
### Training - L1 Model
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ipNkWzuk1_-yotBiROXbOeWBaSGtdeGD?usp=sharing)
- [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](DataTypeIdentification-Training.ipynb)



## Main Features
### Categorization - L1 & L2 Datatype
<img src="documentation/L1_&_L2_Model_Output.png" alt="L1 and L2 Model" >

- Has two models, **L1 model** (_**uses Classifier**_) that identifies normal datatypes  ( **integer, float, alphanumeric, range_type, date & time, open_ended_text, close_ended_text**)
-  **L2 model**  further classifies L1 datatype result that are **integer** or **float** to measure,dimension or unknown (if not classified) (_**uses LLM**_) and date & time into one of **41** date-time formats like (YYYY-MM-DD HH:MM:SS, YYYY/MM/DD, MM-DD-YYYY HH:MM AM/PM ) (_**uses RegEx**_).
<hr>

### Inference Workflow - Datatype Identification 
<img src="documentation/DI_Inference_WorkFlow.png" alt="DataType Identification Inference Workflow">
<hr>

### Training Workflow - L1 Model 
<img src="documentation/DI_Training_WorkFlow.png" alt="L1 Model Training Workflow">

>  [!IMPORTANT]  
> In the figure above **master_id** = dataset_name$$##$$table_name$$##$$column_name   
> that is used to uniquely identify the row and very important when joining labels & training dataset. 


## Where to get it?
Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/legoai/) & also at [GitHub](https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator)
```
# PyPI
> pip install legoai
```
```
# GitHub
> pip install git+https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator
```
## Performance
> [!NOTE]  
> **Source Ecommerce:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
>  ```Total Tables: 9``` , ```Total Columns: 52```   
> **Source Healthcare:** https://mitre.box.com/shared/static/aw9po06ypfb9hrau4jamtvtz0e5ziucz.zip  
> ```Total Tables: 18```, ```Total Columns: 249``` 

### Classification Report - L1 Model
<img src="documentation/L1_Model_Metrics.png" alt="L1 Model Classification Metrics" width="700">    
 <hr>
 
### Classification Report - L2 Model
<img src="documentation/L2_Model_Metrics.png" alt="L2 Model Classification Metrics" width="700">   
 <hr>
 
### Execution Chart - Google Collab Environment
<img src="documentation/Metrics Google Collab.png" alt="DI Execution Chart" width="400" height="300">

## License
The project is released under the [MIT License](LICENSE)

## Contributing
Any contributions to this project is **welcomed**, you can follow the steps below for contribution:
1. Fork the repository.
2. Create a new feature branch feature/*. (```git checkout -b feature/AmazingFeature```)
3. Make & add your changes.
4. Commit your changes. (```git commit -m 'Added some Amazing feature'```)
5. Push to the branch. (```git push origin feature/AmazingFeature```)
6. Create a new [Pull Request](https://github.com/LEGOAI-TECHNOLOGIES/legoai_community_accelerator/pulls).

