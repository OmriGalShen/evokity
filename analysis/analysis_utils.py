import matplotlib.pyplot as plt
from matplotlib import cm


class TestOperatorWrapper:
    def __init__(self, label, test_class):
        self.label = label
        self.test_operator = test_class
        self.result = None


def display_results(test_operators, repeats, x_label, title):
    test_operators.sort(key=lambda x: x.result)
    labels = [x.label for x in test_operators]
    values = [x.result for x in test_operators]
    fig, ax = plt.subplots()
    colors = cm.tab20c.colors
    colors = colors[:len(values)]
    ax.bar(labels, values, label=labels)
    ax.set_ylabel(f'Average generations (repeats={repeats})')
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.bar(labels, values, color=colors[:len(values)])
    fig.autofmt_xdate()
    plt.show()
