def validate_order_input(symbol, side, order_type, quantity, price=None):
    """
    Validates trading order input parameters.
    
    Returns:
        dict: Cleaned and normalized values.
        
    Raises:
        ValueError: If any parameter fails validation.
    """
    
    # --- Validate Symbol ---
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("Symbol cannot be empty. Example: BTCUSDT")
    
    cleaned_symbol = symbol.strip()
    if not cleaned_symbol.isupper():
        raise ValueError(f"Symbol must be uppercase (e.g., BTCUSDT), got: '{symbol}'")

    # --- Validate Side ---
    if not isinstance(side, str):
        raise ValueError("Side must be a string.")
        
    cleaned_side = side.strip().upper()
    if cleaned_side not in ("BUY", "SELL"):
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.")

    # --- Validate Order Type ---
    if not isinstance(order_type, str):
        raise ValueError("Order type must be a string.")
        
    cleaned_order_type = order_type.strip().upper()
    if cleaned_order_type not in ("MARKET", "LIMIT"):
        raise ValueError(f"Invalid order type '{order_type}'. Must be MARKET or LIMIT.")

    # --- Validate Quantity ---
    try:
        cleaned_quantity = float(quantity)
    except (TypeError, ValueError):
        raise ValueError(f"Quantity must be a positive number. Got: '{quantity}'")
        
    if cleaned_quantity <= 0:
        raise ValueError(f"Quantity must be a positive number. Got: '{quantity}'")

    # --- Validate Price ---
    cleaned_price = None
    if cleaned_order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
            
        try:
            cleaned_price = float(price)
        except (TypeError, ValueError):
            raise ValueError(f"Price must be a positive number. Got: '{price}'")
            
        if cleaned_price <= 0:
            raise ValueError(f"Price must be a positive number. Got: '{price}'")
            
    # If order_type is MARKET, price is ignored (remains None)
            
    return {
        "symbol": cleaned_symbol,
        "side": cleaned_side,
        "order_type": cleaned_order_type,
        "quantity": cleaned_quantity,
        "price": cleaned_price
    }
