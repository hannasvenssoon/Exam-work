import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


LINE_RE = re.compile(
    r"TS:(?P<ts>[\d\.]+),"
    r"GT:(?P<gt>[a-z]+),"
    r"PRED:(?P<pred>[A-Z]+),"
    r"LAT:(?P<lat>[\d\.]+)"
)

LABEL_MAP = {
    "lying": 0,
    "standing": 1,
    "moving": 2
}

LABEL_NAMES = ["lying", "standing", "moving"]
LABELS = [0, 1, 2]  


def parse_file(path):
    ts, gt, pred, lat = [], [], [], []

    with open(path, "r") as f:
        for line in f:
            m = LINE_RE.search(line)
            if not m:
                continue  # skip Throughput etc

            ts.append(float(m["ts"]))

            gt_label = m["gt"].lower()
            pred_label = m["pred"].lower()

            gt.append(LABEL_MAP[gt_label])
            pred.append(LABEL_MAP[pred_label])

            lat.append(float(m["lat"]))

    return (
        np.array(ts),
        np.array(gt),
        np.array(pred),
        np.array(lat)
    )



def print_metrics(name, y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    f1_macro = f1_score(y_true, y_pred, average="macro", labels=LABELS)
    f1_weighted = f1_score(y_true, y_pred, average="weighted", labels=LABELS)
    cm = confusion_matrix(y_true, y_pred, labels=LABELS)

    print(f"\n{name}")
    print(f"Accuracy     : {acc:.4f}")
    print(f"F1 macro     : {f1_macro:.4f}")
    print(f"F1 weighted  : {f1_weighted:.4f}")
    print("Confusion matrix:")
    print(cm)

    return cm


def print_latency(name, lat):
    print(f"{name} latency:")
    print(f"  Mean : {np.mean(lat):.3f} ms")
    print(f"  Std  : {np.std(lat):.3f} ms")


def print_throughput(name, ts):
    if len(ts) < 2:
        print(f"{name} throughput: N/A")
        return

    dt = np.diff(ts)
    throughput = 1.0 / np.mean(dt)

    print(f"{name} throughput:")
    print(f"  Mean : {throughput:.2f} inf/s")


def plot_confusion_matrix(cm, title, filename):
    plt.figure(figsize=(5, 4))
    im = plt.imshow(cm, cmap="Blues")
    plt.title(title)
    plt.xlabel("Predicted label")
    plt.ylabel("True label")

    plt.xticks(range(len(LABEL_NAMES)), LABEL_NAMES)
    plt.yticks(range(len(LABEL_NAMES)), LABEL_NAMES)

    plt.colorbar(im, fraction=0.046, pad=0.04)

    thresh = cm.max() / 2.0
    for i in range(len(LABEL_NAMES)):
        for j in range(len(LABEL_NAMES)):
            plt.text(
                j, i, cm[i, j],
                ha="center",
                va="center",
                color="white" if cm[i, j] > thresh else "black",
                fontsize=11
            )

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()



ts, gt, pred, lat = parse_file("edge_evaluation_2026-01-26_13-26-30.txt")

cm = print_metrics("CNN Edge Inference", gt, pred)
print_latency("CNN Edge", lat)
print_throughput("CNN Edge", ts)

plot_confusion_matrix(
    cm,
    title="Confusion Matrix CNN",
    filename="cnn_confusion_edge_simple.png"
)