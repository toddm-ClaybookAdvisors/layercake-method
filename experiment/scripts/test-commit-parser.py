import re

def parse_layer_and_duration(subject, full_message=None):
    """
    Extract layer number and duration from commit subject or full commit message.
    Handles patterns like:
    [0009](45m) This is a summary
    [0010] Another summary
    [12](30m) Foo
    [13] Bar
    Layer 12: ...
    layer 0042 - something
    12: Legacy summary
    13 - Old layer format
    
    For older commits, if no layer found in subject, searches the full message
    for any number which is likely the layer number.
    
    Args:
        subject (str): The commit subject/title
        full_message (str, optional): The full commit message including body
    
    Returns:
        layer (str or None), duration (str or ""), summary (str)
    """
    # Strip leading/trailing whitespace
    subject = subject.strip()
    
    # Try [layer](duration) summary or [layer] summary
    m = re.match(r"\[(\d{1,5})\](?:\(([^)]+)\))?\s*(.*)", subject)
    if m:
        layer = m.group(1).zfill(4)  # Zero-pad to 4 digits for consistency
        duration = m.group(2) if m.group(2) else ""
        summary = m.group(3).strip()
        return layer, duration, summary
    
    # Try 'Layer XX:' or 'layer XX:' pattern (with optional dash)
    m = re.match(r"[Ll]ayer\s+(\d{1,5})[:\-]\s*(.*)", subject)
    if m:
        layer = m.group(1).zfill(4)
        duration = ""
        summary = m.group(2).strip()
        return layer, duration, summary
    
    # Try 'layer XX -' or 'layer XX ' pattern (without colon)
    m = re.match(r"[Ll]ayer\s+(\d{1,5})\s+[-]?\s*(.*)", subject)
    if m:
        layer = m.group(1).zfill(4)
        duration = ""
        summary = m.group(2).strip()
        return layer, duration, summary
    
    # Try just 'XX:' or 'XX -' patterns at the start
    m = re.match(r"(\d{1,5})[:\-]\s+(.*)", subject)
    if m:
        layer = m.group(1).zfill(4)
        duration = ""
        summary = m.group(2).strip()
        return layer, duration, summary
    
    # Try standalone number at the beginning (less strict)
    m = re.match(r"(\d{1,5})\s+(.*)", subject)
    if m:
        layer = m.group(1).zfill(4)
        duration = ""
        summary = m.group(2).strip()
        return layer, duration, summary
    
    # If no layer found in subject and we have full message, search there
    if full_message and full_message.strip() != subject.strip():
        layer_from_body = extract_layer_from_message_body(full_message)
        if layer_from_body:
            return layer_from_body.zfill(4), "", subject
    
    # Fallback: No match
    return None, "", subject

def extract_layer_from_message_body(full_message):
    """
    Extract layer number from full commit message body.
    Looks for patterns like:
    - Layer 42
    - layer 123
    - Any standalone number that's likely a layer
    """
    # First try explicit "layer" patterns in the full message
    layer_patterns = [
        r"[Ll]ayer\s+(\d{1,5})",
        r"Layer:\s*(\d{1,5})",
        r"layer:\s*(\d{1,5})",
    ]
    
    for pattern in layer_patterns:
        m = re.search(pattern, full_message)
        if m:
            return m.group(1)
    
    # If no explicit layer pattern, look for standalone numbers
    # This is more aggressive - finds any number that could be a layer
    numbers = re.findall(r'\b(\d{1,5})\b', full_message)
    
    # Filter out obviously non-layer numbers
    likely_layers = []
    for num in numbers:
        num_int = int(num)
        # Reasonable layer number range (adjust as needed)
        if 1 <= num_int <= 9999:
            likely_layers.append(num)
    
    # Return the first reasonable number found
    # You might want to adjust this logic based on your specific needs
    if likely_layers:
        return likely_layers[0]
    
    return None

# Test function to verify it works
def test_parser():
    """Test the parser with various commit message formats"""
    test_cases = [
        # (subject, full_message)
        ("[0009](45m) This is a summary", None),
        ("[0010] Another summary", None), 
        ("[12](30m) Foo", None),
        ("[13] Bar", None),
        ("Layer 12: some description", None),
        ("layer 0042 - something", None),
        ("12: Legacy summary", None),
        ("13 - Old layer format", None),
        ("Layer 5 some text", None),
        ("layer 99 - description", None),
        ("42 something here", None),
        ("No layer info here", None),
        ("  [0001](10m) Leading spaces  ", None),
        ("Layer 123: Multiple words in summary", None),
        # Test cases with full message body
        ("Fix bug in authentication", "This commit fixes the authentication bug\nLayer 15\nSome other details"),
        ("Update documentation", "Updated the docs\n\nThis is for layer 42\nMore text here"),
        ("Refactor code", "Major refactor\n\nSome details about the change\nThis addresses issue 123 for the system"),
        ("Old commit format", "This is an old commit message\nwith layer: 7\nand some other info"),
        ("Another old format", "Fixed something important\nLayer: 99\nDone"),
    ]
    
    for subject, full_msg in test_cases:
        layer, duration, summary = parse_layer_and_duration(subject, full_msg)
        print(f"Subject: '{subject}'")
        if full_msg:
            print(f"Full message: '{full_msg}'")
        print(f"  Layer: {layer}, Duration: '{duration}', Summary: '{summary}'")
        print()

if __name__ == "__main__":
    test_parser()