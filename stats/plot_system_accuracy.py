import pickle
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# Load the statistics
with open("stats/model_verification_stats.pickle", "rb") as f:
    stats = pickle.load(f)

# Define a function to safely compute and plot KDEs
def safe_plot_kde(data, xs, color, label):
    if len(data) > 1:  # Ensure there are enough data points for KDE
        pdf = st.gaussian_kde(data).pdf(xs)
        plt.plot(xs, pdf, color=color, label=label)
    else:
        print(f"Not enough data for KDE: {label}")

# Registered users
correct_probs = stats["registered"]["accepted_probabilities"]
incorrect_probs = stats["registered"]["rejected_probabilities"]
xs = np.linspace(0, 1.0, 301)  # X-axis for the plots

plt.title("Registered users - Identification prediction probability distribution")
plt.xlim(0, 1.0)
safe_plot_kde(correct_probs, xs, "green", "Correct guesses")
safe_plot_kde(incorrect_probs, xs, "red", "Incorrect guesses")
plt.legend(loc="upper left")
plt.show()

# Unregistered users
accepted_probs = stats["unknown"]["accepted_probabilities"]
rejected_probs = stats["unknown"]["rejected_probabilities"]

plt.title("Unregistered users - Identification prediction probability distribution")
plt.xlim(0, 1.0)
safe_plot_kde(accepted_probs, xs, "green", "Accepted guesses")
safe_plot_kde(rejected_probs, xs, "red", "Rejected guesses")
plt.legend(loc="upper left")
plt.show()
