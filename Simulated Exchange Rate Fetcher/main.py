from functools import lru_cache
import time

# =========================
# Simulated Exchange Rate Fetcher
# =========================

# lru_cache stores results of function calls so the same input doesn’t repeat the computation.
# maxsize=100 means the most recent 100 unique calls will be remembered.
@lru_cache(maxsize=100)
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Simulates an expensive operation to fetch exchange rates.
    In real applications, this might be an API call or a database query.
    """
    print(f"Fetching exchange rate from {from_currency} to {to_currency}...")
    time.sleep(2)  # Simulate delay (e.g. API latency)
    
    # Simulated exchange rates — in real life, this would be dynamic
    fake_rates = {
        ('USD', 'EUR'): 0.93,
        ('EUR', 'USD'): 1.07,
        ('USD', 'JPY'): 155.45,
        ('JPY', 'USD'): 0.0064,
    }

    return fake_rates.get((from_currency, to_currency), 1.0)  # Default to 1.0 if not found


# =========================
# Currency Converter Function
# =========================
def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Converts the amount from one currency to another using cached exchange rates.
    """
    rate = get_exchange_rate(from_currency, to_currency)
    return round(amount * rate, 2)


# =========================
# Demo / Usage
# =========================

# First call will simulate delay
print("1st call: ", convert_currency(100, 'USD', 'EUR'))

# Second call is instant due to cache
print("2nd call (cached): ", convert_currency(100, 'USD', 'EUR'))

# New call: will simulate delay again
print("3rd call: ", convert_currency(100, 'EUR', 'USD'))

# 4th call: also cached
print("4th call (cached): ", convert_currency(100, 'EUR', 'USD'))


# =========================
# Drawbacks & Limitations
# =========================

"""
1. ⚠️ Arguments must be hashable:
   - Strings, ints, tuples = OK
   - Lists, dicts, sets = ❌ NOT allowed
   - You can convert these into tuples or frozensets if needed

2. ⚠️ Limited Cache Size:
   - Once more than `maxsize` entries are cached, the oldest ones are discarded (LRU = Least Recently Used)
   - This could be a problem in memory-constrained apps or where many unique inputs are expected

3. ⚠️ No auto-expiration:
   - Cached values don’t expire unless you restart the program
   - Not good for fast-changing data (e.g. real-time stock prices or currency rates)

4. ⚠️ Thread safety:
   - Safe for single-threaded programs, but you should be cautious using it in multi-threaded environments

5. ✅ Best Use Cases:
   - Expensive pure functions with repeat inputs (e.g. Fibonacci, conversions, configs)
"""