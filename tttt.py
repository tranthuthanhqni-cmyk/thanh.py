#!/usr/bin/env python3
"""
Simplified Parsing Example - Works with Python 3.14
Demonstrates constituency and dependency tree concepts with manual parsing
"""

from nltk import Tree
import json

# Sample text with four types of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",  # Declarative
    "Is Python a programming language?",              # Interrogative  
    "Watch out for that obstacle!",                   # Imperative
    "I think that if you work hard, you will succeed in life."  # Complex
]

# Simplified manual parse trees for demonstration
parse_trees = {
    0: "(S (NP (DET The) (ADJ quick) (ADJ brown) (N fox)) (VP (V jumps) (PP (P over) (NP (DET the) (ADJ lazy) (N dog)))))",
    1: "(SQ (V Is) (NP (N Python)) (NP (DET a) (N programming) (N language)))",
    2: "(S (VP (V Watch) (P out)) (PP (P for) (NP (DET that) (N obstacle))))",
    3: "(S (NP (PRO I)) (VP (V think) (SBAR (IN that) (S (NP (PRO you)) (VP (V work) (ADV hard))))))"
}

# Simplified dependency relations
dependencies = {
    0: [
        ("fox", "nsubj", "jumps"),
        ("quick", "amod", "fox"),
        ("brown", "amod", "fox"),
        ("jumps", "ROOT", "jumps"),
        ("dog", "pobj", "over"),
        ("over", "prep", "jumps"),
        ("lazy", "amod", "dog"),
    ],
    1: [
        ("Python", "nsubj", "Is"),
        ("Is", "ROOT", "Is"),
        ("language", "attr", "Is"),
    ],
    2: [
        ("Watch", "ROOT", "Watch"),
        ("obstacle", "pobj", "for"),
        ("for", "prep", "Watch"),
    ],
    3: [
        ("I", "nsubj", "think"),
        ("think", "ROOT", "think"),
        ("work", "relcl", "think"),
        ("you", "nsubj", "work"),
        ("hard", "advmod", "work"),
    ]
}

def format_parse_tree(parse_string):
    """Format parse tree nicely"""
    # Add indentation
    tree_str = parse_string.replace("(", "(\n  ").replace(")", "\n)")
    return tree_str

def generate_dependency_html(deps, sentence_num):
    """Generate a simple HTML visualization of dependencies"""
    html = '<svg width="100%" height="200" style="background: #f9f9f9; border: 1px solid #ccc;">\n'
    
    # Simple text-based dependency display
    html = '<div style="font-family: monospace; font-size: 12px; padding: 10px; background: #f9f9f9; border-radius: 3px;">\n'
    for head, rel, dep in deps:
        html += f'<div style="margin: 5px 0;"><strong>{head}</strong> <span style="color: #1976D2;">--[{rel}]--&gt;</span> <strong>{dep}</strong></div>\n'
    html += '</div>\n'
    
    return html

def save_trees_to_html(output_file="parsing_results.html"):
    """Generate HTML with constituency and dependency trees"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Constituency and Dependency Parse Trees</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 1400px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #1976D2;
                margin-bottom: 30px;
            }
            .sentence-block {
                margin-bottom: 40px;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 5px;
                background-color: #fafafa;
            }
            .sentence-type {
                display: inline-block;
                background: #2196F3;
                color: white;
                padding: 5px 10px;
                border-radius: 3px;
                font-size: 12px;
                margin-bottom: 10px;
            }
            .sentence-text {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                margin: 10px 0 20px 0;
                padding: 15px;
                background-color: #e3f2fd;
                border-left: 4px solid #2196F3;
                border-radius: 3px;
            }
            .trees-container {
                display: flex;
                gap: 20px;
                margin-top: 20px;
            }
            @media (max-width: 1024px) {
                .trees-container {
                    flex-direction: column;
                }
            }
            .tree-section {
                flex: 1;
                border: 1px solid #ccc;
                padding: 15px;
                border-radius: 4px;
                background-color: white;
            }
            .tree-title {
                font-weight: bold;
                color: #1976D2;
                margin-bottom: 10px;
                border-bottom: 2px solid #1976D2;
                padding-bottom: 5px;
                font-size: 14px;
            }
            .tree-content {
                font-family: monospace;
                font-size: 12px;
                white-space: pre-wrap;
                word-wrap: break-word;
                background-color: #f9f9f9;
                padding: 10px;
                border-radius: 3px;
                overflow-x: auto;
                line-height: 1.5;
            }
            .note {
                background-color: #fff3cd;
                border: 1px solid #ffc107;
                padding: 10px;
                border-radius: 3px;
                margin-top: 15px;
                font-size: 13px;
                color: #856404;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Constituency and Dependency Parse Trees Analysis</h1>
            <div class="note">
                <strong>Note:</strong> This demonstration shows parse trees for four types of sentences:
                <strong>1)</strong> Declarative (statement), 
                <strong>2)</strong> Interrogative (question), 
                <strong>3)</strong> Imperative (command), 
                <strong>4)</strong> Complex (compound sentence)
            </div>
    """
    
    sentence_types = ["Declarative", "Interrogative", "Imperative", "Complex"]
    
    for idx, sentence in enumerate(sentences):
        html_content += f"""
            <div class="sentence-block">
                <div class="sentence-type">{sentence_types[idx]} Sentence</div>
                <div class="sentence-text">Sentence {idx + 1}: {sentence}</div>
                <div class="trees-container">
                    <div class="tree-section">
                        <div class="tree-title">Constituency Tree (Phrase Structure)</div>
                        <div class="tree-content">{parse_trees[idx]}</div>
                    </div>
                    <div class="tree-section">
                        <div class="tree-title">Dependency Relations</div>
                        {generate_dependency_html(dependencies[idx], idx)}
                    </div>
                </div>
            </div>
        """
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML file saved: {output_file}")

# Main program
if __name__ == "__main__":
    print("\n" + "="*70)
    print("Constituency and Dependency Tree Analysis")
    print("="*70 + "\n")
    
    print("Sample text with four sentence types:")
    for idx, sent in enumerate(sentences, 1):
        print(f"{idx}. {sent}")
    
    print("\n" + "="*70)
    print("Generating HTML visualization...")
    print("="*70 + "\n")
    
    save_trees_to_html("parsing_results.html")
    
    print("✓ Analysis complete!")
    print("✓ Open 'parsing_results.html' in your web browser to view the results.")
    print("\nFile location: c:\\PROJECT W6\\parsing_results.html")
