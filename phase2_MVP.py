"""This document is intended to serve a a startup to this coding project, as outlined in the README, 
 i start with a small Minimum Viable Product (MVP) for my Monte Carlo (MC) Risk & Reliability Simulation 
 Framework in Python. 

 First i am going to experiment with python's built in random library packages to test the functionality 
 of the MC simulation framework."""

import math
import random
import statistics
from pathlib import Path

import matplotlib.pyplot as plt

def generate_samples(mean, std, size, seed=None):
    """Generate a list of random numbers following a normal distribution."""
    generator = random.Random(seed)                                             # Create a random number generator instance with the specified seed for reproducibility.
    return [generator.gauss(mean, std) for _ in range(size)]

def calc_summary_stats(samples):
    """Calculate summary statistics for a list of samples."""
    percentiles = statistics.quantiles(samples, n=100, method='inclusive')
    return {
        'mean': statistics.mean(samples),
        'variance': statistics.variance(samples),
        'std_dev': statistics.stdev(samples),
        'median': statistics.median(samples),
        'percentile_25': percentiles[24],
        'percentile_50': percentiles[49],
        'percentile_75': percentiles[74],
        'percentile_95': percentiles[94],
        'minimum': min(samples),
        'maximum': max(samples),
    }

def estimate_prob_above(samples, threshold):
    """Estimate the probability of samples being above a certain threshold."""
    count_above = 0
    for sample in samples:              # Iterates through each item in the sample to see if it exceeds the
        if sample > threshold:          # threshold - if it does, then it assigns a value of 1 to the count_below
            count_above += 1            # variable, and if it does not, it's assigned 0. 
    return count_above / len(samples)   # Then the number of items exceeding the threshold
                                        # in the sample is returned as a probability value.

def estimate_prob_standard_error(probability, sample_size):
    """Estimate (Bernoulli) Monte Carlo standard error for a probability estimate."""
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between zero and one")
    if sample_size < 1:
        raise ValueError("sample_size must be at least 1")

    return math.sqrt(probability * (1 - probability) / sample_size)

def estimate_prob_confidence_interval(
    probability,
    sample_size,
    confidence_level=0.95,
):
    """Estimate a normal-approximation confidence interval for a probability."""
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one")

    standard_error = estimate_prob_standard_error(probability, sample_size)
    tail_probability = (1 + confidence_level) / 2                               
    critical_value = statistics.NormalDist().inv_cdf(tail_probability)      # Calculate the critical value for the given confidence level
    margin_of_error = critical_value * standard_error       # Calculate the margin of error, this physically represents the range of values 
                                                            # within which we expect the true probability to lie, given our sample data and 
    return (                                                # the specified confidence level.
        max(0.0, probability - margin_of_error),
        min(1.0, probability + margin_of_error),
    )

def run_repeated_simulations(
    mean=100,
    std=15,
    size=10_000,
    threshold=80,
    runs=100,
    seed=42,
):
    """Run independent simulations with the same model and parameters."""
    if std <= 0:
        raise ValueError("std must be greater than zero")
    if size < 1:
        raise ValueError("size must be at least 1")
    if runs < 2:
        raise ValueError("runs must be at least 2")

    seed_generator = random.Random(seed)
    probabilities = []
    standard_errors = []

    for _ in range(runs):
        run_seed = seed_generator.randrange(0, 2**63)
        samples = generate_samples(mean, std, size, run_seed)
        probability = estimate_prob_above(samples, threshold)
        probabilities.append(probability)
        standard_errors.append(
            estimate_prob_standard_error(probability, size)
        )

    distribution = statistics.NormalDist(mu=mean, sigma=std)
    theoretical_probability = 1 - distribution.cdf(threshold)
    average_standard_error = statistics.mean(standard_errors)

    results = {
        'probabilities': probabilities,
        'probability_mean': statistics.mean(probabilities),
        'probability_std_dev': statistics.stdev(probabilities),
        'average_standard_error': average_standard_error,
        'theoretical_prob_above': theoretical_probability,
    }

    print(f"Repeated simulations: {runs}")
    print("Mean estimated probability:", results['probability_mean'])
    print("Standard deviation between run estimates:", results['probability_std_dev'])
    print("Average single-run standard error:", average_standard_error)
    print("Theoretical probability:", theoretical_probability)

    return results



def run_simulation(mean=100, std=15, size=10_000, threshold=80, seed=42):       
    """Run the baseline Monte Carlo experiment with configurable inputs."""
    if std <= 0:
        raise ValueError("std must be greater than zero")
    if size < 2:
        raise ValueError("size must be at least 2")

    samples = generate_samples(mean, std, size, seed)
    summary_stats = calc_summary_stats(samples)
    sample_mean = summary_stats['mean']
    sample_std = summary_stats['std_dev']
    prob_above = estimate_prob_above(samples, threshold)
    prob_standard_error = estimate_prob_standard_error(prob_above, size)
    prob_confidence_interval = estimate_prob_confidence_interval(prob_above, size)
    distribution = statistics.NormalDist(mu=mean, sigma=std)
    theoretical_prob_above = 1 - distribution.cdf(threshold)

    print("Sample mean:", sample_mean)
    print("Sample variance:", summary_stats['variance'])
    print("Sample standard deviation:", sample_std)
    print("Sample median:", summary_stats['median'])
    print("Sample 25th percentile:", summary_stats['percentile_25'])
    print("Sample 50th percentile:", summary_stats['percentile_50'])
    print("Sample 75th percentile:", summary_stats['percentile_75'])
    print("Sample 95th percentile:", summary_stats['percentile_95'])
    print("Sample minimum:", summary_stats['minimum'])
    print("Sample maximum:", summary_stats['maximum'])
    print("Estimated probability of exceeding threshold:", prob_above)
    print("Standard error of estimated probability:", prob_standard_error)
    print("95% confidence interval for estimated probability:", prob_confidence_interval)
    print("Theoretical probability:", theoretical_prob_above)
    print(
        "Difference between simulated and theoretical probability:",
        prob_above - theoretical_prob_above,
    )

    output_directory = Path(__file__).resolve().parent / 'outputs' / 'figures' / 'version_0_1'
    output_directory.mkdir(parents=True, exist_ok=True)

    x_start = mean - 4 * std
    x_end = mean + 4 * std
    step = (x_end - x_start) / 400
    x = [x_start + i * step for i in range(401)]
    y = [distribution.pdf(value) for value in x]

    plt.hist(samples, bins=50, density=True, alpha=0.7, label='Simulated')
    plt.plot(x, y, label='Theoretical')
    plt.axvline(threshold, color='red', linestyle='--', label=f'Threshold ({threshold})')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Distribution of Simulated Samples')
    plt.legend()
    figure_path = output_directory / 'histogram.png'
    plt.savefig(figure_path, dpi=300, bbox_inches='tight')
    print(f'Histogram saved to: {figure_path}')
    plt.show()
    plt.close()

    sorted_samples = sorted(samples)
    empirical_cdf = [
        (index + 1) / len(sorted_samples)
        for index in range(len(sorted_samples))
    ]
    theoretical_cdf = [distribution.cdf(value) for value in x]

    plt.step(sorted_samples, empirical_cdf, where='post', label='Simulated')
    plt.plot(x, theoretical_cdf, label='Theoretical')
    plt.axvline(threshold, color='red', linestyle='--', label=f'Threshold ({threshold})')
    plt.scatter(threshold, distribution.cdf(threshold), color='red', zorder=3)
    plt.xlabel('Value')
    plt.ylabel('Cumulative probability')
    plt.title('Cumulative Distribution of Simulated Samples')
    plt.ylim(0, 1.02)
    plt.legend()
    cdf_path = output_directory / 'cdf.png'
    plt.savefig(cdf_path, dpi=300, bbox_inches='tight')
    print(f'CDF saved to: {cdf_path}')
    plt.show()
    plt.close()

    simulation_counts = list(range(1, len(samples) + 1))
    running_count_above = 0
    running_probabilities = []
    for count, sample in enumerate(samples, start=1):
        if sample > threshold:
            running_count_above += 1
        running_probabilities.append(running_count_above / count)

    for lower_limit, filename, title in [
        (0, 'convergence.png', 'Convergence of Threshold Probability Estimate'),
        (0.8, 'convergence_zoomed.png', 'Zoomed Convergence of Threshold Probability Estimate'),
    ]:
        plt.plot(simulation_counts, running_probabilities, label='Simulated estimate')
        plt.axhline(
            theoretical_prob_above,
            color='red',
            linestyle='--',
            label=f'Theoretical ({theoretical_prob_above:.3f})',
        )
        plt.xscale('log')
        plt.xlabel('Number of simulations')
        plt.ylabel('Estimated probability of exceeding threshold')
        plt.title(title)
        plt.ylim(lower_limit, 1.1)
        plt.legend()
        plot_path = output_directory / filename
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        print(f'{title} saved to: {plot_path}')
        plt.show()
        plt.close()

    return {
        'samples': samples,
        'summary_stats': summary_stats,
        'sample_mean': sample_mean,
        'sample_std': sample_std,
        'prob_above': prob_above,
        'prob_standard_error': prob_standard_error,
        'prob_confidence_interval': prob_confidence_interval,
        'theoretical_prob_above': theoretical_prob_above,
    }


if __name__ == '__main__':
    run_simulation()
    run_repeated_simulations()