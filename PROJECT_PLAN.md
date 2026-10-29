# Project Plan

## 1. Monte Carlo Risk & Reliability Simulator

## 2. Project Objective

Build a reusable Python-based Monte Carlo simulation pipeline for quantifying uncertainty and risk in financial and engineering systems. 

The framework will allow investigation into the effects of systematically varying model parameters on the simulated outcomes.
As the project evolves, MC methods will be compared with analytical solutions and where necessary, alternative statistical approaches to evaluate accuracy, computational cost and practical use. 

## 3. Core Question 

How effectively can MC simulations be used to quantify uncertainty and calculate the probability of outcomes in financial and engineering systems, and how do these computational requirements and its accuracy depend on model assumptions and the simulation size. 

## 4. Why this Project

This project sits at the intersection of financial and engineering quantitative research, allowing similar underlying ideas of probability, simulation and uncertainty to be applied to various real-world problems. It demonstrates a capability to develop statistical modelling, uncertainty analysis, model validation and general confidence in using Python. 

## 5. Version 0.1 Scope

Version 0.1 will simulate a single uncertain variable, estimate the probability of exceeding a defined threshold, calculate summary statistics, and visualise the resulting distribution. 

## 6. Finance Use Case

Simulate uncertain investment returns and estimate quantities such as expected return, volatillity, probability of loss, value at risk, expected shortfall and drawdowns, etc. 

Later versions may be extended from one asset to multiple assets, correlation, portfolio risk. 

## 7. Engineering Use Case

Model probability of system failure, expected lifetime, reliability over time, impact of component failure rates, effect of redundancy, which components contribute most to system risk, etc. 

Later versions may further investigate series systems, parallel systems, redundancy. 

## 8. Inputs 

Version 0.1 inputs will include mean value, standard deviation, number of simulations, critical threshold, random seed, etc. 

Later financial versions may include initial investment, expected return, volatility, time horizon, number of simulations. 

likewise, engineering inputs may include component failure probability, system configuration, number of simulations, time horizon. 

## 9. Outputs

Version 0.1 will produce statistical summaries (simulated values, mean, standard deviation, probability of threshold breach) and distribution plots. 

## 10. Assumptions 

Assumptions noted here are subject to change as the project evolves. 

Outcomes follow a normal distribution, independent simulations, parameters are known and fixed, fixed threshold, random draws are representative of the assumed distribution. 

## 11. Mathematical Concepts

Probability distributions, expected value, variance and standard deviation, Monte Carlo estimation, percentiles, confidence intervals/tests, conditional probability, covariance and correlation, reliability probability. 

## 12. Validation Strategy

To prove my simulation works i will compare simulated statistical values against their theoreticals, simulated threshold probability with analytical probability, increase the number of simulations and check where they converge, test known reliability cases against analytical formulas. 

## 13. Planned Development Phases

Phase 1: Basic MC simulation
Phase 2: Single-asset financial risk 
Phase 3: Multi-asset portfolio simulation
Phase 4: Risk metrics and sensitivity    analysis
Phase 5: Engoineering reliability model
Phase 6: Redundancy and system design
Phase 7: Validation and testing
Phase 8: Refactoring and documentation

## 14. Possible Future Extensions

## Financial Statstical Models

Propensity score matching, difference-in-difference, regression discontinuity design, instrumental variables, generalised linear mixed models, structural equation modelling, survival/time-to-event analysis (Cox proportional hazards models), regularisation techniques, resampling methods (bootstrapping, K-fold cross-validation), ensemble methods, Bayesian hierarchial modelling, Markov Chain Monte Carlo. 

## Engineering Statistical Models 

Weibull Analysis (lifetime data analysis - models failure rates over time and maps out the "bathtub curve"), Markov chains 7 stochastic modelling (evaluates multi-state system reliability), MTBF/MTTF mathematical modelling (calculates mean time between failures under various stress testing constraints using accelerated life testing data models), probabilistic risk assessments, factorial design & fractional factorial design, response surface methodology, control charts, process capability indexes. 

