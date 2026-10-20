import pandas as pd
from stock_filter import StockFilter, parse_ai_output


def apply_filter(f: StockFilter, df: pd.DataFrame) -> pd.DataFrame:
    result = df
    if f.metal is not None:
          result = result[result["metal"] == f.metal] 
    if f.purity is not None:
          result = result[result["purity"] == f.purity] 
    if f.category is not None:
          result = result[result["category"] == f.category] 
    if f.branch is not None:
          result = result[result["branch"] == f.branch] 
    if f.weight_min is not None:
          result = result[result["weight_gm"] >= f.weight_min] 
    if f.weight_max is not None:
          result = result[result["weight_gm"] <= f.weight_max] 
       
    # metal      → done above, copy it
    # purity     → done above, copy it
    # category   → same pattern
    # branch     → same pattern
    # weight_min → keep rows where weight_gm >= f.weight_min
    # weight_max → keep rows where weight_gm <= f.weight_max

    return result


def smart_search(ai_text: str, df: pd.DataFrame):
      search_filter= parse_ai_output(ai_text)
      if search_filter is None:
        print("Could not understand the search")
        return None
      return apply_filter(search_filter, df)


if __name__ == "__main__":
    df = pd.read_csv("fake_stock.csv")

    f1 = StockFilter(module="stock", metal="Gold", purity="22K", branch="Chennai")
    print(len(apply_filter(f1, df)), "items")
    print(apply_filter(f1, df).head())

    f2 = StockFilter(module="stock", category="Ring", weight_min=10, weight_max=20)
    r = apply_filter(f2, df)
    print(r["weight_gm"].describe())
    print(len(apply_filter(f2, df)), "items")

    f3 = StockFilter(module="stock")
    print(len(apply_filter(f3, df)), "items")    # no filters → should be 500

    print(smart_search('{"module": "stock", "metal": "Silver", "branch": "Madurai"}', df).head())
    print(smart_search('{"module": "stock", "category": "Necklace", "weight_min": 40}', df).head())
    print(smart_search('{"module": "stock", "metal": "Plastic"}', df))
    print(smart_search('not json at all', df))