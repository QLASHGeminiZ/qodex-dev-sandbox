# Qodex development sandbox

A small, synthetic integration fixture for Qodex development on dev-a.

The initial implementation trims leading and trailing whitespace from display names
and preserves Unicode. The first Qodex task will extend it to collapse repeated
internal whitespace, with regression tests.

Run the checks with `python3 -m unittest discover -s tests -v`.

Pull requests are proposed from the QLASH-Qodex fork and reviewed independently.
The GitHub-hosted workflow has read-only repository permissions and performs no deployment.
