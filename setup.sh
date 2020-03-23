# Modified from https://github.com/mkocabas/VIBE/blob/master/install_conda.sh

export CONDA_ENV_NAME=witchat
echo $CONDA_ENV_NAME

conda create -n $CONDA_ENV_NAME python=3.7 -y

eval "$(conda shell.bash hook)"
conda activate $CONDA_ENV_NAME

which python
which pip

pip install -r requirements.txt
