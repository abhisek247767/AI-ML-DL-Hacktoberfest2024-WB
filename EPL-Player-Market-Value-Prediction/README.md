# EPL-Player-Market-Value-Prediction

## Project Overview

This project focuses on predicting a football player's market value based on their statistical performance. In the competitive world of football, accurately assessing a player's market value is crucial for clubs and scouts. This project aims to provide a data-driven solution for this task.

## Models Explored

Two different models were employed to tackle the prediction problem:

1. **Linear Regression**: A traditional regression method used to establish a linear relationship between a player's statistics and their market value. This model can provide a baseline for prediction.

2. **XGBoost Regressor**: Leveraging the power of gradient boosting, the XGBoost regressor aims to capture complex relationships within the data, potentially leading to improved accuracy.

## Model Evaluation

To compare the performance of the models, several key metrics were used:

- **Mean Squared Error (MSE)**: A measure of the average squared differences between the predicted and actual market values.

- **Mean Absolute Error (MAE)**: This metric provides the average of the absolute differences between the predicted and actual values, offering a more interpretable measure of error.

- **R-squared (R2)**: Also known as the coefficient of determination, it quantifies the proportion of the variance in the market value that is predictable by the model. 

## Results

For Linear Regression:

- **Mean Squared Error (MSE)**: 34.804
- **Mean Absolute Error (MAE)**: 4.346
- **R-squared (R2)**: 0.781

For XGB Regressor:

- **Mean Squared Error (MSE)**: 30.853
- **Mean Absolute Error (MAE)**: 3.798
- **R-squared (R2)**: 0.805

The results indicate that both models show promise in predicting football player market values. The XGBoost Regressor outperforms the Linear Regression model, providing lower error metrics and a higher R-squared value.

## Conclusion

In the world of football, accurately predicting a player's market value can lead to better decision-making for clubs and scouts. This project showcases the potential of data-driven models for this task. The XGBoost Regressor, in particular, demonstrates promising results, indicating its suitability for predicting football player market values.
