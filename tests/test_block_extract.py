# test_example.py
import logging
import os

from block_extract import block_extract

logger = logging.getLogger(__name__)


def test_basic_extract():
    # Call the function that generates the output file
    print("hello world")
    block_extract(
        source_path="tests/sources/basic_extract.md",
        extract_path="tests/outputs",
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/basic_extract.md"
    expected_file = "tests/expected/basic_extract.md"

    # Assert that both files exist
    assert os.path.exists(output_file), f"Output file not found: {output_file}"
    assert os.path.exists(expected_file), f"Expected file not found: {expected_file}"

    # Read the contents of both files
    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()
    with open(expected_file, "r", encoding="utf-8") as f:
        expected_content = f.read()

    # Assert that the contents are identical
    assert output_content == expected_content, "Generated file content does not match expected content."


def test_extract_last_line():
    # Call the function that generates the output file
    print("hello world")
    block_extract(
        source_path="tests/sources/extract_last_line.md",
        extract_path="tests/outputs",
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/extract_last_line.md"
    expected_file = "tests/expected/extract_last_line.md"

    # Assert that both files exist
    assert os.path.exists(output_file), f"Output file not found: {output_file}"
    assert os.path.exists(expected_file), f"Expected file not found: {expected_file}"

    # Read the contents of both files
    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()
    with open(expected_file, "r", encoding="utf-8") as f:
        expected_content = f.read()

    # Assert that the contents are identical
    assert output_content == expected_content, "Generated file content does not match expected content."


def test_extract_indent_1():
    # Call the function that generates the output file
    print("hello world")
    block_extract(
        source_path="tests/sources/extract_indent_1.md",
        extract_path="tests/outputs",
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/extract_indent_1.md"
    expected_file = "tests/expected/extract_indent_1.md"

    # Assert that both files exist
    assert os.path.exists(output_file), f"Output file not found: {output_file}"
    assert os.path.exists(expected_file), f"Expected file not found: {expected_file}"

    # Read the contents of both files
    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()
    with open(expected_file, "r", encoding="utf-8") as f:
        expected_content = f.read()

    # Assert that the contents are identical
    assert output_content == expected_content, "Generated file content does not match expected content."

def test_extract_indent_2():
    # Call the function that generates the output file
    print("hello world")
    block_extract(
        source_path="tests/sources/extract_indent_2.md",
        extract_path="tests/outputs",
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/extract_indent_2.md"
    expected_file = "tests/expected/extract_indent_2.md"

    # Assert that both files exist
    assert os.path.exists(output_file), f"Output file not found: {output_file}"
    assert os.path.exists(expected_file), f"Expected file not found: {expected_file}"

    # Read the contents of both files
    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()
    with open(expected_file, "r", encoding="utf-8") as f:
        expected_content = f.read()

    # Assert that the contents are identical
    assert output_content == expected_content, "Generated file content does not match expected content."
