# Island Perimeter

## Description

Calculates the perimeter of an island in a 2D grid where:
- 0 represents water
- 1 represents land

## Function

```python
def island_perimeter(grid: List[List[int]]) -> int:
```

## Usage

```python
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
```

## Constraints

- Grid is rectangular, max 100x100
- One island (or none)
- No lakes
- Cells connected horizontally/vertically

## Files

- `0-island_perimeter.py`: Implementation
- `0-main.py`: Test file

