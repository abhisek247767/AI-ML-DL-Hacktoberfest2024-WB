//C++ Code Implementation for Decision Tree:
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

// A struct to represent a node in the decision tree
struct Node {
    string feature;
    string label;
    map<string, Node*> children;
    bool isLeaf;

    Node() : isLeaf(false) {}
};

// Function to calculate Gini impurity of a dataset
double calculateGini(const vector<pair<string, vector<string>>>& dataset) {
    map<string, int> classCounts;
    for (const auto& data : dataset) {
        classCounts[data.first]++;
    }

    double gini = 1.0;
    int totalSamples = dataset.size();
    for (const auto& classCount : classCounts) {
        double prob = (double)classCount.second / totalSamples;
        gini -= prob * prob;
    }

    return gini;
}

// Function to split the dataset based on a feature and its value
vector<pair<string, vector<string>>> splitDataset(const vector<pair<string, vector<string>>>& dataset, int featureIndex, const string& value) {
    vector<pair<string, vector<string>>> subset;
    for (const auto& data : dataset) {
        if (data.second[featureIndex] == value) {
            subset.push_back(data);
        }
    }
    return subset;
}

// Function to get unique values of a feature
set<string> getUniqueValues(const vector<pair<string, vector<string>>>& dataset, int featureIndex) {
    set<string> values;
    for (const auto& data : dataset) {
        values.insert(data.second[featureIndex]);
    }
    return values;
}

// Function to find the best feature to split on based on Gini impurity
int findBestFeature(const vector<pair<string, vector<string>>>& dataset) {
    int bestFeatureIndex = -1;
    double bestGini = 1.0;

    for (int i = 0; i < dataset[0].second.size(); i++) {
        double weightedGini = 0.0;

        set<string> uniqueValues = getUniqueValues(dataset, i);
        for (const string& value : uniqueValues) {
            vector<pair<string, vector<string>>> subset = splitDataset(dataset, i, value);
            double subsetGini = calculateGini(subset);
            weightedGini += (double)subset.size() / dataset.size() * subsetGini;
        }

        if (weightedGini < bestGini) {
            bestGini = weightedGini;
            bestFeatureIndex = i;
        }
    }

    return bestFeatureIndex;
}

// Function to build the decision tree
Node* buildTree(const vector<pair<string, vector<string>>>& dataset, const vector<string>& featureNames) {
    // Check if all samples belong to the same class
    set<string> uniqueClasses;
    for (const auto& data : dataset) {
        uniqueClasses.insert(data.first);
    }

    // If only one class is left, create a leaf node
    if (uniqueClasses.size() == 1) {
        Node* leafNode = new Node();
        leafNode->label = dataset[0].first;
        leafNode->isLeaf = true;
        return leafNode;
    }

    // Find the best feature to split the dataset
    int bestFeatureIndex = findBestFeature(dataset);
    if (bestFeatureIndex == -1) {
        return nullptr; // No valid split found
    }

    // Create the root node for this subtree
    Node* root = new Node();
    root->feature = featureNames[bestFeatureIndex];

    // Recursively build subtrees for each unique value of the best feature
    set<string> uniqueValues = getUniqueValues(dataset, bestFeatureIndex);
    for (const string& value : uniqueValues) {
        vector<pair<string, vector<string>>> subset = splitDataset(dataset, bestFeatureIndex, value);
        root->children[value] = buildTree(subset, featureNames);
    }

    return root;
}

// Function to classify a new sample using the decision tree
string classify(Node* tree, const vector<string>& sample, const vector<string>& featureNames) {
    if (tree->isLeaf) {
        return tree->label;
    }

    // Find the index of the feature in the feature names
    int featureIndex = distance(featureNames.begin(), find(featureNames.begin(), featureNames.end(), tree->feature));

    // Traverse to the corresponding child node based on the feature value
    string featureValue = sample[featureIndex];
    if (tree->children.count(featureValue)) {
        return classify(tree->children[featureValue], sample, featureNames);
    } else {
        return "Unknown"; // Unknown feature value
    }
}

int main() {
    // Dataset: Each sample is {class, {feature1, feature2, ...}}
    vector<pair<string, vector<string>>> dataset = {
        {"No", {"Sunny", "Hot", "High", "Weak"}},
        {"No", {"Sunny", "Hot", "High", "Strong"}},
        {"Yes", {"Overcast", "Hot", "High", "Weak"}},
        {"Yes", {"Rain", "Mild", "High", "Weak"}},
        {"Yes", {"Rain", "Cool", "Normal", "Weak"}},
        {"No", {"Rain", "Cool", "Normal", "Strong"}},
        {"Yes", {"Overcast", "Cool", "Normal", "Strong"}},
        {"No", {"Sunny", "Mild", "High", "Weak"}},
        {"Yes", {"Sunny", "Cool", "Normal", "Weak"}},
        {"Yes", {"Rain", "Mild", "Normal", "Weak"}},
    };

    vector<string> featureNames = {"Outlook", "Temperature", "Humidity", "Wind"};

    // Build the decision tree
    Node* decisionTree = buildTree(dataset, featureNames);

    // Classify a new sample
    vector<string> newSample = {"Sunny", "Cool", "High", "Strong"};
    string result = classify(decisionTree, newSample, featureNames);

    cout << "The class of the new sample is: " << result << endl;

    return 0;
}
