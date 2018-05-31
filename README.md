# Mult-class text classification
> Project of classifying tweets of company **Limportant** into 13 categories

## 1. Highlights:
- Language: Python
- It uses CountVectorizer, TfidfTransformer to pre-processing text data
- Machine learing package is sklearn
- It uses GridSearch to get hyperparameter of the best model
- Ensemble modeling with voting
- Full-score, which combines precision and recall, is 0.68/1.00

## 2. Data:

### 2.1 Training:
- Training size: 18 000 tweets
- Input: text, category_id
- Output: category_id

### 2.2 Predicting:
- Input: text
- Output: category_id

## 3. Reference:
- [Multi-Class Text Classification with Scikit-Learn](https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f)


