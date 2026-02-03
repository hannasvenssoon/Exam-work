import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


LINE_RE = re.compile(
    r"TS:(?P<ts>[\d\.]+),GT:(?P<gt>\d),PRED:(?P<pred>\d),LAT:(?P<lat>[\d\.]+)"
)

LABELS = [0, 1]  # 0 = Normal, 1 = Abnormal


def parse_file(path):
    ts, gt, pred, lat = [], [], [], []

    with open(path, "r") as f:
        for line in f:
            m = LINE_RE.search(line)
            if not m:
                continue
            ts.append(float(m["ts"]))
            gt.append(int(m["gt"]))
            pred.append(int(m["pred"]))
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
    plt.xticks([0, 1], ["normal", "abnormal"])
    plt.yticks([0, 1], ["normal", "abnormal"])

    plt.colorbar(im, fraction=0.046, pad=0.04)

    thresh = cm.max() / 2.0
    for i in range(2):
        for j in range(2):
            plt.text(
                j, i, cm[i, j],
                ha="center",
                va="center",
                color="white" if cm[i, j] > thresh else "black",
                fontsize=12
            )

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


ts_norm, gt_norm, pred_norm, lat_norm = parse_file("test_accuracy_cnn_normal.txt")
ts_abn,  gt_abn,  pred_abn,  lat_abn  = parse_file("test_accuracy_cnn_vib.txt")

ts_all   = np.concatenate([ts_norm, ts_abn])
gt_all   = np.concatenate([gt_norm, gt_abn])
pred_all = np.concatenate([pred_norm, pred_abn])
lat_all  = np.concatenate([lat_norm, lat_abn])


cm_all = print_metrics("CNN Merged tests", gt_all, pred_all)
print_latency("CNN merged", lat_all)
print_throughput("CNN merged", ts_all)

plot_confusion_matrix(
    cm_all,
    title="Confusion Matrix CNN",
    filename="cnn_confusion_merged.png"
)


cm_norm = confusion_matrix(gt_norm, pred_norm, labels=LABELS)

print("\nNormal test")
fp = np.sum((gt_norm == 0) & (pred_norm == 1))
print(f"False positive rate: {fp / len(gt_norm):.4f}")
print_latency("Normal test", lat_norm)
print_throughput("Normal test", ts_norm)

plot_confusion_matrix(
    cm_norm,
    title="Confusion Matrix CNN (Normal test)",
    filename="cnn_confusion_normal.png"
)


cm_abn = confusion_matrix(gt_abn, pred_abn, labels=LABELS)

print("\nAbnormal test")
fn = np.sum((gt_abn == 1) & (pred_abn == 0))
print(f"False negative rate: {fn / len(gt_abn):.4f}")
print_latency("Abnormal test", lat_abn)
print_throughput("Abnormal test", ts_abn)

plot_confusion_matrix(
    cm_abn,
    title="Confusion Matrix CNN (Abnormal test)",
    filename="cnn_confusion_abnormal.png"
)


print("\nConfusion matrix plots saved:")
print("cnn_confusion_merged.png")
print("cnn_confusion_normal.png")
print("cnn_confusion_abnormal.png")
