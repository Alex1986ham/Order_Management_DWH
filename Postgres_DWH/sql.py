select_order = ("""
select
    order_id,
    recipient_name,
    ship_address_1,
    ship_address_2,
    ship_address_3,
    ship_postal_code,
    ship_city

 from public.ama_order_export25
""")
