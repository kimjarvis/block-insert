# Lineblocks

Lineblocks is a documentation synchronization tool that maintains consistency between code examples and their corresponding documentation.

Primary Use Case: Keeping Code Documentation Up to Date

The tool addresses the common problem where documentation becomes outdated as code evolves. Developers often copy-paste code examples into documentation, but when the source code changes, these examples quickly become inaccurate. This program solves this by:

- Single Source of Truth: Code examples are stored in actual source files, not duplicated in documentation

- Automatic Synchronization: Running this program updates all documentation with the latest code examples

- Consistent Formatting: Maintains proper indentation and structure when inserting code blocks

- Error Detection: Identifies orphaned markers and missing files to prevent broken documentation

# Installation 

```bash
pipx install lineblocks
```
# Usage

Add markers to source code

```python
def test_lineblocks():
    # block extract test.txt
    import lineblocks
    lineblocks("extract",source=README.md,prefix=".")
    lineblocks("insert",source=".",prefix=".")
    # end extract
```

In your documentation, add markers to indicate where code examples should be inserted.

```python
<!-- block insert test.txt -->
```

Run the extraction process to create the file test.txt

```bash
linebocks extract --source=README.md --prefix=.
```
