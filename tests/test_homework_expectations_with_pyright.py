import subprocess
import re
from pathlib import Path
import homework_02

ERROR_PATTERN = "# expect-type-error"


def calculate_expected_error_count(case: Path):
    return len([1 for line in case.read_text().splitlines() if ERROR_PATTERN in line])


def test_homework_expectations_with_pyright():
    p: Path

    pattern = re.compile(
        r"^\s+(?P<path>.*?):(?P<line>\d+):(?P<position>\d+)\s+-\s+error:.+$"
    )

    for p in Path(homework_02.__file__).parent.glob("**/*.py"):
        expected_errors_count = calculate_expected_error_count(p)
        error_lines = set()
        # Запускаем pyright для анализа кода
        process = subprocess.run(
            ["pyright", p.absolute()], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Отлавливаем вывод и ошибки
        output = process.stdout.decode("utf-8")

        # Проверяем на наличие комментария # expect-type-error
        for line in output.split("\n"):
            matched = pattern.match(line)
            if matched:
                error_lines.add(int(matched["line"]))

        assert expected_errors_count == len(
            error_lines
        ), f"Expected {expected_errors_count} errors, but found {len(error_lines)}"

        print("Assertion passed", p.absolute())

    print("Analysis complete!")
