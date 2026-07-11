#!/usr/bin/env python3
"""
Convert all .txt files to .md files inside the scriptures folder
"""

import os
from pathlib import Path

def convert_txt_to_md(base_path="scriptures"):
    base = Path(base_path)
    
    if not base.exists():
        print(f"❌ Folder '{base_path}' not found!")
        return

    converted = 0
    skipped = 0

    for txt_file in base.rglob("*.txt"):
        md_file = txt_file.with_suffix(".md")
        
        # Skip if .md already exists
        if md_file.exists():
            print(f"⏭️  Skipping (already exists): {md_file}")
            skipped += 1
            continue

        # Read content
        with open(txt_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Optional: Make first line a heading (if it looks like a title)
        lines = content.strip().split("\n", 1)
        if lines and len(lines[0]) < 120:  # Avoid converting very long first lines
            content = f"# {lines[0]}\n\n" + (lines[1] if len(lines) > 1 else "")

        # Write to .md file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)

        # Delete original .txt file (optional - comment out if you want to keep both)
        txt_file.unlink()

        print(f"✅ Converted: {txt_file.name} → {md_file.name}")
        converted += 1

    print(f"\n🎉 Done! Converted {converted} files.")
    if skipped > 0:
        print(f"⏭️  Skipped {skipped} files (already had .md version)")


if __name__ == "__main__":
    convert_txt_to_md("scriptures")