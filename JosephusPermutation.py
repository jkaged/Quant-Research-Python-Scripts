# Sample code #1 of the Josephus Permutation
# This problem combines recursive thinking, modular arithmetic, 
# and efficient coding—making it an excellent practice problem for programmers.

def josephus(n, k):
    """Returns the position of the last person in the Josephus problem."""
    if n == 1:
        return 1
    else:
        # Recursively calculate the position
        return (josephus(n - 1, k) + k - 1) % n + 1

# Example usage
n = 7  # Number of people
k = 3  # Step size
survivor = josephus(n, k)
print(f"The survivor is at position: {survivor}")

# Sample code #2 of the Josephus Permutation for larger inputs
def josephus_iterative(n, k):
    """Returns the position of the last person using an iterative approach."""
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1

# Example usage
survivor = josephus_iterative(n, k)
print(f"The survivor is at position: {survivor}")
