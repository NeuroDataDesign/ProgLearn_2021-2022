# Nonpar MANOVA via Independence Testing
[Vogelstein etal. 2021](https://arxiv.org/pdf/1910.08883.pdf)

## 1 Introduction 
- goal of k-sample testing is to determine whether k datasets were sampled from the same distribution
- ANOVA (analysis of variance), MANOVA (multivariate version), fail or operate poorly on multivariate and nonlinear data, also suffer from fundamental assumptions that are not generally present in real data
- we want non-parametric tests similar to MANOVA
- demonstrate high dim independence tests (KMERF, MGC specifically) have higher statistical power than the alt's

## 2 Prelims
**Hotelling** is a generalization of Student's t-test in an arbitrary dimension 

![image](https://user-images.githubusercontent.com/89429238/138177712-ff6bbe54-9d12-4dbb-a3f1-48128e3d32e1.png)

**MANOVA** is a procedure used to compare 2+ multivariate samples

### Independence tests
**DCORR**  test to determine linear and anonlinear associations between 2 random vars or vectors in arb dims

**HSIC** similar to above but uses kernal similarity matrices instead of distance matrices
- every DCORR test is an HSIC test and vice versa
- DCORR uses an Euclidean distance 
- HSIC uses a Gaussian kernel similarity

**MGC** preserves the consistency property while typically working better in multivariate and non-monotonic relationships

**KMERF** kernal method for calculating independence by using a random forest induced similarity matrix as an input
- high gains in finite sample testing power in high dim setting 

## 3 Results
![image](https://user-images.githubusercontent.com/89429238/138187129-d55ed6d1-02cb-49e0-8e93-83cbbd4bb68e.png)

![image](https://user-images.githubusercontent.com/89429238/138187361-a6cac723-d827-4acd-b0f1-b2bc2b93634a.png)

- suggest that even at a simulation setting where MANOVA  test is expected to perform best (linear sim setting, all distributions gaussian, all distributions same covariance), nonparametric k-sample tests can perform as well and sometimes much better 

![image](https://user-images.githubusercontent.com/89429238/138187680-b9ee398e-9044-4bf3-a14a-4cfaf86b7a29.png)

![image](https://user-images.githubusercontent.com/89429238/138187781-9d7b6e42-0812-46cd-9d1a-6241ead3625b.png)

