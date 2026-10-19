#!/usr/bin/env bash
set -eu
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INFO_FILE="$PROJECT_DIR/Kanatbek_Nurdos_info.txt"

echo "=============================="
echo "Student Information"
echo "=============================="
if [ -f "$INFO_FILE" ]; then
    grep -E '^(Name|Surname|Group|Student ID):' "$INFO_FILE"
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi

echo ""
echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -a)"
echo ""
echo "Disk Usage:"
df -h /
echo ""
echo "Memory Usage:"
free -h
