# Chest-Disease-Classification-from-Chest-CT-Scan-Image

- [Data link](https://drive.google.com/file/d/1z0mreUtRmR-P-magILsDR3T7M6IkGXtY/view?usp=sharing)

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml


## Git commands

```
git add .
``` 

```
git commit -m "Updated"
```

```
git push origin main
```

## How to run?

```
conda create -n chest python=3.8 -y
```

```
conda activate chest
```

```
pip install -r requirements.txt
```

```
python app.py
```

## Mlflow dagshub connection uri

```
MLFLOW_TRACKING_URI=https://dagshub.com/kamleshp95/Chest-Disease-Classification-from-Chest-CT-Scan-Image.mlflow \
MLFLOW_TRACKING_USERNAME=kamleshp95 \
MLFLOW_TRACKING_PASSWORD=cd33eb294b356173fba2db28335743044a55b13b \
python script.py
```

## RUN from bash terminal

```
export MLFLOW_TRACKING_URI=https://dagshub.com/kamleshp95/Chest-Disease-Classification-from-Chest-CT-Scan-Image.mlflow

export MLFLOW_TRACKING_USERNAME=kamleshp95

export MLFLOW_TRACKING_PASSWORD=cd33eb294b356173fba2db28335743044a55b13b
```


### DVC cmd

```
1. dvc init
2. dvc repro
3. dvc dag
```