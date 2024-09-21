# TeamProject

[Team Notion] (https://www.notion.so/c8656358b25140ce94c256873920b7d1?v=9e55264d11a64163b39e387c4c0ff5a0&pvs=4)

Google Colab (https://colab.research.google.com/drive/1saWd4OvidkpzgWAW3TEEeZWHAhMxORqf?usp=sharing)

**Tasks for Sprint 1**

Some tasks that I have finished are: 

* Perform EDA: Visualize patterns, trends, and anomalies in the data; analyze distribution of sentiments and key features.
* Splitting `review_by_dating_category` with two suggestions:
1. Suggestion 1: keeping `id`
   * Each of the items in rating_category have their own column
   * df_final has the same amount of rows as our original df
   * each row keeps the 'id' column and the 'review_id' column even though some 'id' values are tied to the same 'review_id'
   * all NaN/null values are replaced with a 0
2. Suggestion 2: removing `id` since it is tied with `review_id`
   * drops 'id' category and ties all 'id' values to associated 'review_id'
   * all NaN values are replaced with a 0
   * this df will be smaller than the original df, but will retain all necesary information

* Under both of these suggestions I performed Exploratory Data Analysis where I provided visuals
  - in both of the EDA, I started working on removing duplicates and filling in the missing ratings with median values
