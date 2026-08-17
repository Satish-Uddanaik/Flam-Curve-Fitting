import matplotlib.pyplot as plt


def plot_results(x_actual, y_actual, x_pred, y_pred):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        x_actual,
        y_actual,
        s=8,
        color="blue",
        label="Actual Data"
    )

    plt.plot(
        x_pred,
        y_pred,
        color="red",
        linewidth=2,
        label="Predicted Curve"
    )

    plt.title("Curve Fitting Result")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig("../output/final_result.png", dpi=300)

    plt.show()