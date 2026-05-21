# 🔬 Computational Physics & Algorithms Archive

Welcome to this repository! This collection represents an evolving archive of my projects related to **Computational Physics**, **Numerical Methods**, and the study of **Data Structures and Algorithms**.

The codes here range from simulating complex physical systems (molecular dynamics, statistical mechanics, electromagnetism) to optimizing classic algorithmic problems, with a strong focus on computational efficiency.

## 📂 Project Overview

The repository is divided into three main macro-areas:

### 1. Molecular Dynamics and Computational Physics
This section contains simulations based on rigorous physical principles, developed to model the behavior of matter at both microscopic and macroscopic levels.
* **`Lennard Jones`**: A physics engine for simulating crystal formation. It models the interaction between atoms using the Lennard-Jones potential. It implements the *Velocity Verlet* integration algorithm for proper energy conservation, force cut-off logic, and spatial boundary (bounce) conditions. Animations are rendered using Matplotlib/FFmpeg.
* **`Ising`**: Implementation of the Ising model to study phase transitions and ferromagnetism in statistical mechanics.
* **`Statistica Maxwell-Boltzmann`**: Simulation and experimental verification of the particle velocity distribution in an ideal gas.
* **`Campo Elettrico` & `Radioattività`** (Electric Field & Radioactivity): Numerical models to visualize vector fields and simulate radioactive decay curves.

### 2. Numerical Methods, Statistics, and Dynamical Systems
A collection of scripts applying mathematical and probabilistic concepts to dynamic scenarios.
* **`Montecarlo`**: Algorithms based on statistical sampling for calculating integrals or solving complex physical problems.
* **`Random Walk`**: Simulation of "Brownian motion" (random walk) in various dimensions.
* **`Metodi normali`** (Normal Modes): Study of normal modes of oscillation for coupled systems.
* **Kinematic Simulations (`Palla rimbalzante`, `Ruota`, `Orologio`)**: Practical applications of equations of motion to recreate interactive mechanical systems.

### 3. Advanced Algorithms and Problem Solving (LeetCode)
This section is dedicated to pure optimization and the study of time complexity (Big-O Notation).
* **`Leet code`**: Optimized solutions to classic problems. It features the transition from "brute force" (O(N²)) approaches to advanced solutions:
  * Using **Hash Maps (Dictionaries)** to solve problems like *Two Sum* in linear O(N) time.
  * **Two Pointers** techniques for merging arrays and efficiently exploring strings (e.g., *Longest Common Prefix*).
  * **Binary Search** for complex problems like finding the median of sorted arrays in logarithmic O(log(N+M)) time.
* **`Commesso`** (Traveling Salesperson): Approaches to solving the classic TSP (Traveling Salesperson Problem) and optimal path analysis.
* **`Numeri primi`** (Prime Numbers): Efficient generation and verification of prime number sequences (e.g., Sieve of Eratosthenes).

## 🛠️ Technologies Used
* **Primary Language:** `Python 3`
* **Scientific Computing:** `NumPy` (for vectorized computation and optimized linear algebra)
* **Data Visualization & Animations:** `Matplotlib`, `FFmpegWriter` / `PillowWriter`

## 🚀 How to Run the Simulations
To run the codes in this repository, it is recommended to use a virtual environment (e.g., Anaconda or venv). 

Make sure you have the main libraries installed:
```bash
'pip install numpy matplotlib'

