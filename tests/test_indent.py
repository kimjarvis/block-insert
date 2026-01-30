# test_example.py
import logging
import os

from block_insert import block_insert

logger = logging.getLogger(__name__)


def test_indent_1():
    # Call the function that generates the output file
    print("hello world")
    block_insert(
        source_path="tests/sources/indent_1.md",
        insert_path="tests/snippets",
        output_path="tests/outputs"
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/indent_1.md"
    expected_file = "tests/expected/indent_1.md"

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

def test_indent_2():
    # Call the function that generates the output file
    print("hello world")
    block_insert(
        source_path="tests/sources/indent_2.md",
        insert_path="tests/snippets",
        output_path="tests/outputs"
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/indent_2.md"
    expected_file = "tests/expected/indent_2.md"

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


def test_indent_3():
    # Call the function that generates the output file
    print("hello world")
    block_insert(
        source_path="tests/sources/indent_3.md",
        insert_path="tests/snippets",
        output_path="tests/outputs"
    )

    # Define paths to the generated and expected files
    output_file = "tests/outputs/indent_3.md"
    expected_file = "tests/expected/indent_3.md"

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
