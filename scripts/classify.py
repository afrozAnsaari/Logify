from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm
import pandas as pd
from pathlib import Path


def classify(logs: list[tuple[str, str]]) -> list[str]:
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels


def classify_log(source: str, log_msg: str) -> str | None:
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if label is None:
            label = classify_with_bert(log_msg)
    return label


def classify_with_csv(input_path: Path, output_csv_path: Path):
    try:
        df = pd.read_csv(input_path)
    except Exception:
        print(f"Failed to open file at path:{input_path}...\n")
        return

    df["target_label"] = classify(tuple(zip(df["source"], df["log_message"])))

    try:
        df.to_csv(output_csv_path, index=False)
        print(f"Output file created at: {output_csv_path}\n")
    except Exception:
        print("Task failed...\n")
        return


if __name__ == "__main__":
    input_file_name = "test.csv"
    output_file_name = "output.csv"
    BASE_DIR = Path(__file__).resolve().parent
    input_csv_path = BASE_DIR / "resources" / input_file_name
    output_csv_path = BASE_DIR / "resources" / output_file_name
    classify_with_csv(input_csv_path, output_csv_path)
