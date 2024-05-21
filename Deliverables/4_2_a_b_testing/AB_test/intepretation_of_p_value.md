
**The Shapiro-Wilk** tests for questions q1 through q5 in datasets df_A and df_B reveal that the data is not normally distributed, with all p-values significantly lower than the 0.05 threshold. This constant non-normality shows that typical parametric tests are inadequate, and bootstrapped variants should be used for analysis. Despite this, Levene's test for variance equality (p-value: 0.1977) reveals that the variances between groups are equal, satisfying one of the requirements for certain statistical tests. Nonetheless, the large divergence from normal distribution across both datasets emphasizes the significance of using non-parametric approaches or resampling techniques such as bootstrapping to provide accurate results.





**The T-test findings** for questions q1–q5 reveal no statistically significant differences between product versions A and B, indicating that the modifications made were insufficient to influence user replies or that the survey questions failed to capture the impacts of these changes. Notably, q1 and q3 neared significance, indicating a possible modest influence. This finding underscores the importance of reassessing both the changes made in version B and the survey design's efficacy. Future steps might include reevaluating the adjustments, using a bigger sample size, or improving survey questions to properly evaluate the targeted features of user experience and feedback.


The consistent non-normality implies that user answers vary greatly, reflecting different views or experiences with the app's features, necessitating strong, non-parametric analytic approaches for correct insights.