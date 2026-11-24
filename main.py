import os

# One-star review, written by the cat. Deadpan review shape, feline complaint.
LINE = "One star. The door was closed, so I screamed. He opened it. I left. Would not recommend this human."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
