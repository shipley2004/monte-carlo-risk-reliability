# Monte Carlo Risk & Reliability Simulator

A Python project exploring Monte Carlo simulation for financial risk and engineering reliability. The project is in progress; the current MVP models a normally distributed variable and estimates the probability of exceeding a threshold.

## Current MVP

[`phase2_MVP.py`](phase2_MVP.py) generates reproducible samples, reports summary statistics and a threshold probability with its standard error and confidence interval, and compares simulated results with the theoretical normal distribution. It also runs repeated simulations to examine variation between probability estimates.

The script requires Python 3 and Matplotlib:

```bash
python3 -m pip install matplotlib
python3 phase2_MVP.py
```

By default, the script uses a mean of 100, a standard deviation of 15, 10,000 samples, and a threshold of 80. It saves four figures under [`outputs/figures/version_0_1/`](outputs/figures/version_0_1/):

- [Sample histogram and theoretical distribution](outputs/figures/version_0_1/histogram.png)
- [Empirical and theoretical cumulative distributions](outputs/figures/version_0_1/cdf.png)
- [Threshold probability convergence](outputs/figures/version_0_1/convergence.png)
- [Zoomed threshold probability convergence](outputs/figures/version_0_1/convergence_zoomed.png)

The broader project scope and planned phases are described in [`PROJECT_PLAN.md`](PROJECT_PLAN.md).
