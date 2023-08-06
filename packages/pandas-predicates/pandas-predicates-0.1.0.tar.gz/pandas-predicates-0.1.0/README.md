# pandas-predicates

A library for creating predicating expressions to filter pandas dataframes.

## Status

This is a work in progress. Be mindful that:

- there's no released version yet
- the API is not stable
- the documentation is sparse

## Why

I often found myself creating really unwieldy code for creating filtering masks for pandas dataframes. Inspired by libraries like [polars](https://www.pola.rs/) or [pyspark](), which use static expressions to build queries, I decided to create a simple API to create expressions that can be used to filter a dataframe in pandas.

## Goals

For now the goal is to simply provide a simple API to create predicates to filter a pandas dataframe. Initially I don't intend to support generic expressions, but that may change in the future.

Stated goals:

- follow as much as possible the pandas API
- cover all methods that can be used to create a boolean mask
- implement useful combinators to combine predicates

## Progress tracking

We are implementing the methods in this order:

- [ ] Documentation
  - [ ] API reference
  - [ ] Examples
- [ ] Finish packaging and CI
  - [ ] basic packaging (pypi, readthedocs, etc.)
  - [ ] CI
  - [ ] release installable 0.1.0 version
- [ ] All series methods that produce a boolean mask directly (like `isdigit`, `str.contains`, etc.).
  - [x] base API: `isna`, `isnull`, `isin`
  - [ ] str base API: `isalpha`, `isalnum`, `isdigit`, `isspace`, `islower`, `isupper`, `istitle`, `isnumeric`, `isdecimal`
  - [x] str matching API: `contains`, `match`, `fullmatch`, `startswith`
  - [ ] dt API:
  - [ ] cat API:
  - [ ] anything missing?
- [ ] Methods that can be used for simple comparisons (like doing `my_df.my_float_column > 20`).
  - [x] base API: `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__lt__`, `__le__`, `between`
  - [ ] needs reserach to make a complete list
  - [ ] Any other method that would be useful
  - [ ] needs reserach to make a complete list
- [ ] Boolean combinators:
  - [x] trivial: `never`, `always`
  - [x] basic: `__invert__`, `__and__`, `__or__`, , `__xor__`
  - [ ] reverse: `__rand__`, `__ror__`, , `__rxor__`
  - [x] basic aggregations: `all_of`, `any_of`, `none_of`
  - [ ] count based aggregations: `at_most_one_of`, `at_least_k_of`, `at_most_k_of`, `exactly_k_of`
  - [ ] custom aggregators? `aggregate_with(agg_func, *expressions, start=True)`
  - [ ] anything missing?
- Expressions API
  - [ ] Formalize the expression tree
  - [ ] Implement a pretty printer
  - [ ] Improved type checking?
  - [ ] needs research
- [ ] Anything else?

## Syntax

For now the expression language have the following syntax:

```python
    import pandas as pd
    from pandas_predicates import col

    df = pd.DataFrame([
        {"a": 1, "b": "blabla", "c": 3},
        {"a": 4, "b": "bleble", "c": 6},
        {"a": 7, "b": "marco", "c": 9},
    ])

    # simple predicates

    # select rows where column a is equal to 1
    a_is_1 = col("a") == 1
    assert a_is_1.filter(df) == df[df.a == 1]

    # select rows where column a is not equal to 1
    a_is_not_1 = col("a") != 1
    assert a_is_not_1.filter(df) == df[df.a != 1]

    # select rows where column a is greater than 4 and b contains the regex "(bl.)+"
    a_gt_1_and_b_matches = (col("a") > 4) & col("b").str.contains(r"(bl.)+")
    assert a_gt_1_and_b_matches.filter(df) == df[(df.a > 4) & df.b.str.contains(r"(bl.)+")]

    # select rows where column a is greater than 4 or b contains the regex "(bl.)+"
    a_gt_1_or_b_matches = (col("a") > 4) | col("b").str.contains(r"(bl.)+")
    assert a_gt_1_or_b_matches.filter(df) == df[(df.a > 4) | df.b.str.contains(r"(bl.)+")]



```
