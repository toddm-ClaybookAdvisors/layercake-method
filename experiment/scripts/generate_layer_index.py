#!/usr/bin/env python3
"""
Layer Index Generator - Version 3.0
Based on real-world git log analysis and actual commit patterns.
Handles all edge cases discovered through manual parsing.
"""
import os
import re
import json
import subprocess
from datetime import datetime

OUTPUT_PATH = "experiment/LAYER_INDEX.md"

def get_commits():
    """Get all commits with their SHA, subject, body, and commit date."""
    # Get commits with date included - use ISO format for consistency
    log_format = "%H|%ad|%s"
    result = subprocess.run(
        ["git", "log", "--reverse", "--date=short", "--pretty=format:" + log_format],
        capture_output=True, text=True, check=True
    )
    
    commits = []
    for line in result.stdout.strip().split('\n'):
        if '|' not in line:
            continue
            
        parts = line.split('|', 2)
        if len(parts) < 3:
            continue
            
        sha = parts[0]
        date = parts[1]  # This will be in YYYY-MM-DD format
        subject = parts[2]
        
        # Get body separately
        body_result = subprocess.run(
            ["git", "log", "--format=%b", "-1", sha],
            capture_output=True, text=True, check=True
        )
        body = body_result.stdout.strip()
        
        commits.append({
            "sha": sha, 
            "subject": subject, 
            "body": body,
            "date": date
        })
    
    return commits

def extract_layer_json(commit):
    """Extract JSON block from the commit message."""
    match = re.search(r"(\{[\s\S]+\})", commit["body"])
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
        return data
    except Exception:
        return None

def parse_layer_and_duration(subject, full_message=None):
    """
    Extract layer number and duration from commit using real-world patterns.
    Based on actual analysis of commit history.
    """
    subject = subject.strip()
    
    # Pattern 1: [XXXX](duration) - Modern format
    match = re.search(r"\[(\d{1,5})\](?:\(([^)]+)\))?", subject)
    if match:
        layer = match[1].zfill(4)
        duration = match[2] if match[2] else ""
        return layer, duration, subject
    
    # Pattern 2: Layer XXXX: - Legacy format  
    match = re.search(r"Layer\s+(\d{1,5})[:\-]", subject, re.IGNORECASE)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 3: XXXX: at start - Like "0034: Add invisible..."
    match = re.match(r"(\d{1,5}):\s+", subject)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 4: (prompt XXXX) anywhere
    match = re.search(r"\(prompt\s+(\d{1,5})\)", subject, re.IGNORECASE)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 5: prompt XXXX anywhere
    match = re.search(r"prompt\s+(\d{1,5})", subject, re.IGNORECASE)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 6: #XXXX anywhere
    match = re.search(r"#(\d{1,5})", subject)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 7: debug-XXXX anywhere
    match = re.search(r"debug-(\d{4})", subject)
    if match:
        layer = match[1].zfill(4)
        return layer, "", subject
    
    # Pattern 8: Single number in subject (conservative)
    numbers = re.findall(r'\b(\d{1,4})\b', subject)
    if len(numbers) == 1:
        num = int(numbers[0])
        if 1 <= num <= 100:  # Conservative range for single numbers
            layer = str(num).zfill(4)
            return layer, "", subject
    
    # Search in full message body if not found in subject
    if full_message:
        # Try all the same patterns in the body
        body_patterns = [
            r"Layer\s+(\d{1,5})",
            r"\((\d{4})\)",  # (0035) format
            r"Version:\s*(\d{1,5})",
            r"debug-(\d{4})",
            r"devlog-(\d{4})",
            r"transition-(\d{3})",
        ]
        
        for pattern in body_patterns:
            match = re.search(pattern, full_message, re.IGNORECASE)
            if match:
                layer = match[1].zfill(4)
                return layer, "", subject
    
    return None, "", subject

def extract_date_from_commit(commit_text):
    """Extract date from git log format."""
    # Look for Date: line in commit
    match = re.search(r"Date:\s+\w+\s+(\w+\s+\d+)", commit_text)
    if match:
        return match[1]
    return ""

def build_index(commits):
    """Build the layer index markdown."""
    entries = []
    
    for c in commits:
        # Get commit date from git log output  
        commit_text = f"commit {c['sha']}\nDate: {c.get('date', '')}\n{c['subject']}\n{c['body']}"
        
        # Parse layer info
        full_message = c["subject"] + "\n" + c["body"] if c["body"] else c["subject"]
        layer, duration, summary = parse_layer_and_duration(c["subject"], full_message)
        layer_str = layer if layer else "N/A"

        # Check for JSON metadata
        json_data = extract_layer_json(c)
        date = c.get('date', '')     # ← THIS IS THE FIX
        json_ref = ""
        json_block = None
        
        if json_data and "layer" in json_data:
            # Use JSON data if available
            layer = str(json_data.get("layer", layer_str)).zfill(4) if json_data.get("layer") else layer_str
            duration = json_data.get("duration", duration)
            summary = json_data.get("summary", summary)
            date = json_data.get("timestamp_start", "")[:10] if json_data.get("timestamp_start") else ""
            json_ref = f"#{layer}-json" if layer != "N/A" else ""
            json_block = json_data
        
        # Build devlog path only if file actually exists
        devlog = ""
        if layer and layer != "N/A":
            # Script runs from project root, devlog files have no .md extension
            devlog_path = f"experiment/devlog/devlog-{layer}"
            file_exists = os.path.exists(devlog_path)
            # Debug: print path checking for first few layers
            if layer in ['0038', '0037', '0036', '0001', '0002']:
                print(f"Checking layer {layer}: path='{devlog_path}', exists={file_exists}")
            if file_exists:
                devlog = devlog_path
        
        entries.append({
            "layer": layer_str,
            "duration": duration,
            "date": date,
            "summary": summary[:45] + "..." if len(summary) > 45 else summary,
            "full_summary": summary,
            "sha": c["sha"],
            "devlog": devlog,
            "json_ref": json_ref,
            "json_block": json_block
        })

    # Sort: highest layer first, N/A at bottom
    def sort_key(e):
        if e["layer"] == "N/A":
            return -1
        try:
            return int(e["layer"])
        except:
            return 0
    
    entries.sort(key=sort_key, reverse=True)

    # Generate markdown
    md = [
        "# LAYER_INDEX.md",
        "",
        "This index provides a layer-by-layer audit trail for the entire experiment.",
        "",
        "| Layer | Duration | Date       | Summary                                         | Commit SHA  | Devlog        | Protocol/Meta |",
        "|-------|----------|------------|-------------------------------------------------|-------------|---------------|---------------|"
    ]

    # Table rows
    for e in entries:
        sha_short = e['sha'][:7]
        # Use relative GitHub links that work when viewing on GitHub
        # LAYER_INDEX.md is at experiment/LAYER_INDEX.md, so need to go up to repo root
        sha_url = f"[{sha_short}](../../../commit/{e['sha']})"
        devlog_link = f"[{os.path.basename(e['devlog'])}]({e['devlog']})" if e['devlog'] else ""
        # Make JSON link relative to GitHub as well
        json_link = f"[JSON]({e['json_ref']})" if e['json_ref'] else ""
        
        # Ensure consistent spacing and no weird paths
        layer_col = f"{e['layer']:>05}"
        duration_col = f"{e['duration']:<8}"
        date_col = f"{e['date']:<10}"
        summary_col = f"{e['summary']:<47}"
        
        md.append(f"| {layer_col} | {duration_col} | {date_col} | {summary_col} | {sha_url} | {devlog_link} | {json_link} |")

    # JSON blocks section - remove since we're linking to GitHub instead
    # md.append("\n---\n\n## Layer JSON Blocks\n")
    # for e in entries:
    #     if e["json_block"]:
    #         md.append(f"### {e['layer']}")
    #         md.append("\n```json")
    #         md.append(json.dumps(e["json_block"], indent=2))
    #         md.append("```\n")

    return "\n".join(md)

def main():
    print("Getting commits...")
    commits = get_commits()
    print(f"Found {len(commits)} commits")
    
    # Debug: Print first few commits to verify date extraction
    print("\nFirst 5 commits:")
    for commit in commits[:5]:
        print(f"  {commit['sha'][:7]} | '{commit['date']}' | {commit['subject'][:50]}...")
    
    print("\nLast 5 commits:")
    for commit in commits[-5:]:
        print(f"  {commit['sha'][:7]} | '{commit['date']}' | {commit['subject'][:50]}...")
    
    # Check for any empty dates
    empty_dates = [c for c in commits if not c['date']]
    if empty_dates:
        print(f"\nWARNING: {len(empty_dates)} commits have empty dates")
        for c in empty_dates[:3]:
            print(f"  {c['sha'][:7]} | EMPTY | {c['subject'][:50]}...")
    else:
        print("\nAll commits have dates!")
    
    print("\nBuilding index...")
    md = build_index(commits)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(md)
    
    print(f"LAYER_INDEX.md generated with {len(commits)} commits.")

if __name__ == "__main__":
    main()