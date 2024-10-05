---
marp: true
paginate: true
---

<!-- These set styles for the entire document. -->
<style>

h1 {
  background: linear-gradient(90.2deg, rgba(190, 70, 102, 0.93) -15.6%, rgb(252, 154, 154) -15.6%, rgba(190, 70, 102, 0.92) 17.9%, rgb(58, 13, 48) 81.6%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

h1 { font-size: 72px }

h2 { font-size: 48px; color: #fff; }

h3 { font-size: 36px; vertical-align: top; }

h3, h4, h5 {
  background: rgb(58, 13, 48);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

h3, h4, h5 { color: #444 }

section {
  position: absolute;
  height: inherit;
  vertical-align: bottom;
  margin: 0;
  display: table-cell;
}

</style>

<br><br><br>

##### Lecture 3

# Comparing Loss Functions 

#### DSC 40A, Spring 2024

---

### Announcements

- Homework 1 is due on **Thursday, April 11th**.
  - Before working on it, watch the [Walkthrough Videos](https://www.youtube.com/playlist?list=PLDNbnocpJUhYtg3s2__3pbh1kNKYxXaFM) on problem solving and using Overleaf.
  - Using the Overleaf template is required for Homework 2 (and only Homework 2).
- Remember that in, general, groupwork worksheets are released on Sunday and due Monday.
- Look at the office hours schedule [here](https://dsc40a.com/calendar) and plan to start regularly attending!
- Remember to take a look at the supplementary readings linked on the course website.

---

### Agenda

- Recap: Empirical risk minimization.
- Choosing a loss function.
  - The role of outliers.
- Center and spread.
- Towards linear regression.

---

<style scoped>section {background: #f2ecf4 }</style>

### Question 🤔
**Answer at [q.dsc40a.com](https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform)**

<br><br><br>

<center><big><b>Remember, you can always ask questions at <a href="https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform">q.dsc40a.com</a>!</b></big></center>

---

<style scoped>section {background: linear-gradient(90deg, hsla(290, 25%, 76%, 1) 0%, hsla(284, 80%, 10%, 1) 100%);}</style>

<br><br><br><br><br>

## Recap: Empirical risk minimization

---

### Goal

We had one goal in Lecture 2: given a dataset of values from the past, **find the best constant prediction** to make.

<br>

$$y_1 = 72 \:\:\:\:\:\:\:\:\:\: y_2 = 90 \:\:\:\:\:\:\:\:\:\: y_3 = 61 \:\:\:\:\:\:\:\:\:\: y_4 = 85 \:\:\:\:\:\:\:\:\:\: y_5 = 92$$

<br>

**Key idea**: Different definitions of "best" give us different "best predictions."

---

### The modeling recipe

In Lecture 2, we made two full passes through our "modeling recipe."

1. Choose a model.

<br>

2. Choose a loss function.

<br>

3. Minimize average loss to find optimal model parameters.

---

### Empirical risk minimization

- The formal name for the process of minimizing average loss is **empirical risk minimization**.

- Another name for "average loss" is **empirical risk**.

- When we use the squared loss function, $L_\text{sq}(y_i, h) = (y_i - h)^2$, the corresponding empirical risk is mean squared error:

$$R_\text{sq}(h) = \frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$$

- When we use the absolute loss function, $L_\text{abs}(y_i, h) = |y_i - h|$, the corresponding empirical risk is mean absolute error:

$$R_\text{abs}(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - h|$$

---

### Empirical risk minimization, in general

**Key idea**: If $L(y_i, h)$ is **any** loss function, the corresponding empirical risk is:

$$R(h) = \frac{1}{n} \sum_{i = 1}^n L(y_i, h)$$

---

<style scoped>section {background: #f2ecf4 }</style>

### Question 🤔
**Answer at [q.dsc40a.com](https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform)**

<br><br><br>

<center><big><b>What questions do you have?</b></big></center>

---

<style scoped>section {background: #f2ecf4 }</style>

### Question 🤔
**Answer at [q.dsc40a.com](https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform)**

$$R_\text{sq}(h) = \frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$$

$$R_\text{abs}(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - h|$$

Is the following statement true, for any dataset $y_1, y_2, ..., y_n$ and prediction $h$?

$$\left( R_\text{abs}(h) \right)^2 = R_\text{sq}(h)$$

- A. It's true for any $h$ and any dataset.
- B. It's true for at least one $h$ for any dataset, but not in general.
- C. It's never true.


---

<style scoped>section {background: linear-gradient(90deg, hsla(290, 25%, 76%, 1) 0%, hsla(284, 80%, 10%, 1) 100%);}</style>

<br><br><br><br><br>

## Choosing a loss function

---

### Now what?

- We know that, for the constant model $H(x) = h$, the **mean** minimizes mean **squared** error.
- We also know that, for the constant model $H(x) = h$, the **median** minimizes mean **absolute** error.
- **How does our choice of loss function impact the resulting optimal prediction?**

---

### Comparing the mean and median

- Consider our example dataset of 5 commute times.

$$y_1 = 72 \:\:\:\:\:\:\:\:\:\: y_2 = 90 \:\:\:\:\:\:\:\:\:\: y_3 = 61 \:\:\:\:\:\:\:\:\:\: y_4 = 85 \:\:\:\:\:\:\:\:\:\: y_5 = 92$$

- As of now, the **median is 85** and the **mean is 80**.
- What if we add 200 to the largest commute time, $92$?

$$y_1 = 72 \:\:\:\:\:\:\:\:\:\: y_2 = 90 \:\:\:\:\:\:\:\:\:\: y_3 = 61 \:\:\:\:\:\:\:\:\:\: y_4 = 85 \:\:\:\:\:\:\:\:\:\: y_5 = 292$$

- Now, the median is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; but the mean is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!

- **Key idea**: The mean is quite **sensitive** to outliers.


---

### Outliers

Below, $|y_4 - h|$ is 10 times as big as $|y_3 - h|$, but $(y_4 - h)^2$ is 100 times $(y_3 - h)^2$.

<center>

<img src="imgs/outlier-line.png" width="75%">

</center>


The result is that the <span style="color: green"><b>mean</b></span> is "pulled" in the direction of outliers, relative to the <span style="color: purple"><b>median</b></span>.

<center>

<img src="imgs/four-dots-median-mean.png" width="75%">

</center>

As a result, we say the <span style="color: purple"><b>median</b></span> is **robust** to outliers. But the <span style="color: green"><b>mean</b></span> was easier to solve for.

---

<center>

<img src="imgs/hist-minutes.png" width=87%>

</center>

---

### Example: Income inequality

<center>

<img src="imgs/inequality.png" width=75%>

</center>

---

### Balance points

Both the <span style="color: green"><b>mean</b></span> and <span style="color: purple"><b>median</b></span> are "balance points" in the distribution.

<center>

<img src="imgs/four-dots-median-mean.png" width="75%">

</center>

- The <span style="color: green"><b>mean</b></span> is the point where $\sum_{i = 1}^n (y_i - h) = 0$.
  - This appears in Homework 1!

<br>

- The <span style="color: purple"><b>median</b></span> is the point where $\# \: (y_i < h) = \# \: (y_i > h)$.

--- 

### Why stop at squared loss?

<center>

| Empirical Risk, $R(h)$ | Derivative of Empirical Risk, $\frac{d}{dh}R(h)$ | Minimizer |
| --- | --- | --- |
| $\frac{1}{n} \sum_{i = 1}^n \|y_i - h\|$ | $\frac{1}{n} \big( \sum_{y_i < h} 1 - \sum_{y_i > h}1  \big)$| median |
| $\frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$ | $\frac{-2}{n}\sum_{i = 1}^n (y_i - h)$ | mean |
| $\frac{1}{n} \sum_{i = 1}^n \|y_i - h\|^3$ | <br><br> | ??? |
| $\frac{1}{n} \sum_{i = 1}^n (y_i - h)^4$ | <br><br> | ??? |
| $\frac{1}{n} \sum_{i = 1}^n (y_i - h)^{100}$ | <br><br> | ??? |
| ... | ... | ... |

</center>


---

### Generalized $L_p$ loss

For any $p \geq 1$, define the $L_p$ loss as follows:

$$L_p(y_i, h) = |y_i - h|^p$$

The corresponding empirical risk is:

$$R_p(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - h|^p$$

- When $p = 1$, $h^* = \text{Median}(y_1, y_2, ..., y_n)$.
- When $p = 2$, $h^* = \text{Mean}(y_1, y_2, ..., y_n)$.
- What about when $p = 3$?
- What about when $p \rightarrow \infty$?

---

### What value does $h^*$ approach, as $p \rightarrow \infty$?

<div style="width: 100%;">

<br>
    <div style="width: 48%; float: left"> 
<img src="imgs/midrange-limit.png" width=100%>
    </div>
    <div style="margin-left: 50%; height: 100px;" markdown="1"> 

Consider the dataset $1, 2, 3, 14$:

<img src="imgs/four-dots-median-mean.png" width="100%">

On the left:
- The $x$-axis is $p$.
- The $y$-axis is $h^*$, the optimal constant prediction for $L_p$ loss:

$$h^* = \underset{h}{\text{argmin}} \frac{1}{n} \sum_{i = 1}^n |y_i-h|^p$$

</div>
</div>

---

### The _midrange_ minimizes average $L_\infty$ loss!

On the previous slide, we saw that as $p \rightarrow \infty$, the minimizer of mean $L_p$ loss approached **the midpoint of the minimum and maximum values in the dataset**, or the <span style="color: red"><b>midrange</b></span>.


<center>
<img src="imgs/four-dots-median-mean-midrange.png" width="65%">
</center>

- As $p \rightarrow \infty$, $R_p(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - h|^p$ minimizes **the "worst case" distance from any data point".** (Read more [here](https://mathworld.wolfram.com/L-Infinity-Norm.html)).
- If your measure of "good" is "not far from any one data point", then the midrange is the best prediction.

---

### Another example: 0-1 loss

Consider, for example, the **0-1 loss**:

$$L_{0,1}(y_i, h) = \begin{cases} 0 & y_i = h \\ 1 & y_i \neq h \end{cases}$$

The corresponding empirical risk is:

$$R_{0,1}(h) = \frac{1}{n} \sum_{i = 1}^n L_{0, 1}(y_i, h)$$

---

<style scoped>section {background: #f2ecf4 }</style>

### Question 🤔
**Answer at [q.dsc40a.com](https://docs.google.com/forms/d/e/1FAIpQLSfEaSAGovXZCk_51_CVI587CcGW1GZH1w4Y50dKDzoLEX3D4w/viewform)**

$$R_{0,1}(h) = \frac{1}{n} \sum_{i = 1}^n \begin{cases} 0 & y_i = h \\ 1 & y_i \neq h \end{cases}$$

Suppose $y_1, y_2, ..., y_n$ are all unique. What is $R_{0, 1}(y_1)$?

- A. 0.
- B. $\frac{1}{n}$.
- C. $\frac{n-1}{n}$.
- D. 1.

---

### Minimizing empirical risk for 0-1 loss

$$R_{0,1}(h) = \frac{1}{n} \sum_{i = 1}^n \begin{cases} 0 & y_i = h \\ 1 & y_i \neq h \end{cases}$$


---

### Summary: Choosing a loss function

**Key idea**: Different loss functions lead to different best predictions, $h^*$!


<center markdown="1">

| Loss | Minimizer | Always<br>Unique? | Robust to<br>Outliers? | Differentiable? |
| --- | --- | --- | --- | --- |
| $L_\text{sq}$ | mean | yes ✅ | no ❌ | yes ✅ |
| $L_\text{abs}$ | median | no ❌ | yes ✅ | no ❌ |
| $L_\infty$ | midrange | yes ✅ | no ❌ | no ❌ |
| $L_\text{0,1}$ | mode | no ❌ | yes ✅ | no ❌ |

</center>

<br>

The optimal predictions, $h^*$, are all **summary statistics** that measure the **center** of the dataset in different ways.

---

<style scoped>section {background: linear-gradient(90deg, hsla(290, 25%, 76%, 1) 0%, hsla(284, 80%, 10%, 1) 100%);}</style>

<br><br><br><br><br>

## Center and spread

---

### What does it mean?

- The general form of empirical risk, for any loss function $L(y_i, h)$, is:

$$R(h) = \frac{1}{n} \sum_{i = 1}^n L(y_i, h)$$

- As we just saw, the input $h^*$ that minimizes $R(h)$ is some measure of the **center** of the dataset.
  - Examples include the mean ($L_\text{sq}$), median ($L_\text{abs}$), and mode ($L_\text{0,1}$).

- The minimum output, $R(h^*)$, represents some measure of the **spread**, or variation, in the dataset.

---

### Squared loss

- The empirical risk for squared loss, i.e. mean squared error, is:

$$R_\text{sq}(h) = \frac{1}{n} \sum_{i = 1}^n (y_i - h)^2$$

- $R_\text{sq}(h)$ is minimized when $h^* = \text{Mean}(y_1, y_2, ..., y_n)$.
- Therefore, the minimum value of $R_\text{sq}(h)$ is:

$$\begin{align*} R_\text{sq}(h^*) &= R_\text{sq}\left( \text{Mean}(y_1, y_2, ..., y_n) \right) \\  &= \frac{1}{n} \sum_{i = 1}^n \left( y_i -  \text{Mean}(y_1, y_2, ..., y_n) \right)^2  \end{align*}$$

---

### Variance

- The minimum value of $R_\text{sq}(h)$ is the mean squared deviation from the mean, more commonly known as the **variance**.

$$\text{Variance}(y_1, y_2, ..., y_n) =\frac{1}{n} \sum_{i = 1}^n \left( y_i -  \text{Mean}(y_1, y_2, ..., y_n) \right)^2$$

- It measures the squared distance of each data point from the mean, on average.

- Its square root is called the **standard deviation**.

---

<br>

<center>
<img src="imgs/risk.png" width=80%>
</center>

---

### Absolute loss

- The empirical risk for absolute loss, i.e. mean absolute error, is:

$$R_\text{abs}(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - h|$$

- $R_\text{abs}(h)$ is minimized when $h^* = \text{Median}(y_1, y_2, ..., y_n)$.

- Therefore, the minimum value of $R_\text{abs}(h)$ is:

$$\begin{align*} R_\text{abs}(h^*) &= \frac{1}{n} \sum_{i = 1}^n |y_i - h| \\ &= R_\text{abs}(h) = \frac{1}{n} \sum_{i = 1}^n |y_i - \text{Median}(y_1, y_2, ..., y_n)| \end{align*}$$

---

### Mean absolute deviation from the median

- The minimum value of $R_\text{abs}(h)$ is the **mean absolute deviation from the median**.

$$\text{MAD from the median}(y_1, y_2, ..., y_n) =  \frac{1}{n} \sum_{i = 1}^n |y_i - \text{Median}(y_1, y_2, ..., y_n)|$$

- It measures how far each data point is from the median, on average.

- **Example**: What's the MAD from the median in the dataset $2, 3, 3, 4, 5$?

---

### Mean absolute deviation from the median


<center>
<img src="imgs/r-abs-odd.png" width=80%>
</center>

---

### 0-1 loss

- The empirical risk for the 0-1 loss is:

$$R_{0,1}(h) = \frac{1}{n} \sum_{i = 1}^n \begin{cases} 0 & y_i = h \\ 1 & y_i \neq h \end{cases}$$

- This is the proportion (between 0 and 1) of data points not equal to $h$.

- $R_{0,1}(h)$ is minimized when $h^* = \text{Mode}(y_1, y_2, ..., y_n)$.

- Therefore, $R_{0,1}(h^*)$ is the proportion of data points not equal to the mode.

- **Example**: What's the proportion of values not equal to the mode in the dataset $2, 3, 3, 4, 5$?

---

### A poor way to measure spread

- The minimum value of $R_{0,1}(h)$ is the proportion of data points not equal to the mode.

- A higher value means less of the data is clustered at the mode.

- Just as the mode is a very basic way of measuring the center of the data, $R_{0,1}(h^*)$ is a very basic and uninformative way of measuring spread.

---

### Summary of center and spread

- Different loss functions $L(y_i, h)$ lead to different empirical risk functions $R(h)$, which are minimized at various measures of **center**.

- The minimum values of empirical risk, $R(h^*)$, are various measures of **spread**.

- There are many different ways to measure both center and spread; these are sometimes called **descriptive statistics**.

---

<style scoped>section {background: linear-gradient(90deg, hsla(290, 25%, 76%, 1) 0%, hsla(284, 80%, 10%, 1) 100%);}</style>

<br><br><br><br><br>

## What's next?

---

### Towards simple linear regression

<div style="width: 100%;">
    <div style="width: 50%; float: left"> 
    <br>
<img src="imgs/scatter-1.png" width=100%>
    </div>
    <div style="margin-left: 50%; height: 100px;" markdown="1"> 

- In Lecture 1, we introduced the idea of a hypothesis function, $H(x)$.
- We've focused on finding the best **constant model**, $H(x) = h$.
- Now that we understand the modeling recipe, we can apply it to find the best **simple linear regression model**, $H(x) = w_0 + w_1 x$.
- This will allow us to make predictions that aren't all the same for every data point.

</div>
</div>

---

### The modeling recipe

1. Choose a model.

<br><br>

2. Choose a loss function.

<br><br>

3. Minimize average loss to find optimal model parameters.

---