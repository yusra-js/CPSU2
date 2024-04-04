import numpy as np
import pandas as pd
import psycopg2
from collections import Counter


#حساب الموزنة 

class Node:
    def init(self, data=None, attribute=None, value=None, results=None, true_branch=None, false_branch=None):
        self.data = data  # Data points in the node
        self.attribute = attribute  # Attribute used for splitting
        self.value = value  # Value used for splitting
        self.results = results  # Class labels for leaf nodes
        self.true_branch = true_branch  # Subtree for true branch
        self.false_branch = false_branch  # Subtree for false branch

def entropy(data):

    """Calculate entropy of a dataset."""
    labels = data[:, -1]
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return -np.sum(probabilities * np.log2(probabilities + 1e-10))
	

def information_gain(data, attribute, value):

    """Calculate information gain for a split."""
    subset_true = data[data[:, attribute] == value]
    subset_false = data[data[:, attribute] != value]

    p_true = len(subset_true) / len(data)
    p_false = len(subset_false) / len(data)

    gain = entropy(data) - (p_true * entropy(subset_true) + p_false * entropy(subset_false))
    return gain

def find_best_split(data):

    """Find the best attribute and value to split on."""
    num_attributes = data.shape[1] - 1  # Exclude the class label column
    best_gain = 0
    best_attribute = None
    best_value = None

    for attribute in range(num_attributes):
        values = np.unique(data[:, attribute])
        for value in values:
            gain = information_gain(data, attribute, value)
            if gain > best_gain:
                best_gain = gain
                best_attribute = attribute
                best_value = value

    return best_attribute, best_value

def build_tree(data):
    """Recursively build the decision tree."""
    if len(np.unique(data[:, -1])) == 1:

        # If all instances have the same class, create a leaf node
        return Node(data=data, results=Counter(data[:, -1]))

    best_attribute, best_value = find_best_split(data)

    if best_attribute is None:
        # If no split improves information gain, create a leaf node
        return Node(data=data, results=Counter(data[:, -1]))

    subset_true = data[data[:, best_attribute] == best_value]
    subset_false = data[data[:, best_attribute] != best_value]

    true_branch = build_tree(subset_true)
    false_branch = build_tree(subset_false)

    return Node(data=data, attribute=best_attribute, value=best_value, true_branch=true_branch, false_branch=false_branch)

def predict(tree, instance):
    """Make a prediction for a single instance."""
    if tree.results is not None:
        return tree.results.most_common(1)[0][0]

    branch = tree.false_branch
    if instance[tree.attribute] == tree.value:
        branch = tree.true_branch

    return predict(branch, instance)

def load_data_from_database():
    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="12345",
        database="CPSU"
    )

    # Replace 'your_table_name' with the actual name of your table
    query = 'SELECT * FROM your_table_name;'
    
    # Execute the query and fetch the results
    data = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    return data.values  # Convert dataframe to numpy array

# Example usage:
data = load_data_from_database()
decision_tree = build_tree(data)

# Make predictions for a test instance "test"
test_instance = np.array(['type1', 'male', 'NY', 'A'])  # Replace with your test instance
prediction = predict(decision_tree, test_instance)
print("Prediction:", prediction)
