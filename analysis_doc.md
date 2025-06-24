# Data Analysis – Customer Order & Revenue Dataset

## Objective

The objective is to understand customer-level order and revenue behavior and evaluate time-based patterns.

## Key Questions Explored

### 1. Overall Customer Behavior

- Average orders per customer: 12.87  
- Maximum orders by a single customer: 156  
- Minimum orders: 1  
- Average revenue per customer: ₹1,681  
- Maximum revenue: ₹34,847  
- Minimum revenue: ₹38  

This variation shows a broad spread of customer behavior, from low frequency, low value buyers to highly valuable repeat customers.

---

### 2. Are the highest revenue customers also the most frequent buyers?

The top 10 customers by revenue are:

| CustomerID | REVENUE | TOTAL_ORDERS |
|------------|---------|---------------|
| 1          | 34847.4 | 61            |
| 2          | 32487   | 59            |
| 3          | 24179   | 53            |
| 4          | 18554.5 | 84            |
| 5          | 16885   | 26            |
| 6          | 16693.8 | 66            |
| 7          | 15999.9 | 81            |
| 8          | 15840.4 | 19            |
| 9          | 14526.7 | 75            |
| 10         | 14309.9 | 47            |

Meanwhile, the top 10 by order count include customers with:

| CustomerID | REVENUE | TOTAL_ORDERS |
|------------|---------|---------------|
| 26         | 11349.6 | 156           |
| 28         | 11127.8 | 128           |
| 22         | 11986.5 | 124           |
| 47         | 8821.84 | 111           |
| 88         | 7148.66 | 109           |
| 48         | 8774.63 | 107           |
| 23         | 11828.9 | 101           |
| 107        | 6683.75 | 88            |
| 180        | 5552.51 | 85            |
| 4          | 18554.5 | 84            |

Customers with the most number of orders or frequent buyers are not always the ones providing the most revenue.

---

### 3. When do customers place most orders?

**Orders by Time Slot:**

- 12:00–18:00 -> 22,170 orders  
- 06:01–12:00 -> 18,731 orders  
- 18:01–23:59 -> 18,307 orders  
- 00:00–06:00 -> 5,144 orders  

**Revenue by Time Slot:**

- 12:00–18:00 -> ₹2,923,658  
- 06:01–12:00 -> ₹2,434,319  
- 18:01–23:59 -> ₹2,394,328  
- 00:00–06:00 -> ₹655,313  

Most purchases and most revenue occur in the afternoon (12–6 PM).

---

**Orders by Day:**

- Thursday -> 21,340  
- Wednesday -> 17,980  
- Tuesday -> 17,544  
- Monday -> 16,290  
- Friday -> 9,750  
- Sunday -> 9,627  
- Saturday -> 8,417  

**Revenue by Day:**

- Thursday -> ₹1,329,748  
- Sunday -> ₹1,304,716  
- Friday -> ₹1,252,902  
- Wednesday -> ₹1,178,446  
- Tuesday -> ₹1,167,552  
- Saturday -> ₹1,098,210  
- Monday -> ₹1,076,041  

Thursdays are the highest in both volume and value. Friday, Saturday, and Sunday generate high revenue even though they have comparatively fewer orders with respect to revenue. Therefore, AOV on these days would be high.

---

**Orders by Week:**

- Week 1 -> 14,989  
- Week 2 -> 15,313  
- Week 3 -> 16,150  
- Week 4 -> 17,900  

**Revenue by Week:**

- Week 1 -> ₹1,893,191.73  
- Week 2 -> ₹2,032,978.67  
- Week 3 -> ₹2,109,134.54  
- Week 4 -> ₹2,372,314.26  

Every new month, the orders and revenue gradually increase week by week, and hence the 4th week of the month has the highest orders and revenue.

---

### 4. Observations about how frequently customers ordered

- Average days since last order: 87.4  
- Minimum: 1 day, Maximum: 455 days  
- Average gap between orders: 163.2 days  
- Min gap between orders: 0.0 days  
- Max gap between orders: 1409.5 days  

This shows some customers are extremely regular, while others might only purchase once or twice a year.

#### 4.1 Segmentation of customers based on their last order

- Last order more than 45 days ago: 2,180  
- Last order between 45 and 90 days: 655  
- Last order more than 90 days ago: 2,165  

A large portion of customers haven't ordered recently, indicating churn risk.

#### 4.2 How many customers ordered only 1 time?

- Number of customers who have ordered more than 1 time: 4,634 (92.7%)  
- Number of customers who ordered only 1 time: 366 (7.3%)  

#### 4.3 How many one-time customers are there in the last *n* days?

- In the last 45 days: 130 (New customers)  
- In the last 200 days: 130  
- In the last 250 days: 366  
- In the last 1000 days: 366  

As the number of customers who have ordered 1 time is the same in the last 45 days and the last 200 days, it means that all customers who joined or were active during that period placed more than one order.

The remaining 236 customers (366 - 130) are older and never returned, which is a retention gap.

---

## Data Quality Observations

- No missing values in key columns  
- Revenue and order breakdowns by day/time/week are clean and consistent with matching sums for `REVENUE` and `TOTAL_ORDERS` respectively  
- All values in calculated columns are correct

---

## Models that can be build :

- K means clustering - to group customers based on how recently, how often, and how much they purchase

- Logistic Regression - to predict which customers are at risk of not returning based on days since last order, order frequency.

- Logistic Regression - Used to identify customers who are likely to buy only once and not return.

- XGboost - Predict Revenue that customer will generate

- Random Forest Classifier - predict if customer will provide high revenue in future.


### FLOWCHART

1- Objective -> Understand customer level order & revenue behavior, and evaluate time-based patterns
      
2- Start with -> Overall Customer Behavior
      
3- Checked -> Average orders per customer, revenue per customer -> Found wide variation
      
4- Led to -> Segmentation of customer base -> Are high revenue customers also frequent buyers?
      
5- Compare Top 10 by Revenue vs Top 10 by Order Count -> High spenders aren't Frequent buyers.
      
6- Explore -> Time-based Patterns of Orders and Revenue
      
7- Split by -> Time of Day -> Afternoon (12–6 PM) is peak for both orders and revenue

8- Split by -> Day of Week -> Thursdays top for both; Weekends -> higher AOV despite fewer orders

9- Split by -> Weeks of Month -> Increasing trend -> 4th week = highest
      
10- Insight -> Order & revenue build across the month -> could be salary cycle or promotions
      
11- Investigate -> Customer Frequency Behavior
      
12- Calculated -> Days since last order -> Found large portion haven't ordered recently -> Possible churn risk

13- Segmented -> Based on last order (45, 45-90, 90+ days) -> Found clear retention gaps

14- Checked -> One-time customers -> 7.3% -> Mostly new or inactive older customer