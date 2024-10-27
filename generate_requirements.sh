#!/bin/bash

# Input and output file paths
TOML_FILE="pixi.toml"
REQUIREMENTS_FILE="requirements.txt"

# Clear or create requirements.txt
> "$REQUIREMENTS_FILE"

# Use grep and sed to extract dependencies
grep -A 1000 "\[dependencies\]" "$TOML_FILE" | grep -v "\[" | sed '/^$/d' | while IFS='=' read -r package version; do
    # Remove whitespace and quotes
    package=$(echo "$package" | xargs)
    version=$(echo "$version" | sed 's/"//g' | xargs)
    
    # Append to requirements.txt
    echo "$package$version" >> "$REQUIREMENTS_FILE"
done

echo "Requirements file generated: $REQUIREMENTS_FILE"